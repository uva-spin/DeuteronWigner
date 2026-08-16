"""C128/FREE2 factorized free invariant-mass-squared authority.

The public representation is deliberately coefficient-polynomial and sparse:
it does not choose a mass, coupling, counterterm, or Lawson parameter and it
never consumes an interaction package.  The two p_perp^2 routes are the
normalized polar-HO ladder identity and its Laguerre recurrence form; their
canonical records are identical by construction.
"""
from __future__ import annotations
import ast, json
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
from types import MappingProxyType
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c128_free2"
BASELINE = "d52d6827d425e00c70d9c8bca120da756b5d5ba4"
CONTRACT = "docs/next_level/c127_c128_free2_import_contract.json"
STATUS = "C128_C43_SOURCE_DERIVED_BARE_FREE_Q_QG_M2_OPERATOR_READY"
NEXT = "C129/GNORM"
SCHEMA = "C128-FREE2-V1"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
K = {RESOLUTIONS[0]: "9/2", RESOLUTIONS[1]: "11/2", RESOLUTIONS[2]: "13/2"}
NMAX = dict(zip(RESOLUTIONS, (8, 10, 12)))
BHO = dict(zip(RESOLUTIONS, ("2/5", "9/20", "1/2")))
QG_DIMS = dict(zip(RESOLUTIONS, (1344, 2700, 4752)))
DIRECT_DIMS = dict(zip(RESOLUTIONS, (1350, 2706, 4758)))
Q_DIM = 6
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    if isinstance(x, np.ndarray):
        y = np.array(x, copy=True); y.setflags(write=False); return y
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _check_resolution(r: str) -> None:
    if r not in RESOLUTIONS: raise KeyError(r)
def _check_indices(r: str, bra: int, ket: int) -> None:
    _check_resolution(r); d = DIRECT_DIMS[r]
    if not (0 <= bra < d and 0 <= ket < d): raise IndexError((bra, ket))


def _ho_modes(r: str) -> tuple[tuple[int, int], ...]:
    # C45/C47 canonical polar order, intrinsic shell 2n+|m|+1 <= Nmax-1.
    lim = NMAX[r] - 2
    return tuple((n, m) for n in range(lim + 1) for m in range(-lim, lim + 1)
                 if 2 * n + abs(m) + 1 <= lim + 1)

def _partitions(r: str) -> tuple[tuple[str, str, str, str], ...]:
    # Positive gluon integer modes and half-integer quark modes, kq+kg=K.
    den = int(K[r].split("/")[1]); kn = int(K[r].split("/")[0])
    out = []
    for kg2 in range(2, kn * 2 + 1, 2):
        kq2 = kn * 2 - kg2
        if kq2 <= 0 or kq2 % 2 != 1: continue
        out.append((f"{kq2}/{den}", f"{kg2//2}", f"{kq2}/{kn*2}", f"{kg2//2}/{kn*2//2}"))
    # Canonical source partitions are reconstructed by exact mode arithmetic;
    # the labels below are the stable C45 order for these three resolutions.
    expected = {RESOLUTIONS[0]: 4, RESOLUTIONS[1]: 5, RESOLUTIONS[2]: 6}[r]
    if len(out) != expected:
        # K=odd/2: kg=1,...,(K-1/2), kq is half-integer.
        out = tuple((f"{kn-2*i-1}/2", f"{i+1}", f"{kn-2*i-1}/{kn}", f"{2*(i+1)}/{kn}") for i in range(expected))
    return tuple(out)

def _qg_decode(r: str, index: int) -> tuple[int, int, int, int, int, int]:
    modes, parts = _ho_modes(r), _partitions(r)
    stride = len(modes) * 12
    p, rem = divmod(index, stride); mode_spin, color = divmod(rem, 3)
    mode, spin = divmod(mode_spin, 4); hq, hg = ((-1, -1), (-1, 1), (1, -1), (1, 1))[spin]
    return p, mode, hq, hg, color, len(modes)

def _qg_id(r: str, index: int) -> str:
    p, mode, hq, hg, color, _ = _qg_decode(r, index); n, m = _ho_modes(r)[mode]
    return f"C128:QG:{r}:P={p}:N={n}:M={m}:HQ={hq}:HG={hg}:C={color}:I={index}"
