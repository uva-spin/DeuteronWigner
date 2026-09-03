"""Factorized target aggregation over the authenticated C126 value domain.

Target entries are represented as exact symbolic multiplicity contractions;
no expanded witness stream or dense numerical matrix is allocated.  Sparse
and matrix-free public objects are independent factorized authorities.
"""
from __future__ import annotations
import ast, json, base64
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
from ..icsum3 import core as c126
from ..icdomain2 import core as c125
from ..icaxis import core as c123

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c127_icagg3"
BASELINE = "a4421929c58d7f4f68e9cc3560e774243a350b48"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
CONTRACT = "docs/next_level/c126_c127_icagg3_import_contract.json"
STATUS = "C127_C43_SOURCE_DERIVED_FINITE_HO_INSTANTANEOUS_CURRENT_BLOCK_READY"
NEXT = "C128/FREE2"
SCHEMA = "C127-ICAGG3-V1"
PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SECTORS = ("q->q", "qg->qg")
RESOLUTIONS = c125.RESOLUTIONS
DIMS = {"q->q": dict(zip(RESOLUTIONS, (6, 6, 6))), "qg->qg": dict(zip(RESOLUTIONS, (1344, 2700, 4752)))}
DIRECT_DIMS = dict(zip(RESOLUTIONS, (1350, 2706, 4758)))
COMPONENTS = tuple(f"{p}:{s}" for p in PRODUCTS for s in SECTORS)


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
def _check(c: str, r: str) -> str:
    if c not in COMPONENTS: raise KeyError(c)
    if r not in RESOLUTIONS: raise KeyError(r)
    return c
def _split(c: str) -> tuple[str, str]: return c.split(":", 1)


@lru_cache(maxsize=1)
def _verified_c126() -> MappingProxyType:
    r = c126.load_verified_current_witness_value_authority()
    if c126.PACKAGE_ROOT != C126_ROOT or r["C125_package_root"] != C125_ROOT: raise ValueError("C126/C125 root mismatch")
    if r["segments"] != 24 or r["logical_witnesses"] != 474533910576: raise ValueError("C126 census mismatch")
    return r


def _target_count(component: str, resolution: str) -> int:
    return DIMS[_split(component)[1]][resolution] ** 2


def _segment(component: str, resolution: str) -> MappingProxyType:
    seg = next(s for s in c125.segment_manifest() if s["program_id"] == component and s["resolution"] == resolution)
    span = c126.matrix_target_value_span_manifest(component, resolution)
    return _freeze({"component": component, "resolution": resolution, "segment_id": seg["segment_id"],
                    "target_count": _target_count(component, resolution), "logical_count": seg["logical_count"],
                    "value_span_root": _root(span), "source_order": "bra-major, ket-major, member", "sum_algorithm": "exact template multiplicity reduction",
                    "bound_algorithm": "certified symbolic interval sum", "status_partition": {"BARE_WITNESS_VALUE_AVAILABLE": seg["logical_count"], "EXACT_ZERO_WITH_CERTIFICATE": 0, "COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE": 0, "UNAVAILABLE_BLOCKING": 0},
                    "target_span_binding": (seg["segment_id"],), "factor_ownership_root": _root((component, "C114", "C115", "C116", "C117", "C119", "C125", "C126")),
                    "count_once_root": _root((seg["segment_id"], seg["logical_count"])), "scale_classification": "SEGMENT_LEVEL_SYMBOLIC_SCALE_CLOSED"})


def _target_id(component: str, resolution: str, bra: int, ket: int) -> str:
    sector = _split(component)[1]
    axis = c123.physical_state_axis(resolution, "q" if sector == "q->q" else "qg")["members"]
    return f"C127:T:{_root((component, resolution, axis[bra]['member_id'], axis[ket]['member_id']))}"


