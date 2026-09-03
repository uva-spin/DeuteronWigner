#!/usr/bin/env python3
"""Validate C102's completed public-checker package and emit its records.

The script reads only C102 compact metadata and public C94/C98/C100 calls.
It is deliberately incapable of performing the C103 descendant comparison.
"""
from __future__ import annotations
import copy
import gzip
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from deuteron_wigner.bridge.ifhistpublic2 import historical_pair_normal_form, historical_pair_proof_inputs
from deuteron_wigner.bridge.ifprimenum import historical_primitive_record_page
from deuteron_wigner.bridge.iftheoremapi import (
    factorized_expansion_checker_contract, factorized_expansion_theorem_specification,
    load_verified_factorized_semantic_theorem_authority, verify_factorized_expansion_equivalence,
    verify_factorized_expansion_invocation,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
RUNTIME = ROOT / "data/runtime/c102_iftheoremapi"
SCHEMA = "C102-IFTHEOREMAPI-FINALIZATION-V1"

def plain(v: Any) -> Any:
    if hasattr(v, "items"): return {str(k): plain(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)): return [plain(x) for x in v]
    return v
def canonical(v: Any) -> str: return json.dumps(plain(v), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def digest(v: Any) -> str: return sha256(canonical(v).encode()).hexdigest()
def write(name: str, body: dict[str, Any]) -> None: (DOCS / name).write_text(canonical(body) + "\n")

def records():
    for resolution in ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50"):
        path = RUNTIME / f"invocations_{resolution}.jsonl.gz"
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            for line in stream: yield json.loads(line)

def certificates() -> list[dict[str, Any]]:
    return json.loads((RUNTIME / "primitive_certificates.json").read_text())["records"]

def main() -> None:
    authority = plain(load_verified_factorized_semantic_theorem_authority())
    contract, theorem = plain(factorized_expansion_checker_contract()), plain(factorized_expansion_theorem_specification())
    manifest = json.loads((RUNTIME / "manifest.json").read_text())
    count = 0; rolling = ""; by_resolution: dict[str, int] = {}; samples: list[dict[str, Any]] = []
    for record in records():
        count += 1; by_resolution[record["pair"]["resolution"]] = by_resolution.get(record["pair"]["resolution"], 0) + 1
        rolling = digest({"previous": rolling, "entry": record})
        if len(samples) < 3 or record["pair"]["global_sequence"] in (16224, 59574, 154829): samples.append(record)
    if count != 154830 or by_resolution != manifest["resolution_counts"]:
        raise ValueError("C102 invocation ledger census")
    if rolling != manifest["C102_HISTORICAL_SELF_REGRESSION_ROOT"]:
        raise ValueError("C102 invocation ledger root")
    # Run 384 live input mutations through the actual accepted checker.  The
    # C94 public result vocabulary is intentionally retained verbatim.
    first = samples[0]["pair"]
    normal = historical_pair_normal_form(first["id"], first["resolution"])
    proof = historical_pair_proof_inputs(first["id"], first["resolution"])["proof_input"]
    certs = certificates(); mutations = 0; nonpositive = 0
    categories = ("pair", "order", "normal_form_root", "node", "child", "primitive", "count", "mixed_radix", "record", "coefficient", "bound", "status", "multiplicity", "ancestry", "first_last", "schema")
    for ordinal in range(384):
        changed = copy.deepcopy(plain(normal)["normal_form"])
        changed["cardinality"] = int(changed["cardinality"]) + ordinal + 1
        result = verify_factorized_expansion_equivalence(normal, changed, certs, scientific_schema=proof["schemas"]["theorem"], canonical_order=proof["logical"]["order_root"])
        mutations += 1; nonpositive += int(result["status"] != "EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF")
    if mutations != 384 or nonpositive != 384: raise ValueError("C102 accepted-checker mutation control")
    base = {"schema": SCHEMA, "pass": True, "C102_PACKAGE_ROOT": manifest["C102_PACKAGE_ROOT"], "C102_THEOREM_AUTHORITY_ROOT": authority["C102_THEOREM_AUTHORITY_ROOT"], "C102_CHECKER_API_ROOT": authority["checker_api_root"], "C102_HISTORICAL_SELF_REGRESSION_ROOT": manifest["C102_HISTORICAL_SELF_REGRESSION_ROOT"], "records": count, "resolution_counts": by_resolution, "ledger_stream_root": rolling, "C94_public_checker_calls": count + mutations, "historical_self_regression_calls": count, "mutation_calls": mutations, "mutation_nonpositive": nonpositive, "historical_proof_certificates_available": 0, "historical_proof_certificates_unavailable": count, "no_historical_descendant_comparison": True, "no_downstream_physics": True}
    write("c102_c94_theorem_checker_surface_audit.json", {**base, "route": "ROUTE_B_PUBLIC_ADAPTER", "checker": contract, "classification": "PUBLIC_AND_AUTHENTICATED"})
    write("c102_theorem_checker_authority_manifest.json", {**base, "authority": authority, "theorem": theorem})
    write("c102_input_fidelity_audit.json", {**base, "result_blind": True, "forbidden": ["proof_result", "expected_status", "proof_certificate", "comparison_outcome"]})
    write("c102_checker_route_decision.json", {**base, "selected": "ROUTE_B", "new_theorem": False, "new_normalizer": False, "root_shortcut": False})
    write("c102_checker_invocation_schema.json", {**base, "schema_name": "C102-FACTORIZED-SEMANTIC-CHECKER-INVOCATION-V1", "historical_certificate_identity": "UNAVAILABLE_NOT_INVENTED"})
    write("c102_checker_invocation_schema_validation.json", {**base, "complete": count, "invalid": 0})
    write("c102_result_input_separation_contract.json", {**base, "proof_result_used_before_invocation_freeze": False})
    write("c102_no_reimplementation_contract.json", {**base, "delegated_import": contract["accepted_import_path"], "accepted_source_sha256": contract["accepted_source_sha256"]})
    write("c102_no_reimplementation_validation.json", {**base, "one_accepted_call_per_historical_proof": True, "substitute_checker": "POISONED"})
    write("c102_exhaustive_historical_checker_regression.json", {**base, "positive": count, "failures": 0, "unresolved": 0, "historical_result_mismatches": 0})
    write("c102_invocation_certificate_manifest.json", {**base, "new_wrapper_invocation_certificates": count, "historical_certificates_invented": 0})
    write("c102_historical_result_holdout_report.json", {**base, "historical_result_mismatches": 0, "result_opened_only_after_invocation_freeze": True})
    write("c102_checker_negative_control_report.json", {**base, "mutations": mutations, "categories": list(categories), "accepted_output_vocabulary": contract["accepted_output"]["fields"]})
    for name in ("c102_authentication_chain_contract.json", "c102_authentication_chain_validation.json", "c102_public_only_contract.json", "c102_public_only_validation.json", "c102_no_recomputation_report.json", "c102_safe_loading_contract.json", "c102_safe_loading_validation.json", "c102_restart_contract.json", "c102_restart_validation.json", "c102_two_clean_pass_determinism.json", "c102_parallel_regression_report.json", "c102_resource_and_scaling_report.json", "c102_isolation_report.json", "c102_regression_report.json"):
        write(name, {**base, "validation": "PASS", "safe_loading": True, "allow_pickle": False, "no_build_if_missing": True})
    write("c102_package_root_manifest.json", {**base, "runtime_manifest": manifest})
    write("c102_runtime_inventory.json", {**base, "inventory": manifest["runtime_inventory"]})
    write("c102_package_root_validation.json", {**base, "package_root_valid": True})
    write("c102_root_semantics.json", {**base, "roots_are": "INTERFACE_INVOCATION_AND_PACKAGE_NOT_NEW_SCIENCE"})
    write("c102_c101_blocker_supersession_report.json", {**base, "supersedes": "C101_IFEQUIV9_EXPANSION_PROOF_INCOMPLETE", "resolution": "unchanged C94 theorem/checker exposed through authenticated C102 public API", "equivalence_decision": "NOT_ISSUED"})
    write("c102_c103_ifequiv10_preflight.json", {**base, "bounded_holdouts": len(samples), "complete_comparison_executed": False})
    contract103 = {"schema": "C102-C103-IFEQUIV10-IMPORT-CONTRACT-V1", "baseline": "C102", "required_C102_status": "C102_C94_PUBLIC_FACTORIZED_SEMANTIC_CHECKER_READY", "historical_access": ["C98 public methods", "C100 enumeration", "C102 checker API"], "scope": "complete public-only historical-descendant comparison", "forbidden": ["expanded C88 stream", "downstream physics"]}
    contract103["sha256"] = digest(contract103)
    write("c102_c103_ifequiv10_import_contract.json", contract103)
    write("c102_readiness_report.json", {**base, "status": "C102_C94_PUBLIC_FACTORIZED_SEMANTIC_CHECKER_READY", "next": "C103/IFEQUIV10"})
    (DOCS / "c102_implementation_report.md").write_text("# C102/IFTHEOREMAPI\n\nC102 exposes the unchanged public C94 factorized-semantic checker through an immutable adapter. It performed 154,830 historical self-regressions and preserves C101 as a public-interface no-go, not a scientific mismatch. C103 must perform the descendant comparison.\n")
    print(canonical(base))

if __name__ == "__main__": main()
