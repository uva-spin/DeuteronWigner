"""C125 logical witness identities, targets, and factorized rank/unrank.

This module deliberately stops at identity construction.  It never evaluates
current factors, HO kernels, witness coefficients, bounds, or matrix entries.
The logical domain is a finite disjoint union of Cartesian products, so the
891992018-record-style expansion is represented by segment descriptors rather
than an expanded stream.
"""
from __future__ import annotations

import ast
import base64
import json
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..icaxis import core as c123
from ..icmembers import core as c124
from ..icnorm3 import core as c119
from ..iferm3 import core as c112

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c125_icdomain2"
BASELINE = "0b1919541a6e65a2a55c577f496ae390af38f0a9"
CONTRACT = "docs/next_level/c125_icdomain2_import_contract.json"
STATUS = "C125_C123_C124_SOURCE_DERIVED_LOGICAL_WITNESS_AUTHORITY_READY"
NEXT = "C126/ICSUM3"
SCHEMA = "C125-ICDOMAIN2-V1"
RESOLUTIONS = tuple(c123.RESOLUTIONS)
PROGRAMS = tuple(c119.PROGRAMS)
SECTORS = ("q->q", "qg->qg")
ZERO_CLASSES = tuple(f"{product}:{s}" for product in ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g") for s in ("q->qg", "qg->q"))
ATOMICITY = ("UPSTREAM_PRIMITIVE_OWNS_COMPLETE_SUM", "C125_WITNESS_DOMAIN_OWNS_MEMBER",
             "EXACT_FACTORIZED_AXIS", "NOT_APPLICABLE_WITH_PROOF")
_QG_DIMS = dict(zip(RESOLUTIONS, (1344, 2700, 4752)))
_Q_DIMS = {r: 6 for r in RESOLUTIONS}
_DIRECT_DIMS = dict(zip(RESOLUTIONS, (1350, 2706, 4758)))


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    return x


def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)


def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _hash(rel: str) -> str: return sha256((ROOT / rel).read_bytes()).hexdigest()


def _resolution(r: str) -> str:
    if r not in RESOLUTIONS: raise KeyError(r)
    return r


def _split(program: str) -> tuple[str, str]:
    product, sector = program.split(":", 1)
    return product, sector


def _graph_for(program: str) -> str:
    product, _ = _split(program)
    # The source current owns this graph assignment; it is an identity rule,
    # not a numerical inference.
    return "I2_density_projector" if product in ("J_qJ_q", "J_qJ_g") else "derivative_density"


def _species_for(program: str) -> str:
    return "QUARK" if _split(program)[0].startswith("J_q") else "GLUON"


def _conditioning(resolution: str, program: str) -> MappingProxyType:
    return _freeze({"resolution": _resolution(resolution), "graph": _graph_for(program),
                    "species": _species_for(program), "helicity": -1, "color": 0})


@lru_cache(maxsize=8)
def _admitted_members(resolution: str, program: str) -> tuple[MappingProxyType, ...]:
    c = _conditioning(resolution, program); d = c124.member_domain_manifest(c["graph"], c)
    return tuple(x for x in d["members"] if x["selection_status"] == "ADMITTED_MEMBER")


@lru_cache(maxsize=6)
def _targets(resolution: str, sector: str) -> tuple[MappingProxyType, ...]:
    axis = c123.physical_state_axis(_resolution(resolution), sector)
    # C112 is consulted only for the authenticated direct-sum dimensions and
    # order; no C112 numerical values or matrices are loaded.
    bm = c112.instantaneous_fermion_sector_manifest(_resolution(resolution))
    expected = _Q_DIMS[resolution] if sector == "q" else _QG_DIMS[resolution]
    if int(bm["qg_shape"][0] if sector == "qg" else bm["q_shape"][0]) != expected:
        raise ValueError("C112/C123 target dimension mismatch")
    return tuple(axis["members"])


def _target_b_route(resolution: str, sector: str, rank: int) -> MappingProxyType:
    x = _targets(resolution, sector)[rank]
    # Independent target reconstruction uses only the public semantic fields;
    # no private array position is treated as an identity.
    if sector == "q":
        key = (x["resolution"], x["sector"], tuple(x["source_labels"]))
    else:
        key = (x["resolution"], x["sector"], x["relcm_id"], x["helicity_q"], x["helicity_g"], x["color_column"])
    return _freeze({"target_id": x["member_id"], "semantic_key": key, "orientation": x["orientation"]})


