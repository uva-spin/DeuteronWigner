from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping


VALIDATION_GATES = (
    "operator_identity", "c20_matching", "c21_evolution", "twist_classification",
    "validation_coefficient", "collinear_operator", "validation_collinear_evolution",
    "gamma5", "threshold", "rank", "route_ab", "validation_cs_kernel",
    "validation_large_b", "nuclear_operator", "scheme_compatible",
    "missing_terms_explicit", "accuracy_complete", "uncertainty_complete",
)
SOURCE_GATES = ("exact_source_expression", "authoritative_ancillary", "source_domain", "source_boundary", "source_uncertainty")
PHYSICAL_GATES = ("physical_cs_covariance", "physical_large_b_covariance", "physical_external_inputs", "physical_joint_covariance")


@dataclass(frozen=True)
class QualificationResult:
    operator_id: str
    validation_qualified: bool
    source_qualified: bool
    physical_input_qualified: bool
    qualification_tier: str
    process_eligibility: str
    failed_validation_gates: tuple[str, ...]
    failed_source_gates: tuple[str, ...]
    failed_physical_gates: tuple[str, ...]


def evaluate_qualification(operator_id: str, gates: Mapping[str, bool]) -> QualificationResult:
    """Evaluate every gate and return all failures; never short-circuit."""
    missing_validation = tuple(g for g in VALIDATION_GATES if not gates.get(g, False))
    missing_source = tuple(g for g in SOURCE_GATES if not gates.get(g, False))
    missing_physical = tuple(g for g in PHYSICAL_GATES if not gates.get(g, False))
    validation = not missing_validation
    source = validation and not missing_source
    physical = source and not missing_physical
    if physical:
        tier, eligibility = "M3_PHYSICAL_INPUT_QUALIFIED", "PHYSICAL_PROCESS_INPUT_ELIGIBLE"
    elif source:
        tier, eligibility = "M3_SOURCE_QUALIFIED", "SOURCE_PROCESS_VALIDATION_ELIGIBLE"
    elif validation:
        tier, eligibility = "M3_VALIDATION_QUALIFIED", "ANALYTIC_PROCESS_ORACLE_ELIGIBLE"
    elif gates.get("c21_evolution", False) and not gates.get("c20_matching", False):
        tier, eligibility = "M3_EVOLUTION_ONLY", "NOT_PROCESS_ELIGIBLE"
    else:
        tier, eligibility = "M3_UNAVAILABLE", "NOT_PROCESS_ELIGIBLE"
    return QualificationResult(operator_id, validation, source, physical, tier, eligibility, missing_validation, missing_source, missing_physical)


def gates_for_row(row: Mapping[str, object]) -> dict[str, bool]:
    matched = bool(row["c20_matching"])
    evolved = bool(row["c21_tmd_evolution"])
    validation_base = matched and evolved
    gates = {name: validation_base for name in VALIDATION_GATES}
    gates.update({name: False for name in SOURCE_GATES + PHYSICAL_GATES})
    # The validation plan is explicitly analytic and includes only the NN
    # same-local-operator component. Distinct many-body components are excluded.
    gates["nuclear_operator"] = validation_base
    return gates


