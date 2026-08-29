import unittest
from unittest.mock import patch

import numpy as np
from scipy.integrate import quad

from deuteron_wigner.pion_exchange import (
    JAM21IsoscalarPionPDF,
    FockNormalizedMillerPionDistribution,
    NNPiLongitudinalRecoilConvolution,
    MillerPionExchangeParameters,
    MillerTensorPionDistribution,
    SpinAveragedPionConvolution,
    TensorPionConvolution,
    build_spin_averaged_pion_component,
    build_minimal_fock_consistent_pion_component,
    build_longitudinal_recoil_fock_component,
    build_tensor_pion_component,
)
from deuteron_wigner.nuclear_mechanisms import apply_nuclear_corrections
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.spin import HelicityMatrix
from deuteron_wigner.provenance import Mechanism


class PionExchangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.splitting = MillerTensorPionDistribution()
        cls.pdf = JAM21IsoscalarPionPDF(0)

    def test_radial_zero_momentum_limits_reproduce_wave_norms(self):
        s_norm, d_norm = self.splitting.wave.component_norms()
        self.assertAlmostEqual(
            self.splitting.radial_integral("uu0", 0.0), s_norm, places=10
        )
        self.assertAlmostEqual(
            self.splitting.radial_integral("ww0", 0.0), d_norm, places=10
        )
        self.assertAlmostEqual(
            self.splitting.radial_integral("uw2", 0.0), 0.0, places=14
        )
        self.assertAlmostEqual(
            self.splitting.radial_integral("ww2", 0.0), 0.0, places=14
        )
        self.assertEqual(
            self.splitting.provenance.mechanism, Mechanism.MESON_EXCHANGE
        )

    def test_tensor_splitting_is_even_and_obeys_published_sum_rule(self):
        for y in (0.01, 0.05, 0.1, 0.4):
            self.assertAlmostEqual(
                self.splitting.delta_f(y), self.splitting.delta_f(-y)
            )
        moment = quad(
            lambda y: self.splitting.delta_f(y) / y,
            1.0e-5,
            2.0,
            epsabs=2.0e-7,
            epsrel=2.0e-5,
            points=(0.01, 0.03, 0.05, 0.1, 0.2, 0.4, 0.8),
            limit=240,
        )[0]
        self.assertLess(abs(moment), 3.0e-5)

    def test_transverse_quadrature_is_converged(self):
        refined = MillerTensorPionDistribution(
            parameters=MillerPionExchangeParameters(
                q_nodes=2001, transverse_nodes=640
            )
        )
        for y in (0.01, 0.03, 0.05, 0.1, 0.2, 0.4, 0.8):
            reference = refined.delta_f(y)
            actual = self.splitting.delta_f(y)
            self.assertLess(
                abs(actual - reference),
                max(2.0e-6, 1.0e-4 * abs(reference)),
            )

    def test_spin_average_reconstructs_published_helicity_projections(self):
        for y in (0.01, 0.05, 0.1, 0.2, 0.4, 0.8):
            f0 = self.splitting.spin_projection_f(0, y)
            f1 = self.splitting.spin_projection_f(1, y)
            self.assertAlmostEqual(
                self.splitting.spin_averaged_f(y), (f0 + 2.0 * f1) / 3.0,
                places=11,
            )
            self.assertAlmostEqual(self.splitting.delta_f(y), f0 - f1, places=11)

    def test_spin_averaged_connected_pion_moments(self):
        moments = self.splitting.spin_averaged_moments()
        self.assertAlmostEqual(moments["pion_number_connected"], 0.02129174, places=7)
        self.assertAlmostEqual(
            moments["pion_deuteron_plus_momentum_fraction"], 0.00410205, places=7
        )
        audit = self.splitting.momentum_audit()
        self.assertFalse(audit.passes())
        self.assertAlmostEqual(audit.uncompensated_total, 1.00410205, places=7)
        self.assertAlmostEqual(audit.required_nucleon_fraction, 0.99589795, places=7)

    def test_exact_nn_pinn_fock_ledger_closes_probability_and_momentum(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        ledger = normalized.ledger
        self.assertAlmostEqual(
            ledger.nn_probability + ledger.pinn_probability, 1.0, places=14
        )
        self.assertAlmostEqual(ledger.total_momentum, 1.0, places=14)
        self.assertGreater(ledger.pinn_sector_nucleon_momentum, 0.0)
        self.assertGreater(ledger.pinn_sector_pion_momentum, 0.0)
        self.assertAlmostEqual(
            normalized.spin_averaged_f(0.2),
            self.splitting.spin_averaged_f(0.2) / ledger.z_factor,
        )
        self.assertAlmostEqual(
            normalized.delta_f(0.2),
            self.splitting.delta_f(0.2) / ledger.z_factor,
        )
        self.assertAlmostEqual(
            normalized.spin_averaged_f_b(0.2, 0.5, 1.0),
            self.splitting.spin_averaged_f_b(0.2, 0.5, 1.0)
            / ledger.z_factor,
        )

    def test_isoscalar_charge_average_is_flavor_symmetric(self):
        values = [self.pdf.value(flavor, 0.2, 5.0) for flavor in (2, 1, -2, -1)]
        self.assertGreater(values[0], 0.0)
        for value in values[1:]:
            self.assertAlmostEqual(value, values[0], places=10)

    def test_convolution_conventions_and_exact_zero_switch(self):
        active = TensorPionConvolution(self.splitting, self.pdf)
        zero = TensorPionConvolution(self.splitting, self.pdf, strength=0.0)
        delta = active.delta_t(2, 0.1, 5.0)
        self.assertNotEqual(delta, 0.0)
        self.assertAlmostEqual(active.f1ll(2, 0.1, 5.0), -2.0 * delta / 3.0)
        self.assertAlmostEqual(active.b1(0.1, 5.0), 5.0 * delta / 9.0)
        self.assertEqual(zero.delta_t(2, 0.1, 5.0), 0.0)
        self.assertEqual(zero.b1(0.1, 5.0), 0.0)

    def test_correlator_adapter_is_pure_tensor_and_reconstructs(self):
        convolution = TensorPionConvolution(self.splitting, self.pdf)
        component = build_tensor_pion_component(2, convolution)
        zero = Spin1QuarkCorrelator(
            np.zeros((3, 3), dtype=complex),
            np.zeros((3, 3), dtype=complex),
            np.zeros((2, 3, 3), dtype=complex),
        )
        result = apply_nuclear_corrections(
            proton_impulse=zero,
            neutron_impulse=zero,
            x=0.1,
            scale_gev=5.0,
            meson_exchange_input=component,
        )
        pion = result.corrections["meson_exchange"]
        vector = HelicityMatrix(pion.vector)
        self.assertAlmostEqual(
            vector.tensor_difference().real,
            convolution.delta_t(2, 0.1, 5.0),
        )
        self.assertAlmostEqual(
            vector.unpolarized().real, 0.0
        )
        np.testing.assert_array_equal(pion.axial, 0.0)
        np.testing.assert_array_equal(pion.transverse, 0.0)
        np.testing.assert_allclose(result.total.vector, pion.vector)

    def test_spin_averaged_adapter_is_identity_only(self):
        convolution = SpinAveragedPionConvolution(self.splitting, self.pdf)
        with self.assertRaisesRegex(RuntimeError, "momentum policy"):
            build_spin_averaged_pion_component(2, convolution)
        component = build_spin_averaged_pion_component(
            2, convolution, momentum_accounting_acknowledged=True
        )
        zero = Spin1QuarkCorrelator(
            np.zeros((3, 3), dtype=complex),
            np.zeros((3, 3), dtype=complex),
            np.zeros((2, 3, 3), dtype=complex),
        )
        result = apply_nuclear_corrections(
            proton_impulse=zero,
            neutron_impulse=zero,
            x=0.1,
            scale_gev=5.0,
            meson_exchange_input=component,
        )
        pion = result.corrections["meson_exchange"]
        vector = HelicityMatrix(pion.vector)
        self.assertAlmostEqual(
            vector.unpolarized().real, convolution.f1(2, 0.1, 5.0)
        )
        self.assertAlmostEqual(vector.tensor_difference().real, 0.0)
        np.testing.assert_array_equal(pion.axial, 0.0)
        np.testing.assert_array_equal(pion.transverse, 0.0)

    def test_minimal_fock_component_keeps_pion_and_counterterm_identifiable(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        convolution = SpinAveragedPionConvolution(normalized, self.pdf)
        component = build_minimal_fock_consistent_pion_component(
            2, convolution, normalized
        )
        identity = np.eye(3, dtype=complex)
        proton = Spin1QuarkCorrelator(
            2.0 * identity, 0.3 * identity, np.ones((2, 3, 3), dtype=complex)
        )
        neutron = Spin1QuarkCorrelator(
            identity, 0.2 * identity, 2.0 * np.ones((2, 3, 3), dtype=complex)
        )
        correction = component.component(proton, neutron, 0.1, 5.0, "sea")
        fraction = normalized.ledger.pinn_sector_pion_momentum
        pion_f1 = convolution.f1(2, 0.1, 5.0)
        np.testing.assert_allclose(
            correction.vector,
            pion_f1 * identity - fraction * (proton.vector + neutron.vector),
        )
        np.testing.assert_allclose(
            correction.axial, -fraction * (proton.axial + neutron.axial)
        )
        np.testing.assert_allclose(
            correction.transverse,
            -fraction * (proton.transverse + neutron.transverse),
        )
        self.assertIn("temporary", component.uncertainty_description)

    def test_longitudinal_nnpi_recoil_preserves_number_and_removes_exact_momentum(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        recoil = NNPiLongitudinalRecoilConvolution(normalized, nodes=64)
        identity = np.eye(3, dtype=complex)

        def baseline(x):
            scalar = 4.0 * (1.0 - x) ** 3 if 0.0 < x < 1.0 else 0.0
            return Spin1QuarkCorrelator(
                scalar * identity,
                0.3 * scalar * identity,
                np.stack((0.2 * scalar * identity, -0.1 * scalar * identity)),
            )

        nodes, weights = np.polynomial.legendre.leggauss(72)
        x_values = (nodes + 1.0) / 2.0
        x_weights = weights / 2.0
        corrections = [recoil.nucleon_correction(baseline, float(x)) for x in x_values]
        scalar_correction = np.asarray(
            [HelicityMatrix(value.vector).unpolarized().real for value in corrections]
        )
        number_change = float(np.dot(x_weights, scalar_correction))
        momentum_change = float(np.dot(x_weights, x_values * scalar_correction))
        baseline_momentum = 0.2
        expected = (
            -normalized.ledger.pinn_sector_pion_momentum * baseline_momentum
        )
        self.assertAlmostEqual(number_change, 0.0, places=6)
        self.assertAlmostEqual(momentum_change, expected, places=6)

    def test_longitudinal_nnpi_recoil_changes_shape_and_preserves_spin_ratios(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        recoil = NNPiLongitudinalRecoilConvolution(normalized, nodes=64)
        identity = np.eye(3, dtype=complex)

        def baseline(x):
            scalar = (1.0 - x) ** 3 if 0.0 < x < 1.0 else 0.0
            return Spin1QuarkCorrelator(
                scalar * identity,
                0.4 * scalar * identity,
                np.stack((0.25 * scalar * identity, -0.15 * scalar * identity)),
            )

        x = 0.3
        correction = recoil.nucleon_correction(baseline, x)
        unchanged_shape = (
            -normalized.ledger.pinn_sector_pion_momentum * baseline(x).vector
        )
        self.assertFalse(np.allclose(correction.vector, unchanged_shape))
        np.testing.assert_allclose(correction.axial, 0.4 * correction.vector)
        np.testing.assert_allclose(correction.transverse[0], 0.25 * correction.vector)
        np.testing.assert_allclose(correction.transverse[1], -0.15 * correction.vector)

    def test_longitudinal_recoil_component_uses_shifted_baseline_and_is_identifiable(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        convolution = SpinAveragedPionConvolution(normalized, self.pdf)
        recoil = NNPiLongitudinalRecoilConvolution(normalized, nodes=48)
        calls = []
        identity = np.eye(3, dtype=complex)

        def baseline_provider(x, scale, sector):
            calls.append((x, scale, sector))
            scalar = (1.0 - x) ** 2 if 0.0 < x < 1.0 else 0.0
            return Spin1QuarkCorrelator(
                scalar * identity,
                0.2 * scalar * identity,
                np.stack((0.1 * scalar * identity, -0.05 * scalar * identity)),
            )

        component = build_longitudinal_recoil_fock_component(
            2, convolution, recoil, baseline_provider
        )
        local = baseline_provider(0.2, 5.0, "sea")
        zero = Spin1QuarkCorrelator(
            np.zeros((3, 3), dtype=complex),
            np.zeros((3, 3), dtype=complex),
            np.zeros((2, 3, 3), dtype=complex),
        )
        calls.clear()
        resolved = apply_nuclear_corrections(
            proton_impulse=local,
            neutron_impulse=zero,
            x=0.2,
            scale_gev=5.0,
            parton_sector="sea",
            meson_exchange_input=component,
        ).corrections["meson_exchange"]
        self.assertTrue(any(x > 0.2 for x, _, _ in calls))
        self.assertTrue(all(scale == 5.0 and sector == "sea" for _, scale, sector in calls))
        minimal = build_minimal_fock_consistent_pion_component(
            2, convolution, normalized
        ).component(local, zero, 0.2, 5.0, "sea")
        self.assertFalse(np.allclose(resolved.vector, minimal.vector))
        self.assertIn("longitudinal recoil", component.uncertainty_description)

    def test_unintegrated_spin_average_reconstructs_probability_and_nn_recoil_limit(self):
        y = 0.2
        qz2 = (self.splitting.parameters.nucleon_mass_gev * y) ** 2
        upper = self.splitting.parameters.q_max_gev**2 - qz2
        nodes, weights = np.polynomial.legendre.leggauss(180)
        qp2 = upper * (nodes + 1.0) / 2.0
        reconstructed = (
            upper
            / 2.0
            * np.dot(
                weights,
                [
                    self.splitting.spin_averaged_differential(y, float(value))
                    for value in qp2
                ],
            )
        )
        self.assertTrue(
            np.isclose(
                reconstructed,
                self.splitting.spin_averaged_f(y),
                rtol=1.0e-5,
                atol=1.0e-10,
            )
        )
        self.assertEqual(
            self.splitting.spin_averaged_nn_recoil_b(y, 0.4, 0.0),
            self.splitting.spin_averaged_f(y),
        )
        self.assertEqual(
            self.splitting.spin_averaged_nn_recoil_b(y, 0.0, 1.0),
            self.splitting.spin_averaged_f(y),
        )
        self.assertNotEqual(
            self.splitting.spin_averaged_nn_recoil_b(y, 0.4, 1.0),
            self.splitting.spin_averaged_f(y),
        )

    def test_nnpi_bspace_recoil_has_exact_collinear_limit_and_full_spin_transport(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        recoil = NNPiLongitudinalRecoilConvolution(normalized, nodes=48)
        identity = np.eye(3, dtype=complex)

        def baseline_b(x, b):
            scalar = (
                (1.0 - x) ** 3 * np.exp(-0.18 * b**2)
                if 0.0 < x < 1.0 else 0.0
            )
            return Spin1QuarkCorrelator(
                scalar * identity,
                0.35 * scalar * identity,
                np.stack((0.2 * scalar * identity, -0.12 * scalar * identity)),
            )

        def baseline_collinear(x):
            return baseline_b(x, 0.0)

        x = 0.17
        collinear = recoil.nucleon_correction(baseline_collinear, x)
        at_origin = recoil.nucleon_correction_b(baseline_b, x, 0.0)
        np.testing.assert_allclose(at_origin.vector, collinear.vector)
        np.testing.assert_allclose(at_origin.axial, collinear.axial)
        np.testing.assert_allclose(at_origin.transverse, collinear.transverse)
        finite_b = recoil.nucleon_correction_b(baseline_b, x, 1.3)
        self.assertTrue(finite_b.is_target_hermitian())
        self.assertFalse(np.allclose(finite_b.vector, collinear.vector))
        np.testing.assert_allclose(finite_b.axial, 0.35 * finite_b.vector)
        np.testing.assert_allclose(finite_b.transverse[0], 0.2 * finite_b.vector)
        np.testing.assert_allclose(finite_b.transverse[1], -0.12 * finite_b.vector)

    def test_nnpi_bspace_recoil_rejects_negative_impact_parameter(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        recoil = NNPiLongitudinalRecoilConvolution(normalized)
        with self.assertRaisesRegex(ValueError, "impact parameter"):
            recoil.nucleon_correction_b(
                lambda x, b: Spin1QuarkCorrelator(
                    np.eye(3), np.eye(3), np.zeros((2, 3, 3))
                ),
                0.2,
                -0.1,
            )

    def test_nnpi_bspace_recoil_uses_xd_not_xn_in_bessel_fraction(self):
        normalized = FockNormalizedMillerPionDistribution(self.splitting)
        recoil = NNPiLongitudinalRecoilConvolution(normalized, nodes=32)
        calls = []
        identity = np.eye(3, dtype=complex)

        def capture(y, fraction, b):
            calls.append((y, fraction, b))
            return normalized.spin_averaged_f(y)

        with patch.object(
            normalized, "spin_averaged_nn_recoil_b", side_effect=capture
        ):
            recoil.nnpi_nucleon_b(
                lambda shifted_x, b: Spin1QuarkCorrelator(
                    (1.0 - shifted_x) * identity,
                    np.zeros((3, 3)),
                    np.zeros((2, 3, 3)),
                ),
                0.2,
                0.7,
            )
        self.assertEqual(len(calls), 32)
        for y, fraction, b in calls:
            remaining = 1.0 - recoil.pion_deuteron_fraction(y)
            self.assertAlmostEqual(fraction, 0.2 / (2.0 * remaining), places=14)
            self.assertEqual(b, 0.7)


if __name__ == "__main__":
    unittest.main()
