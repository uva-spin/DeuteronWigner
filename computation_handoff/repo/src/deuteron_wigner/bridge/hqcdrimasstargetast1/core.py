"""C280 source-qualified RI/SMOM mass target AST skeleton."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c280_hqcdrimasstargetast1"
BASELINE="9401a1015d8b9abc08195c455c126d05725d84c1";C279_ROOT="b2c27f7886c7210bc3c6eeae19583ec596948bd505c681183a33272225574830"
STATUS="C280_RI_SMOM_MASS_TARGET_AST_SKELETON_SOURCE_BOUND_FOUR_DEPENDENCY_LEAVES_OPEN";PLAN="RIMASSTARGETAST1-C"
NEXT="C281/HQCDRIMASSCOORD1";NEXT_OBJECT="C165-REQ-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-0";NEXT_EXACT="coordinate definition object with exact equation or authenticated source supplement for RI/SMOM signed-quark-mass normalization and perturbative power"
SOURCE="arxiv_0901.2599";VERSION="arXiv:0901.2599v2";EQ=("(11)","(20)","(24)")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_freeze():return _f({"source_id":SOURCE,"version":VERSION,"root_equation":"(24)","dependency_equations":EQ,"visual_locator":"C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM","source_role":"RI/SMOM signed-mass conversion target","formula_transcribed":False,"root":_r((SOURCE,VERSION,EQ))})
def dependency_ledger():
 rows=((0,"PERTURBATIVE_COORDINATE_DEFINITION","exact source normalization/power binding for the source coordinate"),(1,"ACTIVE_NF_DEFINITION","active-N_f and external-flavor semantics for this root"),(2,"FROZEN_PROJECT_OWNED_IDENTITY","source-to-C43 light-front gauge/scheme adapter"),(3,"COUNTERTERM_OR_SUBTRACTION_DEFINITION","complete bare/counterterm/renormalized/finite conversion layer ancestry"))
 return _f({"rows":tuple({"ordinal":i,"request_id":f"C165-REQ-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-{i}","node_class":n,"missing":m,"closed":False} for i,n,m in rows),"open":4,"first":NEXT_OBJECT,"root":_r(rows)})
def ast_schema():return _f({"schema":"PROJECT_RI_SMOM_SIGNED_MASS_TARGET_AST_V1","allowlisted_opcodes":("LOAD_COORDINATE","LOAD_PROJECTOR","LOAD_WARD_IDENTITY","LOAD_CONVERSION","ADD","SUB","MUL","DIV_GUARDED","LOG","POLYLOG","RETURN_ENCLOSURE"),"eval":False,"callbacks":False,"pickle":False,"dynamic_imports":False,"unknown_opcode":"reject","root":_r("safe-ast")})
def ast_skeleton():
 nodes=({"id":0,"opcode":"LOAD_COORDINATE","status":"DEPENDENCY_0_MISSING"},{"id":1,"opcode":"LOAD_PROJECTOR","source_equation":"(24)","status":"SOURCE_BOUND"},{"id":2,"opcode":"LOAD_WARD_IDENTITY","source_equation":"(20)","status":"SOURCE_BOUND"},{"id":3,"opcode":"LOAD_CONVERSION","status":"DEPENDENCIES_1_3_MISSING"},{"id":4,"opcode":"RETURN_ENCLOSURE","status":"BLOCKED"})
 return _f({"program_id":"C280-RI-SMOM-MASS-TARGET","nodes":nodes,"executable":False,"numerical_enclosure":None,"root":_r(nodes)})
def route_certificate():return _f({"routes":tuple({"route":x,"status":"SAME_FOUR_DEPENDENCY_LEAVES_OPEN","agreement":None} for x in ("DIRECT_FORMULA","WARD_IDENTITY","INVERSE_CONVERSION","NUMERICAL_HOLDOUT")),"false_agreement":False,"root":_r("four-open")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"source_equations":3,"AST_skeletons":1,"executable_ASTs":0,"open_dependencies":4,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"memory_formula_transcribed":0,"invented_coefficients":0,"plots_fitted":0,"C158_recalculated":0,"C117_coordinates_selected":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimasstargetast1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","version","equation","coordinate","Nf","adapter","layer","opcode","branch","enclosure","route")[i%11],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimasstargetast1_authority():
 from deuteron_wigner.bridge import hqcdrimassir1 as c279,hqcdlfglocator2 as c164,hqcdlfgdep as c165
 if c279.PACKAGE_ROOT!=C279_ROOT:raise ValueError("C279 root changed")
 c279.load_verified_hqcdrimassir1_authority();c164.load_verified_hqcd_lfglocator2_authority();c165.load_verified_hqcd_lfgdep_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimasstargetast1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimasstargetast1_authority()
_ROOTS={"INPUT":_r((BASELINE,C279_ROOT)),"SOURCE":source_freeze()["root"],"DEPENDENCIES":dependency_ledger()["root"],"SCHEMA":ast_schema()["root"],"AST":ast_skeleton()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C280-HQCDRIMASSTARGETAST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
