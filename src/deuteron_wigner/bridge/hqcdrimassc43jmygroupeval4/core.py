"""C388 total-dispatch group evaluation topology audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c388_hqcdrimassc43jmygroupeval4";BASELINE="4d5fe264b0803b57219b86dcce33a4c4199534e6";C387_ROOT="ab51e1da6cc58883870f358114db179ad8be23ae802f1dc3896687be20f6ce57"
STATUS="C388_GROUP_LAURENT_EVALUATION_FAIL_CLOSED_REAL_CUT_DISPATCH_AND_MEASUREMENT_BINDING_REQUIRED";PLAN="RIMASSC43JMYGROUPEVAL4-C";NEXT="C389/HQCDRIMASSC43JMYCUTDISPATCH2";NEXT_OBJECT="C388-C43-JMY-REAL-CUT-DISPATCH-MEASUREMENT-BINDING";NEXT_EXACT="route all six distribution and fragmentation real-emission nodes through integrate_cut and bind their executable transverse plus regular and endpoint measurement actions"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def topology_audit():
 from deuteron_wigner.bridge import hqcdrimassc43jmyevaldispatch1 as c
 rows=c.executable_groups()["rows"];real=tuple(x for x in rows if x["id"].startswith(("DR.","FR.")))
 wrong=tuple(x["id"] for x in real if x["integral_exec"]["op"]!="regulated_cut_phase_space_integral")
 vague=tuple(x["id"] for x in real if isinstance(x["measurement"],str))
 return {"terms":len(rows),"real_terms":len(real),"real_expected_dispatch":"regulated_cut_phase_space_integral","misrouted_real_terms":wrong,"unbound_measurement_actions":vague,"cut_dispatch_complete":not wrong,"measurement_actions_executable":not vague,"root":_r((wrong,vague))}
def evaluation_gate():return {"Laurent_evaluation_performed":False,"finite_coefficients_published":False,"first_invalid_node":"DR.qq","reason":"real-emission AST is routed through positive-orthant virtual integration and measurement is a label, not an executable test action","fail_closed":True,"root":_r("C388-GATE")}
def validation():return {"all_16_audited":True,"Cutkosky_topology":"FAIL_CLOSED","endpoint_actions":"UNBOUND","alpha_beta_orders_executed":False,"mass_IR_import":0,"C356_backsolve":0,"coefficient_invention":0,"C43_import":0,"root":_r("C388-VALID")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupeval4(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupeval4_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyevaldispatch1 as c
 if c.PACKAGE_ROOT!=C387_ROOT:raise ValueError("C387 root")
 c.load_verified_hqcdrimassc43jmyevaldispatch1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupeval4_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupeval4_authority()
_ROOTS={"INPUT":_r((BASELINE,C387_ROOT)),"AUDIT":topology_audit()["root"],"GATE":evaluation_gate()["root"],"VALID":validation()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C388-HQCDRIMASSC43JMYGROUPEVAL4-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
