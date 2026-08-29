#!/usr/bin/env python3
"""Recover result-blind C90 checker operands into a compact C97 capsule."""
from __future__ import annotations

import argparse
from hashlib import blake2b, sha256
import gzip
import importlib
from itertools import chain
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Iterator

from deuteron_wigner.bridge.ifproofinput.normal_form_index import load_verified_normal_form_key_index
from deuteron_wigner.bridge.ifproofinput.zran_runtime import open_verified_zran_reader


ROOT = Path(__file__).resolve().parents[1]
CAPSULE = ROOT / "data" / "runtime" / "c97_ifproofinput" / "capsule"
C93 = ROOT / "data" / "runtime" / "c93_ifc90payload" / "capsule"
SCHEMA = "C97-HISTORICAL-C90-PROOF-INPUT-V1"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
C90_COMMIT = "ac622ab358b83f090717d7e7fa179b58f18f526d"


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def sha(value: Any) -> str:
    return sha256(canonical(value).encode()).hexdigest()


def b2(value: Any) -> str:
    return blake2b(canonical(value).encode(), digest_size=32).hexdigest()


def hash_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def plain(value: Any) -> Any:
    if isinstance(value, dict) or hasattr(value, "items"):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def _root(entries: list[dict[str, Any]]) -> dict[str, str]:
    return {"sha256": sha(entries), "blake2b_256": b2(entries)}


def _roll(previous: str, entry: dict[str, Any]) -> str:
    return sha({"previous": previous, "entry": entry})


def _expression_roots(node: dict[str, Any]) -> dict[str, str]:
    template_roots = {template["type"]: sha(template["expression"]) for template in node["templates"]}
    return {
        "record_construction": sha(node["child"]),
        "coefficient": sha(node["coefficient_expression"]),
        "bound": template_roots["BOUND_TEMPLATE"],
        "status": template_roots["STATUS_TEMPLATE"],
        "multiplicity": sha({"rank": node["child"]["rank"], "axis_order": node["child"]["axis_order"]}),
        "ancestry": template_roots["ANCESTRY_TEMPLATE"],
        "group": template_roots["GROUP_TEMPLATE"],
    }


def make_proof_input(node: dict[str, Any], global_sequence: int, authority: dict[str, Any], c90: dict[str, str]) -> dict[str, Any]:
    """Canonical pre-checker operands only; it never receives a result."""
    pair = dict(node["pair"])
    cardinality = int(node["cardinality"])
    expressions = _expression_roots(node)
    order = {"axis_order": node["child"]["axis_order"], "rank": node["child"]["rank"], "first_ordinal": 0, "last_ordinal": cardinality - 1}
    body = {
        "schema": SCHEMA,
        "pair": {**pair, "global_sequence": global_sequence, "resolution_sequence": pair["sequence"]},
        "route_a_normal_form": {"root": node["normal_form_root"], "content_root": sha(node), "source": "C90_PRE_CHECKER_OPERAND"},
        "route_b_normal_form": {"root": node["normal_form_root"], "content_root": sha(node), "source": "C93_AUTHENTICATED_NORMAL_FORM"},
        "primitive_equivalence": {"bindings": node["primitive_roots"], "bundle_root": sha(node["primitive_roots"])},
        "schemas": {"C88": node["scientific_field_schema"], "semantic_ir": c90["semantic_ir"], "normal_form": c90["normal_form"], "theorem": "C90-C82-SEMANTIC-IR-V1", "checker_api": "check_proof", "checker_source_sha256": c90["checker_source_sha256"]},
        "logical": {"cardinality": cardinality, "order": order, "order_root": sha(order), "first": sha({"pair": pair["id"], "ordinal": 0, "ir": node["normal_form_root"]}), "last": sha({"pair": pair["id"], "ordinal": cardinality - 1, "ir": node["normal_form_root"]})},
        "expressions": expressions,
        "provenance": {"C90_aggregate": authority["C90_aggregate"], "C93_capsule_root": authority["capsule_root"], "C94_package_root": authority["package_root"], "historical_environment": node["primitive_roots"]["environment"], "historical_C82": node["primitive_roots"]["historical_C82"]},
        "result_input_separation": {"proof_result_used_to_construct_input": False, "forbidden_fields": ["proof_result", "expected_status", "proof_certificate", "comparison_outcome"]},
    }
    body["proof_input_id"] = sha({"pair": pair, "normal_form_root": node["normal_form_root"], "schemas": body["schemas"], "logical": body["logical"], "expressions": expressions})
    body["proof_input_root"] = sha(body)
    return body


