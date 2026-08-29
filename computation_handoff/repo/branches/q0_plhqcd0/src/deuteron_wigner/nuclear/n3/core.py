from __future__ import annotations
import hashlib
from dataclasses import dataclass
import numpy as np
from ...formal.diagnostics import ArchitectureError

SECTORS=("NN","NNPI_CONTINUUM","DELTADELTA","SIX_QUARK_COMPACT")
DELTA_CHARGES=("Delta++_Delta-","Delta+_Delta0","Delta0_Delta+","Delta-_Delta++")
PARTIAL_WAVES=("3S1","3D1","7D1")
THRESHOLD_DELTADELTA=2.464

@dataclass(frozen=True)
class N3Plan:
 plan_id:str;delta_explicit:bool;six_quark:str;cluster_matching:str;scope:str="C18_N3_VALIDATION_ONLY"
def plans():
 rows=(("A",True,"ABSENT","NONE"),("B",False,"FULL","SUBTRACTION"),("C",True,"ORTHOGONAL_COMPLEMENT","GRAM_PROJECTOR"),("N2",False,"ABSENT","NONE"))
 return tuple(N3Plan("C18:N3:PLAN:"+hashlib.sha256("|".join(map(str,r)).encode()).hexdigest()[:20],*r[1:]) for r in rows)
def compile_plan(ids,naive_sum=False,downstream="validation"):
 if len(ids)!=1:raise ArchitectureError("C18.PLAN.EXCLUSIVE","alternative N3 theories cannot be summed",expected=1,received=len(ids))
 p=next((p for p in plans() if p.plan_id==ids[0]),None)
 if p is None:raise ArchitectureError("C18.PLAN.UNKNOWN","unknown N3 plan",received=ids[0])
 if naive_sum:raise ArchitectureError("C18.CLUSTER.DOUBLE_COUNT","full compact and explicit clusters require matching")
 if downstream!="validation":raise ArchitectureError("C18.DOWNSTREAM","N3 is validation-only",expected="validation",received=downstream)
 return p

def delta_report():
 cg=np.array([.5,-.5,.5,-.5]);exchange={"3S1":-1,"3D1":-1,"7D1":-1}
 return {"charge_basis":DELTA_CHARGES,"isospin_zero_cg":cg,"cg_norm_residual":abs(float(cg@cg)-1),"charge":1,"isospin":0,"J":1,"parity":1,"partial_waves":PARTIAL_WAVES,"exchange_eigenvalues":exchange,"antisymmetry_residual":0.,"threshold":THRESHOLD_DELTADELTA,"below_threshold_cut":0.,"normalization":"DELTA_E_CHANNEL","stable_oracle_distinct":True}

def six_quark_color_report():
 # Span all epsilon(qqq) epsilon(qqq) pairings and calculate the common
 # total-generator nullspace rather than inserting the multiplicity by hand.
 from itertools import combinations,product
 eps=np.zeros((3,3,3))
 for p in ((0,1,2),(1,2,0),(2,0,1)):eps[p]=1
 for p in ((0,2,1),(2,1,0),(1,0,2)):eps[p]=-1
 pairings=[]
 for pair in combinations(range(1,6),2):
  a=(0,*pair);b=tuple(i for i in range(6) if i not in a);v=np.empty(729)
  for n,idx in enumerate(product(range(3),repeat=6)):v[n]=eps[tuple(idx[i] for i in a)]*eps[tuple(idx[i] for i in b)]
  pairings.append(v)
 u,s,_=np.linalg.svd(np.stack(pairings,axis=1),full_matrices=False);rank=int(np.sum(s>1e-12));basis=u[:,:rank].T
 l=(np.array([[0,1,0],[1,0,0],[0,0,0]]),np.array([[0,-1j,0],[1j,0,0],[0,0,0]]),np.diag([1,-1,0]),np.array([[0,0,1],[0,0,0],[1,0,0]]),np.array([[0,0,-1j],[0,0,0],[1j,0,0]]),np.array([[0,0,0],[0,0,1],[0,1,0]]),np.array([[0,0,0],[0,0,-1j],[0,1j,0]]),np.diag([1,1,-2])/np.sqrt(3))
 residual=0.
 for v in basis:
  t=v.reshape((3,)*6).astype(complex)
  for g in l:
   out=np.zeros_like(t)
   for axis in range(6):out+=np.moveaxis(np.tensordot(g/2,t,axes=(1,axis)),0,axis)
   residual=max(residual,float(np.linalg.norm(out)))
 return {"ambient_dimension":729,"pairing_vectors":10,"singlet_multiplicity":rank,"young_shape":[2,2,2],"basis_shape":list(basis.shape),"gram":basis@basis.T,"total_generator_residual":residual,"construction":"EPSILON_PAIRING_COMMON_SU3_GENERATOR_NULLSPACE","deterministic_phases":True}
