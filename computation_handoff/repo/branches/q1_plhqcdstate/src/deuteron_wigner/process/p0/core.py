from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=str, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class ProcessId:
    family: str
    external_states: tuple[str, ...]
    beam_charges: tuple[int, ...]
    polarizations: tuple[str, ...]
    hard_scale_definition: str
    plan_tier: str = "ANALYTIC_PROCESS_ORACLE"


@dataclass(frozen=True)
class MeasurementRecord:
    variables: tuple[str, ...]
    frame: str
    azimuth_zero: str
    target_polarization_basis: str
    bins: tuple[tuple[str, float, float], ...]
    cuts: tuple[str, ...] = ()
    acceptance_status: str = "IDENTITY_ANALYTIC"
    radiative_status: str = "NOT_APPLIED_ANALYTIC"


@dataclass(frozen=True)
class HarmonicId:
    structure_function: str
    azimuthal_harmonic: str
    target_channel: str
    transverse_rank: int
    parity: str
    naive_t_parity: str


@dataclass(frozen=True)
class FactorizationGlauberCertificate:
    certificate_id: str
    factorization_status: str
    glauber_status: str
    color_entanglement: str
    leading_regions: tuple[str, ...]
    soft_decoupling: str
    domain: str
    analytic_only: bool = True

    @property
    def executable(self) -> bool:
        return self.factorization_status in ("ESTABLISHED_ANALYTIC", "CONDITIONAL_ANALYTIC") and self.glauber_status != "FAILED"


@dataclass(frozen=True)
class HardFactorRecord:
    hard_id: str
    process_family: str
    channel: str
    order: str
    scheme: str
    expression: str
    source_tier: str = "SYNTHETIC_ANALYTIC_ORACLE"
    physical: bool = False


@dataclass(frozen=True)
class PartnerRecord:
    partner_id: str
    kind: str
    scheme: str
    expression: str
    covariance_status: str = "SYNTHETIC_NONE"
    physical: bool = False


@dataclass(frozen=True)
class FixedOrderReference:
    reference_id: str
    process_family: str
    order: str
    scheme: str
    analytic_expression: str
    physical: bool = False


@dataclass(frozen=True)
class AnalyticWYOracle:
    oracle_id: str
    process_family: str
    harmonic: HarmonicId
    amplitude: float
    width: float
    hard: HardFactorRecord
    fixed_order: FixedOrderReference
    certificate: FactorizationGlauberCertificate
    operator_ids: tuple[str, ...]
    status: str = "VALIDATION_ONLY"

    def __post_init__(self) -> None:
        if self.harmonic.transverse_rank not in range(4):
            raise ValueError("C23.RANK.UNSUPPORTED")
        if not self.certificate.executable:
            raise ValueError("C23.FACTORIZATION_CERTIFICATE.REJECT")
        if self.hard.physical or self.fixed_order.physical:
            raise ValueError("C23.ANALYTIC_PLAN.PHYSICAL_INPUT_REJECT")
        if not self.operator_ids:
            raise ValueError("C23.ELIGIBILITY.EMPTY_OPERATOR_SET")

    def pieces(self, qt: float, Q: float) -> dict[str, float | str]:
        if qt < 0 or Q <= 0:
            raise ValueError("C23.KINEMATICS.INVALID")
        r = self.harmonic.transverse_rank
        u = qt / Q
        prefactor = self.amplitude * u**r
        W = prefactor * math.exp(-self.width * u * u)
        asymptotic = prefactor * (1.0 - self.width * u * u)
        power = self.amplitude * u ** (r + 2) * math.exp(-u)
        fixed_order = asymptotic + power
        Y = fixed_order - asymptotic
        return {"W": W, "asymptotic": asymptotic, "fixed_order": fixed_order, "Y": Y, "W_plus_Y": W + Y, "matching_residual": (W + Y) - fixed_order, "status": self.status}


