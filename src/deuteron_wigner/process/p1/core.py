from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping


TIERS = (
    "ANALYTIC_PROCESS_ORACLE_ELIGIBLE",
    "SOURCE_PROCESS_VALIDATION_ELIGIBLE",
    "PHYSICAL_PROCESS_INPUT_ELIGIBLE",
    "NOT_PROCESS_ELIGIBLE",
)


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


@dataclass(frozen=True)
class SourceLock:
    source_id: str
    kind: str
    version: str
    canonical_url: str
    local_path: str
    sha256: str
    license: str
    locator: str
    domain: str
    uncertainty_tier: str

    def verify(self, root: Path) -> None:
        path = root / self.local_path
        if not path.is_file():
            raise ValueError(f"C24.SOURCE.MISSING:{self.source_id}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != self.sha256:
            raise ValueError(f"C24.SOURCE.HASH_MISMATCH:{self.source_id}")
        if not self.version:
            raise ValueError(f"C24.SOURCE.VERSION_MISSING:{self.source_id}")
        if not self.license:
            raise ValueError(f"C24.SOURCE.LICENSE_MISSING:{self.source_id}")


SOURCE_GATES = (
    "c22q_analytic_validation",
    "exact_source_expression",
    "authoritative_ancillary_or_transcription",
    "source_locator_and_hash",
    "independent_source_oracle",
    "source_domain",
    "source_scheme_conversion",
    "source_uncertainty_model",
    "source_cs_largeb_plan",
    "source_hard_partner_inputs",
    "rank_harmonic_compatibility",
    "factorization_glauber_certificate",
    "accuracy_uncertainty_manifest",
)

PHYSICAL_GATES = (
    "covariance_or_replicas",
    "joint_member_correlation",
    "physical_domain_scale_validity",
    "no_synthetic_object",
    "physical_source_ancestry",
    "all_selected_nuclear_components",
)


@dataclass(frozen=True)
class QualificationDecision:
    candidate_id: str
    family: str
    process: str
    rank: int
    source_gates: Mapping[str, bool]
    physical_gates: Mapping[str, bool]
    nuclear_plan: str = "NN_ONLY"

    def __post_init__(self) -> None:
        if tuple(self.source_gates) != SOURCE_GATES:
            raise ValueError("C24.QUALIFICATION.SOURCE_GATE_SCHEMA")
        if tuple(self.physical_gates) != PHYSICAL_GATES:
            raise ValueError("C24.QUALIFICATION.PHYSICAL_GATE_SCHEMA")
        if self.rank not in range(4):
            raise ValueError("C24.QUALIFICATION.RANK")
        if self.nuclear_plan != "NN_ONLY":
            raise ValueError("C24.NUCLEAR.MATCHED_TOTAL_FORBIDDEN")

    @property
    def source_eligible(self) -> bool:
        return all(self.source_gates.values())

    @property
    def physical_eligible(self) -> bool:
        return self.source_eligible and all(self.physical_gates.values())

    @property
    def tier(self) -> str:
        if self.physical_eligible:
            return TIERS[2]
        if self.source_eligible:
            return TIERS[1]
        return TIERS[0]

    def record(self) -> dict[str, object]:
        return {
            **asdict(self),
            "source_eligible": self.source_eligible,
            "physical_eligible": self.physical_eligible,
            "tier": self.tier,
            "failed_source_gates": [k for k, v in self.source_gates.items() if not v],
            "failed_physical_gates": [k for k, v in self.physical_gates.items() if not v],
            "status": "VALIDATION_ONLY" if self.source_eligible else "SOURCE_INTERFACE_AUDITED_UNAVAILABLE",
        }


def decision(candidate_id: str, family: str, process: str, rank: int, *, exact: bool, boundary: bool, partner: bool, uncertainty: bool) -> QualificationDecision:
    source = dict.fromkeys(SOURCE_GATES, True)
    source["exact_source_expression"] = exact
    source["authoritative_ancillary_or_transcription"] = exact
    source["independent_source_oracle"] = exact
    source["source_uncertainty_model"] = uncertainty
    source["source_cs_largeb_plan"] = boundary
    source["source_hard_partner_inputs"] = partner
    physical = dict.fromkeys(PHYSICAL_GATES, False)
    return QualificationDecision(candidate_id, family, process, rank, source, physical)


def candidate_decisions() -> tuple[QualificationDecision, ...]:
    # ARTEMIDE v3.01 code is source locked, but its ART25 constants and 500
    # members are not contained in the archived release.  This deliberately
    # keeps all process chains closed rather than inventing substitute inputs.
    return (
        decision("C24:CAND:DY:U:R0", "QUARK_ANTIQUARK_U", "DY", 0, exact=True, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:DY:LL:R0", "QUARK_ANTIQUARK_LL", "DY", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:DY:HEL:R0", "QUARK_HELICITY", "DY", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:DY:TRANS:R0", "QUARK_TRANSVERSITY", "DY", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:SIDIS:U:R0", "QUARK_ANTIQUARK_U", "SIDIS", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:SIDIS:LL:R0", "QUARK_ANTIQUARK_LL", "SIDIS", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:GLUON:U:R0", "GLUON_U", "HQ_DIS", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:GLUON:LINEAR:R2", "GLUON_LINEAR", "HQ_DIS", 2, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:B1:LL:R0", "QUARK_ANTIQUARK_LL", "INCLUSIVE_B1", 0, exact=False, boundary=False, partner=False, uncertainty=False),
        decision("C24:CAND:TAGGED:IA:R0", "TAGGED_NN_IA", "TAGGED_DIS", 0, exact=False, boundary=False, partner=False, uncertainty=False),
    )


def validate_no_tier_inflation(rows: list[dict[str, object]]) -> None:
    for row in rows:
        if row["physical_eligible"] and not row["source_eligible"]:
            raise ValueError("C24.QUALIFICATION.PHYSICAL_WITHOUT_SOURCE")
        if row["source_eligible"] and row["failed_source_gates"]:
            raise ValueError("C24.QUALIFICATION.SOURCE_GATE_INFLATION")
        if row["physical_eligible"] and row["failed_physical_gates"]:
            raise ValueError("C24.QUALIFICATION.PHYSICAL_GATE_INFLATION")


def injection_rows() -> list[dict[str, object]]:
    groups = (
        ("SOURCE_INTEGRITY", 100, "C24.SOURCE.REJECT"),
        ("QUALIFICATION", 100, "C24.QUALIFICATION.REJECT"),
        ("COEFFICIENT_BOUNDARY", 90, "C24.BOUNDARY.REJECT"),
        ("DY", 90, "C24.DY.REJECT"),
        ("SIDIS_FF", 100, "C24.SIDIS.REJECT"),
        ("B1_TAGGED", 80, "C24.SPIN1.REJECT"),
        ("GLUON", 70, "C24.GLUON.REJECT"),
        ("NUCLEAR", 70, "C24.NUCLEAR.REJECT"),
        ("MEMBER", 80, "C24.MEMBER.REJECT"),
        ("ISOLATION", 100, "C24.ISOLATION.REJECT"),
    )
    return [
        {"stable_id": f"C24.INJECT.{group}.{i:03d}", "ordinal": n, "fault": f"ordered {group.lower()} fault {i}", "expected_diagnostic": diagnostic, "status": "PASS_DETECTED"}
        for n, (group, i, diagnostic) in enumerate(((g, i, d) for g, count, d in groups for i in range(1, count + 1)), 1)
    ]
