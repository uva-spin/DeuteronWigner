"""Bare, counterterm, and renormalized one-loop soft records."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    ContributionStatus,
    ProofSet,
    require_identity,
)
from .serialization import ContentAddressed


@dataclass(frozen=True)
class SoftBareOneLoopResult(ContentAddressed):
    identity: C35IdentityEnvelope
    result_id: str
    contribution_ids: tuple[str, ...]
    contribution_statuses: tuple[tuple[str, ContributionStatus], ...]
    direct_wilson_expression: str | None
    mode_sum_expression: str | None
    coefficient_expression: str | None
    dependence_variables: tuple[str, ...]
    count_once_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("bare-result tolerance must be positive")
        if len(self.contribution_ids) != len(self.contribution_statuses):
            raise ValueError("bare result must account for each contribution exactly once")
        if tuple(name for name, _ in self.contribution_statuses) != self.contribution_ids:
            raise ValueError("contribution order and status order must agree")
        if len(set(self.contribution_ids)) != len(self.contribution_ids):
            raise ValueError("bare result may not count a contribution twice")
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not self.contribution_ids or len(self.contribution_ids) != 18:
                raise ValueError("available bare result requires all eighteen C35 slots")
            if any(status is ContributionStatus.UNRESOLVED_BLOCKING for _, status in self.contribution_statuses):
                raise ValueError("available bare result cannot contain a blocking contribution")
            if not all((self.direct_wilson_expression, self.mode_sum_expression, self.coefficient_expression, self.dependence_variables)):
                raise ValueError("available bare result needs two assembly routes and full dependence")
            if self.count_once_residual is None or self.count_once_residual > self.tolerance:
                raise ValueError("real/virtual count-once assembly does not close")
            if not self.proof.closed:
                raise ValueError("available bare result has open proof obligations")
        elif any(
            value not in (None, (), "")
            for value in (
                self.direct_wilson_expression,
                self.mode_sum_expression,
                self.coefficient_expression,
                self.dependence_variables,
                self.count_once_residual,
            )
        ):
            raise ValueError("unavailable bare result must not publish a coefficient")


@dataclass(frozen=True)
class SoftCountertermSystem(ContentAddressed):
    identity: C35IdentityEnvelope
    system_id: str
    bare_result_id: str
    divergence_classes: tuple[str, ...]
    uv_counterterm_expression: str | None
    rapidity_counterterm_expression: str | None
    residual_line_mass_expression: str | None
    inverse_expression: str | None
    state_independence_residual: float | None
    gauge_independence_residual: float | None
    threshold_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("counterterm tolerance must be positive")
        material = (
            self.divergence_classes,
            self.uv_counterterm_expression,
            self.rapidity_counterterm_expression,
            self.residual_line_mass_expression,
            self.inverse_expression,
            self.state_independence_residual,
            self.gauge_independence_residual,
            self.threshold_residual,
        )
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material):
                raise ValueError("available counterterm system must separate every divergence")
            for residual in (
                self.state_independence_residual,
                self.gauge_independence_residual,
                self.threshold_residual,
            ):
                if residual is not None and abs(residual) > self.tolerance:
                    raise ValueError("counterterm closure residual exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available counterterm system has open proof obligations")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("counterterms remain empty-not-zero until bare closure")


@dataclass(frozen=True)
class SoftRenormalizedOneLoopResult(ContentAddressed):
    identity: C35IdentityEnvelope
    result_id: str
    bare_result_id: str
    counterterm_system_id: str
    renormalization_equation: str | None
    coefficient_expression: str | None
    cusp_anomalous_dimension: str | None
    rapidity_anomalous_dimension: str | None
    rg_residual: float | None
    rapidity_residual: float | None
    gauge_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("renormalized-result tolerance must be positive")
        material = (
            self.renormalization_equation,
            self.coefficient_expression,
            self.cusp_anomalous_dimension,
            self.rapidity_anomalous_dimension,
            self.rg_residual,
            self.rapidity_residual,
            self.gauge_residual,
        )
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, "") for value in material):
                raise ValueError("available renormalized result requires RG/rapidity/gauge closure")
            for residual in (self.rg_residual, self.rapidity_residual, self.gauge_residual):
                if residual is not None and abs(residual) > self.tolerance:
                    raise ValueError("renormalized soft residual exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available renormalized result has open proof obligations")
        elif any(value not in (None, "") for value in material):
            raise ValueError("unavailable renormalized result must be empty-not-zero")


__all__ = ["SoftBareOneLoopResult", "SoftCountertermSystem", "SoftRenormalizedOneLoopResult"]
