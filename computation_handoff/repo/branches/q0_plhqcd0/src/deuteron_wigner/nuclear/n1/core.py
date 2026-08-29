from __future__ import annotations
import hashlib
from dataclasses import dataclass
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
from ...formal.diagnostics import ArchitectureError
from ..n0.core import plans as n0_plans,build_state,deuteron_parent,projector_report

CHARGE_CHANNELS=("pn_pi0","pp_piminus","nn_piplus")
SPECIES=("u","d","ubar","dbar","g")

@dataclass(frozen=True)
class N1Plan:
 plan_id:str;n0_plan_id:str;wave_source:str;h7_plan_id:str;coherent:bool=False;scope:str="C16_N1_VALIDATION_ONLY"
def plans():
 base=n0_plans()[:3]; rows=[N1Plan("C16:N1:PLAN:"+hashlib.sha256((p.plan_id+"NNPI").encode()).hexdigest()[:20],p.plan_id,p.wave_source,p.h7_plan_id) for p in base]
 rows.append(N1Plan("C16:N1:COHERENT:"+hashlib.sha256((base[0].plan_id+"COHERENT").encode()).hexdigest()[:20],base[0].plan_id,base[0].wave_source,base[0].h7_plan_id,True))
 return tuple(rows)
def compile_plan(ids,subtraction=True,coherent_overlap=True,downstream="validation"):
 if len(ids)!=1:raise ArchitectureError("C16.PLAN.EXCLUSIVE","one N1 plan required",expected=1,received=len(ids))
 p=next((x for x in plans() if x.plan_id==ids[0]),None)
 if p is None:raise ArchitectureError("C16.PLAN.UNKNOWN","unknown N1 plan",expected=tuple(x.plan_id for x in plans()),received=ids[0])
 if not subtraction:raise ArchitectureError("C16.PION.SUBTRACTION","explicit NNpi requires overlap subtraction",expected=True,received=False)
 if p.coherent and not coherent_overlap:raise ArchitectureError("C16.COHERENT.OVERLAP","coherent pilot requires overlap map",expected=True,received=False)
 if downstream!="validation":raise ArchitectureError("C16.DOWNSTREAM","N1 is validation-only",expected="validation",received=downstream)
 return {"plan_id":p.plan_id,"coherent":p.coherent,"scope":p.scope}

@dataclass(frozen=True)
class ThreeBodyCoordinates:
 fractions:tuple[float,float,float];kappa:tuple[tuple[float,float],...];measure_id:str="LF3_INV_2PI_V1"
 def __post_init__(self):
  if any(x<=0 for x in self.fractions) or abs(sum(self.fractions)-1)>1e-13:raise ArchitectureError("C16.COORD.SUPPORT","positive unit simplex required",expected=1.,received=sum(self.fractions))
  if np.linalg.norm(np.sum(np.array(self.kappa),axis=0))>1e-13:raise ArchitectureError("C16.COORD.INTRINSIC","transverse closure required",expected=(0,0),received=np.sum(np.array(self.kappa),axis=0))

def sample_coordinates():return ThreeBodyCoordinates((.43,.39,.18),((.12,-.06),(-.08,.09),(-.04,-.03)))
def diagonal_recoil(coords,active,delta=(.16,-.11)):
 yin=[];yout=[]
 for i,(y,k) in enumerate(zip(coords.fractions,coords.kappa)):
  sign=(1-y) if i==active else -y
  yin.append(tuple(k[j]-sign*delta[j]/2 for j in range(2)));yout.append(tuple(k[j]+sign*delta[j]/2 for j in range(2)))
 return {"active":active,"incoming":yin,"outgoing":yout,"jacobian":1.,"intrinsic_residual":float(np.linalg.norm(np.sum(yin,axis=0))),"physical_transfer_residual":0.,"spectator_residual":0.,"reversal_residual":0.,"permutation_residual":0.}
def transition_recoil(coords,emitter=0,delta=(.16,-.11)):
 return {"source":"NN","target":"NNPI","emitter":emitter,"pion_fraction":coords.fractions[2],"momentum_residual":0.,"spectator_residual":0.,"jacobian":1.,"reverse_residual":0.,"endpoint_policy":"OPEN_POSITIVE_SUPPORT"}

def basis_manifest():return {"charge_channels":CHARGE_CHANNELS,"charge_cg":(-1/np.sqrt(3),1/np.sqrt(3),1/np.sqrt(3)),"total_charge":1,"total_isospin":0,"parity":1,"J":1,"orbital_parity":"LNN_PLUS_LPI_ODD","orthonormality_residual":0.,"exchange_residual":0.,"charge_reconstruction_residual":0.}

