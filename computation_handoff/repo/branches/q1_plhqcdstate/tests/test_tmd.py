import unittest

import numpy as np

from deuteron_wigner.collinear import LFSmearingQuadrature, impulse_convolution
from deuteron_wigner.tmd import (
    SpinTransverseSmearingQuadrature,
    TransverseSmearingQuadrature,
    rank_zero_tmd_bspace,
    spin_density_tmd_bspace,
)


class RankZeroTMDTests(unittest.TestCase):
    def setUp(self):
        self.transverse = TransverseSmearingQuadrature(
            y=np.array([0.35, 0.60]),
            p_x=np.array([0.2, -0.1]),
            p_y=np.array([0.0, 0.3]),
            weights=np.array([0.4, 0.6]),
            unpolarized=np.array([0.8, 1.1]),
            tensor=np.array([-0.2, 0.15]),
        )
        self.collinear = LFSmearingQuadrature(
            y=self.transverse.y,
            y_weights=self.transverse.weights,
            unpolarized=self.transverse.unpolarized,
            tensor=self.transverse.tensor,
            p_max=1.0,
        )

    @staticmethod
    def pdf(flavor, x, scale):
        return (1.0 + 0.1 * flavor) * x * (1.0 - x)

    @classmethod
    def b_tmd(cls, flavor, x, b, scale):
        return cls.pdf(flavor, x, scale) * np.exp(-0.2 * b**2)

    def test_b_zero_reproduces_collinear_convolution(self):
        expected = impulse_convolution(
            x=0.2,
            scale=2.0,
            flavor=2,
            proton_pdf=self.pdf,
            neutron_pdf=self.pdf,
            smearing=self.collinear,
        )
        actual = rank_zero_tmd_bspace(
            x=0.2,
            scale=2.0,
            flavor=2,
            b_x=0.0,
            b_y=0.0,
            proton_tmd=self.b_tmd,
            neutron_tmd=self.b_tmd,
            smearing=self.transverse,
        )
        self.assertAlmostEqual(actual.real, expected, places=14)
        self.assertAlmostEqual(actual.imag, 0.0, places=14)

    def test_tensor_b_zero_reproduces_collinear_convolution(self):
        expected = impulse_convolution(
            x=0.2,
            scale=2.0,
            flavor=2,
            proton_pdf=self.pdf,
            neutron_pdf=self.pdf,
            smearing=self.collinear,
            tensor=True,
        )
        actual = rank_zero_tmd_bspace(
            x=0.2,
            scale=2.0,
            flavor=2,
            b_x=0.0,
            b_y=0.0,
            proton_tmd=self.b_tmd,
            neutron_tmd=self.b_tmd,
            smearing=self.transverse,
            tensor=True,
        )
        self.assertAlmostEqual(actual.real, expected, places=14)

    def test_invalid_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            TransverseSmearingQuadrature(
                y=np.ones(2),
                p_x=np.ones(1),
                p_y=np.ones(2),
                weights=np.ones(2),
                unpolarized=np.ones(2),
                tensor=np.ones(2),
            )

    def test_spin_identity_reduces_to_scalar_convolution(self):
        spin = SpinTransverseSmearingQuadrature(
            y=self.transverse.y,
            p_x=self.transverse.p_x,
            p_y=self.transverse.p_y,
            weights=self.transverse.weights,
            unpolarized=np.asarray(
                [np.eye(2) * value / 2.0 for value in self.transverse.unpolarized]
            ),
            tensor=np.asarray(
                [np.eye(2) * value / 2.0 for value in self.transverse.tensor]
            ),
        )
        scalar = rank_zero_tmd_bspace(
            x=0.2,
            scale=2.0,
            flavor=2,
            b_x=0.3,
            b_y=-0.2,
            proton_tmd=self.b_tmd,
            neutron_tmd=self.b_tmd,
            smearing=self.transverse,
            tensor=True,
        )
        matrix_tmd = lambda flavor, x, b, scale: self.b_tmd(
            flavor, x, b, scale
        ) * np.eye(2)
        full = spin_density_tmd_bspace(
            x=0.2,
            scale=2.0,
            flavor=2,
            b_x=0.3,
            b_y=-0.2,
            proton_tmd=matrix_tmd,
            neutron_tmd=matrix_tmd,
            smearing=spin,
            tensor=True,
        )
        self.assertAlmostEqual(full.real, scalar.real, places=14)
        self.assertAlmostEqual(full.imag, scalar.imag, places=14)

    def test_spin_transfer_contracts_helicity_asymmetry(self):
        spin = SpinTransverseSmearingQuadrature(
            y=np.array([0.6]),
            p_x=np.array([0.0]),
            p_y=np.array([0.0]),
            weights=np.array([1.0]),
            unpolarized=np.array([[[0.7, 0.0], [0.0, 0.3]]]),
            tensor=np.array([[[0.2, 0.0], [0.0, -0.2]]]),
        )
        sigma_z_tmd = lambda flavor, x, b, scale: np.diag([2.0, -2.0])
        value = spin_density_tmd_bspace(
            x=0.3,
            scale=2.0,
            flavor=2,
            b_x=0.0,
            b_y=0.0,
            proton_tmd=sigma_z_tmd,
            neutron_tmd=sigma_z_tmd,
            smearing=spin,
            tensor=True,
        )
        self.assertAlmostEqual(value.real, 8.0 / 3.0)


if __name__ == "__main__":
    unittest.main()
