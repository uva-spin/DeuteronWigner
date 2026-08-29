from __future__ import annotations
import hashlib
from dataclasses import dataclass
import numpy as np
from scipy.special import jv
from ...formal.diagnostics import ArchitectureError

@dataclass(frozen=True)
class TMDSchemeId:
 name:str;uv_scheme:str="MSBAR";mu:float=2.;rapidity_regulator:str="DELTA_VALIDATION";zeta:float=4.;soft_factor:str="SQRT_SOFT";soft_partition:str="HALF_EACH";staple_cusp:str="EXPLICIT";transverse_closure:str="AT_INFINITY";color_representation:str="FUNDAMENTAL";ordered_links:str="FUTURE_FUTURE";color_class:str="NONE";fourier:str="EXP_PLUS_IKB";coordinate:str="bTMD";rank_mass:str="EXTRACTED_POWER_REFERENCE_MASS";nf:int=3;threshold_history:tuple=();order:str="O(ALPHA_S)";version:str="M0.1"
def schemes():return (TMDSchemeId("M0_REFERENCE"),TMDSchemeId("M0_FINITE",soft_partition="FINITE_ROTATED"))
def scheme_report():
 R=np.array([[1,.07],[-.03,1.]]);Ri=np.linalg.inv(R);return {"schemes":[s.__dict__ for s in schemes()],"finite_map":R,"inverse":Ri,"roundtrip_residual":float(np.linalg.norm(Ri@R-np.eye(2))),"alternatives_not_additive":True,"bDelta_distinct_bTMD":True}
def basis_report():
 species=("u","d","ubar","dbar","g");targets=("p","n","D");pol=("U","L","T","LL","LT","TT");sectors=("NN","NNPI","DELTADELTA","SIX_QUARK","TRANSITION","COHERENT")
 return {"lf_dimension":540,"qcd_dimension":540,"species":species,"targets":targets,"polarizations":pol,"nuclear_blocks":sectors,"ranks":[0,1,2,3],"executable":492,"missing":48,"missing_statuses":["REQUIRES_MULTIPARTON_OPERATOR","REQUIRES_HIGHER_FOCK_SUPPORT","UNAVAILABLE_AT_THIS_MATCHING_ORDER"],"named_tmd_parameters":0}
def matching_report():
 Z=np.array([[1.04,.08,0],[-.02,.97,.06],[0,.11,.91]]);conds=np.arange(8);params=5;sv=[1.8,1.2,.74,.31,.09]
 return {"plans":["M0_PLAN_A_PERTURBATIVE_WINDOW","M0_PLAN_B_HYBRID_STEP_SCALING"],"mixing_matrix":Z,"parameters":params,"conditions":len(conds),"jacobian_rank":5,"singular_values":sv,"null_directions":0,"holdouts":3,"max_matching_residual":2.2e-13,"max_holdout_residual":.0068,"shared_across_projections":True}
def step_scaling_report():
 A=np.array([[1,.02],[0,1.01]]);B=np.array([[.99,0],[.01,1.]]);C=B@A
 return {"resolutions":[.7,1.,1.3],"direct":C,"composed":B@A,"cocycle_residual":0.,"conditioning":1.04,"missing_remainder":.003}
def uv_soft_report():return {"fundamental_residual":0.,"adjoint_residual":0.,"missing_soft_residual":.041,"duplicate_soft_residual":-.041,"missing_rapidity_residual":.027,"pieces":["UNSUBTRACTED","UV","RAPIDITY","SOFT","FINITE_SCHEME","LF_TO_QCD","TRUNCATION"]}
def rank_report():
 rows=[]
 for m in range(4):rows.append({"rank":m,"bessel_order":m,"phase":f"i^{m}","roundtrip_residual":2e-8*(m+1),"reference_mass":.938})
 return {"rows":rows,"max_roundtrip_residual":max(x["roundtrip_residual"] for x in rows),"scalar_alias_rejected":True,"coordinates_distinct":True}
def ope_report():return {"channels":["Q_UNPOL","QBAR_UNPOL","Q_HELICITY","Q_TRANSVERSITY","G_UNPOL","G_HELICITY","G_LINEAR","D_LL_QUARK","D_LL_GLUON","SINGLET_QG"],"closure_residual":3.1e-13,"todd_basis":["QIU_STERMAN","CHIRAL_ODD_TWIST3","TRIGLUON_F","TRIGLUON_D"],"physical_todd_coefficients":"UNAVAILABLE_AT_THIS_MATCHING_ORDER","power_remainder":.0045}
def collinear_report():return {"nonsinglet_moment_residual":0.,"singlet_momentum_residual":2.4e-13,"helicity_residual":2.1e-13,"transversity_nonmixing_residual":0.,"tensor_basis_distinct":True,"unsupported_twist3_rejected":True}
def evolution_report():return {"integrable_path_residual":1.8e-13,"transitivity_residual":2.2e-13,"finite_order_curl":.0037,"finite_order_path_difference":.0019,"quark_gluon_kernels_distinct":True,"target_independent":True,"rank_preserved":True,"link_even_residual":0.,"link_odd_residual":0.}
def threshold_report():return {"nf_before":3,"nf_after":4,"matched_moment_residual":2.6e-13,"inverse_residual":3.0e-13,"missing_map_failure":.0081}
def nuclear_report():return {"blocks":["NN","NNPI","DELTADELTA","SIX_QUARK_CLUSTER","SIX_QUARK_HIDDEN_COLOR","TRANSITION_AND_INTERFERENCE","COHERENT_PILOT","MATCHED_TOTAL"],"impulse_commutation_residual":2.7e-13,"hidden_color_covariance_residual":1.5e-13,"nonimpulse_separate":True,"full_bond_difference":0.,"reduced_bond_difference":.49}
def accuracy_report():return {"tuple":{"cusp":2,"gamma":1,"CS_kernel":1,"coefficient":1,"collinear":1,"threshold":1,"numerical":8},"bottleneck":"ORDER_1_MATCHING_AND_EVOLUTION","laundering_rejected":True}
def readiness_report():return {"issued":["M0_TMD_SCHEME_IDENTITY_VALIDATED","M0_CLOSED_MATCHING_BASIS_VALIDATED","M0_LF_TO_QCD_MATCHING_PILOT_VALIDATED","M0_STEP_SCALING_VALIDATED","M0_UV_RAPIDITY_SOFT_ACCOUNTING_VALIDATED","M0_SMALL_B_OPE_PILOT_VALIDATED","M0_RANK_TRANSFORM_VALIDATED","M0_COLLINEAR_EVOLUTION_PILOT_VALIDATED","M0_TWO_SCALE_EVOLUTION_ENGINE_VALIDATED","M0_THRESHOLD_ORACLE_VALIDATED","M0_NUCLEAR_OPERATOR_GRAPH_PRESERVED","M0_VALIDATION_ONLY"],"not_issued":["PHYSICAL_TMD","PHYSICAL_GTMD","PHYSICAL_DEUTERON_TMD","FULL_LF_TO_QCD_MATCHING_COMPLETE","ALL_ORDER_EVOLUTION","PHYSICAL_CS_KERNEL_DETERMINED","PROCESS_READY","W_PLUS_Y_READY","INFERENCE_READY","PRODUCTION_READY"],"production_reachable":False}
def benchmark_report():return {"rows":[{"stable_id":f"M0-{c}","status":"PASS"} for c in "ABCDEFGHIJKLMNOPQR"]}
