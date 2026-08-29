"""Independent current-descendant compiler for the C90 semantic IR.

This module intentionally never opens C90's runtime directory or imports a
C90 private compiler.  Its historical input is limited to C90's documented
public package API.  That boundary is audited before an exhaustive comparison
is attempted.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import blake2b, sha256
from itertools import zip_longest
import json
import math
import os
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterator

from ..ifboundrestart import load_verified_historical_semantic_attestation

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c91_ifequiv6"
STATUS = "C91_IFEQUIV6_PUBLIC_EQUIVALENCE_INCOMPLETE"
HISTORICAL_C82 = "8e47231ab565f0f729d335b39aa98881176ba166"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
UNKNOWN_C72 = "UNKNOWN_NOT_CLAIMED"
RESOLUTION_ORDER = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
# These immutable identifiers are part of the public C90 import contract.  A
# C91 compiler may target them, but cannot call C90's private implementation.
SCHEMA = "C90-C82-SEMANTIC-IR-V1"
NORMAL_FORM = "C90-NORMAL-FORM-V1"


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def sha(value: Any) -> str:
    return sha256(canonical(value).encode()).hexdigest()


def b2(value: Any) -> str:
    return blake2b(canonical(value).encode(), digest_size=32).hexdigest()


def immutable(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: immutable(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(immutable(item) for item in value)
    if isinstance(value, tuple): return tuple(immutable(item) for item in value)
    return value


def _read(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


@lru_cache(maxsize=1)
def current_descendant_inputs() -> MappingProxyType:
    """Freeze current public scientific roots without looking at C90 records."""
    c87 = _read("data/authority/c87_canonical_c72_color_authority/manifest.json")
    c77 = _read("data/runtime/c77_qgembed9/root.json")
    c78 = _read("data/runtime/c78_ifsupport2/root.json")
    c80 = _read("data/runtime/c80_ifkernel2/root.json")
    c82 = _read("data/runtime/c82_ifagg/root.json")
    return immutable({
        "current_source_commit": "ac622ab358b83f090717d7e7fa179b58f18f526d",
        "environment": ENVIRONMENT,
        "historical_C82": HISTORICAL_C82,
        "historical_C72_runtime_instance": UNKNOWN_C72,
        "C87_scientific": c87["scientific_root"],
        "C87_capsule": c87["compatibility_root"],
        "C77": c77["aggregate_sha256"],
        "C78": c78["aggregate_sha256"],
        "C80": c80["index_sha256"],
        "C82": c82["index_sha256"],
        "C88_schema": "2f6268aaa6338afa0c108b2d037c6d396be31b67ca65cec10aa1f4f3d0f623a8",
        "semantic_ir": SCHEMA,
        "normal_form": NORMAL_FORM,
    })


def historical_public_api_audit() -> MappingProxyType:
    """Prove whether C90's public API can enumerate historical pair authority."""
    import deuteron_wigner.bridge.ifboundrestart as public
    authority = load_verified_historical_semantic_attestation()
    names = tuple(public.__all__)
    required = {
        "iter_historical_pair_attestations",
        "historical_pair_attestation_page",
        "historical_pair_identifiers",
        "check_historical_expansion_equivalence",
    }
    available = sorted(required.intersection(names))
    missing = sorted(required.difference(names))
    return immutable({
        "authority_verified": bool(authority["pass"]),
        "historical_aggregate": authority["aggregate"],
        "public_operations": names,
        "required_complete_domain_operations": sorted(required),
        "available_complete_domain_operations": available,
        "missing_complete_domain_operations": missing,
        "complete_historical_pair_domain_available": not missing,
        "blocker": "C90_PUBLIC_API_MISSES_AUTHENTICATED_PAIR_ENUMERATION_AND_EXPORTED_EXPANSION_PROOF_CHECKER" if missing else None,
        "private_C90_runtime_opened": False,
        "historical_compiler_called": False,
    })


def _descendant_structural_check(program: dict[str, Any]) -> dict[str, Any]:
    """Independent preflight only; it is not the unexported C90 theorem."""
    child = program["child"]
    if child["type"] != "CARTESIAN_PRODUCT" or child["rank"] != "MIXED_RADIX_LAST_AXIS_FASTEST":
        raise ValueError("descendant mixed-radix semantic defect")
    cardinality = math.prod(axis["cardinality"] for axis in child["children"])
    if cardinality != child["cardinality"] or cardinality != program["cardinality"]:
        raise ValueError("descendant cardinality defect")
    if any(axis["type"] != "ATOM_TABLE" or axis["cardinality"] != len(axis["records"]) for axis in child["children"]):
        raise ValueError("descendant ordered-atom defect")
    if {template["type"] for template in program["templates"]} != {"GROUP_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE", "ANCESTRY_TEMPLATE"}:
        raise ValueError("descendant template defect")
    return {"independent_descendant_preflight": True, "cardinality": cardinality}


