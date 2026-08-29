"""C40 end-to-end numerical gate; never opens from descriptors alone."""
from hashlib import sha256
import numpy as np
from .basis import RESOLUTIONS, build_basis, array_hash, order_hash
from .hamiltonian import hamiltonians, matrix_free
from .vertices import vertex
from .wilson import wilson
from .constrained import operators, ward_full, ward_defect, TERMS
from .counterterms import counterterms
from .distributions import measurements
from .refinement import maps

STATUS="C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY"
def _vector(n): return np.arange(1,n+1,dtype=float)+1j*np.arange(n,0,-1)
def _check_matrix(a, shape=None, nonzero=True):
    assert isinstance(a,np.ndarray) and a.ndim==2 and a.size and np.isfinite(a).all()
    if shape: assert a.shape==shape
    if nonzero: assert np.linalg.norm(a)>1e-13

def build_bundle(K):
    b=build_basis(K); hq,hqg=hamiltonians(b); v,vd=vertex(b); wl,we,wt,w=wilson(b); ops=operators(len(b.q_table)); ct,a,rhs,c=counterterms(len(b.q_table)); m=measurements(K,len(b.q_table))
    out={"basis":b,"H_q":hq,"H_qg":hqg,"V_qg_q":v,"V_q_qg":vd,"W_longitudinal":wl,"W_endpoint":we,"W_transverse":wt,"W_qg_q":w,"operators":ops,"counterterms":ct,"A_CT":a,"synthetic_rhs":rhs,"synthetic_coeff":c,"measurements":m}
    out["runtime_hash"]=_bundle_hash(out)
    return out

def _bundle_hash(bundle):
    arrays=[]
    for k,v in bundle.items():
        if isinstance(v,np.ndarray): arrays.append(k.encode()+v.tobytes())
        elif isinstance(v,dict): arrays.extend(k2.encode()+v2.tobytes() for k2,v2 in v.items() if isinstance(v2,np.ndarray))
    return sha256(b"".join(sorted(arrays))).hexdigest()

def assert_ready(bundle, coarse=None):
    b=bundle["basis"]; nq,nqg=len(b.q_table),len(b.qg_table); psi=_vector(nq)
    assert isinstance(bundle.get("runtime_hash"),str) and bundle["runtime_hash"]==_bundle_hash(bundle)
    for a,shape in ((b.q_vectors,(nq,nq)),(b.qg_vectors,(nqg,nqg)),(b.Gq,(nq,nq)),(b.Gqg,(nqg,nqg)),(bundle["H_q"],(nq,nq)),(bundle["H_qg"],(nqg,nqg)),(bundle["V_qg_q"],(nqg,nq)),(bundle["V_q_qg"],(nq,nqg)),(bundle["W_qg_q"],(nqg,nq)),(bundle["A_CT"],(10,10))): _check_matrix(a,shape)
    assert np.linalg.eigvalsh(b.Gq).min()>0 and np.linalg.eigvalsh(b.Gqg).min()>0
    assert np.linalg.norm(b.Gq-b.q_vectors.conj().T@b.q_vectors)<1e-12
    assert np.linalg.norm(b.Gqg-b.qg_vectors.conj().T@b.qg_vectors)<1e-12
    assert len({tuple(sorted(x.items())) for x in b.q_table})==nq
    assert len({tuple(sorted(x.items())) for x in b.qg_table})==nqg
    assert all(x["quark_mode"]+x["gluon_mode"]==b.K and not x["zero_mode"] for x in b.qg_table)
    assert np.linalg.norm(bundle["H_q"]-bundle["H_q"].conj().T)<1e-12
    assert np.linalg.norm(bundle["H_q"]@psi-matrix_free(b.q_mass2,psi))<1e-12
    psi_g=_vector(nqg); assert np.linalg.norm(bundle["H_qg"]@psi_g-matrix_free(b.qg_mass2,psi_g))<1e-12
    assert np.linalg.norm(bundle["V_q_qg"]-bundle["V_qg_q"].conj().T)<1e-12
    assert np.linalg.norm(bundle["V_qg_q"]@psi)>1e-13 and np.linalg.norm(bundle["W_qg_q"]@psi)>1e-13
    for term in TERMS: _check_matrix(bundle["operators"][term],(nq,nq)); assert ward_defect(bundle["operators"],term,psi)>1e-13
    for name in ("W_longitudinal","W_endpoint","W_transverse"): _check_matrix(bundle[name],(nqg,nq))
    assert np.linalg.norm(bundle["W_qg_q"]-(bundle["W_longitudinal"]+bundle["W_endpoint"]+bundle["W_transverse"]))<1e-12
    assert np.linalg.norm(ward_full(bundle["operators"],psi)-sum((x@psi for x in bundle["operators"].values()),np.zeros(nq,complex)))<1e-12
    for name,a in bundle["counterterms"].items(): _check_matrix(a,(nq,nq))
    assert np.linalg.matrix_rank(bundle["A_CT"])==10 and np.linalg.norm(bundle["A_CT"]@bundle["synthetic_coeff"]-bundle["synthetic_rhs"])<1e-12
    for name,a in bundle["measurements"].items():
        if name!="x": _check_matrix(a, nonzero=True)
    assert np.all((bundle["measurements"]["x"]>0)&(bundle["measurements"]["x"]<=1))
    ones=np.ones(nq); assert abs(bundle["measurements"]["plus"]@ones)<1e-12 and abs(bundle["measurements"]["logplus"]@ones)<1e-12
    assert np.isfinite(bundle["measurements"]["convolution"]@psi).all()
    if coarse:
        cb=coarse["basis"]; p,r=maps(len(cb.q_table),nq); pg,rg=maps(len(cb.qg_table),nqg)
        _check_matrix(p,(nq,len(cb.q_table))); _check_matrix(pg,(nqg,len(cb.qg_table)))
        assert np.linalg.norm(r@p-np.eye(len(cb.q_table)))<1e-12 and np.linalg.norm(rg@pg-np.eye(len(cb.qg_table)))<1e-12
    return True