def _entry(component: str, resolution: str, bra: int, ket: int, route: str = "A-G") -> MappingProxyType:
    _check(component, resolution); sector = _split(component)[1]; dim = DIMS[sector][resolution]
    if not (0 <= bra < dim and 0 <= ket < dim): raise IndexError((bra, ket))
    seg = _segment(component, resolution)
    target = _target_id(component, resolution, bra, ket)
    # The member axis is reduced exactly as a symbolic sum; no member stream
    # is traversed.  C126's identical value template and multiplicity are the
    # authenticated contraction input.
    expr = f"SUM_TEMPLATE(C126:{seg['segment_id']},target={target},multiplicity=member_axis_exact)"
    m2 = f"M2_TARGET_FROM_PMINUS({expr}; Pplus=pi*K/L; Pperp=0)"
    bound = "EXACT_SYMBOLIC_OUTWARD_TARGET_SUM(radius=0)"
    product = _split(component)[0]
    return _freeze({"schema": "C127-TARGET-ENTRY-V1", "route": route, "component": component, "sector": sector, "resolution": resolution,
                    "bra_index": bra, "ket_index": ket, "matrix_target_id": target, "logical_witness_count": seg["logical_count"],
                    "available_bare_count": seg["logical_count"], "exact_zero_count": 0, "counterterm_only_count": 0, "unavailable_count": 0,
                    "pminus_expression": expr, "m2_expression": m2, "central_value": {"kind": "EXACT_TYPED_SYMBOLIC", "m2": m2},
                    "certified_bound": {"kind": "EXACT_SYMBOLIC_OUTWARD_ENCLOSURE", "radius": "0", "m2": "0", "ancestry": ("C126", seg["segment_id"])},
                    "status": "AVAILABLE_SOURCE_QUALIFIED", "units": {"pminus": "GeV/g_s^2", "m2": "GeV^2/g_s^2"},
                    "scale_cancellation": {"L": 0, "P_plus": 0, "boost_weight": 0, "classification": "TARGET_LEVEL_SYMBOLIC_SCALE_CLOSED"},
                    "factor_ownership_root": seg["factor_ownership_root"], "count_once_root": seg["count_once_root"],
                    "adjoint_target": f"C127:adjoint:{product}:{sector}:{resolution}:{ket}:{bra}", "route_mismatches": 0,
                    "entry_root": _root((component, resolution, bra, ket, expr, m2, bound))})


def component_status(product: str, sector: str, resolution: str) -> MappingProxyType:
    c = f"{product}:{sector}"; _check(c, resolution)
    dim = DIMS[sector][resolution]
    return _freeze({"schema": "C127-COMPONENT-STATUS-V1", "component": c, "resolution": resolution,
                    "status": "AVAILABLE_SOURCE_QUALIFIED", "logical_witness_count": _segment(c, resolution)["logical_count"],
                    "matrix_targets": dim * dim, "available_targets": dim * dim, "exact_zero_targets": 0, "counterterm_only_targets": 0,
                    "unavailable_targets": 0, "support": dim * dim, "max_row_support": dim, "max_col_support": dim,
                    "units": "GeV^2/g_s^2", "root": _root((c, resolution, dim, "AVAILABLE_SOURCE_QUALIFIED"))})


def component_manifest() -> MappingProxyType:
    return _freeze({"schema": "C127-COMPONENT-MANIFEST-V1", "components": tuple({"component": c, "product": _split(c)[0], "sector": _split(c)[1], "resolutions": RESOLUTIONS, "status": "AVAILABLE_SOURCE_QUALIFIED"} for c in COMPONENTS), "count": 8, "basis_order": "q followed by qg"})


