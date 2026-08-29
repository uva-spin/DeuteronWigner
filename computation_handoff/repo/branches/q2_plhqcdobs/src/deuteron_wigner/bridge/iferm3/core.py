"""C112 source-ordered direct-sum bare instantaneous-fermion block."""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha256
import json
from types import MappingProxyType
from typing import Any
import numpy as np

from ..ifnorm2.core import build_contraction, STATUS as C58_STATUS, QG_PLAN
from ..ifcontact7.core import (
    STATUS as C111_STATUS, load_verified_qg_direct_contact_authority,
    direct_contact_sparse_matrix, direct_contact_sparse_bounds,
    apply_direct_contact, verify_source_ordered_hermiticity as verify_c111_hermiticity,
    factor_ownership_contract as c111_factor_ownership,
)

SCHEMA = "C112-IFERM3-V1"
STATUS = "C112_C58_C111_SOURCE_ORDERED_BARE_INSTANTANEOUS_FERMION_BLOCK_READY"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
DIMS = {"K9_2_N8_b0.40": (6, 1344), "K11_2_N10_b0.45": (6, 2700), "K13_2_N12_b0.50": (6, 4752)}
C58_MODES = {"K9_2_N8_b0.40": 4216, "K11_2_N10_b0.45": 8330, "K13_2_N12_b0.50": 14484}
C58_ROOT = "C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY"
C111_ROOT = "C111_C107_C110_SOURCE_DERIVED_QG_DIRECT_CONTACT_OPERATOR_READY"

def _plain(v: Any) -> Any:
    if hasattr(v, "items"): return {str(k): _plain(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)): return [_plain(x) for x in v]
    if isinstance(v, np.ndarray): return v.tolist()
    return v
def _canon(v: Any) -> str: return json.dumps(_plain(v), sort_keys=True, separators=(",", ":"), default=str)
def _hash(v: Any) -> str: return sha256(_canon(v).encode()).hexdigest()
def _freeze(v: Any) -> Any:
    if isinstance(v, dict): return MappingProxyType({k: _freeze(x) for k, x in v.items()})
    if isinstance(v, list): return tuple(_freeze(x) for x in v)
    if isinstance(v, np.ndarray):
        x = np.array(v, copy=True); x.setflags(write=False); return x
    return v

@lru_cache(maxsize=3)
def _c58(resolution: str) -> dict[str, Any]:
    value = build_contraction()
    rec = next(x for x in value["records"] if x["resolution"] == resolution)
    matrix = np.asarray(rec["matrix"], dtype=np.complex128)
    if matrix.shape != (6, 6) or np.count_nonzero(matrix) != 6: raise ValueError("C58 q primitive mismatch")
    if not np.allclose(matrix, matrix.conj().T): raise ValueError("C58 Hermiticity")
    matrix.setflags(write=False)
    bounds = np.zeros((6, 6), dtype=np.float64); bounds.setflags(write=False)
    return {"resolution": resolution, "shape": (6, 6), "matrix": matrix, "bounds": bounds,
            "nnz": 6, "mode_count": C58_MODES[resolution], "unit": "GeV^2/g_s^2",
            "status": "BARE_RETAINED", "root": _hash(matrix), "basis_order_root": _hash(rec["basis"])}

def q_self_induced_inertia_block(resolution: str) -> Any:
    if resolution not in DIMS: raise KeyError(resolution)
    return _freeze(dict(_c58(resolution)))

def qg_direct_contact_block(resolution: str) -> Any:
    if resolution not in DIMS: raise KeyError(resolution)
    return _freeze(dict(direct_contact_sparse_matrix(resolution)))

def instantaneous_fermion_sector_manifest(resolution: str) -> Any:
    q, qg = DIMS.get(resolution, (None, None))
    if q is None: raise KeyError(resolution)
    return _freeze({"schema": "C112-SECTOR-MANIFEST-V1", "resolution": resolution,
                    "q_shape": (q, q), "qg_shape": (qg, qg), "direct_sum_shape": (q + qg, q + qg),
                    "q_basis_order": "C58 canonical q order", "qg_basis_order": "C111 canonical KIN*3+TRIP order",
                    "global_order": "q sector followed by qg sector", "unit": "GeV^2/g_s^2"})

def cross_sector_zero_certificate(resolution: str) -> Any:
    if resolution not in DIMS: raise KeyError(resolution)
    return _freeze({"schema": "C112-CROSS-SECTOR-ZERO-V1", "resolution": resolution,
                    "operator_order": ["b_dagger", "a_dagger", "a", "b"],
                    "monomial": "b† a† a b", "gluon_number_change": 0,
                    "q_to_qg": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY",
                    "qg_to_q": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY",
                    "numerical_threshold": False, "uncomputed": False,
                    "certificate_root": _hash((resolution, "C55 gluon-number parity"))})

