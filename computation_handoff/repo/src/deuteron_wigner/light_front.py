"""Equal-mass two-nucleon instant-form to light-front mapping.

This module implements the first explicit convention for Eq. (53) of the project
brief. It keeps the flat-measure Jacobian amplitude separate from the optional
normalization used in Eq. (50).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable

import numpy as np

from .conventions import HELICITIES, HELICITY_INDEX, TWO_PI
from .kinematics import require_fraction
from .spin import HelicityMatrix

NUCLEON_HELICITIES = (0.5, -0.5)


class LFNormalization(str, Enum):
    """Supported light-front wave-function integration measures."""

    FLAT = "dy_d2p"
    BRIEF_EQ50 = "dy_d2p_over_2y1my_2pi3"


class SpinRotation(str, Enum):
    MELOSH = "melosh"
    IDENTITY = "identity"


@dataclass(frozen=True)
class InternalMomentum:
    """Equal-mass two-body internal kinematics."""

    y: float
    p_x: float
    p_y: float
    mass: float

    def __post_init__(self) -> None:
        require_fraction(self.y, name="y", closed_upper=False)
        if self.mass <= 0.0:
            raise ValueError("constituent mass must be positive")

    @property
    def p_t_squared(self) -> float:
        return self.p_x**2 + self.p_y**2

    @property
    def invariant_mass(self) -> float:
        return np.sqrt((self.mass**2 + self.p_t_squared) / (self.y * (1.0 - self.y)))

    @property
    def energy(self) -> float:
        return 0.5 * self.invariant_mass

    @property
    def k_z(self) -> float:
        return (self.y - 0.5) * self.invariant_mass

    @property
    def k_magnitude(self) -> float:
        return np.sqrt(self.p_t_squared + self.k_z**2)

    @property
    def dkz_dy(self) -> float:
        """Exact equal-mass Jacobian M0/[4 y(1-y)]."""

        return self.invariant_mass / (4.0 * self.y * (1.0 - self.y))

    @classmethod
    def from_cartesian(
        cls, *, k_z: float, p_x: float, p_y: float, mass: float
    ) -> "InternalMomentum":
        energy = np.sqrt(mass**2 + p_x**2 + p_y**2 + k_z**2)
        y = (energy + k_z) / (2.0 * energy)
        return cls(y=y, p_x=p_x, p_y=p_y, mass=mass)


def melosh_rotation(
    *, fraction: float, p_x: float, p_y: float, mass: float, invariant_mass: float
) -> np.ndarray:
    """Canonical-spin to LF-helicity rotation for one equal-mass constituent.

    R_M = [m+x M0 - i sigma.(z x p_T)] /
          sqrt[(m+x M0)^2+p_T^2].
    """

    require_fraction(fraction, name="constituent fraction", closed_upper=False)
    a = mass + fraction * invariant_mass
    k_left = p_x - 1j * p_y
    k_right = p_x + 1j * p_y
    denominator = np.sqrt(a**2 + p_x**2 + p_y**2)
    return np.array([[a, -k_left], [k_right, a]], dtype=np.complex128) / denominator


def _spherical_harmonic_l2(m: int, k_x: float, k_y: float, k_z: float) -> complex:
    radius = np.sqrt(k_x**2 + k_y**2 + k_z**2)
    if radius == 0.0:
        return 0.0j
    cos_theta = k_z / radius
    sin_theta = np.sqrt(max(0.0, 1.0 - cos_theta**2))
    phi = np.arctan2(k_y, k_x)
    if m == 0:
        return np.sqrt(5.0 / (16.0 * np.pi)) * (3.0 * cos_theta**2 - 1.0)
    if m == 1:
        return (
            -np.sqrt(15.0 / (8.0 * np.pi))
            * sin_theta
            * cos_theta
            * np.exp(1j * phi)
        )
    if m == -1:
        return (
            np.sqrt(15.0 / (8.0 * np.pi))
            * sin_theta
            * cos_theta
            * np.exp(-1j * phi)
        )
    if m == 2:
        return np.sqrt(15.0 / (32.0 * np.pi)) * sin_theta**2 * np.exp(2j * phi)
    if m == -2:
        return np.sqrt(15.0 / (32.0 * np.pi)) * sin_theta**2 * np.exp(-2j * phi)
    raise ValueError("l=2 magnetic quantum number must be between -2 and 2")


_D_COUPLING: dict[int, tuple[tuple[int, int, float], ...]] = {
    1: (
        (0, 1, np.sqrt(10.0) / 10.0),
        (1, 0, -np.sqrt(30.0) / 10.0),
        (2, -1, np.sqrt(15.0) / 5.0),
    ),
    0: (
        (-1, 1, np.sqrt(30.0) / 10.0),
        (0, 0, -np.sqrt(10.0) / 5.0),
        (1, -1, np.sqrt(30.0) / 10.0),
    ),
    -1: (
        (-2, 1, np.sqrt(15.0) / 5.0),
        (-1, 0, -np.sqrt(30.0) / 10.0),
        (0, -1, np.sqrt(10.0) / 10.0),
    ),
}


def _triplet_spin_amplitude(m_s: int, sigma_p: int, sigma_n: int) -> float:
    """Canonical spin coupling <1/2 sigma_p,1/2 sigma_n|1 m_s>.

    Spin indices are 0 for +1/2 and 1 for -1/2.
    """

    if m_s == 1:
        return 1.0 if (sigma_p, sigma_n) == (0, 0) else 0.0
    if m_s == 0:
        return 1.0 / np.sqrt(2.0) if sigma_p != sigma_n else 0.0
    if m_s == -1:
        return 1.0 if (sigma_p, sigma_n) == (1, 1) else 0.0
    raise ValueError("triplet spin projection must be -1, 0, or 1")


def canonical_deuteron_amplitude(
    *,
    deuteron_helicity: int,
    sigma_p: int,
    sigma_n: int,
    k_x: float,
    k_y: float,
    k_z: float,
    u: float,
    w: float,
) -> complex:
    """Instant-form S+D amplitude in the convention of Eq. (52)."""

    if deuteron_helicity not in HELICITIES:
        raise ValueError("deuteron helicity must be +1, 0, or -1")
    if sigma_p not in (0, 1) or sigma_n not in (0, 1):
        raise ValueError("canonical nucleon spin indices must be 0 or 1")
    s_wave = (
        u
        / np.sqrt(4.0 * np.pi)
        * _triplet_spin_amplitude(deuteron_helicity, sigma_p, sigma_n)
    )
    d_wave = 0.0j
    for m_l, m_s, coefficient in _D_COUPLING[deuteron_helicity]:
        d_wave += (
            coefficient
            * _spherical_harmonic_l2(m_l, k_x, k_y, k_z)
            * _triplet_spin_amplitude(m_s, sigma_p, sigma_n)
            * w
        )
    # The reduced tabulated w(k) is Fourier-Bessel transformed without the
    # angular partial-wave phase. The full momentum-space L=2 amplitude carries
    # i**2=-1 relative to L=0.
    return s_wave - d_wave


def light_front_wave_function(
    *,
    y: float,
    p_x: float,
    p_y: float,
    mass: float,
    radial: Callable[[float], tuple[float, float]],
    normalization: LFNormalization = LFNormalization.FLAT,
    spin_rotation: SpinRotation = SpinRotation.MELOSH,
) -> np.ndarray:
    """Return Psi[Lambda,lambda_p,lambda_n] with shape (3,2,2)."""

    internal = InternalMomentum(y=y, p_x=p_x, p_y=p_y, mass=mass)
    u, w = radial(internal.k_magnitude)
    if spin_rotation == SpinRotation.MELOSH:
        proton_rotation = melosh_rotation(
            fraction=y,
            p_x=p_x,
            p_y=p_y,
            mass=mass,
            invariant_mass=internal.invariant_mass,
        )
        neutron_rotation = melosh_rotation(
            fraction=1.0 - y,
            p_x=-p_x,
            p_y=-p_y,
            mass=mass,
            invariant_mass=internal.invariant_mass,
        )
    elif spin_rotation == SpinRotation.IDENTITY:
        proton_rotation = np.eye(2, dtype=np.complex128)
        neutron_rotation = np.eye(2, dtype=np.complex128)
    else:
        raise ValueError(f"unsupported spin rotation {spin_rotation}")
    canonical = np.zeros((3, 2, 2), dtype=np.complex128)
    for helicity in HELICITIES:
        h_index = HELICITY_INDEX[helicity]
        for sigma_p in (0, 1):
            for sigma_n in (0, 1):
                canonical[h_index, sigma_p, sigma_n] = canonical_deuteron_amplitude(
                    deuteron_helicity=helicity,
                    sigma_p=sigma_p,
                    sigma_n=sigma_n,
                    k_x=p_x,
                    k_y=p_y,
                    k_z=internal.k_z,
                    u=float(u),
                    w=float(w),
                )
    rotated = np.einsum(
        "as,bt,Hst->Hab", proton_rotation, neutron_rotation, canonical
    )
    amplitude = np.sqrt(internal.dkz_dy) * rotated
    if normalization == LFNormalization.BRIEF_EQ50:
        amplitude *= np.sqrt(2.0 * y * (1.0 - y) * TWO_PI**3)
    elif normalization != LFNormalization.FLAT:
        raise ValueError(f"unsupported LF normalization {normalization}")
    return amplitude


def nucleon_momentum_density(wave_function: np.ndarray) -> HelicityMatrix:
    """Trace active and spectator helicities to form rho[Lambda',Lambda]."""

    wave = np.asarray(wave_function, dtype=np.complex128)
    if wave.shape != (3, 2, 2):
        raise ValueError("light-front wave function must have shape (3,2,2)")
    density = np.einsum("Hab,Iab->IH", wave, wave.conj())
    return HelicityMatrix(density)


def active_nucleon_spin_density(wave_function: np.ndarray) -> np.ndarray:
    """Return S[Lambda',Lambda,lambda',lambda] after tracing the spectator.

    The combined target/active-nucleon matrix is Hermitian and positive
    semidefinite. Tracing the final two indices reproduces
    :func:`nucleon_momentum_density`.
    """

    wave = np.asarray(wave_function, dtype=np.complex128)
    if wave.shape != (3, 2, 2):
        raise ValueError("light-front wave function must have shape (3,2,2)")
    return np.einsum("Icb,Hab->IHca", wave.conj(), wave)


def project_active_nucleon_density(
    density: np.ndarray, *, target_channel: str
) -> np.ndarray:
    """Project the target indices while retaining the active 2x2 spin matrix."""

    values = np.asarray(density, dtype=np.complex128)
    if values.shape != (3, 3, 2, 2):
        raise ValueError("active density must have shape (3,3,2,2)")
    diagonal = np.diagonal(values, axis1=0, axis2=1)
    # np.diagonal places the target diagonal last: (2,2,3), ordered +,0,-.
    if target_channel == "U":
        return np.sum(diagonal, axis=-1) / 3.0
    if target_channel == "LL":
        return diagonal[..., 1] - 0.5 * (
            diagonal[..., 0] + diagonal[..., 2]
        )
    raise ValueError("target_channel must be 'U' or 'LL'")


def off_forward_nucleon_density(
    *,
    y: float,
    p_x: float,
    p_y: float,
    delta_x: float,
    delta_y: float,
    mass: float,
    radial: Callable[[float], tuple[float, float]],
    normalization: LFNormalization = LFNormalization.FLAT,
) -> np.ndarray:
    """Zero-skewness active-nucleon overlap rho[Lambda',Lambda].

    The active-constituent symmetric-frame shifts are
    p'_T = p_T + (1-y) Delta_T/2 and
    p_T  = p_T - (1-y) Delta_T/2, following Eq. (59).

    At nonzero transfer this transition matrix need not be Hermitian at fixed
    Delta; it obeys rho(Delta)^\dagger = rho(-Delta).
    """

    require_fraction(y, name="y", closed_upper=False)
    shift_x = 0.5 * (1.0 - y) * delta_x
    shift_y = 0.5 * (1.0 - y) * delta_y
    outgoing = light_front_wave_function(
        y=y,
        p_x=p_x + shift_x,
        p_y=p_y + shift_y,
        mass=mass,
        radial=radial,
        normalization=normalization,
    )
    incoming = light_front_wave_function(
        y=y,
        p_x=p_x - shift_x,
        p_y=p_y - shift_y,
        mass=mass,
        radial=radial,
        normalization=normalization,
    )
    return np.einsum("Iab,Hab->IH", outgoing.conj(), incoming)


def off_forward_active_nucleon_density(
    *,
    y: float,
    p_x: float,
    p_y: float,
    delta_x: float,
    delta_y: float,
    mass: float,
    radial: Callable[[float], tuple[float, float]],
    normalization: LFNormalization = LFNormalization.FLAT,
) -> np.ndarray:
    """Off-forward S[Lambda',Lambda,lambda',lambda] with spectator traced."""

    require_fraction(y, name="y", closed_upper=False)
    shift_x = 0.5 * (1.0 - y) * delta_x
    shift_y = 0.5 * (1.0 - y) * delta_y
    outgoing = light_front_wave_function(
        y=y,
        p_x=p_x + shift_x,
        p_y=p_y + shift_y,
        mass=mass,
        radial=radial,
        normalization=normalization,
    )
    incoming = light_front_wave_function(
        y=y,
        p_x=p_x - shift_x,
        p_y=p_y - shift_y,
        mass=mass,
        radial=radial,
        normalization=normalization,
    )
    return np.einsum("Icb,Hab->IHca", outgoing.conj(), incoming)


def off_forward_active_component_densities(
    *,
    y: float,
    p_x: float,
    p_y: float,
    delta_x: float,
    delta_y: float,
    mass: float,
    radial: Callable[[float], tuple[float, float]],
    normalization: LFNormalization = LFNormalization.FLAT,
    spin_rotation: SpinRotation = SpinRotation.MELOSH,
) -> dict[str, np.ndarray]:
    """Return coherent SS, SD, DS, and DD retained-spin overlaps.

    The first letter labels the outgoing (complex-conjugated) wave-function
    component and the second labels the incoming component.
    """

    require_fraction(y, name="y", closed_upper=False)
    shift_x = 0.5 * (1.0 - y) * delta_x
    shift_y = 0.5 * (1.0 - y) * delta_y
    component_radials = {
        "S": lambda k: (radial(k)[0], 0.0),
        "D": lambda k: (0.0, radial(k)[1]),
    }
    outgoing = {}
    incoming = {}
    for label, component_radial in component_radials.items():
        outgoing[label] = light_front_wave_function(
            y=y,
            p_x=p_x + shift_x,
            p_y=p_y + shift_y,
            mass=mass,
            radial=component_radial,
            normalization=normalization,
            spin_rotation=spin_rotation,
        )
        incoming[label] = light_front_wave_function(
            y=y,
            p_x=p_x - shift_x,
            p_y=p_y - shift_y,
            mass=mass,
            radial=component_radial,
            normalization=normalization,
            spin_rotation=spin_rotation,
        )
    return {
        outgoing_label + incoming_label: np.einsum(
            "Icb,Hab->IHca",
            outgoing[outgoing_label].conj(),
            incoming[incoming_label],
        )
        for outgoing_label in ("S", "D")
        for incoming_label in ("S", "D")
    }
