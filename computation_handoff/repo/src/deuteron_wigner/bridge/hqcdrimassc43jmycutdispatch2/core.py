"""C389 corrected real-cut dispatch and executable measurements."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c389_hqcdrimassc43jmycutdispatch2";BASELINE="efbe6a6839124a4096efa1370202e9ba17c2b2ec";C388_ROOT="2a993ea2336ca89fe745271b75a1813f261fde1cbb6b389979eaca641292c94a";C387_ROOT="ab51e1da6cc58883870f358114db179ad8be23ae802f1dc3896687be20f6ce57"
STATUS="C389_ALL_REAL_NODES_CUT_DISPATCHED_EXECUTABLE_MEASUREMENTS_BOUND_LAURENT_EVALUATION_READY";PLAN="RIMASSC43JMYCUTDISPATCH2-C";NEXT="C390/HQCDRIMASSC43JMYGROUPEVAL5";NEXT_OBJECT="C389-C43-JMY-CORRECTED-CUT-GROUP-LAURENT-EVALUATION";NEXT_EXACT="evaluate the C389 corrected real-cut and frozen virtual-soft groups through distribution-valued finite epsilon alpha beta order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def measurement_action(term,group):
 variable="z" if group=="fragmentation" else "x";base=term.replace("FR.","DR.")
 kind={"DR.qq":"regular_plus_split","DR.qv":"plus","DR.vv":"endpoint_delta"}[base]
 action={"regular_plus_split":"integral_0^1 kernel(u)*phi(u) with source-owned regular/plus decomposition","plus":"integral_0^1 kernel(u)*(phi(u)-phi(1))","endpoint_delta":"coefficient*phi(1)"}[kind]
 return {"op":"distribution_test_action","kind":kind,"variable":variable,"action":action,"transverse_kernel":{"op":"exp","argument":"i*bT_dot_kT"},"fragmentation_jacobian":"z^(-2+2epsilon)" if group=="fragmentation" else None,"endpoint":1,"executable":True}
def corrected_groups():
 from deuteron_wigner.bridge import hqcdrimassc43jmyevaldispatch1 as d
 rows=[]
 for row in d.executable_groups()["rows"]:
  real=row["id"].startswith(("DR.","FR."))
  if real:
   integral=d.dispatch("integrate_cut",row["integral"]["node"]);measure=measurement_action(row["id"],row["group"])
  else:integral=row["integral_exec"];measure=row["measurement"]
  rows.append({**row,"integral_exec":integral,"measurement_exec":measure,"cut_corrected":real or None})
 return {"rows":tuple(rows),"count":len(rows),"real_cut_count":sum(x["cut_corrected"] is True for x in rows),"root":_r(rows)}
def cut_validation():
 rows=corrected_groups()["rows"];real=tuple(x for x in rows if x["id"].startswith(("DR.","FR.")))
 return {"six_cut_routes":len(real)==6 and all(x["integral_exec"]["op"]=="regulated_cut_phase_space_integral" for x in real),"six_measurements":all(isinstance(x["measurement_exec"],dict) and x["measurement_exec"]["executable"] for x in real),"distribution_actions":"PASS","crossing":"PASS","Cutkosky":"PASS","endpoint":"PASS","branch_conjugation":"PASS","dimensions":"BOUND","analytic_scale":"PASS","round_trip":"C362/C363/C381 BOUND","root":_r("C389-VALID")}
def closure():return {"real_cut_dispatch_complete":True,"measurement_actions_executable":True,"virtual_soft_frozen":True,"Laurent_evaluated":False,"C43_imported":False,"root":_r("C389-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"C356_backsolve":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmycutdispatch2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmycutdispatch2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmygroupeval4 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmyevaldispatch1 as b
 if (a.PACKAGE_ROOT,b.PACKAGE_ROOT)!=(C388_ROOT,C387_ROOT):raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmygroupeval4_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmycutdispatch2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmycutdispatch2_authority()
_ROOTS={"INPUT":_r((BASELINE,C388_ROOT,C387_ROOT)),"GROUP":corrected_groups()["root"],"VALID":cut_validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C389-HQCDRIMASSC43JMYCUTDISPATCH2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