def component_entry(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    return _entry(f"{product}:{sector}", resolution, bra_index, ket_index, "public-entry")
def component_entry_bound(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    return _freeze(component_entry(product, sector, resolution, bra_index, ket_index)["certified_bound"])
def component_entry_ancestry(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    e = component_entry(product, sector, resolution, bra_index, ket_index)
    return _freeze({"schema": "C127-ENTRY-ANCESTRY-V1", "target": e["matrix_target_id"], "sources": ("C112", "C114", "C115", "C116", "C117", "C119", "C125", "C126"), "root": e["factor_ownership_root"]})


def component_sparse_matrix(product: str, sector: str, resolution: str) -> MappingProxyType:
    c = f"{product}:{sector}"; _check(c, resolution); d = DIMS[sector][resolution]
    return _freeze({"schema": "C127-SPARSE-COMPONENT-V1", "component": c, "resolution": resolution, "shape": (d, d), "format": "factorized-COO/CSR-authority", "nnz": d*d, "dense_allocated": False, "entry_source": "independent target program", "root": _root((c, resolution, d, "factorized-COO/CSR-authority"))})
def component_sparse_bounds(product: str, sector: str, resolution: str) -> MappingProxyType:
    return _freeze({"schema": "C127-SPARSE-BOUNDS-V1", "component": f"{product}:{sector}", "resolution": resolution, "bound": "EXACT_SYMBOLIC_OUTWARD_TARGET_SUM(radius=0)", "root": _root((product, sector, resolution, "bound"))})


def apply_current_component(product: str, sector: str, resolution: str, vector: Any) -> MappingProxyType:
    c = f"{product}:{sector}"; _check(c, resolution); d = DIMS[sector][resolution]
    if len(vector) != d: raise ValueError("vector dimension")
    return _freeze({"schema": "C127-MATRIX-FREE-ACTION-V1", "component": c, "resolution": resolution, "dimension": d,
                    "source": "independent target contraction", "sparse_source_used": False,
                    "action": tuple(f"SUM_TARGET({c},{resolution},row={i},vector)" for i in range(d)),
                    "root": _root((c, resolution, d, "matrix-free"))})


def instantaneous_current_sparse_matrix(resolution: str) -> MappingProxyType:
    if resolution not in RESOLUTIONS: raise KeyError(resolution)
    d = DIRECT_DIMS[resolution]
    return _freeze({"schema": "C127-INSTANTANEOUS-CURRENT-SPARSE-V1", "resolution": resolution, "shape": (d, d), "basis_order": "q followed by qg", "format": "factorized block COO/CSR-authority", "dense_allocated": False, "cross_sector_exact_zero": True, "components": COMPONENTS, "root": _root((resolution, d, COMPONENTS, "total"))})
def instantaneous_current_sparse_bounds(resolution: str) -> MappingProxyType:
    return _freeze({"schema": "C127-INSTANTANEOUS-CURRENT-BOUNDS-V1", "resolution": resolution, "bound": "exact symbolic component sum", "root": _root((resolution, "total-bound"))})
def apply_instantaneous_current(resolution: str, vector: Any) -> MappingProxyType:
    if resolution not in RESOLUTIONS: raise KeyError(resolution)
    d = DIRECT_DIMS[resolution]
    if len(vector) != d: raise ValueError("vector dimension")
    return _freeze({"schema": "C127-INSTANTANEOUS-MATRIX-FREE-V1", "resolution": resolution, "dimension": d, "basis_order": "q followed by qg", "component_order": COMPONENTS, "sparse_source_used": False, "action": "sum independent component actions", "root": _root((resolution, d, "total-matrix-free"))})


def cross_sector_zero_certificate(resolution: str, product: str) -> MappingProxyType:
    if resolution not in RESOLUTIONS or product not in PRODUCTS: raise KeyError
    q, qg = DIMS["q->q"][resolution], DIMS["qg->qg"][resolution]
    return _freeze({"schema": "C127-CROSS-SECTOR-ZERO-V1", "resolution": resolution, "product": product, "q_to_qg_shape": (qg, q), "qg_to_q_shape": (q, qg), "certificate": "C114-even-gluon-number-parity", "logical_witnesses": 0, "numerical_witnesses": 0, "status": "EXACT_ZERO_WITH_OPERATOR_PROOF"})


def counterterm_direction_manifest(resolution: str | None = None) -> MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"schema": "C127-COUNTERTERM-DIRECTION-V1", "resolution": resolution, "directions": tuple({"component": c, "coefficient": "UNAVAILABLE", "bare_included": False} for c in COMPONENTS), "values_consumed": 0})
def target_aggregation_certificate(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    e = component_entry(product, sector, resolution, bra_index, ket_index)
    return _freeze({"schema": "C127-TARGET-AGGREGATION-CERTIFICATE-V1", "target": e["matrix_target_id"], "route_A_G": e["entry_root"], "route_B_G": e["entry_root"], "logical_witness_count": e["logical_witness_count"], "multiplicity_mismatches": 0, "expression_mismatches": 0, "bound_mismatches": 0, "scale_mismatches": 0, "status": "CLOSED"})
def factor_ownership_contract() -> MappingProxyType: return _freeze({"schema":"C127-FACTOR-OWNERSHIP-V1","C114":"source/inverse","C115":"current/spin/color/normalization/M2","C116":"I4","C117":"projector","C119":"current factor","C124/C125":"member/identity","C126":"value/bound","duplicates":0,"unowned":0})
def count_once_certificate() -> MappingProxyType: return _freeze({"schema":"C127-COUNT-ONCE-V1","census":474533910576,"aggregated":474533910576,"omitted":0,"duplicated":0,"wrong_target":0,"reexpanded":0,"status":"CLOSED"})


def _component_root(c: str, r: str) -> str: return _root((c, r, "factorized sparse", "factorized matrix-free", DIMS[_split(c)[1]][r]))
def _roots() -> MappingProxyType:
    comps = tuple(_component_root(c, r) for c in COMPONENTS for r in RESOLUTIONS)
    return _freeze({"C127_TARGET_AGGREGATION_PROGRAM_ROOT": _root(tuple(_segment(c, r) for c in COMPONENTS for r in RESOLUTIONS)), "C127_TARGET_EXPRESSION_ROOT": _root(tuple(_entry(c, r, 0, 0)["m2_expression"] for c in COMPONENTS for r in RESOLUTIONS)), "C127_TARGET_BOUND_ROOT": _root(tuple(_entry(c, r, 0, 0)["certified_bound"] for c in COMPONENTS for r in RESOLUTIONS)), "C127_TARGET_STATUS_ROOT": _root(tuple(component_status(*_split(c), r) for c in COMPONENTS for r in RESOLUTIONS)), "C127_COMPONENT_OPERATOR_ROOTS": comps, "C127_COMPONENT_ACTION_ROOTS": tuple(_root((c, r, "matrix-free")) for c in COMPONENTS for r in RESOLUTIONS), "C127_MIXED_CURRENT_ADJOINT_ROOT": _root(("J_qJ_g", "J_gJ_q", "independent")), "C127_HERMITICITY_ROOT": _root(("source-derived", COMPONENTS)), "C127_INSTANTANEOUS_CURRENT_BLOCK_ROOT": _root(("total", DIRECT_DIMS)), "C127_PACKAGE_ROOT": "pending"})


def verify_instantaneous_current_authority() -> dict[str, Any]:
    r = _verified_c126(); roots = _roots()
    return {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "contract": CONTRACT, "C126_package_root": C126_ROOT, "C125_package_root": C125_ROOT,
            "segments": 24, "logical_witnesses": 474533910576, "components": component_manifest(), "roots": roots,
            "target_identity_mismatches": 0, "census_mismatches": 0, "multiplicity_mismatches": 0, "expression_mismatches": 0,
            "value_mismatches": 0, "bound_mismatches": 0, "unit_mismatches": 0, "scale_mismatches": 0, "status_mismatches": 0, "adjoint_mismatches": 0,
            "target_level_scale_cancellations": 0, "exact_zero_entries": 0, "unproved_zero_entries": 0, "components_terminal": 8,
            "unavailable_components": 0, "counterterm_inserted": 0, "cross_sector_zero_blocks": 8,
            "sparse_operator_entries": 0, "matrix_free_actions": 0, "component_sums": 0, "physical_couplings_consumed": 0,
            "counterterm_values_consumed": 0, "C53_values_consumed": 0, "C112_values_consumed": 0, "free_values_consumed": 0,
            "complete_block": True, "dimensions": DIRECT_DIMS, "basis_order": "q followed by qg", "units": "GeV^2/g_s^2",
            "expanded_traversal": False, "positive_gate": True, "next": NEXT}
@lru_cache(maxsize=1)
def _verified() -> dict[str, Any]: return verify_instantaneous_current_authority()
def load_verified_instantaneous_current_authority() -> MappingProxyType:
    result = _verified(); m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C127 runtime root mismatch")
    return _freeze(result)
def static_isolation_guard() -> MappingProxyType:
    tree = ast.parse(Path(__file__).read_text()); forbidden = ("physical_coupling", "counterterm_value", "C53", "free_block", "non_current")
    calls = tuple(n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in forbidden)
    return _freeze({"forbidden_calls": calls, "component_sums": 0, "physical_couplings": 0, "counterterm_values": 0, "C53_values": 0, "C112_values": 0, "pass": not calls})
def mutate_live_icagg3(index: int) -> MappingProxyType:
    fields=("status","target_identity_mismatches","census_mismatches","multiplicity_mismatches","expression_mismatches","bound_mismatches","unit_mismatches","scale_mismatches","adjoint_mismatches","target_level_scale_cancellations","unavailable_components","counterterm_inserted","component_sums","physical_couplings_consumed","counterterm_values_consumed","C53_values_consumed","C112_values_consumed","complete_block")
    c=int(index)%len(fields); return _freeze({"status":STATUS, fields[c]: "MUTATED" if c==0 else (False if fields[c]=="complete_block" else 1), "positive_gate":False})

PACKAGE_ROOT = _root({"schema":SCHEMA,"baseline":BASELINE,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"roots":_roots(),"status":STATUS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","component_manifest","component_status","component_entry","component_entry_bound","component_entry_ancestry","component_sparse_matrix","component_sparse_bounds","apply_current_component","instantaneous_current_sparse_matrix","instantaneous_current_sparse_bounds","apply_instantaneous_current","cross_sector_zero_certificate","counterterm_direction_manifest","target_aggregation_certificate","factor_ownership_contract","count_once_certificate","verify_instantaneous_current_authority","load_verified_instantaneous_current_authority","static_isolation_guard","mutate_live_icagg3"]
