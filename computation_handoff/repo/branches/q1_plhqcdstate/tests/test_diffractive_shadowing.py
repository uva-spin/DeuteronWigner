import unittest

import numpy as np

from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    H1Grid,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)


class DiffractiveShadowingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")

    def test_official_grid_axes_values_and_boundary_clamping(self):
        grid = self.dpdf.singlet
        self.assertEqual(grid.log_z.shape, (100,))
        self.assertEqual(grid.log_q2.shape, (88,))
        self.assertEqual(grid.z_times_density.shape, (100, 88))
        self.assertGreater(grid.value(0.1, 25.0), 0.0)
        self.assertEqual(
            grid.value(1.0e-8, 25.0),
            grid.value(np.exp(grid.log_z[0]), 25.0),
        )

    def test_flux_reproduces_official_normalization(self):
        x = self.dpdf.flux_normalization_x
        nodes, weights = np.polynomial.legendre.leggauss(160)
        t_min_qt2 = 1.0
        qt2 = 0.5 * t_min_qt2 * (nodes + 1.0)
        integral = 0.5 * t_min_qt2 * np.dot(
            weights,
            [self.dpdf.differential_flux(x, value) for value in qt2],
        )
        self.assertAlmostEqual(x * integral, 1.0, places=5)

    def test_fgs_integral_has_domain_scale_and_uncertainty_members(self):
        form_factor = TabulatedBodyFormFactor.load(
            "outputs/stage0/body_form_factor_av18.csv"
        )
        model = build_h1_deuteron_shadowing_input(
            inclusive_density=lambda x, q: 10.0 * x ** -0.2,
            body_form_factor=form_factor,
            dpdf=self.dpdf,
            integration_points=24,
        )
        central = model.value("sea", 0.01, 5.0)
        self.assertGreater(central, 0.0)
        self.assertEqual(model.value("sea", 0.1, 5.0), 0.0)
        self.assertEqual(model.value("gluon", 0.03, 5.0), 0.0)
        members = model.member_values("sea", 0.01, 5.0)
        self.assertEqual(
            set(members),
            {"dpdf_norm_down", "dpdf_norm_up", "t_slope_down", "t_slope_up"},
        )
        self.assertAlmostEqual(members["dpdf_norm_down"], 0.8 * central)
        self.assertAlmostEqual(members["dpdf_norm_up"], 1.2 * central)
        self.assertFalse(model.applies_longitudinal_coherence)
        # Fixed official-grid fixture guards the HERA-to-rescattering 16*pi
        # convention, flux normalization, real-part factor, and form factor.
        self.assertAlmostEqual(central, 0.06570561802567244, places=10)

    def test_malformed_grid_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "expected"):
            H1Grid.load("data/raw/h1_2007_dpdf/readme_h12007.txt")

    def test_production_quadrature_is_converged(self):
        form_factor = TabulatedBodyFormFactor.load(
            "outputs/stage0/body_form_factor_av18.csv"
        )
        values = []
        for points in (32, 48, 64):
            model = build_h1_deuteron_shadowing_input(
                inclusive_density=lambda x, q: 1.0,
                body_form_factor=form_factor,
                dpdf=self.dpdf,
                integration_points=points,
            )
            values.append(model.value("sea", 0.01, 5.0))
        self.assertLess(abs(values[1] - values[2]) / values[2], 1.0e-4)
        self.assertLess(abs(values[0] - values[2]) / values[2], 2.0e-4)


if __name__ == "__main__":
    unittest.main()
