import unittest

import numpy as np

from deuteron_wigner.lf_current import (
    CurrentPrescription,
    NamedCurrentPrescription,
    SpinOnePlusCurrent,
    angular_condition_completion,
    current_from_form_factors,
    dipole_magnetic_completion,
    dirac_pauli_from_sachs,
    extract_form_factors,
    extract_named_form_factors,
    nucleon_plus_current,
    prescription_spread,
)


class SpinOneCurrentTests(unittest.TestCase):
    def test_sachs_dirac_pauli_round_trip(self):
        electric, magnetic = 0.73, 1.81
        f1, f2 = dirac_pauli_from_sachs(
            electric=electric, magnetic=magnetic, q2=0.4, mass=0.9389
        )
        tau = 0.4 / (4.0 * 0.9389**2)
        self.assertAlmostEqual(f1 - tau * f2, electric)
        self.assertAlmostEqual(f1 + f2, magnetic)

    def test_nucleon_current_reversal_hermiticity(self):
        positive = nucleon_plus_current(
            f1=0.8, f2=1.2, delta_x=0.3, delta_y=-0.2, mass=0.94
        )
        negative = nucleon_plus_current(
            f1=0.8, f2=1.2, delta_x=-0.3, delta_y=0.2, mass=0.94
        )
        np.testing.assert_allclose(positive.conj().T, negative, atol=0.0)

    def test_covariant_current_satisfies_angular_condition(self):
        current = current_from_form_factors(
            eta=0.17, charge=0.63, magnetic=0.91, quadrupole=4.2
        )
        self.assertAlmostEqual(current.angular_condition(0.17), 0.0, places=14)
        self.assertLess(current.relative_angular_violation(0.17), 2e-16)

    def test_dipole_magnetic_completion_is_prescription_independent(self):
        eta = 0.17
        correction = dipole_magnetic_completion(
            eta=eta,
            momentum_transfer=0.4,
            delta_magnetic_moment=-0.3,
            cutoff=0.5,
        )
        expected = -0.3 / (1.0 + (0.4 / 0.5) ** 2) ** 2
        self.assertAlmostEqual(correction.angular_condition(eta), 0.0, places=14)
        for prescription in CurrentPrescription:
            actual = extract_form_factors(
                correction, eta=eta, prescription=prescription
            )
            np.testing.assert_allclose(actual, [0.0, expected, 0.0], atol=3e-15)

    def test_all_prescriptions_recover_covariant_form_factors(self):
        expected = np.array([0.63, 0.91, 4.2])
        current = current_from_form_factors(
            eta=0.17,
            charge=expected[0],
            magnetic=expected[1],
            quadrupole=expected[2],
        )
        for prescription in CurrentPrescription:
            actual = extract_form_factors(
                current, eta=0.17, prescription=prescription
            )
            np.testing.assert_allclose(actual, expected, atol=3e-15)
        np.testing.assert_allclose(
            extract_named_form_factors(
                current,
                eta=0.17,
                prescription=NamedCurrentPrescription.GRACH_KONDRATYUK,
            ),
            expected,
            atol=3e-15,
        )
        self.assertEqual(
            NamedCurrentPrescription.BRODSKY_HILLER.omitted_amplitude,
            CurrentPrescription.OMIT_PP,
        )

    def test_angular_violation_creates_prescription_spread(self):
        covariant = current_from_form_factors(
            eta=0.17, charge=0.63, magnetic=0.91, quadrupole=4.2
        )
        violated = SpinOnePlusCurrent(
            plus_plus=covariant.plus_plus,
            plus_zero=covariant.plus_zero,
            plus_minus=covariant.plus_minus,
            zero_zero=covariant.zero_zero + 0.03,
        )
        self.assertGreater(violated.relative_angular_violation(0.17), 1e-4)
        results = prescription_spread(violated, eta=0.17)
        charge_values = np.asarray([value[0].real for value in results.values()])
        self.assertGreater(np.ptp(charge_values), 1e-3)
        for bad_amplitude in CurrentPrescription:
            completed, correction = angular_condition_completion(
                violated, eta=0.17, bad_amplitude=bad_amplitude
            )
            self.assertNotEqual(correction, 0.0)
            self.assertAlmostEqual(completed.angular_condition(0.17), 0.0, places=14)

    def test_static_limit(self):
        current = current_from_form_factors(
            eta=0.0, charge=1.0, magnetic=1.7, quadrupole=25.0
        )
        self.assertEqual(current.plus_plus, 1.0)
        self.assertEqual(current.plus_zero, 0.0)
        self.assertEqual(current.plus_minus, 0.0)
        self.assertEqual(current.zero_zero, 1.0)


if __name__ == "__main__":
    unittest.main()
