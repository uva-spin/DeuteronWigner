"""Stage 0 convention, spin, Fourier, and GTMD marginal tests."""

import unittest

import numpy as np

from deuteron_wigner.conventions import (
    GTMD_IMAGING_CONVENTION,
    TMD_EVOLUTION_CONVENTION,
    delta_t_to_f1ll,
    f1ll_to_delta_t,
)
from deuteron_wigner.fourier import gtmd_to_wigner, tmd_to_b_space
from deuteron_wigner.gtmd import GaugeLink, SampledGTMD, Species
from deuteron_wigner.kinematics import (
    BDelta,
    BTMD,
    LightFrontVector,
    MomentumTransfer,
    TransverseVector,
    ZeroSkewnessKinematics,
)
from deuteron_wigner.registry import (
    CollinearLimit,
    MatchingStatus,
    TMDEntry,
    TargetChannel,
    baseline_registry,
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)
from deuteron_wigner.spin import (
    diagonal_from_u_l_delta_t,
    project_matrix,
    reconstruct_from_basis,
    spin_one_basis,
)


class KinematicsTests(unittest.TestCase):
    def test_light_front_metric_and_on_shell_condition(self) -> None:
        vector = LightFrontVector.on_shell_collinear(plus=10.0, mass=2.0)
        self.assertAlmostEqual(vector.mass_squared(), 4.0)
        transverse = LightFrontVector(2.0, 3.0, TransverseVector(1.0, -2.0))
        self.assertAlmostEqual(transverse.mass_squared(), 7.0)

    def test_zero_skewness_symmetric_frame(self) -> None:
        mass = 1.8756
        kinematics = ZeroSkewnessKinematics.symmetric(
            plus=10.0, mass=mass, delta_t=MomentumTransfer(0.3, -0.4)
        )
        self.assertEqual(kinematics.skewness, 0.0)
        self.assertAlmostEqual(kinematics.invariant_t, -0.25)
        self.assertAlmostEqual(kinematics.incoming.plus, kinematics.outgoing.plus)
        self.assertAlmostEqual(kinematics.incoming.transverse.x, -0.15)
        self.assertAlmostEqual(kinematics.outgoing.transverse.y, -0.2)
        self.assertAlmostEqual(kinematics.incoming.mass_squared(), mass**2)
        self.assertAlmostEqual(kinematics.outgoing.mass_squared(), mass**2)

    def test_b_delta_and_b_tmd_are_distinct_types(self) -> None:
        self.assertNotEqual(type(BDelta(1.0, 0.0)), type(BTMD(1.0, 0.0)))


class SpinTests(unittest.TestCase):
    def test_helicity_combinations_invert_exactly(self) -> None:
        matrix = diagonal_from_u_l_delta_t(2.0, 0.3, -0.6)
        self.assertAlmostEqual(float(matrix.unpolarized().real), 2.0)
        self.assertAlmostEqual(float(matrix.longitudinal_vector().real), 0.3)
        self.assertAlmostEqual(float(matrix.tensor_difference().real), -0.6)

    def test_f1ll_adapter_matches_standard_sll_eigenvalues(self) -> None:
        f1ll = 0.24
        helicity_values = np.array([
            1.0 + 0.5 * f1ll,
            1.0 - f1ll,
            1.0 + 0.5 * f1ll,
        ])
        delta_t = helicity_values[1] - 0.5 * (
            helicity_values[0] + helicity_values[2]
        )
        self.assertAlmostEqual(float(delta_t_to_f1ll(delta_t)), f1ll)
        self.assertAlmostEqual(float(f1ll_to_delta_t(f1ll)), delta_t)

    def test_basis_is_orthogonal_and_reconstructs(self) -> None:
        basis = spin_one_basis()
        labels = list(basis)
        gram = np.array(
            [
                [np.trace(basis[a].conj().T @ basis[b]) for b in labels]
                for a in labels
            ]
        )
        np.testing.assert_allclose(gram, np.diag(np.diag(gram)), atol=1e-14)
        coefficients = {label: (index + 1) / 10 for index, label in enumerate(labels)}
        matrix = reconstruct_from_basis(coefficients)
        for label, expected in coefficients.items():
            actual = project_matrix(matrix.values, basis[label])
            self.assertAlmostEqual(float(actual.real), expected)

    def test_density_matrix_positivity(self) -> None:
        positive = diagonal_from_u_l_delta_t(1.0, 0.0, 0.3)
        negative = diagonal_from_u_l_delta_t(1.0, 0.0, 4.0)
        self.assertTrue(positive.is_positive_semidefinite())
        self.assertFalse(negative.is_positive_semidefinite())


