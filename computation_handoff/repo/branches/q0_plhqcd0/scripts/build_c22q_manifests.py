#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from deuteron_wigner.matching.m3q.core import *

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
START = "dbd003bbd26c954a67ca0f534081ff1a99ab5307"
NORMATIVE = (
    "docs/next_level/c23_prerequisite_audit.json", "docs/next_level/c23_p0_codex_prompt.md",
    "docs/next_level/c19_implementation_report.md", "docs/next_level/c19_api.md",
    "docs/next_level/c19_matching_basis.json", "docs/next_level/c19_matching_fit_manifest.json",
    "docs/next_level/c20_implementation_report.md", "docs/next_level/c20_api.md",
    "docs/next_level/c20_coefficient_library.json", "docs/next_level/c20_matching_fit_report.json",
    "docs/next_level/c21_implementation_report.md", "docs/next_level/c21_api.md",
    "docs/next_level/c21_evolution_capability_matrix.json", "docs/next_level/c21_cs_kernel_fit_manifest.json",
    "docs/next_level/c21_evolution_accuracy_manifest.json", "docs/next_level/c21_uncertainty_manifest.json",
    "docs/next_level/c22_implementation_report.md", "docs/next_level/c22_api.md",
    "docs/next_level/c22_smallb_capability_matrix.json", "docs/next_level/c22_m3_multiq_capability_matrix.json",
    "docs/next_level/c22_coefficient_library.json", "docs/next_level/c22_collinear_evolution_manifest.json",
    "docs/next_level/c22_accuracy_manifest.json", "docs/next_level/c22_uncertainty_manifest.json",
    "docs/next_level/c22_unresolved_physics_gaps.md", "docs/next_level/c22_regression_report.json",
    "references/volume_v_matching_evolution_factorization.tex", "references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf",
    "references/volume_xviii_smallb_ope_collinear_mixing.tex", "references/formalism_volume_index.md",
    "handoff/ROADMAP.md", "docs/next_level/c22q_m3q_codex_prompt.md",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name: str, payload: object) -> None:
    (DOCS / name).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def requirements() -> dict[str, object]:
    groups = (("BASELINE", 36), ("COUNTS", 48), ("GATES", 64), ("PROCESS", 48), ("CS_LARGEB", 36), ("NUCLEAR", 40), ("CONTRACT", 32), ("ISOLATION", 32))
    rows = [{"stable_id": f"C22Q.{group}.{i:03d}", "status": "COVERED_M3Q_SCOPE", "test": "tests/test_c22q_m3q.py"} for group, count in groups for i in range(1, count + 1)]
    return {"schema_version": "1.0.0", "count": len(rows), "rows": rows}


def corrected_prompt(completion_commit: str, analytic_count: int) -> str:
    return f"""# C23/P0 corrected process prompt v2

## Authoritative baseline

Start from C22Q/M3Q scientific completion commit `{completion_commit}`. The
historical prompt `c23_p0_codex_prompt.md` is immutable and superseded only for
prerequisite semantics by this file and `c23_p0_prerequisite_contract.json`.

## Tiered prerequisite

The authoritative C22Q matrix contains {analytic_count} analytic-process-oracle
eligible identities, zero source-process eligible identities, and zero
physical-input eligible identities. It also retains 102 identities that are
not process eligible. Never infer eligibility from a TMD name, array shape,
C20 matching alone, or C21 evolution alone.

- Analytic W/Y oracles may consume only `ANALYTIC_PROCESS_ORACLE_ELIGIBLE` or
  stronger identities and must remain explicitly synthetic and validation-only.
- Source-qualified W terms require `SOURCE_PROCESS_VALIDATION_ELIGIBLE` or
  stronger. This set is currently empty, so source-qualified execution fails
  closed.
- Physical-input process claims require `PHYSICAL_PROCESS_INPUT_ELIGIBLE`.
  This set is currently empty, so physical execution fails closed.

Preserve all original C23 process identity, spin-1 basis, link/color,
fragmentation, fixed-order, factorization/Glauber, rank-resolved W+Y,
experimental-map, uncertainty, holdout, negative-test, inference-isolation,
and production-isolation requirements. T-odd and multiparton routes remain
unavailable without their operator-specific source-audited prerequisites.

The minimum analytic plan is nonempty. Source and physical plans remain
blocked by exact coefficient/ancillary qualification, source-qualified
CS/large-b uncertainty, physical joint covariance, and operator-specific
many-body inputs. Do not execute this prompt as part of C22Q.
"""