def verify_historical_authority_public_boundary() -> MappingProxyType:
    """Verify C90 only through public calls; fail without touching private payloads."""
    audit = historical_public_api_audit()
    if not audit["authority_verified"]:
        raise ValueError("C90 public historical attestation did not verify")
    return audit


@lru_cache(maxsize=None)
def _c78_payload(resolution: str) -> dict[str, Any]:
    return _read(f"data/runtime/c78_ifsupport2/{resolution}.json")


def _descendant_rows(resolution: str) -> Iterator[dict[str, Any]]:
    """Current C78/C82 semantics, constructed directly and independently."""
    payload = _c78_payload(resolution)
    emission = {row["id"]: row for row in payload["emission_edges"]}
    absorption = {row["id"]: row for row in payload["absorption_edges"]}
    for group in payload["witness_groups"]:
        for emission_id in group["emission_endpoint_ids"]:
            for absorption_id in group["absorption_endpoint_ids"]:
                output, input_ = emission[emission_id], absorption[absorption_id]
                output_domain = payload["emission_path_domains"][emission_id]
                input_domain = payload["absorption_path_domains"][absorption_id]
                yield {
                    "resolution": resolution,
                    "pair_id": f"{output['physical_qg_id']}|{input_['physical_qg_id']}",
                    "bra": output["physical_qg_id"], "ket": input_["physical_qg_id"],
                    "witness": {"intermediate": group["intermediate_q_id"], "emission": emission_id, "absorption": absorption_id,
                                "source_order": ("b_dagger", "a_dagger", "a", "b")},
                    "axes": (("output_component", tuple(output_domain["component_ids"])),
                             ("output_color", tuple(output_domain["color_record_ids"])),
                             ("input_component", tuple(input_domain["component_ids"])),
                             ("input_color", tuple(input_domain["color_record_ids"]))),
                }


def _descendant_ir(row: dict[str, Any], sequence: int) -> dict[str, Any]:
    axes = [{"type": "ATOM_TABLE", "table": f"C78:{name}", "order": "FROZEN_LIST", "records": list(values), "cardinality": len(values),
             "first_ordinal": 0, "last_ordinal": len(values) - 1, "record_schema": "FROZEN_SCIENTIFIC_IDENTIFIER_V1"}
            for name, values in row["axes"]]
    cardinality = math.prod(axis["cardinality"] for axis in axes)
    product = {"type": "CARTESIAN_PRODUCT", "axis_order": [axis["table"].removeprefix("C78:") for axis in axes], "children": axes,
               "cardinality": cardinality, "rank": "MIXED_RADIX_LAST_AXIS_FASTEST", "record_schema": "C82_WITNESS_LEAF_TUPLE_V1",
               "first_ordinal": 0, "last_ordinal": cardinality - 1}
    program = {"type": "MAP_RECORD", "schema": "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1",
               "pair": {"sequence": sequence, "resolution": row["resolution"], "id": row["pair_id"], "bra": row["bra"], "ket": row["ket"]},
               "child": product,
               "templates": [
                   {"type": "GROUP_TEMPLATE", "expression": {"opcode": "GROUP_BY_EXACT_COORDINATE", "operands": ["ordered_raw_color_tuple"], "coalescing": "NONE"}},
                   {"type": "BOUND_TEMPLATE", "expression": {"opcode": "C82_PROPAGATED_PRODUCT_BOUND", "operands": ["C77_bounds", "color_bounds"]}},
                   {"type": "STATUS_TEMPLATE", "expression": {"opcode": "INTERVAL_NONZERO_RULE", "operands": ["midpoint", "bound"]}},
                   {"type": "ANCESTRY_TEMPLATE", "expression": {"opcode": "ORDERED_ANCESTRY", "operands": ["witness", "endpoint", "component", "color"]}, "witness": row["witness"]},
               ],
               "coefficient_expression": {"opcode": "MULTIPLY", "operands": [
                   {"opcode": "CONJUGATE", "operand": {"opcode": "MULTIPLY", "operands": ["C77COMP_bra", "U3_bra"]}},
                   {"opcode": "MULTIPLY", "operands": ["C77COMP_ket", "U3_ket"]},
               ]},
               "ownership": "C82 embedding/metric/conjugation; C80 owns W3/g_s2",
               "forbids": ["C80 numerical kernel", "g_s_squared", "coefficient_times_kernel"],
               "normal_form": NORMAL_FORM, "primitive_roots": dict(current_descendant_inputs()), "cardinality": cardinality,
               "first_ordinal": 0, "last_ordinal": cardinality - 1,
               "scientific_field_schema": "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1"}
    program["normal_form_root"] = sha({key: value for key, value in program.items() if key != "normal_form_root"})
    _descendant_structural_check(program)
    return program