class FourierTests(unittest.TestCase):
    def test_declared_signs_and_normalizations(self) -> None:
        self.assertEqual(GTMD_IMAGING_CONVENTION.forward_sign, -1)
        self.assertAlmostEqual(
            GTMD_IMAGING_CONVENTION.forward_normalization, 1.0 / (2.0 * np.pi) ** 2
        )
        self.assertEqual(TMD_EVOLUTION_CONVENTION.forward_sign, 1)
        self.assertEqual(TMD_EVOLUTION_CONVENTION.forward_normalization, 1.0)

    def test_gaussian_transforms(self) -> None:
        axis = np.linspace(-7.0, 7.0, 281)
        x, y = np.meshgrid(axis, axis, indexing="ij")
        gaussian = np.exp(-(x**2 + y**2))
        b_delta = [BDelta(0.0, 0.0), BDelta(0.6, -0.2)]
        wigner = gtmd_to_wigner(axis, axis, gaussian, b_delta)
        b_tmd = [BTMD(0.0, 0.0), BTMD(0.6, -0.2)]
        b_space = tmd_to_b_space(axis, axis, gaussian, b_tmd)
        b2 = 0.6**2 + 0.2**2
        expected_plain = np.pi * np.exp(-b2 / 4.0)
        self.assertAlmostEqual(float(wigner[0].real), 1.0 / (4.0 * np.pi), delta=2e-8)
        self.assertAlmostEqual(float(wigner[1].real), expected_plain / (2 * np.pi) ** 2, delta=2e-8)
        self.assertAlmostEqual(float(b_space[0].real), np.pi, delta=2e-8)
        self.assertAlmostEqual(float(b_space[1].real), expected_plain, delta=2e-8)


class GTMDTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        x_axis = np.linspace(0.1, 0.9, 5)
        k_axis = np.linspace(-3.0, 3.0, 25)
        delta_axis = np.linspace(-2.0, 2.0, 17)
        x, kx, ky, dx, dy = np.meshgrid(
            x_axis, k_axis, k_axis, delta_axis, delta_axis, indexing="ij"
        )
        scalar = (
            x
            * (1.0 - x)
            * np.exp(-0.7 * (kx**2 + ky**2))
            * np.exp(-0.4 * (dx**2 + dy**2))
        )
        helicity = diagonal_from_u_l_delta_t(
            scalar, 0.1 * scalar, -0.2 * scalar
        ).values
        cls.parent = SampledGTMD(
            species=Species.QUARK,
            projection="gamma+",
            gauge_link=GaugeLink("+", "+"),
            x=x_axis,
            k_x=k_axis,
            k_y=k_axis,
            delta_x=delta_axis,
            delta_y=delta_axis,
            values=helicity,
        )

    def test_tmd_and_gpd_pdf_paths_commute(self) -> None:
        via_tmd = self.parent.pdf_from_tmd().values
        via_gpd = self.parent.pdf_from_gpd().values
        np.testing.assert_allclose(via_tmd, via_gpd, atol=1e-13, rtol=1e-13)

    def test_tensor_projection_commutes_with_marginal(self) -> None:
        parent_tensor = diagonal_from_u_l_delta_t(
            np.zeros(self.parent.values.shape[:-2]),
            np.zeros(self.parent.values.shape[:-2]),
            np.ones(self.parent.values.shape[:-2]),
        )
        # Linearity fixture: the stored tensor difference is -0.2 times U.
        pdf = self.parent.pdf_from_tmd()
        np.testing.assert_allclose(
            pdf.tensor_difference(), -0.2 * pdf.unpolarized(), atol=1e-13, rtol=1e-13
        )
        self.assertEqual(parent_tensor.values.shape, self.parent.values.shape)

    def test_wigner_zero_coordinate_normalization(self) -> None:
        point = [BDelta(0.0, 0.0)]
        wigner = self.parent.wigner_at(
            x_index=2, k_x_index=12, k_y_index=12, points=point
        )
        delta_slice = self.parent.values[2, 12, 12]
        from scipy.integrate import simpson

        expected = simpson(
            simpson(delta_slice, x=self.parent.delta_y, axis=1),
            x=self.parent.delta_x,
            axis=0,
        ) / (2.0 * np.pi) ** 2
        np.testing.assert_allclose(wigner.values[0], expected, atol=1e-14, rtol=1e-14)