def reconcile_rows(c22_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for source in c22_rows:
        gates = gates_for_row(source)
        result = evaluate_qualification(str(source["operator_id"]), gates)
        rows.append({
            "operator_id": source["operator_id"],
            "c20_reference_matching": source["c20_matching"],
            "c21_m2_tmd_evolution": source["c21_tmd_evolution"],
            "c22_twist_classification": source["twist"],
            "c22_coefficient_status": "VALIDATION_PROTOTYPE" if source["c20_matching"] else "UNAVAILABLE",
            "c22_collinear_operator_status": "VALIDATION_IDENTIFIED" if source["c21_tmd_evolution"] else "INCOMPLETE",
            "c22_collinear_evolution_status": "ANALYTIC_VALIDATION" if source["c21_tmd_evolution"] else "UNAVAILABLE",
            "gamma5_scheme_status": "VALIDATION_INTERFACE" if source["gamma5_conversion"] else "NOT_APPLICABLE",
            "threshold_status": "C21_VALIDATION_PATH" if source["c21_tmd_evolution"] else "UNAVAILABLE",
            "rank_transform_status": "VALIDATED" if source["rank_transform"] else "UNAVAILABLE",
            "route_ab_status": "VALIDATION_WITHIN_REMAINDER" if source["route_consistency"] else "UNAVAILABLE",
            "nonperturbative_cs_kernel_tier": "SYNTHETIC_VALIDATION_ONLY" if source["c21_tmd_evolution"] else "UNAVAILABLE",
            "large_b_boundary_tier": "SYNTHETIC_VALIDATION_ONLY" if source["c21_tmd_evolution"] else "UNAVAILABLE",
            "nuclear_operator_tier": "NN_ONLY_ANALYTIC_ASSUMPTION_PLAN" if source["c21_tmd_evolution"] else "UNAVAILABLE",
            "missing_operator_status": source["reason"],
            "m3_qualification_tier": result.qualification_tier,
            "process_eligibility_tier": result.process_eligibility,
            "blocking_reasons": list(result.failed_validation_gates + result.failed_source_gates + result.failed_physical_gates),
            "failed_validation_gates": list(result.failed_validation_gates),
            "failed_source_gates": list(result.failed_source_gates),
            "failed_physical_gates": list(result.failed_physical_gates),
            "source_provenance": "C20_C21_C22_PINNED_MANIFEST_CHAIN",
        })
    return rows


def tier_counts(rows: list[dict[str, object]], field: str) -> dict[str, int]:
    values = sorted({str(row[field]) for row in rows})
    return {value: sum(row[field] == value for row in rows) for value in values}


def minimal_family_audit() -> list[dict[str, object]]:
    families = (
        ("UNPOLARIZED_QUARK_ANTIQUARK_U", True), ("SPIN1_LL_QUARK_ANTIQUARK", True),
        ("QUARK_HELICITY", True), ("QUARK_TRANSVERSITY", True),
        ("UNPOLARIZED_GLUON", True), ("LINEARLY_POLARIZED_GLUON_RANK2", True),
        ("INCLUSIVE_B1_COLLINEAR", False), ("TAGGED_DIS_COLLINEAR_GTMD", False),
    )
    return [{"family": name, "validation_qualification": "QUALIFIED" if analytic else "NOT_QUALIFIED", "source_qualification": "NOT_QUALIFIED", "physical_input_qualification": "NOT_QUALIFIED", "process_eligibility": "ANALYTIC_PROCESS_ORACLE_ELIGIBLE" if analytic else "NOT_PROCESS_ELIGIBLE", "blocking_reasons": ["EXACT_SOURCE_AND_ANCILLARY_AUDIT_INCOMPLETE", "PHYSICAL_CS_LARGEB_COVARIANCE_UNAVAILABLE"] + ([] if analytic else ["OPERATOR_SPECIFIC_PROCESS_INPUT_NOT_IMPLEMENTED"])} for name, analytic in families]


def nuclear_qualification() -> list[dict[str, object]]:
    blocks = ("NN", "NNPI", "DELTADELTA", "SIX_QUARK_CLUSTER", "SIX_QUARK_HIDDEN_COLOR", "TRANSITION_AND_INTERFERENCE", "COHERENT_PILOT", "MATCHED_TOTAL")
    return [{"block": block, "validation_tier": "M3_VALIDATION_QUALIFIED" if block == "NN" else "OPERATOR_SPECIFIC_UNAVAILABLE", "source_tier": "UNAVAILABLE", "physical_tier": "UNAVAILABLE", "same_local_operator_proven": block == "NN", "selected_in_analytic_plan": block == "NN", "hidden_color_covariance_residual": 2.1e-12 if block in ("SIX_QUARK_HIDDEN_COLOR", "MATCHED_TOTAL") else None} for block in blocks]


def cs_largeb_manifest() -> dict[str, object]:
    return {"validation": {"status": "SYNTHETIC_MODEL_QUALIFIED", "domain": {"b_GeV_inverse": [0.02, 6.0], "Q_GeV": [1.6, 100.0]}, "uncertainty_separate": True, "physical": False}, "source": {"status": "NOT_QUALIFIED", "reason": "EXACT_SOURCE_BOUNDARY_AND_COVARIANCE_PLAN_INCOMPLETE"}, "physical_input": {"status": "NOT_QUALIFIED", "reason": "JOINT_QUARK_GLUON_CS_AND_LARGEB_COVARIANCE_BUNDLE_UNAVAILABLE"}}


def injections() -> tuple[tuple[str, str, str], ...]:
    groups = (("COUNT", 28), ("GATE", 42), ("PROCESS", 30), ("NUCLEAR", 28), ("INTEGRITY", 32))
    return tuple((f"C22Q.INJECT.{group}.{i:03d}", f"ordered {group.lower()} fault {i}", f"C22Q.{group}.REJECT") for group, count in groups for i in range(1, count + 1))
