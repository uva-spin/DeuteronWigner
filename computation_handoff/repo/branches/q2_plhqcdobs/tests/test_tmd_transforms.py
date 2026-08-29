import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.fourier import (
    bessel_b_to_k,
    bessel_k_to_b,
    gluon_tmd_b_to_k,
    rank_zero_quark_tmd_b_to_k,
)
from deuteron_wigner.gluon_correlator import (
    compose_unpolarized_gluon_correlator,
    project_unpolarized_gluon_correlator,
)
from deuteron_wigner.sidis import (
    rank_zero_sidis_structure,
    tensor_cos2phi_sidis_structure,
    tensor_sidis_ratio,
)
from deuteron_wigner.tmd_models import GaussianRankZeroTMD


class TMDTransformTests(unittest.TestCase):
    def test_gaussian_bessel_pair_and_collinear_integral(self):
        width = 0.7
        b = np.linspace(0.0, 12.0, 1201)
        k = np.linspace(0.0, 8.0, 1001)
        b_values = np.exp(-width * b**2 / 4.0)
        actual = bessel_b_to_k(b, b_values, k)
        expected = np.exp(-k**2 / width) / (np.pi * width)
        self.assertLess(np.max(np.abs(actual.real - expected)), 2e-7)
        collinear = 2.0 * np.pi * simpson(k * actual.real, x=k)
        self.assertAlmostEqual(collinear, 1.0, places=6)

    def test_inverse_gaussian_transform(self):
        width = 0.7
        k = np.linspace(0.0, 8.0, 1201)
        b = np.linspace(0.0, 6.0, 301)
        k_values = np.exp(-k**2 / width) / (np.pi * width)
        actual = bessel_k_to_b(k, k_values, b)
        expected = np.exp(-width * b**2 / 4.0)
        self.assertLess(np.max(np.abs(actual.real - expected)), 2e-7)

    def test_rank_zero_quark_adapter_preserves_three_scalars(self):
        width = 0.7
        b = np.linspace(0.0, 12.0, 1201)
        k = np.asarray((0.0, 0.4, 1.0))
        base = np.exp(-width * b**2 / 4.0)
        actual = rank_zero_quark_tmd_b_to_k(
            b, base, -0.3 * base, 0.2 * base, k
        )
        expected = np.exp(-k**2 / width) / (np.pi * width)
        self.assertLess(np.max(np.abs(actual.f1.real - expected)), 2e-7)
        self.assertLess(np.max(np.abs(actual.g1.real + 0.3 * expected)), 2e-7)
        self.assertLess(np.max(np.abs(actual.h1.real - 0.2 * expected)), 2e-7)

    def test_gluon_rank_two_adapter_and_zero_momentum_limit(self):
        b = np.linspace(0.0, 14.0, 2801)
        k = np.asarray((0.0, 0.2, 0.7))
        h_b = np.exp(-0.6 * b**2)
        transformed = gluon_tmd_b_to_k(
            b,
            np.exp(-0.4 * b**2),
            0.3 * np.exp(-0.4 * b**2),
            h_b,
            k,
            nucleon_mass=0.9389,
        )
        expected_zero = (
            -0.9389**2
            / 4.0
            * simpson(b**3 * h_b / (2.0 * np.pi), x=b)
        )
        self.assertAlmostEqual(
            transformed.h1perp[0].real, expected_zero, places=10
        )
        self.assertTrue(np.all(np.isfinite(transformed.h1perp)))

    def test_rank_two_adapter_reconstructs_cartesian_coefficient(self):
        b = np.linspace(0.0, 12.0, 2401)
        transformed = gluon_tmd_b_to_k(
            b,
            np.exp(-0.5 * b**2),
            np.zeros_like(b),
            0.2 * np.exp(-0.7 * b**2),
            np.asarray((0.4,)),
            nucleon_mass=0.9389,
        )
        correlator = compose_unpolarized_gluon_correlator(
            (0.4, 0.0),
            0.9389,
            f1=transformed.f1[0].real,
            h1perp=transformed.h1perp[0].real,
        )
        projected = project_unpolarized_gluon_correlator(
            correlator, (0.4, 0.0), 0.9389
        )
        self.assertAlmostEqual(
            projected.linear, transformed.h1perp[0].real, places=12
        )

    def test_gaussian_model_normalization(self):
        model = GaussianRankZeroTMD(lambda flavor, x, scale: 3.0 * x, width=0.4)
        self.assertAlmostEqual(model.b_space(2, 0.2, 0.0, 2.0).real, 0.6)

    def test_sidis_ratio_cancels_common_profile(self):
        b = np.linspace(0.0, 10.0, 1001)
        fragmentation = lambda flavor, coordinate: np.exp(-0.3 * coordinate**2)
        unpolarized = rank_zero_sidis_structure(
            b=b,
            p_h_t=0.4,
            z_h=0.5,
            flavors=(1, 2),
            charges={1: -1.0 / 3.0, 2: 2.0 / 3.0},
            deuteron_tmd=lambda flavor, coordinate: (flavor + 2) * np.exp(
                -0.2 * coordinate**2
            ),
            fragmentation_tmd=fragmentation,
        )
        tensor = rank_zero_sidis_structure(
            b=b,
            p_h_t=0.4,
            z_h=0.5,
            flavors=(1, 2),
            charges={1: -1.0 / 3.0, 2: 2.0 / 3.0},
            deuteron_tmd=lambda flavor, coordinate: 0.1
            * (flavor + 2)
            * np.exp(-0.2 * coordinate**2),
            fragmentation_tmd=fragmentation,
        )
        self.assertAlmostEqual(
            tensor_sidis_ratio(unpolarized=unpolarized, tensor_difference=tensor),
            0.1,
            places=12,
        )

    def test_tensor_cos2phi_kernel_is_rotationally_covariant(self):
        axis = np.linspace(-3.0, 3.0, 161)
        gaussian = lambda flavor, x, y: np.exp(-0.8 * (x*x + y*y))
        arguments = dict(
            x=0.2,
            p_axis=axis,
            z_h=0.5,
            target_mass=1.875,
            hadron_mass=0.139,
            flavors=(2,),
            charges={2: 2.0 / 3.0},
            h1ll_perp=gaussian,
            collins=gaussian,
        )
        along_x = tensor_cos2phi_sidis_structure(
            p_h_x=0.4, p_h_y=0.0, **arguments
        )
        along_y = tensor_cos2phi_sidis_structure(
            p_h_x=0.0, p_h_y=0.4, **arguments
        )
        self.assertAlmostEqual(along_x, along_y, places=10)

    def test_tensor_cos2phi_requires_defined_azimuth(self):
        with self.assertRaises(ValueError):
            tensor_cos2phi_sidis_structure(
                x=0.2,
                p_axis=np.linspace(-1.0, 1.0, 9),
                p_h_x=0.0,
                p_h_y=0.0,
                z_h=0.5,
                target_mass=1.875,
                hadron_mass=0.139,
                flavors=(2,),
                charges={2: 2.0 / 3.0},
                h1ll_perp=lambda flavor, x, y: 1.0,
                collins=lambda flavor, x, y: 1.0,
            )


if __name__ == "__main__":
    unittest.main()
