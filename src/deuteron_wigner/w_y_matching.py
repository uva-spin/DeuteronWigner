"""Explicit validity and replacement interface for TMD W+Y observables."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

WTerm = Callable[[float], float]
YTerm = Callable[[float, float], float]


@dataclass(frozen=True)
class LowQTValidity:
    """Declared domain for a resummed W term."""

    maximum_qt_over_q: float = 0.25
    maximum_qt_gev: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 < self.maximum_qt_over_q < 1.0:
            raise ValueError("maximum_qt_over_q must lie in (0,1)")
        if self.maximum_qt_gev <= 0.0:
            raise ValueError("maximum_qt_gev must be positive")

    def contains(self, qt_gev: float, q_gev: float) -> bool:
        if qt_gev < 0.0 or q_gev <= 0.0:
            raise ValueError("require qT>=0 and Q>0")
        return (
            qt_gev <= self.maximum_qt_gev
            and qt_gev / q_gev <= self.maximum_qt_over_q
        )


@dataclass(frozen=True)
class MatchingOverlapEvidence:
    """Numerical evidence that W and its fixed-order asymptotic expansion overlap."""

    passed: bool
    contiguous_points: int
    maximum_relative_difference: float
    qT_interval_gev: tuple[float, float] | None
    source: str


def assess_matching_overlap(
    *,
    qt_gev: np.ndarray,
    w_resummed: np.ndarray,
    asymptotic: np.ndarray,
    q_gev: float,
    relative_tolerance: float = 0.25,
    minimum_contiguous_points: int = 3,
    absolute_floor: float = 1e-12,
    source: str,
) -> MatchingOverlapEvidence:
    """Require a same-sign contiguous W/asymptotic agreement interval."""

    qt = np.asarray(qt_gev, dtype=float)
    w = np.asarray(w_resummed, dtype=float)
    asym = np.asarray(asymptotic, dtype=float)
    if (
        qt.ndim != 1 or len(qt) < minimum_contiguous_points
        or w.shape != qt.shape or asym.shape != qt.shape
        or not np.all(np.diff(qt) > 0.0)
    ):
        raise ValueError("overlap inputs require aligned increasing 1D arrays")
    if q_gev <= 0.0 or not 0.0 < relative_tolerance < 1.0:
        raise ValueError("invalid hard scale or relative tolerance")
    scale = np.maximum(np.maximum(np.abs(w), np.abs(asym)), absolute_floor)
    relative = np.abs(w - asym) / scale
    acceptable = (
        (w * asym > 0.0)
        & (relative <= relative_tolerance)
        & (qt / q_gev >= 0.1)
        & (qt / q_gev <= 1.0)
    )
    runs = []
    start = None
    for index, value in enumerate(acceptable):
        if value and start is None:
            start = index
        if start is not None and (not value or index == len(acceptable) - 1):
            end = index if value and index == len(acceptable) - 1 else index - 1
            runs.append((start, end))
            start = None
    best = max(runs, key=lambda pair: pair[1] - pair[0], default=None)
    count = 0 if best is None else best[1] - best[0] + 1
    interval = None if best is None else (float(qt[best[0]]), float(qt[best[1]]))
    maximum = (
        float("inf") if best is None
        else float(np.max(relative[best[0]:best[1] + 1]))
    )
    return MatchingOverlapEvidence(
        passed=count >= minimum_contiguous_points,
        contiguous_points=count,
        maximum_relative_difference=maximum,
        qT_interval_gev=interval,
        source=source,
    )


@dataclass(frozen=True)
class FixedOrderYRemainder:
    """Process-specific Y=FO-asymptotic remainder with required provenance."""

    response: YTerm
    process: str
    perturbative_order: str
    source: str
    subtraction_convention: str
    overlap_evidence: MatchingOverlapEvidence | None = None

    def __post_init__(self) -> None:
        if not all((
            self.process, self.perturbative_order,
            self.source, self.subtraction_convention,
        )):
            raise ValueError("Y term requires complete process/order provenance")

    def value(self, qt_gev: float, q_gev: float) -> float:
        return float(self.response(qt_gev, q_gev))


@dataclass(frozen=True)
class MatchedWPlusYObservable:
    """Combine a W term with an optional process-specific fixed-order Y term."""

    w_term: WTerm
    validity: LowQTValidity = LowQTValidity()
    y_term: FixedOrderYRemainder | None = None

    def evaluate(self, qt_gev: float, q_gev: float) -> dict[str, object]:
        low_qt = self.validity.contains(qt_gev, q_gev)
        if not low_qt and self.y_term is None:
            raise ValueError(
                "qT lies outside the declared W-term domain and no sourced "
                "process-specific fixed-order Y remainder is installed"
            )
        if (
            not low_qt and self.y_term is not None
            and (
                self.y_term.overlap_evidence is None
                or not self.y_term.overlap_evidence.passed
            )
        ):
            raise ValueError(
                "high-qT W+Y evaluation requires a passed numerical "
                "W/asymptotic overlap assessment"
            )
        w = float(self.w_term(qt_gev))
        y = 0.0 if self.y_term is None else self.y_term.value(qt_gev, q_gev)
        return {
            "value": w + y,
            "W": w,
            "Y": y,
            "mode": "W_only_low_qT" if self.y_term is None else "W_plus_Y",
            "inside_W_domain": low_qt,
            "Q_GeV": float(q_gev),
            "qT_GeV": float(qt_gev),
            "qT_over_Q": float(qt_gev / q_gev),
            "y_provenance": (
                None if self.y_term is None else {
                    "process": self.y_term.process,
                    "order": self.y_term.perturbative_order,
                    "source": self.y_term.source,
                    "subtraction": self.y_term.subtraction_convention,
                    "overlap": (
                        None
                        if self.y_term.overlap_evidence is None
                        else self.y_term.overlap_evidence.__dict__
                    ),
                }
            ),
        }
