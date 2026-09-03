"""Typed soft-subtraction, renormalization, and rapidity-scale contracts."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


class SoftSubtraction(str, Enum):
    """Operator-level soft-factor convention."""

    COLLINS_SQRT_SOFT = "Collins-subtracted sqrt-soft TMD"


class RapidityRegulator(str, Enum):
    """Rapidity regulator used to define the renormalized TMD."""

    DELTA = "delta regulator"


class RapidityPrescription(str, Enum):
    """Choice of evolution path/boundary in the (mu,zeta) plane."""

    ZETA_PRESCRIPTION_CANONICAL_LINE = "zeta prescription; canonical zeta=mu^2 line"


@dataclass(frozen=True)
class TMDScalePoint:
    """One renormalization/rapidity scale point in GeV units."""

    mu_gev: float
    zeta_gev2: float

    def __post_init__(self) -> None:
        if (
            not np.isfinite(self.mu_gev)
            or not np.isfinite(self.zeta_gev2)
            or self.mu_gev <= 0.0
            or self.zeta_gev2 <= 0.0
        ):
            raise ValueError("TMD scales require finite mu>0 and zeta>0")

    @classmethod
    def canonical(cls, mu_gev: float) -> "TMDScalePoint":
        return cls(float(mu_gev), float(mu_gev) ** 2)

    def is_canonical(self, tolerance: float = 1.0e-12) -> bool:
        return bool(
            np.isclose(
                self.zeta_gev2,
                self.mu_gev**2,
                rtol=tolerance,
                atol=0.0,
            )
        )


@dataclass(frozen=True)
class TMDScheme:
    """Complete identifiers needed before TMD components may be composed.

    This contract does not upgrade perturbative accuracy. It prevents a
    boundary defined in one soft/rapidity convention from being silently
    evolved or combined as though it belonged to another.
    """

    soft_subtraction: SoftSubtraction
    rapidity_regulator: RapidityRegulator
    rapidity_prescription: RapidityPrescription
    uv_scheme: str = "MSbar"
    source: str = "arXiv:1706.01473; arXiv:1907.03780"

    def __post_init__(self) -> None:
        if not self.uv_scheme or not self.source:
            raise ValueError("UV scheme and source are required")

    def require_compatible(self, other: "TMDScheme") -> None:
        if self != other:
            raise ValueError(
                "incompatible TMD soft-subtraction/rapidity schemes cannot "
                "be composed or evolved"
            )

    def require_supported_path(
        self, initial: TMDScalePoint, final: TMDScalePoint
    ) -> None:
        if (
            self.rapidity_prescription
            == RapidityPrescription.ZETA_PRESCRIPTION_CANONICAL_LINE
            and (not initial.is_canonical() or not final.is_canonical())
        ):
            raise ValueError(
                "current CSS implementation supports only the canonical "
                "zeta=mu^2 evolution line"
            )

    @property
    def metadata(self) -> dict[str, str]:
        return {
            "soft_subtraction": self.soft_subtraction.value,
            "rapidity_regulator": self.rapidity_regulator.value,
            "rapidity_prescription": self.rapidity_prescription.value,
            "uv_scheme": self.uv_scheme,
            "source": self.source,
        }


DELTA_COLLINS_ZETA_SCHEME = TMDScheme(
    soft_subtraction=SoftSubtraction.COLLINS_SQRT_SOFT,
    rapidity_regulator=RapidityRegulator.DELTA,
    rapidity_prescription=RapidityPrescription.ZETA_PRESCRIPTION_CANONICAL_LINE,
)

