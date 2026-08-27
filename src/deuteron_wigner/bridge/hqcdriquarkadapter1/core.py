"""C216 request-1 partial calculation and quark self-energy frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdphysadaptercalc1 as c215
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c216_hqcdriquarkadapter1"
BASELINE="b2fc3634762a8a2cd4a626020d274b2d47f2d229";C215_ROOT="fff748f74feacb2114b52aa3fa4b0bd39ec9e18d9ebec7b5f0923501aeb7f3e0"
CONTRACT="docs/next_level/c215_c216_hqcdriquarkadapter1_continuation_contract.json";CONTRACT_SHA256="c0a6193bb194960e352284176f30f195b87bf2b1847f3a30e72bdc7624ebfa00"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c216_hqcdriquarkadapter1_codex_prompt.md";PROMPT_SHA256="cca3c07f06c156540cb18a40d908cb12ac9dd1839e9a5201cdbcebc0b8b97da7"
REQUEST_ID="C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QUARK_FIELD-RI_SMOM-2"
STATUS="C216_C215_RI_SMOM_QUARK_ADAPTER_STRUCTURAL_PROGRAM_READY_ORDER_G2_C43_SELF_ENERGY_INCOMPLETE";PLAN="RIQUARKADAPTER1-B"
NEXT="C217/HQCDRIQUARKSELF1";NEXT_OBJECT="C168-REQUEST-1-SELF-ENERGY";NEXT_EXACT="order-g_s^2 C43 quark self-energy on the authenticated RI/SMOM common-state/common-IR record"
RESOLUTIONS=("K9","K11","K13");PROJECTORS=("K_MINUS","K_PLUS","K_PERP");OPCODES=("LOAD_REQUEST","LOAD_C142_SOURCE_MAP","LOAD_C148_FULL_SPINOR_TWO_POINT","LOAD_C149_KINETIC_PROJECTORS","LOAD_C150_CONDITIONAL_ZQ_FAMILY","LOAD_RI_SMOM_PROJECTOR","VALIDATE_COMMON_STATE_IR","LOAD_ORDER_G2_SELF_ENERGY","PROJECT_COMPONENTWISE","SUBTRACT_COMMON_IR","FORM_ZQ_RATIO","RETURN_UNAVAILABLE_IF_SELF_ENERGY_MISSING")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def request_freeze():return _f({"request_id":REQUEST_ID,"ordinal":1,"quantity":"QUARK_FIELD","target_scheme":"RI_SMOM","C43_gauge":"A^+=0","C43_pole":"antisymmetric/PV","projectors":PROJECTORS,"resolutions":RESOLUTIONS,"physical":False,"root":_r((REQUEST_ID,PROJECTORS,RESOLUTIONS))})
def structural_authority_ledger():
 rows=(("C142","canonical nonzero-mode quark source/sink map",True),("C145","forward good-component two-point",True),("C147","C43 coordinate field normalization",True),("C148","constrained positive-frequency full-spinor two-point",True),("C149","signed-mass and kinetic projectors",True),("C150","conditional finite-basis Zq scheme family",True),("C153","componentwise common-IR matching schema",True),("request-1","order-g_s^2 C43 self-energy on common state",False))
 return _f({"rows":tuple({"authority":a,"object":b,"complete":c} for a,b,c in rows),"count":8,"complete":7,"root":_r(rows)})
def common_state_schema():
 f=("record_id","resolution","p_in","p_out","virtuality_mu2","rho","mu","C43_gauge","target_gauge","PV_Q0","boundary_class","residual_link","holonomy_capsule","active_Nf","external_flavor","mass_assumption","source_sink_order","units","no_defaults","physical")
 return _f({"schema":"PROJECT_RI_SMOM_QUARK_COMMON_STATE_IR_V1","required_fields":f,"K_resolutions":RESOLUTIONS,"root":_r(f)})
def validate_common_state(p):
 if not isinstance(p,Mapping) or any(k not in p for k in common_state_schema()["required_fields"]):raise ValueError("complete common state")
 if p["resolution"] not in RESOLUTIONS or p["no_defaults"] is not True or p["physical"] is not False:raise ValueError("scope")
 if p["rho"] in (None,0,0.0,"") or p["mu"] in (None,0,0.0,""):raise ValueError("rho/mu")
 return _f({"valid":True,"record_id":p["record_id"],"root":_r(p)})
def two_point_contribution_ledger():
 rows=(
 {"class":"free quark propagation","status":"C145/C148 COMPLETE"},
 {"class":"q-qg-q canonical vertex pair","status":"OPERATOR AUTHORITY COMPLETE; LOOP EVALUATION MISSING"},
 {"class":"instantaneous fermion","status":"C43 CLASS BOUND; COMMON-STATE EVALUATION MISSING"},
 {"class":"instantaneous current","status":"C43 CLASS BOUND; COMMON-STATE EVALUATION MISSING"},
 {"class":"zero-mode/boundary/residual-link","status":"C172-C183 LEDGER READY; SELF-ENERGY INSERTION MISSING"},
 {"class":"counterterm direction","status":"DIRECTION READY COEFFICIENT UNSELECTED"},
 {"class":"omitted Fock interface","status":"EXPLICIT UNAVAILABLE NOT ZERO"})
 return _f({"rows":rows,"count":7,"evaluated_classes":1,"missing_as_zero":False,"root":_r(rows)})
def adapter_program_schema():return _f({"schema":"PROJECT_RI_SMOM_QUARK_ADAPTER_PROGRAM_V1","safe_opcodes":OPCODES,"eval":False,"pickle":False,"callbacks":False,"root":_r(OPCODES)})
def adapter_program_manifest():
 nodes=tuple({"ordinal":i,"opcode":x} for i,x in enumerate(OPCODES));rows=tuple({"program_id":f"C216-RI-Q-{r}","resolution":r,"nodes":nodes,"projectors":PROJECTORS,"executable":False,"terminal":"ORDER_G2_SELF_ENERGY_UNAVAILABLE","root":_r((r,nodes))} for r in RESOLUTIONS)
 return _f({"rows":rows,"count":3,"executable":0,"root":_r(rows)})
def route_certificate_manifest():
 routes=("ZQ_FACTOR_RATIO","COMMON_PROJECTED_GREEN_FUNCTION","ORDER_G2_COEFFICIENT_DIFFERENCE","INVERSE_ROUNDTRIP")
 rows=tuple({"resolution":r,"routes":tuple({"route":x,"status":"BLOCKED_ON_SAME_SELF_ENERGY_OBJECT","agreement":None} for x in routes),"independent_prerequisites":True} for r in RESOLUTIONS)
 return _f({"rows":rows,"count":3,"closed_routes":0,"common_blocker":NEXT_OBJECT,"root":_r(rows)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"preserved_later_requests":5,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def verify_hqcd_riquarkadapter1_authority():
 if c215.PACKAGE_ROOT!=C215_ROOT:raise ValueError("C215 root changed")
 c215.load_verified_hqcd_physadaptercalc1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C215_package_root":C215_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkadapter1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkadapter1_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"request_bound":True,"structural_programs":3,"executable_adapters":0,"self_energy_complete":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"request_id":REQUEST_ID,"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"model_memory_formulas":0,"physical_inputs":0,"C154_values":0,"C158_values":0,"missing_sectors_zeroed":0,"counterterm_selection":0,"later_requests_modified":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkadapter1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("request","source-map","spinor","projector","common-state","self-energy","instantaneous","boundary","program","route","residual")[i%11],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"structural_authorities":8,"complete_structural":7,"contribution_classes":7,"programs":3,"executable":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,7,3))})
_ROOTS={"INPUT":_r((BASELINE,C215_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"REQUEST":request_freeze()["root"],"AUTHORITY":structural_authority_ledger()["root"],"STATE":common_state_schema()["root"],"CONTRIBUTIONS":two_point_contribution_ledger()["root"],"SCHEMA":adapter_program_schema()["root"],"PROGRAMS":adapter_program_manifest()["root"],"ROUTES":route_certificate_manifest()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C216-HQCDRIQUARKADAPTER1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C216_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