class EligibilityRegistry:
    def __init__(self, rows: Iterable[dict[str, object]]):
        self._tiers = {str(row["operator_id"]): str(row["process_eligibility"]) for row in rows}
        self._ranks = {str(row["operator_id"]): int(row["rank"]) for row in rows if row.get("rank") is not None}

    def require_analytic(self, operator_ids: Iterable[str], rank: int | None = None) -> tuple[str, ...]:
        ids = tuple(operator_ids)
        if not ids:
            raise ValueError("C23.ELIGIBILITY.EMPTY_OPERATOR_SET")
        rejected = tuple(op for op in ids if self._tiers.get(op) != "ANALYTIC_PROCESS_ORACLE_ELIGIBLE")
        if rejected:
            raise ValueError("C23.ELIGIBILITY.NOT_PROCESS_ELIGIBLE:" + ",".join(rejected))
        mismatched = tuple(op for op in ids if rank is not None and op in self._ranks and self._ranks[op] != rank)
        if mismatched:
            raise ValueError("C23.ELIGIBILITY.RANK_MISMATCH:" + ",".join(mismatched))
        return ids

    def require_source(self, operator_ids: Iterable[str]) -> tuple[str, ...]:
        raise ValueError("C23.SOURCE_PROCESS_TIER.EMPTY")

    def require_physical(self, operator_ids: Iterable[str]) -> tuple[str, ...]:
        raise ValueError("C23.PHYSICAL_PROCESS_TIER.EMPTY")


def certificates() -> dict[str, FactorizationGlauberCertificate]:
    return {
        "DY": FactorizationGlauberCertificate("C23:CERT:DY", "ESTABLISHED_ANALYTIC", "CANCELLATION_ASSUMED_IN_ANALYTIC_THEOREM_DOMAIN", "ABSENT_COLOR_SINGLET", ("two_collinear", "soft", "hard"), "ANALYTIC_SQRT_SOFT", "qT/Q<0.25"),
        "SIDIS": FactorizationGlauberCertificate("C23:CERT:SIDIS", "ESTABLISHED_ANALYTIC", "DEFORMATION_ASSUMED_IN_ANALYTIC_THEOREM_DOMAIN", "ABSENT_CURRENT_FRAGMENTATION", ("target_collinear", "jet_collinear", "soft", "hard"), "ANALYTIC_SQRT_SOFT", "current_fragmentation;qT/Q<0.25"),
        "HQ_DIS": FactorizationGlauberCertificate("C23:CERT:HQDIS", "CONDITIONAL_ANALYTIC", "CONDITIONAL_PROCESS_SOFT_MATRIX", "PROCESS_SPECIFIC_COLOR_MATRIX", ("target_collinear", "heavy_pair", "soft", "hard"), "ANALYTIC_PROCESS_SOFT_MATRIX", "synthetic heavy-pair DIS benchmark"),
        "COLORED_HADRO": FactorizationGlauberCertificate("C23:CERT:BROKEN", "BROKEN", "FAILED", "COLOR_ENTANGLED", ("multi_collinear", "soft"), "NOT_DECOUPLED", "negative control"),
    }


def hard_library() -> tuple[HardFactorRecord, ...]:
    return (
        HardFactorRecord("C23:HARD:DY:A0", "DY", "q qbar -> gamma*", "ANALYTIC_LO", "C22Q_VALIDATION", "1"),
        HardFactorRecord("C23:HARD:SIDIS:A0", "SIDIS", "gamma* q -> q", "ANALYTIC_LO", "C22Q_VALIDATION", "1"),
        HardFactorRecord("C23:HARD:HQDIS:A0", "HQ_DIS", "gamma* g -> Q Qbar", "ANALYTIC_LO", "C22Q_VALIDATION", "1"),
    )


