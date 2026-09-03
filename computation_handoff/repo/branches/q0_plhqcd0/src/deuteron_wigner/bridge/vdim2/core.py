"""C52 executable, source-owned component layer for C50's canonical vertex.

The C43 action has one additive canonical ``b† a† b`` term.  C50's named
mass/helicity-flip and transverse/helicity structures are substructures of the
same covariant spinor bilinear, not separately source-defined action terms.
Consequently C52 keeps one operator component and never obtains a component by
subtracting or fitting C50's combined result.  C50 is a recomposition holdout.

This is deliberately color stripped.  It builds no SU(3), triplet, physical
emission, adjoint, or other local-QCD matrix.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import inspect
import json
from math import pi, sqrt
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix

from ..basis1.core import q_basis, qg_basis, resolutions
from ..modes.core import GAMMA, ho_momentum
from ..vsrc import core as c50

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "d074e45e68f04994a4fc8b7979b33d0a99fc0c42"
STATUS = "C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY"
NEXT = "C53/VERTEX2 — exact SU(3)/triplet physical canonical-vertex assembly and adjoint closure"
COMPONENT_ID = "C43_QQG_BDAGGER_ADAGGER_B_COVARIANT_BILINEAR"
PPLUS, KG = sp.symbols("P_plus k_g", positive=True)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def array_hash(value: np.ndarray) -> str:
    a = np.ascontiguousarray(value)
    return sha256(a.dtype.str.encode() + str(a.shape).encode() + a.tobytes()).hexdigest()


def code_hash() -> str:
    return sha256(Path(__file__).read_bytes()).hexdigest()


@dataclass(frozen=True)
class DimensionalSignature:
    mass: int
    L: int = 0
    P_plus: int = 0
    b_HO: int = 0
    regulator: str = "L_CANCELLED"
    operator: str = "DIMENSIONLESS_PRIMITIVE"
    transverse_rank: str = "MIXED_0_1"

    def as_dict(self) -> dict[str, Any]:
        return {"mass": self.mass, "L": self.L, "P_plus": self.P_plus, "b_HO": self.b_HO, "regulator": self.regulator, "operator": self.operator, "transverse_rank": self.transverse_rank}


@dataclass(frozen=True)
class SymbolicCoefficient:
    expression: sp.Expr
    signature: DimensionalSignature
    name: str

    def serialize(self) -> str:
        return sp.srepr(self.expression)

    @property
    def sha256(self) -> str:
        return sha256((self.name + self.serialize() + canonical_json(self.signature.as_dict())).encode()).hexdigest()

    def free_symbols(self) -> tuple[str, ...]:
        return tuple(sorted(str(x) for x in self.expression.free_symbols))

    def evaluate(self, **values: float) -> complex:
        mapping = {sp.Symbol(k, positive=True): v for k, v in values.items()}
        # SymPy symbols compare by assumptions, so map by name as well.
        mapping |= {x: values[str(x)] for x in self.expression.free_symbols if str(x) in values}
        return complex(self.expression.subs(mapping).evalf())


PMINUS_COEFFICIENT = SymbolicCoefficient(1 / sp.sqrt(2 * sp.pi * KG), DimensionalSignature(0, operator="P_MINUS_COEFFICIENT"), "FINITE_CELL_PMINUS")
M2_COEFFICIENT = SymbolicCoefficient(2 * PPLUS / sp.sqrt(2 * sp.pi * KG), DimensionalSignature(1, P_plus=1, operator="M2_COEFFICIENT"), "FINITE_CELL_M2")
PRIMITIVE_SIGNATURE = DimensionalSignature(1, operator="P_MINUS_PRIMITIVE", transverse_rank="MIXED_0_1")
PMINUS_SIGNATURE = DimensionalSignature(1, operator="P_MINUS_COMPONENT", transverse_rank="MIXED_0_1")
M2_SIGNATURE = DimensionalSignature(2, operator="M2_COMPONENT", transverse_rank="MIXED_0_1")


def component_vocabulary() -> dict[str, Any]:
    return {
        "independent_components": [{
            "id": COMPONENT_ID, "classification": "INDEPENDENT_SOURCE_COMPONENT", "primary_source": "hep-ph/0011372v2 Eq. (24); C43 action contract", "C50_derivation": "C50 plane-wave b_dagger a_dagger b derivation", "operator": "-g_s psibar gamma^mu T^a psi A_mu^a -> b_dagger a_dagger b", "meaning": "one covariant canonical quark--gluon bilinear before basis projection", "coupling_power": 1,
        }],
        "subterms": [
            {"id": "MASS_HELICITY_FLIP", "classification": "SUBTERM_NOT_SEPARATELY_GAUGE_OR_OPERATOR_MEANINGFUL", "reason": "C50 supplies no action-level additive operator or independent coefficient; it is a term inside the full C45 spinor bilinear."},
            {"id": "TRANSVERSE_HELICITY", "classification": "SUBTERM_NOT_SEPARATELY_GAUGE_OR_OPERATOR_MEANINGFUL", "reason": "C50 supplies no action-level additive operator or independent coefficient; it is a term inside the same covariant bilinear."},
        ],
    }


def _resolution(label: str):
    return next(r for r in resolutions() if r.label == label)


@lru_cache(maxsize=None)
def colorless_bases(label: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Use C47 physical basis IDs while removing only open color labels."""
    r = _resolution(label)
    qids = tuple(i for i, row in enumerate(q_basis(r)) if row[4] == 0)
    qgids = tuple(i for i, row in enumerate(qg_basis(r)[0]) if row[11] == 0)
    return qids, qgids