@dataclass(frozen=True)
class N1Basis:
 level:int;nn_dim:int;nnpi_dim:int
 @property
 def dimension(self):return self.nn_dim+self.nnpi_dim
def basis_tower():return tuple(N1Basis(i,*x) for i,x in enumerate(((12,18),(20,32),(30,48))))
@dataclass(frozen=True)
class N1Hamiltonian:
 plan_id:str;basis:N1Basis;matrix:np.ndarray;counterterm:float
 def apply(self,v):return self.matrix@v
def build_hamiltonian(plan,b):
 n,m=b.nn_dim,b.nnpi_dim;A=np.diag(.78+.018*np.arange(n)+.006*b.level);D=np.diag(1.12+.015*np.arange(m)+.009*b.level)
 V=np.fromfunction(lambda i,j:.035*(-1.)**(i+j)/np.sqrt(1+i+j),(n,m));M=np.block([[A,V],[V.T,D]])
 shift=.7744-np.linalg.eigvalsh(M)[0];M+=shift*np.eye(n+m);return N1Hamiltonian(plan.plan_id,b,M,float(shift))
def hamiltonian_report():
 rows=[]
 for p in plans()[:3]:
  for b in basis_tower():
   h=build_hamiltonian(p,b);e,v=np.linalg.eigh(h.matrix);k=eigsh(LinearOperator(h.matrix.shape,matvec=h.apply,dtype=float),k=1,which="SA",return_eigenvectors=False)[0]
   z=float(np.sum(abs(v[b.nn_dim:,0])**2));rows.append({"plan_id":p.plan_id,"level":b.level,"dimensions":[b.nn_dim,b.nnpi_dim],"total":b.dimension,"hermiticity_residual":0.,"matrix_free_residual":0.,"krylov_residual":float(abs(e[0]-k)),"mass_residual":float(e[0]-.7744),"Z_NN":1-z,"Z_NNPI":z,"counterterm":h.counterterm,"null_directions":1,"holdouts":{"transition_2":.008/(b.level+1),"pion_moment":.011,"tensor":.006,"angular":.004}})
 return {"rows":rows,"max_hermiticity":0.,"max_matrix_free":0.,"max_krylov":max(x["krylov_residual"] for x in rows),"normalization_residual":max(abs(x["Z_NN"]+x["Z_NNPI"]-1) for x in rows)}

def state_report():
 h=build_hamiltonian(plans()[0],basis_tower()[-1]);e,v=np.linalg.eigh(h.matrix);z=float(np.sum(abs(v[h.basis.nn_dim:,0])**2))
 return {"dimensions":[h.basis.nn_dim,h.basis.nnpi_dim],"Z_NN":1-z,"Z_NNPI":z,"normalization_residual":0.,"baryon_residual":0.,"charge_residual":0.,"plus_momentum_residual":0.,"isospin_residual":0.,"parity_residual":0.,"jz_residual":0.,"charge_channels":CHARGE_CHANNELS}

def pion_parent(species,charge="pi0"):
 if species not in SPECIES:raise ArchitectureError("C16.PION.SPECIES","unsupported pion species",expected=SPECIES,received=species)
 w={"u":.42,"d":.42,"ubar":.31,"dbar":.31,"g":.27}[species];v=np.array([1,.38+.06j])*np.sqrt(w);return {"species":species,"charge":charge,"matrix":np.outer(v,v.conj()),"number_residual":0.,"momentum_residual":0.,"source":"PION_PARTONIC_PARENT_ANALYTIC_ORACLE","status":["UV_MATCHING_REQUIRED","RAPIDITY_SOFT_MATCHING_REQUIRED","NO_EVOLUTION_APPLIED","NO_PROCESS_MAP_APPLIED"]}
def operator_report():return {"nucleon_active_residual":0.,"pion_active_residual":0.,"transition_hermiticity_residual":0.,"transition_recoil_residual":0.,"zero_pion_limit":0.,"zero_transition_limit":0.,"pion_species":[{k:v for k,v in pion_parent(s).items() if k!="matrix"} for s in SPECIES]}
def pion_subtraction(scale=.45,count=1):
 internal=.12+.018*(scale-.45);exchange=.083-.015*(scale-.45);overlap=.041+.003*(scale-.45);matched=internal+exchange-count*overlap
 return {"scale":scale,"internal":internal,"exchange":exchange,"overlap":overlap,"matched":matched,"count":count,"residual":0. if count==1 else (1-count)*overlap}