def _c93_normal_forms() -> Iterator[dict[str, Any]]:
    # Result-blind Route B only selects the persisted normal_form object.  It
    # neither reads nor passes onward the separate top-level proof field.
    with gzip.open(C93 / "normal_forms.jsonl.gz", "rt", encoding="utf-8") as stream:
        for line in stream:
            yield json.loads(line)["normal_form"]


def _c93_results() -> Iterator[dict[str, Any]]:
    with gzip.open(C93 / "pair_attestations.jsonl.gz", "rt", encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            yield {"pair": record["pair"], "historical_proof": record["proof"], "attestation_sha256": record["sha256"]}


def _load_exact_c90(worktree: Path) -> Any:
    if subprocess.check_output(["git", "-C", str(worktree), "rev-parse", "HEAD"], text=True).strip() != C90_COMMIT:
        raise ValueError("C97 Route-A worktree is not pinned to C90 completion")
    source = worktree / "src"
    sys.path.insert(0, str(source))
    module = importlib.import_module("deuteron_wigner.bridge.ifboundrestart.core")
    expected = "51d95bb4acf770e99a63dafd97940662c6eb59ffa5d99c39c7bc5d7bafdbf6a7"
    if hash_file(Path(module.__file__)) != expected:
        raise ValueError("C90 checker source fingerprint mismatch")
    return module


def _public_authority() -> dict[str, Any]:
    """Read C94 in an isolated descendant interpreter before C90 import."""
    program = """
import json
from deuteron_wigner.bridge.ifequivapi2 import load_verified_c93_public_authority
def plain(v):
    if isinstance(v, dict) or hasattr(v, 'items'): return {str(k): plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)): return [plain(x) for x in v]
    return v
print(json.dumps(plain(load_verified_c93_public_authority()), sort_keys=True))
"""
    environment = dict(__import__("os").environ)
    environment["PYTHONPATH"] = str(ROOT / "src")
    output = subprocess.check_output([sys.executable, "-c", program], text=True, env=environment)
    return json.loads(output)


def capture_route_a(worktree: Path, resolution: str) -> dict[str, Any]:
    CAPSULE.mkdir(parents=True, exist_ok=True)
    prior = next(iter(sorted(CAPSULE.glob("capture_meta_*.json"))), None)
    authority = json.loads(prior.read_text())["authority"] if prior is not None else _public_authority()
    c90_module = _load_exact_c90(worktree)
    c90 = {"semantic_ir": c90_module.SCHEMA, "normal_form": c90_module.NORMAL_FORM, "checker_source_sha256": hash_file(Path(c90_module.__file__))}
    route_a_path = CAPSULE / f"route_a_{resolution}.jsonl.gz"
    computed_path = CAPSULE / f"computed_{resolution}.jsonl.gz"
    count = 0
    global_start = {"K9_2_N8_b0.40": 0, "K11_2_N10_b0.45": 16224, "K13_2_N12_b0.50": 59574}[resolution]
    with gzip.open(route_a_path, "wt", encoding="utf-8") as capture, gzip.open(computed_path, "wt", encoding="utf-8") as results:
        for node in c90_module.compile_route_a(resolution):
            record = make_proof_input(node, global_start + count, authority, c90)
            capture.write(canonical(record) + "\n")
            result = c90_module.check_proof(node)
            results.write(canonical({"pair": node["pair"], "computed": result}) + "\n")
            count += 1
    expected = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}[resolution]
    if count != expected:
        raise ValueError("Route-A pair census mismatch")
    meta = {"authority": authority, "c90": c90, "count": count, "resolution": resolution}
    (CAPSULE / f"capture_meta_{resolution}.json").write_text(canonical(meta) + "\n")
    return meta


