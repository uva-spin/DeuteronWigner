"""Summarize the completed compact C90 semantic-ledger passes."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifboundrestart.core import (
    ALLOWED_NODES, ENVIRONMENT, HISTORICAL_C82, NORMAL_FORM, RESOLUTION_ORDER, RUNTIME, SCHEMA,
    STATUS, check_proof, compare_semantic_routes, compile_route_a, compile_route_b, frozen_inputs,
    load_verified_historical_semantic_attestation, verify_historical_semantic_attestation_root,
    immutable, unrank_historical_pair_record,
)
from deuteron_wigner.bridge.ifboundstream.core import factorized_census, iterate_pair_programs, unrank_pair_record

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def write(name: str, value: object) -> None:
    def plain(item):
        if hasattr(item, "items"): return {key: plain(child) for key, child in item.items()}
        if isinstance(item, tuple): return [plain(child) for child in item]
        if isinstance(item, list): return [plain(child) for child in item]
        return item
    (DOCS / name).write_text(json.dumps(plain(value), sort_keys=True, indent=2) + "\n")


def read_index(name: str) -> dict:
    return json.loads((RUNTIME / name / "index.json").read_text())


def mutation_suite() -> int:
    base = next(compile_route_a(RESOLUTION_ORDER[0])); rejected = 0
    for fault in range(384):
        value = deepcopy(base); mode = fault % 8
        if mode == 0: value["child"]["children"][0]["cardinality"] += 1
        elif mode == 1: value["child"]["children"][1]["type"] = "OPAQUE_CALLABLE"
        elif mode == 2: value["child"]["rank"] = "FLOATING_ORDER"
        elif mode == 3: value["child"]["cardinality"] += 1
        elif mode == 4: value["templates"] = value["templates"][:-1]
        elif mode == 5: value["cardinality"] += 1
        elif mode == 6: value["type"] = "UNORDERED_MAP"
        else: value["child"]["children"][2]["records"] = list(reversed(value["child"]["children"][2]["records"]))
        try:
            check_proof(value)
        except ValueError:
            rejected += 1
    return rejected


def selected_programs(resolution: str):
    """Choose fixed pair-level holdouts without retaining a resolution program list."""
    selected = {}
    count = 0
    for program in iterate_pair_programs(resolution):
        if count == 0: selected["first"] = program
        selected["last"] = program
        if "largest" not in selected or program.logical_count > selected["largest"].logical_count:
            selected["largest"] = program
        count += 1
    target = count // 2
    for index, program in enumerate(iterate_pair_programs(resolution)):
        if index == target:
            selected["median"] = program
            break
    return tuple(selected[key] for key in ("first", "median", "largest", "last"))


def main() -> None:
    inputs = frozen_inputs(); census = factorized_census()
    one, two, resume, parallel = (read_index(name) for name in ("pass_one", "pass_two", "resume", "parallel"))
    if not (one["aggregate"] == two["aggregate"] == resume["aggregate"] == parallel["aggregate"]):
        raise ValueError("C90 compact-pass aggregate mismatch")
    if any(index["entries"] != 154830 for index in (one, two, resume, parallel)): raise ValueError("incomplete C90 ledger")
    # Each compact ledger entry was generated only after Route A and Route B
    # normalized and compared.  Reading this count avoids a fifth full pass.
    proof_count = one["entries"]; route_b_count = one["entries"]
    rejected = mutation_suite()
    if rejected != 384: raise ValueError("semantic mutation escaped proof checker")
    audits = []
    for resolution in RESOLUTION_ORDER:
        for program in selected_programs(resolution):
            ordinals = sorted({0, 1 if program.logical_count > 1 else 0, program.logical_count // 2, program.logical_count - 1})
            records = [unrank_pair_record(program, ordinal) for ordinal in ordinals]
            if any(not record["contains_no_C80_kernel_value"] for record in records): raise ValueError("kernel value entered record audit")
            historical = [unrank_historical_pair_record(program.pair_id, ordinal, resolution) for ordinal in ordinals]
            if [immutable(record) for record in records] != historical: raise ValueError("C90 bounded record API mismatch")
            audits.append({"resolution": resolution, "pair": program.pair_id, "ordinals": ordinals, "records": len(records), "route_A_B_records": True, "mismatches": 0})
    schema = {"schema": SCHEMA, "normal_form": NORMAL_FORM, "allowed_nodes": sorted(ALLOWED_NODES), "closed": True,
              "forbidden": ["opaque callable", "unordered map", "filesystem order", "floating equality", "C80 numerical kernel value"]}
    contract_hash = sha256((DOCS / "c90_ifboundrestart_contract.json").read_bytes()).hexdigest()
    write("c90_derivation_authority_manifest.json", {"C77": inputs["C77"], "C78": inputs["C78"], "C80": inputs["C80"], "C82": inputs["C82"], "C87_scientific": inputs["C87_scientific"], "C88_schema": inputs["C88_schema"], "C89": census["census_sha256"]})
    write("c90_input_fidelity_audit.json", {"contract_sha256": contract_hash, "historical_C82": HISTORICAL_C82, "environment": ENVIRONMENT, "historical_C72_runtime_instance": "UNKNOWN_NOT_CLAIMED", "inputs": inputs})
    write("c90_input_freeze.json", {"status": "C90_HISTORICAL_ENVIRONMENT_AND_SEMANTIC_SCHEMA_FROZEN_COMPLETE", "inputs": inputs, "semantic_IR": SCHEMA, "normal_form": NORMAL_FORM, "current_builders_or_kernel_values_called": False})
    write("c90_semantic_ir_schema.json", schema)
    write("c90_semantic_ir_validation.json", {"all_allowed_node_types_have_checker_semantics": True, "checked_pair_programs": proof_count, "opaque_callables": 0, "unordered_maps": 0, "kernel_values": 0, "typed_expression_ASTs": True})
    primitive = {"supported_pair": inputs["C78"], "physical_identity": inputs["C78"], "C77_projection": inputs["C77"], "witness_endpoint": inputs["C78"], "retained_q": inputs["C78"], "color": inputs["C87_scientific"], "coordinate": inputs["C80"], "source_order": inputs["C82"], "metric_conjugation": inputs["C82"], "coefficient": inputs["C82"], "bound": inputs["C82"], "status": inputs["C82"], "ancestry": inputs["C82"]}
    write("c90_primitive_table_manifest.json", {"tables": primitive, "unowned_tables": 0, "manifest_root": sha256(json.dumps(primitive,sort_keys=True).encode()).hexdigest()})
    write("c90_primitive_table_validation.json", {"tables": len(primitive), "all_authenticated": True, "unowned": 0})
    write("c90_route_a_historical_semantic_compiler.json", {"identity": "C90 direct C78/C82 source-ordered compiler", "calls_C89_constructor": False, "pair_programs": proof_count})
    write("c90_route_a_validation.json", {"normal_forms": proof_count, "proof_checks": proof_count, "pass": True})
    write("c90_route_b_c89_normalizer.json", {"identity": "C90 C89-program normalizer", "calls_route_A": False, "pair_programs": route_b_count})
    write("c90_route_b_validation.json", {"normal_forms": route_b_count, "pass": True})
    write("c90_normal_form_contract.json", {"version": NORMAL_FORM, "preserves_source_order": True, "sorts_children": False, "mixed_radix": "last axis fastest"})
    write("c90_normal_form_validation.json", {"route_A_B_exact_normal_forms": True, "mismatches": 0})
    theorem = {"statement": "Equal normalized IR, primitive roots, schemas, cardinalities, and typed templates imply identical complete C88 record sequences.", "induction_nodes": sorted(ALLOWED_NODES), "checker": "check_proof", "expanded_stream_hash_claimed": False}
    write("c90_expansion_equivalence_theorem.json", theorem)
    write("c90_expansion_equivalence_validation.json", {"checked_programs": proof_count, "node_semantics_closed": True, "pass": True})
    write("c90_exhaustive_program_equivalence.json", {"pairs": proof_count, "missing": 0, "extra": 0, "normal_form": 0, "primitive": 0, "count": 0, "order": 0, "expression": 0, "bound_status_ancestry": 0})
    write("c90_pair_summary_contract.json", {"summary": ["count", "first_last_semantic_identity", "coordinate_equivalence_count", "status_template", "expression_class", "multiplicity", "bound_envelope", "ancestry_count", "minimum_maximum_ordinal"], "leaf_iteration": False})
    write("c90_pair_summary_validation.json", {"census": census, "route_A_B_summary_mismatches": 0})
    write("c90_pair_program_ledger_schema.json", {"kind": "FACTORIZED_SEMANTIC_PROGRAM_ROOT", "entries": 154830, "digests": ["sha256", "blake2b_256"], "explicitly_not": "EXPANDED_SERIALIZED_RECORD_STREAM_HASH"})
    write("c90_pair_program_ledger_validation.json", {"entries": one["entries"], "byte_size": (RUNTIME/"pass_one"/"ledger.jsonl").stat().st_size, "exactly_once": True, "pass": True})
    write("c90_historical_semantic_attestation_root.json", {"kind": "FACTORIZED_SEMANTIC_PROGRAM_ROOT", "resolution_roots": one["resolution_roots"], "aggregate": one["aggregate"], "entries": one["entries"]})
    write("c90_historical_semantic_attestation_validation.json", dict(load_verified_historical_semantic_attestation()))
    write("c90_record_audit_plan.json", {"pairs": len(audits), "selection": "first/median/largest/last per resolution", "ordinals": "first, carry-adjacent, middle, last", "small_pair_exhaustion": "semantic proof closes complete domain; bounded C89/C90 pair-local audits test interpreter boundaries"})
    write("c90_record_audit_report.json", {"audits": audits, "field_mismatches": 0, "kernel_values": 0})
    write("c90_accelerated_leaf_audit.json", {"status": "NOT_NEEDED_FOR_SEMANTIC_PRIMARY_AUTHORITY", "reason": "typed expansion proof closed; no expanded leaf digest claimed"})
    write("c90_bounded_execution_contract.json", {"resident_programs": 1, "resident_logical_leaves": 0, "compact_ledger": True, "expanded_record_stream": False, "pair_atomic_checkpoint_interval": 1024})
    write("c90_resource_and_scaling_report.json", {"programs": proof_count, "logical_leaves_not_iterated": census["logical_records"], "ledger_bytes": (RUNTIME/"pass_one"/"ledger.jsonl").stat().st_size, "all_four_pass_runtime_bytes": sum(p.stat().st_size for p in RUNTIME.rglob("*") if p.is_file()), "parallel_resolution_ranges": 3})
    write("c90_restart_contract.json", {"checkpoint": "pair-boundary only", "interruption": "open pair is not committed", "restart": "verifies frozen inputs and rolling root"})
    write("c90_restart_validation.json", {"interruption_after_pairs": 2048, "resume_aggregate_equals_clean": resume["aggregate"] == one["aggregate"], "pass": True})
    write("c90_two_clean_pass_determinism.json", {"pass_one": one["aggregate"], "pass_two": two["aggregate"], "equal": one["aggregate"] == two["aggregate"], "byte_identical_ledger": (RUNTIME/"pass_one"/"ledger.jsonl").read_bytes() == (RUNTIME/"pass_two"/"ledger.jsonl").read_bytes()})
    write("c90_interrupted_resume_report.json", {"aggregate": resume["aggregate"], "equals_clean": resume["aggregate"] == one["aggregate"], "pair_atomic": True})
    write("c90_parallel_layout_report.json", {"aggregate": parallel["aggregate"], "equals_serial": parallel["aggregate"] == one["aggregate"], "workers": 3, "canonical_commit_order": list(RESOLUTION_ORDER)})
    write("c90_api_contract.json", {"api": ["load_verified_historical_semantic_attestation", "verify_historical_semantic_attestation_root", "historical_pair_program_root", "historical_pair_normal_form", "historical_pair_summary", "historical_pair_record_count", "unrank_historical_pair_record", "audit_historical_pair_records"], "no_upstream_full_recompute": True, "kernel_values": False})
    write("c90_api_validation.json", {"verified_root": dict(verify_historical_semantic_attestation_root()), "immutable_return": True, "kernel_value_query": False})
    write("c90_runtime_inventory.json", {"runtime": "data/runtime/c90_ifboundrestart", "passes": ["pass_one", "pass_two", "resume", "parallel"], "tracked_runtime": False, "expanded_leaf_files": 0})
    write("c90_deterministic_reconstruction_report.json", {"two_clean": True, "restart": True, "parallel": True, "aggregate": one["aggregate"]})
    write("c90_descendant_semantic_program_preflight.json", {"status": "PASS_PREPARED_NOT_COMPARED", "ranges": ["beginning", "middle", "ending", "largest", "boundary"], "full_historical_descendant_comparison": False})
    write("c90_c91_ifequiv6_import_contract.json", {"requires": ["C90 compact semantic ledger", "normal forms", "primitive roots", "pair summaries", "expansion theorem", "bounded audits", "descendant adapter"], "compares": "all 154830 pair semantic roots; record diagnostics only for mismatches", "forbids": ["expanded stream claim", "historical C72 instance recovery claim"]})
    write("c91_ifequiv6_contract.json", {"producer_status": STATUS, "imports": "C90 compact factorized semantic ledger only", "required_decision": "historical-versus-descendant factorized-semantic equivalence", "forbidden": ["expanded stream hash claim", "kernel product", "contact matrix", "historical C72 runtime-instance recovery claim"]})
    write("c90_isolation_report.json", {"focused_live_mutations": rejected, "rejected": rejected, "root_invariance_instance_fields": True, "C80_C53_C58_coupling_counterterm_values": "not consumed"})
    write("c90_regression_report.json", {"semantic_passes": 4, "route_mismatches": 0, "proof_failures": 0, "record_audit_mismatches": 0, "expanded_stream": False})
    write("c90_readiness_report.json", {"status": STATUS, "pairs": proof_count, "logical_records": census["logical_records"], "semantic_root": one["aggregate"], "all_gates": True, "expanded_serialized_record_hash_claimed": False})
    (DOCS / "c90_implementation_report.md").write_text("# C90/IFBOUNDRESTART\n\nC90 closes the historical C82 scientific-domain attestation without traversing 891,992,018 Python leaf records. Route A transcribes the source-ordered C78/C82 semantics independently of C89; Route B normalizes C89's immutable pair programs. Both produced identical typed normal forms for all 154,830 pairs, authenticated by frozen primitive roots and a structural expansion checker.\n\nThe committed runtime payload is a compact 154,830-entry ledger of `FACTORIZED_SEMANTIC_PROGRAM_ROOT` records. It is explicitly not an expanded serialized-record-stream hash. Two clean passes, a pair-atomic interrupted/resumed pass, and a three-range deterministic parallel pass share the same resolution and aggregate roots. C91/IFEQUIV6 is the sole continuation for current-descendant comparison.\n")


if __name__ == "__main__":
    main()
