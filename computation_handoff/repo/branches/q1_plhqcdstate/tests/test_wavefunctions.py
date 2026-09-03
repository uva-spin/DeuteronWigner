"""Physics validation tests for instant-form radial inputs."""

from pathlib import Path
import unittest

import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn

from deuteron_wigner.wavefunctions.av18 import (
    av18_asymptotic_tail_norm,
    load_av18_coordinate,
    load_av18_momentum,
)
from deuteron_wigner.wavefunctions.cd_bonn import cd_bonn_parameters
from deuteron_wigner.wavefunctions.models import RadialWaveFunction

ROOT = Path(__file__).resolve().parents[1]


class AV18Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.coordinate = load_av18_coordinate(ROOT / "data/raw/av18/deut.wf")
        cls.momentum = load_av18_momentum(ROOT / "data/raw/av18/deut.wfk")

    def test_metadata_and_grid(self) -> None:
        self.assertEqual(self.coordinate.representation, "coordinate")
        self.assertEqual(self.momentum.representation, "momentum")
        self.assertAlmostEqual(self.coordinate.grid[0], 0.01)
        self.assertAlmostEqual(self.coordinate.grid[-1], 15.0)
        self.assertAlmostEqual(self.momentum.grid[0], 0.0)
        self.assertAlmostEqual(self.momentum.grid[-1], 15.0)

    def test_coordinate_normalization_and_d_state(self) -> None:
        # The authoritative coordinate table stops at 15 fm. Complete only the
        # normalization diagnostic with the header's asymptotic constants.
        s_tail, d_tail = av18_asymptotic_tail_norm(self.coordinate.grid[-1])
        s_norm, d_norm = self.coordinate.component_norms()
        self.assertAlmostEqual(s_norm + d_norm + s_tail + d_tail, 1.0, delta=4e-6)
        self.assertAlmostEqual(d_norm + d_tail, 0.057599, delta=2e-6)

    def test_momentum_normalization_and_d_state(self) -> None:
        self.assertAlmostEqual(self.momentum.norm(), 1.0, delta=2e-5)
        self.assertAlmostEqual(self.momentum.d_state_probability(), 0.057599, delta=2e-6)

    def test_tabulated_derivatives(self) -> None:
        du_numeric = np.gradient(self.coordinate.u, self.coordinate.grid, edge_order=2)
        dw_numeric = np.gradient(self.coordinate.w, self.coordinate.grid, edge_order=2)
        interior = slice(2, -2)
        np.testing.assert_allclose(
            du_numeric[interior], self.coordinate.du[interior], atol=2e-4, rtol=3e-3
        )
        np.testing.assert_allclose(
            dw_numeric[interior], self.coordinate.dw[interior], atol=2e-4, rtol=4e-3
        )

    def test_interpolation_forbids_extrapolation(self) -> None:
        with self.assertRaises(ValueError):
            self.coordinate.interpolate(0.0)
        with self.assertRaises(ValueError):
            self.momentum.interpolate(15.01)

    def test_container_rejects_unsorted_grid(self) -> None:
        with self.assertRaises(ValueError):
            RadialWaveFunction(
                name="invalid",
                representation="coordinate",
                grid=np.array([0.0, 1.0, 0.5]),
                u=np.ones(3),
                w=np.zeros(3),
            )


class CDBonnTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parameters = cd_bonn_parameters()

    def test_coefficient_constraints(self) -> None:
        p = self.parameters
        self.assertAlmostEqual(float(np.sum(p.c)), 0.0, delta=2e-13)
        self.assertAlmostEqual(float(np.sum(p.d)), 0.0, delta=2e-11)
        self.assertAlmostEqual(float(np.sum(p.d * p.masses**2)), 0.0, delta=2e-9)
        self.assertAlmostEqual(float(np.sum(p.d / p.masses**2)), 0.0, delta=2e-13)

    def test_table_xix_coordinate_values(self) -> None:
        # Selected values from Table XIX span the sensitive origin and bulk regions.
        radii = np.array([0.01, 0.10, 0.50, 1.00, 2.00, 4.00, 10.00])
        expected_u = np.array(
            [0.00304061, 0.0301255, 0.194545, 0.431072, 0.510374, 0.347583, 0.0873354]
        )
        expected_w = np.array(
            [-1.37276e-6, -2.64871e-4, 0.0235574, 0.119165, 0.141367, 0.0595344, 0.00636565]
        )
        u, w = self.parameters.coordinate(radii)
        # Appendix D reports an L2 parameterization error of 2.2e-4 for u and
        # 1.1e-4 for w relative to the numerical Table XIX solution.
        np.testing.assert_allclose(u, expected_u, atol=1.5e-4, rtol=5e-4)
        np.testing.assert_allclose(w, expected_w, atol=1.0e-4, rtol=5e-4)

    def test_coordinate_and_momentum_normalizations(self) -> None:
        coordinate = self.parameters.coordinate_norms()
        momentum = self.parameters.momentum_norms()
        self.assertAlmostEqual(sum(coordinate), 1.0, delta=4e-4)
        self.assertAlmostEqual(sum(momentum), 1.0, delta=4e-4)
        self.assertAlmostEqual(coordinate[1], 0.0485, delta=2e-4)
        self.assertAlmostEqual(momentum[1], coordinate[1], delta=2e-8)

    def test_fourier_bessel_consistency(self) -> None:
        # Eq. (D13): u_L(r)/r = sqrt(2/pi) int dk k^2 j_L(kr) psi_L(k).
        p = self.parameters
        for radius in (0.5, 1.0, 2.0, 4.0):
            u_expected, w_expected = p.coordinate(radius)
            u_transform = radius * np.sqrt(2.0 / np.pi) * quad(
                lambda k: k**2 * spherical_jn(0, k * radius) * float(p.momentum(k)[0]),
                0.0,
                200.0,
                epsabs=1e-9,
                limit=300,
            )[0]
            w_transform = radius * np.sqrt(2.0 / np.pi) * quad(
                lambda k: k**2 * spherical_jn(2, k * radius) * float(p.momentum(k)[1]),
                0.0,
                200.0,
                epsabs=1e-9,
                limit=300,
            )[0]
            self.assertAlmostEqual(u_transform, float(u_expected), delta=1e-7)
            self.assertAlmostEqual(w_transform, float(w_expected), delta=1e-7)

    def test_origin_and_asymptotic_behavior(self) -> None:
        p = self.parameters
        origin_u, origin_w = p.coordinate(0.0)
        self.assertEqual(float(origin_u), 0.0)
        self.assertEqual(float(origin_w), 0.0)
        # At radii far enough above floating-point cancellation, the reduced
        # S wave is linear and the D wave is cubic with a finite coefficient.
        radii = np.array([0.004, 0.006, 0.008])
        u, w = p.coordinate(radii)
        np.testing.assert_allclose(u / radii, np.full(3, u[-1] / radii[-1]), rtol=3e-3)
        self.assertTrue(np.all(np.isfinite(w / radii**3)))
        self.assertTrue(np.all(np.abs(w / radii**3) < 2.0))
        large_r = np.array([14.0, 16.0, 18.0])
        u_large, w_large = p.coordinate(large_r)
        s_amplitude = u_large * np.exp(p.gamma * large_r)
        d_amplitude = w_large * np.exp(p.gamma * large_r) / (
            1.0 + 3.0 / (p.gamma * large_r) + 3.0 / (p.gamma * large_r) ** 2
        )
        np.testing.assert_allclose(s_amplitude, np.full(3, p.c[0]), rtol=1e-4)
        np.testing.assert_allclose(d_amplitude, np.full(3, p.d[0]), rtol=1e-4)


if __name__ == "__main__":
    unittest.main()