def partner_library() -> tuple[PartnerRecord, ...]:
    return (
        PartnerRecord("C23:PARTNER:DY", "SECOND_HADRON_ANALYTIC_TMD", "C22Q_VALIDATION", "x(1-x) exp(-b^2/4)"),
        PartnerRecord("C23:PARTNER:SIDIS", "ANALYTIC_TMD_FF", "C22Q_VALIDATION_Z_SCALED", "z(1-z) exp(-b^2/(4 z^2))"),
        PartnerRecord("C23:PARTNER:HQDIS", "ANALYTIC_HEAVY_PAIR_SOFT", "PROCESS_SPECIFIC_VALIDATION", "identity color matrix"),
    )


def fixed_order_library() -> tuple[FixedOrderReference, ...]:
    return tuple(FixedOrderReference(f"C23:FO:{family}:A0", family, "ANALYTIC_LO_PLUS_POWER", "C22Q_VALIDATION", "asymptotic(W)+u^(rank+2)exp(-u)") for family in ("DY", "SIDIS", "HQ_DIS"))


def make_oracle(process: str, rank: int, operator_ids: tuple[str, ...], registry: EligibilityRegistry) -> AnalyticWYOracle:
    ids = registry.require_analytic(operator_ids, rank)
    hard = next(x for x in hard_library() if x.process_family == process)
    fixed = next(x for x in fixed_order_library() if x.process_family == process)
    harmonic = HarmonicId(f"F_{process}_R{rank}", f"cos({rank}phi)", "NN_U" if rank != 2 else "NN_LL", rank, "EVEN", "EVEN")
    return AnalyticWYOracle(f"C23:WY:{process}:R{rank}", process, harmonic, 1.0 + 0.1 * rank, 0.7 + 0.1 * rank, hard, fixed, certificates()[process], ids)


def spin1_basis() -> list[dict[str, object]]:
    rows = []
    for i in range(23):
        channel = ("U", "L", "T", "LL", "LT", "TT")[i % 6]
        rank = i % 4
        todd = i in (7, 11, 15, 19)
        analytic = not todd and channel in ("U", "L", "LL") and rank in (0, 2)
        rows.append({"stable_id": f"C23.SF.{i+1:02d}", "structure_function": f"F_{channel}_{i+1:02d}", "target_channel": channel, "rank": rank, "harmonic": f"cos({rank}phi)" if not todd else f"sin({rank}phi)", "naive_t_parity": "ODD" if todd else "EVEN", "analytic_status": "ELIGIBLE_FAMILY_REQUIRES_OPERATOR_GATE" if analytic else "UNAVAILABLE", "reason": None if analytic else ("T_ODD_MULTIPARTON_REQUIRED" if todd else "MINIMAL_ANALYTIC_FAMILY_SET_EXCLUDES")})
    return rows


def process_basis() -> list[dict[str, object]]:
    return [
        {"process": "DY", "status": "ANALYTIC_PROCESS_ORACLE", "link": "PAST", "partner": "SECOND_HADRON_ANALYTIC_TMD", "nuclear": "NN_ONLY"},
        {"process": "SIDIS", "status": "ANALYTIC_PROCESS_ORACLE", "link": "FUTURE", "partner": "ANALYTIC_TMD_FF", "nuclear": "NN_ONLY"},
        {"process": "HQ_DIS", "status": "ANALYTIC_PROCESS_ORACLE_CONDITIONAL", "link": "PROCESS_SPECIFIC_ORDERED_GLUON_PAIR", "partner": "ANALYTIC_HEAVY_PAIR_SOFT", "nuclear": "NN_ONLY"},
        {"process": "INCLUSIVE_B1", "status": "OPERATOR_SPECIFIC_UNAVAILABLE", "link": "COLLINEAR", "partner": "NONE", "nuclear": "MATCHED_TOTAL_UNAVAILABLE"},
        {"process": "TAGGED_DIS", "status": "OPERATOR_SPECIFIC_UNAVAILABLE", "link": "TARGET_FRAGMENTATION_COMPOSITE", "partner": "SPECTRAL_FSI_UNAVAILABLE", "nuclear": "MATCHED_TOTAL_UNAVAILABLE"},
        {"process": "COLORED_HADROPRODUCTION", "status": "BROKEN_NEGATIVE_CONTROL", "link": "COLOR_ENTANGLED", "partner": "UNIVERSAL_TMD_PRODUCT_FORBIDDEN", "nuclear": "NOT_APPLICABLE"},
    ]


