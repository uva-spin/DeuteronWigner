#!/usr/bin/env python3
"""C103 exhaustive public-only factorized-semantic comparison.

Phase one imports only the independent current descendant compiler.  The
historical C98/C100/C102 API imports are deliberately delayed until the
complete descendant ledger and its roots have been frozen.
"""
from __future__ import annotations

import argparse
import gzip
import io
from hashlib import sha256
import json
from pathlib import Path
import shutil
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/runtime/c103_ifequiv10"
DOCS = ROOT / "docs/next_level"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
COUNTS = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}
LOGICAL = {"K9_2_N8_b0.40": 28606464, "K11_2_N10_b0.45": 165991250, "K13_2_N12_b0.50": 697394304}
DROP_INSTANCE = {"current_source_commit", "historical_C72_runtime_instance", "normal_form", "semantic_ir"}


def plain(value: Any) -> Any:
    if hasattr(value, "items"): return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [plain(v) for v in value]
    return value


def canonical(value: Any) -> str:
    return json.dumps(plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(value: Any) -> str: return sha256(canonical(value).encode()).hexdigest()
def fhash(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()
def atomic(path: Path, value: Any) -> None:
    tmp = path.with_name(path.name + ".tmp"); tmp.write_text(canonical(value) + "\n"); tmp.replace(path)

def deterministic_gzip(path: Path):
    raw=path.open('wb'); gz=gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0)
    return io.TextIOWrapper(gz,encoding='utf-8'),raw


def normalize_descendant(program: dict[str, Any], sha) -> dict[str, Any]:
    result = json.loads(canonical(program))
    result["primitive_roots"] = {key: value for key, value in result["primitive_roots"].items() if key not in DROP_INSTANCE}
    result["normal_form_root"] = sha({key: value for key, value in result.items() if key != "normal_form_root"})
    return result


def freeze_descendant(output: Path) -> dict[str, Any]:
    """D1-D4: no C98/C100/C102 imports or calls occur in this function."""
    from deuteron_wigner.bridge.ifequiv6.core import compile_descendant_programs, current_descendant_inputs, sha
    output.mkdir(parents=True, exist_ok=True)
    path = output / "descendant_ledger.jsonl.gz"
    rolling = ""; roots = {}; counts = {}; logical = {}; global_sequence = 0
    stream,raw_stream=deterministic_gzip(path)
    try:
        for resolution in RESOLUTIONS:
            local_root = ""; count = total = 0
            for local, raw in enumerate(compile_descendant_programs(resolution)):
                program = normalize_descendant(raw, sha)
                if program["pair"]["sequence"] != local or program["pair"]["resolution"] != resolution:
                    raise ValueError("descendant pair ordering defect")
                summary = {"logical_count": program["cardinality"], "first": program["first_ordinal"], "last": program["last_ordinal"], "order": program["child"]["rank"], "normal_form_root": program["normal_form_root"]}
                record = {"pair": {**program["pair"], "global_sequence": global_sequence, "resolution_sequence": local}, "program": program, "summary": summary}
                record["descendant_program_root"] = digest({"pair": record["pair"], "normal_form_root": program["normal_form_root"], "summary": summary})
                stream.write(canonical(record) + "\n")
                local_root = digest({"previous": local_root, "entry": record["descendant_program_root"]})
                rolling = digest({"previous": rolling, "entry": record["descendant_program_root"]})
                count += 1; total += program["cardinality"]; global_sequence += 1
            roots[resolution] = local_root; counts[resolution] = count; logical[resolution] = total
    finally:
        stream.close(); raw_stream.close()
    if counts != COUNTS or logical != LOGICAL or global_sequence != 154830:
        raise ValueError("descendant census mismatch")
    body = {"schema": "C103-DESCENDANT-HISTORICAL-BLIND-FREEZE-V1", "historical_imports": False, "historical_expected_outputs": False, "poisoned": ["C98", "C100", "C102_positive_results", "C99_C101_holdouts"], "adapter_registry_precomparison": {"drop_instance_primitive_root_keys": sorted(DROP_INSTANCE), "classification": "INSTANCE_ONLY_SOURCE_API_METADATA", "scientific_field_changes": False}, "current_inputs": dict(current_descendant_inputs()), "resolution_counts": counts, "logical_records": logical, "pairs": global_sequence, "logical_total": sum(logical.values()), "resolution_roots": roots, "C103_DESCENDANT_AGGREGATE_SEMANTIC_ROOT": rolling, "ledger": path.name, "ledger_sha256": fhash(path)}
    body["root"] = digest(body); atomic(output / "descendant_freeze.json", body)
    return body


def primitives():
    """Enumerate via C100 and obtain content only via C98 after D4 closure."""
    from deuteron_wigner.bridge.ifprimenum import historical_primitive_domain_manifest, historical_primitive_record_page
    from deuteron_wigner.bridge.ifhistpublic2 import historical_primitive_record
    domain = plain(historical_primitive_domain_manifest())
    cursor = None; rows = []
    while True:
        page = plain(historical_primitive_record_page(cursor=cursor, limit=5))
        for identity in page["records"]:
            direct = plain(historical_primitive_record(identity["family_id"], identity["record_id"]))
            if any(direct[key] != identity[key] for key in ("record_digest", "family_root", "inclusion")):
                raise ValueError("public primitive identity/content mismatch")
            rows.append({"family_id": identity["family_id"], "record_id": identity["record_id"], "record_digest": identity["record_digest"], "family_root": identity["family_root"], "inclusion": identity["inclusion"], "C98_return_root": direct["return_root"], "relation": "CANONICALLY_IDENTICAL_SCIENTIFIC_RECORD"})
        cursor = page["next_cursor"]
        if cursor is None: break
    if domain["family_count"] != 5 or len(rows) != 35 or len({(r['family_id'],r['record_id']) for r in rows}) != 35:
        raise ValueError("primitive domain census")
    return domain, rows, digest(rows)


def compare(output: Path, freeze: dict[str, Any]) -> dict[str, Any]:
    from deuteron_wigner.bridge.ifhistpublic2 import historical_pair_normal_form, historical_pair_proof_inputs
    from deuteron_wigner.bridge.iftheoremapi import load_verified_factorized_semantic_theorem_authority, verify_factorized_expansion_equivalence, verify_factorized_expansion_invocation
    authority = plain(load_verified_factorized_semantic_theorem_authority())
    domain, certs, cert_root = primitives()
    atomic(output / "primitive_certificates.json", {"schema": "C103-PRIMITIVE-EQUIVALENCE-CERTIFICATES-V1", "records": certs, "root": cert_root, "families": domain["family_count"], "C100_package_root": domain["C100_package_root"]})
    mismatch_keys = ("MISSING_PAIR", "EXTRA_PAIR", "PAIR_IDENTITY", "PAIR_ORDER", "NORMAL_FORM_ROOT", "NORMAL_FORM_CONTENT", "NODE_GRAPH", "PRIMITIVE_DEPENDENCY", "LOGICAL_COUNT", "ORDER", "RECORD_EXPRESSION", "COEFFICIENT_EXPRESSION", "BOUND_RULE", "STATUS_RULE", "MULTIPLICITY_RULE", "ANCESTRY_RULE", "FIRST_LAST_IDENTITY", "SUMMARY", "PAIR_ROOT")
    mismatches = {key: 0 for key in mismatch_keys}
    total = proof_ok = 0; equivalence_root = ""; desc_roots = {r: "" for r in RESOLUTIONS}; eq_roots = {r: "" for r in RESOLUTIONS}; counts = {r: 0 for r in RESOLUTIONS}
    outfile = output / "pair_ledger.jsonl.gz"
    source=gzip.open(output / "descendant_ledger.jsonl.gz", "rt", encoding="utf-8"); sink,sink_raw=deterministic_gzip(outfile)
    try:
        for line in source:
            row = json.loads(line); pair = row["pair"]; resolution = pair["resolution"]; pair_id = pair["id"]; program = row["program"]
            historical = plain(historical_pair_normal_form(pair_id, resolution)); proof_input = plain(historical_pair_proof_inputs(pair_id, resolution))["proof_input"]
            history = historical["normal_form"]
            # Canonical fields are compared before invoking the theorem.
            if history["pair"] != {k: pair[k] for k in ("sequence", "resolution", "id", "bra", "ket")}: mismatches["PAIR_IDENTITY"] += 1
            if history["normal_form_root"] != program["normal_form_root"]: mismatches["NORMAL_FORM_ROOT"] += 1
            if canonical(history) != canonical(program): mismatches["NORMAL_FORM_CONTENT"] += 1
            if history["cardinality"] != program["cardinality"]: mismatches["LOGICAL_COUNT"] += 1
            if history["child"]["rank"] != program["child"]["rank"] or history["child"]["axis_order"] != program["child"]["axis_order"]: mismatches["ORDER"] += 1
            invocation = plain(verify_factorized_expansion_equivalence(historical, program, certs, scientific_schema=proof_input["schemas"]["theorem"], canonical_order=proof_input["logical"]["order_root"]))
            if not verify_factorized_expansion_invocation(invocation)["pass"]: raise ValueError("C102 invocation certificate")
            if invocation["status"] != "EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF": raise ValueError("C102 theorem nonpositive")
            proof_ok += 1; total += 1; counts[resolution] += 1
            compact = {"pair": pair, "historical_program_root": history["normal_form_root"], "descendant_program_root": row["descendant_program_root"], "primitive_equivalence_certificate_root": cert_root, "logical_count": program["cardinality"], "comparison_status": invocation["status"], "C102_theorem_input_root": digest({"history": history["normal_form_root"], "descendant": program["normal_form_root"], "cert": cert_root, "order": proof_input["logical"]["order_root"]}), "C103_equivalence_certificate_root": invocation["computed_invocation_certificate_root"], "summary": row["summary"], "difference_classification": "NO_DIFFERENCE"}
            sink.write(canonical(compact) + "\n")
            desc_roots[resolution] = digest({"previous": desc_roots[resolution], "entry": row["descendant_program_root"]})
            eq_roots[resolution] = digest({"previous": eq_roots[resolution], "entry": compact["C103_equivalence_certificate_root"]})
            equivalence_root = digest({"previous": equivalence_root, "entry": compact["C103_equivalence_certificate_root"]})
    finally:
        source.close(); sink.close(); sink_raw.close()
    if total != 154830 or proof_ok != total or counts != COUNTS or any(mismatches.values()):
        raise ValueError(f"C103 comparison mismatch {total=} {proof_ok=} {counts=} {mismatches=}")
    return {"authority": authority, "primitive_domain": domain, "primitive_certificates": certs, "primitive_certificate_root": cert_root, "records": total, "proof_successes": proof_ok, "mismatches": mismatches, "resolution_counts": counts, "C103_DESCENDANT_AGGREGATE_SEMANTIC_ROOT": freeze["C103_DESCENDANT_AGGREGATE_SEMANTIC_ROOT"], "C103_HISTORICAL_DESCENDANT_EQUIVALENCE_CERTIFICATE_ROOT": equivalence_root, "descendant_resolution_roots": desc_roots, "equivalence_resolution_roots": eq_roots, "pair_ledger_sha256": fhash(outfile)}


def run(output: Path) -> dict[str, Any]:
    if output.exists(): shutil.rmtree(output)
    freeze = freeze_descendant(output)
    comparison = compare(output, freeze)
    inventory = [{"path": p.name, "bytes": p.stat().st_size, "sha256": fhash(p)} for p in sorted(output.iterdir()) if p.is_file()]
    manifest = {"schema": "C103-IFEQUIV10-PUBLIC-EQUIVALENCE-V1", **{k:v for k,v in comparison.items() if k not in ("primitive_certificates",)}, "descendant_freeze_root": freeze["root"], "adapter_registry_root": digest(freeze["adapter_registry_precomparison"]), "runtime_inventory": inventory, "scientific_decision": "SCIENTIFICALLY_EQUIVALENT_WITH_INSTANCE_ONLY_DIFFERENCES", "expanded_C88_records": False, "downstream_physics": False}
    manifest["C103_PACKAGE_ROOT"] = digest(manifest); atomic(output / "manifest.json", manifest)
    return manifest


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--out", type=Path, default=OUT); args=parser.parse_args(); print(canonical(run(args.out)))
if __name__ == "__main__": main()