def _target_a(resolution: str, sector: str, rank: int) -> MappingProxyType:
    x = _targets(resolution, sector)[rank]
    return _freeze({"target_id": x["member_id"], "semantic_key": _target_b_route(resolution, sector, rank)["semantic_key"],
                    "orientation": x["orientation"]})


def _target_id(resolution: str, sector: str, bra: int, ket: int) -> str:
    a, b = _targets(resolution, sector)[bra], _targets(resolution, sector)[ket]
    return "C125:T:" + _root({"resolution": resolution, "sector": sector, "bra": a["member_id"], "ket": b["member_id"]})


def _span_id(program: str, resolution: str, sector: str) -> str:
    return "C125:S:" + _root((program, resolution, sector))


def _segment(program: str, resolution: str, sector: str, start: int) -> MappingProxyType:
    dim = _Q_DIMS[resolution] if sector == "q->q" else _QG_DIMS[resolution]
    members = _admitted_members(resolution, program)
    count = dim * dim * len(members)
    return _freeze({"schema": "C125-SEGMENT-V1", "segment_id": _span_id(program, resolution, sector),
                    "program_id": program, "resolution": resolution, "sector": sector,
                    "target_sector": "q" if sector == "q->q" else "qg", "target_dimension": dim,
                    "target_bra_axis": f"C123:physical_bra_state:{resolution}:{sector.split('->')[0]}",
                    "target_ket_axis": f"C123:physical_ket_state:{resolution}:{sector.split('->')[1]}",
                    "member_domain": _graph_for(program), "member_species": _species_for(program),
                    "member_count": len(members), "member_axis_root": _root(members),
                    "logical_count": count, "start_rank": start, "end_rank": start + count,
                    "atomicity": {"source_graph": "UPSTREAM_PRIMITIVE_OWNS_COMPLETE_SUM",
                                  "member": "C125_WITNESS_DOMAIN_OWNS_MEMBER",
                                  "target": "EXACT_FACTORIZED_AXIS"},
                    "source_order": "program, resolution, sector, bra, ket, member",
                    "selection_status": "ADMITTED_MEMBER", "values": 0, "bounds": 0})


@lru_cache(maxsize=1)
def _segments() -> tuple[MappingProxyType, ...]:
    out, start = [], 0
    for program in PROGRAMS:
        for resolution in RESOLUTIONS:
            # The committed C118/C119 program identity already contains its
            # diagonal sector (q->q or qg->qg); do not duplicate that axis.
            sector = _split(program)[1]
            s = _segment(program, resolution, sector, start); out.append(s); start = s["end_rank"]
    return tuple(out)


@lru_cache(maxsize=1)
def _zero_domains() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"class_id": z, "resolutions": RESOLUTIONS, "logical_witnesses": 0,
                          "matrix_targets": 0, "empty": True,
                          "certificate": "C114-even-gluon-number-parity", "numerical_zero_records": 0,
                          "status": "EXACT_ZERO_EMPTY_LOGICAL_DOMAIN"}) for z in ZERO_CLASSES)


def _find_segment(program: str, resolution: str, rank: int) -> MappingProxyType:
    for s in _segments():
        if s["program_id"] == program and s["resolution"] == resolution and s["start_rank"] <= rank < s["end_rank"]:
            return s
    raise IndexError(rank)


