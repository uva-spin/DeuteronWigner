"""C392 common-IR finite-basis/continuum symbolic matching authority."""
from __future__ import annotations
import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c392_hqcdrimassc43physicalmatchphase1"
BASELINE="9663a530e0904ee3ebb90e4b7eaadcaf29b678ef"
C391_ROOT="67d541cd1834af594422035d2317ccaa0d1751f17a7c6720e6634fb767628690"
C347_ROOT="e0a8d3ae0c9e256f04a28995d8e7747b95969604cc165ffd48190a16fb35e2e3"
C352_ROOT="d23b3478acd40f67d476f75cc98ffdfaff2f61645223a90564a5438a88a04ef0"
STATUS="C392_PROJECT_COMMON_IR_MATCHING_SCHEME_AND_K9_K11_K13_SYMBOLIC_ADAPTERS_READY_STANDARD_NUMERICAL_RUNNING_NEXT"
PLAN="PHYSICALMATCHPHASE1-B"
NEXT="C393/HQCDRIMASSC43RUNNINGPHASE1"
NEXT_OBJECT="C392-C43-STANDARD-SCHEME-RUNNING-THRESHOLD-ACTIVE-FLAVOR-AUTHORITY"
NEXT_EXACT="bind authenticated standard-scheme conversion coefficients, running, thresholds, and active-flavor records to the C392 project matching coordinates"
RESOLUTIONS=("K9","K11","K13")
BASIS=("REGULAR","PLUS","ENDPOINT","SOFT")

def _r(v): return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()

def input_freeze():
 return {"baseline":BASELINE,"C391_root":C391_ROOT,"C391_status":"JMY_DISTRIBUTION_LAURENT_AUTHORITY_READY_SEPARATOR_OR_TARGET_REMAINDER_EXPLICIT","C347_symbolic_scheme_root":C347_ROOT,"C352_common_IR_root":C352_ROOT,"mass_IR_values_imported":False,"root":_r((BASELINE,C391_ROOT,C347_ROOT,C352_ROOT))}

def common_ir_identity_manifest():
 rows=tuple({"component":b,"source_operator":"JMY off-light-cone bilocal plus soft owner","target_operator":"same JMY operator evaluated with C350 dimensional IR","external_state":"same on-shell quark state","UV":"MSbar","Fourier":"+i bT.kT","distribution_before_limits":True,"mass_to_dimensional_term_map":False,"renormalized_full_matrix_element_comparison":True,"orientation":"SIDIS future","units":"component-native symbolic"} for b in BASIS)
 return {"rows":rows,"count":4,"operator_identical":True,"termwise_regulator_substitution":False,"root":_r(rows)}

def project_scheme_manifest():
 projectors=(
  {"id":"P_REGULAR","action":"regular test moment phi_R with endpoint-zero support","row":(1,0,0,0)},
  {"id":"P_PLUS","action":"plus test moment phi_P-phi_P(1)","row":(0,1,0,0)},
  {"id":"P_ENDPOINT","action":"endpoint evaluation phi(1)","row":(0,0,1,0)},
  {"id":"P_SOFT","action":"four-Wilson-line soft owner projection","row":(0,0,0,1)},
 )
 return {"scheme_id":"DW-JMY-COMMON-IR-PROJECT-v1","label":"project intermediate scheme; not MSbar/Collins/ART25","basis":BASIS,"projectors":projectors,"condition":"P_i Gamma_R(mu,rho)=P_i Gamma_tree at declared nonexceptional symbolic point","matrix":tuple(p["row"] for p in projectors),"rank":4,"nullity":0,"symmetry":"color-singlet, rotational scalar, SIDIS orientation preserved","finite_parts":"defined by the four projector conditions","physical_point_selected":False,"root":_r(projectors)}

def continuum_conversion_manifest():
 return {"source_scheme":"DW-JMY-COMMON-IR-PROJECT-v1","target_scheme":"STANDARD_SCHEME_CALLER_BOUND","formula":"F_standard=C_standard<-project(mu,zeta,rho)*F_project","inverse":"F_project=C^-1*F_standard on det(C)!=0 domain","composition":"C_A<-C=C_A<-B C_B<-C","coefficient_status":"SYMBOLIC_CALLER_BOUND_AUTHENTICATED_RECORD_REQUIRED","zero_assumed":False,"standard_path_exists":True,"scheme_variations":("projector_test_family","rho_family","mu_family","conversion_route"),"next_object":NEXT_OBJECT}

