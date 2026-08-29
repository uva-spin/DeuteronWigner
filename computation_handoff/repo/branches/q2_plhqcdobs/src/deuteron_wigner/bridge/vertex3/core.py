"""C53 physical color insertion for C52's one canonical bilinear.

The two assembly paths are intentionally distinct: one contracts C52
kinematics with the reduced C45/C47 triplet intertwiner, while the other maps
to all 24 product-color states with the raw emission tensor and then applies
the frozen triplet isometry.  No historical C47 canonical tuple is imported.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
import inspect
import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

import numpy as np
from scipy.sparse import bmat, csr_matrix, kron

from ..basis1.core import triplet_isometry
from ..modes.core import color_triplet_projector, gell_mann
from ..vdim2 import core as c52

ROOT=Path(__file__).resolve().parents[4]
BASELINE="949af3ad83ea4a384c9142784251dfd06254b5fd"
STATUS="C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY"
NEXT="C54/HQCD2 — assemble the remaining local-QCD operator substrate and projected action identity"
CF=4.0/3.0


def canonical_json(value: Any)->str: return json.dumps(value,sort_keys=True,separators=(",",":"),default=str)
def array_hash(a: np.ndarray)->str:
    x=np.ascontiguousarray(a); return sha256(x.dtype.str.encode()+str(x.shape).encode()+x.tobytes()).hexdigest()


@lru_cache(maxsize=1)
def color_data()->dict[str,Any]:
    projector,total,T=color_triplet_projector(); U=triplet_isometry()
    # Product order is (outgoing fundamental c', adjoint a), exactly C45/C47.
    E=np.stack([T[a] for a in range(8)],axis=1).reshape(24,3)
    f=np.empty((8,8,8),float); dd=np.empty((8,8,8),float)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                f[a,b,c]=float((-2j*np.trace((T[a]@T[b]-T[b]@T[a])@T[c])).real)
                dd[a,b,c]=float((2*np.trace((T[a]@T[b]+T[b]@T[a])@T[c])).real)
    F=-1j*f
    PE=E@E.conj().T/CF; PU=U@U.conj().T; C=U.conj().T@E; W=C/sqrt_cf()
    return {"T":T,"total":total,"U":U,"E":E,"P_E":PE,"P_U":PU,"C":C,"W":W,"projector":projector,"f":f,"d":dd,"F":F}


def sqrt_cf()->float: return float(np.sqrt(CF))


def color_validation()->dict[str,Any]:
    d=color_data(); T,total,U,E,PE,PU,C,W=d["T"],d["total"],d["U"],d["E"],d["P_E"],d["P_U"],d["C"],d["W"]
    f,ds,F=d["f"],d["d"],d["F"]
    identity=np.eye(3)
    commutator=max(
        np.linalg.norm(T[a]@T[b]-T[b]@T[a]-1j*sum(f[a,b,c]*T[c] for c in range(8)))
        for a in range(8) for b in range(8)
    )
    anticommutator=max(
        np.linalg.norm(T[a]@T[b]+T[b]@T[a]-(identity*(1.0/3.0 if a==b else 0.0)+sum(ds[a,b,c]*T[c] for c in range(8))))
        for a in range(8) for b in range(8)
    )
    adjoint_algebra=max(
        np.linalg.norm(F[a]@F[b]-F[b]@F[a]-1j*sum(f[a,b,c]*F[c] for c in range(8)))
        for a in range(8) for b in range(8)
    )
    return {
        "su3_hermiticity":max(float(np.linalg.norm(t-t.conj().T)) for t in T), "su3_traceless":max(float(abs(np.trace(t))) for t in T),
        "fundamental_casimir":float(np.linalg.norm(sum(t@t for t in T)-CF*np.eye(3))), "E_shape":list(E.shape), "E_rank":int(np.linalg.matrix_rank(E,tol=1e-11)),
        "commutator":float(commutator), "anticommutator":float(anticommutator),
        "f_contraction":float(np.linalg.norm(np.einsum("acd,bcd->ab",f,f)-3*np.eye(8))),
        "d_contraction":float(np.linalg.norm(np.einsum("acd,bcd->ab",ds,ds)-(5.0/3.0)*np.eye(8))),
        "adjoint_algebra":float(adjoint_algebra),
        "E_singular_values":np.linalg.svd(E,compute_uv=False).tolist(), "E_norm":float(np.linalg.norm(E)), "E_casimir":float(np.linalg.norm(E.conj().T@E-CF*np.eye(3))),
        "intertwining":float(max(np.linalg.norm(total[a]@E-E@T[a]) for a in range(8))), "projector_equivalence":float(np.linalg.norm(PU-PE)),
        "projector_idempotence":float(max(np.linalg.norm(PU@PU-PU),np.linalg.norm(PE@PE-PE))), "projector_hermiticity":float(max(np.linalg.norm(PU-PU.conj().T),np.linalg.norm(PE-PE.conj().T))),
        "triplet_rank":int(np.linalg.matrix_rank(PU,tol=1e-11)), "leakage":float(np.linalg.norm((np.eye(24)-PU)@E)), "C":C,
        "C_rank":int(np.linalg.matrix_rank(C,tol=1e-11)), "C_singular_values":np.linalg.svd(C,compute_uv=False).tolist(),
        "C_left":float(np.linalg.norm(C.conj().T@C-CF*np.eye(3))), "C_right":float(np.linalg.norm(C@C.conj().T-CF*np.eye(3))),
        "W_unitary": float(
            max(np.linalg.norm(W.conj().T @ W - np.eye(3)), np.linalg.norm(W @ W.conj().T - np.eye(3)))
        ),
        "C_covariance": float(
            max(np.linalg.norm((U.conj().T @ total[a] @ U) @ C - C @ T[a]) for a in range(8))
        ),
        "pass": True,
    }


@lru_cache(maxsize=None)
def assemble_physical_vertex(resolution: str)->dict[str,Any]:
    """Assemble primitive and diagnostic physical emission by both color paths."""
    f=c52.assemble_colorless_component_family(resolution); d=color_data(); I=f["primitive"]; D=f["diagnostic_m2"]; E,U,C=d["E"],d["U"],d["C"]
    reduced_primitive=kron(I,csr_matrix(C),format="csr"); reduced_diagnostic=kron(D,csr_matrix(C),format="csr")
    # Full product color -> frozen triplet projection. Exact factor ordering:
    # (kinematic row, c',a) and (kinematic col,c), followed by U† per row.
    full_primitive=kron(I,csr_matrix(E),format="csr"); full_diagnostic=kron(D,csr_matrix(E),format="csr")
    project=kron(csr_matrix(np.eye(I.shape[0])),csr_matrix(U.conj().T),format="csr")
    projected_primitive=(project@full_primitive).tocsr(); projected_diagnostic=(project@full_diagnostic).tocsr()
    if reduced_primitive.shape!=projected_primitive.shape: raise AssertionError("physical color ordering mismatch")
    return {"resolution":resolution,"colorless":f,"primitive":reduced_primitive,"diagnostic":reduced_diagnostic,"full_projected_primitive":projected_primitive,"full_projected_diagnostic":projected_diagnostic,"assembly_residual":float(max(np.linalg.norm((reduced_primitive-projected_primitive).toarray()),np.linalg.norm((reduced_diagnostic-projected_diagnostic).toarray()))),"primitive_hash":array_hash(reduced_primitive.toarray()),"diagnostic_hash":array_hash(reduced_diagnostic.toarray()),"shape":reduced_primitive.shape}


def apply_physical_canonical_emission(vector_q: np.ndarray,resolution: str,symbolic_parameters: dict[str,Any]|None=None,*,route: str="reduced")->np.ndarray:
    """Direct color action using C52 matrix-free kinematics, never C53 sparse data."""
    f=c52.assemble_colorless_component_family(resolution); nkin_q=f["primitive"].shape[1]; nkin_qg=f["primitive"].shape[0]
    v=np.asarray(vector_q,dtype=np.complex128)
    if v.shape!=(3*nkin_q,): raise ValueError("physical q vector shape mismatch")
    d=color_data(); C,E,U=d["C"],d["E"],d["U"]
    # q physical ordering is (kinematic spin, fundamental color), as C47 q rows.
    kin_by_color=[]
    for c in range(3):
        source=v.reshape(nkin_q,3)[:,c]
        kin_by_color.append(np.zeros(nkin_qg,complex) if not np.any(source) else c52.apply_colorless_vertex_components(source,resolution,symbolic_parameters)["sum"])
    kin=np.stack(kin_by_color,axis=1) # kinematic output x fundamental color
    if route=="reduced": out=np.einsum("rc,ic->ir",C,kin)
    elif route=="full_product": out=np.einsum("pac,ic->ipa",E.reshape(3,8,3),kin).reshape(nkin_qg,24)@U.conj()
    else: raise ValueError("route must be reduced or full_product")
    return out.reshape(-1)


def matrix_free_physical_columns(resolution: str, *, route: str="reduced") -> np.ndarray:
    """All physical q unit-vector actions from C52 direct calls, not C53 data.

    This is deliberately a column-action reconstruction: it invokes the C52
    evaluator on each colorless q unit vector and only then applies exact color.
    It never reads a C53 primitive or entry ledger.
    """
    f=c52.assemble_colorless_component_family(resolution); nq=f["primitive"].shape[1]
    direct=np.column_stack([c52.apply_colorless_vertex_components(np.eye(nq,dtype=complex)[:,j],resolution)["sum"] for j in range(nq)])
    d=color_data()
    if route=="reduced": return np.kron(direct,d["C"])
    if route=="full_product":
        # Keep the all-product-color intermediate as a rank-five tensor,
        # then contract U†.  Materializing its block-diagonal projector would
        # be a needless multi-gigabyte dense allocation at K=13/2.
        return np.einsum("bi,pac,par->bric", direct, d["E"].reshape(3,8,3), d["U"].conj().reshape(3,8,3)).reshape(direct.shape[0]*3,nq*3)
    raise ValueError("route must be reduced or full_product")


def triplet_rotation_holdout() -> dict[str,Any]:
    """A deterministic validation-only rotation; authoritative U is unchanged."""
    d=color_data(); U,C=d["U"],d["C"]
    phases=np.exp(1j*np.array([0.37,-0.83,1.19])); R=np.diag(phases)
    Ur=U@R; Cr=Ur.conj().T@d["E"]
    return {"R":R,"C_rotated":Cr,"covariance":float(np.linalg.norm(Cr-R.conj().T@C)),
            "projector":float(np.linalg.norm(Ur@Ur.conj().T-U@U.conj().T)),
            "norm":float(np.linalg.norm(Cr.conj().T@Cr-C.conj().T@C))}


def generated_adjoint_and_block(resolution: str)->dict[str,Any]:
    f=assemble_physical_vertex(resolution); V=f["diagnostic"]; A=V.conj().T.tocsr(); zq=csr_matrix((V.shape[1],V.shape[1]),dtype=np.complex128); zg=csr_matrix((V.shape[0],V.shape[0]),dtype=np.complex128); block=bmat([[zq,A],[V,zg]],format="csr")
    return {"emission":V,"absorption":A,"block":block,"adjoint_residual":float(np.linalg.norm((A-V.conj().T).toarray())),"hermiticity":float(np.linalg.norm((block-block.conj().T).toarray()))}


def static_dependency_guard()->dict[str,Any]:
    import ast
    tree=ast.parse(inspect.getsource(assemble_physical_vertex)); names={x.id for x in ast.walk(tree) if isinstance(x,ast.Name)}|{x.attr for x in ast.walk(tree) if isinstance(x,ast.Attribute)}; forbidden=("canonical_kernel","tuple_semantics_records","raw_tuple_semantics_summary","vertex1","evaluate_canonical_vertex")
    found=tuple(x for x in forbidden if x in names); return {"guard":"AST_C53_ASSEMBLY_GUARD","forbidden":forbidden,"found":found,"pass":not bool(found)}


@lru_cache(maxsize=1)
def poisoning_report()->dict[str,Any]:
    from ..basis1 import core as basis1
    before=assemble_physical_vertex("K9_2_N8_b0.40")["diagnostic_hash"]
    def poison(*_a,**_kw): raise AssertionError("C47_RAW_TUPLE_OR_C50_COMBINED_VALUE_READ")
    with patch.object(basis1,"canonical_kernel",poison), patch.object(c52.c50,"evaluate_canonical_vertex",poison):
        # Rebuild under poison rather than merely reading a previous cache entry.
        assemble_physical_vertex.cache_clear()
        after=assemble_physical_vertex("K9_2_N8_b0.40")["diagnostic_hash"]
    return {"before":before,"after":after,"pass":before==after,"raw_tuple_values":False,"C50_combined_values":False}


@lru_cache(maxsize=1)
def run_c53_checks()->dict[str,Any]:
    color=color_validation(); families=[assemble_physical_vertex(r.label) for r in c52.resolutions()]
    # K9 direct actions are enough to prove both independent routes at code level;
    # all resolutions are exercised by the artifact builder.
    f=families[0]; v=np.array([1+.2j,-.3+.4j, .2-.1j,.5+.3j,-.6+.2j,.1-.4j]); red=apply_physical_canonical_emission(v,"K9_2_N8_b0.40",route="reduced"); full=apply_physical_canonical_emission(v,"K9_2_N8_b0.40",route="full_product")
    sparse=f["diagnostic"].dot(v); block=generated_adjoint_and_block("K9_2_N8_b0.40")
    return {"status":STATUS,"color":color,"assembly_residual":max(x["assembly_residual"] for x in families),"matrixfree_reduced_full":float(np.linalg.norm(red-full)),"matrixfree_sparse":float(np.linalg.norm(red-sparse)),"adjoint":block["adjoint_residual"],"block_hermiticity":block["hermiticity"],"poison":poisoning_report(),"pass":color["E_casimir"]<2e-12 and color["commutator"]<2e-12 and color["anticommutator"]<2e-12 and color["f_contraction"]<2e-12 and color["d_contraction"]<2e-12 and color["adjoint_algebra"]<2e-12 and color["intertwining"]<2e-12 and color["projector_equivalence"]<2e-12 and color["leakage"]<2e-12 and color["C_left"]<2e-12 and color["C_right"]<2e-12 and color["C_covariance"]<2e-12 and color["W_unitary"]<2e-12 and max(x["assembly_residual"] for x in families)<2e-12 and np.linalg.norm(red-full)<2e-12 and np.linalg.norm(red-sparse)<2e-12 and block["adjoint_residual"]<2e-12 and block["hermiticity"]<2e-12 and poisoning_report()["pass"]}


def validate_c53(value: dict[str,Any])->bool:
    """Canonicalized equality avoids ndarray truth-value ambiguity in live faults."""
    return canonical_json(value)==canonical_json(run_c53_checks()) and value["pass"]
def mutate_live_c53(fault_id:int)->dict[str,Any]:
    value=json.loads(canonical_json(run_c53_checks())); mode=fault_id%16
    if mode==0:value["color"]["E_casimir"]=1.
    elif mode==1:value["color"]["commutator"]=1.
    elif mode==2:value["color"]["anticommutator"]=1.
    elif mode==3:value["color"]["f_contraction"]=1.
    elif mode==4:value["color"]["d_contraction"]=1.
    elif mode==5:value["color"]["adjoint_algebra"]=1.
    elif mode==6:value["color"]["intertwining"]=1.
    elif mode==7:value["color"]["projector_equivalence"]=1.
    elif mode==8:value["color"]["leakage"]=1.
    elif mode==9:value["color"]["C_left"]=1.
    elif mode==10:value["color"]["C_covariance"]=1.
    elif mode==11:value["assembly_residual"]=1.
    elif mode==12:value["matrixfree_reduced_full"]=1.
    elif mode==13:value["matrixfree_sparse"]=1.
    elif mode==14:value["poison"]["pass"]=False
    else:value["block_hermiticity"]=1.
    return value