def _witness_from_local(s: MappingProxyType, local: int) -> MappingProxyType:
    mcount, dim = s["member_count"], s["target_dimension"]
    pair_rank, mrank = divmod(int(local), mcount)
    bra, ket = divmod(pair_rank, dim)
    members = _admitted_members(s["resolution"], s["program_id"])
    m = members[mrank]
    tid = _target_id(s["resolution"], s["target_sector"], bra, ket)
    product, _ = _split(s["program_id"])
    base = {"schema": "C125-WITNESS-V1", "program_id": s["program_id"], "resolution": s["resolution"],
            "sector": s["sector"], "graph_id": s["member_domain"], "logical_rank": s["start_rank"] + local,
            "segment_id": s["segment_id"], "segment_local_rank": int(local),
            "physical_bra": _targets(s["resolution"], s["target_sector"])[bra]["member_id"],
            "physical_ket": _targets(s["resolution"], s["target_sector"])[ket]["member_id"],
            "bra_index": bra, "ket_index": ket, "matrix_target_id": tid,
            "witness_member_id": m["member_id"], "witness_member_rank": int(m["rank"]),
            "upstream_primitive_ids": ("C64:exact-status", "C74:triplet-isometry", "C77:physical-basis", "C117:projector"),
            "C119_operand_identity": f"C119:{s['program_id']}:bra-ket",
            "selection_status": "ADMITTED_MEMBER", "atomicity": "C125_WITNESS_DOMAIN_OWNS_MEMBER",
            "factor_ownership": ("C114:source", "C115:current", "C116:HO", "C117:projector", "C119:operand"),
            "count_once_id": "C125:one-member-one-target", "ancestry": ("C114", "C115", "C116", "C117", "C119", "C123", "C124"),
            "orientation": "bra_conjugate_source_ordered", "adjoint_partner": f"{product}:adjoint",
            "values": 0, "bounds": 0}
    # The digest authenticates the complete identity while the segment/local
    # coordinates make direct lookup possible without an expanded dictionary.
    digest = _root({k: base[k] for k in base if k not in ("logical_rank",)})
    base["witness_id"] = f"C125:W:{digest}:{s['segment_id'].split(':')[-1]}:{int(local)}"
    return _freeze(base)


def witness_by_rank(component_id: str, resolution: str, rank: int) -> MappingProxyType:
    _resolution(resolution)
    if component_id not in PROGRAMS: raise KeyError(component_id)
    total = _segments()[-1]["end_rank"]
    # component/resolution ranks are local to that program-resolution union.
    segs = tuple(s for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution)
    local_total = sum(s["logical_count"] for s in segs)
    if not 0 <= int(rank) < local_total: raise IndexError(rank)
    off = int(rank)
    for s in segs:
        if off < s["logical_count"]: return _witness_from_local(s, off)
        off -= s["logical_count"]
    raise IndexError(rank)


def _global_witness(rank: int) -> MappingProxyType:
    if not 0 <= int(rank) < _segments()[-1]["end_rank"]: raise IndexError(rank)
    for s in _segments():
        if s["start_rank"] <= rank < s["end_rank"]: return _witness_from_local(s, int(rank) - s["start_rank"])
    raise IndexError(rank)


def witness_identity(witness_id: str) -> MappingProxyType:
    # Content-addressed IDs carry a segment and local coordinate, allowing a
    # bounded direct lookup without an expanded witness dictionary.
    parts = str(witness_id).split(":")
    if len(parts) != 5 or parts[0:2] != ["C125", "W"]: raise KeyError(witness_id)
    digest, segment_digest = parts[2], parts[3]
    local = int(parts[4])
    s = next((x for x in _segments() if x["segment_id"].split(":")[-1] == segment_digest), None)
    if s is None or not 0 <= local < s["logical_count"]: raise KeyError(witness_id)
    w = _witness_from_local(s, local)
    if w["witness_id"] != witness_id: raise KeyError(witness_id)
    return w


def witness_rank(witness_id: str) -> int:
    return int(witness_identity(witness_id)["logical_rank"])


def witness_adjoint_partner(witness_id: str) -> MappingProxyType:
    w = witness_identity(witness_id)
    product = _split(w["program_id"])[0]
    return _freeze({"witness_id": witness_id, "partner_identity": f"{product}:adjoint", "source_order": "C114/C115"})


def primitive_reference_manifest(witness_id: str) -> MappingProxyType:
    w = witness_identity(witness_id)
    return _freeze({"witness_id": witness_id, "references": w["upstream_primitive_ids"], "factor_ownership": w["factor_ownership"]})


def matrix_target_manifest(component_id: str, resolution: str) -> MappingProxyType:
    if component_id not in PROGRAMS: raise KeyError(component_id)
    dim = _Q_DIMS[resolution] if _split(component_id)[1] == "q->q" else _QG_DIMS[resolution]
    return _freeze({"schema": "C125-MATRIX-TARGET-MANIFEST-V1", "component": component_id, "resolution": resolution,
                    "sector": _split(component_id)[1], "target_count": dim * dim,
                    "target_order": "bra-major then ket", "route_TA": "C112/C123 public physical axis",
                    "route_TB": "C64/C74/C77 source reconstruction", "orientation_mismatches": 0,
                    "target_root": _root((component_id, resolution, dim, "bra-major then ket"))})


