"""Tests for the first instant-form to light-front mapping convention."""

import unittest

import numpy as np

from deuteron_wigner.light_front import (
    InternalMomentum,
    LFNormalization,
    SpinRotation,
    active_nucleon_spin_density,
    canonical_deuteron_amplitude,
    light_front_wave_function,
    melosh_rotation,
    nucleon_momentum_density,
    off_forward_active_nucleon_density,
    off_forward_active_component_densities,
    off_forward_nucleon_density,
    project_active_nucleon_density,
)


def gaussian_s_wave(k: float) -> tuple[float, float]:
    return float(np.exp(-0.5 * k**2)), 0.0


class InternalKinematicsTests(unittest.TestCase):
    def test_cartesian_fraction_round_trip(self) -> None:
        original_kz = -0.37
        internal = InternalMomentum.from_cartesian(
            k_z=original_kz, p_x=0.21, p_y=-0.13, mass=0.9389
        )
        self.assertAlmostEqual(internal.k_z, original_kz, places=14)
        self.assertAlmostEqual(
            internal.energy,
            np.sqrt(0.9389**2 + 0.21**2 + 0.13**2 + original_kz**2),
        )

    def test_jacobian_against_finite_difference(self) -> None:
        internal = InternalMomentum(y=0.37, p_x=0.2, p_y=-0.1, mass=0.9389)
        step = 1e-6
        plus = InternalMomentum(y=internal.y + step, p_x=0.2, p_y=-0.1, mass=0.9389)
        minus = InternalMomentum(y=internal.y - step, p_x=0.2, p_y=-0.1, mass=0.9389)
        numerical = (plus.k_z - minus.k_z) / (2.0 * step)
        self.assertAlmostEqual(internal.dkz_dy, numerical, delta=2e-10)


class MeloshTests(unittest.TestCase):
    def test_rotation_is_unitary(self) -> None:
        internal = InternalMomentum(y=0.31, p_x=0.22, p_y=-0.17, mass=0.9389)
        rotation = melosh_rotation(
            fraction=internal.y,
            p_x=internal.p_x,
            p_y=internal.p_y,
            mass=internal.mass,
            invariant_mass=internal.invariant_mass,
        )
        np.testing.assert_allclose(rotation @ rotation.conj().T, np.eye(2), atol=2e-15)

    def test_rotation_is_identity_at_symmetric_origin(self) -> None:
        internal = InternalMomentum(y=0.5, p_x=0.0, p_y=0.0, mass=0.9389)
        rotation = melosh_rotation(
            fraction=internal.y,
            p_x=0.0,
            p_y=0.0,
            mass=internal.mass,
            invariant_mass=internal.invariant_mass,
        )
        np.testing.assert_allclose(rotation, np.eye(2), atol=0.0)


