import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.tmd_models import (
    GaussianSpinHalfGluonGTMD,
    InterpolatedSpinHalfGluonGTMD,
)


class GaussianSpinHalfGluonGTMDTests(unittest.TestCase):
    @staticmethod
    def f1(x, scale):
        return 3.0 * x * (1.0 - x)

    @staticmethod
    def g1(x, scale):
        return 0.4 * GaussianSpinHalfGluonGTMDTests.f1(x, scale)

    def setUp(self):
        self.model = GaussianSpinHalfGluonGTMD(
            self.f1,
            width=0.25,
            nucleon_mass=0.9389,
            helicity_pdf=self.g1,
            linear_fraction=0.6,
            transfer_slope=0.8,
        )

    def test_unpolarized_gaussian_integrates_to_collinear_pdf(self):
        axis = np.linspace(-2.0, 2.0, 501)
        values = np.empty((len(axis), len(axis)))
        for i, k_x in enumerate(axis):
            for j, k_y in enumerate(axis):
                values[i, j] = self.model.tmd_values(
                    0.2, k_x, k_y, 2.0
                )["f1"]
        integral = simpson(simpson(values, x=axis, axis=1), x=axis, axis=0)
        self.assertAlmostEqual(
            integral, self.f1(0.2, 2.0), delta=2.0e-8
        )

    def test_linear_polarization_is_bounded(self):
        for k in np.linspace(0.0, 5.0, 101):
            correlator = self.model(0.2, k, 0.0, 0.0, 0.0, 2.0)
            trace, _, linear = transverse_matrix_parts(correlator[0, 0])
            linear_size = np.sqrt(np.einsum("ij,ij->", linear, linear).real)
            trace_size = np.sqrt(2.0) * abs(trace)
            self.assertLessEqual(linear_size, 0.6 * trace_size + 1.0e-15)

    def test_helicity_changes_sign_with_nucleon_helicity(self):
        correlator = self.model(0.2, 0.3, -0.1, 0.0, 0.0, 2.0)
        _, circular_plus, _ = transverse_matrix_parts(correlator[0, 0])
        _, circular_minus, _ = transverse_matrix_parts(correlator[1, 1])
        self.assertAlmostEqual(circular_plus.real, -circular_minus.real)
        self.assertGreater(abs(circular_plus), 0.0)

    def test_transfer_factor_is_applied(self):
        forward = self.model(0.2, 0.3, -0.1, 0.0, 0.0, 2.0)
        shifted = self.model(0.2, 0.3, -0.1, 0.4, 0.0, 2.0)
        np.testing.assert_allclose(
            shifted, np.exp(-0.8 * 0.4**2) * forward
        )

    def test_invalid_linear_fraction_rejected(self):
        with self.assertRaises(ValueError):
            GaussianSpinHalfGluonGTMD(
                self.f1, width=0.25, nucleon_mass=0.9389, linear_fraction=1.1
            )


class InterpolatedSpinHalfGluonGTMDTests(unittest.TestCase):
    def setUp(self):
        x = np.asarray((0.1, 0.5, 1.0))
        k = np.asarray((0.0, 0.5, 1.0))
        x_grid, k_grid = np.meshgrid(x, k, indexing="ij")
        self.model = InterpolatedSpinHalfGluonGTMD(
            x,
            k,
            f1=2.0 * x_grid + k_grid,
            g1=0.4 * x_grid - 0.2 * k_grid,
            h1perp=x_grid + 0.5 * k_grid,
            nucleon_mass_GeV=0.94,
            momentum_unit_to_GeV=0.2,
        )

    def test_bilinear_values_and_unit_conversion(self):
        values = self.model.tmd_values(0.3, 3.0, 0.0, 9.0)
        self.assertAlmostEqual(values["f1"], 1.2)
        self.assertAlmostEqual(values["g1"], 0.0)
        self.assertAlmostEqual(values["h1perp"], 0.6)

    def test_strict_domain_rejects_extrapolation(self):
        with self.assertRaises(ValueError):
            self.model.tmd_values(0.05, 0.0, 0.0, 2.0)
        with self.assertRaises(ValueError):
            self.model.tmd_values(0.2, 6.0, 0.0, 2.0)

    def test_callable_has_retained_spin_and_gluon_indices(self):
        correlator = self.model(0.3, 2.0, 0.0, 0.0, 0.0, 2.0)
        self.assertEqual(correlator.shape, (2, 2, 2, 2))
        np.testing.assert_allclose(correlator[0, 1], 0.0, atol=0.0)


if __name__ == "__main__":
    unittest.main()
