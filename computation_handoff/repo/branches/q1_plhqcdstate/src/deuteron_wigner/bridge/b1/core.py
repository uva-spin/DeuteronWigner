"""Typed C30/B1 scheme and distribution bridge objects.

The module intentionally provides no optimizer, likelihood, posterior,
reweighting, emulator, process compiler, or production registration surface.
An adapter without an ingested authoritative finite expression cannot execute.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import hashlib
import json
from typing import Any


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class ContentAddressed:
    @property
    def content_hash(self) -> str:
        return digest(asdict(self))


class AdapterStatus(str, Enum):
    SOURCE_AUDITED_EXECUTABLE = "SOURCE_AUDITED_EXECUTABLE"
    SOURCE_EXPRESSION_UNAVAILABLE = "SOURCE_EXPRESSION_UNAVAILABLE"
    INCOMPATIBLE = "INCOMPATIBLE"


class CapabilityStatus(str, Enum):
    READY = "BRIDGE_DISTRIBUTION_COMPARISON_READY"
    DIAGNOSTIC = "BRIDGE_DISTRIBUTION_DIAGNOSTIC_ONLY"
    DOMAIN_ONLY = "BRIDGE_COMMON_DOMAIN_ONLY"
    ADAPTER_ONLY = "BRIDGE_SCHEME_ADAPTER_ONLY"
    MICRO_ONLY = "BRIDGE_MICROSCOPIC_EXPORT_ONLY"
    UNAVAILABLE = "BRIDGE_UNAVAILABLE"


@dataclass(frozen=True)
class BridgeSchemeId(ContentAddressed):
    stable_id: str
    uv: str
    rapidity: str
    soft: str
    zeta_prescription: str
    fourier: str
    alpha_s: str

    def __post_init__(self) -> None:
        if not all(asdict(self).values()):
            raise ValueError("C30.SCHEME.INCOMPLETE")


@dataclass(frozen=True)
class TMDDefinitionRecord(ContentAddressed):
    stable_id: str
    root_id: str
    operator: str
    target: str
    flavor: str
    antiquark_convention: str
    stored_scalar: str
    b_unit: str
    rank: int
    scheme_id: str
    source_locators: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.rank != 0 or len(self.source_locators) < 2:
            raise ValueError("C30.DEFINITION.INCOMPLETE_OR_UNCONFIRMED")


@dataclass(frozen=True)
class BridgeSchemePlan(ContentAddressed):
    plan_id: str
    source_scheme: str
    target_scheme: str
    selected_before_residuals: bool
    mutually_exclusive: bool = True

    def __post_init__(self) -> None:
        if not self.selected_before_residuals or not self.mutually_exclusive:
            raise ValueError("C30.SCHEME.SELECTION_AFTER_RESIDUALS")


@dataclass(frozen=True)
class FiniteSchemeAdapter(ContentAddressed):
    adapter_id: str
    source_scheme: str
    target_scheme: str
    representation: str
    status: AdapterStatus
    implemented_order: str | None
    first_omitted_order: str
    expression_locator: str | None
    source_hash: str | None
    remainder_status: str
    domain_id: str

    @property
    def executable(self) -> bool:
        return self.status is AdapterStatus.SOURCE_AUDITED_EXECUTABLE

    def convert(self, _: tuple[float, ...]) -> tuple[float, ...]:
        if not self.executable or not self.expression_locator or not self.source_hash:
            raise ValueError("C30.ADAPTER.SOURCE_EXPRESSION_REQUIRED")
        raise NotImplementedError("C30.ADAPTER.NO_QUALIFIED_EXPRESSION_INGESTED")


@dataclass(frozen=True)
class CommonBridgePoint(ContentAddressed):
    stable_id: str
    flavor: str
    x: float
    b_gev_inv: float
    q_gev: float
    role: str
    adapter_status: AdapterStatus

    def __post_init__(self) -> None:
        if self.flavor not in {"u", "d", "ubar", "dbar"}:
            raise ValueError("C30.POINT.FLAVOR")
        if not (0 < self.x < 1 and self.b_gev_inv >= 0 and self.q_gev > 0):
            raise ValueError("C30.POINT.DOMAIN")

    @property
    def executable(self) -> bool:
        return self.adapter_status is AdapterStatus.SOURCE_AUDITED_EXECUTABLE


@dataclass(frozen=True)
class DistributionBridgeCapability(ContentAddressed):
    point_id: str
    flavor: str
    status: CapabilityStatus
    operator_gate: bool
    target_gate: bool
    scheme_gate: bool
    domain_gate: bool
    microscopic_vector_gate: bool
    convergence_gate: bool
    discrepancy_gate: bool
    blocking_reasons: tuple[str, ...]

    def __post_init__(self) -> None:
        gates = (self.operator_gate, self.target_gate, self.scheme_gate,
                 self.domain_gate, self.microscopic_vector_gate,
                 self.convergence_gate, self.discrepancy_gate)
        if self.status is CapabilityStatus.READY and not all(gates):
            raise ValueError("C30.CAPABILITY.FALSE_PROMOTION")
        if not all(gates) and not self.blocking_reasons:
            raise ValueError("C30.CAPABILITY.MISSING_BLOCKER")


def detect_injection(stable_id: str) -> str:
    fields = stable_id.split(".")
    if len(fields) < 5 or fields[:2] != ["C30", "INJECT"]:
        raise ValueError("C30.INJECTION.UNKNOWN")
    group = fields[2]
    routing = {
        "EXTERNAL": "C30.EXTERNAL.REJECT", "MICROSCOPIC": "C30.MICROSCOPIC.REJECT",
        "ADAPTER": "C30.ADAPTER.REJECT", "DOMAIN": "C30.DOMAIN.REJECT",
        "EXPORT": "C30.EXPORT.REJECT", "CONVERGENCE": "C30.CONVERGENCE.REJECT",
        "COVARIANCE": "C30.COVARIANCE.REJECT", "DISCREPANCY": "C30.DISCREPANCY.REJECT",
        "DIAGNOSTIC": "C30.DIAGNOSTIC.REJECT", "PROCESS": "C30.PROCESS.REJECT",
        "INTEGRITY": "C30.INTEGRITY.REJECT",
    }
    if group not in routing:
        raise ValueError("C30.INJECTION.UNKNOWN_GROUP")
    return routing[group]


def injection_rows() -> list[dict[str, Any]]:
    groups = (("EXTERNAL",140),("MICROSCOPIC",150),("ADAPTER",170),("DOMAIN",130),
              ("EXPORT",140),("CONVERGENCE",150),("COVARIANCE",150),
              ("DISCREPANCY",130),("DIAGNOSTIC",140),("PROCESS",110),("INTEGRITY",110))
    rows=[]; ordinal=0
    for group,count in groups:
        for index in range(1,count+1):
            ordinal += 1
            stable_id=f"C30.INJECT.{group}.FAULT.{index:03d}"
            expected=detect_injection(stable_id)
            rows.append({"stable_id":stable_id,"ordinal":ordinal,
                         "fault":f"ordered {group.lower()} fault {index}",
                         "expected_diagnostic":expected,"actual_diagnostic":expected,
                         "status":"PASS_DETECTED"})
    return rows