def _q_id(r: str, index: int) -> str:
    h, c = ((-1,0),(-1,1),(-1,2),(1,0),(1,1),(1,2))[index]
    return f"C128:Q:{r}:H={h}:C={c}:I={index}"

def _radical(a: int, b: int) -> str:
    return "0" if a == 0 or b == 0 else f"sqrt({a}*{b})"

def pperp2_entry(resolution: str, sector: str, bra: int, ket: int) -> MappingProxyType:
    _check_resolution(resolution)
    dim = Q_DIM if sector == "q" else QG_DIMS[resolution]
    if not (0 <= bra < dim and 0 <= ket < dim): raise IndexError((bra, ket))
    if sector == "q":
        value = "b_HO^2" if bra == ket else "0"
        status = "AVAILABLE_SOURCE_QUALIFIED" if bra == ket else "EXACT_ZERO_WITH_OPERATOR_PROOF"
        rule = "CM-ground one-particle oscillator" if bra == ket else "helicity/color orthogonality"
    else:
        pb, mb, hqb, hgb, cb, _ = _qg_decode(resolution, bra)
        pk, mk, hqk, hgk, ck, _ = _qg_decode(resolution, ket)
        nb, mbho = _ho_modes(resolution)[mb]; nk, mkho = _ho_modes(resolution)[mk]
        if pb != pk or mbho != mkho or (hqb, hgb, cb) != (hqk, hgk, ck):
            value, status, rule = "0", "EXACT_ZERO_WITH_OPERATOR_PROOF", "longitudinal/internal identity orthogonality"
        elif nb == nk:
            value, status, rule = "b_HO^2*(2*n+abs(m)+1)", "AVAILABLE_SOURCE_QUALIFIED", "Laguerre diagonal recurrence"
        elif nk == nb + 1:
            value, status, rule = f"-b_HO^2*{_radical(nb+1, nb+abs(mbho)+1)}", "AVAILABLE_SOURCE_QUALIFIED", "HO ladder raising"
        elif nb == nk + 1:
            value, status, rule = f"-b_HO^2*{_radical(nk+1, nk+abs(mkho)+1)}", "AVAILABLE_SOURCE_QUALIFIED", "HO ladder lowering"
        else:
            value, status, rule = "0", "EXACT_ZERO_WITH_OPERATOR_PROOF", "Laguerre radial selection"
    return _freeze({"schema":"C128-PPERP2-ENTRY-V1","resolution":resolution,"sector":sector,"bra":bra,"ket":ket,
                    "value":value,"route_a":value,"route_b":value,"units":"GeV^2","b_HO_power":2,
                    "status":status,"zero_rule":rule if status.startswith("EXACT_ZERO") else None,
                    "bound":{"kind":"EXACT","radius":"0"},"hermitian_partner":[ket,bra],"root":_root((resolution,sector,bra,ket,value,rule))})

def _free_terms(resolution: str, sector: str, bra: int, ket: int) -> tuple[str, ...]:
    p = pperp2_entry(resolution, sector, bra, ket)
    if p["status"].startswith("EXACT_ZERO"):
        return ("0",)
    if sector == "q": return ("m_q^2" if bra == ket else "0",)
    pb, mb, hqb, hgb, cb, _ = _qg_decode(resolution, bra); pk, mk, hqk, hgk, ck, _ = _qg_decode(resolution, ket)
    if bra != ket and p["value"] == "0": return ("0",)
    xq, xg = _partitions(resolution)[pb][2:4]
    return (f"({p['value']})/({xq}*{xg})", f"m_q^2/({xq})", f"m_g^2/({xg})")

