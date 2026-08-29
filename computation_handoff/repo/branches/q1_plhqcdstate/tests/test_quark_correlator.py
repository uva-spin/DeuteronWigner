import unittest

import numpy as np

from deuteron_wigner.quark_correlator import (
    T_ODD_QUARK_TMDS,
    compose_spin1_quark_correlator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
    quark_correlator_basis,
    reverse_quark_gauge_link,
)
from deuteron_wigner.uncertainty_validation import (
    minimum_eigenvalues_under_component_replacement,
)
from deuteron_wigner.spin import spin_one_basis
from deuteron_wigner.gluon_correlator import EPSILON_T
from deuteron_wigner.transverse_tensors import symmetric_traceless_2d


class Spin1QuarkCorrelatorTests(unittest.TestCase):
    def test_published_cartesian_scalar_contractions_and_signs(self):
        kx, ky = 0.37, -0.21
        mass = 1.9
        basis = quark_correlator_basis((kx, ky), mass)
        spin = spin_one_basis()
        np.testing.assert_allclose(
            basis["f1Tperp"].vector,
            (ky * spin["T_x"] - kx * spin["T_y"]) / mass,
        )
        np.testing.assert_allclose(
            basis["g1T"].axial,
            (kx * spin["T_x"] + ky * spin["T_y"]) / mass,
        )
        np.testing.assert_allclose(
            basis["f1LT"].vector,
            (kx * spin["LT_x"] + ky * spin["LT_y"]) / mass,
        )
        np.testing.assert_allclose(
            basis["g1LT"].axial,
            (ky * spin["LT_x"] - kx * spin["LT_y"]) / mass,
        )
        np.testing.assert_allclose(basis["f1LL"].vector, -spin["LL"])
        tt_x = (kx**2 - ky**2) / mass**2
        tt_y = 2.0 * kx * ky / mass**2
        np.testing.assert_allclose(
            basis["f1TT"].vector,
            tt_x * spin["TT_x"] + tt_y * spin["TT_y"],
        )
        np.testing.assert_allclose(
            basis["g1TT"].axial,
            -tt_y * spin["TT_x"] + tt_x * spin["TT_y"],
        )

    def test_time_reversal_reverses_exactly_published_t_odd_set(self):
        values = {
            name: float(index + 1)
            for index, name in enumerate(
                quark_correlator_basis((0.31, -0.17), 1.9)
            )
        }
        reversed_values = reverse_quark_gauge_link(values)
        for name, value in values.items():
            expected = -value if name in T_ODD_QUARK_TMDS else value
            self.assertEqual(reversed_values[name], expected)
        self.assertEqual(reverse_quark_gauge_link(reversed_values), values)

    def test_published_chiral_odd_cartesian_signs_and_ranks(self):
        k = np.asarray((0.37, -0.21))
        mass = 1.9
        basis = quark_correlator_basis(k, mass)
        spin = spin_one_basis()
        k2 = symmetric_traceless_2d(k, 2)
        k3 = symmetric_traceless_2d(k, 3)
        epsilon_k = EPSILON_T @ k
        np.testing.assert_allclose(
            basis["h1perp"].transverse,
            np.einsum("i,ab->iab", epsilon_k / mass, spin["U"]),
        )
        np.testing.assert_allclose(
            basis["h1Lperp"].transverse,
            np.einsum("i,ab->iab", k / mass, spin["L"]),
        )
        expected_h1 = np.asarray((spin["T_x"], spin["T_y"]))
        np.testing.assert_allclose(basis["h1"].transverse, expected_h1)
        expected_pretzel = np.zeros_like(expected_h1)
        for target, suffix in enumerate(("x", "y")):
            for operator in range(2):
                expected_pretzel[operator] -= (
                    k2[operator, target] * spin[f"T_{suffix}"] / mass**2
                )
        np.testing.assert_allclose(
            basis["h1Tperp"].transverse, expected_pretzel
        )
        np.testing.assert_allclose(
            basis["h1LLperp"].transverse,
            -np.einsum("i,ab->iab", epsilon_k / mass, spin["LL"]),
        )
        expected_h1lt = np.zeros_like(expected_h1)
        expected_h1lt_perp = np.zeros_like(expected_h1)
        for target, suffix in enumerate(("x", "y")):
            expected_h1lt += np.einsum(
                "i,ab->iab", EPSILON_T[:, target], spin[f"LT_{suffix}"]
            )
            expected_h1lt_perp -= np.einsum(
                "i,ab->iab",
                EPSILON_T @ k2[:, target] / mass**2,
                spin[f"LT_{suffix}"],
            )
        np.testing.assert_allclose(
            basis["h1LT"].transverse, expected_h1lt
        )
        np.testing.assert_allclose(
            basis["h1LTperp"].transverse, expected_h1lt_perp
        )
        tt_matrices = (
            np.asarray(((1.0, 0.0), (0.0, -1.0))),
            np.asarray(((0.0, 1.0), (1.0, 0.0))),
        )
        expected_h1tt = np.zeros_like(expected_h1)
        expected_h1tt_perp = np.zeros_like(expected_h1)
        for target_matrix, suffix in zip(tt_matrices, ("x", "y")):
            expected_h1tt -= np.einsum(
                "i,ab->iab",
                EPSILON_T @ (target_matrix @ k) / mass,
                spin[f"TT_{suffix}"],
            )
            expected_h1tt_perp += np.einsum(
                "i,ab->iab",
                EPSILON_T
                @ np.einsum("irs,rs->i", k3, target_matrix)
                / mass**3,
                spin[f"TT_{suffix}"],
            )
        np.testing.assert_allclose(
            basis["h1TT"].transverse, expected_h1tt
        )
        np.testing.assert_allclose(
            basis["h1TTperp"].transverse, expected_h1tt_perp
        )

    def test_all_18_structures_obey_light_front_parity_reflection(self):
        # Reflection y->-y preserves the LF longitudinal direction. Polar
        # transverse vectors transform with R, axial vectors with det(R) R.
        k = np.asarray((0.31, -0.17))
        reflected = np.asarray((k[0], -k[1]))
        target_parity = np.asarray(
            ((0.0, 0.0, 1.0), (0.0, -1.0, 0.0), (1.0, 0.0, 0.0)),
            dtype=np.complex128,
        )
        axial_transverse = np.diag((-1.0, 1.0))
        original = quark_correlator_basis(k, 1.87)
        image = quark_correlator_basis(reflected, 1.87)
        for name in original:
            vector = (
                target_parity @ image[name].vector @ target_parity.T
            )
            axial = -(
                target_parity @ image[name].axial @ target_parity.T
            )
            transverse_target = np.asarray([
                target_parity @ item @ target_parity.T
                for item in image[name].transverse
            ])
            transverse = np.einsum(
                "ij,jab->iab", axial_transverse, transverse_target
            )
            np.testing.assert_allclose(
                vector, original[name].vector, atol=1e-14,
                err_msg=f"{name} vector parity",
            )
            np.testing.assert_allclose(
                axial, original[name].axial, atol=1e-14,
                err_msg=f"{name} axial parity",
            )
            np.testing.assert_allclose(
                transverse, original[name].transverse, atol=1e-14,
                err_msg=f"{name} transverse parity",
            )
    def test_all_basis_correlators_are_target_hermitian(self):
        basis = quark_correlator_basis((0.31, -0.22), 1.8756)
        self.assertEqual(len(basis), 18)
        self.assertTrue(all(value.is_target_hermitian() for value in basis.values()))

    def test_complete_round_trip(self):
        names = tuple(quark_correlator_basis((0.37, 0.19), 1.8756))
        expected = {name: 0.07 * (index - 7) for index, name in enumerate(names)}
        correlator = compose_spin1_quark_correlator(
            (0.37, 0.19), 1.8756, expected
        )
        projected = project_spin1_quark_correlator(
            correlator, (0.37, 0.19), 1.8756
        )
        for name in names:
            self.assertAlmostEqual(projected[name], expected[name], places=11)

    def test_positive_rank_projector_rejects_origin(self):
        zeros = {name: 0.0 for name in quark_correlator_basis((0.2, 0.1), 1.8756)}
        zeros["f1"] = 1.0
        correlator = compose_spin1_quark_correlator((0.2, 0.1), 1.8756, zeros)
        with self.assertRaises(ValueError):
            project_spin1_quark_correlator(correlator, (0.0, 0.0), 1.8756)

    def test_rank_zero_origin_projector(self):
        values = {name: 0.0 for name in quark_correlator_basis((0.0, 0.0), 1.8756)}
        values.update({"f1": 2.0, "g1": -0.3, "h1": 0.4, "f1LL": 0.02, "h1LT": -0.1})
        correlator = compose_spin1_quark_correlator((0.0, 0.0), 1.8756, values)
        projected = project_spin1_quark_correlator_at_origin(correlator, 1.8756)
        for name, expected in values.items():
            self.assertAlmostEqual(projected[name], expected)

    def test_basis_is_rotationally_covariant_in_norm(self):
        radius = 0.4
        norms = []
        for angle in (0.17, 0.73, 1.29):
            k = radius * np.asarray((np.cos(angle), np.sin(angle)))
            basis = quark_correlator_basis(k, 1.8756)
            norms.append(
                {
                    name: np.linalg.norm(value.vector)
                    + np.linalg.norm(value.axial)
                    + np.linalg.norm(value.transverse)
                    for name, value in basis.items()
                }
            )
        for name in norms[0]:
            np.testing.assert_allclose(
                [item[name] for item in norms],
                norms[0][name],
                rtol=2e-2,
                atol=1e-12,
            )

    def test_complete_joint_spin_density_detects_positivity(self):
        values = {
            name: 0.0
            for name in quark_correlator_basis((0.3, -0.2), 1.8756)
        }
        values["f1"] = 1.0
        physical = compose_spin1_quark_correlator(
            (0.3, -0.2), 1.8756, values
        )
        self.assertGreaterEqual(physical.minimum_positivity_eigenvalue(), 0.0)
        values["g1"] = 1.2
        unphysical = compose_spin1_quark_correlator(
            (0.3, -0.2), 1.8756, values
        )
        self.assertLess(unphysical.minimum_positivity_eigenvalue(), 0.0)

    def test_member_resolved_component_replacement_matches_direct_density(self):
        momentum = (0.3, -0.2)
        mass = 1.8756
        values = {name: 0.0 for name in quark_correlator_basis(momentum, mass)}
        values["f1"] = 1.0
        values["f1Tperp"] = 0.1
        central = compose_spin1_quark_correlator(momentum, mass, values)
        component = quark_correlator_basis(momentum, mass)["f1Tperp"]
        members = np.asarray((-0.3, 0.1, 0.45))
        batched = minimum_eigenvalues_under_component_replacement(
            central, component, values["f1Tperp"], members
        )
        direct = []
        for member in members:
            replaced = dict(values)
            replaced["f1Tperp"] = float(member)
            direct.append(
                compose_spin1_quark_correlator(
                    momentum, mass, replaced
                ).minimum_positivity_eigenvalue()
            )
        np.testing.assert_allclose(batched, direct, atol=2.0e-16, rtol=0.0)


if __name__ == "__main__":
    unittest.main()