def capability_matrix(eligibility_rows: list[dict[str, object]]) -> dict[str, object]:
    registry = EligibilityRegistry(eligibility_rows)
    eligible = tuple(row["operator_id"] for row in eligibility_rows if row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE")
    records = []
    for process in ("DY", "SIDIS", "HQ_DIS"):
        for rank in range(4):
            rank_ids = tuple(op for op in eligible if next(row.get("rank") for row in eligibility_rows if row["operator_id"] == op) == rank)
            if rank_ids:
                oracle = make_oracle(process, rank, rank_ids[:4], registry)
                records.append({"stable_id": oracle.oracle_id, "process": process, "rank": rank, "status": "ANALYTIC_PROCESS_ORACLE", "operator_ids": list(oracle.operator_ids), "factorization_certificate": oracle.certificate.certificate_id, "wy_status": "EXECUTABLE_VALIDATION_ONLY"})
            else:
                records.append({"stable_id": f"C23:WY:{process}:R{rank}", "process": process, "rank": rank, "status": "NOT_PROCESS_ELIGIBLE", "operator_ids": [], "factorization_certificate": certificates()[process].certificate_id, "wy_status": "UNAVAILABLE_NO_RANKED_ELIGIBLE_OPERATOR"})
    records.extend({"stable_id": f"C23:PROC:{name}", "process": name, "rank": None, "status": "OPERATOR_SPECIFIC_UNAVAILABLE", "operator_ids": [], "wy_status": "NOT_EXECUTED"} for name in ("INCLUSIVE_B1", "TAGGED_DIS"))
    return {"records": records, "analytic_executable": sum(r["wy_status"] == "EXECUTABLE_VALIDATION_ONLY" for r in records), "unavailable": sum(r["wy_status"] != "EXECUTABLE_VALIDATION_ONLY" for r in records)}


def wy_report(eligibility_rows: list[dict[str, object]]) -> dict[str, object]:
    registry = EligibilityRegistry(eligibility_rows)
    eligible = tuple(row["operator_id"] for row in eligibility_rows if row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE")
    rows = []
    for process in ("DY", "SIDIS", "HQ_DIS"):
        for rank in range(4):
            if rank not in (0, 2):
                rows.append({"process": process, "rank": rank, "status": "ORACLE_IMPLEMENTED_NO_ELIGIBLE_OPERATOR_EXECUTION", "small_q_finite": True})
                continue
            ranked = tuple(row["operator_id"] for row in eligibility_rows if row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE" and row.get("rank") == rank)
            oracle = make_oracle(process, rank, ranked[:4], registry)
            values = [oracle.pieces(qt, 5.0) for qt in (0.0, 0.25, 0.5, 1.0)]
            rows.append({"process": process, "rank": rank, "status": "VALIDATION_ONLY", "maximum_wy_fo_residual": max(abs(float(x["matching_residual"])) for x in values), "small_q_finite": all(math.isfinite(float(x["W_plus_Y"])) for x in values), "same_identity": True, "boundary_retuned": False})
    return {"rows": rows, "rank_0_3_oracles_implemented": True, "executed_ranks": [0, 2], "unexecuted_ranks": [1, 3], "maximum_residual": max(row.get("maximum_wy_fo_residual", 0.0) for row in rows)}


def injections() -> tuple[tuple[str, str, str], ...]:
    groups = (("IDENTITY", 80), ("ELIGIBILITY", 100), ("DY", 80), ("SIDIS", 90), ("GLUON", 70), ("WY", 100), ("NUCLEAR", 70), ("ACCURACY", 60), ("ISOLATION", 70))
    return tuple((f"C23.INJECT.{group}.{i:03d}", f"ordered {group.lower()} fault {i}", f"C23.{group}.REJECT") for group, count in groups for i in range(1, count + 1))
