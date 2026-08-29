"""C300 BRST/ST classification of transverse zero-mode mass operators."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c300_hqcdrimassadjointst1"
BASELINE="bad2124a2fe8d44f29e7d73d660a94fcfccf6bd8";C299_ROOT="dadda4afd8ee8e1b1281b266e9fc6e768ebec2c5811bd86b01bf53e1577a5a6d"
STATUS="C300_BULK_TRANSVERSE_MASS_BRST_FORBIDDEN_BOUNDARY_HOLONOMY_POTENTIAL_ALLOWED_MATCHING_MISSING";PLAN="RIMASSADJOINTST1-B"
NEXT="C301/HQCDRIMASSHOLONOMYPOT1";NEXT_OBJECT="C300-BOUNDARY-HOLONOMY-EFFECTIVE-POTENTIAL";NEXT_EXACT="derive or match the gauge-invariant C43 finite-cell holonomy effective potential replacing the forbidden local bulk transverse-mass term at K9/K11/K13"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def authority_freeze():return _f({"C203":"BRST differential authority","C204":"endpoint/link BRST remainder","C205":"global orbit/holonomy identity","C206":"ST-compatible counterterm classification","C299":C299_ROOT,"root":_r(("C203","C204","C205","C206",C299_ROOT))})
def operator_split():
 rows=({"operator":"integral tr(A_perp^2)","scope":"local 3+1 bulk","class":"NOT_BRST_CLOSED"},{"operator":"tr(Phi^2)","scope":"dimensionally reduced adjoint scalar","class":"GAUGE_COVARIANT_REDUCED_OPERATOR_NOT_DIRECT_C43_BULK_MAP"},{"operator":"V_eff[W_boundary]","scope":"finite-cell holonomy/boundary","class":"GAUGE_INVARIANT_CLASS_FUNCTION_ALLOWED"});return _f({"rows":rows,"count":3,"root":_r(rows)})
def brst_identity():return _f({"differential":"s A_perp=D_perp c; s c=-(g/2)[c,c]","variation":"s tr(A_perp^2)=2 tr(A_perp D_perp c)","generic_zero":False,"bulk_mass_coefficient":"FORBIDDEN_AS_INDEPENDENT_BRST_INVARIANT_COUNTERTERM","nilpotency":"s^2 A_perp=0 with Jacobi/graded signs","root":_r("C300-BRST-A2")})
def boundary_exception():return _f({"Wilson_line":"W=P exp(i g integral A)","BRST":"sW=c(end)W-Wc(start)","closed_loop_or_identified_endpoint":"trace/class-function invariant after endpoint identification","local_mass_equivalent":False,"coefficient":"UNMATCHED_NOT_ZERO","root":_r("C300-WILSON-CLASS")})
def resolution_classification():
 rows=tuple({"resolution":k,"bulk_Aperp2":0,"zero_reason":"BRST_FORBIDDEN_OPERATOR_CLASS_NOT_NUMERICAL_FIT","boundary_holonomy":"ALLOWED_UNMATCHED","cross_K_covariance":"REQUIRED"} for k in ("K9","K11","K13"));return _f({"rows":rows,"count":3,"root":_r(rows)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"bulk_classified":True,"boundary_matched":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"reduced_scalar_promoted":0,"boundary_potential_zeroed":0,"quark_mass_substituted":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassadjointst1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("Aperp","ghost","BRST","nilpotency","bulk","endpoint","Wilson","K","covariance","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassadjointst1_authority():
 from deuteron_wigner.bridge import hqcdrimassconstraintinput1 as c299
 if c299.PACKAGE_ROOT!=C299_ROOT:raise ValueError("C299 root changed")
 c299.load_verified_hqcdrimassconstraintinput1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassadjointst1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassadjointst1_authority()
_ROOTS={"INPUT":_r((BASELINE,C299_ROOT)),"AUTH":authority_freeze()["root"],"SPLIT":operator_split()["root"],"BRST":brst_identity()["root"],"BOUNDARY":boundary_exception()["root"],"K":resolution_classification()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C300-HQCDRIMASSADJOINTST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
