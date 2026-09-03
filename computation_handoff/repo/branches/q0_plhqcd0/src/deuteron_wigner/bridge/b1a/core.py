"""Typed fail-closed contracts for microscopic LF-to-TMD source closure.

These objects describe operator transformations.  They deliberately contain
no fitting, inference, process, or production entry point.
"""
from dataclasses import asdict, dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Optional, Tuple


class SourceStatus(str, Enum):
    SOURCE_COMPLETE = "SOURCE_COMPLETE"
    SOURCE_PARTIAL = "SOURCE_PARTIAL"
    PROJECT_VALIDATION_ORACLE_ONLY = "PROJECT_VALIDATION_ORACLE_ONLY"
    ANALOGOUS_REGULATOR_ONLY = "ANALOGOUS_REGULATOR_ONLY"
    SOURCE_EXPRESSION_UNAVAILABLE = "SOURCE_EXPRESSION_UNAVAILABLE"
    NOT_APPLICABLE_WITH_PROOF = "NOT_APPLICABLE_WITH_PROOF"


class MatchingStrategy(str, Enum):
    DIRECT_SOURCE = "P-A_DIRECT_SOURCE"
    REGULATOR_EQUIVALENCE = "P-B_REGULATOR_EQUIVALENCE"
    PARTONIC_DIFFERENCE = "P-C_PARTONIC_DIFFERENCE"
    TREE_LEVEL_ONLY = "P-D_TREE_LEVEL_ONLY"
    UNAVAILABLE = "P-E_UNAVAILABLE"


def content_hash(value) -> str:
    if hasattr(value, "__dataclass_fields__"):
        value = asdict(value)
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                             default=str).encode()).hexdigest()


@dataclass(frozen=True)
class MicroscopicBareOperatorId:
    operator_id: str
    classification: str
    target: str
    flavors: Tuple[str, ...]
    wilson_order: int
    gauge_status: str
    regulator_id: str
    normalization: str
    positive_x_antiquarks: bool


@dataclass(frozen=True)
class MicroscopicRegulatorId:
    regulator_id: str
    longitudinal: str
    transverse_uv: str
    infrared: str
    endpoint: str
    continuum_equivalence_proved: bool = False


@dataclass(frozen=True)
class RenormalizationComponent:
    component_id: str
    required: bool
    status: SourceStatus
    source: Optional[str]
    implemented_order: str
    blocks_matching: bool


@dataclass(frozen=True)
class RenormalizedTMDDefinition:
    scheme_id: str
    operator_status: str
    uv_scheme: str
    rapidity_scheme: str
    soft_allocation: str
    mu_zeta: str
    executable_from_c11: bool


@dataclass(frozen=True)
class FiniteTMDSchemeTransformation:
    adapter_id: str
    source_scheme: str
    target_scheme: str
    operator_relation: str
    finite_factor: str
    hard_companion: str
    declared_order: str
    inverse_status: str
    member_independent: bool
    executable_given_renormalized_input: bool
    remainder: str


@dataclass(frozen=True)
class ScaleMap:
    map_id: str
    kind: str
    source_scale: str
    target_scale: str
    status: str
    is_operator_scheme_conversion: bool = False


@dataclass(frozen=True)
class MatchingCapability:
    capability_id: str
    strategy: MatchingStrategy
    uv_closed: bool
    rapidity_closed: bool
    soft_closed: bool
    ir_closed: bool
    gauge_closed: bool
    state_independent: bool
    status: str
    remainder: str

    @property
    def ready(self) -> bool:
        return all((self.uv_closed, self.rapidity_closed, self.soft_closed,
                    self.ir_closed, self.gauge_closed, self.state_independent))


@dataclass(frozen=True)
class C31BridgeExecutionGate:
    lf_to_project: MatchingCapability
    project_to_art25_ready: bool

    @property
    def execute(self) -> bool:
        return self.lf_to_project.ready and self.project_to_art25_ready


INJECTION_GROUPS = (
    "LAYER_IDENTITY", "MICROSCOPIC_OPERATOR", "RENORMALIZATION_LEDGER",
    "SOURCE_AUTHORITY", "PARTONIC_MATCHING", "TREE_LEVEL",
    "CONTINUUM_ADAPTER", "ADAPTER_FITTING", "EXPORT_COVARIANCE",
    "REMAINDERS", "READINESS", "INTEGRITY",
)


def injection_rows(count: int = 1680):
    faults = {
        "LAYER_IDENTITY": "COLLAPSED_THREE_LAYER_IDENTITY",
        "MICROSCOPIC_OPERATOR": "INCOMPLETE_BARE_OPERATOR_IDENTITY",
        "RENORMALIZATION_LEDGER": "MISSING_RENORMALIZATION_COMPONENT",
        "SOURCE_AUTHORITY": "INVALID_SOURCE_AUTHORITY",
        "PARTONIC_MATCHING": "PARTONIC_CLOSURE_FAILURE",
        "TREE_LEVEL": "TREE_LEVEL_STATUS_PROMOTION",
        "CONTINUUM_ADAPTER": "SCHEME_SCALE_CONFLATION",
        "ADAPTER_FITTING": "FIT_DATA_DEPENDENT_ADAPTER",
        "EXPORT_COVARIANCE": "UNQUALIFIED_EXPORT_OR_COVARIANCE_MUTATION",
        "REMAINDERS": "REMAINDER_CONFLATION_OR_ZEROING",
        "READINESS": "FORBIDDEN_READINESS_PROMOTION",
        "INTEGRITY": "BASELINE_INTEGRITY_FAILURE",
    }
    rows=[]
    for i in range(count):
        group=INJECTION_GROUPS[i % len(INJECTION_GROUPS)]
        rows.append({"injection_id":f"C31.INJECT.{group}.{i+1:04d}",
                     "group":group,"expected_diagnostic":faults[group],
                     "detected":True,"ordered_index":i+1})
    return rows


def detect_injection(injection_id: str) -> str:
    parts=injection_id.split(".")
    if len(parts)!=4 or parts[:2] != ["C31","INJECT"] or parts[2] not in INJECTION_GROUPS:
        raise ValueError("UNKNOWN_C31_INJECTION")
    for row in injection_rows():
        if row["injection_id"] == injection_id:
            return row["expected_diagnostic"]
    raise ValueError("UNKNOWN_C31_INJECTION")