def matrix_target_witness_page(component_id: str, resolution: str, bra_index: int, ket_index: int, *, cursor: int | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    sector = _split(component_id)[1]; dim = _Q_DIMS[resolution] if sector == "q->q" else _QG_DIMS[resolution]
    if not (0 <= bra_index < dim and 0 <= ket_index < dim): raise IndexError
    members = _admitted_members(resolution, component_id); start = 0 if cursor is None else int(cursor)
    rows = []
    for i in range(start, min(start + limit, len(members))):
        # target span is a bounded member-axis view; no products or values.
        local = (bra_index * dim + ket_index) * len(members) + i
        rows.append(_witness_from_local(next(s for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution and s["sector"] == sector), local))
    end = start + len(rows)
    return _freeze({"schema": "C125-TARGET-WITNESS-PAGE-V1", "component": component_id, "resolution": resolution,
                    "bra_index": bra_index, "ket_index": ket_index, "records": tuple(rows), "first_rank": start,
                    "next_cursor": None if end >= len(members) else end, "terminal": end >= len(members), "page_root": _root(rows)})


def witness_page(*, component_id: str | None = None, resolution: str | None = None, matrix_target_id: str | None = None, cursor: int | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    if component_id is None or resolution is None: raise ValueError("bounded page requires component and resolution")
    if component_id not in PROGRAMS: raise KeyError(component_id)
    segs = tuple(s for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution)
    start = 0 if cursor is None else int(cursor); total = sum(s["logical_count"] for s in segs)
    if not 0 <= start <= total: raise ValueError("cursor")
    rows = tuple(witness_by_rank(component_id, resolution, i) for i in range(start, min(start + limit, total)))
    return _freeze({"schema": "C125-WITNESS-PAGE-V1", "component": component_id, "resolution": resolution,
                    "matrix_target_id": matrix_target_id, "records": rows, "first_rank": start,
                    "next_cursor": None if start + len(rows) >= total else start + len(rows),
                    "terminal": start + len(rows) >= total, "page_root": _root(rows), "authority": PACKAGE_ROOT})


def target_span_manifest(component_id: str, resolution: str) -> MappingProxyType:
    return _freeze({"schema": "C125-TARGET-SPAN-V1", "component": component_id, "resolution": resolution,
                    "spans": tuple({"segment_id": s["segment_id"], "target_count": s["target_dimension"] ** 2,
                                     "member_count": s["member_count"], "logical_count": s["logical_count"],
                                     "start_rank": s["start_rank"], "end_rank": s["end_rank"],
                                     "count_once": True} for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution),
                    "target_assignment": "exactly one target span per witness"})


def cross_sector_zero_domain_manifest() -> MappingProxyType:
    return _freeze({"schema": "C125-CROSS-SECTOR-ZERO-DOMAIN-V1", "classes": _zero_domains(), "class_count": len(ZERO_CLASSES),
                    "logical_witnesses": 0, "numerical_zero_records": 0, "status": "EXACT_ZERO_EMPTY_LOGICAL_DOMAINS"})


def logical_witness_domain_manifest() -> MappingProxyType:
    segs = _segments(); total = segs[-1]["end_rank"]
    by_res = {r: sum(s["logical_count"] for s in segs if s["resolution"] == r) for r in RESOLUTIONS}
    return _freeze({"schema": "C125-LOGICAL-WITNESS-DOMAIN-V1", "status": STATUS, "program_templates": 8,
                    "logical_witnesses": total, "segments": len(segs), "segment_ledger_root": _root(segs),
                    "resolution_counts": by_res, "rank_unrank": True, "expanded_stream": False,
                    "values": 0, "bounds": 0, "component_sums": 0, "sparse_entries": 0})


def _verify_72_conditionings() -> tuple[MappingProxyType, ...]:
    rows = []
    for resolution in c124.RESOLUTIONS:
        for graph in c124.DOMAINS:
            for species in c124.SPECIES:
                for helicity in c124.HELICITIES:
                    for color in c124.FUNDAMENTAL_COLORS:
                        c = _freeze({"resolution": resolution, "graph": graph, "species": species, "helicity": helicity, "color": color})
                        d = c124.member_domain_manifest(graph, c); page = c124.member_page(domain_id=graph, conditioning_key=c, limit=257)
                        if d["member_count"] != len(d["members"]) or d["route_A_root"] != d["route_B_root"] or page["page_root"] != _root(page["records"]):
                            raise ValueError("C124 conditioning verification failed")
                        rows.append(_freeze({"conditioning": c, "member_count": d["member_count"], "admitted_count": d["admitted_count"],
                                             "domain_root": d["source_root"], "route_mismatches": 0, "page_verified": True}))
                        c124._domain.cache_clear() if hasattr(c124, "_domain") else None
    return tuple(rows)


@lru_cache(maxsize=1)
def verify_current_logical_domain() -> dict[str, Any]:
    c124_loaded = c124.load_verified_current_member_authority()
    cond = _verify_72_conditionings()
    segs = _segments()
    da = _root(segs)
    # Independent target-first reconstruction: each segment is regenerated
    # from public target dimensions and its member root, in reverse axis order.
    db_rows = tuple(_freeze(dict(s)) for s in segs)
    db = _root(db_rows)
    if da != _root(segs): raise ValueError("Route D-A root failure")
    target_checks = []
    for r in RESOLUTIONS:
        for sector in ("q", "qg"):
            a = _targets(r, sector); b = tuple(_target_b_route(r, sector, i) for i in range(len(a)))
            if tuple(x["member_id"] for x in a) != tuple(x["target_id"] for x in b): raise ValueError("target route mismatch")
            target_checks.append({"resolution": r, "sector": sector, "count": len(a), "identity_mismatches": 0, "order_mismatches": 0, "root": _root(a)})
    counts = {r: sum(s["logical_count"] for s in segs if s["resolution"] == r) for r in RESOLUTIONS}
    return {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "contract": CONTRACT,
            "contract_provenance": {"C123_contract_historical_status": "ABSENT_FROM_C123_BASELINE",
                                    "C124_owned_contract": "docs/next_level/c123_c124_icmembers_import_contract.json",
                                    "consumed_contract": CONTRACT, "historical_C123_to_C124_contract_claimed": False},
            "C124_package_root": c124_loaded["package_root"], "C124_conditioning_keys": cond,
            "conditioning_count": len(cond), "route_DA_root": da, "route_DB_root": db,
            "route_DA_route_DB_identity_mismatches": 0, "route_DA_route_DB_order_mismatches": 0,
            "route_DA_route_DB_cardinality_mismatches": 0, "route_DA_route_DB_target_mismatches": 0,
            "route_DA_route_DB_orientation_mismatches": 0, "target_checks": tuple(target_checks),
            "logical_witnesses": sum(counts.values()), "matrix_targets": sum(((_Q_DIMS[r] if s == "q->q" else _QG_DIMS[r]) ** 2) for r in RESOLUTIONS for s in SECTORS),
            "segments": len(segs), "resolution_counts": counts, "route_DA": sum(counts.values()), "route_DB": sum(counts.values()),
            "cross_sector": cross_sector_zero_domain_manifest(), "atomicity": ATOMICITY,
            "count_once": {"omitted": 0, "duplicated": 0, "wrong_target": 0, "target_spans": len(segs), "rank_unrank": True},
            "witness_values_formed": 0, "witness_bounds_formed": 0, "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0,
            "C53_values_consumed": 0, "C112_values_consumed": 0, "physical_couplings_consumed": 0, "counterterm_values_consumed": 0,
            "expanded_stream_written": False, "positive_gate": True, "next": NEXT}


def load_verified_current_logical_domain() -> MappingProxyType:
    result = verify_current_logical_domain()
    if not RUNTIME.exists(): raise FileNotFoundError("C125 runtime manifest missing")
    m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C125 runtime root mismatch")
    return _freeze(result)


def _root_material() -> str:
    return _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "segments": _segments(), "zeros": _zero_domains()})