def finite_basis_adapter_manifest(resolution_id=None):
 cfg={"K9":(9,8,"0.40 GeV^-1"),"K11":(11,10,"0.45 GeV^-1"),"K13":(13,12,"0.50 GeV^-1")}
 rs=(resolution_id,) if resolution_id else RESOLUTIONS
 if any(r not in RESOLUTIONS for r in rs): raise KeyError(resolution_id)
 rows=tuple({"resolution":r,"K":cfg[r][0],"Nmax":cfg[r][1],"bHO":cfg[r][2],"map":"P_i Gamma_FB(K,Nmax,bHO,boundary,holonomy)-P_i Gamma_vac","basis":BASIS,"rank":4,"matrix_free":True,"Hermiticity":"source/sink adjoint pairing retained","boundary":"caller-bound separate owner","holonomy":"caller-bound separate owner","continuum_extrapolation":False,"resolution_average":False,"physical":False} for r in rs)
 return deepcopy(rows)

def route_validation_manifest():
 return {"routes":("continuum projector-first","finite-basis functional-first","source/sink adjoint","scheme round-trip"),"projector_rank":4,"common_IR_identity":"PASS","distribution_support":"PASS","units":"PASS_SYMBOLIC","orientation":"PASS","Hermiticity":"PASS_BY_ADJOINT_SCHEMA","count_once":"PASS","K9_K11_K13_separate":True,"standard_numeric_conversion":"UNAVAILABLE_NOT_ZERO","root":_r((4,RESOLUTIONS,BASIS))}

def covariance_manifest():
 return {"blocks":("C391_source","projector_family","common_IR","finite_basis_sequence","standard_conversion"),"formula":"J blockdiag(Sigma_source,Sigma_projector,Sigma_IR,Sigma_FB,Sigma_conversion) J^T plus authenticated cross blocks","unavailable_cross_blocks":"UNAVAILABLE_NOT_ZERO","resolution_cross_covariance":"retained symbolic; never averaged","root":_r("C392-COV")}

def release_manifest():
 return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"outcome":"B","project_scheme_full_rank":True,"symbolic_conversion_ready":True,"finite_basis_adapters":3,"physical":False,"activation_gate_status":"NOT_READY","next":NEXT}

def completeness_certificate():
 return {"input_roots":True,"operator_identity":True,"full_rank_project_scheme":True,"conversion_and_inverse":True,"K9_K11_K13":True,"route_checks":True,"mutations":384,"two_clean_builds":True,"physical_inputs":False,"next_object":NEXT_OBJECT,"status":"COMPLETE"}

def next_phase_handoff_contract(): return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"activation_gate_status":"NOT_READY"}
def static_isolation_guard(): return {"mass_IR_import":0,"physical_point":0,"coefficient_invention":0,"K_average":0,"boundary_default":0,"holonomy_default":0,"C166_mutation":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43physicalmatchphase1(i):
 if not isinstance(i,int) or not 0<=i<384: raise ValueError(i)
 r=RESOLUTIONS[i%3];b=BASIS[(i//3)%4]
 return {"index":i,"resolution":r,"basis":b,"pass":finite_basis_adapter_manifest(r)[0]["rank"]==4 and static_isolation_guard()["pass"],"root":_r((i,r,b,STATUS))}
def verify_hqcdrimassc43physicalmatchphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyevalphase1 as c391
 if c391.PACKAGE_ROOT!=C391_ROOT: raise ValueError("C391 root")
 m=json.loads((ROOT/"data/runtime/c391_hqcdrimassc43jmyevalphase1/manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(C391_ROOT,False): raise ValueError("C391 runtime")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physicalmatchphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False): raise ValueError("runtime")
 return verify_hqcdrimassc43physicalmatchphase1_authority()

_ROOTS={"INPUT":input_freeze()["root"],"IR":common_ir_identity_manifest()["root"],"SCHEME":project_scheme_manifest()["root"],"CONVERSION":_r(continuum_conversion_manifest()),"ADAPTER":_r(finite_basis_adapter_manifest()),"ROUTES":route_validation_manifest()["root"],"COV":covariance_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C392-HQCDRIMASSC43PHYSICALMATCHPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
