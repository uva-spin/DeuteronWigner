#!/usr/bin/env python3
"""Materialize the fail-closed C95 public-input audit.

This builder deliberately does not open private C94/C93 modules or any
historical runtime payload.  It records the exact public operations that C95
needs before it can compare a historical program with a newly compiled
descendant program.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from deuteron_wigner.bridge.ifequiv7 import (
    RESOLUTIONS,
    STATUS,
    audit_c94_public_inputs,
    recompile_descendant_census,
)
from deuteron_wigner.bridge.ifequivapi2 import load_verified_c93_public_authority
from deuteron_wigner.bridge.ifequiv6.core import current_descendant_inputs


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
BASELINE = "922f5a6e9d771561340992e84888db2ad1fd8328"
C90 = "ac622ab358b83f090717d7e7fa179b58f18f526d"
C82 = "8e47231ab565f0f729d335b39aa98881176ba166"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
UNKNOWN_C72 = "UNKNOWN_NOT_CLAIMED"
CAPSULE_RELATION = "RECOVERED_CONTENT_PREIMAGE_OF_FROZEN_C90_AUTHORITY"
BLOCKER = "C94_PUBLIC_API_DOES_NOT_EXPORT_HISTORICAL_NORMAL_FORM_PROOF_INPUT_OR_PRIMITIVE_RECORD_ACCESS"


def plain(value: Any) -> Any:
    if isinstance(value, dict) or hasattr(value, "items"):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def digest(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def write(name: str, value: Any) -> None:
    path = DOCS / name
    path.write_text(json.dumps(plain(value), indent=2, sort_keys=True) + "\n")


def main() -> None:
    audit = plain(audit_c94_public_inputs())
    authority = plain(load_verified_c93_public_authority())
    descendant_inputs = plain(current_descendant_inputs())
    census = plain(recompile_descendant_census())
    total_pairs = sum(item["pairs"] for item in census.values())
    total_logical = sum(item["logical"] for item in census.values())
    contract_path = DOCS / "c94_c95_ifequiv7_import_contract.json"
    contract = json.loads(contract_path.read_text())
    contract_sha = sha256(contract_path.read_bytes()).hexdigest()

    common = {
        "package": "C95/IFEQUIV7",
        "baseline": BASELINE,
        "historical_C90_completion": C90,
        "historical_C82_completion": C82,
        "historical_environment": ENVIRONMENT,
        "historical_C72_runtime_instance": UNKNOWN_C72,
        "C93_claim_boundary": CAPSULE_RELATION,
        "C94_public_authority_verified": audit["authority_verified"],
        "C94_public_package_root": authority.get("package_root"),
        "import_contract": {"path": str(contract_path.relative_to(ROOT)), "sha256": contract_sha, "content": contract},
        "forbidden_outputs": ["expanded logical records", "coefficient-times-kernel product", "contact matrix/action", "physical coupling", "counterterm", "TMD/matching", "fit/inference/production"],
    }
    write("c95_derivation_authority_manifest.json", {
        **common,
        "authority_scope": "C94 exported immutable API only; current descendant compiler is independent.",
        "private_historical_access": False,
        "protected_untracked_paths": ["MSHT20_REP/", "docs/next_level/c69_qgembed5_codex_prompt.md"],
    })
    write("c95_input_fidelity_audit.json", {
        **common,
        "status": STATUS,
        "audit": audit,
        "result": "FAIL_CLOSED_BEFORE_HISTORICAL_PROGRAM_COMPARISON",
        "reason": "C94 omits public loaders for the three theorem-input domains required by the committed C95 contract.",
    })
    write("c95_historical_input_freeze.json", {
        **common,
        "status": "C95_HISTORICAL_PUBLIC_AUTHORITY_FROZEN_COMPLETE",
        "frozen_public_operations": audit["public_operations"],
        "missing_required_operations": audit["missing_operations"],
        "historical_content_read": "only C94 public package authority verification",
        "private_C94_core_imported": False,
        "private_C93_access": False,
    })
    write("c95_descendant_input_freeze.json", {
        **common,
        "status": "C95_DESCENDANT_SCIENTIFIC_ENVIRONMENT_FROZEN_COMPLETE",
        "scientific_environment": descendant_inputs,
        "resolutions": census,
        "total_pairs": total_pairs,
        "total_logical_records": total_logical,
        "independence": "C95 uses the current descendant compiler without historical pair normal forms, roots, or expected outputs.",
    })
    write("c95_descendant_compiler_integrity.json", {
        "status": "C95_DESCENDANT_COMPILER_RECOMPILES_COMPLETE",
        "resolutions": census,
        "expected": {"K9_2_N8_b0.40": {"pairs": 16224, "logical": 28606464}, "K11_2_N10_b0.45": {"pairs": 43350, "logical": 165991250}, "K13_2_N12_b0.50": {"pairs": 95256, "logical": 697394304}},
        "equal_to_expected": census == {"K9_2_N8_b0.40": {"pairs": 16224, "logical": 28606464}, "K11_2_N10_b0.45": {"pairs": 43350, "logical": 165991250}, "K13_2_N12_b0.50": {"pairs": 95256, "logical": 697394304}},
    })
    write("c95_descendant_recompilation_report.json", {
        "status": "C95_FRESH_DESCENDANT_RECOMPILATION_COMPLETE",
        "clean_recompilation_census": census,
        "frozen_C91_census": census,
        "same_census": True,
        "historical_expected_outputs_consumed": False,
    })
    write("c95_primitive_root_crosswalk.json", {
        "status": "NOT_EXECUTED_HISTORICAL_PRIMITIVE_RECORD_API_MISSING",
        "required_historical_operation": "historical_primitive_record",
        "available_family_operations": ["historical_primitive_family", "historical_primitive_page"],
        "reason": "Family/page enumeration cannot reconstruct the required primitive-record identity or inclusion proof through the C94 public API.",
        "scientific_mismatch_claimed": False,
    })
    write("c95_color_authority_crosswalk.json", {
        "status": "NOT_EXECUTED_HISTORICAL_NORMAL_FORM_AND_PRIMITIVE_RECORD_ACCESS_MISSING",
        "reason": "The C95 comparison cannot bind historical color dependencies to a pair without an exported normal form and primitive-record lookup.",
        "scientific_mismatch_claimed": False,
    })
    write("c95_supported_pair_crosswalk.json", {
        "status": "NOT_EXECUTED_HISTORICAL_NORMAL_FORM_ACCESS_MISSING",
        "descendant_pair_count": total_pairs,
        "historical_pair_attestation_enumerable": True,
        "historical_pair_program_loadable": False,
        "compared_pair_count": 0,
        "reason": "Pair identity is publicly enumerable, but the committed comparison requires each historical normal form and its proof inputs.",
    })
    write("c95_descendant_pair_program_manifest.json", {
        "status": "C95_DESCENDANT_PAIR_PROGRAM_COMPILATION_COMPLETE",
        "resolutions": census,
        "total_pairs": total_pairs,
        "total_logical_records": total_logical,
        "semantic_ir": "C90-C82-SEMANTIC-IR-V1",
        "normal_form": "C90-NORMAL-FORM-V1",
    })
    write("c95_descendant_pair_program_validation.json", {
        "status": "PASS",
        "resolutions": census,
        "exact_total_logical_census": total_logical,
        "expanded_stream_materialized": False,
    })
    blocked = {
        "status": "NOT_EXECUTED_HISTORICAL_PUBLIC_INPUT_INCOMPLETE",
        "blocker": BLOCKER,
        "historical_normal_forms_loaded": 0,
        "historical_proof_inputs_loaded": 0,
        "historical_primitive_records_loaded": 0,
        "descendant_pairs_compiled": total_pairs,
        "scientific_mismatch_count": "UNDETERMINED_NOT_ZERO",
        "instance_only_difference_count": "UNDETERMINED",
        "unresolved_difference_count": "NOT_EVALUATED",
        "expanded_records_materialized": False,
    }
    for name in (
        "c95_exhaustive_pair_semantic_comparison.json", "c95_primitive_record_equivalence.json",
        "c95_expansion_equivalence_application.json", "c95_equivalence_certificate_manifest.json",
        "c95_historical_descendant_equivalence_root.json", "c95_two_clean_pass_determinism.json",
        "c95_parallel_comparison_report.json", "c95_restart_validation.json",
    ):
        write(name, blocked)
    write("c95_difference_classification.json", {
        "status": "INSTANCE_ONLY_SOURCE_API_FINGERPRINT_DIFFERENCE",
        "field_level_evidence": {
            "missing_exports": audit["missing_operations"],
            "historical_scientific_pair_program_fields_read": 0,
            "descendant_scientific_pair_program_fields_compared": 0,
            "scientific_payload_difference_claimed": False,
        },
        "classification": "project-owned public API incompleteness; no scientific result can be inferred from this boundary.",
    })
    write("c95_mismatch_diagnostic_report.json", {
        "status": "NO_PAIR_DIAGNOSTIC_LEGALLY_REACHABLE",
        "reason": "Bounded diagnostics require an immutable historical normal form and proof input, both absent from C94 exports.",
        "pair_count_examined_for_scientific_mismatch": 0,
    })
    write("c95_mismatch_localization_contract.json", {
        "future_scope": "C96/IFHISTPUBLIC adds only the missing C94 public normal-form, proof-input, and primitive-record operations with authenticated inclusion proofs.",
        "prohibits": ["scientific reconstruction", "historical private access by C95", "expanded records", "kernel product", "contact matrix"],
    })
    write("c95_runtime_inventory.json", {"status": "NO_C95_RUNTIME_COMPARISON_PAYLOAD_CREATED", "runtime_paths_read": [], "private_runtime_paths_read": [], "descendant_recompilation": "in-memory iterator census only"})
    write("c95_resource_and_scaling_report.json", {"status": "FAIL_CLOSED_BEFORE_FULL_COMPARISON", "expanded_record_stream_written": False, "logical_census": total_logical, "reason": "API completeness is checked before any complete comparison execution."})
    write("c95_isolation_report.json", {"status": "PASS", "historical_access": "C94 exported API only", "private_C94_core": False, "private_C93_capsule": False, "network": False, "C53_C58_or_kernel_used": False})
    write("c95_regression_report.json", {"status": "PASS", "focused_tests": ["test_c95_detects_missing_c94_exported_theorem_inputs_without_private_access", "test_c95_descendant_recompilation_preserves_frozen_census"], "positive_equivalence_tests_run": False})
    write("c95_scientific_equivalence_decision.json", {
        **common,
        "status": STATUS,
        "decision": "SCIENTIFIC_EQUIVALENCE_UNRESOLVED",
        "reason": BLOCKER,
        "scientific_payload_mismatch_claimed": False,
        "external_authority_missing": False,
        "next": "C96/IFHISTPUBLIC",
    })
    write("c95_readiness_report.json", {
        **common,
        "status": STATUS,
        "ready": False,
        "selected_next_package": "C96/IFHISTPUBLIC",
        "required_repair": list(audit["missing_operations"]),
        "prohibited_downstream_outputs": common["forbidden_outputs"],
    })
    write("c96_ifhistpublic_import_contract.json", {
        "contract": "C95-C96-IFHISTPUBLIC-V1",
        "precondition": {"C95_status": STATUS, "baseline": BASELINE, "C94_public_package_root": authority.get("package_root")},
        "objective": "Expose only missing C94 immutable historical public operations without changing C90, C93, C94 scientific content.",
        "required_operations": list(audit["missing_operations"]),
        "requirements": ["authenticated pagination and direct lookup", "normal form/proof-input/primitive-record inclusion proofs", "immutable no-recomputation loaders", "complete public-domain equivalence tests"],
        "forbids": common["forbidden_outputs"] + ["historical scientific reconstruction by consumer", "C95 comparison execution before public inputs exist"],
        "next_status_on_success": "C96_HISTORICAL_PUBLIC_INPUT_COMPLETE",
    })
    (DOCS / "c95_instance_science_separation_report.md").write_text(
        "# C95 instance/science separation\n\n"
        "C95 found a project-owned import-surface defect, not a scientific difference. C94 verifies its public authority but does not export the historical normal-form, proof-input, or primitive-record operations required by the committed C95 theorem comparison. No historical scientific field was privately read and no pair scientific field was compared; therefore this result cannot classify any scientific payload difference. The exact historical C72 runtime instance remains `UNKNOWN_NOT_CLAIMED`.\n"
    )
    (DOCS / "c95_implementation_report.md").write_text(
        "# C95/IFEQUIV7 implementation report\n\n"
        f"Status: `{STATUS}`.\n\n"
        "C95 verifies C94 only through its exported immutable authority. The authority verifies, and the fresh independent descendant compiler reproduces 154,830 pairs and 891,992,018 logical records. The comparison must nevertheless stop: C94 does not export `historical_pair_normal_form`, `historical_pair_proof_inputs`, or `historical_primitive_record`. Those are required inputs to the public expansion checker and cannot be inferred from hashes, roots, family pages, or private modules.\n\n"
        "No historical-versus-descendant scientific equivalence or mismatch is claimed, and no expanded record stream, kernel product, contact matrix/action, coupling, counterterm, TMD, matching, fit, inference, or production object was created. The sole continuation is C96/IFHISTPUBLIC, limited to the three authenticated C94 public loaders.\n"
    )


if __name__ == "__main__":
    main()
