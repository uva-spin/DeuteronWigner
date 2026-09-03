"""Typed C35/S0C regulator-completion contracts.

The C35 package is an additive descendant of the immutable C33/C34 soft
roots.  It records the exact light-front convention and mathematical chart
oracles that can be established without choosing a new physical regulator.
It also encodes the source-supported no-go: the selected modified-delta
Wilson operator does not have the gauge properties of the original Wilson
operator at finite delta, and the repository contains no regulator-identical
finite-cell BRST/Krein, light-front-physical, or auxiliary completion.

Consequently the authoritative default selects ``S0C-UNAVAILABLE``.  No
finite-basis one-loop coefficient, counterterm, microscopic proton TMD,
bridge result, inference object, or production route can be constructed by
this module.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
from hashlib import sha256
import json
import math
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

from ..s0.core import (
    C32_COLLINEAR_ROOT,
    C33_BASIS_REGULATOR_ID,
    C33_IR_REGULATOR_ID,
    C33_RAPIDITY_REGULATOR_ID,
    C33_SOFT_ROOT,
    C33_SOURCE_SOFT_SCHEME,
    C33_TARGET_SOFT_SCHEME,
    C33_UV_REGULATOR_ID,
    C33_WILSON_GEOMETRY,
)


C35_SCOPE = "C35/S0C"
C35_BASELINE_COMMIT = "6bdb44be2afc79e817f69ce0e35813da8a394db7"
C35_C33_BASELINE = "e0b34c74e8f39c9d42cf49cc598f1533d9353a7e"
C35_C32_ANCESTOR = "0d7b94a5e86882b23a56d4c1f11900d554756a18"
C35_C28_ANCESTOR = "52678312906bf5cc0bb8664e2486d5d676a6b723"
C35_DESCENDANT_ROOT = "C35_SOFT_REGULATOR_COMPLETION_DESCENDANT"
C34_DESCENDANT_ROOT = "C34_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ONE_LOOP_DESCENDANT"
C34_IMPLEMENTATION_REPORT_SHA256 = "aa66b448518dd493ae237822712c15ea160a73aa9cc5257df59fb83722f7ebe1"
C34_REQUIREMENT_COVERAGE_SHA256 = "0a94dfd213bd67ea6f4da498ff0095f38136d5a68c89b0c0ae3d30febb610d5e"
C35_PROMPT_SHA256 = "1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"
MODIFIED_DELTA_SOURCE_SHA256 = "dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d"

C35_PRIMARY_NO_GO = "C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE"
C35_SECONDARY_MODE_NO_GO = "C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE"
C35_OUTCOME_BRANCH = "G"
C35_NEXT_PACKAGE = "C36/O4 — replacement regulator architecture for the microscopic TMD soft root"
NONZERO_UNKNOWN = "NONZERO_UNKNOWN"
EMPTY_NOT_ZERO = "EMPTY_NOT_ZERO"


REQUIRED_ONE_LOOP_CONTRIBUTIONS = (
    "N_NBAR_EXCHANGE",
    "CONJUGATE_LINE_EXCHANGE",
    "SAME_DIRECTION_LINE_EXCHANGE",
    "REAL_ONE_SOFT_GLUON",
    "VIRTUAL_ONE_SOFT_GLUON",
    "WILSON_LINE_SELF_ENERGY",
    "CUSP_ENDPOINT",
    "TRANSVERSE_CLOSURE",
    "AUXILIARY_FIELD_SELF_ENERGY",
    "SOFT_VACUUM_ENERGY",
    "LIGHT_FRONT_INSTANTANEOUS",
    "GAUGE_FIXING",
    "GHOST",
    "ZERO_MODE",
    "BASIS_BOUNDARY",
    "RAPIDITY_COUNTERTERM",
    "UV_COUNTERTERM",
    "RESIDUAL_LINE_MASS_COUNTERTERM",
)


ARCHITECTURE_TYPES = (
    "GaugeCompleteSoftPlan",
    "CovariantKreinPlan",
    "LightFrontPhysicalPlan",
    "GaugePlanSupersession",
    "LightFrontConvention",
    "NullVectorNormalization",
    "RapidityRegulatorRescaling",
    "SoftCoordinateChart",
    "RealSoftCoordinateChart",
    "VirtualSoftCoordinateChart",
    "SoftJacobian",
    "SoftCell",
    "SoftCellBoundary",
    "SoftCellShape",
    "SoftCellMeasure",
    "SoftCellQuadrature",
    "SoftPartitionOfUnity",
    "SoftRefinementMap",
    "SoftModeCollection",
    "SoftGaugeMode",
    "SoftPolarizationMetric",
    "SoftGhostMode",
    "SoftAuxiliaryMode",
    "SoftInstantaneousKernel",
    "SoftFreeAction",
    "SoftFreeHamiltonian",
    "RealCutMeasure",
    "VirtualLoopMeasure",
    "VirtualContourPlan",
    "PoleCellPartition",
    "SingularCellSubtraction",
    "WilsonSegmentParameterization",
    "LongitudinalWilsonSegment",
    "TransverseInfinitySegment",
    "ModifiedDeltaDampingOperator",
    "FiniteSegmentLimit",
    "ExecutableEikonalVertex",
    "ExecutableLinePairKernel",
    "ExecutableSelfKernel",
    "ExecutableCuspKernel",
    "ExecutableBoundaryKernel",
    "SoftZeroModeSector",
    "SoftBoundarySector",
    "SoftBRSTOrConstraintReport",
    "SoftBareOneLoopResult",
    "SoftCountertermSystem",
    "SoftRenormalizedOneLoopResult",
    "SoftTrajectoryFamily",
    "SoftTrajectoryAxis",
    "SoftTrajectoryResult",
    "SoftSideOverlapObject",
    "C35CapabilityMatrix",
    "C35ClosureReport",
)


HOLDOUT_IDS = (
    "C35.HOLDOUT.GAUGE_PARAMETER",
    "C35.HOLDOUT.CONSTRAINT_MODE",
    "C35.HOLDOUT.GHOST_PROOF",
    "C35.HOLDOUT.REAL_MODE_CELL",
    "C35.HOLDOUT.VIRTUAL_CONTOUR_POINT",
    "C35.HOLDOUT.SINGULAR_POLE_CELL",
    "C35.HOLDOUT.LINE_PAIR_COEFFICIENT",
    "C35.HOLDOUT.SAME_DIRECTION_COEFFICIENT",
    "C35.HOLDOUT.WILSON_SELF_ENERGY",
    "C35.HOLDOUT.CUSP_ENDPOINT",
    "C35.HOLDOUT.TRANSVERSE_JUNCTION",
    "C35.HOLDOUT.ZERO_MODE",
    "C35.HOLDOUT.BASIS_BOUNDARY",
    "C35.HOLDOUT.DELTA_PLUS",
    "C35.HOLDOUT.DELTA_MINUS",
    "C35.HOLDOUT.DELTA_DIAGONAL",
    "C35.HOLDOUT.B_POINT",
    "C35.HOLDOUT.B_TO_ZERO",
    "C35.HOLDOUT.UV_SUPPORT",
    "C35.HOLDOUT.IR_SUPPORT",
    "C35.HOLDOUT.RAPIDITY_WINDOW",
    "C35.HOLDOUT.TRANSVERSE_REFINEMENT",
    "C35.HOLDOUT.CONTINUUM_ORACLE",
    "C35.HOLDOUT.COUNTERTERM",
    "C35.HOLDOUT.CONVERSION_ROUNDTRIP",
    "C35.HOLDOUT.SOFT_SIDE_ZERO_BIN",
    "C35.HOLDOUT.ART25_INDEPENDENCE",
)


BENCHMARK_FAMILIES = tuple("S0C-" + chr(ord("A") + index) for index in range(18))


class GaugePlanKind(str, Enum):
    COVARIANT_KREIN = "S0C-COVARIANT-KREIN"
    LIGHT_FRONT_PHYSICAL = "S0C-LIGHT_FRONT-PHYSICAL"
    AUXILIARY_EIKONAL = "S0C-AUXILIARY-EIKONAL"
    UNAVAILABLE = "S0C-UNAVAILABLE"


class ContributionStatus(str, Enum):
    CALCULATED_NONZERO = "CALCULATED_NONZERO"
    CALCULATED_ZERO_BY_EXACT_IDENTITY = "CALCULATED_ZERO_BY_EXACT_IDENTITY"
    CANCELS_WITH_DECLARED_PARTNER = "CANCELS_WITH_DECLARED_PARTNER"
    TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO = (
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO"
    )
    NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF = "NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF"
    UNRESOLVED_BLOCKING = "UNRESOLVED_BLOCKING"


def _canonical(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, complex):
        if not math.isfinite(value.real) or not math.isfinite(value.imag):
            raise ValueError("C35_NONFINITE_COMPLEX_NOT_SERIALIZABLE")
        return {"real": value.real, "imag": value.imag}
    if is_dataclass(value):
        payload = {field.name: _canonical(getattr(value, field.name)) for field in fields(value)}
        if isinstance(value, _ContentAddressed):
            payload["c35_identity_envelope"] = _canonical(value.c35_identity_envelope)
        return payload
    if isinstance(value, Mapping):
        return {str(key): _canonical(value[key]) for key in sorted(value)}
    if isinstance(value, (tuple, list)):
        return [_canonical(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("C35_NONFINITE_FLOAT_NOT_SERIALIZABLE")
    return value


def deterministic_json(value: Any) -> str:
    return json.dumps(
        _canonical(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def content_hash(value: Any) -> str:
    return sha256(deterministic_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class C35IdentityEnvelope:
    envelope_version: str
    object_type: str
    object_identity: str
    scope: str
    baseline_commit: str
    parent_c34_completion_commit: str
    parent_c34_descendant_root_id: str
    parent_c34_implementation_report_sha256: str
    parent_c34_requirement_coverage_sha256: str
    parent_soft_root_id: str
    descendant_root_id: str
    collinear_root_id: str
    baryon_number: int
    gauge_plan: str
    rapidity_regulator: str
    uv_regulator: str
    ir_regulator: str
    basis_regulator: str
    light_front_convention_id: str
    real_coordinate_chart_id: str
    virtual_coordinate_chart_id: str
    mode_collection_status: str
    wilson_segment_status: str
    derivation_authority: str
    modified_delta_source_sha256: str
    state_independence_required: bool
    state_independence_proved: bool
    hadron_independence_required: bool
    hadron_independence_proved: bool
    consumes_art25: bool
    consumes_process_data: bool
    consumes_bridge_residuals: bool
    inference_reachable: bool
    production_reachable: bool

    def __post_init__(self) -> None:
        if self.scope != C35_SCOPE or self.baseline_commit != C35_BASELINE_COMMIT:
            raise ValueError("C35_IDENTITY_SCOPE_OR_BASELINE_MISMATCH")
        if (
            self.parent_c34_completion_commit != C35_BASELINE_COMMIT
            or self.parent_c34_descendant_root_id != C34_DESCENDANT_ROOT
            or self.parent_c34_implementation_report_sha256 != C34_IMPLEMENTATION_REPORT_SHA256
            or self.parent_c34_requirement_coverage_sha256 != C34_REQUIREMENT_COVERAGE_SHA256
        ):
            raise ValueError("C35_C34_PARENT_IDENTITY_MISMATCH")
        if self.parent_soft_root_id != C33_SOFT_ROOT or self.collinear_root_id != C32_COLLINEAR_ROOT:
            raise ValueError("C35_PARENT_ROOT_MISMATCH")
        if self.descendant_root_id != C35_DESCENDANT_ROOT or self.baryon_number != 0:
            raise ValueError("C35_DESCENDANT_ROOT_OR_BARYON_MISMATCH")
        if self.gauge_plan not in {plan.value for plan in GaugePlanKind}:
            raise ValueError("C35_UNKNOWN_GAUGE_PLAN_IDENTITY")
        if self.light_front_convention_id != "C35.LF.CONVENTION.SQRT2.v1":
            raise ValueError("C35_LIGHT_FRONT_CONVENTION_IDENTITY_MISMATCH")
        if (
            self.real_coordinate_chart_id != "C35.REAL.CHART.KAPPA_Y_PHI.v1"
            or self.virtual_coordinate_chart_id != "C35.VIRTUAL.CHART.KPLUS_KMINUS_KX_KY.v1"
        ):
            raise ValueError("C35_COORDINATE_CHART_IDENTITY_MISMATCH")
        if self.modified_delta_source_sha256 != MODIFIED_DELTA_SOURCE_SHA256:
            raise ValueError("C35_MODIFIED_DELTA_SOURCE_IDENTITY_MISMATCH")
        if not all((self.mode_collection_status, self.wilson_segment_status, self.derivation_authority)):
            raise ValueError("C35_IDENTITY_ENVELOPE_COMPLETION_FIELD_MISSING")
        if not self.state_independence_required or not self.hadron_independence_required:
            raise ValueError("C35_SOFT_UNIVERSALITY_REQUIREMENT_MISSING")
        if self.gauge_plan == GaugePlanKind.UNAVAILABLE.value and (
            self.state_independence_proved or self.hadron_independence_proved
        ):
            raise ValueError("C35_UNAVAILABLE_REGULATOR_CANNOT_PROVE_UNIVERSALITY")
        if any(
            (
                self.consumes_art25,
                self.consumes_process_data,
                self.consumes_bridge_residuals,
                self.inference_reachable,
                self.production_reachable,
            )
        ):
            raise ValueError("C35_FORBIDDEN_REACHABILITY")


class _ContentAddressed:
    @property
    def c35_identity_envelope(self) -> C35IdentityEnvelope:
        identity = type(self).__name__
        for field in fields(self):
            if field.name.endswith("_id"):
                candidate = getattr(self, field.name)
                if isinstance(candidate, str) and candidate:
                    identity = candidate
                    break
        gauge_candidate = getattr(self, "gauge_plan", None)
        if gauge_candidate is None:
            gauge_candidate = getattr(self, "gauge_realization", None)
        if gauge_candidate is None:
            gauge_candidate = getattr(self, "selected", None)
        if gauge_candidate is None:
            gauge_candidate = getattr(self, "kind", None)
        if isinstance(gauge_candidate, GaugePlanKind):
            gauge_identity = gauge_candidate.value
        elif gauge_candidate in {plan.value for plan in GaugePlanKind}:
            gauge_identity = str(gauge_candidate)
        else:
            gauge_identity = GaugePlanKind.UNAVAILABLE.value
        mode_status = str(getattr(self, "mode_collection_status", EMPTY_NOT_ZERO))
        wilson_status = str(getattr(self, "wilson_segment_status", EMPTY_NOT_ZERO))
        derivation_authority = str(
            getattr(self, "derivation_authority", "C35_SOURCE_AUDIT_AND_EXACT_KINEMATICS")
        )
        return C35IdentityEnvelope(
            envelope_version="C35.IDENTITY.ENVELOPE.v1",
            object_type=type(self).__name__,
            object_identity=identity,
            scope=C35_SCOPE,
            baseline_commit=C35_BASELINE_COMMIT,
            parent_c34_completion_commit=C35_BASELINE_COMMIT,
            parent_c34_descendant_root_id=C34_DESCENDANT_ROOT,
            parent_c34_implementation_report_sha256=C34_IMPLEMENTATION_REPORT_SHA256,
            parent_c34_requirement_coverage_sha256=C34_REQUIREMENT_COVERAGE_SHA256,
            parent_soft_root_id=C33_SOFT_ROOT,
            descendant_root_id=C35_DESCENDANT_ROOT,
            collinear_root_id=C32_COLLINEAR_ROOT,
            baryon_number=0,
            gauge_plan=gauge_identity,
            rapidity_regulator=C33_RAPIDITY_REGULATOR_ID,
            uv_regulator=C33_UV_REGULATOR_ID,
            ir_regulator=C33_IR_REGULATOR_ID,
            basis_regulator=C33_BASIS_REGULATOR_ID,
            light_front_convention_id="C35.LF.CONVENTION.SQRT2.v1",
            real_coordinate_chart_id="C35.REAL.CHART.KAPPA_Y_PHI.v1",
            virtual_coordinate_chart_id="C35.VIRTUAL.CHART.KPLUS_KMINUS_KX_KY.v1",
            mode_collection_status=mode_status,
            wilson_segment_status=wilson_status,
            derivation_authority=derivation_authority,
            modified_delta_source_sha256=MODIFIED_DELTA_SOURCE_SHA256,
            state_independence_required=True,
            state_independence_proved=bool(getattr(self, "state_independence_proved", False)),
            hadron_independence_required=True,
            hadron_independence_proved=bool(getattr(self, "hadron_independence_proved", False)),
            consumes_art25=False,
            consumes_process_data=False,
            consumes_bridge_residuals=False,
            inference_reachable=False,
            production_reachable=False,
        )

    @property
    def deterministic_json(self) -> str:
        return deterministic_json(self)

    @property
    def content_hash(self) -> str:
        return content_hash(self)


@dataclass(frozen=True)
class GaugePlanCandidate(_ContentAddressed):
    plan_id: str
    kind: GaugePlanKind
    supported: bool
    gauge_complete_at_finite_regulator: bool
    regulator_identical: bool
    source_authority: Tuple[str, ...]
    blockers: Tuple[str, ...]
    coefficient_execution_allowed: bool = False

    def __post_init__(self) -> None:
        if not self.plan_id or not self.source_authority:
            raise ValueError("C35_GAUGE_PLAN_ID_OR_EVIDENCE_MISSING")
        validated = self.supported and self.gauge_complete_at_finite_regulator and self.regulator_identical
        if validated and self.blockers:
            raise ValueError("C35_VALIDATED_GAUGE_PLAN_CANNOT_RETAIN_BLOCKERS")
        if not validated and not self.blockers:
            raise ValueError("C35_UNVALIDATED_GAUGE_PLAN_REQUIRES_BLOCKERS")
        if self.coefficient_execution_allowed:
            if not validated:
                raise ValueError("C35_GAUGE_PLAN_EXECUTION_WITH_OPEN_IDENTITY")


@dataclass(frozen=True)
class GaugePlanSelection(_ContentAddressed):
    selection_id: str
    candidates: Tuple[GaugePlanCandidate, ...]
    selected: GaugePlanKind
    frozen_before_coefficient: bool
    coefficient_attempted: bool
    primary_no_go: str
    outcome_branch: str
    exact_next_package: str

    def __post_init__(self) -> None:
        if tuple(candidate.kind for candidate in self.candidates) != tuple(GaugePlanKind):
            raise ValueError("C35_ALL_MUTUALLY_EXCLUSIVE_GAUGE_PLANS_REQUIRED")
        if not self.frozen_before_coefficient:
            raise ValueError("C35_PLAN_MUST_BE_FROZEN_BEFORE_COEFFICIENT")
        selected = {candidate.kind: candidate for candidate in self.candidates}[self.selected]
        if self.selected is GaugePlanKind.UNAVAILABLE:
            if self.coefficient_attempted:
                raise ValueError("C35_COEFFICIENT_ATTEMPTED_WITH_UNAVAILABLE_PLAN")
            if not self.primary_no_go or not self.exact_next_package:
                raise ValueError("C35_UNAVAILABLE_SELECTION_REQUIRES_NO_GO_AND_NEXT_PACKAGE")
        elif not (
            selected.supported
            and selected.gauge_complete_at_finite_regulator
            and selected.regulator_identical
        ):
            raise ValueError("C35_UNSUPPORTED_GAUGE_PLAN_SELECTED")


def default_gauge_plan_selection() -> GaugePlanSelection:
    candidates = (
        GaugePlanCandidate(
            "C35.GAUGE.CANDIDATE.COVARIANT_KREIN",
            GaugePlanKind.COVARIANT_KREIN,
            False,
            False,
            False,
            ("ARXIV:1511.05590v2:p4",),
            (
                "NO_FINITE_CELL_BRST_KREIN_ACTION_OR_METRIC",
                "MODIFIED_DELTA_WILSON_LINES_LACK_ORIGINAL_GAUGE_PROPERTIES_AT_FINITE_DELTA",
                "NO_ZERO_MODE_OR_TRANSVERSE_BOUNDARY_COMPLETION",
            ),
        ),
        GaugePlanCandidate(
            "C35.GAUGE.CANDIDATE.LIGHT_FRONT_PHYSICAL",
            GaugePlanKind.LIGHT_FRONT_PHYSICAL,
            False,
            False,
            False,
            ("ARXIV:1612.07740v1:LIGHT_FRONT_COMPARISON_ONLY",),
            (
                "NO_INSTANTANEOUS_GLUON_KERNEL",
                "NO_CONSTRAINED_ZERO_MODE_OR_RESIDUAL_GAUGE_PRESCRIPTION",
                "NO_PROVED_MAP_TO_COVARIANT_MODIFIED_DELTA_SOFT_FUNCTION",
            ),
        ),
        GaugePlanCandidate(
            "C35.GAUGE.CANDIDATE.AUXILIARY_EIKONAL",
            GaugePlanKind.AUXILIARY_EIKONAL,
            False,
            False,
            False,
            ("ARXIV:2312.04315v3:AUXILIARY_METHOD_ONLY",),
            (
                "EUCLIDEAN_SPACELIKE_OPERATOR_NOT_LIGHTLIKE_MINKOWSKI_MODIFIED_DELTA",
                "NO_ENDPOINT_OR_FINITE_REGULATOR_CONVERSION",
            ),
        ),
        GaugePlanCandidate(
            "C35.GAUGE.CANDIDATE.UNAVAILABLE",
            GaugePlanKind.UNAVAILABLE,
            True,
            False,
            True,
            ("C35_SOURCE_AUDIT",),
            ("NO_SUPPORTED_GAUGE_COMPLETE_REGULATOR_IDENTICAL_REALIZATION",),
        ),
    )
    return GaugePlanSelection(
        "C35.GAUGE.PLAN.SELECTION.v1",
        candidates,
        GaugePlanKind.UNAVAILABLE,
        True,
        False,
        C35_PRIMARY_NO_GO,
        C35_OUTCOME_BRANCH,
        C35_NEXT_PACKAGE,
    )


@dataclass(frozen=True)
class LightFrontConvention(_ContentAddressed):
    convention_id: str = "C35.LF.CONVENTION.SQRT2.v1"
    metric_signature: str = "+---"
    component_definition: str = "v_plus_minus=(v0+/-v3)/sqrt(2)"
    n: Tuple[float, float, float, float] = (1.0 / math.sqrt(2.0), 0.0, 0.0, 1.0 / math.sqrt(2.0))
    nbar: Tuple[float, float, float, float] = (1.0 / math.sqrt(2.0), 0.0, 0.0, -1.0 / math.sqrt(2.0))
    fourier_convention: str = "A(x)=integral[d4k/(2pi)^4] exp(-i k.x) A(k)"

    def __post_init__(self) -> None:
        if self.metric_signature != "+---":
            raise ValueError("C35_METRIC_SIGNATURE_CHANGED")
        if abs(self.dot(self.n, self.n)) > 1.0e-15 or abs(self.dot(self.nbar, self.nbar)) > 1.0e-15:
            raise ValueError("C35_NULL_VECTOR_NOT_NULL")
        if abs(self.dot(self.n, self.nbar) - 1.0) > 1.0e-15:
            raise ValueError("C35_NULL_VECTOR_NORMALIZATION_NOT_ONE")

    @staticmethod
    def dot(a: Sequence[float], b: Sequence[float]) -> float:
        if len(a) != 4 or len(b) != 4:
            raise ValueError("C35_MINKOWSKI_VECTOR_DIMENSION")
        return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]

    @staticmethod
    def plus_minus(v: Sequence[float]) -> Tuple[float, float]:
        if len(v) != 4:
            raise ValueError("C35_LIGHT_FRONT_VECTOR_DIMENSION")
        return ((v[0] + v[3]) / math.sqrt(2.0), (v[0] - v[3]) / math.sqrt(2.0))

    @staticmethod
    def reconstruct(plus: float, minus: float, transverse: Tuple[float, float]) -> Tuple[float, float, float, float]:
        return (
            (plus + minus) / math.sqrt(2.0),
            transverse[0],
            transverse[1],
            (plus - minus) / math.sqrt(2.0),
        )

    def pole_components(self, k: Sequence[float]) -> Tuple[float, float]:
        return self.dot(self.nbar, k), self.dot(self.n, k)


@dataclass(frozen=True)
class RapidityRegulatorRescaling(_ContentAddressed):
    rescaling_id: str = "C35.NULL.DELTA.RESCALING.v1"
    law: str = "n->lambda*n;nbar->lambda^-1*nbar;delta_minus->lambda*delta_minus;delta_plus->lambda^-1*delta_plus"
    source_to_project_delta_scale: float = 1.0 / math.sqrt(2.0)

    def transform(self, lam: float, delta_plus: float, delta_minus: float) -> Tuple[float, float]:
        if lam <= 0.0 or delta_plus <= 0.0 or delta_minus <= 0.0:
            raise ValueError("C35_DELTA_RESCALING_POSITIVE_INPUT_REQUIRED")
        return delta_plus / lam, delta_minus * lam

    def invariant_product(self, lam: float, delta_plus: float, delta_minus: float) -> float:
        transformed = self.transform(lam, delta_plus, delta_minus)
        return transformed[0] * transformed[1]


@dataclass(frozen=True)
class RealSoftCoordinateChart(_ContentAddressed):
    chart_id: str = "C35.REAL.CHART.KAPPA_Y_PHI.v1"
    coordinates: Tuple[str, str, str] = ("kappa", "y", "phi")
    domain: str = "kappa>0;y_finite;phi_in_[0,2pi)"
    measure: str = "kappa*dkappa*dy*dphi/[2*(2pi)^3]"
    status: str = "EXECUTABLE_GEOMETRIC_CHART_NOT_GAUGE_MODE_BASIS"

    @staticmethod
    def map(kappa: float, rapidity: float, phi: float) -> Tuple[float, float, float, float]:
        if kappa <= 0.0 or not all(math.isfinite(value) for value in (rapidity, phi)):
            raise ValueError("C35_REAL_CHART_DOMAIN")
        k_plus = kappa * math.exp(rapidity) / math.sqrt(2.0)
        k_minus = kappa * math.exp(-rapidity) / math.sqrt(2.0)
        return k_plus, k_minus, kappa * math.cos(phi), kappa * math.sin(phi)

    @staticmethod
    def mass_shell_residual(momentum: Sequence[float]) -> float:
        k_plus, k_minus, kx, ky = momentum
        return 2.0 * k_plus * k_minus - kx * kx - ky * ky

    @staticmethod
    def measure_density(kappa: float) -> float:
        if kappa <= 0.0:
            raise ValueError("C35_REAL_MEASURE_POSITIVE_KAPPA_REQUIRED")
        return kappa / (2.0 * (2.0 * math.pi) ** 3)


@dataclass(frozen=True)
class VirtualSoftCoordinateChart(_ContentAddressed):
    chart_id: str = "C35.VIRTUAL.CHART.KPLUS_KMINUS_KX_KY.v1"
    coordinates: Tuple[str, str, str, str] = ("k_plus", "k_minus", "k_x", "k_y")
    measure: str = "dk_plus*dk_minus*dk_x*dk_y/(2pi)^4"
    propagator_denominator: str = "2*k_plus*k_minus-kT^2+i0"
    contour_status: str = "UNRESOLVED_BLOCKING_NO_REGULATOR_IDENTICAL_CONTOUR"

    @staticmethod
    def invariant(momentum: Sequence[float]) -> float:
        k_plus, k_minus, kx, ky = momentum
        return 2.0 * k_plus * k_minus - kx * kx - ky * ky

    @staticmethod
    def measure_density() -> float:
        return 1.0 / (2.0 * math.pi) ** 4


@dataclass(frozen=True)
class SoftCellBoundary(_ContentAddressed):
    boundary_id: str
    lower: Tuple[float, ...]
    upper: Tuple[float, ...]
    chart_id: str

    def __post_init__(self) -> None:
        if len(self.lower) != len(self.upper) or not self.lower:
            raise ValueError("C35_CELL_BOUNDARY_DIMENSION")
        if any(not lo < hi for lo, hi in zip(self.lower, self.upper)):
            raise ValueError("C35_CELL_BOUNDARY_ORDER")


@dataclass(frozen=True)
class SoftCellPrototype(_ContentAddressed):
    cell_id: str
    boundary: SoftCellBoundary
    measure_value: float
    top_hat_normalization: float
    status: str = "NORMALIZED_SCALAR_CELL_PROTOTYPE_NOT_GAUGE_MODE"

    def __post_init__(self) -> None:
        if self.measure_value <= 0.0 or self.top_hat_normalization <= 0.0:
            raise ValueError("C35_CELL_MEASURE_OR_NORMALIZATION_INVALID")
        residual = self.measure_value * self.top_hat_normalization ** 2 - 1.0
        if abs(residual) > 2.0e-14:
            raise ValueError("C35_TOP_HAT_CELL_NOT_NORMALIZED")


def real_cell_prototype(
    cell_id: str,
    kappa_interval: Tuple[float, float],
    y_interval: Tuple[float, float],
    phi_interval: Tuple[float, float],
) -> SoftCellPrototype:
    boundary = SoftCellBoundary(
        cell_id + ".BOUNDARY",
        (kappa_interval[0], y_interval[0], phi_interval[0]),
        (kappa_interval[1], y_interval[1], phi_interval[1]),
        RealSoftCoordinateChart().chart_id,
    )
    k0, k1 = kappa_interval
    y0, y1 = y_interval
    p0, p1 = phi_interval
    volume = (
        0.25
        * (k1 * k1 - k0 * k0)
        * (y1 - y0)
        * (p1 - p0)
        / (2.0 * math.pi) ** 3
    )
    return SoftCellPrototype(cell_id, boundary, volume, 1.0 / math.sqrt(volume))


@dataclass(frozen=True)
class ModifiedDeltaDampingOperator(_ContentAddressed):
    operator_id: str = "C35.MODIFIED.DELTA.FINITE.SEGMENT.v1"
    source_locator: str = "ARXIV:1511.05590v2:p3:Eqs.(5)-(6);p4:gauge-property warning"
    gauge_property_at_finite_delta: bool = False
    gauge_property_restored_only_in_delta_limit: bool = True
    power_delta_terms_must_be_discarded: bool = True

    @staticmethod
    def finite_segment_factor(omega: float, delta: float, length: float) -> complex:
        if delta <= 0.0 or length <= 0.0 or not math.isfinite(omega):
            raise ValueError("C35_MODIFIED_DELTA_SEGMENT_DOMAIN")
        exponent = complex(-delta, omega)
        # ``cmath`` has no ``expm1`` on the supported Python 3.9 runtime.
        # The domain enforces delta>0, so the denominator cannot vanish.
        return (cmath.exp(exponent * length) - 1.0) / exponent

    @staticmethod
    def infinite_segment_factor(omega: float, delta: float) -> complex:
        if delta <= 0.0 or not math.isfinite(omega):
            raise ValueError("C35_MODIFIED_DELTA_INFINITE_DOMAIN")
        return 1.0 / complex(delta, -omega)

    @staticmethod
    def ward_bulk_defect(omega: float, delta: float, length: float) -> complex:
        factor = ModifiedDeltaDampingOperator.finite_segment_factor(omega, delta, length)
        endpoint = cmath.exp(complex(-delta, omega) * length) - 1.0
        return 1j * omega * factor - endpoint


@dataclass(frozen=True)
class SingularCellOracle(_ContentAddressed):
    oracle_id: str = "C35.SINGULAR.CELL.PV.CUT.v1"
    center_sampling_forbidden: bool = True
    physical_cells_executed: int = 0
    status: str = "ANALYTIC_METHOD_ORACLE_ONLY"

    @staticmethod
    def principal_value_constant(lower: float, upper: float, pole: float = 0.0) -> float:
        if not lower < pole < upper:
            raise ValueError("C35_PV_ORACLE_REQUIRES_INTERIOR_POLE")
        return math.log(abs(upper - pole)) - math.log(abs(lower - pole))

    @staticmethod
    def distributional_constant(
        lower: float, upper: float, pole: float = 0.0, pole_sign: int = -1
    ) -> complex:
        if pole_sign not in (-1, 1):
            raise ValueError("C35_POLE_SIGN_INVALID")
        pv = SingularCellOracle.principal_value_constant(lower, upper, pole)
        # 1/(x - i0) = PV(1/x) + i*pi*delta(x).
        return complex(pv, pole_sign * math.pi)

    @staticmethod
    def finite_delta_constant(
        lower: float, upper: float, delta: float, pole: float = 0.0, pole_sign: int = -1
    ) -> complex:
        if not lower < upper or delta <= 0.0 or pole_sign not in (-1, 1):
            raise ValueError("C35_FINITE_DELTA_CELL_DOMAIN")
        shift = complex(pole, pole_sign * delta)
        return cmath.log(upper - shift) - cmath.log(lower - shift)


@dataclass(frozen=True)
class ArchitectureObjectRecord(_ContentAddressed):
    record_id: str
    object_type: str
    status: str
    implemented_scope: str
    blockers: Tuple[str, ...]
    positive_regulator_claim: bool = False

    def __post_init__(self) -> None:
        if self.object_type not in ARCHITECTURE_TYPES:
            raise ValueError("C35_UNKNOWN_ARCHITECTURE_OBJECT")
        if self.positive_regulator_claim:
            raise ValueError("C35_POSITIVE_REGULATOR_CLAIM_FORBIDDEN_ON_BRANCH_G")
        if not self.status or not self.implemented_scope:
            raise ValueError("C35_ARCHITECTURE_RECORD_INCOMPLETE")


@dataclass(frozen=True)
class SoftContributionResult(_ContentAddressed):
    contribution_id: str
    contribution_class: str
    status: ContributionStatus
    expression: str
    blocking: bool
    exact_missing_calculation: str
    gauge_action_proof: Optional[str] = None

    def __post_init__(self) -> None:
        if self.contribution_class not in REQUIRED_ONE_LOOP_CONTRIBUTIONS:
            raise ValueError("C35_UNKNOWN_CONTRIBUTION_CLASS")
        if self.status is ContributionStatus.UNRESOLVED_BLOCKING:
            if self.expression != NONZERO_UNKNOWN or not self.blocking:
                raise ValueError("C35_UNRESOLVED_CONTRIBUTION_MUST_BLOCK_AND_REMAIN_UNKNOWN")
        else:
            if self.blocking:
                raise ValueError("C35_RESOLVED_CONTRIBUTION_CANNOT_BLOCK")
            if self.status is ContributionStatus.NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF and not self.gauge_action_proof:
                raise ValueError("C35_NONAPPLICABILITY_REQUIRES_SELECTED_GAUGE_ACTION_PROOF")
        if not self.exact_missing_calculation:
            raise ValueError("C35_CONTRIBUTION_MISSING_CALCULATION_SPECIFICATION")


def fail_closed_contribution_ledger() -> Tuple[SoftContributionResult, ...]:
    return tuple(
        SoftContributionResult(
            "C35.SOFT.%02d.%s" % (index, name),
            name,
            ContributionStatus.UNRESOLVED_BLOCKING,
            NONZERO_UNKNOWN,
            True,
            "SELECT_GAUGE_COMPLETE_REGULATOR_IDENTICAL_REALIZATION_THEN_CALCULATE_" + name,
        )
        for index, name in enumerate(REQUIRED_ONE_LOOP_CONTRIBUTIONS, 1)
    )


@dataclass(frozen=True)
class SoftBareOneLoopResult(_ContentAddressed):
    result_id: str
    tree_value: float
    one_loop_value: Optional[float]
    one_loop_status: str
    convention: str
    all_required_slots_resolved: bool
    continuum_substituted: bool

    def __post_init__(self) -> None:
        if self.tree_value != 1.0:
            raise ValueError("C35_TREE_VALUE_CHANGED")
        if self.continuum_substituted:
            raise ValueError("C35_CONTINUUM_COEFFICIENT_SUBSTITUTION_FORBIDDEN")
        if self.all_required_slots_resolved:
            if self.one_loop_value is None or self.one_loop_status == NONZERO_UNKNOWN:
                raise ValueError("C35_RESOLVED_LEDGER_REQUIRES_FINITE_BASIS_COEFFICIENT")
        elif self.one_loop_value is not None or self.one_loop_status != NONZERO_UNKNOWN:
            raise ValueError("C35_FINITE_BASIS_COEFFICIENT_FABRICATED")


@dataclass(frozen=True)
class SoftCountertermSystem(_ContentAddressed):
    system_id: str
    bare_coefficient_available: bool
    uv_counterterm: Optional[float]
    rapidity_counterterm: Optional[float]
    residual_line_mass_counterterm: Optional[float]
    status: str

    def __post_init__(self) -> None:
        values = (
            self.uv_counterterm,
            self.rapidity_counterterm,
            self.residual_line_mass_counterterm,
        )
        if not self.status:
            raise ValueError("C35_COUNTERTERM_STATUS_REQUIRED")
        if not self.bare_coefficient_available and any(value is not None for value in values):
            raise ValueError("C35_COUNTERTERM_SOLVED_BEFORE_BARE_COEFFICIENT")
        if self.bare_coefficient_available and any(value is None for value in values):
            raise ValueError("C35_AVAILABLE_BARE_COEFFICIENT_REQUIRES_COMPLETE_COUNTERTERM_SYSTEM")


@dataclass(frozen=True)
class C35ClosureReport(_ContentAddressed):
    closure_id: str
    gauge_plan_decided: bool
    gauge_complete_regulator_validated: bool
    light_front_normalization_validated: bool
    real_chart_validated: bool
    virtual_chart_geometry_validated: bool
    executable_mode_basis_validated: bool
    finite_basis_one_loop_validated: bool
    uv_renormalization_validated: bool
    rapidity_renormalization_validated: bool
    soft_side_zero_bin_ready: bool
    primary_no_go: str
    secondary_no_go: str
    outcome_branch: str
    exact_next_package: str

    def __post_init__(self) -> None:
        if not self.gauge_plan_decided or not self.light_front_normalization_validated:
            raise ValueError("C35_DECISION_OR_EXACT_CONVENTION_MISSING")
        if self.executable_mode_basis_validated and not self.gauge_complete_regulator_validated:
            raise ValueError("C35_MODE_BASIS_VALIDATED_WITHOUT_GAUGE_COMPLETE_REGULATOR")
        if self.finite_basis_one_loop_validated and not self.executable_mode_basis_validated:
            raise ValueError("C35_ONE_LOOP_VALIDATED_WITHOUT_MODE_BASIS")
        if self.uv_renormalization_validated or self.rapidity_renormalization_validated:
            if not self.finite_basis_one_loop_validated:
                raise ValueError("C35_RENORMALIZATION_VALIDATED_BEFORE_BARE_ONE_LOOP")
        if not self.finite_basis_one_loop_validated and not self.primary_no_go:
            raise ValueError("C35_INCOMPLETE_CLOSURE_REQUIRES_EXACT_NO_GO")
        if not self.exact_next_package:
            raise ValueError("C35_CLOSURE_REQUIRES_EXACT_NEXT_PACKAGE")


def default_closure_report() -> C35ClosureReport:
    return C35ClosureReport(
        "C35.CLOSURE.v1",
        True,
        False,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        C35_PRIMARY_NO_GO,
        C35_SECONDARY_MODE_NO_GO,
        C35_OUTCOME_BRANCH,
        C35_NEXT_PACKAGE,
    )


def architecture_records() -> Tuple[ArchitectureObjectRecord, ...]:
    exact_oracles = {
        "LightFrontConvention",
        "NullVectorNormalization",
        "RapidityRegulatorRescaling",
        "SoftCoordinateChart",
        "RealSoftCoordinateChart",
        "VirtualSoftCoordinateChart",
        "SoftJacobian",
        "SoftCell",
        "SoftCellBoundary",
        "SoftCellShape",
        "SoftCellMeasure",
        "PoleCellPartition",
        "SingularCellSubtraction",
        "C35CapabilityMatrix",
        "C35ClosureReport",
    }
    plan_records = {"GaugeCompleteSoftPlan", "CovariantKreinPlan", "LightFrontPhysicalPlan", "GaugePlanSupersession"}
    rows = []
    for index, object_type in enumerate(ARCHITECTURE_TYPES, 1):
        if object_type in exact_oracles:
            status = "EXACT_OR_GEOMETRIC_ORACLE_IMPLEMENTED"
            scope = "CONVENTION_OR_METHOD_ONLY_NOT_FINITE_BASIS_SOFT_RESULT"
            blockers = ("NO_SELECTED_GAUGE_COMPLETE_REGULATOR_IDENTICAL_REALIZATION",)
        elif object_type in plan_records:
            status = "PLAN_COMPILED_FAIL_CLOSED"
            scope = "MUTUALLY_EXCLUSIVE_PLAN_AND_NO_GO_DECISION"
            blockers = ("S0C_UNAVAILABLE_SELECTED",)
        else:
            status = "UNAVAILABLE_EMPTY_NOT_ZERO"
            scope = "TYPED_INTERFACE_ONLY"
            blockers = ("GAUGE_COMPLETE_REGULATOR_REQUIRED_FIRST",)
        rows.append(
            ArchitectureObjectRecord(
                "C35.ARCH.%03d.%s" % (index, object_type.upper()),
                object_type,
                status,
                scope,
                blockers,
            )
        )
    return tuple(rows)


INJECTION_GROUPS = (
    "BASELINE_PROVENANCE",
    "GAUGE_REALIZATION",
    "LIGHT_FRONT_CONVENTION",
    "MODE_BASIS",
    "REAL_VIRTUAL_MEASURES",
    "WILSON_SEGMENTS",
    "ONE_LOOP_DIAGRAMS",
    "COUNTERTERMS_TRAJECTORY",
    "SOFT_COLLINEAR_INTERFACE",
    "SCOPE_LEAKAGE",
)


INJECTION_FAULTS: Dict[str, Tuple[str, ...]] = {
    "BASELINE_PROVENANCE": (
        "WRONG_C34_BASELINE",
        "C34_REPORT_ABSENT",
        "VOLUME_XXI_HASH_CHANGED",
        "C33_C34_HISTORICAL_RECORD_OVERWRITTEN",
        "B0_STATE_INSERTED_IN_PROTON_NORMALIZATION",
    ),
    "GAUGE_REALIZATION": (
        "PHYSICAL_MODES_USED_FOR_COVARIANT_XI_SCAN",
        "INDEFINITE_METRIC_OMITTED",
        "CONSTRAINT_MODE_OMITTED",
        "GHOST_OMITTED_WITHOUT_PROOF",
        "INSTANTANEOUS_KERNEL_OMITTED",
        "RESIDUAL_GAUGE_PRESCRIPTION_OMITTED",
        "GAUGE_PLAN_CHANGED_AFTER_RESIDUAL_INSPECTION",
    ),
    "LIGHT_FRONT_CONVENTION": (
        "NULL_DOT_NOT_ONE",
        "KPLUS_KMINUS_SWAPPED",
        "SQRT2_MISSING",
        "DELTA_NOT_RESCALED_WITH_NULL_VECTORS",
        "EIKONAL_NUMERATOR_NORMALIZATION_INCONSISTENT",
    ),
    "MODE_BASIS": (
        "DESCRIPTOR_HASH_TREATED_AS_MODE_COLLECTION",
        "CELL_BOUNDARIES_OMITTED",
        "QUADRATURE_WEIGHTS_OMITTED",
        "SHAPE_FUNCTIONS_UNNORMALIZED",
        "COMMUTATOR_WRONG",
        "POLARIZATION_METRIC_WRONG",
        "RAPIDITY_REGIONS_OVERLAP_WITHOUT_PARTITION",
        "REFINEMENT_MAP_INVENTED",
        "ONE_RESOLUTION_CALLED_COMPLETE",
    ),
    "REAL_VIRTUAL_MEASURES": (
        "REAL_MODE_TAKEN_OFF_SHELL",
        "VIRTUAL_MODE_FORCED_ON_SHELL",
        "PHASE_SPACE_JACOBIAN_WRONG",
        "VIRTUAL_CONTOUR_OMITTED",
        "POLE_CROSSING_HIDDEN",
        "SINGULAR_CELL_CENTER_SAMPLED",
        "NUMERICAL_EPSILON_STORED_AS_SUPPORT",
    ),
    "WILSON_SEGMENTS": (
        "LINE_LENGTH_UNDEFINED",
        "TRANSVERSE_CLOSURE_OMITTED",
        "ENDPOINT_OMITTED",
        "MODIFIED_DELTA_APPLIED_AFTER_INTEGRATION",
        "PATH_ORDER_WRONG",
        "CONJUGATION_WRONG",
        "BASEPOINT_WRONG",
    ),
    "ONE_LOOP_DIAGRAMS": (
        *("%s_SILENTLY_ZEROED" % name for name in REQUIRED_ONE_LOOP_CONTRIBUTIONS),
        "TARGET_DR_RESULT_COPIED_TO_FINITE_REGULATOR",
        "REAL_TERM_OMITTED",
        "VIRTUAL_TERM_OMITTED",
        "LINE_SELF_ENERGY_OMITTED",
        "CUSP_BOUNDARY_MERGED_WITHOUT_IDENTITY",
        "VACUUM_TERM_OMITTED",
        "ZERO_MODE_OMITTED",
        "COUNTERTERM_SOLVED_BEFORE_BARE_COEFFICIENT",
    ),
    "COUNTERTERMS_TRAJECTORY": (
        "POWER_DIVERGENCE_HIDDEN_IN_LOG",
        "FINITE_CONSTANT_TUNED_TO_CONTINUUM",
        "UNDERDETERMINED_THREE_POINT_FIT",
        "HOLDOUT_USED_IN_FIT",
        "MULTIPLE_AXES_INTERPRETED_AS_ONE_COEFFICIENT",
        "FIRST_OMITTED_ORDER_SET_TO_ZERO",
    ),
    "SOFT_COLLINEAR_INTERFACE": (
        "OFFSHELL_ZERO_BIN_EQUALITY_ASSUMED",
        "ZERO_BIN_EQUALITY_CLAIMED_FROM_CITATION_ONLY",
        "DIFFERENT_MEASUREMENT_ACCEPTED",
        "DIFFERENT_B_CONVENTION_ACCEPTED",
        "SOFT_SECTOR_CALLED_COMPLETE_TMD",
        "C32_COLLINEAR_COEFFICIENT_FABRICATED",
    ),
    "SCOPE_LEAKAGE": (
        "ART25_MEMBER_USED",
        "ART25_DATA_USED",
        "PROTON_TMD_EXPORTED",
        "BRIDGE_RERUN",
        "LIKELIHOOD_PRODUCED",
        "PVALUE_PRODUCED",
        "CALIBRATION_PERFORMED",
        "REWEIGHTING_PERFORMED",
        "PROCESS_STATUS_PROMOTED",
        "DEUTERON_STATUS_PROMOTED",
        "GLUON_STATUS_PROMOTED",
        "TODD_STATUS_PROMOTED",
        "PRODUCTION_MUTATED",
        "RAW_MSHT_COMMITTED",
        "NONDETERMINISTIC_MANIFEST",
    ),
}


INJECTION_DIAGNOSTICS = {
    group: "C35_INJECTION_DETECTED_" + group for group in INJECTION_GROUPS
}


INJECTION_CONTROL_BASELINE: Dict[str, Dict[str, Any]] = {
    group: {fault: False for fault in INJECTION_FAULTS[group]} for group in INJECTION_GROUPS
}


FAULT_CATALOG = tuple((group, fault) for group in INJECTION_GROUPS for fault in INJECTION_FAULTS[group])


# Every injected failure is tied to a concrete scientific object.  The 98
# targets deliberately span every formal architecture type, contribution
# slot, and frozen holdout.  Cycling the 93 coprime fault modes against these
# 98 targets makes the first 2,511 pairs unique; rows therefore do not differ
# only by an ordinal counter.
SEMANTIC_INJECTION_TARGETS = tuple(
    ("ARCHITECTURE_OBJECT", "C35.ARCH.TYPE." + object_type, object_type)
    for object_type in ARCHITECTURE_TYPES
) + tuple(
    ("CONTRIBUTION_SLOT", "C35.SOFT.CONTRIBUTION." + name, name)
    for name in REQUIRED_ONE_LOOP_CONTRIBUTIONS
) + tuple(
    ("HOLDOUT", holdout_id, "holdout_status") for holdout_id in HOLDOUT_IDS
)

SEMANTIC_INJECTION_TARGET_INDEX = {
    target_id: (target_kind, mutation_field)
    for target_kind, target_id, mutation_field in SEMANTIC_INJECTION_TARGETS
}


def _injection_payload(
    index: int,
    group: str,
    fault: str,
    semantic_target: Tuple[str, str, str],
) -> Dict[str, Any]:
    target_kind, target_id, target_field = semantic_target
    return {
        "payload_version": "C35.INJECTION.MUTATION.v1",
        "instance_index": index,
        "operation": "REPLACE",
        "path": [
            "domains",
            group,
            fault,
            "targets",
            target_kind,
            target_id,
            target_field,
        ],
        "semantic_target_kind": target_kind,
        "semantic_target_id": target_id,
        "mutation_field": target_field,
        "expected_before": False,
        "replacement": True,
        "fault": fault,
    }


def execute_injection_payload(payload: Mapping[str, Any], expected_payload_sha256: Optional[str] = None) -> str:
    if expected_payload_sha256 is not None and content_hash(payload) != expected_payload_sha256:
        raise ValueError("C35_INJECTION_PAYLOAD_HASH_MISMATCH")
    if payload.get("payload_version") != "C35.INJECTION.MUTATION.v1" or payload.get("operation") != "REPLACE":
        raise ValueError("C35_INJECTION_PAYLOAD_CONTRACT_MISMATCH")
    path = payload.get("path")
    if not isinstance(path, list) or len(path) != 7 or path[0] != "domains" or path[3] != "targets":
        raise ValueError("C35_INJECTION_PATH_INVALID")
    _, group, fault, _, target_kind, target_id, target_field = path
    if group not in INJECTION_CONTROL_BASELINE or fault not in INJECTION_CONTROL_BASELINE[group]:
        raise ValueError("C35_INJECTION_TARGET_UNKNOWN")
    if SEMANTIC_INJECTION_TARGET_INDEX.get(target_id) != (target_kind, target_field):
        raise ValueError("C35_INJECTION_SEMANTIC_TARGET_UNKNOWN")
    if (
        payload.get("semantic_target_kind") != target_kind
        or payload.get("semantic_target_id") != target_id
        or payload.get("mutation_field") != target_field
    ):
        raise ValueError("C35_INJECTION_SEMANTIC_TARGET_MISMATCH")
    state = {name: dict(values) for name, values in INJECTION_CONTROL_BASELINE.items()}
    target_state = {target_id: {target_field: False}}
    if payload.get("expected_before") is not False or payload.get("replacement") is not True:
        raise ValueError("C35_INJECTION_NOT_SINGLE_SAFE_TO_UNSAFE_MUTATION")
    state[group][fault] = True
    target_state[target_id][target_field] = True
    violations = [(name, key) for name, values in state.items() for key, value in values.items() if value]
    if violations != [(group, fault)]:
        raise ValueError("C35_INJECTION_MUST_CREATE_EXACTLY_ONE_SEMANTIC_VIOLATION")
    target_violations = [
        (identity, field)
        for identity, values in target_state.items()
        for field, value in values.items()
        if value
    ]
    if target_violations != [(target_id, target_field)]:
        raise ValueError("C35_INJECTION_MUST_MUTATE_EXACTLY_ONE_CONCRETE_TARGET")
    return INJECTION_DIAGNOSTICS[group]


def injection_rows(count: int = 2511) -> Tuple[Dict[str, Any], ...]:
    if count < 2440:
        raise ValueError("C35_MINIMUM_2440_ORDERED_INJECTIONS_REQUIRED")
    rows = []
    for offset in range(count):
        group, fault = FAULT_CATALOG[offset % len(FAULT_CATALOG)]
        semantic_target = SEMANTIC_INJECTION_TARGETS[offset % len(SEMANTIC_INJECTION_TARGETS)]
        payload = _injection_payload(offset + 1, group, fault, semantic_target)
        payload_sha = content_hash(payload)
        observed = execute_injection_payload(payload, payload_sha)
        rows.append(
            {
                "injection_id": "C35.INJECT.%s.%04d" % (group, offset + 1),
                "ordered_index": offset + 1,
                "group": group,
                "fault": fault,
                "semantic_target_kind": semantic_target[0],
                "semantic_target_id": semantic_target[1],
                "mutation_field": semantic_target[2],
                "mutation_payload": payload,
                "mutation_payload_sha256": payload_sha,
                "mutation_executed": True,
                "expected_diagnostic": INJECTION_DIAGNOSTICS[group],
                "observed_diagnostic": observed,
                "detected": observed == INJECTION_DIAGNOSTICS[group],
            }
        )
    semantic_pairs = {
        (row["group"], row["fault"], row["semantic_target_id"], row["mutation_field"])
        for row in rows
    }
    if len(semantic_pairs) != len(rows):
        raise ValueError("C35_INJECTION_ROWS_NOT_SEMANTICALLY_UNIQUE")
    return tuple(rows)


if len(ARCHITECTURE_TYPES) != 53:
    raise RuntimeError("C35_ARCHITECTURE_TYPE_COUNT_MISMATCH")
if len(REQUIRED_ONE_LOOP_CONTRIBUTIONS) != 18:
    raise RuntimeError("C35_CONTRIBUTION_COUNT_MISMATCH")
if len(HOLDOUT_IDS) != 27:
    raise RuntimeError("C35_HOLDOUT_COUNT_MISMATCH")
if len(BENCHMARK_FAMILIES) != 18:
    raise RuntimeError("C35_BENCHMARK_COUNT_MISMATCH")
if len(FAULT_CATALOG) != 93:
    raise RuntimeError("C35_FAULT_CATALOG_COUNT_MISMATCH")
if len(SEMANTIC_INJECTION_TARGETS) != 98:
    raise RuntimeError("C35_SEMANTIC_INJECTION_TARGET_COUNT_MISMATCH")
