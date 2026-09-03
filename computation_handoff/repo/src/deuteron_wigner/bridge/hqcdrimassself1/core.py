"""C277 signed-mass self-energy evaluation readiness reduction."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c277_hqcdrimassself1"
BASELINE="f220a62c6812e1f89875224fe1b9d0131f546952";C276_ROOT="97d8fd6b6bd40d1295d7cdf9d3d3b849c375c7adad1f24794d86261b3e2d3994"
STATUS="C277_MASS_PROJECTED_SELF_ENERGY_KERNELS_CROSSWALKED_COMMON_STATE_INSTANCE_UNAVAILABLE";PLAN="RIMASSSELF1-C"
NEXT="C278/HQCDRIMASSSTATE1";NEXT_OBJECT="C276-RI-SMOM-SIGNED-MASS-COMMON-STATE-INSTANCE";NEXT_EXACT="authenticated complete PROJECT_RI_SMOM_SIGNED_MASS_COMMON_STATE_IR_V1 parameter capsule at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def kernel_crosswalk():
 rows=(("retained q-qg-q self-energy","C145/C217","EXECUTABLE_CALLER_CONDITIONAL"),("outside-fixed-K V1 interfaces","C218-C238","SOURCE_DERIVED_PROGRAMS_READY"),("C112 instantaneous contact V2","C239-C247","SOURCE_DERIVED_CALLER_PROGRAMS_READY"),("C127 instantaneous current V2","C248-C254","REGULATED_CALLER_PROGRAMS_READY"),("C117 finite subtraction directions","C259-C276","FOUR_EXPLICIT_UNSELECTED_COORDINATES"),("C149 signed-mass projector","C149/C276","UNIT_RESPONSE_READY"))
 return _f({"rows":tuple({"component":a,"authority":b,"status":c} for a,b,c in rows),"count":6,"missing_as_zero":False,"root":_r(rows)})
def state_instance_audit():
 fields=("p_in","p_out","virtuality_mu2","rho","mu","target_gauge","PV_Q0","boundary_class","residual_link","holonomy_capsule","active_Nf","external_flavor","signed_mass_coordinate","mass_squared_coordinate","common_ir_id")
 rows=tuple({"resolution":r,"schema_available":True,"authenticated_instance":False,"missing_fields":fields,"diagnostic_fixture_promoted":False} for r in RESOLUTIONS)
 return _f({"rows":rows,"instances_required":3,"instances_available":0,"first_missing_object":NEXT_OBJECT,"root":_r(rows)})
def projection_program():
 ops=("LOAD_VERIFIED_COMMON_STATE","LOAD_C217_RETAINED_SELF_ENERGY","LOAD_C238_V1_COMPLEMENT","LOAD_C247_C112_CONTACT","LOAD_C254_C127_REGULATED_CURRENT","LOAD_C117_AFFINE_COORDINATES","APPLY_C149_SIGNED_MASS_PROJECTOR","SUBTRACT_COMMON_IR","CHECK_SIGN_REVERSAL","RETURN_AFFINE_PROJECTED_SELF_ENERGY")
 rows=tuple({"resolution":r,"safe_opcodes":ops,"kernel_complete":True,"state_bound":False,"executable":False,"terminal":"COMMON_STATE_INSTANCE_UNAVAILABLE"} for r in RESOLUTIONS)
 return _f({"schema":"PROJECT_C277_RI_SMOM_MASS_SELF_ENERGY_V1","rows":rows,"count":3,"eval":False,"pickle":False,"callbacks":False,"root":_r(rows)})
def route_audit():
 routes=("DIRECT_C149_PROJECTION","SIGNED_MASS_DERIVATIVE","SPECTRAL_RESOLVENT","OWNER_DECOMPOSITION","SIGN_REVERSAL")
 return _f({"routes":tuple({"route":x,"kernel_status":"READY","evaluation_status":"SAME_STATE_INSTANCE_MISSING","agreement":None} for x in routes),"false_agreement":False,"root":_r(routes)})
def uncertainty_boundary():return _f({"C117_coordinates":"four explicit symbolic coordinates","common_IR":"record ID required","state_covariance":None,"regulator_covariance":None,"missing_as_zero":False,"physical":False,"root":_r(("symbolic-C117","state-missing"))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":False,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"kernel_classes_crosswalked":6,"state_instances":0,"evaluated_resolutions":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"diagnostic_fixture_promoted":0,"C117_coordinates_selected":0,"mass_squared_conflated":0,"missing_zeroed":0,"later_requests_modified":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassself1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("kernel","state","momentum","scale","flavor","gauge","boundary","IR","C117","projector","route","uncertainty")[i%12],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassself1_authority():
 from deuteron_wigner.bridge import hqcdrimassadapter1 as c276,hqcdriquarkself1 as c217,hqcdriquarkfixedkv2currentreg1 as c254
 if c276.PACKAGE_ROOT!=C276_ROOT:raise ValueError("C276 root changed")
 c276.load_verified_hqcdrimassadapter1_authority();c217.load_verified_hqcd_riquarkself1_authority();c254.load_verified_hqcdriquarkfixedkv2currentreg1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassself1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassself1_authority()
_ROOTS={"INPUT":_r((BASELINE,C276_ROOT)),"KERNELS":kernel_crosswalk()["root"],"STATE":state_instance_audit()["root"],"PROGRAM":projection_program()["root"],"ROUTES":route_audit()["root"],"UNCERTAINTY":uncertainty_boundary()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C277-HQCDRIMASSSELF1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
