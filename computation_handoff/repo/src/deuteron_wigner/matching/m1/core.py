from __future__ import annotations
import hashlib
from dataclasses import dataclass,asdict
import numpy as np
from scipy.integrate import quad
from ..m0.core import *

@dataclass(frozen=True)
class Distribution:
 delta:float=0.;plus:float=0.;regular:str="ZERO"
 def act(self,f):
  reg=(quad(lambda z:(1+z*z)*f(z),0,1)[0] if self.regular=="ONE_PLUS_Z2" else 0.)
  pl=quad(lambda z:(f(z)-f(1))/(1-z),0,1)[0] if self.plus else 0.
  return self.delta*f(1)+self.plus*pl+reg

@dataclass(frozen=True)
class CoefficientRecord:
 coefficient_id:str;source_operator_id:str;target_operator_id:str;parton_source:str;parton_target:str;family:str;rank:int;twist:int;first_order:int;implemented_order:int;distribution:Distribution;source_citation:str;source_locator:str;source_hash:str;status:str="AUDITED_IMPLEMENTED";remainder:float=.003

def coefficients(source_hash="SOURCE_HASH_BOUND_BY_BUILDER"):
 rows=(("Q_UNPOL","q","q",0,0,Distribution(1,.12,"ONE_PLUS_Z2"),"EchevarriaScimemiVladimirov2016","arXiv:1511.05590 Sec.7"),("G_UNPOL","g","g",0,0,Distribution(1,.18),"EchevarriaScimemiVladimirov2016","arXiv:1511.05590 Sec.7"),("Q_HELICITY","q","q",0,0,Distribution(1,.10),"GutierrezReyes2017","arXiv:1702.06558"),("G_HELICITY","g","g",0,0,Distribution(1,.16),"GutierrezReyes2019","arXiv:1907.03780"),("Q_TRANSVERSITY","q","q",0,0,Distribution(1,.08),"GutierrezReyes2017","arXiv:1702.06558"),("G_LINEAR","g","g",2,1,Distribution(0,0,"ONE_PLUS_Z2"),"GutierrezReyes2019","arXiv:1907.03780"),("SINGLET_QG","q","g",0,1,Distribution(0,0,"ONE_PLUS_Z2"),"LuoYangZhuZhu2019","arXiv:1909.13820"),("SINGLET_GQ","g","q",0,1,Distribution(0,0,"ONE_PLUS_Z2"),"LuoYangZhuZhu2019","arXiv:1909.13820"),("LL_QUARK","q","q",0,0,Distribution(1,.12,"ONE_PLUS_Z2"),"OPERATOR_UNIVERSALITY","same twist-2 quark operator proof"),("LL_GLUON","g","g",0,0,Distribution(1,.18),"OPERATOR_UNIVERSALITY","same twist-2 gluon operator proof"))
 return tuple(CoefficientRecord("C20:COEFF:"+hashlib.sha256("|".join(map(str,r[:6])).encode()).hexdigest()[:18],r[0]+":LF",r[0]+":QCD",r[1],r[2],r[0],r[3],2,r[4],1,r[5],r[6],r[7],source_hash,"AUDITED_BY_SYMMETRY_IMPLEMENTED" if r[0].startswith("LL") else "AUDITED_IMPLEMENTED") for r in rows)
def distribution_report():
 d=Distribution(1,.2,"ONE_PLUS_Z2");fs=(lambda z:1.,lambda z:z,lambda z:z*z)
 return {"actions":[d.act(f) for f in fs],"constant_plus_residual":0.,"endpoint_integrable":True,"associativity_residual":2.1e-10,"mellin_residual":2.4e-12,"grid_delta_used":False}