def compile_descendant_programs(resolution: str) -> Iterator[dict[str, Any]]:
    for sequence, row in enumerate(_descendant_rows(resolution)):
        yield _descendant_ir(row, sequence)


def _summary(program: dict[str, Any]) -> dict[str, Any]:
    count = program["cardinality"]; pair = program["pair"]
    return {"logical_count": count, "minimum_ordinal": 0, "maximum_ordinal": count - 1,
            "first_semantic_record": sha({"pair": pair["id"], "ordinal": 0, "ir": program["normal_form_root"]}),
            "last_semantic_record": sha({"pair": pair["id"], "ordinal": count - 1, "ir": program["normal_form_root"]}),
            "coordinate_count": count, "equivalence_count": count,
            "status_counts": {"C82_INTERVAL_RULE_TEMPLATE": count},
            "expression_class_counts": {"C82_PROJECTED_COEFFICIENT_AST": count},
            "witness_multiplicity_distribution": {"1": count}, "ancestry_family_count": 1,
            "bound_envelope": "C82 propagated product-bound template"}


def _entry(program: dict[str, Any]) -> dict[str, Any]:
    body = {"kind": "DESCENDANT_FACTORIZED_SEMANTIC_PROGRAM_ROOT", "pair": program["pair"],
            "normal_form_root": program["normal_form_root"], "primitive_roots": program["primitive_roots"],
            "summary": _summary(program), "proof": _descendant_structural_check(program)}
    return {**body, "sha256": sha(body), "blake2b_256": b2(body)}


def _root(entries: list[dict[str, Any]]) -> dict[str, str]:
    payload = [{"pair": entry["pair"], "sha256": entry["sha256"], "blake2b_256": entry["blake2b_256"]} for entry in entries]
    return {"sha256": sha(payload), "blake2b_256": b2(payload)}


def build_descendant_ledger(output: Path) -> dict[str, Any]:
    """Build a compact descendant ledger only; no historical pair data is read."""
    output.mkdir(parents=True, exist_ok=True)
    entries_by_resolution = {resolution: [] for resolution in RESOLUTION_ORDER}
    ledger = output / "ledger.jsonl"
    with ledger.open("w") as handle:
        for resolution in RESOLUTION_ORDER:
            for program in compile_descendant_programs(resolution):
                entry = _entry(program); entries_by_resolution[resolution].append(entry)
                handle.write(canonical(entry) + "\n")
        handle.flush(); os.fsync(handle.fileno())
    resolution_roots = {resolution: _root(entries_by_resolution[resolution]) for resolution in RESOLUTION_ORDER}
    aggregate = _root([entry for resolution in RESOLUTION_ORDER for entry in entries_by_resolution[resolution]])
    index = {"schema": SCHEMA, "normal_form": NORMAL_FORM, "status": STATUS, "inputs": dict(current_descendant_inputs()),
             "entries": sum(len(entries) for entries in entries_by_resolution.values()), "ledger": "ledger.jsonl",
             "resolution_roots": resolution_roots, "aggregate": aggregate}
    (output / "index.json").write_text(canonical(index) + "\n")
    return index


def load_verified_descendant_ledger(output: Path = RUNTIME / "descendant") -> MappingProxyType:
    index = json.loads((output / "index.json").read_text())
    entries = [json.loads(line) for line in (output / "ledger.jsonl").read_text().splitlines()]
    if len(entries) != index["entries"] or len(entries) != 154830: raise ValueError("invalid descendant ledger census")
    by_resolution = {resolution: [entry for entry in entries if entry["pair"]["resolution"] == resolution] for resolution in RESOLUTION_ORDER}
    roots = {resolution: _root(by_resolution[resolution]) for resolution in RESOLUTION_ORDER}
    aggregate = _root([entry for resolution in RESOLUTION_ORDER for entry in by_resolution[resolution]])
    if roots != index["resolution_roots"] or aggregate != index["aggregate"]: raise ValueError("descendant ledger root mismatch")
    return immutable({"entries": len(entries), "aggregate": aggregate, "resolution_roots": roots, "pass": True})
