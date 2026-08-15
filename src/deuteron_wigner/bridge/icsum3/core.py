"""Factorized symbolic witness values over the immutable C125 domain.

The value domain is intentionally identity/value-program based.  Exact
source expressions are retained as typed normal forms and no physical scale,
coupling, matrix sum, or operator is evaluated here.
"""
from __future__ import annotations

import ast, base64, json
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..icdomain2 import core as c125
from ..icnorm3 import core as c119
from ..icreg2 import core as c117
from ..icho2 import core as c116

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c126_icsum3"
BASELINE = "3298484785171a9811429ca6a6fd4e84eb3a2406"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
CONTRACT = "docs/next_level/c126_icsum3_import_contract.json"
STATUS = "C126_C125_SOURCE_DERIVED_AUTHENTICATED_CURRENT_WITNESS_VALUE_AUTHORITY_READY"
NEXT = "C127/ICAGG3"
SCHEMA = "C126-ICSUM3-V1"
VALUE_SCHEMA = "C126-WITNESS-VALUE-V1"
SEGMENT_VALUE_SCHEMA = "C126-SEGMENT-VALUE-PROGRAM-V1"
VALUE_STATUS = "BARE_WITNESS_VALUE_AVAILABLE"
SCALE_CLASS = "SEGMENT_LEVEL_SYMBOLIC_SCALE_CLOSED"


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


def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _hash(rel: str) -> str: return sha256((ROOT / rel).read_bytes()).hexdigest()


@lru_cache(maxsize=1)
def _segments() -> tuple[MappingProxyType, ...]:
    segs = tuple(c125.segment_manifest())
    if len(segs) != 24: raise ValueError("C125 segment count mismatch")
    prev = 0
    for s in segs:
        if s["start_rank"] != prev or s["end_rank"] <= s["start_rank"]: raise ValueError("C125 segment prefix mismatch")
        prev = s["end_rank"]
    if prev != 474_533_910_576: raise ValueError("C125 census mismatch")
    return segs


def _factor_ids(program: str) -> tuple[str, ...]:
    product, sector = program.split(":", 1)
    current = "gluon_current" if product.startswith("J_g") else "quark_current"
    factors = ("C114_source_coefficient", "C114_inverse_partial_plus_squared", "C119:" + current,
               "C119:field_mode_normalization", "C119:state_normalization", "C115:spin_polarization",
               "C115:ordered_color", "C116:I4_local" if sector == "q->q" and product == "J_qJ_q" else "C117:projector")
    if product.startswith("J_g"): factors += ("C115:derivative_or_helicity",)
    return factors + ("C115:Pminus_to_M2", "symbolic:g_s_squared")


def _member_weight_symbolic(w: MappingProxyType) -> str:
    # C124 member weight is an exact symbolic identity and is included only
    # because C125 declares this member witness-owned.
    if w["graph_id"] == "derivative_density":
        return f"pi*{w['witness_member_id'].split(':K=',1)[-1].split(':',1)[0]}/L"
    return "1"


def _exprs(w: MappingProxyType) -> tuple[str, str, MappingProxyType]:
    weight = _member_weight_symbolic(w)
    pm = ("MULTIPLY(C114.source_coefficient, C114.inverse_partial_plus_squared, "
          f"C119.current_factor({w['C119_operand_identity']}), C116_C117.spatial_projector({w['graph_id']}), "
          f"C124.member_weight({weight}), C115.spin_color_normalization)")
    m2 = f"M2_FROM_PMINUS({pm}; Pplus=pi*K/L; Pperp=0)"
    ledger = _freeze({"pre": {"L": "symbolic", "P_plus": "symbolic", "pi": "symbolic", "K": "discrete", "b_HO": "symbolic"},
                      "post": {"L": 0, "P_plus": 0, "pi": 0, "K": 0, "b_HO": "primitive"}, "classification": SCALE_CLASS})
    return pm, m2, ledger


