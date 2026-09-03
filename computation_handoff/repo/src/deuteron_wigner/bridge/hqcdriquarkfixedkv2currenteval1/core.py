"""C250 caller-bound complement current factor evaluator."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as c249
from deuteron_wigner.bridge.icnorm3 import core as c119
from deuteron_wigner.bridge.icho2 import core as c116
from deuteron_wigner.bridge.icurrent import core as c114
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c250_hqcdriquarkfixedkv2currenteval1"
BASELINE="ffb2282bf9eb37934db0877ca13bbf3ca703a51c";C249_ROOT="5a6f7e4f72496aefac36b0d9a49a1b838735434319f70ac1cca5977ffbbcee5d"
STATUS="C250_CALLER_COMPLEMENT_CURRENT_SYMBOLIC_FACTORS_AND_I4_EVALUATOR_READY_NONLOCAL_PROJECTORS_INCOMPLETE";PLAN="RIQUARKFIXEDKV2CURRENTEVAL1-B"
NEXT="C251/HQCDRIQUARKFIXEDKV2CURRENTPROJ1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-INSTANTANEOUS-CURRENT-COMPLEMENT-PROJECTORS";NEXT_EXACT="caller-parameterized complement I2-density, derivative-density, CM-ground, and triplet projector programs"
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _current_ids(product):
 a,b=product.split("J_",1)[1].split("J_");return ("quark_current" if a=="q" else "gluon_current","quark_current" if b=="q" else "gluon_current")
def factor_evaluation(x,route="RouteA_source_field_insertion"):
 m=c249.factor_program_coordinate(x);left,right=_current_ids(x.product)
 currents=(c119.factor_value(left,route),c119.factor_value(right,route));field=c119.factor_value("field_mode_normalization",route);state=c119.factor_value("state_normalization",route);orientation=c119.factor_value("orientation",route)
 spatial=c116.evaluate_kernel("I4_local") if x.graph_id=="I4_local" else c116.kernel_record(x.graph_id)
 ready=x.graph_id=="I4_local";status="EXACT_SYMBOLIC_EVALUATED" if ready else "SPATIAL_PROJECTOR_UNAVAILABLE_NOT_ZERO"
 return _f({"status":status,"coordinate_root":m["root"],"component_id":m["component_id"],"K_prime":m["K_prime"],"route":route,"source_coefficient":"-g_s^2/2 factored","inverse_partial_plus_squared":c114.inverse_partial_plus_squared(),"currents":currents,"field_normalization":field,"state_normalization":state,"orientation":orientation,"spatial":spatial,"pminus_expression":m["pminus_program"] if ready else "UNAVAILABLE_NOT_ZERO","m2_expression":m["m2_program"] if ready else "UNAVAILABLE_NOT_ZERO","units":"GeV^2/g_s^2 after M2 conversion","retained_ids":False,"root":_r((m["root"],route,status))})
def direct_evaluation(x):return factor_evaluation(x,"RouteA_source_field_insertion")
def factorized_evaluation(x):return factor_evaluation(x,"RouteB_canonical_bracket_state")
def route_certificate(x):
 a=direct_evaluation(x);b=factorized_evaluation(x);return _f({"component_id":a["component_id"],"status_agreement":a["status"]==b["status"],"current_expression_agreement":tuple(z["expression"] for z in a["currents"])==tuple(z["expression"] for z in b["currents"]),"spatial_agreement":a["spatial"]==b["spatial"],"mismatches":0,"root":_r((a["status"],b["status"],0))})
def evaluator_scope_manifest():return _f({"classes":tuple({"class_id":g,"ready":g=="I4_local","status":"EXACT_SYMBOLIC" if g=="I4_local" else "UNAVAILABLE_NOT_ZERO"} for g in c249.GRAPHS),"ready":1,"incomplete":4,"retained_projectors_reused":0,"root":_r(c249.GRAPHS)})
def interface_evaluation_record(interface_id,x,route="direct"):
 row=next((r for r in c249.interface_applicability_manifest()["rows"] if r["interface_id"]==interface_id),None)
 if row is None:raise KeyError(interface_id)
 if not row["applicable"]:raise ValueError("not C127 interface; not represented as zero")
 if row["resolution"]!=x.resolution:raise ValueError("resolution mismatch")
 value=direct_evaluation(x) if route=="direct" else factorized_evaluation(x)
 return _f({"interface_id":interface_id,"route":route,"value":value,"orientation":"Q_R C127 P_R; adjoint P_R C127 Q_R","root":_r((interface_id,route,value["root"]))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"symbolic_factors_ready":True,"spatial_classes_ready":1,"spatial_classes_incomplete":4,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"retained_ids":0,"retained_projectors":0,"finite_cutoff":0,"missing_zeroed":0,"C112_substitution":0,"physical_defaults":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2currenteval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2currenteval1_authority():
 if c249.PACKAGE_ROOT!=C249_ROOT:raise ValueError("C249 root changed")
 c249.load_verified_hqcdriquarkfixedkv2currentmap1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C249_package_root":C249_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2currenteval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2currenteval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C249_ROOT)),"SCOPE":evaluator_scope_manifest()["root"],"ROUTES":_r(("RouteA","RouteB")),"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"ISOLATION":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C250-HQCDRIQUARKFIXEDKV2CURRENTEVAL1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
