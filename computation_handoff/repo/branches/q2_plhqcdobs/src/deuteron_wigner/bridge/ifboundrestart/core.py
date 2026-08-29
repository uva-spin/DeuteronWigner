"""Typed, nonmaterializing semantic IR for C82 pair-coordinate programs."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import lru_cache
from hashlib import blake2b, sha256
import json
import os
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterator
from itertools import zip_longest

from ..ifboundstream.core import RESOLUTION_ORDER, iterate_pair_programs

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c90_ifboundrestart"
STATUS = "C90_C82_FACTORIZED_SEMANTIC_ATTESTATION_READY"
SCHEMA = "C90-C82-SEMANTIC-IR-V1"
NORMAL_FORM = "C90-NORMAL-FORM-V1"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
HISTORICAL_C82 = "8e47231ab565f0f729d335b39aa98881176ba166"
ALLOWED_NODES = {"ATOM_TABLE", "ORDERED_RANGE", "ORDERED_UNION", "CARTESIAN_PRODUCT", "FILTER", "PERMUTE", "MAP_RECORD", "GROUP_TEMPLATE", "ANCESTRY_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE"}


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def sha(value: Any) -> str: return sha256(canonical(value).encode()).hexdigest()
def b2(value: Any) -> str: return blake2b(canonical(value).encode(), digest_size=32).hexdigest()


def immutable(value: Any) -> Any:
    """Recursively freeze a public semantic record without changing its value."""
    if isinstance(value, dict): return MappingProxyType({key: immutable(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(immutable(item) for item in value)
    if isinstance(value, tuple): return tuple(immutable(item) for item in value)
    return value


@lru_cache(maxsize=1)
def frozen_inputs() -> dict[str, str]:
    def read(path: str) -> dict[str, Any]: return json.loads((ROOT / path).read_text())
    c87 = read("data/authority/c87_canonical_c72_color_authority/manifest.json")
    c77, c78, c80, c82 = (read(path) for path in ("data/runtime/c77_qgembed9/root.json", "data/runtime/c78_ifsupport2/root.json", "data/runtime/c80_ifkernel2/root.json", "data/runtime/c82_ifagg/root.json"))
    return {"historical_C82": HISTORICAL_C82, "environment": ENVIRONMENT, "C87_scientific": c87["scientific_root"], "C87_capsule": c87["compatibility_root"],
            "C77": c77["aggregate_sha256"], "C78": c78["aggregate_sha256"], "C80": c80["index_sha256"], "C82": c82["index_sha256"],
            "C88_schema": "2f6268aaa6338afa0c108b2d037c6d396be31b67ca65cec10aa1f4f3d0f623a8"}


@lru_cache(maxsize=None)
def _payload(resolution: str) -> dict[str, Any]:
    return json.loads((ROOT / "data/runtime/c78_ifsupport2" / f"{resolution}.json").read_text())


def _route_a_rows(resolution: str) -> Iterator[dict[str, Any]]:
    """Direct historical C78/C82 loop semantics; never calls C89 constructors."""
    payload = _payload(resolution)
    emission = {row["id"]: row for row in payload["emission_edges"]}; absorption = {row["id"]: row for row in payload["absorption_edges"]}
    for group in payload["witness_groups"]:
        for eid in group["emission_endpoint_ids"]:
            for aid in group["absorption_endpoint_ids"]:
                out, inn = emission[eid], absorption[aid]; od, id_ = payload["emission_path_domains"][eid], payload["absorption_path_domains"][aid]
                yield {"resolution": resolution, "pair_id": f"{out['physical_qg_id']}|{inn['physical_qg_id']}", "bra": out["physical_qg_id"], "ket": inn["physical_qg_id"],
                       "witness": {"intermediate": group["intermediate_q_id"], "emission": eid, "absorption": aid, "source_order": ("b_dagger", "a_dagger", "a", "b")},
                       "axes": (("output_component", tuple(od["component_ids"])), ("output_color", tuple(od["color_record_ids"])),
                                ("input_component", tuple(id_["component_ids"])), ("input_color", tuple(id_["color_record_ids"])))}


def _base_ir(row: dict[str, Any], sequence: int) -> dict[str, Any]:
    axes = []
    for name, values in row["axes"]:
        axes.append({"type": "ATOM_TABLE", "table": f"C78:{name}", "order": "FROZEN_LIST", "records": list(values), "cardinality": len(values),
                     "first_ordinal": 0, "last_ordinal": len(values) - 1, "record_schema": "FROZEN_SCIENTIFIC_IDENTIFIER_V1"})
    product = {"type": "CARTESIAN_PRODUCT", "axis_order": [axis["table"].removeprefix("C78:") for axis in axes], "children": axes,
               "cardinality": int(__import__("math").prod(axis["cardinality"] for axis in axes)), "rank": "MIXED_RADIX_LAST_AXIS_FASTEST",
               "record_schema": "C82_WITNESS_LEAF_TUPLE_V1"}
    return {"type": "MAP_RECORD", "schema": "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1", "pair": {"sequence": sequence, "resolution": row["resolution"], "id": row["pair_id"], "bra": row["bra"], "ket": row["ket"]},
            "child": product, "templates": [
              {"type": "GROUP_TEMPLATE", "expression": {"opcode": "GROUP_BY_EXACT_COORDINATE", "operands": ["ordered_raw_color_tuple"], "coalescing": "NONE"}},
              {"type": "BOUND_TEMPLATE", "expression": {"opcode": "C82_PROPAGATED_PRODUCT_BOUND", "operands": ["C77_bounds", "color_bounds"]}},
              {"type": "STATUS_TEMPLATE", "expression": {"opcode": "INTERVAL_NONZERO_RULE", "operands": ["midpoint", "bound"]}},
              {"type": "ANCESTRY_TEMPLATE", "expression": {"opcode": "ORDERED_ANCESTRY", "operands": ["witness", "endpoint", "component", "color"]}, "witness": row["witness"]}],
            "coefficient_expression": {"opcode": "MULTIPLY", "operands": [{"opcode": "CONJUGATE", "operand": {"opcode": "MULTIPLY", "operands": ["C77COMP_bra", "U3_bra"]}}, {"opcode": "MULTIPLY", "operands": ["C77COMP_ket", "U3_ket"]}]},
            "ownership": "C82 embedding/metric/conjugation; C80 owns W3/g_s2", "forbids": ["C80 numerical kernel", "g_s_squared", "coefficient_times_kernel"]}


def normalize(ir: dict[str, Any]) -> dict[str, Any]:
    """Closed canonical normalizer: it never sorts a source-ordered axis."""
    if ir["type"] != "MAP_RECORD": raise ValueError("top-level MAP_RECORD required")
    node = dict(ir); product = dict(node["child"])
    if product["type"] != "CARTESIAN_PRODUCT" or product["rank"] != "MIXED_RADIX_LAST_AXIS_FASTEST": raise ValueError("invalid product semantics")
    product["children"] = [dict(child) for child in product["children"]]
    for child in product["children"]:
        if child["type"] != "ATOM_TABLE" or child["cardinality"] != len(child["records"]): raise ValueError("invalid ordered primitive axis")
    product["cardinality"] = int(__import__("math").prod(child["cardinality"] for child in product["children"]))
    product["first_ordinal"] = 0; product["last_ordinal"] = product["cardinality"] - 1
    node["child"] = product; node["templates"] = [dict(x) for x in node["templates"]]
    node["normal_form"] = NORMAL_FORM; node["primitive_roots"] = frozen_inputs(); node["cardinality"] = product["cardinality"]
    node["first_ordinal"] = 0; node["last_ordinal"] = product["cardinality"] - 1
    node["scientific_field_schema"] = "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1"
    node["normal_form_root"] = sha({key: value for key, value in node.items() if key != "normal_form_root"})
    return node


def compile_route_a(resolution: str) -> Iterator[dict[str, Any]]:
    for sequence, row in enumerate(_route_a_rows(resolution)):
        yield normalize(_base_ir(row, sequence))


def compile_route_b(resolution: str) -> Iterator[dict[str, Any]]:
    """Independent consumer of C89's immutable factorized program API."""
    for program in iterate_pair_programs(resolution):
        row = {"resolution": resolution, "pair_id": program.pair_id, "bra": program.physical_bra_id, "ket": program.physical_ket_id,
               "witness": {"intermediate": program.intermediate_q_id, "emission": program.emission_endpoint_id, "absorption": program.absorption_endpoint_id, "source_order": ("b_dagger", "a_dagger", "a", "b")},
               "axes": (("output_component", program.output_component_ids), ("output_color", program.output_color_record_ids), ("input_component", program.input_component_ids), ("input_color", program.input_color_record_ids))}
        yield normalize(_base_ir(row, program.pair_sequence))