def selection_rule(incoming_q_basis_id: int, outgoing_qg_basis_id: int, resolution: str) -> str:
    r = _resolution(resolution); q = q_basis(r)[incoming_q_basis_id]; qg = qg_basis(r)[0][outgoing_qg_basis_id]
    _, kq, kg, _, _, _, m, _, _, hq, hg, _, _, _ = qg
    h_in = q[3]
    if kq + kg != r.K:
        return "ZERO_BY_LONGITUDINAL_SELECTION"
    if Fraction(h_in, 2) != Fraction(hq, 2) + hg + m:
        return "ZERO_BY_HELICITY_SELECTION"
    return "ADMITTED"


def _vector_spinor(pplus: np.ndarray, px: np.ndarray, py: np.ndarray, mass: float, helicity: int) -> np.ndarray:
    """Vectorized C45/BPP spinor, algebraically identical to modes.spinor."""
    pminus = (mass * mass + px * px + py * py) / (2.0 * pplus)
    E, pz = (pplus + pminus) / sqrt(2.0), (pplus - pminus) / sqrt(2.0)
    a = np.sqrt(E + mass).astype(np.complex128)
    out = np.zeros(pplus.shape + (4,), dtype=np.complex128)
    if helicity == 1:
        out[..., 0] = a; out[..., 2] = pz / a; out[..., 3] = (px + 1j * py) / a
    else:
        out[..., 1] = a; out[..., 2] = (px - 1j * py) / a; out[..., 3] = -pz / a
    return out