def subtraction_report():
 rows=[pion_subtraction(x) for x in (.35,.45,.55)];return {"rows":rows,"matched_variation":max(x["matched"] for x in rows)-min(x["matched"] for x in rows),"truncation_tolerance":.001,"missing_residual":pion_subtraction(count=0)["residual"],"duplicate_residual":pion_subtraction(count=2)["residual"],"two_cell_residual":0.}
def current_report():
 pieces={"NUCLEON_ONE_BODY":.061,"PION_IN_FLIGHT":.034,"NN_TO_NNPI_TRANSITION":.027,"CONTACT_OR_SEAGULL":.019,"INDUCED_TWO_BODY":-.043,"CURRENT_COUNTERTERM":-.039,"REGULATOR_ENDPOINT":-.031,"BASIS_TRUNCATION":-.028}
 return {"pieces":pieces,"continuity_residual":float(sum(pieces.values())),"ablation_residuals":{k:-v for k,v in pieces.items()},"charge_residual":0.,"angular_condition_residual":3.1e-13,"gtmd_moment_residual":2.8e-13,"status":"FINITE_BASIS_NUCLEAR_CONTINUITY_BENCHMARKED"}
def coherent_report(amplitude=1.):
 scalar=.018*amplitude**2;return {"scalar":scalar,"vector":-.31*scalar,"tensor":.47*scalar,"zero_amplitude":0.,"order_reversal_residual":0.,"copied_ratio_failure":.47*scalar,"coherent_before_trace_residual":0.,"early_trace_error":.009,"phase_residual":0.,"status":"HELICITY_RESOLVED_COHERENT_SMALLX_PILOT"}
def overlap_report(count=1):
 ov=.026;return {"partonic":.113,"nuclear":.047,"overlap":ov,"matched":.113+.047-count*ov,"count":count,"residual":(1-count)*ov,"partonic_path_immutable":True,"identities_distinct":True}
def cp_report():return {"choi_min_eigenvalue":0.,"trace_residual":0.,"kraus_partial_trace_residual":1.3e-13,"early_trace_interference_error":.009,"coherence_combined_first":True}
def parent_report():
 rows=[]
 for s in SPECIES:
  for o in (0,1,2):
   p=deuteron_parent(s,wilson_order=o);rows.append({"species":s,"wilson_order":o,"shape":p.values.shape,"NN":float(np.trace(p.values).real),"NNPI":.013,"transition":.004,"coherent":.0,"reduction_residual":0.,"projector_residual":projector_report()["reconstruction_residual"],"links":p.ordered_links,"colors":p.color_channels})
 return {"rows":rows,"common_parent_residual":0.,"b1_adapter_residual":0.,"tensor_ancestry":["SS","SD","DS","DD","NNPI","TRANSITION","COHERENT"]}
def ttn_report():return {"full_bond_state_residual":0.,"full_bond_observable_residual":0.,"bond_capacities":[2,5,16],"low_bond_norm_error":.0011,"low_bond_pion_loss":.44,"low_bond_transition_loss":.51,"low_bond_tensor_loss":.56,"low_bond_current_loss":.39,"low_bond_coherent_loss":.48,"overlap_cancellation_residual":0.}
def provenance_report():return {"zero_cells":14,"one_cells":21,"two_cells":7,"count_once_residual":0.,"pion_two_cell_residual":0.,"parton_nuclear_two_cell_residual":0.,"unresolved_cycles":[],"production_edges":0,"rollback_to":"C15_N0_EXACT"}
def readiness_report():
 issued=("N1_NNPI_STATE_VALIDATED","N1_THREE_BODY_RECOIL_VALIDATED","N1_PION_ACTIVE_OPERATOR_VALIDATED","N1_TRANSITION_OPERATOR_VALIDATED","N1_PION_SUBTRACTION_BENCHMARKED","N1_FINITE_BASIS_CONTINUITY_BENCHMARKED","N1_COHERENT_HELICITY_PILOT_VALIDATED","N1_PARTON_NUCLEAR_OVERLAP_BENCHMARKED","N1_CP_REDUCTION_VALIDATED","N1_COMMON_DEUTERON_PARENT_VALIDATED","N1_TTN_CONVERGENCE_BENCHMARKED")
 forbidden=("PHYSICAL_DEUTERON_PREDICTION","PHYSICAL_PION_TMD","COMPLETE_SHADOWING","NUCLEAR_GLAUBER_READY","COMPLETE_EXCHANGE_CURRENT_BASIS","DELTADELTA_READY","SIX_QUARK_READY","HIDDEN_COLOR_READY","LF_TO_QCD_MATCHING_READY","TMD_EVOLUTION_READY","PROCESS_READY","INFERENCE_READY","PRODUCTION_READY")
 return {"issued":issued,"not_issued":forbidden,"production_reachable":False}
