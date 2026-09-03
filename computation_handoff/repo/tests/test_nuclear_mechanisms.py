import unittest

import numpy as np

from deuteron_wigner.nuclear_mechanisms import (
    DiffractiveShadowingInput,
    AdditionalNuclearComponentInput,
    CJ26_ADDITIVE,
    CJ26_MULTIPLICATIVE,
    NuclearCorrectionParameters,
    OffShellModificationInput,
    apply_nuclear_corrections,
    build_polarized_tensor_shadowing_input,
    build_momentum_sum_antishadowing_input,
    default_off_shell_input,
    default_diffractive_shadowing_input,
    longitudinal_coherence_factor,
)
from deuteron_wigner.provenance import EvidenceClass
from deuteron_wigner.provenance import Mechanism, ValidityDomain
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.spin import spin_one_basis


class NuclearMechanismTests(unittest.TestCase):
    def correlator(self, scale):
        basis = spin_one_basis()
        vector = scale * (basis["U"] + 0.1 * basis["LL"])
        axial = scale * (0.2 * basis["L"])
        transverse = np.asarray(
            (scale * 0.1 * basis["T_x"], scale * 0.1 * basis["T_y"])
        )
        return Spin1QuarkCorrelator(vector, axial, transverse)

    def test_mechanisms_are_separate_and_reconstruct_total(self):
        result = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.04,
        )
        self.assertEqual(
            set(result.corrections),
            {
                "coherent_shadowing", "antishadowing", "off_shell",
                "meson_exchange", "non_nucleonic",
            },
        )
        expected = result.impulse.vector.copy()
        for correction in result.corrections.values():
            expected += correction.vector
        np.testing.assert_allclose(result.total.vector, expected)
        self.assertTrue(result.total.is_target_hermitian())
        np.testing.assert_array_equal(
            result.corrections["meson_exchange"].vector, 0.0
        )
        np.testing.assert_array_equal(
            result.corrections["non_nucleonic"].vector, 0.0
        )

    def test_off_shell_component_vanishes_at_zero_virtuality(self):
        result = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.1,
            parameters=NuclearCorrectionParameters(
                average_nucleon_virtuality=0.0
            ),
        )
        np.testing.assert_allclose(result.corrections["off_shell"].vector, 0.0)

    def test_shadowing_uses_replaceable_diffractive_input_and_domain(self):
        calls = []
        input_model = DiffractiveShadowingInput(
            fraction=lambda sector, x, q: calls.append((sector, x, q)) or 0.04,
            source="synthetic DPDF fixture",
            relative_uncertainty=0.2,
            classification=EvidenceClass.PHENOMENOLOGY,
        )
        low_x = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.01, scale_gev=5.0, parton_sector="gluon",
            diffractive_input=input_model,
        )
        self.assertEqual(calls, [("gluon", 0.01, 5.0)])
        self.assertGreater(
            np.linalg.norm(low_x.corrections["coherent_shadowing"].vector), 0.0
        )
        high_x = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.2, scale_gev=5.0, diffractive_input=input_model,
        )
        np.testing.assert_allclose(
            high_x.corrections["coherent_shadowing"].vector, 0.0
        )

    def test_polarized_tensor_shadowing_is_operator_and_irrep_resolved(self):
        base = DiffractiveShadowingInput(
            fraction=lambda sector, x, q: 0.04,
            source="synthetic common diffractive anchor",
            relative_uncertainty=0.2,
            classification=EvidenceClass.PHENOMENOLOGY,
        )
        model = build_polarized_tensor_shadowing_input(
            base,
            vector_ratios={
                "U": 1.0, "L": 0.2, "T": 0.3,
                "LL": 2.0, "LT": 1.2, "TT": 1.4,
            },
            axial_operator_ratio=0.5,
            transverse_operator_ratio=0.75,
        )
        self.assertAlmostEqual(
            model.value("vector", "U", "sea", 0.01, 5.0), 0.04
        )
        self.assertAlmostEqual(
            model.value("axial", "L", "sea", 0.01, 5.0), 0.004
        )
        self.assertAlmostEqual(
            model.value("transverse", "T_x", "sea", 0.01, 5.0), 0.009
        )
        self.assertAlmostEqual(
            model.value("vector", "LL", "sea", 0.01, 5.0), 0.08
        )
        self.assertNotEqual(
            model.value("vector", "LT_x", "sea", 0.01, 5.0),
            model.value("vector", "TT_x", "sea", 0.01, 5.0),
        )

    def test_zero_polarized_shadowing_recovers_impulse_for_every_projection(self):
        zero = DiffractiveShadowingInput(
            fraction=lambda sector, x, q: 0.0,
            source="exact configured zero response",
            relative_uncertainty=0.0,
            classification=EvidenceClass.EXACT,
        )
        result = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.01,
            polarized_shadowing_input=build_polarized_tensor_shadowing_input(zero),
        )
        coherent = result.corrections["coherent_shadowing"]
        np.testing.assert_array_equal(coherent.vector, 0.0)
        np.testing.assert_array_equal(coherent.axial, 0.0)
        np.testing.assert_array_equal(coherent.transverse, 0.0)

    def test_coherence_factor_decreases_with_x(self):
        low = longitudinal_coherence_factor(
            0.005, nucleon_mass_gev=0.9389, radius_fm=1.975
        )
        high = longitudinal_coherence_factor(
            0.08, nucleon_mass_gev=0.9389, radius_fm=1.975
        )
        self.assertGreater(low, high)
        self.assertLessEqual(low, 1.0)

    def test_default_shadowing_reproduces_published_deuteron_anchors(self):
        model = default_diffractive_shadowing_input()
        self.assertAlmostEqual(model.value("sea", 1.0e-2, 5.0), 0.015)
        self.assertAlmostEqual(model.value("valence", 1.0e-5, 5.0), 0.030)
        self.assertEqual(model.value("sea", 0.1, 5.0), 0.0)
        self.assertAlmostEqual(
            model.value("gluon", 1.0e-2, 5.0), 1.5 * 0.015
        )

    def test_off_shell_input_is_replaceable(self):
        calls = []
        model = OffShellModificationInput(
            delta_f=lambda sector, x, q: calls.append((sector, x, q)) or 0.5,
            source="synthetic off-shell fixture",
            relative_uncertainty=0.1,
            classification=EvidenceClass.PHENOMENOLOGY,
        )
        result = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.4, scale_gev=5.0, parton_sector="valence",
            off_shell_input=model,
        )
        self.assertEqual(calls, [("valence", 0.4, 5.0)])
        self.assertGreater(np.linalg.norm(result.corrections["off_shell"].vector), 0)

    def test_cj26_off_shell_central_and_uncertainty_follow_tables(self):
        self.assertAlmostEqual(CJ26_ADDITIVE.value(0.0), -0.474)
        self.assertAlmostEqual(CJ26_MULTIPLICATIVE.value(0.0), -0.408)
        model = default_off_shell_input()
        for x in (0.0, 0.2, 0.5, 0.7):
            expected = 0.5 * (
                CJ26_ADDITIVE.value(x) + CJ26_MULTIPLICATIVE.value(x)
            )
            self.assertAlmostEqual(model.value("valence", x, 5.0), expected)
            self.assertGreater(model.uncertainty(x), 0.0)
        self.assertEqual(model.classification, EvidenceClass.PHENOMENOLOGY)
        self.assertEqual(model.constrained_x_max, 0.7)

    def test_antishadowing_restores_configured_shadowing_momentum(self):
        model = build_momentum_sum_antishadowing_input(
            lambda x, q: x ** 0.3 * (1.0 - x) ** 3,
            scale_gev=5.0,
            parton_sector="sea",
            compensation_fraction=0.8,
        )
        self.assertAlmostEqual(
            model.restored_momentum,
            0.8 * model.lost_momentum,
            places=13,
        )
        self.assertEqual(model.value(0.03, 5.0), 0.0)
        self.assertGreater(model.value(0.12, 5.0), 0.0)

    def test_antishadowing_rejects_failed_sum_rule(self):
        from deuteron_wigner.nuclear_mechanisms import AntishadowingInput

        with self.assertRaises(ValueError):
            AntishadowingInput(
                enhancement=lambda x, q: 0.0,
                source="invalid fixture",
                relative_uncertainty=0.0,
                compensation_fraction=1.0,
                lost_momentum=0.1,
                restored_momentum=0.0,
            )

    def test_source_required_additional_component_is_replaceable(self):
        model = AdditionalNuclearComponentInput(
            component=lambda proton, neutron, x, q, sector: self.correlator(0.03),
            source="synthetic pion convolution fixture",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.MESON_EXCHANGE,
            relative_uncertainty=0.5,
            validity=ValidityDomain(0.01, 0.3, 2.0, 20.0),
        )
        active = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.1, meson_exchange_input=model,
        )
        self.assertGreater(
            np.linalg.norm(active.corrections["meson_exchange"].vector), 0.0
        )
        inactive = apply_nuclear_corrections(
            proton_impulse=self.correlator(1.0),
            neutron_impulse=self.correlator(0.8),
            x=0.5, meson_exchange_input=model,
        )
        np.testing.assert_array_equal(
            inactive.corrections["meson_exchange"].vector, 0.0
        )


if __name__ == "__main__":
    unittest.main()
