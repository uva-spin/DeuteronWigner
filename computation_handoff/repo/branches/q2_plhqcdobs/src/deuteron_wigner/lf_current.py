"""Spin-1 light-front plus-current helicity amplitudes and angular condition."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


def dirac_pauli_from_sachs(
    *,
    electric: float,
    magnetic: float,
    q2: float,
    mass: float,
) -> tuple[float, float]:
    """Convert space-like Sachs form factors to \(F_1,F_2\)."""

    if q2 < 0.0 or mass <= 0.0:
        raise ValueError("require q2 >= 0 and mass > 0")
    tau = q2 / (4.0 * mass**2)
    return (
        (electric + tau * magnetic) / (1.0 + tau),
        (magnetic - electric) / (1.0 + tau),
    )


def nucleon_plus_current(
    *,
    f1: float,
    f2: float,
    delta_x: float,
    delta_y: float,
    mass: float,
) -> np.ndarray:
    """Normalized Drell-Yan \(J^+/(2p^+)\) in LF helicity space.

    Momenta and mass must share units. The diagonal is helicity conserving
    \(F_1\); the Pauli term flips helicity.
    """

    if mass <= 0.0:
        raise ValueError("mass must be positive")
    q_right = delta_x + 1j * delta_y
    q_left = delta_x - 1j * delta_y
    return np.asarray(
        [
            [f1, -q_left * f2 / (2.0 * mass)],
            [q_right * f2 / (2.0 * mass), f1],
        ],
        dtype=np.complex128,
    )


class CurrentPrescription(str, Enum):
    OMIT_PP = "omit_I++"
    OMIT_P0 = "omit_I+0"
    OMIT_PM = "omit_I+-"
    OMIT_00 = "omit_I00"


class NamedCurrentPrescription(str, Enum):
    GRACH_KONDRATYUK = "GK"
    BRODSKY_HILLER = "BH"

    @property
    def omitted_amplitude(self) -> CurrentPrescription:
        if self == NamedCurrentPrescription.GRACH_KONDRATYUK:
            return CurrentPrescription.OMIT_00
        if self == NamedCurrentPrescription.BRODSKY_HILLER:
            return CurrentPrescription.OMIT_PP
        raise ValueError(f"unsupported named prescription {self}")


@dataclass(frozen=True)
class SpinOnePlusCurrent:
    """Four normalized Drell-Yan-frame amplitudes \(I=J^+/(2P^+)\).

    ``plus_zero`` is \(I_{+0}\). Light-front time reversal gives
    \(I_{0+}=-I_{+0}\) for the real elastic amplitudes used here.
    """

    plus_plus: complex
    plus_zero: complex
    plus_minus: complex
    zero_zero: complex

    @property
    def zero_plus(self) -> complex:
        return -self.plus_zero

    def angular_condition(self, eta: float) -> complex:
        """Carlson-Ji Eq. (4.7), divided by the common \(2P^+\)."""

        if eta < 0.0:
            raise ValueError("eta cannot be negative")
        return (
            (1.0 + 2.0 * eta) * self.plus_plus
            + np.sqrt(8.0 * eta) * self.zero_plus
            + self.plus_minus
            - self.zero_zero
        )

    def relative_angular_violation(self, eta: float) -> float:
        terms = np.asarray(
            [
                (1.0 + 2.0 * eta) * self.plus_plus,
                np.sqrt(8.0 * eta) * self.zero_plus,
                self.plus_minus,
                -self.zero_zero,
            ],
            dtype=np.complex128,
        )
        scale = float(np.sum(np.abs(terms)))
        return 0.0 if scale == 0.0 else float(abs(np.sum(terms)) / scale)


def current_from_form_factors(
    *, eta: float, charge: float, magnetic: float, quadrupole: float
) -> SpinOnePlusCurrent:
    """Construct the covariant spin-1 helicity amplitudes.

    The convention is chosen so that Carlson-Ji Eq. (4.7) is identically
    satisfied, with ``zero_plus=-plus_zero``.
    """

    if eta < 0.0:
        raise ValueError("eta cannot be negative")
    denominator = 1.0 + eta
    plus_plus = (
        charge + eta * magnetic + eta * quadrupole / 3.0
    ) / denominator
    plus_zero = (
        np.sqrt(eta / 2.0)
        * (
            2.0 * charge
            + (eta - 1.0) * magnetic
            + 2.0 * eta * quadrupole / 3.0
        )
        / denominator
    )
    plus_minus = (
        eta
        * (
            charge
            - magnetic
            - (1.0 + 2.0 * eta / 3.0) * quadrupole
        )
        / denominator
    )
    zero_zero = (
        (1.0 - eta) * charge
        + 2.0 * eta * magnetic
        - 2.0 * eta * (1.0 + 2.0 * eta) * quadrupole / 3.0
    ) / denominator
    return SpinOnePlusCurrent(plus_plus, plus_zero, plus_minus, zero_zero)


def dipole_magnetic_completion(
    *,
    eta: float,
    momentum_transfer: float,
    delta_magnetic_moment: float,
    cutoff: float,
) -> SpinOnePlusCurrent:
    """Return a covariant, purely magnetic phenomenological completion.

    The added form factor is
    ``delta_mu / (1 + (momentum_transfer / cutoff)**2)**2``.  This is a
    controlled calibration/sensitivity term, not a microscopic two-body
    current. Momentum transfer and cutoff must use the same units.
    """

    if momentum_transfer < 0.0:
        raise ValueError("momentum_transfer cannot be negative")
    if cutoff <= 0.0:
        raise ValueError("cutoff must be positive")
    delta_gm = delta_magnetic_moment / (
        1.0 + (momentum_transfer / cutoff) ** 2
    ) ** 2
    return current_from_form_factors(
        eta=eta,
        charge=0.0,
        magnetic=delta_gm,
        quadrupole=0.0,
    )


def _coefficient_matrix(eta: float) -> np.ndarray:
    """Rows map (GC,GM,GQ) to (++,+0,+-,00)."""

    if eta <= 0.0:
        raise ValueError("form-factor extraction requires eta > 0")
    denominator = 1.0 + eta
    return np.asarray(
        [
            [1.0, eta, eta / 3.0],
            [
                np.sqrt(eta / 2.0) * 2.0,
                np.sqrt(eta / 2.0) * (eta - 1.0),
                np.sqrt(eta / 2.0) * 2.0 * eta / 3.0,
            ],
            [eta, -eta, -eta * (1.0 + 2.0 * eta / 3.0)],
            [
                1.0 - eta,
                2.0 * eta,
                -2.0 * eta * (1.0 + 2.0 * eta) / 3.0,
            ],
        ],
        dtype=np.float64,
    ) / denominator


def extract_form_factors(
    current: SpinOnePlusCurrent,
    *,
    eta: float,
    prescription: CurrentPrescription,
) -> tuple[complex, complex, complex]:
    """Extract \(G_C,G_M,G_Q\) from any three of the four amplitudes."""

    amplitudes = np.asarray(
        [
            current.plus_plus,
            current.plus_zero,
            current.plus_minus,
            current.zero_zero,
        ],
        dtype=np.complex128,
    )
    omitted = {
        CurrentPrescription.OMIT_PP: 0,
        CurrentPrescription.OMIT_P0: 1,
        CurrentPrescription.OMIT_PM: 2,
        CurrentPrescription.OMIT_00: 3,
    }[prescription]
    keep = np.asarray([index for index in range(4) if index != omitted])
    solution = np.linalg.solve(_coefficient_matrix(eta)[keep], amplitudes[keep])
    return tuple(complex(value) for value in solution)


def prescription_spread(
    current: SpinOnePlusCurrent, *, eta: float
) -> dict[str, tuple[complex, complex, complex]]:
    return {
        prescription.value: extract_form_factors(
            current, eta=eta, prescription=prescription
        )
        for prescription in CurrentPrescription
    }


def extract_named_form_factors(
    current: SpinOnePlusCurrent,
    *,
    eta: float,
    prescription: NamedCurrentPrescription,
) -> tuple[complex, complex, complex]:
    return extract_form_factors(
        current,
        eta=eta,
        prescription=prescription.omitted_amplitude,
    )


def angular_condition_completion(
    current: SpinOnePlusCurrent,
    *,
    eta: float,
    bad_amplitude: CurrentPrescription,
) -> tuple[SpinOnePlusCurrent, complex]:
    """Add the unique one-amplitude correction that restores covariance.

    This is a diagnostic completion, not a dynamical two-body-current model.
    The returned complex number is the correction to the selected amplitude.
    """

    if eta < 0.0:
        raise ValueError("eta cannot be negative")
    residual = current.angular_condition(eta)
    values = {
        "plus_plus": current.plus_plus,
        "plus_zero": current.plus_zero,
        "plus_minus": current.plus_minus,
        "zero_zero": current.zero_zero,
    }
    if bad_amplitude == CurrentPrescription.OMIT_PP:
        correction = -residual / (1.0 + 2.0 * eta)
        values["plus_plus"] += correction
    elif bad_amplitude == CurrentPrescription.OMIT_P0:
        if eta == 0.0:
            raise ValueError("I+0 cannot repair the angular condition at eta=0")
        correction = residual / np.sqrt(8.0 * eta)
        values["plus_zero"] += correction
    elif bad_amplitude == CurrentPrescription.OMIT_PM:
        correction = -residual
        values["plus_minus"] += correction
    elif bad_amplitude == CurrentPrescription.OMIT_00:
        correction = residual
        values["zero_zero"] += correction
    else:
        raise ValueError(f"unsupported bad amplitude {bad_amplitude}")
    completed = SpinOnePlusCurrent(**values)
    return completed, complex(correction)
