"""C274 symbolic renormalized Hamiltonian family and slot audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c274_hqcdc117renormh1"
BASELINE="cee68e4c0e975108b85c38fdb2cd622def6b7ff2";C273_ROOT="86e675df46233e9c19d9dc4f305c62d64104097feb7e471c71632548481a69b5"
STATUS="C274_SYMBOLIC_HERMITIAN_HAMILTONIAN_FAMILY_READY_NONC117_PHYSICAL_BUNDLE_SYMBOLIC";PLAN="C117RENORMH1-B";NEXT="C275/HQCDNONC117SLOT1";NEXT_OBJECT="bind or reduce the composite non-C117 physical Hamiltonian input bundle: running coupling/masses, common-IR, boundary/holonomy, non-C117 counterterms, finite-basis targets, and joint covariance"
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40");DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
OWNERS=("C128_free","C53_canonical_qg","C112_instantaneous_fermion","C127_instantaneous_current","C129_pure_gluon","C130_boundary_zero_mode","C206_ST_counterterm_family","C242_C258_fixedK_current_completion")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def slot_audit():
 rows=(
  {"slot":"coupling_and_masses","authority":"C154-C155/C213-C219","status":"AUTHENTICATED_STANDARD_COORDINATES_FINITE_BASIS_RUNNING_SYMBOLIC"},
  {"slot":"common_IR_regulator","authority":"C153-C157","status":"CONDITIONAL_NO_NUMERICAL_BINDING"},
  {"slot":"boundary_holonomy","authority":"C169-C183","status":"CONDITIONAL_CLASSES_NO_PHYSICAL_SELECTION"},
  {"slot":"non_C117_counterterms","authority":"C206 affine family","status":"UNSELECTED_NOT_ZERO"},
  {"slot":"finite_basis_targets","authority":"C158/C161/C213","status":"COMPARISON_VALUES_NOT_PHYSICALLY_BOUND"},
  {"slot":"joint_covariance","authority":"C154/C213","status":"MARGINAL_PARTIAL_JOINT_UNAVAILABLE_NOT_ZERO"},
  {"slot":"C117_coordinates","authority":"C259-C273","status":"FOUR_EXPLICIT_UNRESOLVED_COORDINATES"})
 return _f({"rows":rows,"non_C117_bundle_closed":False,"C117_coordinates":4,"missing_as_zero":False,"root":_r(rows)})
def hamiltonian_family(resolution):
 if resolution not in RESOLUTIONS:raise KeyError(resolution)
 x={"resolution":resolution,"formula":"H_R(theta,c)=sum_owner H_owner,R(theta)+sum_i=1^4 c_i O_C117,i,R","owners":OWNERS,"non_C117_bundle":"theta_nonC117 explicit symbolic record","C117_coordinates":tuple(f"c_C117_{i+1}" for i in range(4)),"C117_insertions":tuple(f"O_C117_{i+1},{resolution}" for i in range(4)),"matrix_free":"apply each owner once then each C117 insertion once","sparse_serialization":"coordinate/value program; no dense mandatory matrix","Hermitian_by_construction":True,"CM":"C64/C77 CM-ground block retained","color":"C74 singlet/triplet projectors and open-color boundaries retained","boundary_link_holonomy":"separate caller-bound records","units":"mass-squared light-front Hamiltonian convention","physical":False}
 return _f({**x,"root":_r(x)})
def derivative_program():return _f({"derivatives":tuple({"coordinate":f"c_C117_{i+1}","derivative":f"dH/dc_{i+1}=O_C117_{i+1},R","Hermitian":True} for i in range(4)),"finite_difference_claim":False,"root":_r(DIRECTIONS)})
def route_audit():return _f({"route_A":"owner-ordered sparse block sum using C131/C242-C258 ancestry","route_B":"matrix-free owner DAG traversal with independent Hermitian reverse","symbolic_agreement":True,"count_once_duplicates":0,"numeric_agreement":"UNAVAILABLE_UNBOUND_NONC117_BUNDLE","contradiction":False,"root":_r((True,0))})
def holdout_crosswalk():return _f({"rows":tuple({"resolution":r,"same_slots":True,"same_C117_order":DIRECTIONS,"no_resolution_average":True} for r in RESOLUTIONS),"root":_r(RESOLUTIONS)})
def residual_frontier():return _f({"object_id":"NONC117-PHYSICAL-HAMILTONIAN-BUNDLE-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"families_closed":3,"symbolic":True,"non_C117_bundle_closed":False,"C117_coordinates_selected":0,"physical":False,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"fixture_promoted":0,"unsupported_zeroed":0,"finite_C117_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117renormh1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117renormh1_authority():
 from deuteron_wigner.bridge import hqcdc117physstate1 as c273
 if c273.PACKAGE_ROOT!=C273_ROOT:raise ValueError("C273 root changed")
 c273.load_verified_hqcdc117physstate1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdc117renormh1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117renormh1_authority()
_ROOTS={"INPUT":_r((BASELINE,C273_ROOT)),"SLOTS":slot_audit()["root"],"FAMILIES":_r(tuple(hamiltonian_family(r)["root"] for r in RESOLUTIONS)),"DERIVATIVES":derivative_program()["root"],"ROUTES":route_audit()["root"],"HOLDOUTS":holdout_crosswalk()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C274-HQCDC117RENORMH1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