def assemble_route_b() -> dict[str, Any]:
    raise RuntimeError(
        "legacy Route-B assembly is forbidden: it constructs resolution-wide "
        "lookup dictionaries; use the bounded external bucket assembler"
    )
    # Historical implementation retained below only as a non-executable audit
    # specimen.  It must never be selected for K9, K11, or K13.
    metas = [json.loads((CAPSULE / f"capture_meta_{resolution}.json").read_text()) for resolution in RESOLUTIONS]
    authority = metas[0]["authority"]; c90 = metas[0]["c90"]; count = sum(int(meta["count"]) for meta in metas)
    if any(meta["authority"] != authority or meta["c90"] != c90 for meta in metas): raise ValueError("Route-A capture authority mismatch")

    records_dir = CAPSULE / "records"; records_dir.mkdir()
    resolution_indices: list[dict[str, Any]] = []
    current_resolution = None; current_by_pair: dict[str, Any] = {}; current_by_sequence: dict[str, Any] = {}
    resolution_start = 0
    operand_rolling = ""; resolution_operand_roots = {resolution: "" for resolution in RESOLUTIONS}
    shard_size = 256; shard = None; shard_ordinal = 0; shard_number = -1; shard_path = None
    route_streams = [gzip.open(CAPSULE / f"route_a_{resolution}.jsonl.gz", "rt", encoding="utf-8") for resolution in RESOLUTIONS]
    try:
        for sequence, (line, node) in enumerate(zip(chain.from_iterable(route_streams), _c93_normal_forms())):
            captured = json.loads(line)
            reconstructed = make_proof_input(node, sequence, authority, c90)
            if canonical(captured) != canonical(reconstructed):
                raise ValueError(f"Route-A/Route-B result-blind operand mismatch at {sequence}")
            resolution = reconstructed["pair"]["resolution"]
            if current_resolution is None:
                current_resolution = resolution; resolution_start = sequence
            elif resolution != current_resolution:
                index_path = f"index/{current_resolution}.json"
                (CAPSULE / "index").mkdir(exist_ok=True)
                (CAPSULE / index_path).write_text(canonical({"schema": SCHEMA, "resolution": current_resolution, "records": len(current_by_pair), "by_pair": current_by_pair, "by_sequence": current_by_sequence}) + "\n")
                resolution_indices.append({"resolution": current_resolution, "start": resolution_start, "records": len(current_by_pair), "index_path": index_path})
                current_resolution = resolution; resolution_start = sequence; current_by_pair = {}; current_by_sequence = {}
            if sequence % shard_size == 0:
                if shard is not None: shard.close()
                shard_number += 1; shard_ordinal = 0
                shard_path = f"records/shard_{shard_number:04d}.jsonl.gz"
                shard = gzip.open(CAPSULE / shard_path, "wt", encoding="utf-8")
            shard.write(canonical(reconstructed) + "\n")
            entry = {"path": shard_path, "ordinal": shard_ordinal}
            key = reconstructed["pair"]["id"]
            if key in current_by_pair:
                raise ValueError("duplicate C97 proof-input pair")
            local_sequence = sequence - resolution_start
            current_by_pair[key] = entry; current_by_sequence[str(local_sequence)] = entry
            root_entry = {"pair": reconstructed["pair"], "proof_input_root": reconstructed["proof_input_root"]}
            operand_rolling = _roll(operand_rolling, root_entry)
            resolution_operand_roots[resolution] = _roll(resolution_operand_roots[resolution], root_entry)
            shard_ordinal += 1
    finally:
        for stream in route_streams: stream.close()
    if shard is not None: shard.close()
    if current_resolution is None:
        raise ValueError("empty Route-B stream")
    index_path = f"index/{current_resolution}.json"
    (CAPSULE / "index").mkdir(exist_ok=True)
    (CAPSULE / index_path).write_text(canonical({"schema": SCHEMA, "resolution": current_resolution, "records": len(current_by_pair), "by_pair": current_by_pair, "by_sequence": current_by_sequence}) + "\n")
    resolution_indices.append({"resolution": current_resolution, "start": resolution_start, "records": len(current_by_pair), "index_path": index_path})
    # Stream-length comparison without retaining a second C93 result-bearing
    # iterator during Route B.
    c93_count = sum(1 for _ in _c93_normal_forms())
    if c93_count != count:
        raise ValueError("Route-B pair census mismatch")

    # Only after inputs and operand root are immutable may the holdout stream
    # be opened and historical proof results compared.
    result_rolling = ""; result_count = 0
    mismatches = 0
    result_streams = [gzip.open(CAPSULE / f"computed_{resolution}.jsonl.gz", "rt", encoding="utf-8") for resolution in RESOLUTIONS]
    with gzip.open(CAPSULE / "result_holdout.jsonl.gz", "wt", encoding="utf-8") as output:
        try:
            for item, hold in zip(chain.from_iterable(result_streams), _c93_results()):
                if item["pair"] != hold["pair"]:
                    raise ValueError("checker holdout pair-order mismatch")
                equal = canonical(item["computed"]) == canonical(hold["historical_proof"])
                mismatches += int(not equal)
                body = {"pair": item["pair"], "computed": item["computed"], "historical": hold["historical_proof"], "historical_attestation_sha256": hold["attestation_sha256"], "match": equal}
                output.write(canonical(body) + "\n")
                result_rolling = _roll(result_rolling, {"pair": item["pair"], "computed": sha(item["computed"]), "historical": sha(hold["historical_proof"]), "match": equal})
                result_count += 1
        finally:
            for stream in result_streams: stream.close()
    if result_count != count:
        raise ValueError("checker holdout census mismatch")
    if mismatches:
        raise ValueError("C90 checker regression mismatch")

    resolution_counts = {item["resolution"]: item["records"] for item in resolution_indices}
    index = {"schema": SCHEMA, "records": count, "resolutions": resolution_indices}
    (CAPSULE / "index.json").write_text(canonical(index) + "\n")
    # The temporary Route-A capture is not payload authority; it is removed
    # only after Route-B equality has closed.
    for resolution in RESOLUTIONS:
        (CAPSULE / f"route_a_{resolution}.jsonl.gz").unlink()
        (CAPSULE / f"computed_{resolution}.jsonl.gz").unlink()
        (CAPSULE / f"capture_meta_{resolution}.json").unlink()
    inventory_paths = ["index.json", "result_holdout.jsonl.gz"] + [str(path.relative_to(CAPSULE)) for path in sorted(records_dir.glob("*.gz"))] + [item["index_path"] for item in resolution_indices]
    inventory = {name: hash_file(CAPSULE / name) for name in inventory_paths}
    manifest = {"schema": SCHEMA, "records": count, "resolution_counts": resolution_counts, "C90_commit": C90_COMMIT, "C90_checker_source_sha256": c90["checker_source_sha256"], "C90_aggregate": authority["C90_aggregate"], "C93_capsule_root": authority["capsule_root"], "C94_package_root": authority["package_root"], "scientific_relation": "DESCENDANT_RECOVERED_CANONICAL_OPERAND_RECORD_FOR_FROZEN_C90_PROOF", "original_c90_runtime_proof_input_domain": "NOT_CLAIMED", "proof_result_used_to_construct_input": False, "operand_root": {"sha256": operand_rolling, "resolution_roots": resolution_operand_roots, "kind": "C97_PROOF_INPUT_OPERAND_ROOT"}, "result_root": {"sha256": result_rolling, "kind": "C97_PROOF_REGRESSION_RESULT_ROOT"}, "inventory": inventory, "claim_boundary": "RESULT_BLIND_CHECKER_OPERANDS_ONLY"}
    manifest["capsule_root"] = sha(manifest)
    (CAPSULE / "manifest.json").write_text(canonical(manifest) + "\n")
    return manifest


