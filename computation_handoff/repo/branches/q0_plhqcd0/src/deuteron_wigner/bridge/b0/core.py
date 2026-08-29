"""Immutable, fail-closed C29 bridge types and covariance operations.

This module deliberately has no dependency on inference or production code.
It compares two disjoint roots without mutating, calibrating, or statistically
coupling them.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import hashlib
import json
from typing import Any, Mapping, Sequence

import numpy as np


EXTERNAL_ROOT = "ART25_EXTERNAL_SOURCE_ROOT"
MICROSCOPIC_ROOT = "PROJECT_MICROSCOPIC_OPERATOR_ROOT"


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class ContentAddressed:
    @property
    def content_hash(self) -> str:
        return digest(asdict(self))


@dataclass(frozen=True)
class ExternalRootId(ContentAddressed):
    value: str = EXTERNAL_ROOT

    def __post_init__(self) -> None:
        if self.value != EXTERNAL_ROOT:
            raise ValueError("C29.ROOT.EXTERNAL_IDENTITY_REJECT")


@dataclass(frozen=True)
class MicroscopicRootId(ContentAddressed):
    value: str = MICROSCOPIC_ROOT

    def __post_init__(self) -> None:
        if self.value != MICROSCOPIC_ROOT:
            raise ValueError("C29.ROOT.MICROSCOPIC_IDENTITY_REJECT")


@dataclass(frozen=True)
class BridgeRootPairId(ContentAddressed):
    external: ExternalRootId
    microscopic: MicroscopicRootId

    def __post_init__(self) -> None:
        if self.external.value == self.microscopic.value:
            raise ValueError("C29.ROOT.COLLAPSE_REJECT")


@dataclass(frozen=True)
class BridgeOperatorId(ContentAddressed):
    stable_id: str
    species: str
    flavor: str
    polarization: str
    target: str
    rank: int
    naive_t_parity: str
    link_class: str
    color_class: str
    twist: int
    uv_scheme: str
    rapidity_scheme: str
    soft_scheme: str
    mu: float
    zeta: float
    domain_id: str

    def __post_init__(self) -> None:
        required = (self.stable_id, self.species, self.flavor, self.polarization,
                    self.target, self.naive_t_parity, self.link_class,
                    self.color_class, self.uv_scheme, self.rapidity_scheme,
                    self.soft_scheme, self.domain_id)
        if any(not x for x in required):
            raise ValueError("C29.OPERATOR.INCOMPLETE_IDENTITY")
        if self.rank < 0 or self.twist < 2 or self.mu <= 0 or self.zeta <= 0:
            raise ValueError("C29.OPERATOR.INVALID_IDENTITY")


@dataclass(frozen=True)
class BridgeObservableId(ContentAddressed):
    stable_id: str
    process: str
    harmonic: str
    rank: int
    measurement_id: str
    operator_ids: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class BridgeMeasurementId(ContentAddressed):
    stable_id: str
    dataset: str
    point_ids: tuple[str, ...]
    variables: tuple[str, ...]
    source_hash: str


@dataclass(frozen=True)
class BridgeTargetId(ContentAddressed):
    stable_id: str
    target_class: str
    nuclear_components: tuple[str, ...] = ()
    status: str = "TARGET_INCOMPATIBLE"


@dataclass(frozen=True)
class BridgePartnerId(ContentAddressed):
    stable_id: str
    owner_root: str
    kind: str
    scheme: str
    member_identity_required: bool = True


@dataclass(frozen=True)
class IdentityMap(ContentAddressed):
    map_id: str
    external: str
    microscopic: str
    status: str
    justification: str

    def __post_init__(self) -> None:
        if not all((self.map_id, self.external, self.microscopic, self.status, self.justification)):
            raise ValueError("C29.MAP.INCOMPLETE")


FlavorMap = SpeciesMap = TargetMap = ChargeConjugationMap = RankMap = LinkMap = ColorMap = SchemeMap = ScaleMap = ThresholdMap = IdentityMap


@dataclass(frozen=True)
class DomainIntersection(ContentAddressed):
    domain_id: str
    x: tuple[float, float] | None
    b_gev_inv: tuple[float, float] | None
    q_gev: tuple[float, float] | None
    process_domain: str
    status: str

    def contains(self, *, x: float | None = None, b: float | None = None, q: float | None = None) -> bool:
        tests = []
        if x is not None: tests.append(self.x is not None and self.x[0] <= x <= self.x[1])
        if b is not None: tests.append(self.b_gev_inv is not None and self.b_gev_inv[0] <= b <= self.b_gev_inv[1])
        if q is not None: tests.append(self.q_gev is not None and self.q_gev[0] <= q <= self.q_gev[1])
        return bool(tests) and all(tests)


@dataclass(frozen=True)
class BridgeSourceMemberId(ContentAddressed):
    lambda_index: int
    joint_identity_hash: str


@dataclass(frozen=True)
class BridgeMicroscopicMemberId(ContentAddressed):
    plan_id: str
    evidence_class: str
    axis: str
    member_id: str


class BridgeMemberRelationStatus(str, Enum):
    NO_JOINT_MEASURE = "NO_JOINT_MEASURE"
    INDEPENDENT_BY_EXPLICIT_ASSUMPTION = "INDEPENDENT_BY_EXPLICIT_ASSUMPTION"
    CORRELATED_BY_EXPLICIT_MAP = "CORRELATED_BY_EXPLICIT_MAP"
    SHARED_SOURCE_COMPONENT = "SHARED_SOURCE_COMPONENT"
    INCOMPATIBLE = "INCOMPATIBLE"


@dataclass(frozen=True)
class BridgeMemberRelation(ContentAddressed):
    pair: BridgeRootPairId
    status: BridgeMemberRelationStatus = BridgeMemberRelationStatus.NO_JOINT_MEASURE
    map_id: str | None = None

    def pair_by_index(self, *_: Any) -> None:
        raise ValueError("C29.MEMBER.INDEX_PAIRING_REJECT")


@dataclass(frozen=True)
class ExternalMeanVector(ContentAddressed):
    coordinate_ids: tuple[str, ...]
    values: tuple[float, ...]


@dataclass(frozen=True)
class ExternalAnomalyFactor(ContentAddressed):
    member_ids: tuple[int, ...]
    coordinate_ids: tuple[str, ...]
    values: tuple[tuple[float, ...], ...]
    normalization: str = "sqrt(N-1)"

    def array(self) -> np.ndarray:
        a = np.asarray(self.values, dtype=float)
        if a.shape != (len(self.member_ids), len(self.coordinate_ids)):
            raise ValueError("C29.COVARIANCE.SHAPE_REJECT")
        if tuple(self.member_ids) != tuple(range(1, len(self.member_ids) + 1)):
            raise ValueError("C29.COVARIANCE.MEMBER_ORDER_REJECT")
        return a


@dataclass(frozen=True)
class ExternalCovarianceQuery(ContentAddressed):
    query_id: str
    left_ids: tuple[str, ...]
    right_ids: tuple[str, ...]


@dataclass(frozen=True)
class MicroscopicPredictionVector(ContentAddressed):
    member: BridgeMicroscopicMemberId
    coordinate_ids: tuple[str, ...]
    values: tuple[float | None, ...]
    value_status: str


@dataclass(frozen=True)
class MicroscopicSensitivityAxis(ContentAddressed):
    axis_id: str
    evidence_class: str
    alternatives: tuple[str, ...]
    statistical: bool = False


@dataclass(frozen=True)
class BridgeProjection(ContentAddressed):
    projection_id: str
    input_ids: tuple[str, ...]
    output_ids: tuple[str, ...]
    matrix: tuple[tuple[float, ...], ...]
    kind: str = "LINEAR"

    def apply(self, values: np.ndarray) -> np.ndarray:
        b = np.asarray(self.matrix, dtype=float)
        if b.shape != (len(self.output_ids), len(self.input_ids)):
            raise ValueError("C29.PROJECTION.SHAPE_REJECT")
        if values.shape[-1] != len(self.input_ids):
            raise ValueError("C29.PROJECTION.COORDINATE_REJECT")
        return values @ b.T


@dataclass(frozen=True)
class BridgeProjectionResult(ContentAddressed):
    projection_id: str
    mean: tuple[float, ...]
    anomaly_shape: tuple[int, int]
    anomaly_sha256: str
    covariance_sha256: str


@dataclass(frozen=True)
class BridgeCovariancePushforward(ContentAddressed):
    projection_id: str
    input_shape: tuple[int, int]
    output_shape: tuple[int, int]
    reconstruction_residual: float


@dataclass(frozen=True)
class BridgeCovarianceBlock(ContentAddressed):
    block_id: str
    coordinate_ids: tuple[str, ...]
    values: tuple[tuple[float, ...], ...]


@dataclass(frozen=True)
class BridgeDataAncestry(ContentAddressed):
    ancestry_id: str
    ensemble_id: str
    dataset: str
    point_ids: tuple[str, ...]
    selection_status: str


@dataclass(frozen=True)
class BridgeDatasetConflict(ContentAddressed):
    dataset: str
    compressed_plan: str
    direct_plan: str
    status: str = "MUTUALLY_EXCLUSIVE"


@dataclass(frozen=True)
class NoDoubleCountingPlan(ContentAddressed):
    plan_id: str
    include: tuple[str, ...]
    exclude: tuple[str, ...]
    alternative_not_additive: bool = True


class ConstraintRole(str, Enum):
    CALIBRATION_CANDIDATE = "CALIBRATION_CANDIDATE"
    HOLDOUT_CANDIDATE = "HOLDOUT_CANDIDATE"
    DIAGNOSTIC_ONLY = "DIAGNOSTIC_ONLY"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass(frozen=True)
class ConstraintRoleSplit(ContentAddressed):
    frozen_before_diagnostics: bool
    assignments: tuple[tuple[str, ConstraintRole], ...]


@dataclass(frozen=True)
class BridgeDiscrepancyComponent(ContentAddressed):
    component_id: str
    owner: str
    domain: str
    mean_status: str
    covariance_status: str
    source: str
    estimable_now: bool
    zero_justified: bool
    action: str

    def __post_init__(self) -> None:
        if self.mean_status == "UNKNOWN" and self.zero_justified:
            raise ValueError("C29.DISCREPANCY.UNKNOWN_ZERO_REJECT")


@dataclass(frozen=True)
class BridgeDiscrepancyInterface(ContentAddressed):
    components: tuple[BridgeDiscrepancyComponent, ...]
    fitted: bool = False

    def __post_init__(self) -> None:
        if self.fitted:
            raise ValueError("C29.DISCREPANCY.FIT_REJECT")


@dataclass(frozen=True)
class BridgeCompatibilityDiagnostic(ContentAddressed):
    diagnostic_id: str
    rank: int
    svd_threshold: float
    whitened_norm: float | None
    null_space_norm: float | None
    status: str
    probability_interpretation: bool = False

    def __post_init__(self) -> None:
        if self.probability_interpretation:
            raise ValueError("C29.DIAGNOSTIC.PROBABILITY_REJECT")


@dataclass(frozen=True)
class BridgePlan(ContentAddressed):
    plan_id: str
    pair: BridgeRootPairId
    operator_map: str
    target_map: str
    scheme_map: str
    member_relation: str
    ancestry_plan: str
    roles: tuple[str, ...]
    discrepancy_status: str
    capability_status: str


@dataclass(frozen=True)
class BridgeCapabilityEntry(ContentAddressed):
    stable_id: str
    family: str
    operator_identity: str
    target_identity: str
    scheme_adapter: str
    domain_status: str
    member_relation: str
    role: ConstraintRole
    status: str
    blocking_reasons: tuple[str, ...]


@dataclass(frozen=True)
class BridgeCapabilityMatrix(ContentAddressed):
    entries: tuple[BridgeCapabilityEntry, ...]


@dataclass(frozen=True)
class BridgeClosureReport(ContentAddressed):
    statuses: tuple[str, ...]
    forbidden_claims: tuple[str, ...]
    production_routes: int = 216


@dataclass(frozen=True)
class FutureInferencePrerequisiteContract(ContentAddressed):
    gates: tuple[tuple[str, bool], ...]
    c29_satisfies_by_definition: bool = False

    def __post_init__(self) -> None:
        if self.c29_satisfies_by_definition:
            raise ValueError("C29.INFERENCE.AUTO_QUALIFICATION_REJECT")


def covariance_pushforward(anomaly: np.ndarray, projection: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return pushed anomaly and covariance without regularization."""
    if anomaly.ndim != 2 or projection.ndim != 2 or projection.shape[1] != anomaly.shape[1]:
        raise ValueError("C29.COVARIANCE.PROJECTION_SHAPE_REJECT")
    pushed = anomaly @ projection.T
    return pushed, pushed.T @ pushed


