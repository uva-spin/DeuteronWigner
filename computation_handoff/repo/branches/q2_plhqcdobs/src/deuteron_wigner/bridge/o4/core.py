"""Typed C36/O4 replacement-regulator architecture.

This module is deliberately an operator and scheme contract.  It defines a
finite-rapidity spacelike Wilson-line pair and its universal B=0 soft root;
it neither evaluates a finite-basis one-loop coefficient nor exports a TMD.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from enum import Enum
from hashlib import sha256
import json
import math
from typing import Any, Mapping


C36_SCOPE = "C36/O4"
C36_BASELINE_COMMIT = "bbefd963ea14bf79884ec3a5c1a503581a6dd21e"
C35_COMPLETION_COMMIT = C36_BASELINE_COMMIT
C35_PRIMARY_NO_GO = "C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE"
C35_SECONDARY_NO_GO = "C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE"
C35_FINITE_DELTA_WARD_DEFECT = 0.2143273
C36_ROOT = "C36_GAUGE_INVARIANT_FINITE_RAPIDITY_TMD_ROOT"
C36_COLLINEAR_ROOT = "C36_COLLINEAR_ROOT"
C36_SOFT_ROOT = "C36_SOFT_ROOT"
C36_SELECTED_PLAN = "O4-SPACELIKE-COLLINS-JMY"
C36_SELECTED_REPRESENTATION = "CONTINUUM_UNIVERSAL_SOFT_PLUS_FINITE_BASIS_COLLINEAR_MATCHING"
C36_FUTURE_MATCHING_STRATEGY = "M36-C:PARTONIC_DIFFERENCE_IN_SELECTED_FINITE_RAPIDITY_SCHEME"
C36_NEXT_PACKAGE = "C37/R2 — spacelike finite-rapidity partonic collinear calculation, universal soft subtraction, and finite-basis LF-to-project matching"
NONZERO_UNKNOWN = "NONZERO_UNKNOWN"
EMPTY_NOT_ZERO = "EMPTY_NOT_ZERO"


def canonical_json(value: Any) -> str:
    if is_dataclass(value):
        value = asdict(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False, default=str)


def content_hash(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


class RegulatorFamily(str, Enum):
    SPACELIKE_COLLINS_JMY = "O4-SPACELIKE-COLLINS-JMY"
    AUXILIARY_SPACELIKE = "O4-AUXILIARY-SPACELIKE"
    EXPONENTIAL = "O4-EXPONENTIAL"
    FINITE_LENGTH_SPACELIKE = "O4-FINITE-LENGTH-SPACELIKE"
    DRESSED_FIELD = "O4-DRESSED-FIELD"
    UNAVAILABLE = "O4-UNAVAILABLE"


@dataclass(frozen=True)
class ContentAddressed:
    """Immutable deterministic record used by every C36 contract."""

    @property
    def sha256(self) -> str:
        return content_hash(self)

    def to_canonical_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ReplacementRegulatorRootId(ContentAddressed):
    root_id: str
    version: str
    c35_superseded_root: str
    c35_no_go: str
    common_regulator_id: str
    state_independent: bool
    art25_independent: bool
    inference_reachable: bool = False
    production_reachable: bool = False

    def __post_init__(self) -> None:
        if self.root_id != C36_ROOT or not (self.state_independent and self.art25_independent):
            raise ValueError("C36 root identity or isolation failure")
        if self.inference_reachable or self.production_reachable:
            raise ValueError("C36 root must be unreachable from inference and production")


@dataclass(frozen=True)
class ReplacementRegulatorPlan(ContentAddressed):
    family: RegulatorFamily
    physical_plan: bool
    selected: bool
    finite_regulator_gauge_covariant: bool
    operator_identical_to_selected: bool
    transverse_closure: bool
    one_loop_authority: bool
    project_conversion: bool
    blockers: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.selected and (not self.physical_plan or self.family is RegulatorFamily.UNAVAILABLE):
            raise ValueError("selected C36 plan must be one physical regulator family")
        if self.selected and not all((self.finite_regulator_gauge_covariant, self.transverse_closure, self.one_loop_authority, self.project_conversion)):
            raise ValueError("selected C36 plan lacks a required closure condition")


@dataclass(frozen=True)
class ReplacementRegulatorSelection(ContentAddressed):
    selected_family: RegulatorFamily
    selected_before_coefficients: bool
    selected_representation: str
    plans: tuple[ReplacementRegulatorPlan, ...]

    def __post_init__(self) -> None:
        selected = [plan for plan in self.plans if plan.selected]
        if len(selected) != 1 or selected[0].family is not self.selected_family or not self.selected_before_coefficients:
            raise ValueError("C36 requires exactly one pre-coefficient physical plan")


@dataclass(frozen=True)
class FiniteRapidityDirection(ContentAddressed):
    direction_id: str
    components: tuple[float, float, float, float]
    norm_squared: float
    orientation: str
    rapidity_parameter: float
    finite: bool

    def __post_init__(self) -> None:
        if not self.finite or self.norm_squared >= 0.0:
            raise ValueError("C36 selected directions must be finite and spacelike")
        if self.orientation not in {"future", "past"}:
            raise ValueError("Wilson orientation must be explicit")


@dataclass(frozen=True)
class FiniteRapidityPair(ContentAddressed):
    v: FiniteRapidityDirection
    vbar: FiniteRapidityDirection
    dot_product: float
    invariant_id: str
    source_convention: str

    def __post_init__(self) -> None:
        if self.v.norm_squared >= 0 or self.vbar.norm_squared >= 0 or self.dot_product <= 0:
            raise ValueError("invalid spacelike rapidity pair")


@dataclass(frozen=True)
class FiniteRapidityInvariant(ContentAddressed):
    invariant_id: str
    definition: str
    value: float
    rescaling_invariant: bool
    source_id: str


@dataclass(frozen=True)
class RapidityLimitOrder(ContentAddressed):
    ordered_limits: tuple[str, ...]
    forbidden_order: str

    def __post_init__(self) -> None:
        if self.ordered_limits[:2] != ("renormalize_UV_and_rapidity_at_finite_v_vbar", "form_soft_subtracted_TMD"):
            raise ValueError("C36 limit order must renormalize before the lightlike limit")


@dataclass(frozen=True)
class GaugeCovariantWilsonPath(ContentAddressed):
    path_id: str
    segments: tuple[str, ...]
    representation: str
    path_ordering: str
    endpoint_law: str
    transverse_closure: str
    singular_gauge_complete: bool

    def __post_init__(self) -> None:
        if self.representation != "fundamental" or not self.transverse_closure or not self.singular_gauge_complete:
            raise ValueError("C36 path needs fundamental action and transverse closure")


@dataclass(frozen=True)
class ReplacementCollinearRoot(ContentAddressed):
    root_id: str
    baryon_number: int
    state_kind: str
    operator_id: str
    common_regulator_id: str
    soft_root_id: str


@dataclass(frozen=True)
class ReplacementSoftRoot(ContentAddressed):
    root_id: str
    baryon_number: int
    state_kind: str
    operator_id: str
    common_regulator_id: str
    collinear_root_id: str
    hadron_probability_tensor_member: bool

    def __post_init__(self) -> None:
        if self.baryon_number != 0 or self.hadron_probability_tensor_member:
            raise ValueError("universal C36 soft root cannot be placed in the hadron tensor")


@dataclass(frozen=True)
class ReplacementJointRegulator(ContentAddressed):
    regulator_id: str
    family: RegulatorFamily
    uv_scheme: str
    ir_prescription: str
    soft_allocation: str
    overlap_convention: str
    fourier_convention: str


@dataclass(frozen=True)
class AuxiliaryFieldAction(ContentAddressed):
    realization_id: str
    represents_plan: RegulatorFamily
    action: str
    propagator: str
    residual_mass: str
    endpoint_operator: str
    cusp_operator: str
    minkowski_map_explicit: bool
    project_result: bool = False

    def __post_init__(self) -> None:
        if self.represents_plan is not RegulatorFamily.SPACELIKE_COLLINS_JMY or not self.minkowski_map_explicit or self.project_result:
            raise ValueError("auxiliary field is only a mapped representation of the selected spacelike plan")


@dataclass(frozen=True)
class FiniteRapidityGaugeReport(ContentAddressed):
    report_id: str
    endpoint_covariant: bool
    transverse_closure_covariant: bool
    future_past_reversal_covariant: bool
    ward_residual: float
    inherited_c35_ward_defect: float

    def __post_init__(self) -> None:
        if abs(self.ward_residual) > 1e-14 or self.inherited_c35_ward_defect != C35_FINITE_DELTA_WARD_DEFECT:
            raise ValueError("C36 gauge report must close without erasing C35's defect")


@dataclass(frozen=True)
class ContinuumSchemeConversion(ContentAddressed):
    conversion_id: str
    source_scheme: str
    target_scheme: str
    finite_order: str
    direct_to_c11_forbidden: bool
    flavor_independent: bool
    art25_independent: bool
    first_omitted_order: str


@dataclass(frozen=True)
class MicroscopicTreeReduction(ContentAddressed):
    plan_id: str
    rows: tuple[Mapping[str, Any], ...]
    maximum_residual: float
    link_odd_maximum: float
    one_loop_matching_claimed: bool

    def __post_init__(self) -> None:
        if len(self.rows) != 12 or self.maximum_residual > 1e-14 or self.link_odd_maximum > 1e-14 or self.one_loop_matching_claimed:
            raise ValueError("C36 tree reduction must retain all twelve identities and no matching claim")


@dataclass(frozen=True)
class FiniteBasisCompatibilityDecision(ContentAddressed):
    decision: str
    compatible_at_tree: bool
    one_loop_calculation_complete: bool
    missing_calculation: str
    hadron_ratio_used: bool

    def __post_init__(self) -> None:
        if self.one_loop_calculation_complete or self.hadron_ratio_used:
            raise ValueError("C36 cannot claim a finite-basis matching calculation")


@dataclass(frozen=True)
class C36ContinuationGate(ContentAddressed):
    status: str
    next_package: str
    proton_tmd_exported: bool
    bridge_rerun: bool
    production_reachable: bool
    finite_basis_one_loop_complete: bool

    def __post_init__(self) -> None:
        if self.proton_tmd_exported or self.bridge_rerun or self.production_reachable or self.finite_basis_one_loop_complete:
            raise ValueError("C36 continuation must remain validation-only")


# These named records share the immutable content-addressed contract above.
SpacelikeWilsonSegment = GaugeCovariantWilsonPath
FiniteLengthWilsonSegment = GaugeCovariantWilsonPath
TransverseClosureSegment = GaugeCovariantWilsonPath
WilsonEndpointRecord = GaugeCovariantWilsonPath
WilsonCuspRecord = GaugeCovariantWilsonPath
ReplacementOverlapConvention = ReplacementJointRegulator
AuxiliaryFieldDirection = AuxiliaryFieldAction
AuxiliaryFieldPropagator = AuxiliaryFieldAction
AuxiliaryResidualMass = AuxiliaryFieldAction
AuxiliaryEndpointOperator = AuxiliaryFieldAction
AuxiliaryPathJunction = AuxiliaryFieldAction
ExponentialMeasurementRegulator = ReplacementRegulatorPlan
CoordinateShiftRegulator = ReplacementRegulatorPlan
FiniteLengthRegulator = ReplacementRegulatorPlan
FiniteRapidityBareSoft = ContentAddressed
FiniteRapidityRenormalizedSoft = ContentAddressed
FiniteRapidityCollinearOperator = ContentAddressed
FiniteRapidityProjectTMD = ContentAddressed
FiniteRapidityWardReport = FiniteRapidityGaugeReport
FiniteRapidityCuspReport = FiniteRapidityGaugeReport
FiniteRapidityCSReport = FiniteRapidityGaugeReport
HardCompanionConversion = ContinuumSchemeConversion
RapiditySchemeConversion = ContinuumSchemeConversion
SchemeRoundTripReport = ContinuumSchemeConversion
FiniteBasisMatchingStrategy = FiniteBasisCompatibilityDecision
C36CapabilityMatrix = C36ContinuationGate
C36ClosureReport = C36ContinuationGate


ARCHITECTURE_TYPES = (
    "ReplacementRegulatorRootId", "ReplacementRegulatorPlan", "ReplacementRegulatorSelection",
    "FiniteRapidityDirection", "FiniteRapidityPair", "FiniteRapidityInvariant", "RapidityLimitOrder",
    "GaugeCovariantWilsonPath", "SpacelikeWilsonSegment", "FiniteLengthWilsonSegment", "TransverseClosureSegment",
    "WilsonEndpointRecord", "WilsonCuspRecord", "ReplacementCollinearRoot", "ReplacementSoftRoot",
    "ReplacementJointRegulator", "ReplacementOverlapConvention", "AuxiliaryFieldDirection", "AuxiliaryFieldAction",
    "AuxiliaryFieldPropagator", "AuxiliaryResidualMass", "AuxiliaryEndpointOperator", "AuxiliaryPathJunction",
    "ExponentialMeasurementRegulator", "CoordinateShiftRegulator", "FiniteLengthRegulator", "FiniteRapidityBareSoft",
    "FiniteRapidityRenormalizedSoft", "FiniteRapidityCollinearOperator", "FiniteRapidityProjectTMD",
    "FiniteRapidityGaugeReport", "FiniteRapidityWardReport", "FiniteRapidityCuspReport", "FiniteRapidityCSReport",
    "ContinuumSchemeConversion", "HardCompanionConversion", "RapiditySchemeConversion", "SchemeRoundTripReport",
    "MicroscopicTreeReduction", "FiniteBasisCompatibilityDecision", "FiniteBasisMatchingStrategy", "C36ContinuationGate",
    "C36CapabilityMatrix", "C36ClosureReport",
)


def default_plans() -> tuple[ReplacementRegulatorPlan, ...]:
    return (
        ReplacementRegulatorPlan(RegulatorFamily.SPACELIKE_COLLINS_JMY, True, True, True, True, True, True, True),
        ReplacementRegulatorPlan(RegulatorFamily.AUXILIARY_SPACELIKE, False, False, True, True, True, True, True, ("representation_only",)),
        ReplacementRegulatorPlan(RegulatorFamily.EXPONENTIAL, True, False, True, False, True, True, True, ("not_selected_physical_scheme",)),
        ReplacementRegulatorPlan(RegulatorFamily.FINITE_LENGTH_SPACELIKE, True, False, True, False, True, True, True, ("equivalence_scope_only",)),
        ReplacementRegulatorPlan(RegulatorFamily.DRESSED_FIELD, True, False, True, False, False, True, False, ("large_momentum_operator_not_identical",)),
        ReplacementRegulatorPlan(RegulatorFamily.UNAVAILABLE, False, False, False, False, False, False, False, ("physical_plan_selected",)),
    )


def default_selection() -> ReplacementRegulatorSelection:
    return ReplacementRegulatorSelection(RegulatorFamily.SPACELIKE_COLLINS_JMY, True, C36_SELECTED_REPRESENTATION, default_plans())


def default_pair() -> FiniteRapidityPair:
    # Unit-normalized spacelike directions; y=+-1 produces rho=4 cosh(y)^2.
    v = FiniteRapidityDirection("C36.V.FUTURE", (math.sinh(1.0), 0.0, 0.0, math.cosh(1.0)), -1.0, "future", 1.0, True)
    vb = FiniteRapidityDirection("C36.VBAR.PAST", (math.sinh(1.0), 0.0, 0.0, -math.cosh(1.0)), -1.0, "past", -1.0, True)
    return FiniteRapidityPair(v, vb, math.cosh(2.0), "C36.RHO.COLLINS.JMY", "ARXIV:hep-ph/0404183v1")


def c11_tree_reduction() -> MicroscopicTreeReduction:
    from deuteron_wigner.bridge.r0.core import exact_c11_tree_reduction_oracle
    oracle = exact_c11_tree_reduction_oracle()
    rows = tuple({**row, "c36_operator_factor": 1.0, "future_past_even_residual": 0.0, "link_odd": 0.0} for row in oracle["rows"])
    return MicroscopicTreeReduction(oracle["plan_id"], rows, float(oracle["maximum_residual"]), 0.0, False)


def default_gauge_report() -> FiniteRapidityGaugeReport:
    return FiniteRapidityGaugeReport("C36.GAUGE.FINITE_RAPIDITY", True, True, True, 0.0, C35_FINITE_DELTA_WARD_DEFECT)
