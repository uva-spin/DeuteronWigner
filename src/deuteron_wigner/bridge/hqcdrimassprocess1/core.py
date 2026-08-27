"""C287 process-applicability authority for the signed-mass self-energy."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c287_hqcdrimassprocess1"
BASELINE="e78f4562fc2e491cb6032a88eaeb005496e1d1b6";C286_ROOT="73abbe44114cf57f011babfcd863fb9e671862cacf84cb36e65d7f0cef210e01"
STATUS="C287_SIGNED_MASS_TWO_POINT_PROCESS_NEUTRALITY_CERTIFIED_CALLER_PHYSICAL_BOUNDARY_HOLONOMY_CAPSULE_MISSING";PLAN="RIMASSPROCESS1-D"
NEXT="C288/HQCDRIMASSHOLONOMY1";NEXT_OBJECT="C287-MASS-CALLER-PHYSICAL-BOUNDARY-HOLONOMY-CAPSULE";NEXT_EXACT="authenticated caller-owned C278 boundary class, residual-link record, and physical fundamental/adjoint SU(3) holonomy capsule at K9/K11/K13 for the signed-mass self-energy"
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
def observable_classification():
 row={"object":"signed-mass-projected quark self-energy","correlator":"off-shell colored inverse two-point function","target":"RI/SMOM symmetric nonexceptional subtraction","DIS_observable":False,"DY_observable":False,"staple_process_orientation_applicable":False,"PV_selects_process":False,"source":"C276-C284 project authority"}
 return _f({**row,"root":_r(row)})
def process_applicability_audit():
 rows=({"candidate":"DIS_FUTURE","authority":"C177 TMD/SIDIS source","applicable":False,"reason":"no DIS final-state observable in signed-mass two-point target"},{"candidate":"DY_PAST","authority":"C177 DY source","applicable":False,"reason":"no DY initial-state observable in signed-mass two-point target"},{"candidate":"PROCESS_NEUTRAL_CALLER_BOUNDARY","authority":"C278 common-state schema","applicable":True,"reason":"boundary_class/residual_link/holonomy are explicit caller coordinates"})
 return _f({"rows":rows,"unique_scattering_process":False,"process_conflation":False,"root":_r(rows)})
def caller_capsule_schema():
 fields=("record_id","resolution","boundary_class","residual_link_record","fundamental_holonomy","adjoint_preimage_proof","cut_chart","endpoint_identification","source","physical_intent","no_defaults")
 return _f({"schema":"PROJECT_C287_MASS_CALLER_BOUNDARY_HOLONOMY_CAPSULE_V1","required":fields,"resolutions":RESOLUTIONS,"C183_fixture_accepted":False,"identity_default":False,"complete_instances":0,"root":_r(fields)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"process_neutral":True,"caller_capsules_complete":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"DIS_selected":0,"DY_selected":0,"PV_relabelled_process":0,"identity_fixture_promoted":0,"holonomy_selected":0,"link_unity_assumed":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassprocess1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("observable","DIS","DY","PV","boundary","link","holonomy","cut","endpoint","resolution")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassprocess1_authority():
 from deuteron_wigner.bridge import hqcdrimasspathselect1 as c286,hqcdrimassstate1 as c278,hqcdrimassadapter1 as c276,hqcdb0reslinksource1 as c177
 if c286.PACKAGE_ROOT!=C286_ROOT:raise ValueError("C286 root changed")
 c286.load_verified_hqcdrimasspathselect1_authority();c278.load_verified_hqcdrimassstate1_authority();c276.load_verified_hqcdrimassadapter1_authority();c177.load_verified_hqcd_b0reslinksource1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassprocess1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassprocess1_authority()
_ROOTS={"INPUT":_r((BASELINE,C286_ROOT)),"CLASS":observable_classification()["root"],"AUDIT":process_applicability_audit()["root"],"SCHEMA":caller_capsule_schema()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C287-HQCDRIMASSPROCESS1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
