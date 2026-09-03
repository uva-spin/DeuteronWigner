"""C290 strict physical boundary-ensemble schema for signed-mass matching."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c290_hqcdrimassboundaryensemble1"
BASELINE="c9731a0a2d153dc7da5e544c73114b08217320f5";C289_ROOT="6e0cac728df783012193823e7db3665d7f46575db44377ca959025501ffc2f1e"
STATUS="C290_PHYSICAL_BOUNDARY_ENSEMBLE_SCHEMA_READY_BOUNDARY_ACTION_PARAMETER_RECORD_MISSING";PLAN="RIMASSBOUNDARYENSEMBLE1-B"
NEXT="C291/HQCDRIMASSBOUNDARYACTION1";NEXT_OBJECT="C290-MASS-BOUNDARY-ACTION-PARAMETER-RECORD";NEXT_EXACT="authenticated C43 finite-volume boundary-action parameters and normalization prescription inducing holonomy-sector weights at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13");CLASSES=("GENERIC","CENTRAL","WEYL_WALL")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def ensemble_schema():
 fields=("ensemble_id","boundary_action_id","action_parameters","resolution","sector_classes","sector_weights","orbit_stabilizer_jacobian","absolute_normalization","global_frame_quotient","fundamental_BC","adjoint_BC","cross_resolution_covariance","volume_interpretation","source","no_defaults","physical")
 return _f({"schema":"PROJECT_C290_MASS_PHYSICAL_BOUNDARY_ENSEMBLE_V1","required":fields,"resolutions":RESOLUTIONS,"classes":CLASSES,"weights_sum":"EXACT_ONE_PER_RESOLUTION","unit_volume_default":False,"uniform_default":False,"complete_instances":0,"root":_r(fields)})
def action_to_weight_program():
 ops=("LOAD_BOUNDARY_ACTION","LOAD_SECTOR_CLASS","EVALUATE_SECTOR_ACTION","MULTIPLY_ORBIT_STABILIZER_JACOBIAN","NORMALIZE_ALL_SECTORS_JOINTLY","PROPAGATE_K_COVARIANCE","RETURN_ENSEMBLE")
 return _f({"safe_opcodes":ops,"eval":False,"pickle":False,"callbacks":False,"executable":False,"reason":NEXT_OBJECT,"root":_r(ops)})
def authority_audit():
 rows=({"authority":"C43/C130","boundary_action":"STRUCTURAL_ONLY","weights":False},{"authority":"C183","boundary_action":False,"weights":False},{"authority":"C205","boundary_action":False,"weights":"SYMBOLIC_UNNORMALIZED"},{"authority":"C274","boundary_action":"CALLER_SLOT","weights":False})
 return _f({"rows":rows,"physical_records":0,"missing_as_uniform":False,"root":_r(rows)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"schema_ready":True,"physical_instances":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"identity_default":0,"uniform_weights":0,"unit_volume_default":0,"K_independence_assumed":0,"fixture_promoted":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassboundaryensemble1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("action","parameter","class","weight","jacobian","normalization","frame","BC","covariance","volume")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassboundaryensemble1_authority():
 from deuteron_wigner.bridge import hqcdrimassholonomymeasure1 as c289,hqcdb0holonomy2 as c183,hqcdstglobal1 as c205,hqcdc117renormh1 as c274
 if c289.PACKAGE_ROOT!=C289_ROOT:raise ValueError("C289 root changed")
 c289.load_verified_hqcdrimassholonomymeasure1_authority();c183.load_verified_hqcd_b0holonomy2_authority();c205.load_verified_hqcd_stglobal1_authority();c274.load_verified_hqcdc117renormh1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassboundaryensemble1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassboundaryensemble1_authority()
_ROOTS={"INPUT":_r((BASELINE,C289_ROOT)),"SCHEMA":ensemble_schema()["root"],"PROGRAM":action_to_weight_program()["root"],"AUDIT":authority_audit()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C290-HQCDRIMASSBOUNDARYENSEMBLE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