def assemble_route_b_indexed() -> dict[str, Any]:
    """Pair-local result-blind Route B using only the C97 metadata transport."""
    transport = CAPSULE.parent / "transport"
    source = C93 / "normal_forms.jsonl.gz"
    zran = open_verified_zran_reader(source, transport / "normal_forms.zran", transport / "c97_zran")
    forms = load_verified_normal_form_key_index(source, transport / "normal_forms.keyindex", zran)
    metas = {resolution: json.loads((CAPSULE / f"capture_meta_{resolution}.json").read_text()) for resolution in RESOLUTIONS}
    authority, c90 = metas[RESOLUTIONS[0]]["authority"], metas[RESOLUTIONS[0]]["c90"]
    results = {"records": 0, "field_mismatches": 0, "root_mismatches": 0, "order_mismatches": 0, "resolutions": {}}
    streams = {resolution: gzip.open(CAPSULE / f"route_a_{resolution}.jsonl.gz", "rt", encoding="utf-8") for resolution in RESOLUTIONS}
    output_paths = {resolution: CAPSULE / f"route_b_indexed_{resolution}.jsonl.gz" for resolution in RESOLUTIONS}
    temporary_paths = {resolution: path.with_suffix(path.suffix + ".tmp") for resolution, path in output_paths.items()}
    outputs = {resolution: gzip.open(path, "wt", encoding="utf-8") for resolution, path in temporary_paths.items()}
    local = {resolution: 0 for resolution in RESOLUTIONS}
    completed = False
    try:
        with gzip.open(C93 / "pair_attestations.jsonl.gz", "rt", encoding="utf-8") as bindings:
            for global_sequence, line in enumerate(bindings):
                binding = json.loads(line)
                pair = binding["pair"]; resolution = pair["resolution"]
                node = dict(forms.lookup_normal_form(resolution=resolution, pair_id=pair["id"], normal_form_root=binding["normal_form_root"])["normal_form"])
                if node["pair"] != pair or node["primitive_roots"] != binding["primitive_roots"]: raise ValueError("pair binding/normal-form mismatch")
                rebuilt = make_proof_input(node, global_sequence, authority, c90)
                outputs[resolution].write(canonical(rebuilt) + "\n")
                captured_raw = streams[resolution].readline()
                if not captured_raw: raise ValueError("missing Route-A capture")
                captured = json.loads(captured_raw)
                if captured["pair"] != rebuilt["pair"] or captured["pair"]["global_sequence"] != global_sequence or captured["pair"]["resolution"] != resolution: results["order_mismatches"] += 1
                if captured["proof_input_root"] != rebuilt["proof_input_root"]: results["root_mismatches"] += 1
                if canonical(captured) != canonical(rebuilt): results["field_mismatches"] += 1
                local[resolution] += 1; results["records"] += 1
        completed = True
    finally:
        for stream in streams.values(): stream.close()
        for output in outputs.values(): output.close()
        forms.close()
        if completed:
            for resolution in RESOLUTIONS: temporary_paths[resolution].replace(output_paths[resolution])
        else:
            for path in temporary_paths.values(): path.unlink(missing_ok=True)
    for resolution, expected in metas.items():
        if local[resolution] != expected["count"]: raise ValueError("Route-B resolution census mismatch")
        results["resolutions"][resolution] = local[resolution]
    if results["records"] != 154830 or any(results[key] for key in ("field_mismatches", "root_mismatches", "order_mismatches")): raise ValueError(f"Route-A/Route-B mismatch {results}")
    return results