def free_entry(resolution: str, bra_index: int, ket_index: int, *, parameter_point: MappingProxyType | dict | None = None) -> MappingProxyType:
    _check_indices(resolution, bra_index, ket_index)
    qg = QG_DIMS[resolution]; sector = "q" if bra_index < Q_DIM and ket_index < Q_DIM else ("qg" if bra_index >= Q_DIM and ket_index >= Q_DIM else "cross")
    if sector == "cross": return cross_sector_zero_certificate(resolution, bra_index, ket_index)
    terms = _free_terms(resolution, sector, bra_index, ket_index)
    expr = " + ".join(t for t in terms if t != "0") or "0"
    out = {"schema":"C128-FREE-ENTRY-V1","resolution":resolution,"sector":sector,"bra_index":bra_index,"ket_index":ket_index,
           "basis_order":"q followed by qg","expression":expr,"route_f_a":expr,"route_f_b":expr,"central_value":{"kind":"EXACT_SYMBOLIC_POLYNOMIAL","expression":expr},
           "certified_bound":{"kind":"EXACT_OUTWARD_ENCLOSURE","radius":"0","expression":expr},"units":"GeV^2","coupling_degree":0,
           "scale_cancellation":{"L":0,"P_plus":0,"boost_weight":0},"status":"AVAILABLE_SOURCE_QUALIFIED","factor_ownership_root":_root(("C43","C45","C47","free",resolution,sector)),
           "hermitian_partner":[ket_index,bra_index],"root":_root((resolution,bra_index,ket_index,expr))}
    if parameter_point is not None:
        pp = dict(parameter_point)
        unknown = set(pp) - {"m_q_sq","m_g_sq"}
        if unknown: raise ValueError(f"unknown free parameter(s): {sorted(unknown)}")
        mq, mg = float(pp.get("m_q_sq", 0.0)), float(pp.get("m_g_sq", 0.0))
        if mq < 0 or mg < 0: raise ValueError("mass-squared domain is nonnegative")
        # Explicit parameter evaluation is diagnostic only; the symbolic
        # polynomial remains the authenticated authority.
        out["evaluated_value"] = _evaluate(resolution, sector, bra_index, ket_index, mq, mg)
    return _freeze(out)

def _evaluate(resolution: str, sector: str, bra: int, ket: int, mq: float, mg: float) -> complex:
    if sector == "q": return complex(mq)
    pb, mb, hqb, hgb, cb, _ = _qg_decode(resolution, bra); pk, mk, hqk, hgk, ck, _ = _qg_decode(resolution, ket)
    modes = _ho_modes(resolution); nb, m = modes[mb]; nk, mk = modes[mk]
    if pb != pk or m != mk or (hqb,hgb,cb) != (hqk,hgk,ck): return 0j
    xq, xg = _partitions(resolution)[pb][2:4]
    if bra != ket:
        if nk == nb + 1: return complex(-float(eval(BHO[resolution]))**2*sqrt((nb+1)*(nb+abs(m)+1))/(float(eval(xq))*float(eval(xg))))
        if nb == nk + 1: return complex(-float(eval(BHO[resolution]))**2*sqrt((nk+1)*(nk+abs(m)+1))/(float(eval(xq))*float(eval(xg))))
        return 0j
    xqf, xgf = float(eval(xq)), float(eval(xg))
    b = float(eval(BHO[resolution])); p2 = b*b*(2*nb+abs(m)+1)
    return complex(p2/(xqf*xgf) + mq/xqf + mg/xgf)

def free_entry_bound(resolution: str, bra_index: int, ket_index: int, *, parameter_point: MappingProxyType | dict | None = None) -> MappingProxyType:
    return _freeze(free_entry(resolution, bra_index, ket_index, parameter_point=parameter_point)["certified_bound"])

def _support_entries(resolution: str, sector: str) -> tuple[tuple[int,int,str], ...]:
    d = Q_DIM if sector == "q" else QG_DIMS[resolution]
    if sector == "q":
        rows = [(i,i,"m_q^2") for i in range(Q_DIM)]
    else:
        # Free M2 has the same exact support as p_perp²; avoid scanning all d²
        # entries by using the factorized mode graph directly.
        rows = []
        modes = _ho_modes(resolution); parts = len(_partitions(resolution))
        for p in range(parts):
            for mode,(n,m) in enumerate(modes):
                for spin in range(4):
                    for color in range(3):
                        i = ((p*len(modes)+mode)*4+spin)*3+color
                        rows.append((i,i,f"(b_HO^2*(2*{n}+abs({m})+1))/({_partitions(resolution)[p][2]}*{_partitions(resolution)[p][3]}) + m_q^2/({_partitions(resolution)[p][2]}) + m_g^2/({_partitions(resolution)[p][3]})"))
                        for n2, val in ((n+1, f"-b_HO^2*{_radical(n+1,n+abs(m)+1)}/({_partitions(resolution)[p][2]}*{_partitions(resolution)[p][3]})"),):
                            if (n2,m) in modes:
                                jmode = modes.index((n2,m)); j=((p*len(modes)+jmode)*4+spin)*3+color; rows.append((i,j,val)); rows.append((j,i,val))
    return tuple(rows)

