import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.gtmd_convolution import (
    OffForwardSpinQuadrature,
    TransferMapping,
    build_off_forward_component_quadratures,
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    convolve_gluon_gtmd_components,
    convolve_gluon_gtmd_wave_components,
    convolve_local_current,
    convolve_gtmd_point,
    project_deuteron_gluon_target_channel,
    project_deuteron_gluon_tt,
    project_deuteron_gluon_u_ll,
    spectator_on_shell_virtuality,
    spin_half_collinear_gluon_correlator,
)
from deuteron_wigner.gluon_correlator import (
    compose_polarized_gluon_correlator,
    compose_ll_gluon_correlator,
    compose_unpolarized_gluon_correlator,
    GluonTargetPolarization,
)
from deuteron_wigner.registry import TargetChannel
from deuteron_wigner.spin import reconstruct_from_basis


def synthetic_quadrature(delta_x=0.0, delta_y=0.0):
    y = np.array([0.55, 0.75])
    p_x = np.array([0.1, -0.2])
    p_y = np.array([-0.05, 0.15])
    weights = np.array([0.4, 0.6])
    spectral = np.zeros((2, 3, 3, 2, 2), dtype=np.complex128)
    target = (
        np.diag([0.8, 1.1, 0.9]),
        np.diag([1.2, 0.7, 1.0]),
    )
    for node in range(2):
        spectral[node] = target[node][..., None, None] * np.eye(2) / 2.0
    return OffForwardSpinQuadrature(
        y=y,
        p_x=p_x,
        p_y=p_y,
        weights=weights,
        delta_x=delta_x,
        delta_y=delta_y,
        spectral=spectral,
    )


def gaussian_gtmd(flavor, x, k_x, k_y, delta_x, delta_y, scale):
    scalar = (
        (1.0 + 0.1 * flavor)
        * x
        * (1.0 - x)
        * np.exp(-(k_x**2 + k_y**2) / 0.4)
        / (np.pi * 0.4)
        * np.exp(-0.2 * (delta_x**2 + delta_y**2))
    )
    return scalar * np.eye(2)


