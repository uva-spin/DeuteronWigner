"""Typed light-front conventions and real/virtual integration charts."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    ProofSet,
    ValidationStatus,
    require_closed,
    require_identity,
)
from .serialization import ContentAddressed


def _finite_tuple(values: tuple[float, ...], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if any(value != value or abs(value) == float("inf") for value in values):
        raise ValueError(f"{name} must contain finite values")


def _minkowski_dot(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    if len(a) != 4 or len(b) != 4:
        raise ValueError("light-front basis vectors must have four components")
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


@dataclass(frozen=True)
class LightFrontConvention(ContentAddressed):
    identity: C35IdentityEnvelope
    convention_id: str
    plus_definition: str
    minus_definition: str
    metric_signature: str
    n_components: tuple[float, float, float, float]
    nbar_components: tuple[float, float, float, float]
    n_dot_nbar: float
    k_plus_projection: str
    k_minus_projection: str
    integration_measure: str
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.plus_definition != "(v0+v3)/sqrt(2)" or self.minus_definition != "(v0-v3)/sqrt(2)":
            raise ValueError("C35 requires the normalized sqrt(2) light-front convention")
        if self.metric_signature != "+---":
            raise ValueError("C35 requires the +--- metric")
        _finite_tuple(self.n_components, "n_components")
        _finite_tuple(self.nbar_components, "nbar_components")
        expected_n = (1.0 / math.sqrt(2.0), 0.0, 0.0, 1.0 / math.sqrt(2.0))
        expected_nbar = (1.0 / math.sqrt(2.0), 0.0, 0.0, -1.0 / math.sqrt(2.0))
        if max(abs(value - expected) for value, expected in zip(self.n_components, expected_n)) > 1e-14:
            raise ValueError("n components do not match the frozen project convention")
        if max(abs(value - expected) for value, expected in zip(self.nbar_components, expected_nbar)) > 1e-14:
            raise ValueError("nbar components do not match the frozen project convention")
        if abs(_minkowski_dot(self.n_components, self.n_components)) > 1e-14:
            raise ValueError("n must be null")
        if abs(_minkowski_dot(self.nbar_components, self.nbar_components)) > 1e-14:
            raise ValueError("nbar must be null")
        if (
            abs(self.n_dot_nbar - 1.0) > 1e-14
            or abs(_minkowski_dot(self.n_components, self.nbar_components) - self.n_dot_nbar) > 1e-14
        ):
            raise ValueError("n dot nbar must equal one")
        if self.k_plus_projection != "nbar.k" or self.k_minus_projection != "n.k":
            raise ValueError("light-front scalar-product projections are inconsistent")
        if not self.integration_measure:
            raise ValueError("the light-front integration measure must be explicit")
        require_closed(self.validation, self.proof, "light-front convention")


@dataclass(frozen=True)
class NullVectorNormalization(ContentAddressed):
    identity: C35IdentityEnvelope
    normalization_id: str
    n_squared: float
    nbar_squared: float
    n_dot_nbar: float
    reconstruction_residual: float
    line_rescaling_law: str
    delta_plus_rescaling_law: str
    delta_minus_rescaling_law: str
    numerator_normalization: str
    tolerance: float
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.validation is ValidationStatus.VALIDATED and (
            abs(self.n_squared) > self.tolerance
            or abs(self.nbar_squared) > self.tolerance
            or abs(self.n_dot_nbar - 1.0) > self.tolerance
            or abs(self.reconstruction_residual) > self.tolerance
        ):
            raise ValueError("validated null-vector normalization exceeds tolerance")
        require_closed(self.validation, self.proof, "null-vector normalization")


@dataclass(frozen=True)
class RapidityRegulatorRescaling(ContentAddressed):
    identity: C35IdentityEnvelope
    rescaling_id: str
    lambda_symbol: str
    n_law: str
    nbar_law: str
    delta_plus_law: str
    delta_minus_law: str
    invariant_combinations: tuple[str, ...]
    covariance_residual: float | None
    tolerance: float
    validation: ValidationStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.validation is ValidationStatus.VALIDATED:
            if self.covariance_residual is None or abs(self.covariance_residual) > self.tolerance:
                raise ValueError("validated regulator rescaling needs an in-tolerance residual")
            if not self.invariant_combinations:
                raise ValueError("validated rescaling needs an invariant combination")
        elif self.covariance_residual is not None:
            raise ValueError("unvalidated rescaling may not publish a residual")
        require_closed(self.validation, self.proof, "rapidity-regulator rescaling")


@dataclass(frozen=True)
class SoftCoordinateChart(ContentAddressed):
    identity: C35IdentityEnvelope
    chart_id: str
    branch: str
    coordinates: tuple[str, ...]
    ranges: tuple[tuple[str, str], ...]
    momentum_map: tuple[tuple[str, str], ...]
    domain_statement: str
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if len(self.coordinates) != len(self.ranges):
            raise ValueError("every coordinate needs one explicit range")
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not self.coordinates or not self.momentum_map or not self.proof.closed:
                raise ValueError("an available coordinate chart must be executable and proved")
        elif self.coordinates or self.ranges or self.momentum_map:
            raise ValueError("an unavailable chart must be empty-not-zero")


@dataclass(frozen=True)
class RealSoftCoordinateChart(ContentAddressed):
    identity: C35IdentityEnvelope
    chart_id: str
    coordinates: tuple[str, ...]
    coordinate_ranges: tuple[tuple[str, str], ...]
    k_plus_expression: str | None
    k_minus_expression: str | None
    k_transverse_expression: str | None
    on_shell_constraint: str | None
    positive_energy_constraint: str | None
    jacobian_id: str | None
    measure_id: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (
            self.coordinates,
            self.coordinate_ranges,
            self.k_plus_expression,
            self.k_minus_expression,
            self.k_transverse_expression,
            self.on_shell_constraint,
            self.positive_energy_constraint,
            self.jacobian_id,
            self.measure_id,
        )
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material) or not self.proof.closed:
                raise ValueError("an available real chart must specify the complete on-shell map")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("an unavailable real chart must be empty-not-zero")


@dataclass(frozen=True)
class VirtualSoftCoordinateChart(ContentAddressed):
    identity: C35IdentityEnvelope
    chart_id: str
    representation: str | None
    coordinates: tuple[str, ...]
    coordinate_ranges: tuple[tuple[str, str], ...]
    loop_momentum_map: tuple[tuple[str, str], ...]
    modified_delta_denominators: tuple[str, ...]
    finite_cutoff_map: str | None
    contour_plan_id: str | None
    jacobian_id: str | None
    measure_id: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (
            self.representation,
            self.coordinates,
            self.coordinate_ranges,
            self.loop_momentum_map,
            self.modified_delta_denominators,
            self.finite_cutoff_map,
            self.contour_plan_id,
            self.jacobian_id,
            self.measure_id,
        )
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material) or not self.proof.closed:
                raise ValueError("an available virtual chart must preserve poles and cutoffs")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("an unavailable virtual chart must be empty-not-zero")


@dataclass(frozen=True)
class SoftJacobian(ContentAddressed):
    identity: C35IdentityEnvelope
    jacobian_id: str
    chart_id: str
    symbolic_expression: str | None
    generated_code_hash: str | None
    independent_check_expression: str | None
    maximum_residual: float | None
    tolerance: float
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not all((self.symbolic_expression, self.generated_code_hash, self.independent_check_expression)):
                raise ValueError("available Jacobians require symbolic, generated, and oracle identities")
            if self.maximum_residual is None or self.maximum_residual > self.tolerance:
                raise ValueError("Jacobian check does not close")
            if not self.proof.closed:
                raise ValueError("available Jacobian has open proof obligations")
        elif any(value is not None for value in (self.symbolic_expression, self.generated_code_hash, self.independent_check_expression, self.maximum_residual)):
            raise ValueError("unavailable Jacobian must be empty-not-zero")


@dataclass(frozen=True)
class RealCutMeasure(ContentAddressed):
    identity: C35IdentityEnvelope
    measure_id: str
    chart_id: str
    lorentz_measure: str | None
    on_shell_delta: str | None
    theta_constraint: str | None
    chart_measure: str | None
    normalization_factor: str | None
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.lorentz_measure, self.on_shell_delta, self.theta_constraint, self.chart_measure, self.normalization_factor)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not all(material) or not self.proof.closed:
                raise ValueError("available cut measures require all normalization data")
        elif any(value is not None for value in material):
            raise ValueError("unavailable cut measure must be empty-not-zero")


@dataclass(frozen=True)
class VirtualLoopMeasure(ContentAddressed):
    identity: C35IdentityEnvelope
    measure_id: str
    chart_id: str
    loop_measure: str | None
    contour_plan_id: str | None
    cutoff_operator: str | None
    normalization_factor: str | None
    regulator_identical_to_operator: bool
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        material = (self.loop_measure, self.contour_plan_id, self.cutoff_operator, self.normalization_factor)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not all(material) or not self.regulator_identical_to_operator or not self.proof.closed:
                raise ValueError("available virtual measure must be regulator-identical and proved")
        elif any(value is not None for value in material):
            raise ValueError("unavailable virtual measure must be empty-not-zero")


@dataclass(frozen=True)
class VirtualContourPlan(ContentAddressed):
    identity: C35IdentityEnvelope
    contour_id: str
    integration_variables: tuple[str, ...]
    pole_locations: tuple[str, ...]
    deformation_segments: tuple[str, ...]
    crossing_policy: str | None
    numerical_epsilon_role: str
    tolerance: float
    maximum_subdivisions: int
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0 or self.maximum_subdivisions < 0:
            raise ValueError("contour tolerance/subdivision limits are invalid")
        if self.numerical_epsilon_role not in ("ERROR_CONTROL_ONLY", "NONE"):
            raise ValueError("numerical epsilon may not define physical support")
        material = (self.integration_variables, self.pole_locations, self.deformation_segments, self.crossing_policy)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material) or not self.proof.closed:
                raise ValueError("available contour plan requires explicit poles and deformations")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("unavailable contour plan must be empty-not-zero")


__all__ = [
    "LightFrontConvention",
    "NullVectorNormalization",
    "RapidityRegulatorRescaling",
    "RealCutMeasure",
    "RealSoftCoordinateChart",
    "SoftCoordinateChart",
    "SoftJacobian",
    "VirtualContourPlan",
    "VirtualLoopMeasure",
    "VirtualSoftCoordinateChart",
]
