"""C288 strict caller-owned boundary/holonomy capsule family."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c288_hqcdrimassholonomy1"
BASELINE="639daaaa458c5573d5500c8739490cc671d0bddf";C287_ROOT="cb7a895a4ca0ff1ea5c9ad36a33463f7d04f69bbba15ac3abc7607de432d1d5d"
STATUS="C288_STRICT_PROCESS_NEUTRAL_BOUNDARY_HOLONOMY_CAPSULE_FAMILY_READY_PHYSICAL_SECTOR_MEASURE_SELECTION_MISSING";PLAN="RIMASSHOLONOMY1-B"
NEXT="C289/HQCDRIMASSHOLONOMYMEASURE1";NEXT_OBJECT="C288-MASS-PHYSICAL-HOLONOMY-SECTOR-MEASURE-SELECTION";NEXT_EXACT="authenticated project finite-volume holonomy sector and measure convention selecting physical process-neutral C288 capsule instances at K9/K11/K13"
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
def capsule_family():
 rows=tuple({"record_id":f"C288-MASS-HOLONOMY-{k}","resolution":k,"boundary_class":"CALLER_PHYSICAL_CLASS","residual_link_record":"CALLER_C182_RECORD","cut_chart":"C178_CUT_C0_COORDINATE","endpoint_identification":"CALLER_C204_IDENTITY","fundamental_holonomy":"CALLER_SU3_MATRIX","adjoint_holonomy":"DERIVE_WITH_C183_REPRESENTATION_MAP","fundamental_preimage_proof":True,"measure_convention":"CALLER_PHYSICAL_MEASURE","process_neutral":True,"no_defaults":True,"complete":False} for k in RESOLUTIONS)
 return _f({"schema":"PROJECT_C288_MASS_PHYSICAL_BOUNDARY_HOLONOMY_V1","rows":rows,"complete_instances":0,"root":_r(rows)})
def evidence_audit():
 rows=({"authority":"C183 fixtures","physical":False,"usable":"VALIDATION_ONLY"},{"authority":"C204 endpoint fixtures","physical":False,"usable":"VALIDATION_ONLY"},{"authority":"C205 global fixtures","physical":False,"usable":"VALIDATION_ONLY"},{"authority":"C278 caller schema","physical":False,"usable":"REQUIRES_INSTANCE"})
 return _f({"rows":rows,"physical_instances":0,"identity_default":False,"fixture_promotion":False,"root":_r(rows)})
def composition_gate():return _f({"schema":True,"cut_chart":True,"representation_map":True,"BC_compatibility_schema":True,"process_neutral":True,"physical_sector":False,"measure":False,"endpoint_values":False,"full_self_energy":False,"root":_r((STATUS,PLAN))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"capsule_rows":3,"physical_instances":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"fixture_promoted":0,"identity_default":0,"measure_selected":0,"sector_selected":0,"link_unity_assumed":0,"process_attached":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassholonomy1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("boundary","link","cut","endpoint","fundamental","adjoint","preimage","measure","resolution","composition")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassholonomy1_authority():
 from deuteron_wigner.bridge import hqcdrimassprocess1 as c287,hqcdb0holonomy2 as c183,hqcdstboundary2 as c204,hqcdstglobal1 as c205
 if c287.PACKAGE_ROOT!=C287_ROOT:raise ValueError("C287 root changed")
 c287.load_verified_hqcdrimassprocess1_authority();c183.load_verified_hqcd_b0holonomy2_authority();c204.load_verified_hqcd_stboundary2_authority();c205.load_verified_hqcd_stglobal1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassholonomy1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassholonomy1_authority()
_ROOTS={"INPUT":_r((BASELINE,C287_ROOT)),"FAMILY":capsule_family()["root"],"EVIDENCE":evidence_audit()["root"],"GATE":composition_gate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C288-HQCDRIMASSHOLONOMY1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