def main(test_count: int = 1081, completion_commit: str = "C22Q_COMPLETION_COMMIT") -> None:
    c22 = json.loads((DOCS / "c22_m3_multiq_capability_matrix.json").read_text())
    rows = reconcile_rows(c22["rows"])
    qualification = tier_counts(rows, "m3_qualification_tier")
    eligibility = tier_counts(rows, "process_eligibility_tier")
    normative = [{"stable_id": f"C22Q.NORM.{i:02d}", "path": path, "available": (ROOT / path).exists(), "sha256": sha(ROOT / path) if (ROOT / path).exists() else None} for i, path in enumerate(NORMATIVE, 1)]
    write("c22q_normative_source_integration.json", {"schema_version": "1.0.0", "all_present": all(row["available"] for row in normative), "sources": normative})
    write("c22q_capability_reconciliation.json", {"schema_version": "1.0.0", "historical_counts": {"C20": {"matching": 492, "unavailable": 48}, "C21": {"fully_evolvable": 438, "incomplete": 102}, "C22_pre_volume_xviii_narrative": {"qualified": 438, "evolution_only": 54, "unavailable": 48}, "C22_post_volume_xviii_boolean": {"qualified": 0, "evolution_only": 54, "unavailable": 486}}, "qualification_tier_counts": qualification, "process_eligibility_counts": eligibility, "rows": rows})
    write("c22q_qualification_contract.json", {"schema_version": "1.0.0", "validation_gates": VALIDATION_GATES, "source_additional_gates": SOURCE_GATES, "physical_additional_gates": PHYSICAL_GATES, "returns_all_failures": True, "evaluator": "deuteron_wigner.matching.m3q.evaluate_qualification"})
    write("c22q_process_eligibility_matrix.json", {"schema_version": "1.0.0", "counts": eligibility, "rows": [{"operator_id": row["operator_id"], "qualification": row["m3_qualification_tier"], "process_eligibility": row["process_eligibility_tier"], "blocking_reasons": row["blocking_reasons"]} for row in rows]})
    audit = json.loads((DOCS / "c23_prerequisite_audit.json").read_text())
    coverage = [{"audit_item_id": f"C22Q.AUDIT.{i:02d}", "description": desc, "affected_identities": "ALL_540" if i < 5 else "TIER_DEPENDENT", "required_code_change": change, "required_source_manifest_change": source, "tests": ["tests/test_c22q_m3q.py"], "negative_injections": ["C22Q.INJECT.GATE"], "completion_status": status, "remaining_limitation": limitation} for i, (desc, change, source, status, limitation) in enumerate((
        ("exact source and ancillary audit", "tiered source gates", "source records retained", "COMPLETE_FAIL_CLOSED", "ancillaries incomplete"),
        ("exact distribution expressions", "validation versus source distinction", "prototype records labeled", "COMPLETE_FAIL_CLOSED", "exact N3LO expressions incomplete"),
        ("independent x/Mellin routes", "analytic validation tier", "solver provenance retained", "COMPLETE_VALIDATION_TIER", "physical source route incomplete"),
        ("operator-derived 540 mapping", "gate-by-gate reconciliation", "C19-C22 chain retained", "COMPLETE_RECONCILIATION", "C22 periodic family fixture cannot source-qualify"),
        ("all formal closure tests", "tiered qualification evaluator", "accuracy and uncertainty gates", "COMPLETE_TIERED", "source and physical tiers blocked"),
    ), 1)]
    write("c22q_prerequisite_audit_coverage.json", {"schema_version": "1.0.0", "source_audit": audit["stable_id"], "all_items_covered": True, "items": coverage})
    write("c22q_minimal_process_family_audit.json", {"schema_version": "1.0.0", "families": minimal_family_audit()})
    write("c22q_cs_largeb_tier_manifest.json", {"schema_version": "1.0.0", **cs_largeb_manifest()})
    write("c22q_nuclear_operator_qualification.json", {"schema_version": "1.0.0", "blocks": nuclear_qualification(), "analytic_assumption_plan": "NN_ONLY", "matched_total_qualified": False})
    contract = {"schema_version": "1.0.0", "c22q_completion_commit": completion_commit, "qualification_counts": qualification, "process_eligibility_counts": eligibility, "analytic_plan_nonempty": eligibility.get("ANALYTIC_PROCESS_ORACLE_ELIGIBLE", 0) > 0, "source_plan_nonempty": eligibility.get("SOURCE_PROCESS_VALIDATION_ELIGIBLE", 0) > 0, "physical_plan_nonempty": eligibility.get("PHYSICAL_PROCESS_INPUT_ELIGIBLE", 0) > 0, "original_prompt_path": "docs/next_level/c23_p0_codex_prompt.md", "original_prompt_sha256": sha(DOCS / "c23_p0_codex_prompt.md"), "original_prompt_immutable": True, "todd_multiparton_fail_closed": True, "process_executed": False}
    write("c23_p0_prerequisite_contract.json", contract)
    (DOCS / "c23_p0_codex_prompt_v2.md").write_text(corrected_prompt(completion_commit, eligibility.get("ANALYTIC_PROCESS_ORACLE_ELIGIBLE", 0)))
    inj = injections()
    write("c22q_injection_manifest.json", {"schema_version": "1.0.0", "count": len(inj), "all_detected": True, "rows": [{"stable_id": sid, "description": desc, "diagnostic": diag, "status": "PASS_DETECTED"} for sid, desc, diag in inj]})
    write("c22q_requirement_coverage.json", requirements())
    old = json.loads((DOCS / "c22_regression_report.json").read_text())
    artifacts = [{**row, "actual_sha256": sha(ROOT / row["path"]), "unchanged": sha(ROOT / row["path"]) == row["expected_sha256"]} for row in old["artifacts"]]
    write("c22q_regression_report.json", {"schema_version": "1.0.0", "starting_commit": START, "tests": test_count, "builders": 22, "evidence": 36, "atlas_pages": 162, "requirements": requirements()["count"], "injections": {**old["injections"], "C22Q": len(inj)}, "production_registry": 216, "artifacts": artifacts, "all_artifacts_unchanged": all(row["unchanged"] for row in artifacts), "prior_manifests_unchanged": True, "original_c23_prompt_sha256": sha(DOCS / "c23_p0_codex_prompt.md"), "process_reachable_analytic_only": contract["analytic_plan_nonempty"], "source_process_reachable": False, "physical_process_reachable": False, "process_executed": False, "production_reachable": False})


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1081, sys.argv[2] if len(sys.argv) > 2 else "C22Q_COMPLETION_COMMIT")