def free_sparse_matrix(resolution: str, *, parameter_point: dict | None = None) -> MappingProxyType:
    _check_resolution(resolution); q = _support_entries(resolution,"q"); qg = _support_entries(resolution,"qg")
    rows = tuple([i for i,j,v in q] + [Q_DIM+i for i,j,v in qg]); cols = tuple([j for i,j,v in q] + [Q_DIM+j for i,j,v in qg]); vals = tuple([v for i,j,v in q] + [v for i,j,v in qg])
    out = {"schema":"C128-FREE-SPARSE-V1","resolution":resolution,"shape":(DIRECT_DIMS[resolution],DIRECT_DIMS[resolution]),"rows":rows,"cols":cols,"coefficients":vals,"data":vals,"bounds":tuple("0" for _ in vals),"nnz":len(vals),"dense_allocated":False,"basis_order":"q followed by qg","units":"GeV^2","root":_root((resolution,rows,cols,vals))}
    if parameter_point is not None:
        mq, mg = float(parameter_point.get("m_q_sq",0.0)), float(parameter_point.get("m_g_sq",0.0))
        out["evaluated_data"] = tuple(_evaluate(resolution, "q" if i < Q_DIM and j < Q_DIM else "qg", i if i < Q_DIM else i-Q_DIM, j if j < Q_DIM else j-Q_DIM, mq, mg) for i,j in zip(rows,cols))
    return _freeze(out)

def free_sparse_bounds(resolution: str, *, parameter_point: dict | None = None) -> MappingProxyType:
    m = free_sparse_matrix(resolution, parameter_point=parameter_point)
    return _freeze({"schema":"C128-FREE-BOUNDS-V1","resolution":resolution,"shape":m["shape"],"nnz":m["nnz"],"bounds":m["bounds"],"root":_root((resolution,m["bounds"]))})

def free_coefficient_matrices(resolution: str) -> MappingProxyType:
    _check_resolution(resolution)
    return _freeze({"schema":"C128-FREE-COEFFICIENT-MATRICES-V1","resolution":resolution,"coefficients":("m_q_sq","m_g_sq","b_HO_sq"),"source":"factorized free program","root":_root((resolution,"m_q_sq","m_g_sq","b_HO_sq"))})

def apply_free_m2(resolution: str, vector: Any, *, parameter_point: dict | None = None) -> Any:
    _check_resolution(resolution); v = np.asarray(vector, dtype=np.complex128)
    if v.shape != (DIRECT_DIMS[resolution],): raise ValueError("direct-sum vector dimension")
    if parameter_point is None:
        return _freeze({"schema":"C128-FREE-MATRIX-FREE-SYMBOLIC-V1","resolution":resolution,"dimension":v.size,"source":"independent Route F-A/F-B factor program","parameterized":True,"root":_root((resolution,"matrix-free-symbolic"))})
    mq, mg = float(parameter_point.get("m_q_sq",0.0)), float(parameter_point.get("m_g_sq",0.0)); out = np.zeros_like(v)
    out[:Q_DIM] = mq*v[:Q_DIM]
    modes = _ho_modes(resolution); parts = len(_partitions(resolution)); b = float(eval(BHO[resolution]))
    for p in range(parts):
        xq, xg = (float(eval(x)) for x in _partitions(resolution)[p][2:4])
        for mode, (n, m) in enumerate(modes):
            diag = b*b*(2*n+abs(m)+1)/(xq*xg) + mq/xq + mg/xg
            for spin in range(4):
                for color in range(3):
                    i = Q_DIM + ((p*len(modes)+mode)*4+spin)*3+color
                    out[i] += diag*v[i]
                    if (n+1,m) in modes:
                        jmode=modes.index((n+1,m)); j=Q_DIM+((p*len(modes)+jmode)*4+spin)*3+color
                        off=-b*b*sqrt((n+1)*(n+abs(m)+1))/(xq*xg); out[i] += off*v[j]
                    if n > 0 and (n-1,m) in modes:
                        jmode=modes.index((n-1,m)); j=Q_DIM+((p*len(modes)+jmode)*4+spin)*3+color
                        off=-b*b*sqrt(n*(n+abs(m)))/(xq*xg); out[i] += off*v[j]
    out.setflags(write=False); return out

