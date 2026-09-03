#!/usr/bin/env python3
"""Materialize the C96 fail-closed proof-input persistence audit."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from deuteron_wigner.bridge.ifhistpublic import STATUS, audit_authenticated_proof_input_payload


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
BASELINE = "8e9be179236507171d670bbcc9e540d018260fa3"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
UNKNOWN = "UNKNOWN_NOT_CLAIMED"
RELATION = "RECOVERED_CONTENT_PREIMAGE_OF_FROZEN_C90_AUTHORITY"
BLOCKER = "C93_PROOF_INPUTS_ARE_ONLY_PRIVATE_ROOT_BASED_COMPOSITIONS_OF_PAIR_ATTESTATION_AND_NORMAL_FORM"


def plain(value: Any) -> Any:
    if isinstance(value, dict) or hasattr(value, "items"):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def write(name: str, body: Any) -> None:
    (DOCS / name).write_text(json.dumps(plain(body), indent=2, sort_keys=True) + "\n")


def hash_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    audit = plain(audit_authenticated_proof_input_payload())
    contract_path = DOCS / "c96_ifhistpublic_import_contract.json"
    contract = json.loads(contract_path.read_text())
    common = {
        "package": "C96/IFHISTPUBLIC",
        "baseline": BASELINE,
        "contract": {"path": str(contract_path.relative_to(ROOT)), "sha256": hash_file(contract_path), "schema": contract["contract"]},
        "historical_C90_completion": "ac622ab358b83f090717d7e7fa179b58f18f526d",
        "historical_C82_completion": "8e47231ab565f0f729d335b39aa98881176ba166",
        "historical_environment": ENVIRONMENT,
        "historical_C72_runtime_instance": UNKNOWN,
        "scientific_relation": RELATION,
        "original_c90_runtime_payload": "NOT_CLAIMED",
        "root_semantics": "FACTORIZED_SEMANTIC_PROGRAM_ROOT",
        "C94_package_root": audit["C94_package_root"],
        "C93_capsule_root": audit["C93_capsule_root"],
        "C90_aggregate": audit["C90_aggregate"],
        "forbidden_outputs": contract["forbids"],
    }
    write("c96_derivation_authority_manifest.json", {
        **common,
        "source_files": [
            "data/runtime/c93_ifc90payload/capsule/manifest.json",
            "data/runtime/c93_ifc90payload/capsule/pair_attestations.jsonl.gz",
            "data/runtime/c93_ifc90payload/capsule/normal_forms.jsonl.gz",
            "src/deuteron_wigner/bridge/ifc90payload/core.py",
            "src/deuteron_wigner/bridge/ifequivapi2/core.py",
        ],
        "source_access": "verified C94 authority plus C94-referenced C93 payload bytes; no C93 recovery call",
    })
    write("c96_input_fidelity_audit.json", {**common, "status": STATUS, "audit": audit, "result": "FAIL_CLOSED_BEFORE_PUBLIC_LOADER_ADAPTER"})
    write("c96_descendant_qualification.json", {
        "C94_C93_PUBLIC_EQUIVALENCE_IMPORT_READY": "C94_GENERAL_PUBLIC_AUTHORITY_READY_BUT_THREE_THEOREM_INPUT_LOADERS_ABSENT",
        "C95_IFEQUIV7_HISTORICAL_PUBLIC_INPUT_INCOMPLETE": "descendant domain reproduced; comparison remains blocked by historical theorem-input retrieval.",
        "C96_result": STATUS,
        "scientific_content_changed": False,
    })
    write("c96_claim_boundary.json", {**common, "claim": "project-owned persisted-proof-input audit only", "does_not_claim": ["historical-versus-descendant equivalence", "scientific mismatch", "original C90 runtime recovery", "expanded stream", "coefficient package", "kernel product", "contact matrix/action"]})
    write("c96_input_freeze.json", {**common, "status": "C96_HISTORICAL_PUBLIC_AUTHORITY_FROZEN_COMPLETE", "pair_bindings": audit["pair_attestations"]["records"], "normal_form_records": audit["normal_forms"]["records"], "proof_input_records": 0, "frozen_before_adapter": True})
    write("c96_required_loader_payload_audit.json", {
        **common,
        "loaders": [
            {"method": "historical_pair_normal_form(pair_id, resolution)", "persisted_source": "normal_forms.jsonl.gz", "record_count": audit["normal_forms"]["records"], "source_schema": audit["normal_forms"]["top_level_schemas"], "route_if_proof_input_gate_closes": "B: direct C96 location index", "content_present": True},
            {"method": "historical_pair_proof_inputs(pair_id, resolution)", "persisted_source": None, "record_count": 0, "content_present": False, "forbidden_surrogate": "ifc90payload.recovered_pair_proof_inputs joins pair attestation and normal form by normal_form_root", "result": "UNAVAILABLE_WITHOUT_FORBIDDEN_PRIVATE_ROOT_BASED_COMPOSITION"},
            {"method": "historical_primitive_record(family_id, record_id)", "persisted_source": "primitive_families.json", "content_present": True, "route_if_proof_input_gate_closes": "B: direct C96 family-record location index"},
        ],
    })
    write("c96_public_surface_gap_matrix.json", {
        "historical_pair_normal_form": {"C93_content": "present", "C94_export": "absent", "C96_status": "not published because exact three-loader package cannot close"},
        "historical_pair_proof_inputs": {"C93_independent_persisted_content": "absent", "C94_export": "absent", "C96_status": "blocking"},
        "historical_primitive_record": {"C93_content": "present", "C94_export": "absent", "C96_status": "not published because exact three-loader package cannot close"},
    })
    write("c96_loader_route_decision.json", {"status": STATUS, "normal_form": "B_DEFERRED_DIRECT_INDEX_OVER_AUTHENTICATED_BYTES", "proof_inputs": "C_UNAVAILABLE_SEPARATE_PERSISTED_RECORD_ABSENT", "primitive_record": "B_DEFERRED_DIRECT_INDEX_OVER_AUTHENTICATED_BYTES", "selected_next": "C97/IFPROOFINPUT"})
    blocked = {"status": "NOT_PUBLISHED_PROOF_INPUT_PERSISTENCE_BLOCKER", "blocker": BLOCKER, "no_loader_output_constructed": True, "scientific_reconstruction": False}
    for name in (
        "c96_package_root_manifest.json", "c96_runtime_inventory.json", "c96_package_root_validation.json",
        "c96_historical_pair_normal_form_contract.json", "c96_historical_pair_normal_form_validation.json",
        "c96_historical_pair_proof_inputs_contract.json", "c96_historical_pair_proof_inputs_validation.json",
        "c96_historical_primitive_record_contract.json", "c96_historical_primitive_record_validation.json",
        "c96_loader_inclusion_proof_contract.json", "c96_loader_inclusion_proof_validation.json",
        "c96_no_recomputation_contract.json", "c96_no_recomputation_validation.json",
        "c96_safe_loading_contract.json", "c96_safe_loading_validation.json",
        "c96_exhaustive_normal_form_loader_regression.json", "c96_exhaustive_proof_input_checker_regression.json",
        "c96_exhaustive_primitive_direct_lookup_regression.json", "c96_c97_ifequiv8_preflight.json",
        "c96_deterministic_reconstruction_report.json", "c96_restart_validation.json", "c96_resource_and_scaling_report.json",
        "c96_isolation_report.json", "c96_regression_report.json",
    ):
        write(name, {**common, **blocked})
    write("c96_c95_blocker_supersession_report.json", {
        "status": "NOT_SUPERSEDED",
        "C95_status": "C95_IFEQUIV7_HISTORICAL_PUBLIC_INPUT_INCOMPLETE",
        "reason": "The exact persisted proof-input object required for the third C95 loader is absent; no private root-based composition may be promoted to public authority.",
        "comparison_retroactively_created": False,
    })
    write("c96_readiness_report.json", {**common, "status": STATUS, "ready": False, "next": "C97/IFPROOFINPUT", "exact_missing_object": "independent authenticated historical pair-proof-input record domain", "C95_blocker_superseded": False})
    write("c97_ifproofinput_import_contract.json", {
        "contract": "C96-C97-IFPROOFINPUT-V1",
        "precondition": {"C96_status": STATUS, "C94_package_root": audit["C94_package_root"], "C93_capsule_root": audit["C93_capsule_root"]},
        "objective": "Recover or locate only the exact persisted historical proof-input object domain; do not derive it by joining a pair attestation to a normal-form root or proof result.",
        "forbids": contract["forbids"] + ["private C93 recovered_pair_proof_inputs", "root-based proof-input composition", "historical-versus-descendant comparison"],
        "success_status": "C97_HISTORICAL_PROOF_INPUT_PUBLIC_PAYLOAD_READY",
    })
    (DOCS / "c96_implementation_report.md").write_text(
        "# C96/IFHISTPUBLIC implementation report\n\n"
        f"Status: `{STATUS}`.\n\n"
        "C96 verified the C94-to-C93-to-C90 authority chain and exhaustively censused the two authenticated JSONL source domains: 154,830 pair attestations and 154,830 normal-form records. Neither source contains a terminal `proof_input` or `proof_inputs` record. The only available C93 proof-input routine joins a pair attestation's `normal_form_root` and proof result to a normal-form record. C96 is explicitly forbidden from promoting that private root-based composition as a public persisted object.\n\n"
        "No C96 three-loader adapter, public theorem-input method, comparison, expanded record stream, kernel product, contact matrix/action, or physical result was created. The exact next package is C97/IFPROOFINPUT, limited to locating or recovering the missing persisted proof-input domain without root/proof-result reconstruction.\n"
    )


if __name__ == "__main__":
    main()