def _primitive_bilinear(*, kq: Fraction, kg: Fraction, K: Fraction, n: int, m: int, hq: int, hg: int, h_in: int, b: float, mass: float, total_pplus: float, nodes: int = 19) -> complex:
    """Independent C43/C45 plane-wave numerator followed by C45 HO projection.

    This does not call C50's combined evaluator or split its numerical output.
    """
    grid = np.linspace(-3.5 * b, 3.5 * b, nodes); dx = float(grid[1] - grid[0])
    X, Y = np.meshgrid(grid, grid, indexing="ij")
    xq, xg = float(kq / K), float(kg / K)
    uout = _vector_spinor(np.full_like(X, xq * total_pplus), sqrt(xg)*X, sqrt(xg)*Y, mass, hq)
    uin = _vector_spinor(np.full_like(X, total_pplus), np.zeros_like(X), np.zeros_like(X), mass, h_in)
    epsx, epsy = -hg / sqrt(2.0), -1j / sqrt(2.0)
    eminus = ((-sqrt(xq)*X) * epsx + (-sqrt(xq)*Y) * epsy) / (xg * total_pplus)
    ecart = np.stack((np.conjugate(eminus)/sqrt(2.0), np.full(X.shape, np.conjugate(epsx), dtype=np.complex128), np.full(X.shape, np.conjugate(epsy), dtype=np.complex128), -np.conjugate(eminus)/sqrt(2.0)), axis=-1)
    gamma_dot = (GAMMA[0][None,None] * ecart[...,0,None,None] - GAMMA[1][None,None] * ecart[...,1,None,None] - GAMMA[2][None,None] * ecart[...,2,None,None] - GAMMA[3][None,None] * ecart[...,3,None,None])
    ubar = np.einsum("...i,ij->...j", np.conjugate(uout), GAMMA[0])
    numerator = np.einsum("...i,...ij,...j->...", ubar, gamma_dot, uin)
    phi = ho_momentum(n, m, X, Y, b)
    return complex(np.sum(np.conjugate(phi) * numerator) * dx * dx / (2*pi)**2)