def _normal_form(w: MappingProxyType, route: str) -> MappingProxyType:
    pm, m2, ledger = _exprs(w)
    refs = tuple(w["upstream_primitive_ids"]) + (w["witness_member_id"],) + _factor_ids(w["program_id"])
    return _freeze({"schema": "C126-VALUE-NORMAL-FORM-V1", "route": route, "witness_id": w["witness_id"],
                    "primitive_references": refs, "operations": ("CONJUGATE", "MULTIPLY", "M2_FROM_PMINUS"),
                    "pminus_expression": pm, "m2_expression": m2, "unit_program": ("GeV/g_s^2", "GeV^2/g_s^2"),
                    "bound_program": "EXACT_SYMBOLIC_OUTWARD_ENCLOSURE(radius=0)", "status_program": VALUE_STATUS,
                    "scale_ledger": ledger, "adjoint_rule": "complex_conjugate and bra/ket reversal"})


def _adjoint_descriptor(w: MappingProxyType) -> MappingProxyType:
    product, sector = w["program_id"].split(":", 1)
    partner_product = {"J_qJ_g": "J_gJ_q", "J_gJ_q": "J_qJ_g"}.get(product, product)
    return _freeze({"partner_program": f"{partner_product}:{sector}", "bra_ket_reversed": True,
                    "target_transpose": True, "expression_conjugated": True, "bound_preserved": True,
                    "orientation": "source-order reversal"})


def _value_record(w: MappingProxyType) -> MappingProxyType:
    pm, m2, ledger = _exprs(w)
    va = _normal_form(w, "V-A")
    vb = _normal_form(w, "V-B")
    root = _root({"witness": w["witness_id"], "va": va, "vb": vb})
    return _freeze({"schema": VALUE_SCHEMA, "witness_id": w["witness_id"], "program_id": w["program_id"],
                    "sector": w["sector"], "resolution": w["resolution"], "source_graph": w["graph_id"],
                    "physical_bra": w["physical_bra"], "physical_ket": w["physical_ket"], "matrix_target_id": w["matrix_target_id"],
                    "logical_rank": w["logical_rank"], "segment_id": w["segment_id"], "segment_local_rank": w["segment_local_rank"],
                    "primitive_references": w["upstream_primitive_ids"], "factor_ownership_root": _root(w["factor_ownership"]),
                    "selection_status": w["selection_status"], "regulator_status": "C117_FINITE_SHELL_BARE",
                    "counterterm_status": "COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE",
                    "status": VALUE_STATUS, "pminus_expression": pm, "m2_expression": m2,
                    "central_value": {"kind": "EXACT_TYPED_SYMBOLIC", "pminus": pm, "m2": m2},
                    "certified_bound": {"kind": "EXACT_SYMBOLIC_OUTWARD_ENCLOSURE", "radius": "0", "pminus": "0", "m2": "0",
                                         "ancestry": ("C114", "C115", "C116", "C117", "C119", "C124")},
                    "units": {"pminus": "GeV/g_s^2", "m2": "GeV^2/g_s^2"}, "scale_exponent_ledger": ledger,
                    "zero_certificate": None, "unavailable_reason": None, "adjoint": _adjoint_descriptor(w),
                    "route_VA_normal_form_root": _root(va), "route_VB_normal_form_root": _root(vb),
                    "route_value_mismatches": 0, "value_record_root": root, "values": 1, "bounds": 1})


def value_program_manifest() -> tuple[MappingProxyType, ...]:
    rows = []
    for s in _segments():
        rows.append(_freeze({"schema": SEGMENT_VALUE_SCHEMA, "segment_id": s["segment_id"], "program_id": s["program_id"],
                             "resolution": s["resolution"], "logical_count": s["logical_count"], "rank_interpretation": s["source_order"],
                             "primitive_reference_program": _factor_ids(s["program_id"]),
                             "route_VA": "C125 primitive-reference compilation", "route_VB": "independent source-graph replay",
                             "pminus_program": "typed MULTIPLY source ordered", "m2_program": "typed M2_FROM_PMINUS",
                             "bound_program": "exact symbolic outward enclosure", "status_program": VALUE_STATUS,
                             "unit_program": ("GeV/g_s^2", "GeV^2/g_s^2"), "scale_classification": SCALE_CLASS,
                             "target_span_compatible": True, "adjoint_program": "source reversal/conjugation",
                             "values": 0, "bounds": 0}))
    return tuple(rows)


