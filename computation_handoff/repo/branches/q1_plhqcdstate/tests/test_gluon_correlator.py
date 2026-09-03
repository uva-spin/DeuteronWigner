import unittest

import numpy as np

from deuteron_wigner.gluon_correlator import (
    compose_spin1_gluon_correlator,
    EPSILON_T,
    GluonCorrelatorObservation,
    GluonTargetPolarization,
    compose_ll_gluon_correlator,
    compose_longitudinal_gluon_correlator,
    compose_polarized_gluon_correlator,
    compose_unpolarized_gluon_correlator,
    gluon_correlator_basis,
    project_ll_gluon_correlator,
    project_longitudinal_gluon_correlator,
    project_polarized_gluon_correlators,
    project_unpolarized_gluon_correlator,
    transverse_matrix_parts,
)
from deuteron_wigner.registry import TargetChannel


class TestGluonCorrelator(unittest.TestCase):
    def setUp(self):
        self.k = np.asarray((0.37, -0.21))
        self.mass = 1.8756

    def test_matrix_parts_reconstruct_general_matrix(self):
        phi = np.asarray(((2.0, 0.7 + 0.4j), (0.7 - 0.4j, -1.0)))
        trace, circular, linear = transverse_matrix_parts(phi)
        rebuilt = trace * np.eye(2) + circular * 1j * EPSILON_T + linear
        np.testing.assert_allclose(rebuilt, phi)

    def test_unpolarized_round_trip(self):
        phi = compose_unpolarized_gluon_correlator(
            self.k, self.mass, f1=2.3, h1perp=-0.8
        )
        result = project_unpolarized_gluon_correlator(phi, self.k, self.mass)
        self.assertAlmostEqual(result.trace, 2.3)
        self.assertAlmostEqual(result.linear, -0.8)

    def test_longitudinal_round_trip(self):
        phi = compose_longitudinal_gluon_correlator(
            self.k, self.mass, -0.7, g1=0.41, h1Lperp=-1.2
        )
        result = project_longitudinal_gluon_correlator(
            phi, self.k, self.mass, -0.7
        )
        np.testing.assert_allclose(result, (0.41, -1.2))

    def test_ll_round_trip(self):
        phi = compose_ll_gluon_correlator(
            self.k, self.mass, 0.5, f1LL=-0.31, h1LLperp=0.92
        )
        result = project_ll_gluon_correlator(phi, self.k, self.mass, 0.5)
        self.assertAlmostEqual(result.trace, -0.31)
        self.assertAlmostEqual(result.linear, 0.92)

    def test_unpolarized_rotational_covariance(self):
        angle = 0.73
        rotation = np.asarray(
            ((np.cos(angle), -np.sin(angle)), (np.sin(angle), np.cos(angle)))
        )
        phi = compose_unpolarized_gluon_correlator(
            self.k, self.mass, f1=1.1, h1perp=0.6
        )
        rotated = compose_unpolarized_gluon_correlator(
            rotation @ self.k, self.mass, f1=1.1, h1perp=0.6
        )
        np.testing.assert_allclose(rotated, rotation @ phi @ rotation.T)

    def test_zero_momentum_rank_two_projection_rejected(self):
        phi = compose_unpolarized_gluon_correlator(
            (0.0, 0.0), self.mass, f1=1.0, h1perp=2.0
        )
        with self.assertRaises(ValueError):
            project_unpolarized_gluon_correlator(
                phi, (0.0, 0.0), self.mass
            )

    def _round_trip(self, channel, tmds, polarizations):
        observations = []
        angles = np.linspace(0.0, 1.7, len(polarizations))
        radius = np.linalg.norm(self.k)
        for angle, polarization in zip(angles, polarizations):
            momentum = (radius * np.cos(angle), radius * np.sin(angle))
            phi = compose_polarized_gluon_correlator(
                channel, momentum, self.mass, polarization, tmds
            )
            observations.append(
                GluonCorrelatorObservation(momentum, polarization, phi)
            )
        result = project_polarized_gluon_correlators(
            channel, observations, self.mass
        )
        if channel == TargetChannel.TT:
            expected_combination = tmds["f1TT"] - tmds["h1TTperp"]
            self.assertAlmostEqual(
                result["f1TT_minus_h1TTperp"], expected_combination, places=11
            )
            tmds = {
                name: value
                for name, value in tmds.items()
                if name not in ("f1TT", "h1TTperp")
            }
        for name, expected in tmds.items():
            self.assertAlmostEqual(result[name], expected, places=11)

    def test_t_round_trip_all_four_tmds(self):
        polarizations = [
            GluonTargetPolarization(spin_transverse=(1.0, 0.0)),
            GluonTargetPolarization(spin_transverse=(0.0, 1.0)),
            GluonTargetPolarization(spin_transverse=(0.6, -0.8)),
        ]
        self._round_trip(
            TargetChannel.T,
            {"f1Tperp": 0.2, "g1T": -0.4, "h1": 0.7, "h1Tperp": -1.1},
            polarizations,
        )

    def test_lt_round_trip_all_four_tmds(self):
        polarizations = [
            GluonTargetPolarization(spin_lt=(1.0, 0.0)),
            GluonTargetPolarization(spin_lt=(0.0, 1.0)),
            GluonTargetPolarization(spin_lt=(0.6, -0.8)),
        ]
        self._round_trip(
            TargetChannel.LT,
            {"f1LT": -0.3, "g1LT": 0.8, "h1LT": 1.2, "h1LTperp": -0.5},
            polarizations,
        )

    def test_tt_round_trip_all_five_tmds(self):
        polarizations = [
            GluonTargetPolarization(spin_tt=((1.0, 0.0), (0.0, -1.0))),
            GluonTargetPolarization(spin_tt=((0.0, 1.0), (1.0, 0.0))),
            GluonTargetPolarization(spin_tt=((0.6, -0.8), (-0.8, -0.6))),
            GluonTargetPolarization(spin_tt=((-0.3, 0.4), (0.4, 0.3))),
        ]
        self._round_trip(
            TargetChannel.TT,
            {
                "f1TT": 0.6,
                "g1TT": -0.2,
                "h1TT": 1.4,
                "h1TTperp": -0.9,
                "h1TTperpperp": 0.35,
            },
            polarizations,
        )

    def test_joint_projection_rejects_rank_deficient_ensemble(self):
        polarization = GluonTargetPolarization()
        tmds = {
            "f1TT": 0.6,
            "g1TT": -0.2,
            "h1TT": 1.4,
            "h1TTperp": -0.9,
            "h1TTperpperp": 0.35,
        }
        phi = compose_polarized_gluon_correlator(
            TargetChannel.TT, self.k, self.mass, polarization, tmds
        )
        with self.assertRaisesRegex(ValueError, "rank|ill-conditioned"):
            project_polarized_gluon_correlators(
                TargetChannel.TT,
                [GluonCorrelatorObservation(tuple(self.k), polarization, phi)],
                self.mass,
            )

    def test_basis_rejects_nontraceless_tt_polarization(self):
        polarization = GluonTargetPolarization(
            spin_tt=((1.0, 0.0), (0.0, 1.0))
        )
        with self.assertRaisesRegex(ValueError, "traceless"):
            gluon_correlator_basis(
                TargetChannel.TT, self.k, self.mass, polarization
            )

    def test_complete_joint_gluon_density_detects_positivity(self):
        names = {
            "f1", "h1perp", "g1", "h1Lperp",
            "f1Tperp", "g1T", "h1", "h1Tperp",
            "f1LL", "h1LLperp", "f1LT", "g1LT",
            "h1LT", "h1LTperp", "f1TT_minus_h1TTperp",
            "g1TT", "h1TT", "h1TTperpperp",
        }
        values = {name: 0.0 for name in names}
        values["f1"] = 1.0
        physical = compose_spin1_gluon_correlator(
            self.k, self.mass, values
        )
        self.assertGreaterEqual(physical.minimum_positivity_eigenvalue(), 0.0)
        values["g1"] = 1.2
        unphysical = compose_spin1_gluon_correlator(
            self.k, self.mass, values
        )
        self.assertLess(unphysical.minimum_positivity_eigenvalue(), 0.0)

    def test_all_polarized_basis_matrices_are_rotationally_covariant(self):
        angle = 0.49
        rotation = np.asarray(
            ((np.cos(angle), -np.sin(angle)), (np.sin(angle), np.cos(angle)))
        )
        cases = (
            (
                TargetChannel.T,
                GluonTargetPolarization(spin_transverse=(0.3, -0.7)),
                GluonTargetPolarization(
                    spin_transverse=tuple(rotation @ np.asarray((0.3, -0.7)))
                ),
            ),
            (
                TargetChannel.LT,
                GluonTargetPolarization(spin_lt=(-0.4, 0.8)),
                GluonTargetPolarization(
                    spin_lt=tuple(rotation @ np.asarray((-0.4, 0.8)))
                ),
            ),
            (
                TargetChannel.TT,
                GluonTargetPolarization(
                    spin_tt=((0.6, -0.2), (-0.2, -0.6))
                ),
                GluonTargetPolarization(
                    spin_tt=tuple(
                        map(
                            tuple,
                            rotation
                            @ np.asarray(((0.6, -0.2), (-0.2, -0.6)))
                            @ rotation.T,
                        )
                    )
                ),
            ),
        )
        for channel, polarization, rotated_polarization in cases:
            basis = gluon_correlator_basis(
                channel, self.k, self.mass, polarization
            )
            rotated_basis = gluon_correlator_basis(
                channel, rotation @ self.k, self.mass, rotated_polarization
            )
            for name in basis:
                np.testing.assert_allclose(
                    rotated_basis[name],
                    rotation @ basis[name] @ rotation.T,
                    atol=2.0e-16,
                    err_msg=f"{channel.value}:{name}",
                )


if __name__ == "__main__":
    unittest.main()