def evaluate_canonical_vertex_components(incoming_q_basis_id: int, outgoing_qg_basis_id: int, resolution: str, symbolic_parameters: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return executable source component values; C50 is never used as input."""
    r = _resolution(resolution); params = {"mass_GeV": 1.2, "P_plus_GeV": 3.0, "L": "symbolic", "g_s": "FACTORED"}
    if symbolic_parameters: params.update(symbolic_parameters)
    decision = selection_rule(incoming_q_basis_id, outgoing_qg_basis_id, resolution)
    qg = qg_basis(r)[0][outgoing_qg_basis_id]
    _, kq, kg, _, _, n, m, _, _, hq, hg, _, _, _ = qg
    if decision != "ADMITTED":
        primitive = 0j
    else:
        primitive = _primitive_bilinear(kq=kq, kg=kg, K=r.K, n=n, m=m, hq=hq, hg=hg, h_in=q_basis(r)[incoming_q_basis_id][3], b=r.b_GeV, mass=float(params["mass_GeV"]), total_pplus=float(params["P_plus_GeV"]))
    pcoef = PMINUS_COEFFICIENT.evaluate(k_g=float(kg))
    mcoef = M2_COEFFICIENT.evaluate(k_g=float(kg), P_plus=float(params["P_plus_GeV"]))
    pminus, m2 = pcoef*primitive, mcoef*primitive
    return {"status": "COMPONENT_EVALUATED" if decision == "ADMITTED" else decision, "raw_C47_tuple_value_consumed": False, "resolution": resolution, "incoming_q_basis_id": incoming_q_basis_id, "outgoing_qg_basis_id": outgoing_qg_basis_id, "selection_rule": decision, "combined_pminus_GeV": [pminus.real,pminus.imag], "combined_m2_GeV2": [m2.real,m2.imag], "components": [{"id": COMPONENT_ID, "symbolic_pminus": PMINUS_COEFFICIENT.serialize(), "symbolic_m2": M2_COEFFICIENT.serialize(), "symbolic_hashes": [PMINUS_COEFFICIENT.sha256, M2_COEFFICIENT.sha256], "primitive_GeV": [primitive.real,primitive.imag], "pminus_GeV": [pminus.real,pminus.imag], "m2_GeV2": [m2.real,m2.imag], "primitive_signature": PRIMITIVE_SIGNATURE.as_dict(), "pminus_signature": PMINUS_SIGNATURE.as_dict(), "m2_signature": M2_SIGNATURE.as_dict(), "ancestry": ["C43 Eq.24", "C45 spinor/polarization/HO", "C47 CM-clean basis", "C50 finite-cell normalization", "C50 component-wise 2Pplus conversion"]}], "parameters": params}


def recomposition_against_c50(incoming_q_basis_id: int, outgoing_qg_basis_id: int, resolution: str, parameters: dict[str, Any] | None = None) -> dict[str, Any]:
    """Independent holdout only; no C50 result can feed the C52 primitive."""
    params = {"mass_GeV": 1.2, "P_plus_GeV": 3.0, "g_s": 1.0, "L": "symbolic"}
    if parameters: params.update(parameters)
    derived = evaluate_canonical_vertex_components(incoming_q_basis_id, outgoing_qg_basis_id, resolution, params)
    c50_value = c50.evaluate_canonical_vertex(incoming_q_basis_id, outgoing_qg_basis_id, resolution, params)
    a, b = complex(*derived["combined_pminus_GeV"]), complex(*c50_value["pminus_GeV"])
    c, d = complex(*derived["combined_m2_GeV2"]), complex(*c50_value["m2_GeV2"])
    return {"pminus_residual": abs(a-b), "m2_residual": abs(c-d), "derived": derived, "C50_holdout": c50_value}


@lru_cache(maxsize=None)
def component_domain(resolution: str) -> tuple[tuple[int,int,str], ...]:
    qids, qgids = colorless_bases(resolution)
    return tuple((iq, io, selection_rule(iq, io, resolution)) for io in qgids for iq in qids)


@lru_cache(maxsize=None)
def assemble_colorless_component_family(resolution: str, mass: float = 1.2, pplus: float = 3.0) -> dict[str, Any]:
    """Exhaustive colorless primitive and diagnostic M2 matrices; no SU(3)."""
    qids, qgids = colorless_bases(resolution); qi = {x:i for i,x in enumerate(qids)}; oi = {x:i for i,x in enumerate(qgids)}
    row=[]; col=[]; primitive=[]; m2=[]; ledger=[]
    for iq, io, status in component_domain(resolution):
        rec = {"incoming_q_basis_id":iq,"outgoing_qg_basis_id":io,"status":status,"component_id":COMPONENT_ID}
        if status == "ADMITTED":
            value = evaluate_canonical_vertex_components(iq,io,resolution,{"mass_GeV":mass,"P_plus_GeV":pplus})
            z = complex(*value["components"][0]["primitive_GeV"]); zz = complex(*value["components"][0]["m2_GeV2"])
            rec["status"] = "COMPONENT_NONZERO" if abs(z)>1e-14 else "COMPONENT_EXACT_ZERO"
            rec["primitive_hash"] = sha256(np.asarray([z.real,z.imag],dtype=np.float64).tobytes()).hexdigest()
            if abs(z)>1e-14: row.append(oi[io]); col.append(qi[iq]); primitive.append(z); m2.append(zz)
        else: rec["status"] = "PRESELECTION_FORBIDDEN_EXACT"
        ledger.append(rec)
    shape=(len(qgids),len(qids)); prim=csr_matrix((np.asarray(primitive), (row,col)),shape=shape,dtype=np.complex128); diag=csr_matrix((np.asarray(m2),(row,col)),shape=shape,dtype=np.complex128)
    return {"resolution":resolution,"qids":qids,"qgids":qgids,"ledger":ledger,"primitive":prim,"diagnostic_m2":diag,"primitive_hash":array_hash(prim.toarray()),"diagnostic_m2_hash":array_hash(diag.toarray()),"counts":{x:sum(1 for r in ledger if r["status"]==x) for x in sorted({r["status"] for r in ledger})}}


def apply_colorless_vertex_components(vector_q: np.ndarray, resolution: str, symbolic_parameters: dict[str, Any] | None = None) -> dict[str, np.ndarray]:
    """Independent direct component action; it never multiplies a stored matrix."""
    qids, qgids = colorless_bases(resolution); vector_q=np.asarray(vector_q,dtype=np.complex128)
    if vector_q.shape != (len(qids),): raise ValueError("colorless q vector shape mismatch")
    out=np.zeros(len(qgids),dtype=np.complex128); oi={x:i for i,x in enumerate(qgids)}; qi={x:i for i,x in enumerate(qids)}
    for iq,io,status in component_domain(resolution):
        if status == "ADMITTED": out[oi[io]] += complex(*evaluate_canonical_vertex_components(iq,io,resolution,symbolic_parameters)["combined_m2_GeV2"])*vector_q[qi[iq]]
    return {COMPONENT_ID:out,"sum":out.copy()}


def static_raw_tuple_guard() -> dict[str, Any]:
    import ast
    tree=ast.parse(inspect.getsource(evaluate_canonical_vertex_components))
    names={x.id for x in ast.walk(tree) if isinstance(x,ast.Name)} | {x.attr for x in ast.walk(tree) if isinstance(x,ast.Attribute)}
    forbidden=("canonical_kernel", "tuple_semantics_records", "raw_tuple_semantics_summary", "vertex1")
    found=tuple(x for x in forbidden if x in names)
    return {"forbidden":forbidden,"found":found,"pass":not bool(found),"guard":"AST_COMPONENT_EVALUATOR_RAW_VALUE_GUARD"}


@lru_cache(maxsize=1)
def run_c52_checks() -> dict[str, Any]:
    # Every frozen C50 holdout is an independent descendant check.  Exact
    # selection-rule zeros remain zeros up to the C50 quadrature residual.
    holds=[]
    for sample in c50.run_c50_checks()["samples"]:
        holds.append(recomposition_against_c50(sample["incoming_q_basis_id"],sample["outgoing_qg_basis_id"],sample["resolution"]))
    return {"status":STATUS,"raw_guard":static_raw_tuple_guard(),"max_pminus_recomposition_residual":max(x["pminus_residual"] for x in holds),"max_m2_recomposition_residual":max(x["m2_residual"] for x in holds),"holds":holds,"pass":static_raw_tuple_guard()["pass"] and max(x["pminus_residual"] for x in holds)<2e-12 and max(x["m2_residual"] for x in holds)<2e-11}


@lru_cache(maxsize=1)
def runtime_raw_tuple_poisoning() -> dict[str, Any]:
    """C52 component result survives a poisoned historical tuple producer."""
    from unittest.mock import patch
    from ..basis1 import core as basis1
    before=evaluate_canonical_vertex_components(3,3,"K9_2_N8_b0.40")
    def poison(*_args,**_kwargs): raise AssertionError("C47_RAW_VALUE_READ")
    with patch.object(basis1,"canonical_kernel",poison): after=evaluate_canonical_vertex_components(3,3,"K9_2_N8_b0.40")
    return {"before":sha256(canonical_json(before).encode()).hexdigest(),"after":sha256(canonical_json(after).encode()).hexdigest(),"pass":before==after,"historical_component_metadata_read":False}


def validate_c52(value: dict[str, Any]) -> bool:
    expected=run_c52_checks(); poison=runtime_raw_tuple_poisoning()
    return value==expected and value["pass"] and poison["pass"] and component_vocabulary()["independent_components"][0]["id"]==COMPONENT_ID


def mutate_live_c52(fault_id: int) -> dict[str, Any]:
    value=json.loads(canonical_json(run_c52_checks())); mode=fault_id%10
    if mode==0: value["raw_guard"]["pass"]=False
    elif mode==1: value["raw_guard"]["found"]=["canonical_kernel"]
    elif mode==2: value["max_pminus_recomposition_residual"]=1.0
    elif mode==3: value["max_m2_recomposition_residual"]=1.0
    elif mode==4: value["holds"][0]["derived"]["raw_C47_tuple_value_consumed"]=True
    elif mode==5: value["holds"][0]["derived"]["components"][0]["pminus_signature"]["mass"]=2
    elif mode==6: value["holds"][0]["derived"]["components"][0]["symbolic_hashes"][0]="0"*64
    elif mode==7: value["holds"][0]["derived"]["components"].append(value["holds"][0]["derived"]["components"][0])
    elif mode==8: value["holds"][0]["derived"]["selection_rule"]="ZERO_BY_OAM_SELECTION"
    else: value["pass"]=False
    return value
