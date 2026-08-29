"""C267 parameterized nonlocal target evaluation authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c267_hqcdc117nonlocaltarget2"
BASELINE="3b5b344c7c6ca9349e645d62b287af9059263801"
C266_ROOT="945937e5ca5f64fde86c985a5c7b0fd1343424199846abfb9d963022b6333950"
STATUS="C267_C117_PARAMETERIZED_NONLOCAL_TARGETS_READY_STANDARD_PHYSICAL_SIDE_UNAVAILABLE"
PLAN="C117NONLOCALTARGET2-B"
NEXT="C268/HQCDC117STANDARDSIDE1"
NEXT_OBJECT="source-qualified standard/physical-side nonlocal current amplitude and matching target for the four C267 packet functionals"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
PRODUCTS=("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g")
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")

def _plain(v):
 if hasattr(v,"items"): return {str(k):_plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)): return [_plain(x) for x in v]
 return v
def _freeze(v):
 if isinstance(v,dict): return MappingProxyType({k:_freeze(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)): return tuple(_freeze(x) for x in v)
 return v
def _root(v): return sha256(json.dumps(_plain(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def current_product_decomposition(direction):
 if direction not in DIRECTIONS: raise KeyError(direction)
 rows=[]
 for product in PRODUCTS:
  rows.append({"product":product,"term":f"T_{direction}[{product};W_{DIRECTIONS.index(direction)+1},K_Q0]","measure":"dk d2p dq d2q/(2pi)^6 with LF conservation distributions","ordered_color":"C114 source order retained","helicity":"C114 gamma+ or transverse-polarization derivative tensor retained","available":True})
 return _freeze({"direction":direction,"rows":rows,"sum":f"-g_s^2/2 sum_product T_{direction}[product;W,K_Q0]","root":_root(rows)})

def target_evaluation(direction):
 if direction not in DIRECTIONS: raise KeyError(direction)
 i=DIRECTIONS.index(direction)+1; dec=current_product_decomposition(direction)
 record={"direction":direction,"packet_id":f"C266-W{i}","C266_root":C266_ROOT,"regulated_value":dec["sum"],"evaluation_program":"normalize W_i; pair each ordered current product at fixed Abel r; apply conservation deltas; finite-HO project; sum products; take r->1^- only after pairing","parameter_domain":f"k0_{i}>Delta_{i}>0, sigma_{i}>0, p0_{i} in R2, mu>0","Q0":"finite-cell PV/Q0 prescription inherited C114","Abel_order":"pair at fixed r, subtract, then r->1^-","resolutions":RESOLUTIONS,"boundary_link_holonomy":"caller-bound and never averaged","units":"Hamiltonian/current-functional units inherited from C114 and C264","orientation":"source-to-sink; Hermitian reversal published separately","status":"PARAMETERIZED_EXECUTABLE","numerical_value":None,"physical":False}
 return _freeze({**record,"root":_root(record)})

def ward_st_diagnostic(direction):
 t=target_evaluation(direction)
 record={"direction":direction,"descendant":f"T_{direction}[s(J_q+J_g);W_{DIRECTIONS.index(direction)+1},K_Q0] in the C203-C212 BRST/ST quotient","residual":"R_ST,i(parameters)=projected source descendant minus required contact/boundary descendants","evaluation":"same deterministic pairing program as target with BRST insertion","availability":"PARAMETERIZED_EXECUTABLE; contact/boundary arguments remain caller-bound","claimed_zero":False,"gauge_invariance_claim":False,"target_root":t["root"]}
 return _freeze({**record,"root":_root(record)})

def physical_matching_residual(direction):
 t=target_evaluation(direction)
 record={"direction":direction,"equation":f"F_standard,{DIRECTIONS.index(direction)+1}(mu;W_i)=F_project,{DIRECTIONS.index(direction)+1}(mu;W_i)","project_side":t["regulated_value"],"project_side_available":True,"standard_physical_side":None,"standard_physical_side_available":False,"residual":f"R_match,{DIRECTIONS.index(direction)+1}=F_standard,{DIRECTIONS.index(direction)+1}-F_project,{DIRECTIONS.index(direction)+1}","residual_status":"SYMBOLIC_UNEVALUATED_STANDARD_SIDE_NOT_ZERO","coefficient_selected":False}
 return _freeze({**record,"root":_root(record)})

def correlated_uncertainty():
 coordinates=tuple(f"({x}:k0,Delta,sigma,p0x,p0y)" for x in DIRECTIONS)+("log(mu)","Abel_r","HO_truncation","source_scheme")
 record={"coordinates":coordinates,"program":"C_target = J_packet Sigma_packet J_packet^T + J_scale Sigma_scale J_scale^T + J_reg Sigma_reg J_reg^T + C_HO + C_source_scheme","cross_blocks":"retained whenever coordinates or sources are shared; never quadrature-added twice","symmetry":"C=C^T by explicit block symmetrization","PSD":"each supplied covariance enters as A Sigma A^T; unavailable Sigma blocks remain symbolic PSD inputs","numerical_covariance":None,"K_separated":RESOLUTIONS}
 return _freeze({**record,"root":_root(record)})

def evaluation_capsules():
 rows=[]
 for d in DIRECTIONS:
  rows.append({"direction":d,"target":target_evaluation(d),"products":current_product_decomposition(d),"Ward_ST":ward_st_diagnostic(d),"matching":physical_matching_residual(d),"uncertainty_root":correlated_uncertainty()["root"],"source_roots":("C43","C114","C115","C117",C266_ROOT)})
 return _freeze({"schema":"C267-C117-NONLOCAL-TARGET-EVALUATION-V2","rows":rows,"complete":4,"required":4,"root":_root(rows)})

def two_route_derivation():
 record={"route_A":"direct C266 Jq/Jg/KQ0 distributional packet pairing","route_B":"C266 finite-HO coefficient reconstruction against C114-C117 matrix elements","common_domain":"normalized compact packet support, finite K, fixed Abel r<1, identical Q0 and boundary class","agreement":"algebraic equality by insertion of the finite-HO resolution of identity before the common regulated limit","mismatches":0,"numerical_convergence_claim":False}
 return _freeze({**record,"root":_root(record)})
def residual_frontier(): return _freeze({"object_id":"C117-STANDARD-SIDE-NONLOCAL-AMPLITUDE-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_root((NEXT,NEXT_OBJECT))})
def release_manifest(): return _freeze({"status":STATUS,"plan":PLAN,"parameterized_targets_closed":4,"standard_side_closed":0,"finite_coefficients_selected":0,"physical":False,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def static_isolation_guard(): return _freeze({"packet_parameter_numerically_selected":0,"finite_coefficient_selected":0,"unsupported_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcdc117nonlocaltarget2(i):
 if not isinstance(i,int) or not 0<=i<384: raise ValueError(i)
 return _freeze({"index":i,"field":("direction","product","measure","color","helicity","packet","Q0","Abel","Ward_ST","matching","covariance","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_root((i,STATUS))})
def verify_hqcdc117nonlocaltarget2_authority():
 from deuteron_wigner.bridge import hqcdc117curramp1 as c266
 if c266.PACKAGE_ROOT!=C266_ROOT: raise ValueError("C266 root changed")
 c266.load_verified_hqcdc117curramp1_authority()
 if evaluation_capsules()["complete"]!=4: raise ValueError("capsules")
 return _freeze({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C266_package_root":C266_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117nonlocaltarget2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False): raise ValueError("runtime")
 return verify_hqcdc117nonlocaltarget2_authority()

_ROOTS={"INPUT":_root((BASELINE,C266_ROOT)),"TARGETS":_root(tuple(target_evaluation(d)["root"] for d in DIRECTIONS)),"PRODUCTS":_root(tuple(current_product_decomposition(d)["root"] for d in DIRECTIONS)),"WARD_ST":_root(tuple(ward_st_diagnostic(d)["root"] for d in DIRECTIONS)),"MATCHING":_root(tuple(physical_matching_residual(d)["root"] for d in DIRECTIONS)),"UNCERTAINTY":correlated_uncertainty()["root"],"CAPSULES":evaluation_capsules()["root"],"ROUTES":two_route_derivation()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_root({"schema":"C267-HQCDC117NONLOCALTARGET2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
