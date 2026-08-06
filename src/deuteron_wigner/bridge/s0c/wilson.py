"""Executable Wilson-segment, damping, vertex, and one-loop kernel identities."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    ContributionStatus,
    ProofSet,
    validate_contribution,
    require_identity,
)
from .serialization import ContentAddressed


def _available(status: AvailabilityStatus, material: tuple[object, ...], proof: ProofSet, name: str) -> None:
    if status is AvailabilityStatus.AVAILABLE:
        if any(value in (None, (), "") for value in material) or not proof.closed:
            raise ValueError(f"available {name} requires complete executable material")
    elif any(value not in (None, (), "") for value in material):
        raise ValueError(f"unavailable {name} must be empty-not-zero")


@dataclass(frozen=True)
class WilsonSegmentParameterization(ContentAddressed):
    identity: C35IdentityEnvelope
    segment_id: str
    line_id: str
    start_point: tuple[str, str, str, str]
    direction: tuple[str, str, str, str]
    affine_parameter: str
    parameter_range: tuple[str, str]
    orientation: str
    ordering: str
    representation_action: str
    damping_operator_id: str | None
    endpoint_ids: tuple[str, str]
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.start_point, self.direction, self.affine_parameter, self.parameter_range, self.orientation, self.ordering, self.representation_action, self.damping_operator_id, self.endpoint_ids), self.proof, "Wilson segment")


@dataclass(frozen=True)
class LongitudinalWilsonSegment(ContentAddressed):
    identity: C35IdentityEnvelope
    segment_id: str
    parameterization_id: str
    null_direction: str
    finite_length_symbol: str | None
    infinite_limit_prescription: str | None
    pole_component: str | None
    pole_prescription: str | None
    transverse_basepoint: tuple[str, str] | tuple[()]
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        _available(self.availability, (self.finite_length_symbol, self.infinite_limit_prescription, self.pole_component, self.pole_prescription, self.transverse_basepoint), self.proof, "longitudinal Wilson segment")


@dataclass(frozen=True)
class TransverseInfinitySegment(ContentAddressed):
    identity: C35IdentityEnvelope
    segment_id: str
    parameterization_id: str
    infinity_limit: str | None
    transverse_path: str | None
    junction_ids: tuple[str, ...]
    residual_gauge_prescription: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(self.contribution_status, self.proof, value_expression=self.value_expression, cancellation_partner_id=self.cancellation_partner_id)
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING and not all((self.infinity_limit, self.transverse_path, self.junction_ids, self.residual_gauge_prescription)):
            raise ValueError("resolved transverse segment needs explicit geometry and gauge prescription")


@dataclass(frozen=True)
class ModifiedDeltaDampingOperator(ContentAddressed):
    identity: C35IdentityEnvelope
    operator_id: str
    segment_id: str
    delta_component: str
    orientation: str
    damping_kernel: str | None
    complex_pole: str | None
    conjugate_operator_id: str | None
    rescaling_law: str | None
    finite_line_action: str | None
    infinite_line_limit: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.delta_component not in ("delta+", "delta-"):
            raise ValueError("modified-delta operator must select delta+ or delta-")
        _available(self.availability, (self.damping_kernel, self.complex_pole, self.conjugate_operator_id, self.rescaling_law, self.finite_line_action, self.infinite_line_limit), self.proof, "modified-delta operator")


@dataclass(frozen=True)
class FiniteSegmentLimit(ContentAddressed):
    identity: C35IdentityEnvelope
    limit_id: str
    segment_id: str
    finite_expression: str | None
    damped_infinite_expression: str | None
    regulator_removal_order: tuple[str, ...]
    sampled_lengths: tuple[float, ...]
    maximum_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("limit tolerance must be positive")
        _available(self.availability, (self.finite_expression, self.damped_infinite_expression, self.regulator_removal_order, self.sampled_lengths, self.maximum_residual), self.proof, "finite-segment limit")
        if self.availability is AvailabilityStatus.AVAILABLE and self.maximum_residual is not None and self.maximum_residual > self.tolerance:
            raise ValueError("finite-line limit residual exceeds tolerance")


@dataclass(frozen=True)
class ExecutableEikonalVertex(ContentAddressed):
    identity: C35IdentityEnvelope
    vertex_id: str
    line_id: str
    mode_collection_id: str
    segment_id: str | None
    damping_operator_id: str | None
    color_action: str | None
    orientation_factor: str | None
    mode_matrix_element: str | None
    generated_kernel_hash: str | None
    ward_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("vertex tolerance must be positive")
        _available(self.availability, (self.segment_id, self.damping_operator_id, self.color_action, self.orientation_factor, self.mode_matrix_element, self.generated_kernel_hash, self.ward_residual), self.proof, "eikonal vertex")
        if self.availability is AvailabilityStatus.AVAILABLE and self.ward_residual is not None and abs(self.ward_residual) > self.tolerance:
            raise ValueError("eikonal Ward residual exceeds tolerance")


@dataclass(frozen=True)
class ExecutableLinePairKernel(ContentAddressed):
    identity: C35IdentityEnvelope
    kernel_id: str
    line_pair: tuple[str, str]
    branch: str
    vertex_ids: tuple[str, str]
    color_contraction: str | None
    transverse_phase: str | None
    measure_id: str | None
    cell_ids: tuple[str, ...]
    generated_kernel_hash: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if len(self.line_pair) != 2 or len(self.vertex_ids) != 2:
            raise ValueError("line-pair kernel requires exactly two lines and vertices")
        validate_contribution(self.contribution_status, self.proof, value_expression=self.value_expression, cancellation_partner_id=self.cancellation_partner_id)
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING and not all((self.color_contraction, self.transverse_phase, self.measure_id, self.cell_ids, self.generated_kernel_hash)):
            raise ValueError("resolved line-pair kernel lacks executable identities")


@dataclass(frozen=True)
class ExecutableSelfKernel(ContentAddressed):
    identity: C35IdentityEnvelope
    kernel_id: str
    line_id: str
    vertex_id: str
    measure_id: str | None
    subtraction_id: str | None
    generated_kernel_hash: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(self.contribution_status, self.proof, value_expression=self.value_expression, cancellation_partner_id=self.cancellation_partner_id)
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING and not all((self.measure_id, self.subtraction_id, self.generated_kernel_hash)):
            raise ValueError("resolved self kernel lacks measure/subtraction/code identities")


@dataclass(frozen=True)
class ExecutableCuspKernel(ContentAddressed):
    identity: C35IdentityEnvelope
    kernel_id: str
    incoming_segment_id: str
    outgoing_segment_id: str
    junction_id: str
    cusp_angle: str | None
    measure_id: str | None
    generated_kernel_hash: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(self.contribution_status, self.proof, value_expression=self.value_expression, cancellation_partner_id=self.cancellation_partner_id)
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING and not all((self.cusp_angle, self.measure_id, self.generated_kernel_hash)):
            raise ValueError("resolved cusp kernel lacks geometry or executable identity")


@dataclass(frozen=True)
class ExecutableBoundaryKernel(ContentAddressed):
    identity: C35IdentityEnvelope
    kernel_id: str
    boundary_sector_id: str
    segment_ids: tuple[str, ...]
    boundary_condition: str | None
    measure_id: str | None
    generated_kernel_hash: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(self.contribution_status, self.proof, value_expression=self.value_expression, cancellation_partner_id=self.cancellation_partner_id)
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING and not all((self.segment_ids, self.boundary_condition, self.measure_id, self.generated_kernel_hash)):
            raise ValueError("resolved boundary kernel lacks explicit boundary data")


__all__ = [
    "ExecutableBoundaryKernel",
    "ExecutableCuspKernel",
    "ExecutableEikonalVertex",
    "ExecutableLinePairKernel",
    "ExecutableSelfKernel",
    "FiniteSegmentLimit",
    "LongitudinalWilsonSegment",
    "ModifiedDeltaDampingOperator",
    "TransverseInfinitySegment",
    "WilsonSegmentParameterization",
]