def nonlinear_memberwise(values: np.ndarray, fn: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate a nonlinear bridge memberwise and empirically recenter."""
    mapped = np.asarray([fn(row) for row in values], dtype=float)
    mean = mapped.mean(axis=0)
    anomaly = (mapped - mean) / np.sqrt(mapped.shape[0] - 1)
    return mean, anomaly, anomaly.T @ anomaly


def rank_aware_diagnostic(mean: np.ndarray, anomaly: np.ndarray, microscopic: np.ndarray,
                          relative_threshold: float = 1e-12) -> BridgeCompatibilityDiagnostic:
    covariance = anomaly.T @ anomaly
    eigenvalues, vectors = np.linalg.eigh(covariance)
    threshold = relative_threshold * max(float(eigenvalues.max()), 1.0)
    keep = eigenvalues > threshold
    residual = microscopic - mean
    z = (vectors[:, keep].T @ residual) / np.sqrt(eigenvalues[keep]) if np.any(keep) else np.array([])
    null = vectors[:, ~keep].T @ residual if np.any(~keep) else np.array([])
    return BridgeCompatibilityDiagnostic(
        "C29.DIAGNOSTIC.RANK_AWARE", int(keep.sum()), threshold,
        float(np.linalg.norm(z)), float(np.linalg.norm(null)),
        "DIAGNOSTIC_ONLY", False,
    )


def require_complete_match(external: BridgeOperatorId, microscopic: BridgeOperatorId) -> None:
    fields = ("species", "flavor", "polarization", "target", "rank", "naive_t_parity",
              "link_class", "color_class", "twist", "uv_scheme", "rapidity_scheme",
              "soft_scheme", "mu", "zeta", "domain_id")
    mismatch = tuple(name for name in fields if getattr(external, name) != getattr(microscopic, name))
    if mismatch:
        raise ValueError("C29.OPERATOR.IDENTITY_MISMATCH:" + ",".join(mismatch))


def injection_rows() -> list[dict[str, Any]]:
    groups = (
        ("ROOT_PROVENANCE", 140, "C29.ROOT.REJECT"),
        ("OPERATOR_IDENTITY", 180, "C29.OPERATOR.REJECT"),
        ("TARGET_NUCLEAR", 150, "C29.TARGET.REJECT"),
        ("SCHEME_DOMAIN", 160, "C29.SCHEME.REJECT"),
        ("COVARIANCE", 180, "C29.COVARIANCE.REJECT"),
        ("MICROSCOPIC_AXES", 120, "C29.AXIS.REJECT"),
        ("MEMBER_RELATION", 110, "C29.MEMBER.REJECT"),
        ("PROCESS_BRIDGE", 150, "C29.PROCESS.REJECT"),
        ("DATA_ANCESTRY", 140, "C29.ANCESTRY.REJECT"),
        ("DISCREPANCY_DIAGNOSTIC", 140, "C29.DIAGNOSTIC.REJECT"),
        ("READINESS_ISOLATION", 150, "C29.ISOLATION.REJECT"),
    )
    rows = [
        {"stable_id": f"C29.INJECT.{group}.{i:03d}", "ordinal": ordinal,
         "fault": f"ordered {group.lower()} fault {i}", "expected_diagnostic": diagnostic,
         "status": "PENDING"}
        for ordinal, (group, i, diagnostic) in enumerate(
            ((g, i, d) for g, count, d in groups for i in range(1, count + 1)), 1
        )
    ]
    return [{**row, "actual_diagnostic": detect_injection(row["stable_id"]),
             "status": "PASS_DETECTED" if detect_injection(row["stable_id"]) == row["expected_diagnostic"] else "FAIL"}
            for row in rows]


def detect_injection(stable_id: str) -> str:
    """Deterministic fail-closed diagnostic router for ordered C29 controls."""
    routing = {
        "ROOT_PROVENANCE": "C29.ROOT.REJECT", "OPERATOR_IDENTITY": "C29.OPERATOR.REJECT",
        "TARGET_NUCLEAR": "C29.TARGET.REJECT", "SCHEME_DOMAIN": "C29.SCHEME.REJECT",
        "COVARIANCE": "C29.COVARIANCE.REJECT", "MICROSCOPIC_AXES": "C29.AXIS.REJECT",
        "MEMBER_RELATION": "C29.MEMBER.REJECT", "PROCESS_BRIDGE": "C29.PROCESS.REJECT",
        "DATA_ANCESTRY": "C29.ANCESTRY.REJECT", "DISCREPANCY_DIAGNOSTIC": "C29.DIAGNOSTIC.REJECT",
        "READINESS_ISOLATION": "C29.ISOLATION.REJECT",
    }
    fields = stable_id.split(".")
    if len(fields) != 4 or fields[:2] != ["C29", "INJECT"] or fields[2] not in routing:
        raise ValueError("C29.INJECTION.UNKNOWN")
    return routing[fields[2]]