class RegistryTests(unittest.TestCase):
    def test_baseline_registry_separates_species(self) -> None:
        registry = baseline_registry()
        self.assertEqual(len(registry), 6)
        self.assertEqual(len(registry.select(species=Species.QUARK)), 2)
        self.assertEqual(len(registry.select(species=Species.ANTIQUARK)), 2)
        self.assertEqual(len(registry.select(species=Species.GLUON)), 2)
        tensor_quark = registry.get(Species.QUARK, "deltaT_f1")
        self.assertEqual(tensor_quark.target_channel, TargetChannel.LL)
        self.assertIn("Convention-safe", tensor_quark.notes)

    def test_registry_rejects_rank_collinear_contradiction(self) -> None:
        with self.assertRaises(ValueError):
            TMDEntry(
                name="invalid",
                species=Species.GLUON,
                parent_projection="test",
                target_channel=TargetChannel.TT,
                parton_polarization="linear",
                transverse_rank=2,
                gauge_link_required=True,
                collinear_limit=CollinearLimit.NONZERO,
                matching_status=MatchingStatus.OPEN,
                positivity_block="test",
            )

    def test_complete_gluon_registry_matches_published_table(self) -> None:
        registry = leading_twist_gluon_registry()
        self.assertEqual(len(registry), 19)
        self.assertEqual(
            len(registry.select(target_channel=TargetChannel.LL)), 2
        )
        transversity = registry.get(Species.GLUON, "h1TT")
        self.assertEqual(transversity.transverse_rank, 0)
        self.assertEqual(transversity.collinear_limit, CollinearLimit.NONZERO)
        t_odd = tuple(entry for entry in registry.select() if "T-odd" in entry.notes)
        self.assertEqual(len(t_odd), 6)

    def test_complete_quark_registries_match_published_table(self) -> None:
        for species in (Species.QUARK, Species.ANTIQUARK):
            registry = leading_twist_quark_registry(species)
            self.assertEqual(len(registry), 18)
            self.assertEqual(
                len(registry.select(target_channel=TargetChannel.TT)), 4
            )
            t_odd = tuple(
                entry for entry in registry.select() if "T-odd" in entry.notes
            )
            self.assertEqual(len(t_odd), 9)
            exception = registry.get(species, "h1LT")
            self.assertEqual(exception.transverse_rank, 0)
            self.assertEqual(exception.collinear_limit, CollinearLimit.NONE)
            collinear = tuple(
                entry for entry in registry.select()
                if entry.collinear_limit == CollinearLimit.NONZERO
            )
            self.assertEqual(
                {entry.name for entry in collinear},
                {"f1", "g1", "h1", "f1LL"},
            )

    def test_quark_registry_rejects_gluon_species(self) -> None:
        with self.assertRaises(ValueError):
            leading_twist_quark_registry(Species.GLUON)


if __name__ == "__main__":
    unittest.main()