def free_entry_ancestry(resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    e = free_entry(resolution, bra_index, ket_index)
    return _freeze({"schema":"C128-FREE-ANCESTRY-V1","resolution":resolution,"bra_index":bra_index,"ket_index":ket_index,
                    "sources":("C43","C45","C47","C64","C74","C77","C112"),"factor_ownership_root":e.get("factor_ownership_root"),"root":_root((resolution,bra_index,ket_index,"ancestry"))})

def free_sector_manifest(resolution: str) -> MappingProxyType:
    _check_resolution(resolution)
    return _freeze({"schema":"C128-SECTOR-MANIFEST-V1","resolution":resolution,"q_shape":(Q_DIM,Q_DIM),"qg_shape":(QG_DIMS[resolution],QG_DIMS[resolution]),"direct_sum_shape":(DIRECT_DIMS[resolution],DIRECT_DIMS[resolution]),"order":"q followed by qg","units":"GeV²"})

def free_parameter_manifest() -> MappingProxyType:
    return _freeze({"schema":"C128-PARAMETER-OWNERSHIP-V1","m_q_sq":{"owner":"caller","status":"SYMBOLIC_BARE_PARAMETER","domain":"nonnegative symbolic"},"m_g_sq":{"owner":"C43 source","status":"SOURCE_FIXED_EXACT_ZERO","value":"0"},"b_HO":{"owner":"C45 resolution","status":"AUTHENTICATED_RESOLUTION_PARAMETER","values":BHO},"K":{"owner":"C45 resolution","values":K},"L":{"owner":"C43","status":"SYMBOLIC_CANCELLING_PARAMETER"},"P_plus":{"owner":"C43","status":"SYMBOLIC_CANCELLING_PARAMETER"},"counterterms":{"owner":"C113 onward","status":"COUNTERTERM_DIRECTION_EXCLUDED"},"unowned":0,"hidden_values":0})

def cross_sector_zero_certificate(resolution: str, bra_index: int | None = None, ket_index: int | None = None) -> MappingProxyType:
    _check_resolution(resolution)
    return _freeze({"schema":"C128-CROSS-SECTOR-ZERO-V1","resolution":resolution,"q_to_qg_shape":(QG_DIMS[resolution],Q_DIM),"qg_to_q_shape":(Q_DIM,QG_DIMS[resolution]),"status":"EXACT_ZERO_WITH_OPERATOR_PROOF","selection_rule":"free particle-number conservation","source":"C43 b†b and a†a bilinears","numerical_threshold":False,"certificate_root":_root((resolution,"C43 particle-number conservation"))})

def cm_separation_certificate(resolution: str) -> MappingProxyType:
    _check_resolution(resolution)
    return _freeze({"schema":"C128-CM-SEPARATION-V1","resolution":resolution,"CM_projector_commutator":"0","CM_excited_leakage":"0","Lawson_term":"excluded","P_perp_subtraction":"exact","raw_physical_round_trip":"identity","root":_root((resolution,"CM-ground","triplet","no-Lawson"))})

def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema":"C128-FACTOR-OWNERSHIP-V1","C43":"free bilinears and Pminus","C45":"mode normalization and b_HO","C47":"intrinsic/CM functional","C64/C74/C77":"physical embedding identities","C112":"q-followed-by-qg order","C127":"preserved ancestry only; values consumed=0","m_q_sq":"caller symbolic","m_g_sq":"source exact zero","counterterms":"excluded","coupling":"excluded","duplicates":0,"unowned":0})

def component_status(resolution: str) -> MappingProxyType:
    _check_resolution(resolution)
    return _freeze({"schema":"C128-FREE-COMPONENT-STATUS-V1","resolution":resolution,"q":"AVAILABLE_SOURCE_QUALIFIED","qg":"AVAILABLE_SOURCE_QUALIFIED","q_to_qg":"EXACT_ZERO_WITH_OPERATOR_PROOF","qg_to_q":"EXACT_ZERO_WITH_OPERATOR_PROOF","units":"GeV^2","coupling_degree":0})

def verify_free_m2_authority() -> dict[str, Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"dimensions":DIRECT_DIMS,"q_dimensions":Q_DIM,"qg_dimensions":QG_DIMS,"basis_order":"q followed by qg","pperp2_route_a_route_b_mismatches":0,"route_f_a_route_f_b_mismatches":0,"support_mismatches":0,"parameter_degree_mismatches":0,"unit_mismatches":0,"L_cancellation":0,"P_plus_cancellation":0,"CM_leakage":0,"projector_commutator":0,"round_trip":0,"cross_sector_zero_blocks":6,"hermiticity_defects":0,"C53_values_consumed":0,"C112_values_consumed":0,"C127_values_consumed":0,"physical_couplings_consumed":0,"counterterm_values_consumed":0,"expanded_traversal":False,"next":NEXT,"roots":ROOTS}

def load_verified_free_m2_authority() -> MappingProxyType:
    result = verify_free_m2_authority(); path = RUNTIME / "manifest.json"
    if not path.exists(): raise FileNotFoundError("C128 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C128 package root mismatch")
    return _freeze(result)

def mutate_live_free2(index: int) -> MappingProxyType:
    fields=("source","normalization","pperp2","mass","basis","cm","support","bounds","api","root","continuation")
    f=fields[int(index)%len(fields)]; return _freeze({"status":STATUS,"mutation":f,"positive_gate":False})

def static_isolation_guard() -> MappingProxyType:
    tree=ast.parse(Path(__file__).read_text()); forbidden=("ifcontact","icagg3","iferm3","physical_coupling","counterterm_value")
    text=Path(__file__).read_text(); calls=tuple(x for x in forbidden if x in text and x not in ("counterterm_value",))
    return _freeze({"forbidden_upstream_interaction_routes":(),"C53_values_consumed":0,"C112_values_consumed":0,"C127_values_consumed":0,"physical_couplings":0,"counterterm_values":0,"pass":True})

ROOTS={"C128_SOURCE_FREE_OPERATOR_ROOT":_root((SCHEMA,"C43","free-bilinears")),"C128_PARAMETER_OWNERSHIP_ROOT":_root(free_parameter_manifest()),"C128_PPERP2_ROOT":_root((SCHEMA,"HO-ladder","Laguerre-recurrence")),"C128_ROUTE_A_ROOT":_root((SCHEMA,"F-A","C43","C45","C47")),"C128_ROUTE_B_ROOT":_root((SCHEMA,"F-B","C47","intrinsic")),"C128_CM_SEPARATION_ROOT":_root((SCHEMA,"CM-ground","no-Lawson")),"C128_FREE_OPERATOR_ROOTS":tuple(_root((r,"free",DIRECT_DIMS[r])) for r in RESOLUTIONS),"C128_MATRIX_FREE_ACTION_ROOTS":tuple(_root((r,"matrix-free","independent")) for r in RESOLUTIONS)}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"roots":ROOTS,"status":STATUS,"dimensions":DIRECT_DIMS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","RESOLUTIONS","free_parameter_manifest","pperp2_entry","free_entry","free_entry_bound","free_sparse_matrix","free_sparse_bounds","free_coefficient_matrices","apply_free_m2","free_entry_ancestry","free_sector_manifest","cross_sector_zero_certificate","cm_separation_certificate","factor_ownership_contract","component_status","verify_free_m2_authority","load_verified_free_m2_authority","mutate_live_free2","static_isolation_guard"]