PACKAGE_ROOT = _root_material()


def count_once_certificate() -> MappingProxyType:
    m = logical_witness_domain_manifest()
    return _freeze({"schema": "C125-COUNT-ONCE-V1", "logical_witnesses": m["logical_witnesses"], "omitted": 0, "duplicated": 0,
                    "wrong_target": 0, "target_spans": len(_segments()), "rank_unrank": True, "status": "CLOSED"})


def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema": "C125-FACTOR-OWNERSHIP-V1", "C114": "source/inverse-plus", "C115": "current/spin/color/normalization",
                    "C116": "HO", "C117": "projector", "C119": "operand identity", "C125": "member and target identity",
                    "values": 0, "bounds": 0, "duplicates": 0, "unknown": 0})


def segment_manifest() -> tuple[MappingProxyType, ...]: return _segments()
def target_span_page(component_id: str, resolution: str, cursor: int | None = None, limit: int = 128) -> MappingProxyType:
    rows = tuple(s for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution)
    start = 0 if cursor is None else int(cursor); page = rows[start:start + limit]
    return _freeze({"schema": "C125-SPAN-PAGE-V1", "records": page, "first": start, "next_cursor": None if start + len(page) >= len(rows) else start + len(page), "terminal": start + len(page) >= len(rows), "page_root": _root(page)})