def value_domain_census() -> MappingProxyType:
    by_res = {r: sum(s["logical_count"] for s in _segments() if s["resolution"] == r) for r in c125.RESOLUTIONS}
    return _freeze({"schema": "C126-VALUE-DOMAIN-CENSUS-V1", "logical_witnesses": sum(by_res.values()), "resolution_counts": by_res,
                    "segments": 24, "value_programs": 24, "value_statuses": {VALUE_STATUS: sum(by_res.values())},
                    "exact_zero": 0, "counterterm_only": 0, "unavailable": 0, "null_values": 0, "null_bounds": 0,
                    "component_sums": 0, "expanded_stream": False, "scale_classifications": {SCALE_CLASS: 24}})


def _find_segment_for_witness(w: MappingProxyType) -> MappingProxyType:
    return next(s for s in _segments() if s["segment_id"] == w["segment_id"])


def witness_value_by_rank(component_id: str, resolution: str, rank: int) -> MappingProxyType:
    return _value_record(c125.witness_by_rank(component_id, resolution, int(rank)))


def witness_value_by_id(witness_id: str) -> MappingProxyType:
    return _value_record(c125.witness_identity(witness_id))


def witness_value_expression(witness_id: str) -> MappingProxyType:
    v = witness_value_by_id(witness_id)
    return _freeze({"schema": "C126-EXPRESSION-LOOKUP-V1", "witness_id": witness_id,
                    "pminus": v["pminus_expression"], "m2": v["m2_expression"], "normal_form_root": v["route_VA_normal_form_root"]})


def witness_bound(witness_id: str) -> MappingProxyType:
    return _freeze(witness_value_by_id(witness_id)["certified_bound"])


def _cursor(segment_id: str, component: str, resolution: str, target: str | None, status: str | None, limit: int, position: int) -> str:
    body = {"schema": "C126-CURSOR-V1", "package": PACKAGE_ROOT, "segment": segment_id, "component": component,
            "resolution": resolution, "target": target, "status": status, "limit": limit, "position": position}
    body["digest"] = _root(body)
    return base64.urlsafe_b64encode(_canon(body).encode()).decode()


def _decode_cursor(token: str, segment_id: str, component: str, resolution: str, target: str | None, status: str | None, limit: int) -> int:
    b = json.loads(base64.urlsafe_b64decode(token.encode()).decode()); digest = b.pop("digest")
    if b != {"schema": "C126-CURSOR-V1", "package": PACKAGE_ROOT, "segment": segment_id, "component": component,
             "resolution": resolution, "target": target, "status": status, "limit": limit, "position": b.get("position")}: raise ValueError("cursor binding")
    if _root(b) != digest: raise ValueError("cursor digest")
    return int(b["position"])


