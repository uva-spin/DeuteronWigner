"""Gauge-complete plan, mode, action, Hamiltonian, and closure records."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    GaugePlanKind,
    ProofSet,
    ValidationStatus,
    require_closed,
    require_identity,
)
from .serialization import ContentAddressed


def _available(status: AvailabilityStatus, material: tuple[object, ...], proof: ProofSet, name: str) -> None:
    present = all(value not in (None, (), "") for value in material)
    if status is AvailabilityStatus.AVAILABLE:
        if not present or not proof.closed:
            raise ValueError(f"available {name} needs complete material and closed proof")
    elif any(value not in (None, (), "") for value in material):
        raise ValueError(f"unavailable {name} must be empty-not-zero")


@dataclass(frozen=True)
class GaugeCompleteSoftPlan(ContentAddressed):
    identity: C35IdentityEnvelope
    plan_id: str
    kind: GaugePlanKind
    selected: bool
    selected_before_results: bool
    gauge_complete: bool
    regulator_identical: bool
    action_id: str | None
    mode_metric_id: str | None
    constraint_sector_id: str | None
    zero_mode_sector_id: str | None
    boundary_sector_id: str | None
    execution_allowed: bool
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.execution_allowed:
            if not (self.selected and self.selected_before_results and self.gauge_complete and self.regulator_identical):
                raise ValueError("execution requires a preselected, gauge-complete, identical regulator")
            if self.kind is GaugePlanKind.UNAVAILABLE or not all((self.action_id, self.mode_metric_id, self.zero_mode_sector_id, self.boundary_sector_id)):
                raise ValueError("execution requires complete gauge-plan object identities")
            if not self.proof.closed:
                raise ValueError("gauge-plan execution has open proof obligations")
        elif self.kind is GaugePlanKind.UNAVAILABLE and any((self.action_id, self.mode_metric_id, self.constraint_sector_id, self.zero_mode_sector_id, self.boundary_sector_id)):
            raise ValueError("the unavailable gauge plan must be empty-not-zero")


@dataclass(frozen=True)
class CovariantKreinPlan(ContentAddressed):
    identity: C35IdentityEnvelope
    plan_id: str
    gauge_parameter_values: tuple[float, ...]
    four_vector_mode_ids: tuple[str, ...]
    indefinite_metric_id: str | None
    constraint_sector_id: str | None
    ghost_sector_id: str | None
    brst_report_id: str | None
    propagator_projection: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.gauge_parameter_values, self.four_vector_mode_ids, self.indefinite_metric_id, self.constraint_sector_id, self.ghost_sector_id, self.brst_report_id, self.propagator_projection), self.proof, "covariant/Krein plan")


@dataclass(frozen=True)
class LightFrontPhysicalPlan(ContentAddressed):
    identity: C35IdentityEnvelope
    plan_id: str
    gauge_condition: str | None
    transverse_mode_ids: tuple[str, ...]
    instantaneous_kernel_id: str | None
    boundary_link_id: str | None
    constrained_zero_mode_id: str | None
    residual_gauge_prescription: str | None
    covariant_target_map_id: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.gauge_condition, self.transverse_mode_ids, self.instantaneous_kernel_id, self.boundary_link_id, self.constrained_zero_mode_id, self.residual_gauge_prescription, self.covariant_target_map_id), self.proof, "light-front physical plan")
        if self.availability is AvailabilityStatus.AVAILABLE and len(self.transverse_mode_ids) != 2:
            raise ValueError("light-front physical realization needs exactly two propagating polarizations")


@dataclass(frozen=True)
class GaugePlanSupersession(ContentAddressed):
    identity: C35IdentityEnvelope
    supersession_id: str
    prior_plan_id: str
    replacement_plan_id: str
    reason: str
    selected_before_results: bool
    prior_results_inspected: bool
    effective_version: str
    evidence_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.prior_plan_id == self.replacement_plan_id:
            raise ValueError("a supersession must change the plan")
        if not self.reason or not self.evidence_ids:
            raise ValueError("a gauge-plan supersession needs reason and evidence")
        if not self.selected_before_results or self.prior_results_inspected:
            raise ValueError("gauge plan may not change after residual inspection")


@dataclass(frozen=True)
class SoftGaugeMode(ContentAddressed):
    identity: C35IdentityEnvelope
    mode_id: str
    collection_id: str
    cell_id: str | None
    color_index: str | None
    polarization_index: str | None
    four_momentum: tuple[str, str, str, str]
    mode_function: str | None
    commutator: str | None
    metric_entry: int | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.cell_id, self.color_index, self.polarization_index, self.four_momentum, self.mode_function, self.commutator, self.metric_entry), self.proof, "soft gauge mode")


@dataclass(frozen=True)
class SoftPolarizationMetric(ContentAddressed):
    identity: C35IdentityEnvelope
    metric_id: str
    gauge_plan_id: str
    polarization_labels: tuple[str, ...]
    matrix_entries: tuple[tuple[str, ...], ...]
    signature: tuple[int, ...]
    inverse_entries: tuple[tuple[str, ...], ...]
    inverse_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("metric tolerance must be positive")
        _available(self.availability, (self.polarization_labels, self.matrix_entries, self.signature, self.inverse_entries, self.inverse_residual), self.proof, "polarization metric")
        if self.availability is AvailabilityStatus.AVAILABLE:
            n = len(self.polarization_labels)
            if len(self.matrix_entries) != n or len(self.inverse_entries) != n or len(self.signature) != n:
                raise ValueError("polarization metric dimensions do not agree")
            if self.inverse_residual is not None and self.inverse_residual > self.tolerance:
                raise ValueError("polarization metric inverse residual exceeds tolerance")


@dataclass(frozen=True)
class SoftGhostMode(ContentAddressed):
    identity: C35IdentityEnvelope
    mode_id: str
    cell_id: str | None
    ghost_number: int
    grassmann_parity: int
    action_term: str | None
    propagator: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.grassmann_parity not in (0, 1):
            raise ValueError("Grassmann parity must be 0 or 1")
        _available(self.availability, (self.cell_id, self.action_term, self.propagator), self.proof, "ghost mode")


@dataclass(frozen=True)
class SoftAuxiliaryMode(ContentAddressed):
    identity: C35IdentityEnvelope
    mode_id: str
    field_kind: str
    cell_id: str | None
    constraint_equation: str | None
    action_term: str | None
    propagating: bool
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.cell_id, self.constraint_equation, self.action_term), self.proof, "auxiliary mode")


@dataclass(frozen=True)
class SoftInstantaneousKernel(ContentAddressed):
    identity: C35IdentityEnvelope
    kernel_id: str
    gauge_plan_id: str
    operator_expression: str | None
    inverse_derivative_prescription: str | None
    zero_mode_relation: str | None
    boundary_relation: str | None
    contribution_order: str
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.operator_expression, self.inverse_derivative_prescription, self.zero_mode_relation, self.boundary_relation), self.proof, "instantaneous kernel")


@dataclass(frozen=True)
class SoftFreeAction(ContentAddressed):
    identity: C35IdentityEnvelope
    action_id: str
    gauge_plan_id: str
    lagrangian_expression: str | None
    gauge_fixing_expression: str | None
    constraint_action: str | None
    ghost_action: str | None
    boundary_action: str | None
    propagator_expression: str | None
    vacuum_normalization: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.lagrangian_expression, self.gauge_fixing_expression, self.constraint_action, self.ghost_action, self.boundary_action, self.propagator_expression, self.vacuum_normalization), self.proof, "free gauge action")


@dataclass(frozen=True)
class SoftFreeHamiltonian(ContentAddressed):
    identity: C35IdentityEnvelope
    hamiltonian_id: str
    action_id: str
    mode_collection_id: str
    free_operator_expression: str | None
    constraint_terms: tuple[str, ...]
    instantaneous_terms: tuple[str, ...]
    zero_mode_terms: tuple[str, ...]
    vacuum_energy_prescription: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.free_operator_expression, self.constraint_terms, self.instantaneous_terms, self.zero_mode_terms, self.vacuum_energy_prescription), self.proof, "free Hamiltonian")


@dataclass(frozen=True)
class SoftBRSTOrConstraintReport(ContentAddressed):
    identity: C35IdentityEnvelope
    report_id: str
    gauge_plan_id: str
    route: str
    identities_tested: tuple[str, ...]
    residuals: tuple[tuple[str, float], ...]
    tolerance: float
    ghost_status: str
    constraint_status: str
    instantaneous_status: str
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("closure tolerance must be positive")
        if self.validation is ValidationStatus.VALIDATED:
            if not self.identities_tested or not self.residuals:
                raise ValueError("validated gauge closure requires tested identities and residuals")
            if any(abs(value) > self.tolerance for _, value in self.residuals):
                raise ValueError("gauge-closure residual exceeds tolerance")
        require_closed(self.validation, self.proof, "BRST/constraint report")


__all__ = [
    "CovariantKreinPlan",
    "GaugeCompleteSoftPlan",
    "GaugePlanSupersession",
    "LightFrontPhysicalPlan",
    "SoftAuxiliaryMode",
    "SoftBRSTOrConstraintReport",
    "SoftFreeAction",
    "SoftFreeHamiltonian",
    "SoftGaugeMode",
    "SoftGhostMode",
    "SoftInstantaneousKernel",
    "SoftPolarizationMetric",
]