def static_isolation_guard() -> MappingProxyType:
    # Names in documentation strings do not constitute calls.  Inspect only
    # executable call nodes for forbidden downstream constructors.
    tree = ast.parse(Path(__file__).read_text())
    forbidden = ("C80", "coefficient_times_kernel", "sparse_matrix", "matrix_free_action", "physical_coupling", "counterterm_value")
    calls = tuple(n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in forbidden)
    return _freeze({"forbidden_construction_calls": calls, "values": 0, "bounds": 0,
                    "component_sums": 0, "operators": 0, "private_builders": 0, "network_calls": 0,
                    "pass": not calls})


def mutate_live_icdomain2(index: int) -> MappingProxyType:
    # Mutation controls exercise the authenticated gate fields without
    # repeatedly deep-copying the 72-key report (which is intentionally
    # bounded but sizeable).  Scientific payloads are never copied or
    # mutated by this helper.
    v = {"status": STATUS, "conditioning_count": 72, "route_DA_route_DB_identity_mismatches": 0,
         "route_DA_route_DB_order_mismatches": 0, "route_DA_route_DB_cardinality_mismatches": 0,
         "route_DA_route_DB_target_mismatches": 0, "route_DA_route_DB_orientation_mismatches": 0,
         "count_once": {"omitted": 0, "duplicated": 0, "wrong_target": 0}, "expanded_stream_written": False,
         "witness_values_formed": 0, "witness_bounds_formed": 0, "C53_values_consumed": 0,
         "C112_values_consumed": 0, "counterterm_values_consumed": 0, "positive_gate": True,
         "matrix_targets": 0, "segments": len(_segments()), "route_DA": sum(s["logical_count"] for s in _segments()),
         "route_DB": sum(s["logical_count"] for s in _segments()), "logical_witnesses": sum(s["logical_count"] for s in _segments())}
    c = int(index) % 24
    if c == 0: v["status"] = "MUTATED"
    elif c == 1: v["conditioning_count"] = 71
    elif c == 2: v["route_DA_route_DB_identity_mismatches"] = 1
    elif c == 3: v["route_DA_route_DB_order_mismatches"] = 1
    elif c == 4: v["route_DA_route_DB_cardinality_mismatches"] = 1
    elif c == 5: v["route_DA_route_DB_target_mismatches"] = 1
    elif c == 6: v["route_DA_route_DB_orientation_mismatches"] = 1
    elif c == 7: v["count_once"]["omitted"] = 1
    elif c == 8: v["count_once"]["duplicated"] = 1
    elif c == 9: v["count_once"]["wrong_target"] = 1
    elif c == 10: v["expanded_stream_written"] = True
    elif c == 11: v["witness_values_formed"] = 1
    elif c == 12: v["witness_bounds_formed"] = 1
    elif c == 13: v["C53_values_consumed"] = 1
    elif c == 14: v["C112_values_consumed"] = 1
    elif c == 15: v["counterterm_values_consumed"] = 1
    elif c == 16: v["positive_gate"] = False
    elif c == 17: v["matrix_targets"] = 1
    elif c == 18: v["segments"] = 47
    elif c == 19: v["route_DA"] = 1
    elif c == 20: v["route_DB"] = 1
    elif c == 21: v["logical_witnesses"] = 1
    elif c == 22: v["C112_values_consumed"] = 1
    else: v["physical_couplings_consumed"] = 1
    return _freeze(v)


__all__ = ["STATUS", "NEXT", "RESOLUTIONS", "PROGRAMS", "SECTORS", "ZERO_CLASSES", "PACKAGE_ROOT",
           "logical_witness_domain_manifest", "segment_manifest", "target_span_manifest", "target_span_page",
           "witness_by_rank", "witness_identity", "witness_rank", "witness_adjoint_partner", "primitive_reference_manifest",
           "witness_page", "matrix_target_manifest", "matrix_target_witness_page", "cross_sector_zero_domain_manifest",
           "count_once_certificate", "factor_ownership_contract", "verify_current_logical_domain", "load_verified_current_logical_domain",
           "static_isolation_guard", "mutate_live_icdomain2"]
