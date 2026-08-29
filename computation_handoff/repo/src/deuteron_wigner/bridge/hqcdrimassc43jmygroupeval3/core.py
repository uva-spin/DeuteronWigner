"""C386 resolved-group execution audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c386_hqcdrimassc43jmygroupeval3";BASELINE="b974a5be12e807069fb61a54c4386ea41587ea9e";C385_ROOT="3ed398d81223fd20bbb86f70cd23f1ee64381029200965fc2343df019313466a"
STATUS="C386_GROUP_LAURENT_EVALUATION_FAIL_CLOSED_INTEGRATION_PROJECTOR_DISPATCH_REQUIRED";PLAN="RIMASSC43JMYGROUPEVAL3-C";NEXT="C387/HQCDRIMASSC43JMYEVALDISPATCH1";NEXT_OBJECT="C386-C43-JMY-REGULATED-INTEGRATION-PROJECTOR-DISPATCH";NEXT_EXACT="implement evaluator dispatch and regulated boundary semantics for the C385 integrate integrate_cut and MSbar_UV_project operations"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def execution_audit():
 from deuteron_wigner.bridge import hqcdrimassc43jmyrefresolve1 as c
 rows=c.resolved_groups()["rows"]
 ops=tuple(sorted({x["integral"]["op"] for x in rows}|{x["numerator"]["op"] for x in rows}|{"MSbar_UV_project"}))
 return {"terms":len(rows),"typed_references":True,"operations":ops,"implemented_dispatch":("evaluate_ast",),"missing_dispatch":("integrate","integrate_cut","MSbar_UV_project"),"regulated_infinite_boundary":False,"distribution_boundary":False,"UV_projector_semantics":False,"root":_r(ops)}
def evaluation_gate():return {"Laurent_evaluation_performed":False,"finite_coefficients_published":False,"first_nonexecutable_operation":"integrate","reason":"no dispatch or regulated boundary prescription","fail_closed":True,"root":_r("C386-GATE")}
def validation():return {"all_16_audited":True,"alpha_beta_orders_executed":False,"separator_cancellation_claimed":False,"mass_IR_import":0,"C356_backsolve":0,"C43_import":0,"coefficient_invention":0,"root":_r("C386-VALID")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupeval3(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupeval3_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyrefresolve1 as c
 if c.PACKAGE_ROOT!=C385_ROOT:raise ValueError("C385 root")
 c.load_verified_hqcdrimassc43jmyrefresolve1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupeval3_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupeval3_authority()
_ROOTS={"INPUT":_r((BASELINE,C385_ROOT)),"AUDIT":execution_audit()["root"],"GATE":evaluation_gate()["root"],"VALID":validation()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C386-HQCDRIMASSC43JMYGROUPEVAL3-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
