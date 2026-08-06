"""Soft-side overlap, capability, and package-closure records."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    OutcomeBranch,
    ProofSet,
    ValidationStatus,
    require_closed,
    require_identity,
)
from .serialization import ContentAddressed


@dataclass(frozen=True)
class SoftSideOverlapObject(ContentAddressed):
    identity: C35IdentityEnvelope
    overlap_id: str
    measurement_identity: str | None
    b_convention_id: str | None
    soft_regulator_id: str | None
    c32_collinear_regulator_id: str
    c32_off_shell_ir_plan_id: str
    conversion_map_id: str | None
    relation_status: str
    value_expression: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        allowed = {
            "SOFT_SIDE_ZERO_BIN_OBJECT_READY",
            "SOFT_COLLINEAR_EXACT_CONVERSION_READY",
            "SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST",
            "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED",
            "SOFT_COLLINEAR_INCOMPATIBLE",
        }
        if self.relation_status not in allowed:
            raise ValueError("unknown C35 soft/collinear relation status")
        material = (self.measurement_identity, self.b_convention_id, self.soft_regulator_id, self.value_expression)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, "") for value in material) or not self.proof.closed:
                raise ValueError("available soft overlap needs an executable soft-side value")
        elif any(value not in (None, "") for value in material):
            raise ValueError("unavailable overlap must be empty-not-zero")
        if self.relation_status == "SOFT_COLLINEAR_EXACT_CONVERSION_READY" and not self.conversion_map_id:
            raise ValueError("an exact conversion status requires a typed conversion map")


@dataclass(frozen=True)
class C35CapabilityMatrix(ContentAddressed):
    identity: C35IdentityEnvelope
    matrix_id: str
    capability_rows: tuple[tuple[str, ValidationStatus, str], ...]
    forbidden_statuses: tuple[str, ...]
    selected_gauge_plan_id: str
    all_eighteen_contributions_closed: bool
    bare_soft_available: bool
    renormalized_soft_available: bool
    conversion_available: bool
    soft_overlap_available: bool
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        names = tuple(row[0] for row in self.capability_rows)
        if len(set(names)) != len(names):
            raise ValueError("capability matrix rows require stable unique names")
        if any(status.value in self.forbidden_statuses for _, status, _ in self.capability_rows):
            raise ValueError("forbidden capability was promoted")
        if self.renormalized_soft_available and not self.bare_soft_available:
            raise ValueError("renormalization cannot precede the bare result")
        if self.conversion_available and not self.renormalized_soft_available:
            raise ValueError("conversion cannot precede renormalization")
        if self.bare_soft_available and not self.all_eighteen_contributions_closed:
            raise ValueError("bare soft result requires all eighteen slots")
        if any((self.bare_soft_available, self.renormalized_soft_available, self.conversion_available, self.soft_overlap_available)) and not self.proof.closed:
            raise ValueError("positive capabilities require a closed proof set")


@dataclass(frozen=True)
class C35ClosureReport(ContentAddressed):
    identity: C35IdentityEnvelope
    report_id: str
    capability_matrix_id: str
    outcome_branch: OutcomeBranch
    package_statuses: tuple[str, ...]
    blocking_requirements: tuple[str, ...]
    missing_calculation_ids: tuple[str, ...]
    exact_next_package: str
    gauge_regulator_validated: bool
    mode_basis_validated: bool
    one_loop_validated: bool
    uv_renormalization_validated: bool
    rapidity_renormalization_validated: bool
    overlap_ready: bool
    no_scope_leakage: bool
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        complete = all(
            (
                self.gauge_regulator_validated,
                self.mode_basis_validated,
                self.one_loop_validated,
                self.uv_renormalization_validated,
                self.rapidity_renormalization_validated,
                self.overlap_ready,
                self.no_scope_leakage,
            )
        )
        if self.outcome_branch is OutcomeBranch.REGULATOR_AND_ONE_LOOP_CLOSE:
            if not complete or self.blocking_requirements or self.missing_calculation_ids:
                raise ValueError("Branch A requires every C35 closure gate")
        else:
            if not self.blocking_requirements or not self.missing_calculation_ids:
                raise ValueError("every C35 no-go branch requires exact missing calculations")
        if not self.no_scope_leakage:
            raise ValueError("C35 cannot close or fail safely with downstream scope leakage")
        require_closed(self.validation, self.proof, "C35 closure report")


__all__ = ["C35CapabilityMatrix", "C35ClosureReport", "SoftSideOverlapObject"]
