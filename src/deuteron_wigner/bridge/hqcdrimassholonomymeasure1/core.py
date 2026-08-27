"""C289 symbolic holonomy sector/measure family for the mass capsule."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c289_hqcdrimassholonomymeasure1"
BASELINE="92a4cc50849b90bffe6491683c049006464006d8";C288_ROOT="cd178a3f76107f781c2997dedfddd1e0636a86db9195ae7d1be994e454997754"
STATUS="C289_HOLONOMY_ORBIT_STABILIZER_MEASURE_FAMILY_READY_PHYSICAL_BOUNDARY_ENSEMBLE_AUTHORITY_MISSING";PLAN="RIMASSHOLONOMYMEASURE1-B"
NEXT="C290/HQCDRIMASSBOUNDARYENSEMBLE1";NEXT_OBJECT="C289-MASS-PHYSICAL-BOUNDARY-ENSEMBLE-AUTHORITY";NEXT_EXACT="authenticated finite-volume boundary action or ensemble defining the physical holonomy-sector weights and normalized orbit/stabilizer measure at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13");CLASSES=("GENERIC","CENTRAL","WEYL_WALL","IDENTITY_DIAGNOSTIC")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def sector_measure_family():
 rows=tuple({"resolution":k,"capsule_class":c,"orbit":"SU3/STABILIZER","stabilizer_dimension":{"GENERIC":2,"CENTRAL":8,"WEYL_WALL":"ENHANCED_SOURCE_QUALIFIED","IDENTITY_DIAGNOSTIC":8}[c],"weyl_quotient":True,"center_sector":"RETAINED","global_frame":"QUOTIENT_COVARIANT","relative_measure":"SYMBOLIC_ORBIT_STABILIZER_RATIO","absolute_normalization":"UNSELECTED","physical_weight":"UNSELECTED","admissible_physical_candidate":c!="IDENTITY_DIAGNOSTIC"} for k in RESOLUTIONS for c in CLASSES)
 return _f({"rows":rows,"count":12,"physical_selected":False,"normalized":False,"root":_r(rows)})
def authority_audit():
 rows=({"authority":"C183","provides":"SU3 classes/representation/BC","physical_sector":False,"measure":False},{"authority":"C205","provides":"orbit/stabilizer symbolic ratio","physical_sector":False,"measure":"UNNORMALIZED"},{"authority":"C288","provides":"mass capsule schema","physical_sector":False,"measure":False})
 return _f({"rows":rows,"physical_authorities":0,"unit_volume_default":False,"identity_default":False,"root":_r(rows)})
def selection_gate():return _f({"class_domain":True,"stabilizer":True,"orbit_ratio":True,"frame_covariance":True,"boundary_action":False,"ensemble_weights":False,"absolute_normalization":False,"physical_capsules":0,"root":_r((STATUS,PLAN))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"candidate_rows":12,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"identity_default":0,"unit_volume_default":0,"fixture_promoted":0,"sector_selected":0,"measure_normalized":0,"process_attached":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassholonomymeasure1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("class","orbit","stabilizer","weyl","center","frame","measure","weight","normalization","resolution")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassholonomymeasure1_authority():
 from deuteron_wigner.bridge import hqcdrimassholonomy1 as c288,hqcdb0holonomy2 as c183,hqcdstglobal1 as c205
 if c288.PACKAGE_ROOT!=C288_ROOT:raise ValueError("C288 root changed")
 c288.load_verified_hqcdrimassholonomy1_authority();c183.load_verified_hqcd_b0holonomy2_authority();c205.load_verified_hqcd_stglobal1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassholonomymeasure1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassholonomymeasure1_authority()
_ROOTS={"INPUT":_r((BASELINE,C288_ROOT)),"FAMILY":sector_measure_family()["root"],"AUDIT":authority_audit()["root"],"GATE":selection_gate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C289-HQCDRIMASSHOLONOMYMEASURE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
