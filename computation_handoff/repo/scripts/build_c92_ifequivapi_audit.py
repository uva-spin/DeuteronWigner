"""Emit the C92 Route-C payload-incompleteness audit artifacts."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifequivapi.core import (
    ENVIRONMENT, HISTORICAL_C82, STATUS, UNKNOWN_C72, audit_existing_c90_payload, select_packaging_route,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
CONTRACT = DOCS / "c91_c92_ifequivapi_import_contract.json"


def write(name: str, value: object) -> None:
    def plain(item):
        if hasattr(item, "items"): return {key: plain(child) for key, child in item.items()}
        if isinstance(item, tuple): return [plain(child) for child in item]
        if isinstance(item, list): return [plain(child) for child in item]
        return item
    (DOCS / name).write_text(json.dumps(plain(value), sort_keys=True, indent=2) + "\n")


def main() -> None:
    audit, route = audit_existing_c90_payload(), select_packaging_route()
    contract_hash = sha256(CONTRACT.read_bytes()).hexdigest()
    common = {"status": STATUS, "route": route["route"], "reason": route["reason"], "historical_C82": HISTORICAL_C82,
              "environment": ENVIRONMENT, "historical_C72_runtime_instance": UNKNOWN_C72,
              "no_scientific_reconstruction": True, "expanded_records": False, "kernel_product": False}
    write("c92_derivation_authority_manifest.json", {"sole_continuation_contract": str(CONTRACT.relative_to(ROOT)), "contract_sha256": contract_hash, "C90_public_aggregate": audit["historical_aggregate"], "C90_runtime_payloads": len(audit["payloads"]), "C91_descendant_compilation": "preserved unchanged"})
    write("c92_input_fidelity_audit.json", {**common, "historical_public_authority_verified": audit["historical_public_aggregate_verified"], "payload_audit": audit})
    write("c92_descendant_qualification.json", {"C90_C82_FACTORIZED_SEMANTIC_ATTESTATION_READY": "C90_SCIENCE_COMPLETE_PUBLIC_PAIR_IMPORT_INCOMPLETE", "C91_IFEQUIV6_PUBLIC_EQUIVALENCE_INCOMPLETE": "descendant compiler remains complete; comparison remains blocked by missing persisted historical objects", "retraction": False})
    write("c92_input_freeze.json", {"status": "C92_C90_SCIENTIFIC_INPUTS_FROZEN_COMPLETE", "C90_aggregate": audit["historical_aggregate"], "payload_hashes": [{"path": item["path"], "sha256": item["sha256"]} for item in audit["payloads"]], "scientific_fields_modified": 0})
    write("c92_c90_payload_inventory.json", {"payloads": audit["payloads"], "canonical_ledger_fields": audit["canonical_ledger_fields"], "missing_pair_fields": audit["missing_pair_fields"], "missing_package_objects": audit["missing_package_objects"], "all_passes_agree": audit["all_runtime_passes_byte_identical"]})
    write("c92_c90_public_surface_gap_matrix.json", {"persisted_pair_attestation_root": True, "pair_enumeration": "CAN_BE_DERIVED_FROM_LEDGER_BUT_INSUFFICIENT", "normal_form_content": False, "primitive_family_records": False, "theorem_specification": False, "proof_checker_input_schema": False, "legal_no_recomputation_facade": False})
    write("c92_packaging_route_decision.json", dict(route))
    for name, subject in (("c92_pair_attestation_schema.json", "HistoricalC90PairAttestation"), ("c92_pair_attestation_schema_validation.json", "schema validation"), ("c92_pair_enumeration_manifest.json", "pair enumeration"), ("c92_pair_enumeration_validation.json", "pair enumeration validation"), ("c92_pagination_contract.json", "pagination"), ("c92_pagination_validation.json", "pagination validation"), ("c92_pair_inclusion_proof_contract.json", "pair inclusion"), ("c92_pair_inclusion_proof_validation.json", "pair inclusion validation"), ("c92_normal_form_public_contract.json", "normal-form public access"), ("c92_normal_form_public_validation.json", "normal-form validation"), ("c92_primitive_family_manifest.json", "primitive families"), ("c92_primitive_public_access_validation.json", "primitive access validation"), ("c92_expansion_theorem_public_spec.json", "theorem specification"), ("c92_expansion_theorem_spec_validation.json", "theorem specification validation"), ("c92_expansion_checker_contract.json", "proof checker"), ("c92_expansion_checker_validation.json", "proof checker validation"), ("c92_no_recomputation_contract.json", "no-recomputation loader"), ("c92_no_recomputation_validation.json", "no-recomputation validation"), ("c92_safe_loading_contract.json", "safe public loading"), ("c92_safe_loading_validation.json", "safe loading validation"), ("c92_api_contract.json", "public API"), ("c92_api_validation.json", "public API validation"), ("c92_runtime_inventory.json", "C92 runtime"), ("c92_exhaustive_c90_public_equivalence.json", "exhaustive C90-to-C92 equivalence"), ("c92_c91_blocker_supersession_report.json", "C91 blocker supersession"), ("c92_c93_ifequiv7_preflight.json", "C93 preflight"), ("c92_deterministic_reconstruction_report.json", "deterministic reconstruction"), ("c92_resource_and_scaling_report.json", "resource scaling"), ("c92_isolation_report.json", "mutation/isolation"), ("c92_regression_report.json", "regression")):
        write(name, {"subject": subject, **common, "result": "NOT_CREATED_OR_NOT_EXECUTED_BECAUSE_REQUIRED_C90_PERSISTED_OBJECTS_ARE_ABSENT"})
    write("c92_c93_ifc90payload_import_contract.json", {"selected_status": STATUS, "objective": "recover only the missing C90-owned authenticated normal-form content, primitive-family records, theorem specification, and proof-checker input schema", "forbids": ["C77/C78/C82 scientific reconstruction", "expanded records", "kernel product", "contact matrix"], "must_preserve": ["C90 aggregate root", "C90 ledger entries", "C91 descendant ledger"]})
    write("c92_readiness_report.json", {**common, "selected_next": "C93/IFC90PAYLOAD", "C91_blocker_superseded": False, "positive_status_issued": False})
    (DOCS / "c92_implementation_report.md").write_text("# C92/IFEQUIVAPI\n\nC92 audited the actual persisted C90 runtime before adding any API. The four deterministic C90 runtime ledgers are byte-identical compact semantic-root ledgers and the public aggregate verifies. However, their entries persist only pair identity, normal-form root, primitive-root bundle, summary, and proof result. They do not persist normal-form content, primitive-family records, expression-rule roots, theorem specification, or proof-checker inputs.\n\nC92 selects Route C: `C92_IFEQUIVAPI_C90_PAYLOAD_INCOMPLETE`. Reconstructing those omitted objects through C77/C78/C82/C89/C90 builders would violate the sole continuation contract. No public facade, snapshot, C91 supersession, C93 preflight, or scientific-equivalence claim was created. The next package is C93/IFC90PAYLOAD.\n")


if __name__ == "__main__":
    main()
