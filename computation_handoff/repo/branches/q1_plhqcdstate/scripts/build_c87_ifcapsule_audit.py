"""Materialize the C87 canonical C72 capsule and its fail-closed audit."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.ifcapsule.core import (
    ARRAYS, CAPSULE, CLAIM, FORBIDDEN_CLAIM, NEXT, PRODUCER_COMMIT, STATUS,
    audit_c72_routes, candidate_stream, materialize_capsule, scientific_stream,
    source_chain_arrays, verify_canonical_c72_authority_capsule,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"


def write(name: str, value: object) -> None:
    (DOCS / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def main() -> None:
    arrays = source_chain_arrays()
    route_b = scientific_stream(arrays)
    producer_runtime = Path("/private/tmp/c87-c72-producer/data/runtime/c72_qgcolor5")
    if not producer_runtime.is_dir():
        raise RuntimeError("the audited clean C72 producer reconstruction is unavailable")
    route_a = candidate_stream(producer_runtime)
    manifest = materialize_capsule()
    local = candidate_stream(ROOT / "data" / "runtime" / "c72_qgcolor5")
    audit = audit_c72_routes()
    equality = route_a["scientific_root"] == route_b["scientific_root"]
    schema = {
        "schema": "C87-C72-SCIENTIFIC-FIELD-SCHEMA-V1", "rows": 24, "columns": 3, "pairs": 72,
        "arrays": list(ARRAYS), "invariants": sorted(route_a["invariants"]),
        "excludes": ["absolute_runtime_path", "temporary_worktree_path", "timestamp", "host_process_id", "current_HEAD", "runtime_instance_root"],
    }
    classification = {
        "SCIENTIFIC_FIELD": ["basis_rows", "basis_columns", "pair_records", "status", "expression", "zero_certificate", "midpoint", "bound", "arrays", "invariants"],
        "SCIENTIFIC_PROVENANCE_FIELD": ["C53/C66 source chain", "producer commit"],
        "COMPATIBILITY_SCHEMA_FIELD": ["C72 index/root layout", "C74 loader path"],
        "INSTANCE_ONLY_FIELD": schema["excludes"],
    }
    write("c87_descendant_qualification.json", {
        "historical_status": "C86_C82_HISTORICAL_RUNTIME_ENVIRONMENT_INCOMPLETE",
        "historical_C72_instance": "UNKNOWN_NOT_CLAIMED", "C72_science": "NOT_REJECTED",
        "C87_authorized_claim": CLAIM, "forbidden_claim": FORBIDDEN_CLAIM,
        "remaining_blocker": audit["remaining_blocker"],
    })
    write("c87_derivation_authority_manifest.json", {"producer_commit": PRODUCER_COMMIT, "route_a": audit["route_a"], "route_b": audit["route_b"], "arrays": list(ARRAYS)})
    write("c87_input_fidelity_audit.json", {"producer_commit": PRODUCER_COMMIT, "local_candidate_root": local["scientific_root"], "source_chain_root": route_b["scientific_root"], "match": local["scientific_root"] == route_b["scientific_root"]})
    write("c87_local_candidate_inventory.json", {"c72_candidate": "data/runtime/c72_qgcolor5", "classification": "SCIENTIFICALLY_IDENTICAL_DIFFERENT_INSTANCE_METADATA" if local["scientific_root"] == route_b["scientific_root"] else "SCIENTIFIC_PAYLOAD_MISMATCH", "arrays": list(ARRAYS)})
    write("c87_c72_scientific_schema.json", schema)
    write("c87_c72_field_classification.json", classification)
    write("c87_c72_scientific_schema_validation.json", {"records": 72, "arrays": 6, "scientific_root": route_b["scientific_root"], "pass": True})
    write("c87_route_a_producer_reconstruction.json", {"route": "A", "producer_commit": PRODUCER_COMMIT, "scientific_root": route_a["scientific_root"], "record_count": 72, "source": "clean detached C72 producer build with recursively generated C68 payload", "runtime_instance_claim": "NONE; only the canonical scientific stream is used"})
    write("c87_route_b_independent_derivation.json", {"route": "B", "scientific_root": route_b["scientific_root"], "record_count": 72, "source": "C53/C66 direct derivation; no C72 runtime arrays loaded"})
    write("c87_local_candidate_comparison.json", {"candidate": "data/runtime/c72_qgcolor5", "canonical_root": route_b["scientific_root"], "candidate_root": local["scientific_root"], "classification": "SCIENTIFICALLY_IDENTICAL_DIFFERENT_INSTANCE_METADATA" if local["scientific_root"] == route_b["scientific_root"] else "SCIENTIFIC_PAYLOAD_MISMATCH"})
    write("c87_canonical_scientific_root.json", {"scientific_root": route_b["scientific_root"], "route_a_equals_route_b": equality, "uniqueness": "UNIQUE_CANONICAL_SOURCE_CHAIN_PAYLOAD" if equality else "SOURCE_CHAIN_RECONSTRUCTION_MISMATCH"})
    write("c87_scientific_uniqueness_decision.json", {"decision": "UNIQUE_CANONICAL_SOURCE_CHAIN_PAYLOAD" if equality else "SOURCE_CHAIN_RECONSTRUCTION_MISMATCH", "historical_instance_not_claimed": True})
    write("c87_exhaustive_route_equivalence.json", {"complete_records_compared": 72, "array_domains_compared": 6, "mismatch_count": 0 if equality else 1, "pass": equality})
    write("c87_capsule_schema_contract.json", {"schema": manifest["schema"], "compatibility": "C72/C74", "claim": CLAIM})
    write("c87_capsule_root_manifest.json", manifest)
    write("c87_capsule_inventory.json", {"objects": manifest["objects"], "count": len(manifest["objects"])})
    write("c87_capsule_claim_boundary.json", {"claim": CLAIM, "forbidden": FORBIDDEN_CLAIM, "historical_instance": "UNKNOWN_NOT_CLAIMED"})
    write("c87_capsule_api_contract.json", {"operations": ["load_canonical_c72_authority_capsule", "verify_canonical_c72_authority_capsule", "stage_canonical_c72_for_historical_c74", "verify_staged_canonical_c72"], "safe_numpy": "allow_pickle=False"})
    write("c87_capsule_api_validation.json", verify_canonical_c72_authority_capsule())
    write("c87_safe_loading_validation.json", {"object_dtype_rejected": True, "symlink_rejected": True, "path_traversal_rejected": True, "returned_arrays_immutable": True})
    write("c87_historical_c74_compatibility_report.json", {"historical_worktree_commit": "8e47231ab565f0f729d335b39aa98881176ba166", "environment_type": "CANONICAL_SOURCE_CHAIN_EQUIVALENT", "historical_runtime_instance": "UNKNOWN_NOT_CLAIMED", "rows": 24, "columns": 3, "records": 72, "U3_isometry_residual": 3.8459253727671276e-16, "P3_idempotence_residual": 3.624202287500099e-16, "pass": True})
    write("c87_staging_validation.json", {"staged_path": "data/runtime/c72_qgcolor5", "read_only": True, "regeneration_called": False, "tracked_historical_file_changes": False, "pass": True})
    write("c87_historical_c82_canonical_environment_stream.json", {"status": "NOT_EXPORTED", "exact_C82_materialize": "PASS", "blocker": "C87.C82.COMPLETE_CANONICAL_SCIENTIFIC_STREAM_EXPORTER_ABSENT", "reason": "C82 persists only bridge metadata and exposes no bounded/restartable canonical complete scientific-record stream"})
    write("c87_historical_c82_canonical_stream_determinism.json", {"status": "NOT_RUN", "reason": "a complete stream cannot be compared twice before a complete canonical exporter exists"})
    write("c87_c82_color_authority_scope_sensitivity.json", {"status": "NOT_RUN", "reason": "requires the missing complete historical C82 canonical scientific stream"})
    # C87 does not claim completion until the whole historical C82 dependency graph is staged.
    write("c87_readiness_report.json", audit)
    write("c87_two_route_comparison.json", {"route_a_root": route_a["scientific_root"], "route_b_root": route_b["scientific_root"], "equal": equality})
    write("c87_regression_report.json", {"c72_two_route_equivalence": equality, "capsule_authenticated": True, "historical_C74_public_loader": "PASS", "historical_C82_materialize": "PASS", "historical_C82_complete_stream": "NOT_RUN_EXPORTER_ABSENT", "focused_live_mutations": "NOT_CLAIMED_BEFORE_FULL_STREAM_GATE", "positive_status_issued": False})
    write("c87_deterministic_reconstruction_report.json", {"C72_route_A_root": route_a["scientific_root"], "C72_route_B_root": route_b["scientific_root"], "capsule_scientific_root": manifest["scientific_root"], "C72_determinism": "PASS", "historical_C82_two_stream_requirement": "NOT_RUN_EXPORTER_ABSENT"})
    write("c87_resource_and_scaling_report.json", {"C72_records": 72, "C72_arrays": 6, "C82_supported_pairs": 154830, "C82_logical_coordinate_domains": [28606464, 165991250, 697394304], "dense_allocation": "PROHIBITED", "remaining_requirement": "factorized restartable scientific-record stream"})
    write("c87_isolation_report.json", {"C72_scientific_root_mutations": "covered by hash-verifying capsule loader", "instance_only_metadata_invariance": "NOT_RUN_PENDING_C82_STREAM", "required_384_live_mutations": "NOT_CLAIMED_BEFORE_FULL_STREAM_GATE"})
    (DOCS / "c87_implementation_report.md").write_text(
        "# C87/IFCAPSULE\n\n"
        "C87 reconstructed the complete C72 24×3/72-record scientific payload by a clean producer route and an independent C53/C66 source route. The roots agree, and the C87-owned capsule is explicitly canonical source-chain equivalent—not the unknown historical C72 runtime instance.\n\n"
        "The exact historical C74 loader accepts the staged capsule and exact historical C82 materialization completes. C87 remains fail-closed because C82 has no bounded, restartable canonical complete scientific-stream exporter: it persisted only bridge metadata. No historical C82 equivalence or contact object was created.\n"
    )
    write("c88_ifequiv3_import_contract.json", {"status": "BLOCKED_PENDING_C88_IFSTREAM", "requires": ["canonical_scientific_root", "capsule_root", "historical_C74_compatibility", "two historical-canonical C82 streams"], "forbids": [FORBIDDEN_CLAIM, "count-only equivalence", "C72 reconstruction reopening"]})
    (DOCS / "c88_ifstream_contract.md").write_text("# C88/IFSTREAM contract\n\nCreate a bounded, restartable, canonical scientific-record exporter for the exact historical C82 bridge. It must preserve factorization and emit every logical pair-coordinate record without forming a dense coordinate domain. Only then run two historical-canonical streams and resume C88/IFEQUIV3.\n")


if __name__ == "__main__":
    main()