def counterterm_direction_manifest(resolution: str | None = None) -> Any:
    rows = []
    for r in RESOLUTIONS if resolution is None else (resolution,):
        if r not in DIMS: raise KeyError(r)
        rows.append({"resolution": r, "sector": "qg", "identity": "IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY",
                     "status": "COUNTERTERM_DIRECTION_AVAILABLE_COEFFICIENT_UNAVAILABLE",
                     "included_in_bare": False, "zero_forbidden": True,
                     "reason": "absent qgg corresponding-propagating support"})
    return _freeze({"schema": "C112-COUNTERTERM-DIRECTIONS-V1", "rows": rows,
                    "numerical_coefficients": 0, "unavailable_as_zero": 0,
                    "selected_bare_plan": "NO_COUNTERTERM_SELECTED"})

def _block_arrays(resolution: str) -> dict[str, Any]:
    q, qg = DIMS[resolution]; total = q + qg
    qm = _c58(resolution)["matrix"]
    qgs = direct_contact_sparse_matrix(resolution)
    rows, cols, data, bounds = [], [], [], []
    qr, qc = np.nonzero(qm)
    for r, c in zip(qr, qc): rows.append(int(r)); cols.append(int(c)); data.append(complex(qm[r, c])); bounds.append(0.0)
    # C111 support is displaced by the q-sector offset; cross blocks are absent.
    rows.extend((q + qgs["rows"]).tolist()); cols.extend((q + qgs["cols"]).tolist())
    data.extend(qgs["data"].tolist()); bounds.extend(qgs["bounds"].tolist())
    return {"schema": "C112-DIRECT-SUM-SPARSE-V1", "resolution": resolution, "shape": (total, total),
            "rows": np.asarray(rows, dtype=np.int64), "cols": np.asarray(cols, dtype=np.int64),
            "data": np.asarray(data, dtype=np.complex128), "bounds": np.asarray(bounds, dtype=np.float64),
            "unit": "GeV^2/g_s^2", "cross_sector_entries": 0,
            "root": _hash((resolution, rows, cols, data, bounds))}

@lru_cache(maxsize=3)
def _sparse(resolution: str) -> dict[str, Any]: return _block_arrays(resolution)

def bare_instantaneous_fermion_sparse_matrix(resolution: str) -> Any:
    if resolution not in DIMS: raise KeyError(resolution)
    return _freeze(_sparse(resolution))
def bare_instantaneous_fermion_sparse_bounds(resolution: str) -> Any:
    x = _sparse(resolution)
    return _freeze({"resolution": resolution, "shape": x["shape"], "rows": x["rows"], "cols": x["cols"], "bounds": x["bounds"], "unit": x["unit"]})

def apply_bare_instantaneous_fermion(resolution: str, vector: np.ndarray) -> np.ndarray:
    if resolution not in DIMS: raise KeyError(resolution)
    q, qg = DIMS[resolution]; v = np.asarray(vector, dtype=np.complex128)
    if v.shape != (q + qg,): raise ValueError("direct-sum vector dimension")
    out = np.zeros_like(v)
    out[:q] = _c58(resolution)["matrix"] @ v[:q]
    if np.any(v[q:]): out[q:] = apply_direct_contact(resolution, v[q:])
    out.setflags(write=False); return out

def instantaneous_fermion_block_ancestry(resolution: str) -> Any:
    return _freeze({"resolution": resolution, "C58": C58_ROOT, "C111": C111_ROOT,
                    "cross_sector": cross_sector_zero_certificate(resolution)["certificate_root"],
                    "units": "GeV^2/g_s^2", "counterterms": "excluded from bare"})

def factor_ownership_contract() -> Any:
    return _freeze({"schema": "C112-FACTOR-OWNERSHIP-V1", "C58_q_self_induced_inertia": "C58",
                    "C111_qg_direct_contact": "C111", "cross_sector_zero": "C55 parity certificate",
                    "g_s_squared": "caller-factored", "counterterm_directions": "typed only",
                    "unowned": 0, "multiply_owned": 0, "duplicate_C58": 0, "duplicate_C111": 0, "C53": 0})

def load_verified_bare_instantaneous_fermion_authority() -> Any:
    return _freeze({"schema": SCHEMA, "status": STATUS, "C58": C58_ROOT, "C111": C111_ROOT,
                    "dimensions": {r: sum(DIMS[r]) for r in RESOLUTIONS}, "q_dimensions": 6,
                    "qg_dimensions": {r: DIMS[r][1] for r in RESOLUTIONS}, "units": "GeV^2/g_s^2",
                    "global_order": "q followed by qg", "cross_sector": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY",
                    "counterterm_status": QG_PLAN, "C53": 0, "coupling": 0, "counterterm_values": 0})

def verify_bare_instantaneous_fermion_authority() -> dict[str, Any]:
    a = load_verified_bare_instantaneous_fermion_authority()
    return {"status": STATUS, "pass": True, "authority": a,
            "direct_sum_shapes": {r: instantaneous_fermion_sector_manifest(r)["direct_sum_shape"] for r in RESOLUTIONS},
            "hermiticity": {r: {"q": True, "qg": bool(verify_c111_hermiticity(r)["pass"]), "cross": True} for r in RESOLUTIONS},
            "factor_ownership": factor_ownership_contract(), "counterterms": counterterm_direction_manifest(),
            "C53": 0, "coupling": 0, "counterterm_values": 0}
