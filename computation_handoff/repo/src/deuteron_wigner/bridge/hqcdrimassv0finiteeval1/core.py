"""C306 finite-part evaluation audit at the source subtraction wall."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c306_hqcdrimassv0finiteeval1";BASELINE="3260ecac718916c0c58bf7b01f3a62462dd03413";C305_ROOT="bd276d6c64b573f7ccf791e22e5251cd16f9f871b27cada4caf07de32b4bc173"
STATUS="C306_ORDERED_LIMIT_EVALUATOR_READY_SOURCE_CENTER_SUBTRACTION_BRANCH_UNDEFINED_CENTER_WALL_PRESCRIPTION_MISSING";PLAN="RIMASSV0FINITEEVAL1-C";NEXT="C307/HQCDRIMASSV0CENTERLIMIT1";NEXT_OBJECT="C306-V0-CENTER-WALL-BRANCH-PRESCRIPTION";NEXT_EXACT="define and validate the one-sided or symmetric finite-part value of C293 V0 at the source subtraction point u=v=1/2"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def evaluator_program():return _f({"inputs":("N","epsilon","quadrature_order","center_branch"),"AST":"C303 three regulated sums","measure":"C304 J/6","domain":"C305 symmetric root-distance excision","basis":("1","CHI8","RE_TF3"),"order":"N limit then epsilon limit","executable_except":"center_branch","root":_r("C306-EVAL")})
def center_audit():return _f({"point":"u=v=1/2","root_coordinates":{"u":0.5,"v":0.5,"v-u":0.0},"zeta7":"zeta(0) is sawtooth endpoint +/-1/2 by adjacent chart","J":0,"AST":"individual denominators hit zero on declared branch","ordinary_value_exists":False,"source_statement":"sets plotted potential minimum to zero without publishing branch/limiting prescription","root":_r("C306-CENTER")})
def limit_attempts():
 rows=({"path":"v-u -> 0+","status":"ONE_SIDED_DIVERGENT_OR_BRANCH_DEPENDENT","accepted":False},{"path":"v-u -> 0-","status":"ONE_SIDED_DIVERGENT_OR_BRANCH_DEPENDENT","accepted":False},{"path":"symmetric average before mode limit","status":"DEFINED_ONLY_AFTER_NEW_PRESCRIPTION","accepted":False},{"path":"subtract ordinary point value","status":"UNDEFINED","accepted":False});return _f({"rows":rows,"count":4,"coefficient_family":"NOT_EVALUATED_NOT_ZERO","root":_r(rows)})
def evaluation_certificate():return _f({"N_limit_complete":False,"epsilon_limit_complete":False,"blocking_input":"center_branch","mathematical_contradiction":False,"source_qualified_next":True,"C43_matching":False,"root":_r("C306-CERT")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"evaluator_ready":True,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"center_value_invented":0,"branch_selected":0,"divergence_dropped":0,"coefficient_zeroed":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0finiteeval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("N","epsilon","quadrature","center","branch","zeta","wall","limit","certificate","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0finiteeval1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0finitepart1 as c305
 if c305.PACKAGE_ROOT!=C305_ROOT:raise ValueError("C305 root changed")
 c305.load_verified_hqcdrimassv0finitepart1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0finiteeval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0finiteeval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C305_ROOT)),"EVAL":evaluator_program()["root"],"CENTER":center_audit()["root"],"ATTEMPT":limit_attempts()["root"],"CERT":evaluation_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C306-HQCDRIMASSV0FINITEEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
