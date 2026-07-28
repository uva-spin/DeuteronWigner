"""Poincare-covariant spin-1 current scaffold in the longitudinal Breit frame.

The construction follows Lev, Pace, and Salme, Phys. Rev. C 62, 064004
(2000), Eqs. (11), (14), and (21).  Component order is (+, -, x, y), and
spin order is canonical m=(+1, 0, -1) along the Breit-frame z axis.
"""

from __future__ import annotations

import numpy as np


def lps_longitudinal_kinematics(
    *,
    fraction: float,
    momentum_transfer: float,
    deuteron_mass: float,
) -> tuple[float, float, float, float]:
    """Return ``(fraction_prime, K_plus, K_prime_plus, tau)`` from LPS Eq. (45)."""

    if not 0.0 < fraction < 1.0:
        raise ValueError("fraction must lie in (0,1)")
    if momentum_transfer < 0.0 or deuteron_mass <= 0.0:
        raise ValueError("require nonnegative transfer and positive mass")
    half_transfer = 0.5 * momentum_transfer
    energy = np.sqrt(deuteron_mass**2 + half_transfer**2)
    k_plus = (energy - half_transfer) / np.sqrt(2.0)
    k_prime_plus = (energy + half_transfer) / np.sqrt(2.0)
    fraction_prime = 1.0 + (fraction - 1.0) * k_plus / k_prime_plus
    tau = momentum_transfer**2 / (4.0 * deuteron_mass**2)
    return fraction_prime, k_plus, k_prime_plus, tau


def lps_nucleon_current_kernels(
    *,
    fraction: float,
    k_x: float,
    k_y: float,
    momentum_transfer: float,
    nucleon_mass: float,
    deuteron_mass: float,
    electric: float,
    magnetic: float,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return the active-nucleon ``(J+, Jx, q_N^2)`` kernels.

    This implements the spin matrices inside LPS Eqs. (42)-(46). The returned
    invariant transfer ``q_N^2`` is positive and denotes ``-(p'-p)^2``.
    """

    if nucleon_mass <= 0.0:
        raise ValueError("nucleon_mass must be positive")
    fraction_prime, k_plus, k_prime_plus, tau = lps_longitudinal_kinematics(
        fraction=fraction,
        momentum_transfer=momentum_transfer,
        deuteron_mass=deuteron_mass,
    )
    ratio = k_prime_plus * fraction_prime / (k_plus * fraction)
    root = np.sqrt(ratio)
    a = root + 1.0 / root
    b = root - 1.0 / root
    k_perp_squared = k_x**2 + k_y**2
    denominator = a**2 * nucleon_mass**2 + b**2 * k_perp_squared
    sigma_x = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    sigma_y = np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
    sigma_z = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    identity = np.eye(2, dtype=np.complex128)
    common = (
        a * nucleon_mass * identity
        + 1j * b * (k_x * sigma_x + k_y * sigma_y)
    )
    plus = (
        a
        * nucleon_mass
        * (electric - magnetic)
        * common
        / denominator
        + magnetic * identity
    )
    transverse_x = (
        4.0
        * nucleon_mass
        * k_x
        * (electric - magnetic)
        * common
        / denominator
        + magnetic
        * (
            a * k_x * identity
            + 1j * b * (nucleon_mass * sigma_y + k_y * sigma_z)
        )
    )
    q_n_squared = (
        4.0
        * tau
        * (nucleon_mass**2 + k_perp_squared)
        / (fraction * fraction_prime)
    )
    return plus, transverse_x, float(q_n_squared)


def spin_one_rotation_x_pi() -> np.ndarray:
    """Return ``exp(i*pi*S_x)`` in the canonical spin-one basis."""

    spin_x = np.asarray(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
        dtype=np.complex128,
    ) / np.sqrt(2.0)
    eigenvalues, eigenvectors = np.linalg.eigh(spin_x)
    return (eigenvectors * np.exp(1j * np.pi * eigenvalues)) @ eigenvectors.conj().T


def hermitian_lps_current(free_current: np.ndarray) -> np.ndarray:
    """Apply the Lev-Pace-Salme Hermitian current construction.

    ``free_current`` has shape ``(4, 3, 3)`` and components ``(+, -, x, y)``.
    Following their Eq. (14), the auxiliary minus component is first set equal
    to the plus component. The returned current satisfies their Eq. (10) and
    elastic current conservation ``j- = j+``.
    """

    candidate = np.asarray(free_current, dtype=np.complex128)
    if candidate.shape != (4, 3, 3):
        raise ValueError("free_current must have shape (4, 3, 3)")
    candidate = candidate.copy()
    candidate[1] = candidate[0]
    rotation = spin_one_rotation_x_pi()
    rotated_adjoint = np.asarray(
        [
            rotation @ component.conj().T @ rotation.conj().T
            for component in candidate
        ]
    )
    # A pi rotation about x interchanges + and - and changes the sign of y.
    transformed = rotated_adjoint[[1, 0, 2, 3]].copy()
    transformed[3] *= -1.0
    return 0.5 * (candidate + transformed)


def lps_hermiticity_transform(current: np.ndarray) -> np.ndarray:
    """Right-hand side of the elastic LPS Hermiticity constraint."""

    values = np.asarray(current, dtype=np.complex128)
    if values.shape != (4, 3, 3):
        raise ValueError("current must have shape (4, 3, 3)")
    rotation = spin_one_rotation_x_pi()
    rotated_adjoint = np.asarray(
        [rotation @ component.conj().T @ rotation.conj().T for component in values]
    )
    transformed = rotated_adjoint[[1, 0, 2, 3]].copy()
    transformed[3] *= -1.0
    return transformed


def extract_lps_form_factors(
    current: np.ndarray,
    *,
    momentum_transfer: float,
    deuteron_mass: float,
) -> tuple[complex, complex, complex]:
    """Extract ``(GC, GM, GQ)`` from the free auxiliary current, LPS Eq. (21).

    Momentum transfer and mass must have the same units. The input current uses
    the unnormalized free-current matrix-element convention of that equation,
    before applying :func:`hermitian_lps_current`.
    """

    values = np.asarray(current, dtype=np.complex128)
    if values.shape != (4, 3, 3):
        raise ValueError("current must have shape (4, 3, 3)")
    if momentum_transfer <= 0.0 or deuteron_mass <= 0.0:
        raise ValueError("momentum_transfer and deuteron_mass must be positive")
    tau = momentum_transfer**2 / (4.0 * deuteron_mass**2)
    # LPS define zeta^{-1} = sqrt(2) M sqrt(1+tau).
    zeta = 1.0 / (np.sqrt(2.0) * deuteron_mass * np.sqrt(1.0 + tau))
    j_plus_11 = values[0, 0, 0]
    j_plus_00 = values[0, 1, 1]
    jx_10 = values[2, 0, 1]
    jx_01 = values[2, 1, 0]
    return (
        zeta * (2.0 * j_plus_11 + j_plus_00) / 3.0,
        zeta * (jx_10 - jx_01) / (2.0 * np.sqrt(tau)),
        zeta * (j_plus_00 - j_plus_11) / (2.0 * tau),
    )
