import unittest

import numpy as np

from deuteron_wigner.covariant_current import (
    extract_lps_form_factors,
    hermitian_lps_current,
    lps_longitudinal_kinematics,
    lps_nucleon_current_kernels,
    lps_hermiticity_transform,
    spin_one_rotation_x_pi,
)


class CovariantCurrentTests(unittest.TestCase):
    def test_longitudinal_kinematics_preserves_spectator_plus_momentum(self):
        fraction, q, mass = 0.37, 0.4, 1.8756
        fraction_prime, k_plus, k_prime_plus, tau = (
            lps_longitudinal_kinematics(
                fraction=fraction,
                momentum_transfer=q,
                deuteron_mass=mass,
            )
        )
        self.assertAlmostEqual(
            (1.0 - fraction) * k_plus,
            (1.0 - fraction_prime) * k_prime_plus,
        )
        self.assertAlmostEqual(tau, q**2 / (4.0 * mass**2))

    def test_nucleon_kernels_have_correct_zero_transfer_limit(self):
        plus, transverse_x, q_n_squared = lps_nucleon_current_kernels(
            fraction=0.37,
            k_x=0.21,
            k_y=-0.13,
            momentum_transfer=0.0,
            nucleon_mass=0.9389,
            deuteron_mass=1.8756,
            electric=0.8,
            magnetic=1.7,
        )
        np.testing.assert_allclose(plus, 0.8 * np.eye(2), atol=2e-15)
        np.testing.assert_allclose(transverse_x, 2.0 * 0.21 * 0.8 * np.eye(2), atol=2e-15)
        self.assertEqual(q_n_squared, 0.0)

    def test_nucleon_kernel_electric_magnetic_decomposition_is_linear(self):
        arguments = dict(
            fraction=0.37,
            k_x=0.21,
            k_y=-0.13,
            momentum_transfer=0.4,
            nucleon_mass=0.9389,
            deuteron_mass=1.8756,
        )
        total = lps_nucleon_current_kernels(
            **arguments, electric=0.8, magnetic=1.7
        )
        electric = lps_nucleon_current_kernels(
            **arguments, electric=0.8, magnetic=0.0
        )
        magnetic = lps_nucleon_current_kernels(
            **arguments, electric=0.0, magnetic=1.7
        )
        np.testing.assert_allclose(total[0], electric[0] + magnetic[0], atol=2e-15)
        np.testing.assert_allclose(total[1], electric[1] + magnetic[1], atol=2e-15)
        self.assertEqual(total[2], electric[2])
        self.assertEqual(total[2], magnetic[2])

    def test_spin_one_pi_rotation_is_unitary_and_involutory(self):
        rotation = spin_one_rotation_x_pi()
        np.testing.assert_allclose(rotation @ rotation.conj().T, np.eye(3), atol=2e-15)
        np.testing.assert_allclose(rotation @ rotation, np.eye(3), atol=2e-15)

    def test_lps_completion_enforces_hermiticity_and_current_conservation(self):
        rng = np.random.default_rng(20260724)
        free = rng.normal(size=(4, 3, 3)) + 1j * rng.normal(size=(4, 3, 3))
        completed = hermitian_lps_current(free)
        np.testing.assert_allclose(
            completed, lps_hermiticity_transform(completed), atol=2e-15
        )
        np.testing.assert_allclose(completed[0], completed[1], atol=2e-15)

    def test_lps_extraction_recovers_synthetic_form_factors(self):
        q, mass = 0.4, 1.8756
        tau = q**2 / (4.0 * mass**2)
        zeta = 1.0 / (np.sqrt(2.0) * mass * np.sqrt(1.0 + tau))
        expected = np.asarray([0.7, 1.3, 12.0])
        current = np.zeros((4, 3, 3), dtype=np.complex128)
        current[0, 0, 0] = (expected[0] - 2.0 * tau * expected[2] / 3.0) / zeta
        current[0, 1, 1] = (expected[0] + 4.0 * tau * expected[2] / 3.0) / zeta
        current[2, 0, 1] = np.sqrt(tau) * expected[1] / zeta
        current[2, 1, 0] = -np.sqrt(tau) * expected[1] / zeta
        np.testing.assert_allclose(
            extract_lps_form_factors(
                current, momentum_transfer=q, deuteron_mass=mass
            ),
            expected,
            atol=2e-15,
        )


if __name__ == "__main__":
    unittest.main()