def _typed_expression(expression: Any) -> bool:
    if not isinstance(expression, dict) or not isinstance(expression.get("opcode"), str):
        return False
    return all(_typed_expression(value) if isinstance(value, dict) else True for value in expression.values())


def check_node_semantics(node: dict[str, Any]) -> int:
    """Closed structural rules for the full C90 node vocabulary."""
    node_type = node.get("type")
    if node_type not in ALLOWED_NODES:
        raise ValueError(f"unrecognized or opaque IR node {node_type!r}")
    if node_type == "ATOM_TABLE":
        if node.get("order") != "FROZEN_LIST" or node.get("cardinality") != len(node.get("records", ())):
            raise ValueError("invalid ordered atom table")
        return int(node["cardinality"])
    if node_type == "ORDERED_RANGE":
        start, stop, step = (int(node[key]) for key in ("start", "stop", "step"))
        if step == 0 or (stop - start) * step < 0:
            raise ValueError("invalid ordered range")
        count = max(0, (abs(stop - start) + abs(step) - 1) // abs(step))
        if node.get("cardinality") != count: raise ValueError("range cardinality failure")
        return count
    if node_type == "ORDERED_UNION":
        children = node.get("children", ())
        if node.get("order") != "CONCATENATE" or node.get("cardinality") != sum(check_node_semantics(child) for child in children):
            raise ValueError("ordered-union theorem failure")
        if node.get("multiplicity") not in {"DISJOINT", "RETAINED"}: raise ValueError("union multiplicity policy missing")
        return int(node["cardinality"])
    if node_type == "CARTESIAN_PRODUCT":
        children = node.get("children", ())
        if node.get("rank") != "MIXED_RADIX_LAST_AXIS_FASTEST": raise ValueError("invalid mixed-radix rule")
        count = int(__import__("math").prod(check_node_semantics(child) for child in children))
        if node.get("cardinality") != count: raise ValueError("product cardinality theorem failure")
        return count
    if node_type == "FILTER":
        child_count = check_node_semantics(node["child"])
        selected = node.get("selected_ordinals", ())
        if not isinstance(node.get("predicate"), dict) or any(not isinstance(index, int) or index < 0 or index >= child_count for index in selected):
            raise ValueError("filter predicate or selected domain invalid")
        if list(selected) != sorted(set(selected)) or node.get("cardinality") != len(selected): raise ValueError("filter ordering failure")
        return int(node["cardinality"])
    if node_type == "PERMUTE":
        count = check_node_semantics(node["child"]); permutation = node.get("permutation", ())
        if sorted(permutation) != list(range(count)) or node.get("cardinality") != count: raise ValueError("permutation bijection failure")
        return count
    if node_type in {"GROUP_TEMPLATE", "ANCESTRY_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE"}:
        if not _typed_expression(node.get("expression")): raise ValueError("template lacks typed expression AST")
        return 1
    if node_type == "MAP_RECORD":
        count = check_node_semantics(node["child"])
        template_types = {item.get("type") for item in node.get("templates", ())}
        if template_types != {"GROUP_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE", "ANCESTRY_TEMPLATE"}:
            raise ValueError("record-template theorem coverage failure")
        for template in node["templates"]: check_node_semantics(template)
        if not _typed_expression(node.get("coefficient_expression")): raise ValueError("coefficient expression lacks typed AST")
        if node.get("cardinality") != count: raise ValueError("record-map cardinality failure")
        return count
    raise ValueError("unproved node semantics")


def check_proof(node: dict[str, Any]) -> dict[str, Any]:
    """Executable structural-induction checker for every C90 node type used by a program."""
    if node["type"] != "MAP_RECORD": raise ValueError("unproved top-level node")
    count = check_node_semantics(node)
    expected_root = sha({key: value for key, value in node.items() if key != "normal_form_root"})
    if expected_root != node.get("normal_form_root"):
        raise ValueError("normal-form root does not authenticate source order and records")
    return {"node_types": ("ATOM_TABLE", "CARTESIAN_PRODUCT", "MAP_RECORD", "GROUP_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE", "ANCESTRY_TEMPLATE"),
            "cardinality": count, "normal_form_root": node["normal_form_root"], "pass": True}


def _semantic_record(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    if a != b: raise ValueError("Route-A/Route-B normal form mismatch")
    proof = check_proof(a); pair = a["pair"]
    summary = {"logical_count": a["cardinality"], "first_semantic_record": sha({"pair": pair["id"], "ordinal": 0, "ir": a["normal_form_root"]}),
               "last_semantic_record": sha({"pair": pair["id"], "ordinal": a["cardinality"] - 1, "ir": a["normal_form_root"]}),
               "coordinate_count": a["cardinality"], "equivalence_count": a["cardinality"], "minimum_ordinal": 0, "maximum_ordinal": a["cardinality"] - 1,
               "status_counts": {"C82_INTERVAL_RULE_TEMPLATE": a["cardinality"]}, "expression_class_counts": {"C82_PROJECTED_COEFFICIENT_AST": a["cardinality"]},
               "witness_multiplicity_distribution": {"1": a["cardinality"]}, "ancestry_family_count": 1,
               "bound_envelope": "C82 propagated product-bound template"}
    body = {"kind": "FACTORIZED_SEMANTIC_PROGRAM_ROOT", "pair": pair, "normal_form_root": a["normal_form_root"], "primitive_roots": a["primitive_roots"], "summary": summary, "proof": proof}
    return {**body, "sha256": sha(body), "blake2b_256": b2(body)}


def compare_semantic_routes(resolution: str) -> Iterator[dict[str, Any]]:
    sentinel = object()
    for a, b in zip_longest(compile_route_a(resolution), compile_route_b(resolution), fillvalue=sentinel):
        if a is sentinel or b is sentinel: raise ValueError("Route-A/Route-B pair-domain length mismatch")
        yield _semantic_record(a, b)


def _root(entries: list[dict[str, Any]]) -> dict[str, str]:
    ordered = [{"pair": x["pair"], "sha256": x["sha256"], "blake2b_256": x["blake2b_256"]} for x in entries]
    return {"sha256": sha(ordered), "blake2b_256": b2(ordered)}


def build_semantic_ledger(output: Path, *, stop_after: int | None = None, resume: bool = False, parallel: bool = False, checkpoint_interval: int = 1024) -> dict[str, Any]:
    """Pair-atomic compact ledger writer; never expands a logical leaf stream."""
    output.mkdir(parents=True, exist_ok=True); ledger = output / "ledger.jsonl"; checkpoint = output / "checkpoint.json"
    start = 0
    rolling = ""
    if resume and checkpoint.exists():
        state = json.loads(checkpoint.read_text()); start = int(state["next_pair"])
        if state["inputs"] != frozen_inputs() or state["schema"] != SCHEMA: raise ValueError("checkpoint scientific inputs changed")
    elif not resume:
        ledger.write_text("")
    parallel_rows: dict[str, list[dict[str, Any]]] | None = None
    if parallel:
        if resume or stop_after is not None: raise ValueError("parallel semantic pass is clean-only")
        # Independent resolution ranges are computed concurrently; the
        # coordinator below remains the sole canonical-order ledger writer.
        with ThreadPoolExecutor(max_workers=len(RESOLUTION_ORDER)) as pool:
            futures = {resolution: pool.submit(lambda r=resolution: list(compare_semantic_routes(r))) for resolution in RESOLUTION_ORDER}
            parallel_rows = {resolution: futures[resolution].result() for resolution in RESOLUTION_ORDER}
    mode = "a" if start else "w"; completed = start; by_resolution: dict[str, list[dict[str, Any]]] = {r: [] for r in RESOLUTION_ORDER}
    if start:
        for line in ledger.read_text().splitlines():
            item = json.loads(line); by_resolution[item["pair"]["resolution"]].append(item)
            rolling = sha({"previous": rolling, "entry": item["sha256"]})
        if rolling != state["rolling_root"]: raise ValueError("checkpoint closed-ledger root mismatch")
    sequence = 0
    def close_checkpoint() -> None:
        handle.flush(); os.fsync(handle.fileno())
        temporary = checkpoint.with_suffix(".tmp")
        temporary.write_text(canonical({"schema": SCHEMA, "inputs": frozen_inputs(), "next_pair": sequence, "rolling_root": rolling}) + "\n")
        os.replace(temporary, checkpoint)
    with ledger.open(mode) as handle:
        for resolution in RESOLUTION_ORDER:
            iterator = iter(parallel_rows[resolution]) if parallel_rows is not None else compare_semantic_routes(resolution)
            for item in iterator:
                if sequence < start: sequence += 1; continue
                handle.write(canonical(item) + "\n")
                by_resolution[resolution].append(item); sequence += 1; completed += 1
                rolling = sha({"previous": rolling, "entry": item["sha256"]})
                if sequence % checkpoint_interval == 0: close_checkpoint()
                if stop_after is not None and completed >= stop_after:
                    close_checkpoint(); return {"interrupted": True, "next_pair": sequence, "ledger": str(ledger)}
        handle.flush(); os.fsync(handle.fileno())
    roots = {resolution: _root(by_resolution[resolution]) for resolution in RESOLUTION_ORDER}
    aggregate = _root([item for resolution in RESOLUTION_ORDER for item in by_resolution[resolution]])
    index = {"schema": SCHEMA, "status": STATUS, "inputs": frozen_inputs(), "ledger": "ledger.jsonl", "entries": sequence, "resolution_roots": roots, "aggregate": aggregate, "kind": "FACTORIZED_SEMANTIC_PROGRAM_ROOT"}
    (output / "index.json").write_text(canonical(index) + "\n"); checkpoint.unlink(missing_ok=True)
    return index


def verify_semantic_ledger(output: Path) -> dict[str, Any]:
    index = json.loads((output / "index.json").read_text()); entries = [json.loads(line) for line in (output / "ledger.jsonl").read_text().splitlines()]
    if len(entries) != index["entries"] or any(item["kind"] != "FACTORIZED_SEMANTIC_PROGRAM_ROOT" for item in entries): raise ValueError("invalid semantic ledger")
    if any(item["primitive_roots"] != index["inputs"] for item in entries): raise ValueError("ledger primitive-root mismatch")
    by_resolution = {resolution: [item for item in entries if item["pair"]["resolution"] == resolution] for resolution in RESOLUTION_ORDER}
    roots = {resolution: _root(by_resolution[resolution]) for resolution in RESOLUTION_ORDER}
    aggregate = _root([item for resolution in RESOLUTION_ORDER for item in by_resolution[resolution]])
    if roots != index["resolution_roots"] or aggregate != index["aggregate"]:
        raise ValueError("ledger root mismatch")
    return MappingProxyType({"entries": len(entries), "aggregate": index["aggregate"], "pass": True})


def load_verified_historical_semantic_attestation() -> Any:
    return immutable(dict(verify_semantic_ledger(RUNTIME / "pass_one")))


def _ledger_entry(pair_id: str, resolution: str) -> dict[str, Any]:
    verified = load_verified_historical_semantic_attestation()
    for line in (RUNTIME / "pass_one" / "ledger.jsonl").open():
        item = json.loads(line)
        if item["pair"]["id"] == pair_id and item["pair"]["resolution"] == resolution:
            return item
    raise KeyError(pair_id)


def historical_pair_program_root(pair_id: str, resolution: str) -> str:
    return _ledger_entry(pair_id, resolution)["normal_form_root"]


def historical_pair_summary(pair_id: str, resolution: str) -> Any:
    return MappingProxyType(_ledger_entry(pair_id, resolution)["summary"])


def historical_pair_record_count(pair_id: str, resolution: str) -> int:
    return int(_ledger_entry(pair_id, resolution)["summary"]["logical_count"])


def historical_pair_normal_form(pair_id: str, resolution: str) -> Any:
    for item in compile_route_a(resolution):
        if item["pair"]["id"] == pair_id:
            return immutable(item)
    raise KeyError(pair_id)


def unrank_historical_pair_record(pair_id: str, ordinal: int, resolution: str) -> Any:
    """Return one C88-compatible C89 record without a kernel value or full-domain rebuild."""
    from ..ifboundstream.core import unrank_pair_record
    for program in iterate_pair_programs(resolution):
        if program.pair_id == pair_id:
            return immutable(unrank_pair_record(program, ordinal))
    raise KeyError(pair_id)


def audit_historical_pair_records(pair_id: str, ordinal_ranges: tuple[tuple[int, int], ...], resolution: str) -> Any:
    """Bounded, pair-local historical record audit with no coefficient/kernel product."""
    limit = historical_pair_record_count(pair_id, resolution)
    records: list[dict[str, Any]] = []
    for start, stop in ordinal_ranges:
        if not (0 <= start <= stop <= limit): raise ValueError("audit range outside pair program")
        for ordinal in range(start, stop):
            records.append(dict(unrank_historical_pair_record(pair_id, ordinal, resolution)))
    return tuple(immutable(record) for record in records)


def verify_historical_semantic_attestation_root() -> Any:
    return load_verified_historical_semantic_attestation()["aggregate"]
