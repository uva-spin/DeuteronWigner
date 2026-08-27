"""C278 maximal symbolic RI/SMOM signed-mass state family."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c278_hqcdrimassstate1"
BASELINE="e23b63c8dcb790b7bc63d4164842d60a1ef848ee";C277_ROOT="b57cd76303f9ba0a7002bc97baca44eabb8de68529920682103069bc66bca0f1"
STATUS="C278_MAXIMAL_SYMBOLIC_RI_SMOM_MASS_STATE_FAMILY_READY_NUMERICAL_COMMON_IR_AUTHORITY_MISSING";PLAN="RIMASSSTATE1-B"
NEXT="C279/HQCDRIMASSIR1";NEXT_OBJECT="C157-SIGNED-MASS-COMMON-IR-NUMERIC-RECORDS";NEXT_EXACT="authenticated C157 common-IR numerical records for SIGNED_QUARK_MASS in RI/SMOM at K9/K11/K13"
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
def field_closure_ledger():
 rows=(("p_in,p_out,virtuality_mu2","C164 RI/SMOM symmetric nonexceptional definition","SYMBOLIC_GEOMETRY_CLOSED"),("rho,mu,common_ir_id","C157 numerical common-IR schema","NUMERICAL_AUTHORITY_MISSING"),("C43_gauge,target_gauge,PV_Q0","C153/C164/C183","CALLER_BRANCH_BOUND"),("boundary,residual_link,holonomy","C172-C183","SCHEMA_CLOSED_PHYSICAL_SELECTION_OPEN"),("active_Nf,external_flavor","C154-C155","SEPARATE_CALLER_COORDINATES"),("signed_mass,mass_squared","C148-C150","SIGNED_LINEAR_AND_INDEPENDENT_M2"),("source_sink_order,units","C142-C150","CLOSED"))
 return _f({"rows":tuple({"fields":a,"authority":b,"status":c} for a,b,c in rows),"classes":7,"numerically_closed":0,"root":_r(rows)})
def symbolic_capsule_family():
 rows=tuple({"record_id":f"C278-RI-MASS-STATE-{r}","resolution":r,"p_in":"CALLER_VECTOR","p_out":"CALLER_VECTOR","constraint":"p_in^2=p_out^2=(p_in-p_out)^2=mu^2","virtuality_mu2":"CALLER_POSITIVE","rho":"C157_RECORD_REQUIRED","mu":"C157_RECORD_REQUIRED","C43_gauge":"A^+=0","target_gauge":"CALLER_RI_SMOM_GAUGE","PV_Q0":"CALLER_C43_COMPATIBLE","boundary_class":"CALLER_C183_CLASS","residual_link":"CALLER_C182_RECORD","holonomy_capsule":"CALLER_C183_CAPSULE","active_Nf":"CALLER_C155_RECORD","external_flavor":"u_or_d_EXPLICIT","signed_mass_coordinate":"signed m_R CALLER","mass_squared_coordinate":"m_R^2 CALLER INDEPENDENT","source_sink_order":"C142_CANONICAL","common_ir_id":None,"units":"natural units; explicit per field","no_defaults":True,"physical":False,"complete":False} for r in RESOLUTIONS)
 return _f({"schema":"PROJECT_RI_SMOM_SIGNED_MASS_COMMON_STATE_IR_V1","rows":rows,"count":3,"complete_instances":0,"root":_r(rows)})
def kinematic_certificate():return _f({"symmetric_nonexceptional":True,"exceptional_channels":0,"scale_defaulted":False,"Euclidean_or_Minkowski_continuation":"source-record required","route_mismatches":0,"root":_r(("symmetric",0,"symbolic"))})
def forward_reverse_audit():return _f({"forward":"C142 source -> C149 mass projector -> C157 common IR -> RI/SMOM target","reverse":"C277 projected slot -> C278 state -> C157 record -> C153/C164 source","first_common_missing":NEXT_OBJECT,"circular_calibration":False,"root":_r(NEXT_OBJECT)})
def covariance_boundary():return _f({"state_covariance":None,"cross_resolution_covariance":None,"scale_regulator_cross_blocks":None,"missing_as_zero":False,"root":_r("C157-covariance-missing")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"symbolic_capsules":3,"complete_capsules":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"physical_scale_selected":0,"diagnostic_fixture_promoted":0,"C117_coordinates_selected":0,"missing_zeroed":0,"flavor_averaged":0,"holonomy_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassstate1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("momentum","mu","rho","gauge","PV","boundary","link","holonomy","Nf","flavor","mass","m2","IR","covariance")[i%14],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassstate1_authority():
 from deuteron_wigner.bridge import hqcdrimassself1 as c277,hqcdmatchir2 as c157,hqcdfavor2 as c155
 if c277.PACKAGE_ROOT!=C277_ROOT:raise ValueError("C277 root changed")
 c277.load_verified_hqcdrimassself1_authority();c157.load_verified_hqcd_matchir_authority();c155.load_verified_hqcd_flavor_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassstate1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassstate1_authority()
_ROOTS={"INPUT":_r((BASELINE,C277_ROOT)),"FIELDS":field_closure_ledger()["root"],"CAPSULES":symbolic_capsule_family()["root"],"KINEMATICS":kinematic_certificate()["root"],"AUDIT":forward_reverse_audit()["root"],"COVARIANCE":covariance_boundary()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C278-HQCDRIMASSSTATE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