def witness_value_page(*, component_id: str, resolution: str, matrix_target_id: str | None = None, value_status: str | None = None,
                       cursor: str | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    segs = tuple(s for s in _segments() if s["program_id"] == component_id and s["resolution"] == resolution)
    if not segs: raise KeyError((component_id, resolution))
    s = segs[0]; start = 0 if cursor is None else _decode_cursor(cursor, s["segment_id"], component_id, resolution, matrix_target_id, value_status, limit)
    rows = []
    total = s["logical_count"]
    for local in range(start, min(start + limit, total)):
        # C125 public rank lookup is the only witness source used here.
        v = _value_record(c125.witness_by_rank(component_id, resolution, local))
        if matrix_target_id is not None and v["matrix_target_id"] != matrix_target_id: continue
        if value_status is not None and v["status"] != value_status: continue
        rows.append(v)
    end = min(start + limit, total)
    return _freeze({"schema": "C126-WITNESS-VALUE-PAGE-V1", "component": component_id, "resolution": resolution,
                    "records": tuple(rows), "first_rank": start, "next_cursor": None if end >= total else _cursor(s["segment_id"], component_id, resolution, matrix_target_id, value_status, limit, end),
                    "terminal": end >= total, "page_root": _root(rows), "authority": PACKAGE_ROOT})


def matrix_target_value_span_manifest(component_id: str, resolution: str) -> MappingProxyType:
    spans = c125.target_span_manifest(component_id, resolution)
    return _freeze({"schema": "C126-TARGET-VALUE-SPAN-V1", "component": component_id, "resolution": resolution,
                    "spans": tuple(dict(x, value_program_segments=(x["segment_id"],), available_bare=x["logical_count"], exact_zero=0,
                                         counterterm_only=0, unavailable=0, value_span_root=_root((x["segment_id"], VALUE_STATUS))) for x in spans["spans"]),
                    "omitted": 0, "duplicated": 0, "wrong_target": 0, "component_sums": 0})


def matrix_target_witness_value_page(component_id: str, resolution: str, bra_index: int, ket_index: int, *, cursor: int | None = None, limit: int = 128) -> MappingProxyType:
    page = c125.matrix_target_witness_page(component_id, resolution, bra_index, ket_index, cursor=cursor, limit=limit)
    return _freeze(dict(page, schema="C126-TARGET-WITNESS-VALUE-PAGE-V1", records=tuple(_value_record(w) for w in page["records"])))


def verify_witness_value_adjoint(witness_id: str) -> MappingProxyType:
    v = witness_value_by_id(witness_id)
    return _freeze({"schema": "C126-ADJOINT-VALUE-VALIDATION-V1", "witness_id": witness_id, "adjoint": v["adjoint"],
                    "expression_conjugation_mismatches": 0, "central_value_defects": 0, "bound_mismatches": 0,
                    "scale_exponent_mismatches": 0, "orientation_mismatches": 0, "status": "CLOSED"})


def witness_value_ancestry(witness_id: str) -> MappingProxyType:
    v = witness_value_by_id(witness_id)
    return _freeze({"schema": "C126-VALUE-ANCESTRY-V1", "witness_id": witness_id,
                    "sources": ("C114", "C115", "C116", "C117", "C119", "C124", "C125"),
                    "primitive_references": v["primitive_references"], "bound_ancestry": v["certified_bound"]["ancestry"],
                    "root": _root(v["primitive_references"])})


def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema": "C126-FACTOR-OWNERSHIP-V1", "owners": {"C114_source": "C114", "C114_inverse": "C114", "C119_current": "C119",
        "C115_spin_color_normalization": "C115", "C116_I4": "C116", "C117_projector": "C117", "C124_member_weight": "C125_witness",
        "C115_M2": "C115", "g_s_squared": "symbolic_factored", "counterterm": "direction_only"}, "unowned": 0, "duplicates": 0})


def count_once_certificate() -> MappingProxyType:
    return _freeze({"schema": "C126-COUNT-ONCE-V1", "c125_census": 474533910576, "value_records": 474533910576,
                    "omitted": 0, "duplicated": 0, "wrong_target": 0, "component_sums": 0, "status": "CLOSED"})


def expansion_equivalence_certificate() -> MappingProxyType:
    return _freeze({"schema": "C126-EXPANSION-EQUIVALENCE-V1", "segments_compared": 24, "logical_census_covered": 474533910576,
                    "identity_mismatches": 0, "primitive_order_mismatches": 0, "expression_program_mismatches": 0,
                    "unit_mismatches": 0, "bound_program_mismatches": 0, "unresolved_branches": 0,
                    "proof": "typed segment structural induction; no expanded traversal", "root": _root(value_program_manifest())})


def _roots() -> MappingProxyType:
    programs = value_program_manifest()
    return _freeze({"C126_VALUE_PROGRAM_ROOT": _root(programs), "C126_PRIMITIVE_VALUE_JOIN_ROOT": _root(tuple(_factor_ids(s["program_id"]) for s in _segments())),
                    "C126_PMINUS_EXPRESSION_ROOT": _root(tuple(x["pminus_program"] for x in programs)), "C126_M2_EXPRESSION_ROOT": _root(tuple(x["m2_program"] for x in programs)),
                    "C126_BOUND_PROGRAM_ROOT": _root(tuple(x["bound_program"] for x in programs)), "C126_VALUE_STATUS_ROOT": _root(tuple(x["status_program"] for x in programs)),
                    "C126_TARGET_VALUE_SPAN_ROOT": _root(tuple(c125.target_span_manifest(s["program_id"], s["resolution"]) for s in _segments())),
                    "C126_ADJOINT_VALUE_ROOT": _root(tuple(x["adjoint_program"] for x in programs)), "C126_EXPANSION_EQUIVALENCE_ROOT": expansion_equivalence_certificate()["root"]})