def freeze_result_blind_capsule() -> dict[str, Any]:
    """Authenticate only the already-frozen C97 operand records.

    This deliberately does not open C93 proof attestations, historical
    checker results, or any result-bearing certificate source.
    """
    files = [f"route_b_indexed_{resolution}.jsonl.gz" for resolution in RESOLUTIONS]
    rolling = ""; count = 0
    for relative in files:
        with gzip.open(CAPSULE / relative, "rt", encoding="utf-8") as stream:
            for line in stream:
                record = json.loads(line)
                if set(record).intersection({"proof_result", "expected_status", "proof_certificate", "comparison_outcome"}):
                    raise ValueError("result-bearing field in frozen C97 operand")
                rolling = _roll(rolling, {"pair": record["pair"], "proof_input_root": record["proof_input_root"]})
                count += 1
    if count != 154830: raise ValueError("incomplete C97 operand capsule")
    meta = json.loads((CAPSULE / f"capture_meta_{RESOLUTIONS[0]}.json").read_text())
    transport = CAPSULE.parent / "transport" / "normal_forms.keyindex.json"
    index = json.loads(transport.read_text())
    proof_transport = CAPSULE.parent / "proof_transport"
    proof_indices = {resolution: json.loads((proof_transport / f"{resolution}.index.json").read_text())["root"] for resolution in RESOLUTIONS}
    body = {
        "schema": SCHEMA,
        "records": count,
        "record_paths": files,
        "inventory": {relative: hash_file(CAPSULE / relative) for relative in files},
        "C90_commit": C90_COMMIT,
        "C90_checker_source_sha256": meta["c90"]["checker_source_sha256"],
        "C90_aggregate": meta["authority"]["C90_aggregate"],
        "C93_capsule_root": meta["authority"]["capsule_root"],
        "C94_package_root": meta["authority"]["package_root"],
        "normal_form_transport_root": index["root"],
        "proof_input_transport_roots": proof_indices,
        "C97_PROOF_INPUT_OPERAND_ROOT": rolling,
        "proof_result_used_to_construct_input": False,
        "claim_boundary": "RESULT_BLIND_CHECKER_OPERANDS_ONLY",
    }
    body["C97_PROOF_INPUT_CAPSULE_ROOT"] = sha(body)
    temporary = CAPSULE / "proof_input_capsule_manifest.json.tmp"
    target = CAPSULE / "proof_input_capsule_manifest.json"
    temporary.write_text(canonical(body) + "\n"); temporary.replace(target)
    return body


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--c90-worktree", type=Path)
    parser.add_argument("--phase", choices=("capture", "assemble", "indexed", "freeze"), required=True)
    parser.add_argument("--resolution", choices=RESOLUTIONS)
    args = parser.parse_args()
    if args.phase == "capture":
        if args.c90_worktree is None: parser.error("--c90-worktree is required for capture")
        if args.resolution is None: parser.error("--resolution is required for capture")
        print(canonical(capture_route_a(args.c90_worktree, args.resolution)))
    elif args.phase == "assemble":
        print(canonical(assemble_route_b()))
    elif args.phase == "freeze":
        print(canonical(freeze_result_blind_capsule()))
    else:
        print(canonical(assemble_route_b_indexed()))
