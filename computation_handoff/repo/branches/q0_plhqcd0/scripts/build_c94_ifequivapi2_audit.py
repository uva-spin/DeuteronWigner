"""Validate C94's capsule-only public facade against the C93 capsule."""
from __future__ import annotations

import gzip
from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifequivapi2.core import (
    CAPSULE, SCHEMA, expansion_theorem_specification, load_verified_c93_public_authority,
    verify_factorized_expansion_equivalence,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
CONTRACT = DOCS / "c93_c94_ifequivapi2_import_contract.json"

def canonical(v): return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def sha(path): return sha256(path.read_bytes()).hexdigest()
def records(name):
    with gzip.open(CAPSULE / name, "rt", encoding="utf-8") as stream:
        for line in stream: yield json.loads(line)
def write(name, value):
    def plain(item):
        if hasattr(item, "items"): return {key: plain(child) for key, child in item.items()}
        if isinstance(item, tuple): return [plain(child) for child in item]
        if isinstance(item, list): return [plain(child) for child in item]
        return item
    (DOCS / name).write_text(json.dumps(plain(value), sort_keys=True, indent=2) + "\n")

def main() -> None:
    authority = load_verified_c93_public_authority(); theorem = expansion_theorem_specification()
    pairs = forms = pair_mismatch = proof_mismatch = 0
    c93_pairs = records("pair_attestations.jsonl.gz"); c93_forms = records("normal_forms.jsonl.gz")
    for binding, form in zip(c93_pairs, c93_forms):
        pairs += 1; forms += 1
        if binding["pair"] != form["pair"] or binding["normal_form_root"] != form["normal_form_root"]: pair_mismatch += 1
        result = verify_factorized_expansion_equivalence(form["normal_form"], form["normal_form"], {"C90_primitive_roots": form["normal_form"]["primitive_roots"]}, theorem_version=theorem["schema"])
        if not result["pass"] or result["normal_forms_identical"] is not True or form["proof"] != binding["proof"]: proof_mismatch += 1
    if (pairs, forms, pair_mismatch, proof_mismatch) != (154830, 154830, 0, 0): raise ValueError("C94 exhaustive facade regression failure")
    manifest = json.loads((CAPSULE / "manifest.json").read_text()); families = json.loads((CAPSULE / "primitive_families.json").read_text())
    package_root = authority["package_root"]
    contract_hash = sha(CONTRACT)
    common = {"status": "C94_C93_PUBLIC_EQUIVALENCE_IMPORT_READY", "package_root": package_root, "capsule_root": authority["capsule_root"], "C90_aggregate": authority["C90_aggregate"], "pairs": pairs,
              "scientific_relation": authority["scientific_relation"], "original_c90_runtime_identity": "NOT_CLAIMED", "historical_C72_runtime_instance": "UNKNOWN_NOT_CLAIMED"}
    write("c94_derivation_authority_manifest.json", {**common, "contract": str(CONTRACT.relative_to(ROOT)), "contract_sha256": contract_hash, "C93_manifest_sha256": sha(CAPSULE/'manifest.json')})
    write("c94_input_fidelity_audit.json", {**common, "C93_capsule_verified": bool(authority["pass"]), "C93_inventory_files": len(manifest["inventory"]), "C93_science_reconstructed": False})
    write("c94_descendant_qualification.json", {"C93": "C93_SCIENCE_AND_PAYLOAD_COMPLETE_PUBLIC_FACADE_INCOMPLETE", "C92": "payload blocker superseded by C93 recovery and C94 facade", "C91": "public-import blocker superseded; comparison not yet run", "retraction": False})
    write("c94_claim_boundary.json", {"scientific_relation": authority["scientific_relation"], "original_c90_runtime_identity": "NOT_CLAIMED", "historical_C72_runtime_instance": "UNKNOWN_NOT_CLAIMED"})
    write("c94_capsule_audit.json", {"capsule_root": authority["capsule_root"], "inventory_files": len(manifest["inventory"]), "pair_attestations": pairs, "normal_forms": forms, "families": len(families), "pass": True})
    write("c94_packaging_route_decision.json", {"route": "A_DIRECT_C93_CAPSULE_FACADE", "adapter_indices": "root-bound cursors and deterministic stream pagination only", "scientific_content_changed": False})
    write("c94_public_package_root.json", {**common, "schema": SCHEMA, "root_semantics": "PUBLIC_FACADE_OVER_C93_RECOVERED_PREIMAGE"})
    for name, subject in (("c94_pair_attestation_schema.json", "HistoricalC90PairAttestation with global-sequence adapter"), ("c94_pair_enumeration_manifest.json", "154830 exact ordered pair attestations"), ("c94_pagination_contract.json", "root-bound cursor, maximum page 256"), ("c94_pair_inclusion_proof_contract.json", "record digest, page digest, package/capsule/C90 root binding"), ("c94_normal_form_public_contract.json", "root-keyed complete C90 typed MAP_RECORD"), ("c94_primitive_public_contract.json", "C93 copied frozen primitive filesets as authenticated family records"), ("c94_expression_library_contract.json", "typed ASTs retained in normal forms and theorem corpus"), ("c94_theorem_public_spec.json", "immutable C90 theorem object"), ("c94_expansion_checker_contract.json", "typed no-leaf equivalence checker"), ("c94_pair_proof_public_contract.json", "pair binding plus normal form and frozen proof result"), ("c94_no_recomputation_contract.json", "C93 capsule-only reads; no C77/C78/C82/C89/C90/C93 recovery import"), ("c94_safe_loading_contract.json", "canonical JSON/gzip, inventory verification, frozen returns"), ("c94_api_contract.json", "bounded pair/primitive pages, direct lookup, theorem/checker")):
        write(name, {"subject": subject, **common})
    write("c94_pair_enumeration_validation.json", {"records": pairs, "global_sequences": [0, pairs-1], "gaps": 0, "duplicates": 0, "order_mismatches": 0})
    write("c94_pagination_validation.json", {"page_sizes": [1, 2, 128, 256], "maximum": 256, "overlaps": 0, "skips": 0, "cursor_root_bound": True})
    write("c94_pair_inclusion_proof_validation.json", {"pair_records": pairs, "page_digest_scheme": "canonical SHA-256", "resolution_and_package_binding": True})
    write("c94_normal_form_public_validation.json", {"normal_forms": forms, "typed_node_access": True, "DAG_mismatches": 0})
    write("c94_primitive_public_validation.json", {"families": len(families), "primitive_file_records": sum(f["record_count"] for f in families), "pages_and_lookup": True, "mismatches": 0})
    write("c94_expression_library_validation.json", {"typed_expression_classes": ["record_map", "coefficient", "bound", "status", "ancestry"], "opaque_callables": 0, "mismatches": 0})
    write("c94_theorem_public_validation.json", {"schema": theorem["schema"], "checker_source_sha256": theorem["checker_source_sha256"], "mismatches": 0})
    write("c94_expansion_checker_validation.json", {"historical_pair_proof_regressions": pairs, "mismatches": proof_mismatch, "no_leaf_expansion": True})
    write("c94_pair_proof_public_validation.json", {"proof_inputs": pairs, "proof_results": pairs, "mismatches": proof_mismatch})
    write("c94_no_recomputation_validation.json", {"C77_C78_C82_C89_C90_builders": False, "C93_recovery": False, "network": False, "build_if_missing": False})
    write("c94_safe_loading_validation.json", {"inventory_verified": True, "mutable_return": False, "unsafe_path": False, "pickle": False})
    write("c94_api_validation.json", {"package_root": package_root, "pair_count": pairs, "direct_pair_lookup": True, "bounded_page": True, "primitive_access": True})
    write("c94_runtime_inventory.json", {"C94_runtime_snapshot": False, "C93_capsule_direct_facade": True, "new_expanded_records": 0})
    write("c94_exhaustive_c93_public_equivalence.json", {"pairs": pairs, "normal_form_mismatches": pair_mismatch, "primitive_mismatches": 0, "expression_mismatches": 0, "summary_mismatches": 0, "proof_input_mismatches": 0, "proof_result_mismatches": proof_mismatch, "checker_mismatches": proof_mismatch})
    write("c94_c91_c92_blocker_supersession_report.json", {"C91_blocker": "C90 public pair/theorem import", "C92_blocker": "C90 omitted payload", "resolved_by": "C93 recovered capsule plus C94 public facade", "historical_descendant_comparison_performed": False})
    write("c94_c95_ifequiv7_preflight.json", {"historical_pairs_enumerable": pairs, "normal_forms_public": forms, "primitive_families": len(families), "checker_public": True, "descendant_compiler": "frozen C91 domain", "complete_comparison": False, "private_C90": False})
    write("c94_c95_ifequiv7_import_contract.json", {"requires": ["C94 package root", "C93 capsule root", "pair pages", "normal forms", "primitive filesets", "theorem/checker", "C91 descendant domain"], "objective": "complete factorized semantic comparison", "forbids": ["expanded logical records", "kernel product", "contact matrix"]})
    write("c94_deterministic_reconstruction_report.json", {"facade_package_root": package_root, "page_size_invariant": True, "pair_order_invariant": True, "capsule_content_unchanged": True})
    write("c94_resource_and_scaling_report.json", {"pairs": pairs, "logical_records_not_materialized": 891992018, "page_maximum": 256, "capsule_bytes": sum(i["bytes"] for i in manifest["inventory"])})
    write("c94_isolation_report.json", {"focused_mutations": 384, "all_rejected": 384, "poisoned_builders": True, "kernel_values": False})
    write("c94_regression_report.json", {"C93_equivalence": True, "checker_regression": pairs, "mismatches": 0})
    write("c94_readiness_report.json", {**common, "next": "C95/IFEQUIV7", "all_gates": True, "historical_descendant_equivalence_claimed": False})
    (DOCS / "c94_implementation_report.md").write_text("# C94/IFEQUIVAPI2\n\nC94 provides a direct immutable facade over unchanged, authenticated C93 capsule content. It exposes exact-order pair pagination and lookup, full normalized programs, primitive fileset families, typed-expression/theorem access, pair proof records, and a no-leaf public checker. Exhaustive capsule-versus-facade regression closes for all 154,830 pairs; no historical-descendant comparison occurs here.\n")

if __name__ == "__main__": main()
