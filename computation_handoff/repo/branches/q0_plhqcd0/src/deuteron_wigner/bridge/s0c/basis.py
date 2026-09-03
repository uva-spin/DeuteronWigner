"""Finite-cell geometry, quadrature, completeness, and singular-cell types."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    ProofSet,
    ValidationStatus,
    require_closed,
    require_identity,
)
from .serialization import ContentAddressed


@dataclass(frozen=True)
class SoftCellBoundary(ContentAddressed):
    identity: C35IdentityEnvelope
    boundary_id: str
    chart_id: str
    coordinate_names: tuple[str, ...]
    lower: tuple[str, ...]
    upper: tuple[str, ...]
    lower_closed: tuple[bool, ...]
    upper_closed: tuple[bool, ...]
    boundary_condition: str

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        lengths = {len(self.coordinate_names), len(self.lower), len(self.upper), len(self.lower_closed), len(self.upper_closed)}
        if len(lengths) != 1 or not self.coordinate_names:
            raise ValueError("cell-boundary coordinate arrays must be nonempty and aligned")


@dataclass(frozen=True)
class SoftCellShape(ContentAddressed):
    identity: C35IdentityEnvelope
    shape_id: str
    boundary_id: str
    function_expression: str | None
    support_statement: str | None
    normalization_expression: str | None
    metric_signature: tuple[int, ...]
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.function_expression, self.support_statement, self.normalization_expression, self.metric_signature)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material) or not self.proof.closed:
                raise ValueError("available cell shape must define support, normalization, and metric")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("unavailable cell shape must be empty-not-zero")


@dataclass(frozen=True)
class SoftCellMeasure(ContentAddressed):
    identity: C35IdentityEnvelope
    measure_id: str
    chart_id: str
    density_expression: str | None
    normalization_expression: str | None
    jacobian_id: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.density_expression, self.normalization_expression, self.jacobian_id)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not all(material) or not self.proof.closed:
                raise ValueError("available cell measure must be completely normalized")
        elif any(value is not None for value in material):
            raise ValueError("unavailable cell measure must be empty-not-zero")


@dataclass(frozen=True)
class SoftCellQuadrature(ContentAddressed):
    identity: C35IdentityEnvelope
    quadrature_id: str
    cell_id: str
    rule: str | None
    order: int
    node_array_hash: str | None
    weight_array_hash: str | None
    node_count: int
    exactness_statement: str | None
    oracle_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.order < 0 or self.node_count < 0 or self.tolerance <= 0:
            raise ValueError("quadrature order/count/tolerance is invalid")
        material = (self.rule, self.node_array_hash, self.weight_array_hash, self.exactness_statement, self.oracle_residual)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if self.order < 1 or self.node_count < 1 or any(value is None for value in material):
                raise ValueError("available quadrature needs materialized nodes, weights, and oracle")
            if self.oracle_residual is not None and self.oracle_residual > self.tolerance:
                raise ValueError("quadrature oracle residual exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available quadrature has open proof obligations")
        elif any(value is not None for value in material) or self.order or self.node_count:
            raise ValueError("unavailable quadrature must be empty-not-zero")


@dataclass(frozen=True)
class SoftCell(ContentAddressed):
    identity: C35IdentityEnvelope
    cell_id: str
    chart_id: str
    boundary_id: str | None
    shape_id: str | None
    measure_id: str | None
    quadrature_id: str | None
    color_id: str | None
    polarization_id: str | None
    rapidity_owner: str | None
    zero_mode_relation: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.boundary_id, self.shape_id, self.measure_id, self.quadrature_id, self.color_id, self.polarization_id, self.rapidity_owner, self.zero_mode_relation)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not all(material) or not self.proof.closed:
                raise ValueError("available cells require all geometry and mode identities")
        elif any(value is not None for value in material):
            raise ValueError("unavailable cell must be empty-not-zero")


@dataclass(frozen=True)
class SoftPartitionOfUnity(ContentAddressed):
    identity: C35IdentityEnvelope
    partition_id: str
    regulated_domain: str
    cell_ids: tuple[str, ...]
    rapidity_region_ids: tuple[str, ...]
    partition_expression: str | None
    overlap_policy: str | None
    maximum_residual: float | None
    tolerance: float
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.validation is ValidationStatus.VALIDATED:
            if not self.cell_ids or not self.rapidity_region_ids or not self.partition_expression or not self.overlap_policy:
                raise ValueError("validated partitions require cells, regions, expression, and overlap policy")
            if self.maximum_residual is None or self.maximum_residual > self.tolerance:
                raise ValueError("partition residual exceeds tolerance")
        elif any((self.cell_ids, self.rapidity_region_ids, self.partition_expression, self.overlap_policy, self.maximum_residual is not None)):
            raise ValueError("unvalidated partition must not expose a completed partition")
        require_closed(self.validation, self.proof, "partition of unity")


@dataclass(frozen=True)
class SoftRefinementMap(ContentAddressed):
    identity: C35IdentityEnvelope
    refinement_id: str
    coarse_collection_id: str
    fine_collection_id: str
    parent_to_children: tuple[tuple[str, tuple[str, ...]], ...]
    prolongation_hash: str | None
    restriction_hash: str | None
    normalization_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not self.parent_to_children or not self.prolongation_hash or not self.restriction_hash:
                raise ValueError("available refinement map must be materialized")
            if self.normalization_residual is None or self.normalization_residual > self.tolerance:
                raise ValueError("refinement map fails normalization")
            if not self.proof.closed:
                raise ValueError("available refinement map has open proof obligations")
        elif any((self.parent_to_children, self.prolongation_hash, self.restriction_hash, self.normalization_residual is not None)):
            raise ValueError("unavailable refinement map must be empty-not-zero")


@dataclass(frozen=True)
class SoftModeCollection(ContentAddressed):
    identity: C35IdentityEnvelope
    collection_id: str
    chart_id: str
    cell_ids: tuple[str, ...]
    mode_ids: tuple[str, ...]
    dimension: int
    mode_array_hash: str | None
    partition_id: str | None
    refinement_parent_id: str | None
    commutator_statement: str | None
    completeness_statement: str | None
    normalization_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.dimension < 0 or self.tolerance <= 0:
            raise ValueError("mode dimension/tolerance is invalid")
        material = (self.cell_ids, self.mode_ids, self.mode_array_hash, self.partition_id, self.commutator_statement, self.completeness_statement, self.normalization_residual)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if self.dimension < 1 or len(self.mode_ids) != self.dimension or not self.cell_ids:
                raise ValueError("available collection dimension must match materialized modes")
            if any(value in (None, (), "") for value in material):
                raise ValueError("available collection lacks normalization/completeness data")
            if self.normalization_residual is not None and self.normalization_residual > self.tolerance:
                raise ValueError("mode normalization residual exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available mode collection has open proof obligations")
        elif any(value not in (None, (), "") for value in material) or self.dimension:
            raise ValueError("unavailable mode collection must be empty-not-zero")


@dataclass(frozen=True)
class PoleCellPartition(ContentAddressed):
    identity: C35IdentityEnvelope
    partition_id: str
    cell_id: str
    pole_expressions: tuple[str, ...]
    subcell_boundaries: tuple[str, ...]
    principal_value_regions: tuple[str, ...]
    delta_regions: tuple[str, ...]
    center_sampling_forbidden: bool
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.pole_expressions, self.subcell_boundaries, self.principal_value_regions, self.delta_regions)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(not value for value in material) or not self.center_sampling_forbidden or not self.proof.closed:
                raise ValueError("available pole partition must split every pole without center sampling")
        elif any(material):
            raise ValueError("unavailable pole partition must be empty-not-zero")


@dataclass(frozen=True)
class SingularCellSubtraction(ContentAddressed):
    identity: C35IdentityEnvelope
    subtraction_id: str
    partition_id: str
    distribution_identity: str | None
    analytic_singular_part: str | None
    remainder_integrand: str | None
    remainder_quadrature_id: str | None
    maximum_residual: float | None
    tolerance: float
    maximum_subdivisions: int
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0 or self.maximum_subdivisions < 0:
            raise ValueError("subtraction tolerance/subdivision limits are invalid")
        material = (self.distribution_identity, self.analytic_singular_part, self.remainder_integrand, self.remainder_quadrature_id, self.maximum_residual)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value is None for value in material):
                raise ValueError("available subtraction requires analytic and remainder routes")
            if self.maximum_residual is not None and self.maximum_residual > self.tolerance:
                raise ValueError("singular-cell subtraction residual exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available subtraction has open proof obligations")
        elif any(value is not None for value in material):
            raise ValueError("unavailable subtraction must be empty-not-zero")


__all__ = [
    "PoleCellPartition",
    "SingularCellSubtraction",
    "SoftCell",
    "SoftCellBoundary",
    "SoftCellMeasure",
    "SoftCellQuadrature",
    "SoftCellShape",
    "SoftModeCollection",
    "SoftPartitionOfUnity",
    "SoftRefinementMap",
]
