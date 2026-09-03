"""Support-aware moment bookkeeping across species, flavor, and mechanisms."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence

import numpy as np
from scipy.integrate import simpson


class MomentObservable(str, Enum):
    NUMBER = "number"
    MOMENTUM = "momentum"
    HELICITY = "helicity"
    TENSOR = "tensor"
    TRANSVERSITY = "transversity"

    @property
    def x_power(self) -> int:
        return 1 if self is MomentObservable.MOMENTUM else 0


@dataclass(frozen=True)
class EndpointCompletion:
    """Explicit contribution outside a tabulated x interval."""

    corrections: Mapping[MomentObservable, float]
    source: str
    uncertainty_description: str
    uncertainties: Mapping[MomentObservable, float] | None = None

    def __post_init__(self) -> None:
        if not self.source or not self.uncertainty_description:
            raise ValueError("endpoint completion requires source and uncertainty")
        if any(not np.isfinite(value) for value in self.corrections.values()):
            raise ValueError("endpoint corrections must be finite")
        if self.uncertainties is not None and any(
            not np.isfinite(value) or value < 0.0
            for value in self.uncertainties.values()
        ):
            raise ValueError("endpoint uncertainties must be finite and nonnegative")


def local_power_endpoint_completion(
    source: "TabulatedMomentInput",
    *,
    points: int = 4,
    low_x_max: float = 0.01,
    high_x_min: float = 0.9,
) -> EndpointCompletion:
    """Fit integrable local endpoint powers, refusing non-asymptotic grids.

    This is a documented model completion, not an exact sum-rule constraint.
    Separate fits are made to ``|F|`` at each endpoint and retain the local
    sign.  It is suitable only when the serialized parent reaches both
    endpoint neighborhoods and the selected points do not cross zero.
    """
    x, y = source.x, source.values
    if points < 3 or len(x) < 2 * points:
        raise ValueError("endpoint fit requires at least three points per tail")
    if x[0] > low_x_max or x[-1] < high_x_min:
        raise ValueError("table does not reach configured endpoint neighborhoods")

    def fit(axis: np.ndarray, values: np.ndarray, label: str) -> tuple[float, float]:
        signs = np.sign(values)
        if np.any(values == 0.0) or not np.all(signs == signs[0]):
            raise ValueError(f"{label} endpoint values must be nonzero and sign stable")
        slope, intercept = np.polyfit(np.log(axis), np.log(np.abs(values)), 1)
        return float(signs[0] * np.exp(intercept)), float(slope)

    power = source.x_power

    def correction(n: int) -> float:
        low_a, low_p = fit(x[:n], y[:n], "low-x")
        high_a, high_p = fit(1.0 - x[-n:], y[-n:], "high-x")
        if low_p + power <= -1.0 or high_p <= -1.0:
            raise ValueError("fitted endpoint power is not integrable")
        low = low_a * x[0] ** (low_p + power + 1.0) / (low_p + power + 1.0)
        if power == 0:
            high = high_a * (1.0 - x[-1]) ** (high_p + 1.0) / (high_p + 1.0)
        else:
            tail_x = np.linspace(x[-1], 1.0, 513)
            high = float(simpson(
                tail_x**power * high_a * (1.0 - tail_x) ** high_p, x=tail_x
            ))
        return float(low + high)

    central = correction(points)
    variants = [correction(n) for n in sorted({
        max(3, points - 1), points, min(len(x) // 2, points + 1)
    })]
    uncertainty = max(abs(value - central) for value in variants)
    return EndpointCompletion(
        corrections={source.observable: central},
        source=(
            f"local power fits to {source.source}; {points} serialized parent "
            "nodes per endpoint"
        ),
        uncertainty_description=(
            "maximum absolute shift under adjacent endpoint fit windows; "
            "model sensitivity, not a fit covariance"
        ),
        uncertainties={source.observable: uncertainty},
    )


@dataclass(frozen=True)
class TabulatedMomentInput:
    species: str
    flavor: int
    mechanism: str
    observable: MomentObservable
    x: np.ndarray
    values: np.ndarray
    source: str
    endpoint_completion: EndpointCompletion | None = None
    x_power_override: int | None = None

    def __post_init__(self) -> None:
        x = np.asarray(self.x, dtype=float)
        values = np.asarray(self.values, dtype=float)
        if (
            x.ndim != 1
            or values.shape != x.shape
            or len(x) < 3
            or not np.all(np.isfinite(x))
            or not np.all(np.isfinite(values))
            or not np.all(np.diff(x) > 0.0)
            or x[0] < 0.0
            or x[-1] > 1.0
        ):
            raise ValueError("moment input requires finite aligned increasing x data")
        if not self.species or not self.mechanism or not self.source:
            raise ValueError("species, mechanism, and source are required")
        if self.x_power_override is not None and self.x_power_override < 0:
            raise ValueError("moment x power must be nonnegative")
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "values", values)

    @property
    def tabulated_full_support(self) -> bool:
        return self.x[0] == 0.0 and self.x[-1] == 1.0

    @property
    def support_complete(self) -> bool:
        return self.tabulated_full_support or (
            self.endpoint_completion is not None
            and self.observable in self.endpoint_completion.corrections
        )

    @property
    def x_power(self) -> int:
        return (
            self.observable.x_power
            if self.x_power_override is None
            else int(self.x_power_override)
        )


@dataclass(frozen=True)
class MomentLedgerEntry:
    species: str
    flavor: int
    mechanism: str
    observable: MomentObservable
    tabulated_integral: float
    endpoint_correction: float
    total: float
    x_interval: tuple[float, float]
    support_complete: bool
    source: str
    endpoint_source: str | None
    endpoint_uncertainty: float | None
    x_power: int


def evaluate_moment(source: TabulatedMomentInput) -> MomentLedgerEntry:
    weighted = source.x ** source.x_power * source.values
    tabulated = float(simpson(weighted, x=source.x))
    correction = (
        0.0
        if source.endpoint_completion is None
        else float(source.endpoint_completion.corrections.get(source.observable, 0.0))
    )
    return MomentLedgerEntry(
        species=source.species,
        flavor=source.flavor,
        mechanism=source.mechanism,
        observable=source.observable,
        tabulated_integral=tabulated,
        endpoint_correction=correction,
        total=tabulated + correction,
        x_interval=(float(source.x[0]), float(source.x[-1])),
        support_complete=source.support_complete,
        source=source.source,
        endpoint_source=(
            None
            if source.endpoint_completion is None
            else source.endpoint_completion.source
        ),
        endpoint_uncertainty=(
            None
            if source.endpoint_completion is None
            or source.endpoint_completion.uncertainties is None
            else source.endpoint_completion.uncertainties.get(source.observable)
        ),
        x_power=source.x_power,
    )


@dataclass(frozen=True)
class SumRuleAudit:
    name: str
    expected: float
    observed: float
    tolerance: float
    residual: float
    passed: bool
    entries: tuple[MomentLedgerEntry, ...]


def audit_sum_rule(
    name: str,
    entries: Sequence[MomentLedgerEntry],
    *,
    expected: float,
    tolerance: float,
) -> SumRuleAudit:
    if not name or tolerance < 0.0 or not np.isfinite(expected):
        raise ValueError("sum-rule name, finite expectation, and tolerance required")
    if not entries:
        raise ValueError("sum-rule audit requires at least one ledger entry")
    incomplete = [
        f"{entry.species}:{entry.flavor}:{entry.mechanism}:{entry.observable.value}"
        for entry in entries
        if not entry.support_complete
    ]
    if incomplete:
        raise ValueError(
            "cannot make conservation/sum-rule claim with incomplete x support: "
            + ", ".join(incomplete)
        )
    observed = float(sum(entry.total for entry in entries))
    residual = observed - expected
    return SumRuleAudit(
        name=name,
        expected=float(expected),
        observed=observed,
        tolerance=float(tolerance),
        residual=residual,
        passed=abs(residual) <= tolerance,
        entries=tuple(entries),
    )


def audit_linear_sum_rule(
    name: str,
    weighted_entries: Sequence[tuple[float, MomentLedgerEntry]],
    *,
    expected: float,
    tolerance: float,
) -> SumRuleAudit:
    """Audit a signed flavor/mechanism combination such as q minus qbar."""
    if not weighted_entries:
        raise ValueError("linear sum-rule audit requires weighted entries")
    entries = tuple(entry for _, entry in weighted_entries)
    incomplete = [entry for _, entry in weighted_entries if not entry.support_complete]
    if incomplete:
        raise ValueError("cannot make linear sum-rule claim with incomplete x support")
    observed = float(sum(weight * entry.total for weight, entry in weighted_entries))
    residual = observed - expected
    return SumRuleAudit(
        name=name, expected=float(expected), observed=observed,
        tolerance=float(tolerance), residual=residual,
        passed=abs(residual) <= tolerance, entries=entries,
    )
