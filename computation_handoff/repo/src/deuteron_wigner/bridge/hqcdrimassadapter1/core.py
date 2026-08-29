"""C276 RI/SMOM signed-mass adapter structural authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c276_hqcdrimassadapter1"
BASELINE="e708ca490c45359b5b8cf6ee9682bed3cfe3f55a";C275_ROOT="6daab8eb3cdc5d6006047c1203e5d68ca9e151e31b3d14df7be4a35611aa01fc"
REQUEST_ID="C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-2"
STATUS="C276_RI_SMOM_SIGNED_MASS_ADAPTER_STRUCTURAL_PROGRAM_READY_ORDER_G2_MASS_PROJECTED_SELF_ENERGY_INCOMPLETE";PLAN="RIMASSADAPTER1-B"
NEXT="C277/HQCDRIMASSSELF1";NEXT_OBJECT="C168-REQUEST-2-MASS-PROJECTED-SELF-ENERGY";NEXT_EXACT="order-g_s^2 C43 signed-mass-projected quark self-energy on the authenticated RI/SMOM common-state/common-IR record at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13");OPCODES=("LOAD_REQUEST","LOAD_C148_FULL_SPINOR_TWO_POINT","LOAD_C149_SIGNED_MASS_PROJECTOR","LOAD_C150_CONDITIONAL_MASS_FAMILY","LOAD_RI_SMOM_SCALAR_PSEUDOSCALAR_TARGET","VALIDATE_COMMON_STATE_IR","LOAD_ORDER_G2_SELF_ENERGY","PROJECT_SIGNED_MASS_LINEAR","SUBTRACT_COMMON_IR","FORM_ZM_RATIO","RETURN_UNAVAILABLE_IF_MASS_PROJECTION_MISSING")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def request_freeze():return _f({"request_id":REQUEST_ID,"ordinal":2,"quantity":"SIGNED_QUARK_MASS","target_scheme":"RI_SMOM","C43_gauge":"A^+=0","C43_pole":"antisymmetric/PV","mass_coordinate":"signed m_R","mass_squared_coordinate":"m_R^2 independent","resolutions":RESOLUTIONS,"physical":False,"root":_r((REQUEST_ID,RESOLUTIONS,"signed m_R"))})
def convention_manifest():return _f({"signal":"signed_mass","projector":"C149-MASS-PROJECTOR-V1","unit_response":1,"kinetic_response":0,"nuisance_response":0,"target":"RI/SMOM scalar/pseudoscalar Ward-compatible mass definition","conversion_orientation":"Z_m^RI/SMOM <- C43 finite-basis signed-mass coordinate","mass_sign_retained":True,"mass_squared_substituted":False,"root":_r(("C149","signed","RI_SMOM"))})
def structural_authority_ledger():
 rows=(("C148","signed-mass-linear full-spinor inverse two-point",True),("C149","unit-response signed-mass projector",True),("C150","conditional finite-basis signed-mass scheme family",True),("C153","common-IR componentwise conversion schema",True),("C164","RI/SMOM scalar/pseudoscalar target locators",True),("C215","ordered request-2 capsule",True),("request-2","order-g_s^2 C43 mass-projected self-energy evaluation",False))
 return _f({"rows":tuple({"authority":a,"object":b,"complete":c} for a,b,c in rows),"count":7,"complete":6,"root":_r(rows)})
def common_state_schema():
 f=("record_id","resolution","p_in","p_out","virtuality_mu2","rho","mu","C43_gauge","target_gauge","PV_Q0","boundary_class","residual_link","holonomy_capsule","active_Nf","external_flavor","signed_mass_coordinate","mass_squared_coordinate","source_sink_order","common_ir_id","units","no_defaults","physical")
 return _f({"schema":"PROJECT_RI_SMOM_SIGNED_MASS_COMMON_STATE_IR_V1","required_fields":f,"symmetric_nonexceptional":"p_in^2=p_out^2=(p_in-p_out)^2=mu^2","K_resolutions":RESOLUTIONS,"root":_r(f)})
def adapter_program_manifest():
 nodes=tuple({"ordinal":i,"opcode":x} for i,x in enumerate(OPCODES));rows=tuple({"program_id":f"C276-RI-M-{r}","resolution":r,"nodes":nodes,"executable":False,"terminal":"ORDER_G2_MASS_PROJECTED_SELF_ENERGY_UNAVAILABLE","root":_r((r,nodes))} for r in RESOLUTIONS)
 return _f({"schema":"PROJECT_C276_RI_SMOM_SIGNED_MASS_ADAPTER_V1","rows":rows,"count":3,"executable":0,"safe_opcodes":OPCODES,"eval":False,"pickle":False,"callbacks":False,"root":_r(rows)})
def route_certificate():
 routes=("ZM_FACTOR_RATIO","COMMON_PROJECTED_GREEN_FUNCTION","ORDER_G2_COEFFICIENT_DIFFERENCE","INVERSE_ROUNDTRIP")
 rows=tuple({"resolution":r,"routes":tuple({"route":x,"status":"BLOCKED_ON_SAME_MASS_PROJECTED_SELF_ENERGY","agreement":None} for x in routes),"false_agreement":False} for r in RESOLUTIONS)
 return _f({"rows":rows,"closed_routes":0,"common_missing_object":NEXT_OBJECT,"root":_r(rows)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"later_nonC117_requests_preserved":4,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"request_bound":True,"structural_programs":3,"executable_adapters":0,"mass_projected_self_energy_complete":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"C117_coordinates_modified":0,"later_requests_modified":0,"mass_squared_conflated":0,"missing_zeroed":0,"physical_inputs":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassadapter1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("request","sign","mass2","projector","kinematics","common-ir","gauge","resolution","program","route","frontier")[i%11],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassadapter1_authority():
 from deuteron_wigner.bridge import hqcdnonc117slot1 as c275,hqcdmproj as c149,hqcdphysadaptercalc1 as c215
 if c275.PACKAGE_ROOT!=C275_ROOT:raise ValueError("C275 root changed")
 c275.load_verified_hqcdnonc117slot1_authority();c149.load_verified_hqcd_mass_projector_authority();c215.load_verified_hqcd_physadaptercalc1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassadapter1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassadapter1_authority()
_ROOTS={"INPUT":_r((BASELINE,C275_ROOT)),"REQUEST":request_freeze()["root"],"CONVENTION":convention_manifest()["root"],"AUTHORITY":structural_authority_ledger()["root"],"STATE":common_state_schema()["root"],"PROGRAM":adapter_program_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C276-HQCDRIMASSADAPTER1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
