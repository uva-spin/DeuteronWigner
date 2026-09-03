"""Physically constrained completion of the full spin-1 leading-twist basis.

This layer distinguishes externally/impulse-derived anchors from constrained
completion terms.  It is a phenomenological closure model, not a claim that
all spin-1 TMDs have been calculated from first principles.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Mapping

import numpy as np

from .registry import CollinearLimit, TMDEntry, TMDRegistry

Anchor = Callable[[float, float], float]
DirectTMD = Callable[[float, float, float], tuple[float, float, float]]


class GaugeLink(str, Enum):
    FUTURE = "future_SIDIS"
    PAST = "past_DY"

    @property
    def t_odd_sign(self) -> float:
        return 1.0 if self == GaugeLink.FUTURE else -1.0


class PredictionStatus(str, Enum):
    DERIVED = "derived"
    STRUCTURAL_ZERO = "structural_zero"
    CONSTRAINED = "constrained_model"


@dataclass(frozen=True)
class AmplitudePrior:
    """Dimensionless physical-modulation prior."""

    central: float
    sigma: float
    maximum: float

    def __post_init__(self) -> None:
        if self.sigma < 0.0 or not 0.0 <= self.maximum <= 1.0:
            raise ValueError("invalid amplitude uncertainty or bound")
        if abs(self.central) > self.maximum:
            raise ValueError("central amplitude exceeds its physical bound")

    def interval(self, coverage: float = 1.96) -> tuple[float, float]:
        return (
            max(-self.maximum, self.central - coverage * self.sigma),
            min(self.maximum, self.central + coverage * self.sigma),
        )


@dataclass(frozen=True)
class TMDPrediction:
    central: float
    lower: float
    upper: float
    status: PredictionStatus
    physical_ratio_central: float
    physical_ratio_lower: float
    physical_ratio_upper: float


def conservative_default_priors() -> dict[str, AmplitudePrior]:
    """Correlated-hierarchy defaults used only where no derived input exists.

    Bounds decrease with tensor complexity and are deliberately well inside
    the unit positivity ceiling. T-odd central values are small but nonzero;
    gauge-link reversal supplies their process sign.
    """

    return {
        "U": AmplitudePrior(0.10, 0.035, 0.25),
        "L": AmplitudePrior(0.12, 0.040, 0.30),
        "T": AmplitudePrior(0.08, 0.035, 0.22),
        "LL": AmplitudePrior(0.035, 0.015, 0.10),
        "LT": AmplitudePrior(0.045, 0.020, 0.12),
        "TT": AmplitudePrior(0.020, 0.010, 0.07),
        "T_ODD": AmplitudePrior(0.025, 0.015, 0.08),
    }


@dataclass(frozen=True)
class CompleteSpin1TMDModel:
    """Complete registry evaluator with rank-safe positivity envelopes."""

    registry: TMDRegistry
    mass: float
    width: float
    f1_anchor: Anchor
    g1_anchor: Anchor | None = None
    f1ll_anchor: Anchor | None = None
    h1_anchor: Anchor | None = None
    derived: Mapping[str, Anchor] | None = None
    direct_tmds: Mapping[str, DirectTMD] | None = None
    structural_zeros: frozenset[str] = frozenset()
    priors: Mapping[str, AmplitudePrior] | None = None
    anchor_relative_uncertainty: float = 0.05

    def __post_init__(self) -> None:
        if self.mass <= 0.0 or self.width <= 0.0:
            raise ValueError("mass and width must be positive")
        if self.anchor_relative_uncertainty < 0.0:
            raise ValueError("anchor uncertainty cannot be negative")

    def _anchor_for(self, entry: TMDEntry) -> Anchor | None:
        if self.derived and entry.name in self.derived:
            return self.derived[entry.name]
        if entry.name == "f1":
            return self.f1_anchor
        if entry.name == "g1":
            return self.g1_anchor
        if entry.name == "f1LL":
            return self.f1ll_anchor
        if entry.name == "h1":
            return self.h1_anchor
        return None

    def _base_profile(self, x: float, k: float, scale: float) -> float:
        if not 0.0 < x <= 1.0 or k < 0.0 or scale <= 0.0:
            raise ValueError("require 0<x<=1, k>=0, and positive scale")
        if self.direct_tmds and "f1" in self.direct_tmds:
            return float(self.direct_tmds["f1"](x, k, scale)[0])
        return float(
            self.f1_anchor(x, scale)
            * np.exp(-k**2 / self.width)
            / (np.pi * self.width)
        )

    def _rank_coefficient_shape(self, rank: int, k: float) -> float:
        return float(
            (self.mass / np.sqrt(self.width)) ** rank
            * np.exp(-0.5 * rank * k**2 / self.width)
        )

    def _physical_rank_factor(self, rank: int, k: float) -> float:
        return float((k / self.mass) ** rank)

    def predict(
        self,
        entry: TMDEntry,
        *,
        x: float,
        k: float,
        scale: float,
        gauge_link: GaugeLink,
    ) -> TMDPrediction:
        base = self._base_profile(x, k, scale)
        if self.direct_tmds and entry.name in self.direct_tmds:
            central, lower, upper = self.direct_tmds[entry.name](x, k, scale)
            physical_factor = self._physical_rank_factor(
                entry.transverse_rank, k
            )
            denominator = base if base != 0.0 else 1.0
            ratios = np.sort(
                physical_factor
                * np.asarray((lower, upper), dtype=np.float64)
                / denominator
            )
            return TMDPrediction(
                float(central),
                float(min(lower, upper)),
                float(max(lower, upper)),
                PredictionStatus.DERIVED,
                float(physical_factor * central / denominator),
                float(ratios[0]),
                float(ratios[1]),
            )
        if entry.name in self.structural_zeros:
            return TMDPrediction(
                0.0, 0.0, 0.0, PredictionStatus.STRUCTURAL_ZERO,
                0.0, 0.0, 0.0,
            )

        anchor = self._anchor_for(entry)
        if anchor is not None:
            central = float(
                anchor(x, scale)
                * np.exp(-k**2 / self.width)
                / (np.pi * self.width)
            )
            error = self.anchor_relative_uncertainty * abs(central)
            ratio = central / base if base != 0.0 else 0.0
            ratio_error = error / abs(base) if base != 0.0 else 0.0
            return TMDPrediction(
                central,
                central - error,
                central + error,
                PredictionStatus.DERIVED,
                ratio,
                ratio - ratio_error,
                ratio + ratio_error,
            )

        priors = self.priors or conservative_default_priors()
        prior = priors["T_ODD"] if entry.t_odd else priors[entry.target_channel.value]
        process_sign = gauge_link.t_odd_sign if entry.t_odd else 1.0
        coefficient_shape = self._rank_coefficient_shape(
            entry.transverse_rank, k
        )
        if (
            entry.transverse_rank == 0
            and entry.collinear_limit == CollinearLimit.NONE
        ):
            u = k**2 / self.width
            # Multiplied by the base exp(-u), this gives
            # exp(-2u)*(1-2u), whose two-dimensional integral vanishes.
            coefficient_shape *= (1.0 - 2.0 * u) * np.exp(-u)
        physical_factor = self._physical_rank_factor(
            entry.transverse_rank, k
        )
        low, high = prior.interval()
        amplitudes = np.sort(process_sign * np.asarray((low, high)))
        central_amplitude = process_sign * prior.central
        central = central_amplitude * base * coefficient_shape
        lower = amplitudes[0] * base * coefficient_shape
        upper = amplitudes[1] * base * coefficient_shape
        physical_scale = physical_factor * coefficient_shape
        return TMDPrediction(
            central,
            min(lower, upper),
            max(lower, upper),
            PredictionStatus.CONSTRAINED,
            central_amplitude * physical_scale,
            amplitudes[0] * physical_scale,
            amplitudes[1] * physical_scale,
        )

    def predict_all(
        self,
        *,
        x: float,
        k: float,
        scale: float,
        gauge_link: GaugeLink,
    ) -> dict[str, TMDPrediction]:
        return {
            entry.name: self.predict(
                entry, x=x, k=k, scale=scale, gauge_link=gauge_link
            )
            for entry in self.registry.select()
        }

    def require_modulation_bounds(
        self,
        predictions: Mapping[str, TMDPrediction],
        tolerance: float = 1.0e-12,
    ) -> None:
        for name, prediction in predictions.items():
            if name == "f1":
                continue
            if max(
                abs(prediction.physical_ratio_lower),
                abs(prediction.physical_ratio_upper),
            ) > 1.0 + tolerance:
                raise ValueError(f"{name} violates the conservative modulation bound")

    def require_block_budgets(
        self,
        predictions: Mapping[str, TMDPrediction],
        tolerance: float = 1.0e-12,
    ) -> None:
        """Require a conservative sufficient positivity budget per target sector.

        This triangle-inequality budget is stronger than bounding each
        modulation separately. It is sufficient but not necessary for the
        modeled polarization corrections to remain below the unpolarized
        reference scale.
        """

        budgets: dict[str, float] = {}
        for entry in self.registry.select():
            if entry.name == "f1":
                continue
            prediction = predictions[entry.name]
            size = max(
                abs(prediction.physical_ratio_lower),
                abs(prediction.physical_ratio_upper),
            )
            budgets[entry.target_channel.value] = (
                budgets.get(entry.target_channel.value, 0.0) + size
            )
        for channel, budget in budgets.items():
            if budget > 1.0 + tolerance:
                raise ValueError(
                    f"{channel} polarization block exceeds unit budget ({budget:g})"
                )
