"""Scheme-explicit LO b-space boundaries for rank-zero quark TMDs.

The implemented boundary is deliberately restricted to the T-even,
rank-zero functions f1, g1, and h1.  It combines their collinear input with
the exact two-dimensional Fourier transform of the flavor-dependent Gaussian
used by :mod:`nucleon_quark_correlator`.  Rank-one/rank-two and T-odd
functions require different tensor transforms or fit-native evolution and
are rejected rather than silently treated as rank zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from .gluon_tmd_matching import CF
from .nucleon_quark_correlator import FlavorResolvedNucleonQuarkModel
from .tmd_scheme import DELTA_COLLINS_ZETA_SCHEME, TMDScheme

SUPPORTED_RANK_ZERO = ("f1", "g1", "h1")


class QuarkLargeBProfile(str, Enum):
    """Named extra large-b sensitivities, separate from intrinsic widths."""

    NONE = "none"
    LOW = "low"
    CENTRAL = "central"
    HIGH = "high"


@dataclass(frozen=True)
class QuarkTMDMatchingConfig:
    """LO matching and optional additional large-b profile."""

    profile: QuarkLargeBProfile = QuarkLargeBProfile.NONE
    b_max: float = 1.5
    g2_low: float = 0.02
    g2_central: float = 0.05
    g2_high: float = 0.10
    scheme: TMDScheme = DELTA_COLLINS_ZETA_SCHEME

    def __post_init__(self) -> None:
        if self.b_max <= 0.0:
            raise ValueError("b_max must be positive")
        if min(self.g2_low, self.g2_central, self.g2_high) < 0.0:
            raise ValueError("large-b coefficients cannot be negative")
        if not self.g2_low <= self.g2_central <= self.g2_high:
            raise ValueError("large-b coefficients must be ordered")

    @property
    def g2(self) -> float:
        return {
            QuarkLargeBProfile.NONE: 0.0,
            QuarkLargeBProfile.LOW: self.g2_low,
            QuarkLargeBProfile.CENTRAL: self.g2_central,
            QuarkLargeBProfile.HIGH: self.g2_high,
        }[self.profile]


@dataclass(frozen=True)
class BSpaceQuarkTMDValue:
    name: str
    value: float
    collinear_value: float
    intrinsic_factor: float
    profile_factor: float
    width_gev2: float
    b: float
    b_star: float
    scale: float


@dataclass(frozen=True)
class MatchedRankZeroQuarkTMD:
    """LO rank-zero boundary backed by a flavor-resolved nucleon model."""

    nucleon: FlavorResolvedNucleonQuarkModel
    config: QuarkTMDMatchingConfig = QuarkTMDMatchingConfig()

    def b_star(self, b: float) -> float:
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        return float(b / np.sqrt(1.0 + (b / self.config.b_max) ** 2))

    def value(
        self,
        name: str,
        flavor: int,
        x: float,
        b: float,
        scale: float,
    ) -> BSpaceQuarkTMDValue:
        if name not in SUPPORTED_RANK_ZERO:
            raise ValueError(
                f"{name!r} is not a supported rank-zero T-even boundary; "
                "use a tensor-rank or fit-native adapter"
            )
        if not 0.0 < x <= 1.0 or scale <= 0.0 or b < 0.0:
            raise ValueError("require 0<x<=1, positive scale, and b>=0")
        component = self.nucleon.components[name]
        if component.momentum_value is not None:
            raise ValueError(
                f"{name} has a fit-native momentum representation and cannot "
                "be replaced by the Gaussian b-space adapter"
            )
        width = component.width(flavor)
        collinear = float(component.value(flavor, x, scale))
        intrinsic = float(np.exp(-width * b**2 / 4.0))
        profile = float(np.exp(-self.config.g2 * b**2))
        return BSpaceQuarkTMDValue(
            name=name,
            value=collinear * intrinsic * profile,
            collinear_value=collinear,
            intrinsic_factor=intrinsic,
            profile_factor=profile,
            width_gev2=width,
            b=float(b),
            b_star=self.b_star(b),
            scale=float(scale),
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "space": "b_T",
            "b_unit": "GeV^-1",
            "scheme": self.config.scheme.metadata,
            "boundary_construction": (
                "LO collinear matching plus exact intrinsic-Gaussian transform"
            ),
            "supported": list(SUPPORTED_RANK_ZERO),
            "matching_accuracy": {name: "tree" for name in SUPPORTED_RANK_ZERO},
            "color_representation": "fundamental",
            "C_F": CF,
            "large_b_profile": self.config.profile.value,
            "g2_GeV2": self.config.g2,
            "production_ready": False,
            "limitations": (
                "No NLO coefficient functions; rank-one/rank-two and T-odd "
                "functions require separate convention-aware adapters."
            ),
        }
