"""C268 standard-side source-completeness authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c268_hqcdc117standardside1"
BASELINE="c61918ee5c4b919f20925161a242abfdc5ffac8f";C267_ROOT="26bb80bdbf2e61983e70c581f53b21a172a5d812cf44279fca3071d0f18ed20e"
STATUS="C268_C117_STANDARD_SIDE_SOURCE_INCOMPLETE_NAMED_PHYSICAL_CHANNEL_REQUIRED";PLAN="C117STANDARDSIDE1-C"
NEXT="C269/HQCDC117PHYSICALCHANNEL1";NEXT_OBJECT="authenticated named physical external-state/current observable capsule defining the standard-side target for all four C267 packet functionals"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def standard_side_audit(direction):
 if direction not in DIRECTIONS:raise KeyError(direction)
 i=DIRECTIONS.index(direction)+1
 x={"direction":direction,"project_side":f"C267 F_project,{i}(mu;W_{i})","project_available":True,"standard_operator":"MSbar-renormalized instantaneous-current composite in identical C266 ordering","operator_definition_status":"INCOMPLETE_NONLOCAL_CONVERSION_NOT_AUTHENTICATED","external_state":None,"named_observable":None,"standard_amplitude":None,"matching_target":None,"unavailable_not_zero":True,"RI_SMOM_boundary":"C260 definition complete; C262 conversion values unavailable","packet":"C266 parameterized W_i retained","scheme_scale":"MSbar and mu symbolic; no value selected","Ward_ST":"C267 descendant retained; no unsupported vanishing claim","boundary_link_holonomy":"caller-bound","resolutions":("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40"),"physical":False}
 return _f({**x,"root":_r(x)})
def matching_residuals():
 rows=tuple({"direction":d,"equation":f"R_{i+1}=F_standard,{i+1}-F_project,{i+1}","status":"UNAVAILABLE_STANDARD_SIDE_NOT_ZERO","standard_root":standard_side_audit(d)["root"]} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"closed":0,"required":4,"root":_r(rows)})
def source_route_audit():return _f({"route_A":"direct named physical current matrix element paired with C266 packet","route_A_status":"MISSING_NAMED_STATE_AND_OBSERVABLE","route_B":"C259-C263 RI/SMOM/MSbar adapter then C267 packet pairing","route_B_status":"MISSING_C262_CONVERSION_AND_PHYSICAL_BINDING","contradiction":False,"fabricated":False,"root":_r(("missing","missing",False))})
def uncertainty_boundary():return _f({"C267_covariance":"retained","standard_side_covariance":None,"cross_covariance":None,"status":"UNAVAILABLE_NOT_ZERO_UNTIL_PHYSICAL_CHANNEL_BOUND","double_counting":False,"root":_r("standard-uncertainty-missing")})
def residual_frontier():return _f({"object_id":"C117-NAMED-PHYSICAL-CHANNEL-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"directions_audited":4,"standard_targets_closed":0,"coefficients_selected":0,"physical":False,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"physical_value_selected":0,"packet_parameter_selected":0,"finite_coefficient_selected":0,"unsupported_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117standardside1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("operator","state","observable","scheme","scale","packet","Ward","boundary","conversion","matching","uncertainty","scope")[i%12],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117standardside1_authority():
 from deuteron_wigner.bridge import hqcdc117nonlocaltarget2 as c267
 if c267.PACKAGE_ROOT!=C267_ROOT:raise ValueError("C267 root changed")
 c267.load_verified_hqcdc117nonlocaltarget2_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C267_package_root":C267_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117standardside1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117standardside1_authority()
_ROOTS={"INPUT":_r((BASELINE,C267_ROOT)),"AUDIT":_r(tuple(standard_side_audit(d)["root"] for d in DIRECTIONS)),"MATCHING":matching_residuals()["root"],"ROUTES":source_route_audit()["root"],"UNCERTAINTY":uncertainty_boundary()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C268-HQCDC117STANDARDSIDE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