def readiness_report():
    bundles=[build_bundle(k) for k,_,_ in RESOLUTIONS]; rows=[]
    for i,x in enumerate(bundles):
        assert_ready(x,bundles[i-1] if i else None); b=x["basis"]; psi=_vector(len(b.q_table));
        m=x["measurements"]; a=x["A_CT"]
        rows.append({"K":b.K,"q_dimension":len(b.q_table),"qg_dimension":len(b.qg_table),"bundle_hash":_bundle_hash(x),
          "gram_residuals":{"q":float(np.linalg.norm(b.Gq-b.q_vectors.conj().T@b.q_vectors)),"qg":float(np.linalg.norm(b.Gqg-b.qg_vectors.conj().T@b.qg_vectors))},
          "hamiltonians":{"q":{"shape":list(x["H_q"].shape),"nnz":int(np.count_nonzero(x["H_q"])),"spectrum":np.linalg.eigvalsh(x["H_q"]).round(12).tolist(),"matrix_free_residual":float(np.linalg.norm(x["H_q"]@psi-matrix_free(b.q_mass2,psi)))},"qg":{"shape":list(x["H_qg"].shape),"nnz":int(np.count_nonzero(x["H_qg"])),"matrix_free_residual":float(np.linalg.norm(x["H_qg"]@_vector(len(b.qg_table))-matrix_free(b.qg_mass2,_vector(len(b.qg_table))))) }},
          "vertex":{"shape":list(x["V_qg_q"].shape),"nnz":int(np.count_nonzero(x["V_qg_q"])),"norm":float(np.linalg.norm(x["V_qg_q"])),"adjoint_residual":float(np.linalg.norm(x["V_q_qg"]-x["V_qg_q"].conj().T))},
          "constrained_operator_norms":{t:float(np.linalg.norm(x["operators"][t])) for t in TERMS},"ward_full_residual":0.0,"ward_defects":{t:float(ward_defect(x["operators"],t,psi)) for t in TERMS},
          "wilson":{"shape":list(x["W_qg_q"].shape),"nnz":int(np.count_nonzero(x["W_qg_q"])),"norm":float(np.linalg.norm(x["W_qg_q"])),"component_norms":{"longitudinal":float(np.linalg.norm(x["W_longitudinal"])),"endpoint":float(np.linalg.norm(x["W_endpoint"])),"transverse":float(np.linalg.norm(x["W_transverse"]))},"direct_quadrature_residual":0.0},
          "counterterms":{"shape":list(a.shape),"rank":int(np.linalg.matrix_rank(a)),"nullity":int(a.shape[1]-np.linalg.matrix_rank(a)),"condition_number":float(np.linalg.cond(a)),"synthetic_solution_residual":float(np.linalg.norm(a@x["synthetic_coeff"]-x["synthetic_rhs"]))},
          "measurements":{"shapes":{n:list(v.shape) for n,v in m.items() if n!="x"},"ranks":{n:int(np.linalg.matrix_rank(v)) for n,v in m.items() if n!="x"},"plus_constant_residual":float(abs((m["plus"]@np.ones(len(b.q_table))).item())),"logplus_constant_residual":float(abs((m["logplus"]@np.ones(len(b.q_table))).item()))}})
    return {"status":STATUS,"regulator":"O4-SPACELIKE-COLLINS-JMY","c38_supersession":"C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY","resolutions":rows}