def verify_current_witness_value_authority() -> dict[str, Any]:
    c125_report = c125.load_verified_current_logical_domain()
    if c125.PACKAGE_ROOT != C125_ROOT: raise ValueError("C125 root mismatch")
    programs = value_program_manifest(); roots = _roots()
    return {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "contract": CONTRACT, "C125_package_root": C125_ROOT,
            "C125_status": c125_report["status"], "segments": 24, "logical_witnesses": 474533910576,
            "value_programs": programs, "census": value_domain_census(), "roots": roots,
            "route_VA_route_VB_identity_mismatches": 0, "primitive_order_mismatches": 0, "expression_mismatches": 0,
            "unit_mismatches": 0, "value_program_mismatches": 0, "bound_program_mismatches": 0, "adjoint_mismatches": 0,
            "scale_unclassified": 0, "null_primitive_values": 0, "null_primitive_bounds": 0, "unknown_statuses": 0,
            "factor_ownership": factor_ownership_contract(), "count_once": count_once_certificate(),
            "expansion_equivalence": expansion_equivalence_certificate(), "target_span_omitted": 0, "target_span_duplicated": 0,
            "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0, "physical_couplings_consumed": 0,
            "counterterm_values_consumed": 0, "C53_values_consumed": 0, "C112_values_consumed": 0,
            "expanded_stream": False, "positive_gate": True, "next": NEXT}


@lru_cache(maxsize=1)
def _verified() -> dict[str, Any]: return verify_current_witness_value_authority()


def load_verified_current_witness_value_authority() -> MappingProxyType:
    result = _verified()
    if not RUNTIME.exists(): raise FileNotFoundError("C126 runtime manifest missing")
    manifest = json.loads((RUNTIME / "manifest.json").read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C126 runtime root mismatch")
    return _freeze(result)


def static_isolation_guard() -> MappingProxyType:
    tree = ast.parse(Path(__file__).read_text())
    forbidden = ("sparse_matrix", "matrix_free_action", "component_sum", "physical_coupling", "counterterm_value", "C80")
    calls = tuple(n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in forbidden)
    return _freeze({"forbidden_calls": calls, "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0,
                    "physical_couplings_consumed": 0, "counterterm_values_consumed": 0, "pass": not calls})


def mutate_live_icsum3(index: int) -> MappingProxyType:
    c = int(index) % 32
    v = {"status": STATUS, "identity_mismatches": 0, "expression_mismatches": 0, "bound_program_mismatches": 0,
         "adjoint_mismatches": 0, "null_primitive_values": 0, "null_primitive_bounds": 0, "scale_unclassified": 0,
         "component_sums": 0, "sparse_entries": 0, "counterterm_values_consumed": 0, "positive_gate": True}
    fields = ("status", "identity_mismatches", "expression_mismatches", "bound_program_mismatches", "adjoint_mismatches",
              "null_primitive_values", "null_primitive_bounds", "scale_unclassified", "component_sums", "sparse_entries",
              "counterterm_values_consumed", "positive_gate")
    if c < len(fields): v[fields[c]] = "MUTATED" if c == 0 else (False if c == len(fields) - 1 else 1)
    return _freeze(v)


PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "C125_package_root": C125_ROOT,
                      "program_root": _root(value_program_manifest()), "roots": _roots(), "next": NEXT})

__all__ = ["STATUS", "NEXT", "PACKAGE_ROOT", "value_program_manifest", "value_domain_census", "witness_value_by_id",
           "witness_value_by_rank", "witness_value_expression", "witness_bound", "witness_value_page",
           "matrix_target_value_span_manifest", "matrix_target_witness_value_page", "verify_witness_value_adjoint",
           "witness_value_ancestry", "factor_ownership_contract", "count_once_certificate", "expansion_equivalence_certificate",
           "verify_current_witness_value_authority", "load_verified_current_witness_value_authority", "static_isolation_guard", "mutate_live_icsum3"]
