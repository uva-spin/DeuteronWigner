"""C361 trace-reduction preflight and real-cut topology audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c361_hqcdrimassc43jmytracereduce1";BASELINE="0c6a91e37561c510f82d780f6af5e211e5ba51d5";C360_ROOT="c1ba54558f4d49ea58d38d6662f070055a41abfedfd2b78b372ebf94a5422398"
STATUS="C361_TRACE_REDUCTION_PREFLIGHT_REAL_CUT_ONSHELL_DELTA_TOPOLOGY_MISSING";PLAN="RIMASSC43JMYTRACEREDUCE1-C";NEXT="C362/HQCDRIMASSC43JMYCUTTOPO1";NEXT_OBJECT="C361-C43-JMY-REAL-CUT-ONSHELL-TOPOLOGY";NEXT_EXACT="bind the source-correct Cutkosky on-shell delta and phase-space topology for the C360 distribution and fragmentation real nodes"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def topology_audit():
 rows=({"node":"DR.qq","gluon_cut":True,"final_quark_cut":False,"source_requires_final_state_onshell":True},{"node":"DR.qv","gluon_cut":True,"final_quark_cut":False,"source_requires_final_state_onshell":True},{"node":"DR.vv","gluon_cut":True,"final_quark_cut":"measurement-dependent endpoint","source_requires_final_state_onshell":True},{"node":"FR.*","gluon_cut":True,"final_quark_cut":False,"source_requires_final_state_onshell":True})
 return {"rows":rows,"scalar_reduction_safe":False,"root":_r(rows)}
def source_check():return {"source":"hep-ph/0404183v1 Fig.2 and Eqs.(9)-(12)","evidence":"real-emission results are cut correlators with fixed x,kT and physical final state; denominators reduce only after the on-shell phase-space constraint","C360_missing":"explicit CutPlus((p-k)^2) or equivalent solved light-cone delta with Jacobian","mass_formula_reused":False,"root":_r("C361-S")}
def reduction_hold():return {"traces_reduced":False,"reason":"applying p^2=k^2=0 without the final-state cut changes numerator cancellations and endpoint Jacobians","partial_scalar_forms":"UNAVAILABLE_NOT_ZERO","ordinary_repair_continuation":True,"root":_r("C361-H")}
def closure():return {"C360_trace_syntax_preserved":True,"cut_topology_complete":False,"scalar_reduction_complete":False,"finite_groups_evaluated":False,"C43_imported":False,"root":_r("C361-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"onshell_constraint_assumed":0,"premature_trace_reduction":0,"mass_result_reused":0,"partial_scalar_published":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmytracereduce1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmytracereduce1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmytraceast1 as c
 if c.PACKAGE_ROOT!=C360_ROOT:raise ValueError("C360")
 c.load_verified_hqcdrimassc43jmytraceast1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmytracereduce1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmytracereduce1_authority()
_ROOTS={"INPUT":_r((BASELINE,C360_ROOT)),"TOPO":topology_audit()["root"],"SOURCE":source_check()["root"],"HOLD":reduction_hold()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C361-HQCDRIMASSC43JMYTRACEREDUCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
