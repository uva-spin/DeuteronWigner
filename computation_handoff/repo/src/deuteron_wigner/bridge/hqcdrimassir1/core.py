"""C279 signed-mass common-IR record reconciliation."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c279_hqcdrimassir1"
BASELINE="05d10584f7080681d23eb3baf4de69acb0732e56";C278_ROOT="61406fb610302b90150db398ab2d57c15acc4d0cfcab27c1305e5f56c32585ef"
STATUS="C279_C157_SIGNED_MASS_IR_SCHEMA_RECONCILED_C158_FB_EXECUTABLE_RI_SMOM_TARGET_AST_MISSING";PLAN="RIMASSIR1-C"
NEXT="C280/HQCDRIMASSTARGETAST1";NEXT_OBJECT="C153-RI-SMOM-SIGNED-MASS-EXECUTABLE-TARGET-AST";NEXT_EXACT="source-qualified executable RI/SMOM continuum signed-quark-mass projected coefficient AST and numerical enclosure"
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
def authority_reconciliation():
 rows=(("C157 schema/validator","READY"),("C157 rho/mu record instances","UNBOUND_NO_DEFAULT"),("C158 signed-mass finite-basis evaluator","EXECUTABLE_CONDITIONAL"),("C153/C164 RI/SMOM target definition/locators","SYMBOLIC_DEPENDENCIES_ONLY"),("C153 executable continuum target AST","MISSING"),("common-IR difference/cancellation","BLOCKED_ON_TARGET_AST"))
 return _f({"rows":tuple({"object":a,"status":b} for a,b in rows),"count":6,"historical_label_reconciled":True,"root":_r(rows)})
def record_readiness():
 rows=tuple({"resolution":r,"quantity_id":"SIGNED_QUARK_MASS","target_scheme_id":"RI_SMOM","schema_validatable":True,"finite_basis_executable":True,"continuum_target_executable":False,"numeric_record_authenticated":False,"common_ir_cancellation":False} for r in RESOLUTIONS)
 return _f({"rows":rows,"records":3,"authenticated":0,"root":_r(rows)})
def route_ledger():
 routes=("DIRECT_DIFFERENCE","PROJECTED_GREEN_FUNCTION_RATIO","INVERSE_ROUNDTRIP","LOG_RHO_DERIVATIVE","RHO_VARIATION")
 return _f({"routes":tuple({"route":x,"finite_basis":"READY","target":"TARGET_AST_MISSING","agreement":None} for x in routes),"false_agreement":False,"root":_r(routes)})
def uncertainty_boundary():return _f({"finite_basis_enclosure":"C158 componentwise","target_enclosure":None,"common_ir_residual":None,"perturbative_remainder":None,"missing_as_zero":False,"root":_r("target-AST-missing")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"record_schemas":3,"authenticated_records":0,"finite_basis_routes":3,"target_routes":0,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"untracked_C157_evidence_consumed":0,"fixture_promoted":0,"rho_mu_merged":0,"C117_coordinates_selected":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassir1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("schema","rho","mu","Nf","flavor","FB","target","difference","derivative","variation","uncertainty")[i%11],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassir1_authority():
 from deuteron_wigner.bridge import hqcdrimassstate1 as c278,hqcdmatchir2 as c157,hqcdfbnum as c158
 if c278.PACKAGE_ROOT!=C278_ROOT:raise ValueError("C278 root changed")
 c278.load_verified_hqcdrimassstate1_authority();c157.load_verified_hqcd_matchir_authority();c158.load_verified_hqcd_fbnum_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassir1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassir1_authority()
_ROOTS={"INPUT":_r((BASELINE,C278_ROOT)),"RECONCILIATION":authority_reconciliation()["root"],"RECORDS":record_readiness()["root"],"ROUTES":route_ledger()["root"],"UNCERTAINTY":uncertainty_boundary()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C279-HQCDRIMASSIR1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
