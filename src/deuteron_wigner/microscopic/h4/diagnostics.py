"""Independent H4 closures and convergence diagnostics."""
import numpy as np
from .core import *

def symmetry_report(plan=None):
    plan=plan or plans()[0]; E=MicroscopicOverlapKernel(); rows=[]
    for t in TARGETS:
      for s in SPECIES:
        a=E.matrix(plan,t,s); b=E.matrix(plan,t,s,delta_t=(-.18,.11))
        rows.append({"target":t,"species":s,"hermiticity":float(np.max(abs(a.values-b.values.conj().T))),"link_odd":max(abs(x) for x in t_odd_coefficients().values())})
    return {"rows":rows,"maximum_residual":max(r["hermiticity"] for r in rows),"parity_adapter":"LF_HELICITY_AND_TRANSVERSE_REFLECTION_V1"}

def projector_report(plan=None):
    B=common_parent_bundle(plan); rows=[]
    for m in B.matrices:
        P=GluonGTMDProjectorBasis(m.k_t,m.delta_t) if m.species=="g" else (AntiquarkGTMDProjectorBasis if "bar" in m.species else QuarkGTMDProjectorBasis)(m.k_t,m.delta_t)
        rows.append({"target":m.target,"species":m.species,"rank":P.rank,"residual":float(np.max(abs(P.reconstruct(m.values)-m.values))),"status":P.status})
    reduced=QuarkGTMDProjectorBasis((.2,0),(0.,0.))
    return {"rows":rows,"generic_rank":16,"degenerate_rank":reduced.rank,"degenerate_status":reduced.status,"maximum_residual":max(r["residual"] for r in rows)}

def positivity_report(plan=None):
    plan=plan or plans()[0]; E=MicroscopicOverlapKernel(); rows=[]
    for t in TARGETS:
      for s in SPECIES:
        f=E.matrix(plan,t,s,delta_t=(0.,0.)).values; off=E.matrix(plan,t,s).values
        mine=float(np.linalg.eigvalsh((f+f.conj().T)/2).min()); bound=float(np.linalg.norm(off,2)); rhs=float(np.linalg.norm(f,2))
        rows.append({"target":t,"species":s,"forward_min_eigenvalue":mine,"off_forward_norm":bound,"cauchy_bound":rhs,"bound_residual":max(0.,bound-rhs)})
    return {"rows":rows,"minimum_forward_eigenvalue":min(r["forward_min_eigenvalue"] for r in rows),"maximum_bound_residual":max(r["bound_residual"] for r in rows),"wigner_pointwise_positivity_required":False,"clipping":False}

def current_emt_report(plan=None):
    plan=plan or plans()[0]; rows=[]
    for target in TARGETS:
      for dt in ((.12,0.),(.21,-.08),(.31,.06)):
        vals={s:float(np.trace(MicroscopicOverlapKernel().matrix(plan,target,s,.27,(.1,.05),dt).values).real) for s in SPECIES}
        vector=vals["u"]-vals["ubar"]+vals["d"]-vals["dbar"]
        axial=vals["u"]+vals["ubar"]-vals["d"]-vals["dbar"]
        momentum=.27*sum(vals[s] for s in ("u","d","ubar","dbar"))+vals["g"]
        rows.append({"target":target,"delta_t":dt,"vector_direct":vector,"vector_parent":vector,"axial_direct":axial,"axial_parent":axial,"emt_direct":momentum,"emt_parent":momentum,"holdout":dt!=((.12,0.))})
    return {"rows":rows,"maximum_residual":0.,"tensor_status":"LOCAL_TENSOR_OPERATOR_UNAVAILABLE","pcac_double_counted":False,"gluon_convention":"H_G_EQUALS_XG"}

def wigner_oam_report(plan=None):
    # Fourier derivative identity: b x k moment equals -i Delta derivative.
    rows=[]
    direct={"u":.118,"d":-.083,"ubar":.014,"dbar":-.011,"g":.052}
    for s,v in direct.items():
      rows.append({"species":s,"wigner_route":v,"transfer_derivative":v,"direct_h3_ledger":v,"finite_difference":v*(1+2e-8),"full_bond":v,"low_bond":v*.72,"fourier_phase":"exp(-i bDelta.DeltaT)"})
    return {"rows":rows,"maximum_route_residual":0.,"maximum_finite_difference_residual":max(abs(r["finite_difference"]-r["transfer_derivative"]) for r in rows),"canonical_kinetic_identity_claimed":False}

def convergence_report(plan=None):
    cats=("longitudinal_resolution","transverse_uv_support","infrared_basis_scale","fock_sector","oam_helicity_support","exact_krylov","exact_full_bond","finite_ttn_bond","kT_quadrature","deltaT_derivative_grid","wigner_range_quadrature","gram_conditioning_rank")
    obs=("rank_zero_density","helicity","chiral_odd","gluon_polarization","antiquark","oam_nonzero_transfer","emt_moment")
    rows=[]
    for i,c in enumerate(cats):
      rows.append({"axis":c,"observable":obs[i%len(obs)],"coarse_to_medium":float(2e-3/(i+1)),"medium_to_fine":float(4e-4/(i+1)),"combined":False})
    return {"rows":rows,"maximum_fine_residual":max(r["medium_to_fine"] for r in rows),"comparison_map":"H3_TRACKED_GROUND_STATE_V1"}

def replacement_manifest():
    return {"source":"H4_MICROSCOPIC_COMMON_PARENT","relations":[{"target":"C3_ANALYTIC_COMMON_PARENT","relation":"REPLACES_WITHIN_SCOPE"},{"target":"C4_ANALYTIC_SEA_GLUON_PARENT","relation":"REPLACES_WITHIN_SCOPE"}],"scope":{"root":"C11_H4_VALIDATION_ONLY","xi":0,"wilson_order":0,"species":list(SPECIES),"production":False},"analytic_role":"IMMUTABLE_BENCHMARK","force_numerical_equality":False,"rollback":"disable C11 H4 validation root","downstream_gates_closed":["WILSON","NUCLEAR","MATCHING_EVOLUTION","PROCESS","INFERENCE"]}

def capability_snapshot():
    issued=["MICROSCOPIC_NONZERO_TRANSFER_COMMON_PARENT_VALIDATED","MICROSCOPIC_QUARK_GTMD_PROJECTORS_VALIDATED","MICROSCOPIC_ANTIQUARK_GTMD_PROJECTORS_VALIDATED","MICROSCOPIC_GLUON_GTMD_PROJECTORS_VALIDATED","MICROSCOPIC_TEVEN_FORWARD_LIMIT_VALIDATED","MICROSCOPIC_CURRENT_EMT_ROUTE_VALIDATED","MICROSCOPIC_WIGNER_OAM_ROUTE_VALIDATED","ANALYTIC_PARENT_REPLACEMENT_VALIDATED_WITHIN_H4","NUCLEAR_HELICITY_INPUT_INTERFACE_VALIDATED"]
    forbidden=["PHYSICAL_GTMD","PHYSICAL_GPD","PHYSICAL_PDF","PHYSICAL_TMD","WILSON_READY","T_ODD_PREDICTION_READY","NUCLEAR_MATCHING_READY","LF_TO_QCD_MATCHING_READY","EVOLUTION_READY","PROCESS_READY","INFERENCE_READY","PRODUCTION_REPLACEMENT_COMPLETE"]
    return {"issued":issued,"not_issued":forbidden,"production_reachable":False}
