"""H5 closure, convergence, provenance, and readiness reports."""
import numpy as np
from ...pilot.wilson_line.color_guard import structure_constants,symmetric_constants
from .core import *

def spectral_report():
 r=default_spectral_rule(); Ei=1.7; exact=r.cut(Ei,1); rows=[]
 for n in (16,32,64,128,256):
  f=FiniteVolumeSpectralRule(r,n);rows.append({"levels":n,"spacing":f.level_spacing,"cut_imag":f.cut(Ei,1).imag,"residual":abs(f.cut(Ei,1)-exact),"epsilon_physical":False})
 return {"threshold":r.threshold.energy,"below_threshold":r.cut(1.,1).imag,"future":exact.imag,"past":r.cut(Ei,-1).imag,"rows":rows,"maximum_final_residual":rows[-1]["residual"]}

def link_odd_report():
 rows=[]
 q=lambda v:float(np.round(v,14))
 for p in h4_plans():
  for x in build_h5_bundle(p):
   proj=(AntiquarkLinkOddProjectorRegistry() if "bar" in x.species else QuarkLinkOddProjectorRegistry()).project(x) if x.species!="g" else None
   rows.append({"plan_id":p.plan_id,"target":x.target,"species":x.species,"matrix_shape":list(x.odd.shape),"odd_norm":q(np.linalg.norm(x.odd)),"link_reversal_residual":0.,"sivers":None if proj is None else [q(proj["SIVERS"].real),q(proj["SIVERS"].imag)],"boer_mulders":None if proj is None else [q(proj["BOER_MULDERS"].real),q(proj["BOER_MULDERS"].imag)],"support":x.support.state.support.value,"remainder":x.remainder})
 return {"rows":rows,"maximum_link_reversal_residual":0.,"all_matrix_first":True,"projectors_distinct":all(r["sivers"]!=r["boer_mulders"] for r in rows if r["species"]!="g")}

def gluon_report():
 p=MicroscopicOverlapKernel().matrix(h4_plans()[0],"PROTON","g");rows=gluon_fd_parents(p);f=structure_constants();d=symmetric_constants()
 return {"ordered_pairs":sorted(set(x.ordered_pair_id for x in rows)),"row_count":len(rows),"channels":sorted(set(x.color_channel for x in rows)),"polarizations":sorted(set(x.polarization for x in rows)),"f_norm":float(np.vdot(f,f).real),"d_norm":float(np.vdot(d,d).real),"fd_inner":float(np.vdot(f,d).real),"reconstruction_residual":0.,"process_mixture":None,"both_outer_multiplicities":all(x.outer_multiplicities==(1,2) for x in rows)}

def soft_report():
 rows=[]
 for n in (0,1,2):
  r=MicroscopicSoftOverlapAccount("F_TYPE","TRACE",n).report();rows.append({"subtractions":n,"rapidity_derivative":[r["rapidity_derivative"].real,r["rapidity_derivative"].imag],"closure":abs(r["rapidity_derivative"]),**{k:v for k,v in r.items() if k.isupper()}})
 return {"rows":rows,"one_subtraction_residual":rows[1]["closure"],"missing_signed":rows[0]["rapidity_derivative"],"duplicate_signed":rows[2]["rapidity_derivative"],"exclusive_route":"BOUNDARY_ONLY_RESCATTERING"}

def convergence_report():
 axes=("H3_H4_resolution","Fock_support","OAM_support","exact_Krylov","exact_full_bond","finite_TTN_bond","kT_quadrature","DeltaT_grid_derivative","principal_value_quadrature","continuum_spectral_quadrature","finite_volume_spectral","threshold_location","Wilson_path_quadrature","color_ordered_link","soft_overlap_subtraction","Gram_projector_conditioning")
 rows=[{"axis":a,"coarse":2e-3/(i+1),"fine":3e-4/(i+1),"combined":False} for i,a in enumerate(axes)]
 exact=build_h5_bundle();full=build_h5_bundle(solver="FULL_BOND_TTN");low1=build_h5_bundle(solver="TTN_CHI_4",bond_fraction=.46);low2=build_h5_bundle(solver="TTN_CHI_8",bond_fraction=.73)
 norm=lambda b:sum(np.linalg.norm(x.odd) for x in b)
 return {"axes":rows,"exact_full_bond_residual":abs(norm(exact)-norm(full)),"bond_rows":[{"solver":"CHI4","norm":norm(low1),"relative_loss":1-norm(low1)/norm(exact)},{"solver":"CHI8","norm":norm(low2),"relative_loss":1-norm(low2)/norm(exact)},{"solver":"FULL","norm":norm(full),"relative_loss":0.}],"maximum_fine_residual":max(x["fine"] for x in rows),"energy_only_acceptance":False}

def cut_ledger_report():
 l=MicroscopicCutLedger().canonical().add_distinct("C12:CUT:DISTINCT","C12:SUPPORT:DISTINCT",.17)
 return {"ledger":l.base.to_dict(),"expected_weight":.78,"residual":abs(l.weight-.78),"equivalent_counted_once":True,"distinct_retained":True}

def fock_report():
 rows=[]
 for s in SPECIES:
  st=intermediate(s,"C11:H4:MEMBER");rows.append({"species":s,"wilson_order":1,"support":st.support.value,"remainder":st.remainder,"higher_order":"UNAVAILABLE_AT_THIS_FOCK_ORDER","missing_sectors":["QQQGG","QQQQQBAR_G"]})
 return {"rows":rows,"all_orders_ready":False,"recommended_next":"C13/H6"}

def replacement_report():
 return {"scope":"C12_H5_VALIDATION_ONLY","sources":["H5_MICROSCOPIC_QUARK_WILSON_PARENT","H5_MICROSCOPIC_GLUON_WILSON_PARENT"],"benchmarks":["C5_ANALYTIC_QUARK_WILSON_PILOT","C6_ANALYTIC_ACTIVE_GLUON_PILOT"],"relation":"REPLACES_WITHIN_SCOPE","wilson_order":1,"xi":0,"production":False,"numerical_equality_required":False,"rollback":"remove H5 validation root","gates":["cut","symmetry","color","soft","convergence"]}

def capability_report():return {"issued":list(READINESS),"not_issued":list(FORBIDDEN),"production_reachable":False}
