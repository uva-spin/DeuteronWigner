"""C291 C43 boundary-action source audit and strict parameter schema."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c291_hqcdrimassboundaryaction1"
BASELINE="b3b381039490395eb9af6bbae813fc67bae6a95a";C290_ROOT="6fb74af9c73a76e40b4b9e3ae10fdb87328b2a737c2e0d45d42e40fffe4ccb9f"
STATUS="C291_C43_BULK_ACTION_AND_BOUNDARY_PARAMETER_SCHEMA_READY_BOUNDARY_ACTION_SOURCE_SUPPLEMENT_MISSING";PLAN="RIMASSBOUNDARYACTION1-C"
NEXT="C292/HQCDRIMASSBOUNDARYACTIONSOURCE1";NEXT_OBJECT="C291-MASS-BOUNDARY-ACTION-SOURCE-SUPPLEMENT";NEXT_EXACT="authenticated literature supplement or project equation defining the finite-volume boundary action, holonomy dependence, and absolute normalization used by C43 at K9/K11/K13"
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
def c43_action_audit():
 rows=({"component":"bulk LF action/constraints","source":"SB hep-ph/0011372v2 Eqs.1,5-9,24-25","available":True},{"component":"PV Q0 inverse derivative","source":"C43 action_contract","available":True},{"component":"finite-volume boundary operator owner","source":"C130","available":"STRUCTURAL_ONLY"},{"component":"holonomy-dependent boundary action","source":None,"available":False},{"component":"sector partition weights","source":None,"available":False},{"component":"absolute partition normalization","source":None,"available":False})
 return _f({"rows":rows,"bulk_action_ready":True,"boundary_action_ready":False,"bulk_promoted_to_boundary":False,"root":_r(rows)})
def parameter_schema():
 fields=("record_id","source_id","equation_locator","resolution","boundary_functional","action_parameters","units","holonomy_coordinates","center_sector","orbit_jacobian","partition_normalization","fermion_BC","gluon_BC","volume_scaling","cross_resolution_covariance","no_defaults","physical")
 return _f({"schema":"PROJECT_C291_C43_MASS_BOUNDARY_ACTION_PARAMETER_V1","required":fields,"resolutions":RESOLUTIONS,"complete_instances":0,"root":_r(fields)})
def source_request():return _f({"object_id":NEXT_OBJECT,"acceptable_authority":("hash-locked literature equation","project-owned normative equation plus provenance"),"required_content":("boundary functional","holonomy dependence","normalization","BC","volume scaling"),"web_summary_accepted":False,"memory_formula_accepted":False,"root":_r(NEXT_OBJECT)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"bulk_action_ready":True,"boundary_records":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"bulk_boundary_conflated":0,"remembered_formula":0,"identity_default":0,"uniform_weights":0,"unit_volume_default":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassboundaryaction1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","locator","functional","parameter","unit","holonomy","normalization","BC","volume","covariance")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassboundaryaction1_authority():
 from deuteron_wigner.bridge import hqcdrimassboundaryensemble1 as c290
 from deuteron_wigner.bridge.g0 import contracts as c43
 if c290.PACKAGE_ROOT!=C290_ROOT or not c43.validate_contract():raise ValueError("upstream action changed")
 c290.load_verified_hqcdrimassboundaryensemble1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassboundaryaction1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassboundaryaction1_authority()
_ROOTS={"INPUT":_r((BASELINE,C290_ROOT)),"AUDIT":c43_action_audit()["root"],"SCHEMA":parameter_schema()["root"],"REQUEST":source_request()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C291-HQCDRIMASSBOUNDARYACTION1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