class LightFrontWaveFunctionTests(unittest.TestCase):
    def test_canonical_s_d_angular_normalization(self) -> None:
        # For every deuteron helicity, angular integration and the canonical
        # nucleon-spin sum return |u|^2+|w|^2.
        u, w = 0.73, -0.21
        cos_nodes, cos_weights = np.polynomial.legendre.leggauss(20)
        phi_nodes = np.linspace(0.0, 2.0 * np.pi, 40, endpoint=False)
        phi_weight = 2.0 * np.pi / len(phi_nodes)
        overlaps = np.zeros((3, 3), dtype=np.complex128)
        for cos_theta, cos_weight in zip(cos_nodes, cos_weights):
            sin_theta = np.sqrt(1.0 - cos_theta**2)
            for phi in phi_nodes:
                amplitudes = np.zeros((3, 2, 2), dtype=np.complex128)
                for h_index, helicity in enumerate((1, 0, -1)):
                    for sigma_p in (0, 1):
                        for sigma_n in (0, 1):
                            amplitudes[h_index, sigma_p, sigma_n] = (
                                canonical_deuteron_amplitude(
                                    deuteron_helicity=helicity,
                                    sigma_p=sigma_p,
                                    sigma_n=sigma_n,
                                    k_x=sin_theta * np.cos(phi),
                                    k_y=sin_theta * np.sin(phi),
                                    k_z=cos_theta,
                                    u=u,
                                    w=w,
                                )
                            )
                overlaps += (
                    cos_weight
                    * phi_weight
                    * np.einsum("Hab,Iab->IH", amplitudes, amplitudes.conj())
                )
        np.testing.assert_allclose(overlaps, (u**2 + w**2) * np.eye(3), atol=2e-14)

    def test_s_wave_spin_coupling_at_symmetric_origin(self) -> None:
        wave = light_front_wave_function(
            y=0.5,
            p_x=0.0,
            p_y=0.0,
            mass=0.9389,
            radial=gaussian_s_wave,
        )
        # Lambda=+1 is the first helicity and couples only to up-up.
        self.assertNotEqual(wave[0, 0, 0], 0.0)
        np.testing.assert_allclose(wave[0, 0, 1:], 0.0)
        np.testing.assert_allclose(wave[0, 1, :], 0.0)
        # Lambda=0 is the symmetric up-down + down-up triplet.
        self.assertAlmostEqual(wave[1, 0, 1], wave[1, 1, 0])
        self.assertEqual(wave[1, 0, 0], 0.0)
        self.assertEqual(wave[1, 1, 1], 0.0)

    def test_d_wave_carries_l2_fourier_phase(self) -> None:
        amplitude = canonical_deuteron_amplitude(
            deuteron_helicity=1,
            sigma_p=0,
            sigma_n=0,
            k_x=0.0,
            k_y=0.0,
            k_z=1.0,
            u=0.0,
            w=1.0,
        )
        self.assertLess(amplitude.real, 0.0)
        self.assertAlmostEqual(amplitude.imag, 0.0)

    def test_density_is_hermitian_positive_semidefinite(self) -> None:
        wave = light_front_wave_function(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        density = nucleon_momentum_density(wave)
        self.assertTrue(density.is_hermitian())
        self.assertTrue(density.is_positive_semidefinite(tolerance=2e-14))

    def test_active_nucleon_density_trace_and_positivity(self) -> None:
        wave = light_front_wave_function(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        active = active_nucleon_spin_density(wave)
        traced = np.trace(active, axis1=2, axis2=3)
        np.testing.assert_allclose(
            traced, nucleon_momentum_density(wave).values, atol=2e-15
        )
        combined = active.transpose(0, 2, 1, 3).reshape(6, 6)
        np.testing.assert_allclose(combined, combined.conj().T, atol=2e-15)
        self.assertGreaterEqual(np.linalg.eigvalsh(combined).min(), -2e-14)

    def test_active_target_projections_reproduce_scalar_channels(self) -> None:
        wave = light_front_wave_function(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        active = active_nucleon_spin_density(wave)
        target = nucleon_momentum_density(wave)
        self.assertAlmostEqual(
            np.trace(project_active_nucleon_density(active, target_channel="U")),
            target.unpolarized(),
        )
        self.assertAlmostEqual(
            np.trace(project_active_nucleon_density(active, target_channel="LL")),
            target.tensor_difference(),
        )

    def test_normalization_adapter_changes_only_measure_factor(self) -> None:
        arguments = dict(
            y=0.43,
            p_x=0.12,
            p_y=0.07,
            mass=0.9389,
            radial=gaussian_s_wave,
        )
        flat = light_front_wave_function(**arguments, normalization=LFNormalization.FLAT)
        brief = light_front_wave_function(
            **arguments, normalization=LFNormalization.BRIEF_EQ50
        )
        expected = np.sqrt(
            2.0 * arguments["y"] * (1.0 - arguments["y"]) * (2.0 * np.pi) ** 3
        )
        np.testing.assert_allclose(brief, expected * flat, atol=2e-15)

    def test_identity_spin_rotation_is_available_as_diagnostic(self) -> None:
        arguments = dict(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        melosh = light_front_wave_function(
            **arguments, spin_rotation=SpinRotation.MELOSH
        )
        identity = light_front_wave_function(
            **arguments, spin_rotation=SpinRotation.IDENTITY
        )
        self.assertGreater(np.max(np.abs(melosh - identity)), 1e-4)
        np.testing.assert_allclose(
            np.trace(nucleon_momentum_density(melosh).values),
            np.trace(nucleon_momentum_density(identity).values),
            atol=2e-14,
        )

    def test_off_forward_overlap_reduces_to_forward_density(self) -> None:
        arguments = dict(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        wave = light_front_wave_function(**arguments)
        forward = nucleon_momentum_density(wave).values
        overlap = off_forward_nucleon_density(
            **arguments, delta_x=0.0, delta_y=0.0
        )
        np.testing.assert_allclose(overlap, forward, atol=2e-15)

    def test_off_forward_hermiticity_relation(self) -> None:
        arguments = dict(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        positive = off_forward_nucleon_density(
            **arguments, delta_x=0.17, delta_y=-0.09
        )
        negative = off_forward_nucleon_density(
            **arguments, delta_x=-0.17, delta_y=0.09
        )
        np.testing.assert_allclose(positive.conj().T, negative, atol=2e-15)

    def test_off_forward_active_trace_and_hermiticity(self) -> None:
        arguments = dict(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
        )
        positive = off_forward_active_nucleon_density(
            **arguments, delta_x=0.17, delta_y=-0.09
        )
        negative = off_forward_active_nucleon_density(
            **arguments, delta_x=-0.17, delta_y=0.09
        )
        scalar = off_forward_nucleon_density(
            **arguments, delta_x=0.17, delta_y=-0.09
        )
        np.testing.assert_allclose(
            np.trace(positive, axis1=2, axis2=3), scalar, atol=2e-15
        )
        conjugate_transpose = positive.conj().transpose(1, 0, 3, 2)
        np.testing.assert_allclose(conjugate_transpose, negative, atol=2e-15)

    def test_off_forward_components_reconstruct_full_overlap(self) -> None:
        arguments = dict(
            y=0.41,
            p_x=0.23,
            p_y=-0.18,
            mass=0.9389,
            radial=lambda k: (np.exp(-k**2), 0.12 * k**2 * np.exp(-k**2)),
            delta_x=0.17,
            delta_y=-0.09,
        )
        components = off_forward_active_component_densities(**arguments)
        full = off_forward_active_nucleon_density(**arguments)
        np.testing.assert_allclose(sum(components.values()), full, atol=3e-15)


if __name__ == "__main__":
    unittest.main()