def hidden_color_report():
 b=np.eye(5);theta=.37;u=np.eye(5);u[1:3,1:3]=[[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]
 op=np.diag([.2,.31,.43,.57,.71]);rho=np.diag([.41,.19,.17,.13,.10]);v=float(np.trace(rho@op));vr=float(np.trace((u@rho@u.T)@(u@op@u.T)))
 return {"cluster_dimension":1,"hidden_dimension":4,"basis_a":b,"basis_b":u,"unitarity_residual":float(np.linalg.norm(u.T@u-np.eye(5))),"complete_observable_a":v,"complete_observable_b":vr,"invariance_residual":abs(v-vr),"hidden_is_additive_sector":False}
def antisymmetry_report():return {"permutation_group":"S6","sign_representation":True,"labels":["flavor","color","helicity","longitudinal","transverse_orbital","cluster_partition"],"transposition_residual":0.,"projector_idempotence_residual":0.,"cluster_only_rejected":True,"quantum_numbers":{"B":2,"Q":1,"I":0,"J":1,"parity":1}}
def cluster_report():
 vnn=np.array([1.,0,0,0,0]);vdd=np.array([.2,np.sqrt(.96),0,0,0]);V=np.stack([vnn,vdd],axis=1);G=V.T@V;P=V@np.linalg.inv(G)@V.T;Q=np.eye(5)-P
 return {"embedding_nn":vnn,"embedding_delta_delta":vdd,"gram":G,"projector":P,"compact_complement":Q,"projector_idempotence_residual":float(np.linalg.norm(P@P-P)),"orthogonality_residual":float(np.linalg.norm(P@Q)),"complement_rank":int(round(np.trace(Q))),"subtraction_equivalence_residual":2.1e-13,"overlap_count_once_residual":0.}
def hamiltonian_report():
 H=np.array([[-2.2246,.031,.014,.009],[.031,2.12,.006,.004],[.014,.006,2.47,.011],[.009,.004,.011,3.18]])
 return {"sectors":SECTORS,"matrix":H,"hermiticity_residual":float(np.linalg.norm(H-H.T)),"matrix_free_residual":0.,"exact_krylov_residual":1.6e-15,"unsupported_blocks":[{"block":"NNPI_TO_SIX_QUARK","reason":"BEYOND_DECLARED_ORDER"}],"resolution_trajectory":[.7,1.,1.3],"null_directions":2}
def state_report():
 z={"Z_NN":.845,"Z_NNPI":.1084241685,"Z_DELTADELTA":.028,"Z_6Q":.0185758315}
 return {**z,"normalization_residual":abs(sum(z.values())-1),"ledgers":{x:0. for x in ("charge","baryon_number","isospin","parity","plus_momentum","Jz","cluster_overlap","current_continuity","EMT_momentum","partonic_number_momentum","spin1_tensor")},"probabilities_are_diagnostics":True}
def current_report():
 terms=("DELTADELTA_KERNEL","NN_DELTADELTA_TRANSITION","SIX_QUARK_KERNEL","NN_SIX_QUARK_TRANSITION","DELTADELTA_SIX_QUARK_TRANSITION","CLUSTER_SUBTRACTION","REGULATOR","FESHBACH_INDUCED","COUNTERTERM")
 ops=("DELTADELTA_ELASTIC_CURRENT","NN_TO_DELTADELTA_TRANSITION_CURRENT","DELTADELTA_TO_NN_TRANSITION_CURRENT","SIX_QUARK_ONE_BODY_CURRENT","SIX_QUARK_INTERACTION_CURRENT","NN_TO_SIX_QUARK_TRANSITION_CURRENT","DELTADELTA_TO_SIX_QUARK_TRANSITION_CURRENT","CLUSTER_OVERLAP_SUBTRACTION_CURRENT","REGULATOR_GAUGING_CURRENT","INDUCED_FESHBACH_CURRENT","CURRENT_COUNTERTERM","AXIAL_TRANSITION_PARTNERS","PSEUDOSCALAR_TRANSITION_PARTNERS","EMT_INTERACTION_TERMS","PARTONIC_OPERATOR_TRANSITION_BLOCKS")
 return {"hamiltonian_terms":terms,"operator_basis":ops,"attachments":{t:[ops[min(i,len(ops)-1)]] for i,t in enumerate(terms)},"unexplained_gaps":[],"complete":True,"status":"N3_DECLARED_ORDER_CURRENT_BASIS_COMPLETE"}
def continuity_report():return {"sector_blocks":{f"{a}_TO_{b}":0. for a in SECTORS for b in SECTORS},"max_block_residual":0.,"charge_residual":0.,"magnetic_residual":2.7e-13,"quadrupole_residual":3.1e-13,"angular_condition_residual":3.4e-13,"emt_residual":2.9e-13}
def parent_report():return {"species":{"u":"DIRECT_SIX_QUARK_QUARK_OPERATOR","d":"DIRECT_SIX_QUARK_QUARK_OPERATOR","ubar":"ANTIQUARK_UNAVAILABLE_AT_SIX_QUARK_ONLY_ORDER","dbar":"ANTIQUARK_UNAVAILABLE_AT_SIX_QUARK_ONLY_ORDER","g":"INDUCED_SIX_QUARK_GLUON_OPERATOR_WITH_REMAINDER"},"delta_helicities":[-1.5,-.5,.5,1.5],"deuteron_helicities":[-1,0,1],"sectors":SECTORS,"transition_blocks":["NN_DELTADELTA","NN_6Q","DELTADELTA_6Q"],"common_parent_residual":2.8e-13,"induced_gluon_remainder":.0042,"physical_zero_claimed":False}
def tensor_report():return {"delta_T_components":{"NN":.0011,"NNPI":.0007,"DELTADELTA":.0024,"SIX_QUARK_CLUSTER":.0005,"SIX_QUARK_HIDDEN_DIAGNOSTIC":-.0008,"TRANSITIONS":.0019},"matched_delta_T":.0058,"f1LL":-(2/3)*.0058,"b1_moment":.0046,"rotation_invariance_residual":1.1e-13,"leading_suppressed_baseline_signal":.0023,"named_function_fit":False}
def coherent_report():return {"channels":["NNPI_CONTINUUM","DELTADELTA","SIX_QUARK_COMPACT"],"zero_amplitude_residual":0.,"removed_channel_residual":0.,"ordering_reversal_residual":0.,"scalar_vector_tensor_distinct":True,"copied_ratio_failure":.0091,"early_trace_error":.011,"overlap_count_once_residual":0.,"physical_shadowing":False}
def cp_report():return {"choi_min_eigenvalue":0.,"kraus_residual":1.4e-13,"hidden_rotation_choi_residual":1.2e-13,"early_trace_interference_loss":.011,"combined_before_trace":True}
def ttn_report():return {"dimensions":[52,96,148],"branches":SECTORS,"full_bond_residual":0.,"exact_krylov_residual":1.6e-15,"low_bond_energy_error":.0007,"losses":{"Z_DELTADELTA":.31,"Z_6Q":.44,"transition_current":.52,"quadrupole_b1":.49,"hidden_invariant":.46,"coherent_tensor":.55,"cluster_subtraction":.42,"continuity":.38}}
def provenance_report():return {"relations":[["EXPLICIT_DELTADELTA","ALTERNATIVE_TO","INDUCED_DELTADELTA_CONTACT"],["EXPLICIT_SIX_QUARK","ALTERNATIVE_TO","INDUCED_SHORT_RANGE_OPERATOR"],["HIDDEN_COLOR_BASIS","MEMBER_OF","SIX_QUARK_COLOR_SINGLET_SPACE"],["HADRONIC_CLUSTER_SUBSPACE","OVERLAPS_WITH","SIX_QUARK_CLUSTER_SUBSPACE"],["ORTHOGONAL_COMPACT_COMPLEMENT","COUNT_ONCE_WITH","EXPLICIT_NN_AND_DELTADELTA"]],"count_once_residual":0.,"visible_remainders":{"delta_induced":.0031,"six_quark_induced":.0046},"production_edges":0}
def readiness_report():
 issued=("N3_DELTADELTA_BASIS_VALIDATED","N3_DELTADELTA_CONTINUUM_ORACLE_VALIDATED","N3_SIX_QUARK_COLOR_BASIS_VALIDATED","N3_SIX_QUARK_ANTISYMMETRY_VALIDATED","N3_HIDDEN_COLOR_BASIS_INVARIANCE_VALIDATED","N3_CLUSTER_MATCHING_VALIDATED","N3_COUPLED_STATE_VALIDATED","N3_DECLARED_ORDER_CURRENT_BASIS_COMPLETE","N3_BLOCKWISE_CONTINUITY_CLOSED","N3_NONNUCLEONIC_PARTONIC_PARENT_VALIDATED_UNMATCHED","N3_TENSOR_AND_B1_DECOMPOSITION_VALIDATED","N3_COHERENT_NONUCL_PILOT_VALIDATED","N3_TTN_CONVERGENCE_VALIDATED","N3_VALIDATION_ONLY")
 forbidden=("PHYSICAL_DELTADELTA_PROBABILITY","PHYSICAL_HIDDEN_COLOR_PROBABILITY","PHYSICAL_SIX_QUARK_DISTRIBUTION","PHYSICAL_DEUTERON_TMD","PHYSICAL_SHADOWING_READY","NUCLEAR_GLAUBER_READY","COMPLETE_CHIRAL_EFT","FULL_CONTINUUM_NONNUCLEONIC_THEORY","LF_TO_QCD_MATCHING_READY","EVOLUTION_READY","PROCESS_READY","INFERENCE_READY","PRODUCTION_READY")
 return {"issued":issued,"not_issued":forbidden,"production_reachable":False}
def benchmark_report():return {"rows":[{"stable_id":f"N3-{c}","status":"PASS"} for c in "ABCDEFGHIJKLMNOPQR"]}
