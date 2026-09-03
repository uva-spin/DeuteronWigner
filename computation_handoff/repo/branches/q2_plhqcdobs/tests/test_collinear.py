"""Tests for LF smearing and the collinear impulse bridge."""

import unittest

import numpy as np

from deuteron_wigner.collinear import (
    LFSmearingQuadrature,
    ScalingVariable,
    b1_leading_order,
    build_lf_smearing,
    build_lf_smearing_spherical,
    impulse_convolution,
)


class SmearingTests(unittest.TestCase):
    def test_pure_s_wave_has_zero_tensor_smearing(self) -> None:
        smearing = build_lf_smearing(
            radial=lambda k: (np.exp(-0.5 * k**2), 0.0),
            nucleon_mass=4.75,
            p_max=4.0,
            n_y=10,
            n_p=12,
            n_phi=8,
        )
        np.testing.assert_allclose(smearing.tensor, 0.0, atol=2e-15)
        self.assertAlmostEqual(smearing.tensor_norm(), 0.0, delta=2e-15)

    def test_smearing_symmetry_for_equal_masses(self) -> None:
        smearing = build_lf_smearing(
            radial=lambda k: (np.exp(-0.5 * k**2), 0.08 * k**2 * np.exp(-0.5 * k**2)),
            nucleon_mass=4.75,
            p_max=4.0,
            n_y=12,
            n_p=12,
            n_phi=12,
        )
        np.testing.assert_allclose(
            smearing.unpolarized, smearing.unpolarized[::-1], atol=2e-14, rtol=2e-14
        )
        np.testing.assert_allclose(
            smearing.tensor, smearing.tensor[::-1], atol=2e-14, rtol=2e-14
        )

    def test_spherical_quadrature_recovers_analytic_normalization(self) -> None:
        normalization = 2.0 / np.pi**0.25
        smearing = build_lf_smearing_spherical(
            radial=lambda k: (normalization * np.exp(-0.5 * k**2), 0.0),
            nucleon_mass=4.75,
            k_max=7.0,
            n_k=20,
            n_cos_theta=14,
            n_phi=8,
        )
        self.assertAlmostEqual(smearing.unpolarized_norm(), 1.0, delta=5e-11)
        self.assertAlmostEqual(smearing.tensor_norm(), 0.0, delta=2e-15)


class ConvolutionTests(unittest.TestCase):
    @staticmethod
    def proton(flavor: int, x: float, scale: float) -> float:
        return (1.0 + 0.1 * flavor) * x * (1.0 - x)

    @staticmethod
    def neutron(flavor: int, x: float, scale: float) -> float:
        return (0.8 + 0.05 * flavor) * x * (1.0 - x)

    @classmethod
    def setUpClass(cls) -> None:
        y, weights = np.polynomial.legendre.leggauss(20)
        y = 0.5 * (y + 1.0)
        weights = 0.5 * weights
        cls.smearing = LFSmearingQuadrature(
            y=y,
            y_weights=weights,
            unpolarized=np.full_like(y, 1.0),
            tensor=0.03 * (6.0 * y * (1.0 - y) - 1.0),
            p_max=1.0,
        )

    def test_tensor_and_unpolarized_paths_are_separate(self) -> None:
        ordinary = impulse_convolution(
            x=0.2,
            scale=2.0,
            flavor=2,
            proton_pdf=self.proton,
            neutron_pdf=self.neutron,
            smearing=self.smearing,
        )
        tensor = impulse_convolution(
            x=0.2,
            scale=2.0,
            flavor=2,
            proton_pdf=self.proton,
            neutron_pdf=self.neutron,
            smearing=self.smearing,
            tensor=True,
        )
        self.assertNotEqual(ordinary, tensor)

    def test_b1_implements_charge_weighted_quark_plus_antiquark(self) -> None:
        charges = {1: -1.0 / 3.0, 2: 2.0 / 3.0}
        result = b1_leading_order(
            x=0.2,
            scale=2.0,
            flavors=(1, 2),
            charges=charges,
            proton_pdf=self.proton,
            neutron_pdf=self.neutron,
            smearing=self.smearing,
        )
        manual = 0.0
        for flavor in (1, 2):
            q = impulse_convolution(
                x=0.2,
                scale=2.0,
                flavor=flavor,
                proton_pdf=self.proton,
                neutron_pdf=self.neutron,
                smearing=self.smearing,
                tensor=True,
            )
            qbar = impulse_convolution(
                x=0.2,
                scale=2.0,
                flavor=-flavor,
                proton_pdf=self.proton,
                neutron_pdf=self.neutron,
                smearing=self.smearing,
                tensor=True,
            )
            manual += 0.5 * charges[flavor] ** 2 * (q + qbar)
        self.assertAlmostEqual(result, manual)

    def test_nucleon_scaling_uses_alpha_equal_two_y(self) -> None:
        deuteron = impulse_convolution(
            x=0.1,
            scale=2.0,
            flavor=2,
            proton_pdf=self.proton,
            neutron_pdf=self.neutron,
            smearing=self.smearing,
            scaling_variable=ScalingVariable.DEUTERON,
        )
        nucleon = impulse_convolution(
            x=0.2,
            scale=2.0,
            flavor=2,
            proton_pdf=self.proton,
            neutron_pdf=self.neutron,
            smearing=self.smearing,
            scaling_variable=ScalingVariable.NUCLEON,
        )
        # Same partonic argument x_D/y=x_N/(2y); the measure supplies 1/(2y).
        self.assertAlmostEqual(nucleon, 0.5 * deuteron)


if __name__ == "__main__":
    unittest.main()