class GTMDConvolutionTests(unittest.TestCase):
    def test_spectator_virtuality_has_bound_state_and_free_limits(self):
        mass = 0.93891897
        deuteron_mass = 1.87561294257
        bound = spectator_on_shell_virtuality(
            0.0, nucleon_mass=mass, deuteron_mass=deuteron_mass
        )
        self.assertLess(bound, 0.0)
        self.assertAlmostEqual(
            spectator_on_shell_virtuality(
                0.0, nucleon_mass=mass, deuteron_mass=2.0 * mass
            ),
            0.0,
            places=14,
        )
        self.assertLess(
            spectator_on_shell_virtuality(
                0.1, nucleon_mass=mass, deuteron_mass=deuteron_mass
            ),
            bound,
        )

    def test_spin_half_collinear_gluon_correlator_has_no_linear_part(self):
        correlator = spin_half_collinear_gluon_correlator(2.4, -0.7)
        self.assertEqual(correlator.shape, (2, 2, 2, 2))
        for nucleon_out in range(2):
            for nucleon_in in range(2):
                _, _, linear = transverse_matrix_parts(
                    correlator[nucleon_out, nucleon_in]
                )
                np.testing.assert_allclose(linear, 0.0, atol=1.0e-15)

    def test_gluon_convolution_retains_both_index_pairs(self):
        quadrature = synthetic_quadrature()

        def gluon_input(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(x, 0.25 * x)

        actual = convolve_gluon_gtmd_point(
            x=0.2,
            k_x=0.1,
            k_y=-0.05,
            scale=2.0,
            proton_gtmd=gluon_input,
            neutron_gtmd=gluon_input,
            quadrature=quadrature,
        )
        self.assertEqual(actual.shape, (3, 3, 2, 2))
        expected = np.zeros_like(actual)
        for y, weight, spectral in zip(
            quadrature.y, quadrature.weights, quadrature.spectral
        ):
            nucleon = 2.0 * spin_half_collinear_gluon_correlator(
                0.2 / y, 0.25 * 0.2 / y
            )
            expected += (
                weight
                * np.einsum("IHca,acij->IHij", spectral, nucleon)
                / y
            )
        np.testing.assert_allclose(actual, expected, atol=1.0e-14)

    def test_gluon_convolution_retains_proton_neutron_provenance(self):
        quadrature = synthetic_quadrature()

        def proton(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(2.0 * x, 0.1 * x)

        def neutron(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(0.7 * x, -0.05 * x)

        components = convolve_gluon_gtmd_components(
            x=0.2,
            k_x=0.1,
            k_y=-0.05,
            scale=2.0,
            proton_gtmd=proton,
            neutron_gtmd=neutron,
            quadrature=quadrature,
        )
        total = convolve_gluon_gtmd_point(
            x=0.2,
            k_x=0.1,
            k_y=-0.05,
            scale=2.0,
            proton_gtmd=proton,
            neutron_gtmd=neutron,
            quadrature=quadrature,
        )
        self.assertEqual(set(components), {"proton", "neutron"})
        self.assertFalse(
            np.allclose(components["proton"], components["neutron"])
        )
        np.testing.assert_allclose(
            total, components["proton"] + components["neutron"], atol=1e-14
        )

    def test_gluon_wave_components_reconstruct_full_parent(self):
        full = synthetic_quadrature()
        fractions = {"SS": 0.7, "SD": 0.1, "DS": 0.08, "DD": 0.12}
        quadratures = {
            label: OffForwardSpinQuadrature(
                y=full.y, p_x=full.p_x, p_y=full.p_y,
                weights=full.weights, delta_x=0.0, delta_y=0.0,
                spectral=fraction * full.spectral,
            )
            for label, fraction in fractions.items()
        }

        def proton(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(2.0 * x, 0.1 * x)

        def neutron(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(0.7 * x, -0.05 * x)

        arguments = dict(
            x=0.2, k_x=0.1, k_y=-0.05, scale=2.0,
            proton_gtmd=proton, neutron_gtmd=neutron,
        )
        resolved = convolve_gluon_gtmd_wave_components(
            **arguments, quadratures=quadratures
        )
        direct = convolve_gluon_gtmd_components(
            **arguments, quadrature=full
        )
        for nucleon in ("proton", "neutron"):
            np.testing.assert_allclose(
                sum(value[nucleon] for value in resolved.values()),
                direct[nucleon], atol=1e-14,
            )

    def test_one_body_collinear_h1tt_gluon_is_structurally_zero(self):
        quadrature = synthetic_quadrature()
        # Supply a target double-helicity-flip spectral component.  This
        # deliberately gives a nonzero TT target projection, while the
        # spin-1/2 collinear nucleon correlator still cannot create a
        # symmetric-traceless gluon-index matrix.
        spectral = quadrature.spectral.copy()
        spectral[:, 0, 2] = np.eye(2)[None, :, :] * 0.3
        spectral[:, 2, 0] = np.eye(2)[None, :, :] * 0.3
        quadrature = OffForwardSpinQuadrature(
            y=quadrature.y,
            p_x=quadrature.p_x,
            p_y=quadrature.p_y,
            weights=quadrature.weights,
            delta_x=0.0,
            delta_y=0.0,
            spectral=spectral,
        )

        def collinear_input(x, k_x, k_y, delta_x, delta_y, scale):
            return spin_half_collinear_gluon_correlator(1.0 + x, 0.2 * x)

        deuteron = convolve_gluon_gtmd_point(
            x=0.2,
            k_x=0.0,
            k_y=0.0,
            scale=2.0,
            proton_gtmd=collinear_input,
            neutron_gtmd=collinear_input,
            quadrature=quadrature,
        )
        tt_x = project_deuteron_gluon_target_channel(deuteron, "TT_x")
        self.assertGreater(abs(np.trace(tt_x)), 0.0)
        _, _, linear = transverse_matrix_parts(tt_x)
        np.testing.assert_allclose(linear, 0.0, atol=1.0e-14)

    def test_u_ll_named_projection_includes_convention_adapter(self):
        momentum = (0.31, -0.18)
        mass = 1.8756
        phi_u = compose_unpolarized_gluon_correlator(
            momentum, mass, f1=2.0, h1perp=-0.4
        )
        phi_ll = compose_ll_gluon_correlator(
            momentum, mass, 1.0, f1LL=0.3, h1LLperp=0.7
        )
        target = reconstruct_from_basis(
            {"U": np.moveaxis(phi_u, (0, 1), (0, 1)), "LL": -np.moveaxis(phi_ll, (0, 1), (0, 1))}
        )
        # reconstruct_from_basis places target indices last; restore IHij.
        correlator = np.moveaxis(target.values, (-2, -1), (0, 1))
        unpolarized, ll = project_deuteron_gluon_u_ll(
            correlator, momentum, mass
        )
        self.assertAlmostEqual(unpolarized.trace, 2.0)
        self.assertAlmostEqual(unpolarized.linear, -0.4)
        self.assertAlmostEqual(ll.trace, 0.3)
        self.assertAlmostEqual(ll.linear, 0.7)

    def test_tt_named_projection_recovers_all_identifiable_functions(self):
        momentum = (0.31, -0.18)
        mass = 1.8756
        physical = {
            "f1TT": 0.8,
            "g1TT": -0.3,
            "h1TT": 0.45,
            "h1TTperp": -0.2,
            "h1TTperpperp": 0.12,
        }
        phi_x = compose_polarized_gluon_correlator(
            TargetChannel.TT,
            momentum,
            mass,
            GluonTargetPolarization(
                spin_tt=((1.0, 0.0), (0.0, -1.0))
            ),
            physical,
        )
        phi_y = compose_polarized_gluon_correlator(
            TargetChannel.TT,
            momentum,
            mass,
            GluonTargetPolarization(
                spin_tt=((0.0, 1.0), (1.0, 0.0))
            ),
            physical,
        )
        target = reconstruct_from_basis({"TT_x": phi_x, "TT_y": phi_y})
        correlator = np.moveaxis(target.values, (-2, -1), (0, 1))
        projected = project_deuteron_gluon_tt(correlator, momentum, mass)
        expected = {
            "f1TT_minus_h1TTperp": 1.0,
            "g1TT": -0.3,
            "h1TT": 0.45,
            "h1TTperpperp": 0.12,
        }
        for name, value in expected.items():
            self.assertAlmostEqual(projected[name], value)

    def test_component_quadratures_reconstruct_full_kernel(self):
        radial = lambda k: (np.exp(-k**2), 0.1 * k**2 * np.exp(-k**2))
        arguments = dict(
            radial=radial,
            nucleon_mass=0.94,
            k_max=2.0,
            delta_x=0.2,
            delta_y=-0.1,
            n_k=3,
            n_cos_theta=3,
            n_phi=4,
        )
        full = build_off_forward_spin_quadrature(**arguments)
        components = build_off_forward_component_quadratures(**arguments)
        np.testing.assert_allclose(
            sum(value.spectral for value in components.values()),
            full.spectral,
            atol=2e-15,
        )

    def test_off_forward_radial_subinterval_is_supported(self):
        radial = lambda k: (np.exp(-k**2), 0.0)
        interval = build_off_forward_spin_quadrature(
            radial=radial,
            nucleon_mass=0.94,
            k_min=0.5,
            k_max=1.0,
            delta_x=0.0,
            delta_y=0.0,
            n_k=3,
            n_cos_theta=2,
            n_phi=2,
        )
        self.assertEqual(len(interval.y), 12)
        with self.assertRaises(ValueError):
            build_off_forward_spin_quadrature(
                radial=radial,
                nucleon_mass=0.94,
                k_min=1.0,
                k_max=1.0,
                delta_x=0.0,
                delta_y=0.0,
            )

    def test_transfer_mapping_is_explicit(self):
        self.assertEqual(
            TransferMapping.IDENTITY.nucleon_transfer(0.4, 0.2, -0.1),
            (0.2, -0.1),
        )
        np.testing.assert_allclose(
            TransferMapping.ACTIVE_FRACTION.nucleon_transfer(0.4, 0.2, -0.1),
            (0.08, -0.04),
            atol=0.0,
        )

    def test_forward_result_is_hermitian(self):
        result = convolve_gtmd_point(
            x=0.2,
            k_x=0.1,
            k_y=-0.05,
            scale=2.0,
            flavor=2,
            proton_gtmd=gaussian_gtmd,
            neutron_gtmd=gaussian_gtmd,
            quadrature=synthetic_quadrature(),
        )
        self.assertTrue(result.is_hermitian())

    def test_k_integral_reproduces_shift_independent_gpd_convolution(self):
        quadrature = synthetic_quadrature()
        axis = np.linspace(-4.0, 4.0, 161)
        values = np.empty((len(axis), len(axis), 3, 3), dtype=np.complex128)
        for i, k_x in enumerate(axis):
            for j, k_y in enumerate(axis):
                values[i, j] = convolve_gtmd_point(
                    x=0.2,
                    k_x=float(k_x),
                    k_y=float(k_y),
                    scale=2.0,
                    flavor=2,
                    proton_gtmd=gaussian_gtmd,
                    neutron_gtmd=gaussian_gtmd,
                    quadrature=quadrature,
                ).values
        integrated = simpson(simpson(values, x=axis, axis=1), x=axis, axis=0)
        expected = np.zeros((3, 3), dtype=np.complex128)
        for y, weight, spectral in zip(
            quadrature.y, quadrature.weights, quadrature.spectral
        ):
            z = 0.2 / y
            collinear = 2.0 * (1.0 + 0.2) * z * (1.0 - z)
            expected += weight * np.einsum(
                "IHca,ac->IH", spectral, collinear * np.eye(2)
            ) / y
        np.testing.assert_allclose(integrated, expected, atol=2e-10)

    def test_delta_hermiticity_relation(self):
        phase_matrix = np.array([[1.0, 0.2j], [-0.2j, 0.7]])

        def off_forward(flavor, x, k_x, k_y, delta_x, delta_y, scale):
            return np.exp(-k_x**2 - k_y**2) * np.exp(0.3j * delta_x) * phase_matrix

        plus = synthetic_quadrature(delta_x=0.2)
        minus_spectral = plus.spectral.conj().transpose(0, 2, 1, 4, 3)
        minus = OffForwardSpinQuadrature(
            y=plus.y,
            p_x=plus.p_x,
            p_y=plus.p_y,
            weights=plus.weights,
            delta_x=-0.2,
            delta_y=0.0,
            spectral=minus_spectral,
        )
        positive = convolve_gtmd_point(
            x=0.2,
            k_x=0.1,
            k_y=0.05,
            scale=2.0,
            flavor=2,
            proton_gtmd=off_forward,
            neutron_gtmd=off_forward,
            quadrature=plus,
        ).values
        negative = convolve_gtmd_point(
            x=0.2,
            k_x=0.1,
            k_y=0.05,
            scale=2.0,
            flavor=2,
            proton_gtmd=off_forward,
            neutron_gtmd=off_forward,
            quadrature=minus,
        ).values
        np.testing.assert_allclose(positive.conj().T, negative, atol=2e-14)

    def test_local_current_constant_reproduces_spectral_moment(self):
        quadrature = synthetic_quadrature(delta_x=0.2)
        identity = lambda delta_x, delta_y, scale: np.eye(2)
        actual = convolve_local_current(
            scale=2.0,
            proton_current=identity,
            neutron_current=identity,
            quadrature=quadrature,
        ).values
        expected = sum(
            weight * np.einsum("IHca,ac->IH", spectral, 2.0 * np.eye(2))
            for weight, spectral in zip(quadrature.weights, quadrature.spectral)
        )
        np.testing.assert_allclose(actual, expected, atol=1e-14)


if __name__ == "__main__":
    unittest.main()
