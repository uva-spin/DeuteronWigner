import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.gtmd_convolution import OffForwardSpinQuadrature
from deuteron_wigner.gtmd_convolution import convolve_gtmd_point
from deuteron_wigner.gtmd_models import FactorizedGaussianGTMD
from deuteron_wigner.gtmd_sampling import (
    convolve_factorized_gaussian_gpd,
    convolve_factorized_gaussian_grid,
    deuteron_x_parent_to_nucleon_x,
)
from deuteron_wigner.spin import HelicityMatrix


class GTMDSamplingTests(unittest.TestCase):
    def setUp(self):
        spectral = np.zeros((1, 3, 3, 2, 2), dtype=np.complex128)
        spectral[0] = np.diag([0.8, 1.1, 0.9])[..., None, None] * np.eye(2)
        self.quadrature = OffForwardSpinQuadrature(
            y=np.array([0.7]), p_x=np.array([0.13]), p_y=np.array([-0.08]),
            weights=np.array([1.0]), delta_x=0.2, delta_y=-0.1,
            spectral=spectral,
        )
        pdf = lambda flavor, x, scale: (1.0 + 0.1 * flavor) * x * (1.0 - x)
        self.model = FactorizedGaussianGTMD(pdf=pdf, width=0.35, slope=0.4)

    def test_k_marginal_matches_analytic_gpd(self):
        axis = np.linspace(-4.0, 4.0, 241)
        sampled = convolve_factorized_gaussian_grid(
            x=0.2, k_x=axis, k_y=axis, scale=2.0, flavor=2,
            proton=self.model, neutron=self.model, quadrature=self.quadrature,
        ).values
        integrated = simpson(simpson(sampled, x=axis, axis=1), x=axis, axis=0)
        expected = convolve_factorized_gaussian_gpd(
            x=0.2, scale=2.0, flavor=2, proton=self.model,
            neutron=self.model, quadrature=self.quadrature,
        ).values
        np.testing.assert_allclose(integrated, expected, atol=2e-12)

    def test_model_helicity_trace_and_transfer_normalization(self):
        matrix = self.model(2, 0.3, 0.1, -0.2, 0.0, 0.0, 2.0)
        self.assertAlmostEqual(np.trace(matrix).real, self.model.scalar(
            2, 0.3, 0.1, -0.2, 0.0, 0.0, 2.0
        ))
        self.assertAlmostEqual(
            self.model.collinear(2, 0.3, 0.0, 0.0, 2.0),
            self.model.pdf(2, 0.3, 2.0),
        )

    def test_vectorized_grid_matches_point_convolution(self):
        sampled = convolve_factorized_gaussian_grid(
            x=0.2, k_x=np.array([-0.1, 0.2]), k_y=np.array([0.05]),
            scale=2.0, flavor=2, proton=self.model, neutron=self.model,
            quadrature=self.quadrature,
        ).values
        for ix, k_x in enumerate((-0.1, 0.2)):
            point = convolve_gtmd_point(
                x=0.2, k_x=k_x, k_y=0.05, scale=2.0, flavor=2,
                proton_gtmd=self.model, neutron_gtmd=self.model,
                quadrature=self.quadrature,
            ).values
            np.testing.assert_allclose(sampled[ix, 0], point, atol=1e-15)

    def test_x_density_conversion_preserves_integrated_number(self):
        parent = HelicityMatrix(np.eye(3))
        converted = deuteron_x_parent_to_nucleon_x(
            parent, x_nucleon=0.4, x_deuteron=0.2
        )
        np.testing.assert_allclose(converted.values, 0.5 * parent.values)


if __name__ == "__main__":
    unittest.main()