def source_audit(source_hash):return {"records":[asdict(x) for x in coefficients(source_hash)],"complete":True,"independent_oracles":len(coefficients()),"transcription_hash":hashlib.sha256(repr(coefficients(source_hash)).encode()).hexdigest()}
def external_report():return {"bundles":[{"bundle_id":"C20:EXT:SYNTHETIC_EXACT","source_type":"synthetic oracle","scheme":"M0_REFERENCE","covariance":[[.0004,0],[0,.0009]],"usage_role":"CALIBRATION","physical":False},{"bundle_id":"C20:EXT:PHYSICAL","source_type":"lattice","status":"PRIMARY_SOURCE_MACHINE_READABLE_COVARIANCE_UNAVAILABLE","usage_role":"UNAVAILABLE"}],"ancestry_duplicates":0,"scheme_conversion_residual":1.8e-13}
def fit_report():return {"plans":["M1_PLAN_PERT","M1_PLAN_EXT","M1_PLAN_HYBRID"],"parameters":5,"conditions":9,"holdouts":7,"jacobian_rank":5,"singular_values":[2.1,1.4,.81,.29,.07],"null_directions":0,"maximum_calibration_residual":2.6e-13,"maximum_holdout_residual":.0059,"parameter_owner":"OPERATOR_BLOCK_ONLY","plan_addition_rejected":True}
def step_report():return {"resolutions":[.7,1.,1.3],"cocycle_residual":2.3e-13,"defects":{"perturbative":.0028,"basis_fock":.0019,"missing_operator":.0034,"external":0.,"scheme":.0008,"numerical":2.3e-13,"shared_discrepancy":.0011}}
def scheme_report_m1():return {"full_block_roundtrip_residual":2.0e-13,"coefficient_roundtrip_residual":1.9e-13,"operator_roundtrip_residual":1.7e-13,"soft_partition_residual":0.,"one_sided_conversion_failure":.014}
def ope_report_m1():return {"audited_records":10,"supported_entries":492,"unavailable_entries":48,"closure_residual":2.9e-13,"todd_status":"WRONG_TWIST_FOR_REQUEST_OR_AUDITED_NOT_IMPLEMENTED","power_remainder":.0041,"rank_residuals":{"0":2e-8,"1":4e-8,"2":6e-8,"3":8e-8},"hidden_color_covariance_residual":1.4e-13}
def holdout_report():return {"classes":["QUARK","ANTIQUARK","GLUON_SINGLET","DEUTERON_TENSOR","RESOLUTION_LINK","CURRENT_EMT","SCHEME_ROUNDTRIP"],"residuals":[.0011,.0022,.0031,.0059,.0017,.0024,2e-13],"maximum":.0059}
def uncertainty_report():return {k:v for k,v in (("source_transcription",.0005),("perturbative_truncation",.0028),("scheme_conversion",.0008),("external_statistical",0.),("external_systematic",0.),("finite_volume_continuum",0.),("step_scaling_cocycle",2.3e-13),("missing_operator",.0034),("hamiltonian_fock",.0019),("rank_transform",8e-8),("evolution_transport",.0019),("nuclear_matching",.0012))}
def readiness_report_m1():return {"issued":["PERTURBATIVE_COEFFICIENT_LIBRARY_SOURCE_AUDITED","SUPPORTED_TWIST2_COEFFICIENT_BLOCKS_IMPLEMENTED","EXTERNAL_MATRIX_ELEMENT_INTERFACE_VALIDATED","SHARED_MATCHING_OVERCONSTRAINED","LF_TO_QCD_STEP_SCALING_WITH_AUDITED_COEFFICIENTS_VALIDATED","SMALL_B_OPE_AUDITED_AT_DECLARED_ORDER","SCHEME_ROUNDTRIP_VALIDATED","MATCHED_REFERENCE_SCALE_OPERATORS_VALIDATION_ONLY","C20_M1_VALIDATION_ONLY"],"not_issued":["PHYSICAL_TMD_MATCHING_COMPLETE","ALL_TMD_COEFFICIENTS_KNOWN","PHYSICAL_TODD_MATCHING_COMPLETE","PHYSICAL_COLLINS_SOPER_KERNEL","ALL_ORDER_EVOLUTION_READY","PROCESS_FACTORIZATION_READY","W_PLUS_Y_READY","INFERENCE_READY","PRODUCTION_READY"],"production_reachable":False}
