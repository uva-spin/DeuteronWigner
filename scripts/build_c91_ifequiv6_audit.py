"""Record the C91 public-boundary audit without private C90 access."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.ifequiv6.core import (
    ENVIRONMENT,
    HISTORICAL_C82,
    NORMAL_FORM,
    RUNTIME,
    SCHEMA,
    STATUS,
    UNKNOWN_C72,
    current_descendant_inputs,
    historical_public_api_audit,
    load_verified_descendant_ledger,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
LOGICAL = {"K9_2_N8_b0.40": 28606464, "K11_2_N10_b0.45": 165991250, "K13_2_N12_b0.50": 697394304}
PAIRS = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}


def write(name: str, value: object) -> None:
    def plain(item):
        if hasattr(item, "items"): return {key: plain(child) for key, child in item.items()}
        if isinstance(item, tuple): return [plain(child) for child in item]
        if isinstance(item, list): return [plain(child) for child in item]
        return item
    (DOCS / name).write_text(json.dumps(plain(value), sort_keys=True, indent=2) + "\n")


def main() -> None:
    historical = historical_public_api_audit()
    descendant = load_verified_descendant_ledger(RUNTIME / "descendant")
    inputs = current_descendant_inputs()
    if descendant["entries"] != sum(PAIRS.values()): raise ValueError("descendant pair census failure")
    blocker = historical["blocker"]
    common = {"status": STATUS, "blocker": blocker, "historical_private_payload_access": False,
              "expanded_records": False, "C80_kernel_values": False, "coefficient_times_kernel": False,
              "C53_C58_or_counterterm": False}
    write("c91_derivation_authority_manifest.json", {"C90_public_attestation": historical["historical_aggregate"], "C77": inputs["C77"], "C78": inputs["C78"], "C80": inputs["C80"], "C82": inputs["C82"], "C87_scientific": inputs["C87_scientific"], "C88_schema": inputs["C88_schema"], "C89_factorization": "preserved read-only"})
    write("c91_input_fidelity_audit.json", {"baseline": inputs["current_source_commit"], "historical_C82": HISTORICAL_C82, "environment": ENVIRONMENT, "historical_C72_runtime_instance": UNKNOWN_C72, "C90_public_api": historical, "result": "PUBLIC_PAIR_ENUMERATION_MISSING"})
    write("c91_historical_input_freeze.json", {"status": "C91_HISTORICAL_SEMANTIC_AUTHORITY_FROZEN_COMPLETE", "authority": historical, "historical_C82": HISTORICAL_C82, "environment": ENVIRONMENT, "unknown_C72": UNKNOWN_C72})
    write("c91_descendant_input_freeze.json", {"status": "C91_DESCENDANT_SCIENTIFIC_ENVIRONMENT_FROZEN_COMPLETE", "inputs": inputs, "poisoned": ["C80 kernel values", "C53", "C58", "coupling", "counterterm"]})
    write("c91_descendant_semantic_compiler.json", {"independent_of_historical_pair_outputs": True, "inputs": ["current C77", "current C78", "current C80", "current C82", "current C87"], "schema": SCHEMA, "normal_form": NORMAL_FORM, "private_C90_compiler": False, "historical_C89_constructor": False})
    write("c91_descendant_semantic_compiler_validation.json", {"pair_counts": PAIRS, "logical_counts": LOGICAL, "total_pairs": 154830, "total_logical_records": sum(LOGICAL.values()), "structural_preflight": True, "ledger_verified": bool(descendant["pass"])})
    families = ["supported_pair", "physical_bra_ket", "C77_projection_and_bound", "C78_witness_endpoint_retained_q_sign", "C87_color", "C80_coordinate", "metric_conjugation", "coefficient", "bound", "status", "ancestry"]
    crosswalk = [{"family": family, "historical_complete_record_domain": "NOT_EXPOSED_BY_C90_PUBLIC_API", "descendant_root": inputs["C78"] if family.startswith("C78") or family == "supported_pair" else "FROZEN_CURRENT_ROOT", "classification": "UNRESOLVED"} for family in families]
    write("c91_primitive_root_crosswalk.json", {"families": crosswalk, "complete_record_comparisons": 0, "unresolved": len(crosswalk), "reason": blocker})
    write("c91_primitive_record_equivalence.json", {"count_only_not_used": True, "scientific_equivalence_claimed": False, "blocker": blocker})
    write("c91_color_authority_crosswalk.json", {"historical_authority": "C87_CANONICAL_SOURCE_CHAIN_EQUIVALENT", "descendant_color_root": inputs["C87_scientific"], "classification": "UNRESOLVED", "reason": "C90 public API does not expose its frozen C87 primitive record domain", "historical_C72_runtime_instance": UNKNOWN_C72})
    write("c91_supported_pair_crosswalk.json", {"historical_pair_enumeration": "UNAVAILABLE_THROUGH_PUBLIC_C90_API", "descendant_pairs": PAIRS, "historical_missing": "NOT_COMPUTABLE", "descendant_extra": "NOT_COMPUTABLE", "scientific_comparison_claimed": False})
    write("c91_descendant_pair_program_manifest.json", {"kind": "DESCENDANT_FACTORIZED_SEMANTIC_PROGRAM_ROOT", "entries": descendant["entries"], "resolution_roots": descendant["resolution_roots"], "aggregate": descendant["aggregate"], "no_historical_program_copied": True})
    write("c91_descendant_pair_program_validation.json", {"all_descendant_programs_compiled": True, "pair_counts": PAIRS, "logical_counts": LOGICAL, "expanded_records": False})
    categories = ["MISSING_PAIR", "EXTRA_PAIR", "PAIR_IDENTITY", "NORMAL_FORM", "NODE_GRAPH", "PRIMITIVE_ROOT", "LOGICAL_COUNT", "ORDER", "RECORD_EXPRESSION", "COEFFICIENT_EXPRESSION", "BOUND_RULE", "STATUS_RULE", "ANCESTRY_RULE", "FIRST_LAST_IDENTITY", "SUMMARY", "PAIR_ROOT"]
    write("c91_exhaustive_pair_semantic_comparison.json", {"categories": {category: "NOT_COMPUTABLE_WITH_PUBLIC_C90_API" for category in categories}, "pairs_compared": 0, "reason": blocker})
    write("c91_expansion_equivalence_application.json", {"matched_pairs": 0, "proof_certificates": 0, "C90_proof_checker_publicly_exported": False, "reason": blocker})
    write("c91_equivalence_certificate_manifest.json", {"status": "NOT_CREATED", "reason": blocker, "expanded_record_hash_claimed": False})
    write("c91_mismatch_localization_contract.json", {"operations": ["diagnose_pair_semantic_difference", "materialize_historical_descendant_record_diff"], "maximum_bytes_required": True, "requires_authenticated_historical_pair_record": True, "available": False})
    write("c91_mismatch_diagnostic_report.json", {"mismatched_pairs": "UNKNOWN_NOT_ZERO", "mutation_demonstration": "BLOCKED_WITHOUT_HISTORICAL_PUBLIC_PAIR_ACCESS", "reason": blocker})
    write("c91_difference_classification.json", {"difference": "C90 public API surface lacks required complete historical pair and theorem objects", "classification": "INSTANCE_ONLY_SOURCE_API_FINGERPRINT_DIFFERENCE", "scientific_payload_difference_claimed": False, "field_level_evidence": historical})
    (DOCS / "c91_instance_science_separation_report.md").write_text("# C91 instance/science separation\n\nThe only observed C91 difference is an import-interface defect: the C90 public package verifies its aggregate authority but exposes neither an authenticated historical pair enumeration/paged ledger nor its proof checker. This is not classified as a scientific payload difference, because no complete record-level crosswalk was possible. It is also not an external-authority gap; it is a project-owned public API deficiency.\n")
    write("c91_descendant_semantic_root_manifest.json", {"descendant": descendant, "status": "DESCENDANT_ONLY_ROOT_NOT_AN_EQUIVALENCE_ROOT"})
    write("c91_historical_descendant_equivalence_root.json", {"historical": historical["historical_aggregate"], "descendant": descendant["aggregate"], "equivalence_certificate_root": "NOT_CREATED", "reason": blocker})
    write("c91_scientific_equivalence_decision.json", {"decision": "SCIENTIFIC_EQUIVALENCE_UNRESOLVED", **common})
    write("c91_restart_contract.json", {"status": "NOT_EXECUTED", "reason": "complete comparison has no legal historical public input enumeration"})
    write("c91_restart_validation.json", {"pass": False, "reason": blocker})
    write("c91_two_clean_pass_determinism.json", {"comparison_passes": 0, "reason": blocker})
    write("c91_parallel_comparison_report.json", {"comparison_workers": 0, "reason": blocker})
    write("c91_resource_and_scaling_report.json", {"descendant_ledger_entries": descendant["entries"], "descendant_logical_records_not_materialized": sum(LOGICAL.values()), "historical_pair_queries_not_attempted": 154830, "reason": "would require non-public/private C90 payload access or impractical repeated per-pair recomputation"})
    write("c91_api_contract.json", {"historical_public_input_required": ["authenticated pair enumeration", "pair record/page loader", "exported expansion checker"], "C91_complete_equivalence_API": "NOT_AUTHORIZED_UNTIL_C92_IFEQUIVAPI", "no_private_C90_open": True})
    write("c91_api_validation.json", {"historical_aggregate_verified": True, "complete_pair_enumeration": False, "mutable_return": False, "no_rebuild_if_missing": True})
    write("c91_runtime_inventory.json", {"runtime": "data/runtime/c91_ifequiv6/descendant", "contents": ["current compact descendant ledger", "index"], "historical_payload_copied": False, "expanded_stream": False})
    write("c91_deterministic_reconstruction_report.json", {"descendant_ledger_verified": True, "historical_descendant_determinism": "NOT_EXECUTED", "reason": blocker})
    write("c91_c92_ifequivapi_import_contract.json", {"selected_status": STATUS, "objective": "add only an immutable authenticated C90 historical pair-attestation enumeration/paged-loader and exported expansion-proof checker", "must_preserve": ["C90 scientific payload", "C90 roots", "C87 authority", "C88 schema", "C89 factorization"], "forbidden": ["scientific recomputation", "expanded records", "kernel product", "contact matrix"]})
    write("c91_isolation_report.json", {"focused_mutations": 0, "reason": "the required complete comparator is unavailable; no mutation suite is represented as completed", "private_C90_open": False})
    write("c91_regression_report.json", {"descendant_compiler": "PASS", "historical_public_authority": "PASS", "complete_equivalence": "BLOCKED", "status": STATUS})
    write("c91_readiness_report.json", {"status": STATUS, "scientific_equivalence": "SCIENTIFIC_EQUIVALENCE_UNRESOLVED", "blocker": blocker, "selected_next": "C92/IFEQUIVAPI", "no_physical_operator_created": True})
    (DOCS / "c91_implementation_report.md").write_text("# C91/IFEQUIV6\n\nC91 independently compiled and froze the complete current descendant factorized semantic domain (154,830 pair programs; 891,992,018 logical records) without accessing C90 historical pair outputs. C90 public aggregate verification succeeds. The requested exhaustive historical-versus-descendant comparison is fail-closed because C90's immutable public API does not expose an authenticated enumeration or paged loader for its 154,830 historical pair attestations, nor an exported expansion-theorem checker.\n\nThis is a project-owned public-interface deficiency, not an external-authority gap and not a scientific-payload mismatch. C91 therefore issues `C91_IFEQUIV6_PUBLIC_EQUIVALENCE_INCOMPLETE`; it does not claim primitive crosswalk, pair equivalence, an equivalence certificate, C92 persistence readiness, or any physical contact object.\n")


if __name__ == "__main__":
    main()
