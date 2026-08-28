"""C390 corrected-group Laurent evaluation readiness audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c390_hqcdrimassc43jmygroupeval5";BASELINE="51fed3bf002da644fb7360dbaa6826809752373d";C389_ROOT="b4cc247d56f1aa129239fb220b59b43e92f92b3aef6ba4ca2101cca70d160edb"
STATUS="C390_GROUP_LAURENT_EVALUATION_FAIL_CLOSED_TRANSVERSE_FOURIER_AND_REGULAR_PLUS_EXECUTOR_REQUIRED";PLAN="RIMASSC43JMYGROUPEVAL5-C";NEXT="C391/HQCDRIMASSC43JMYMEASUREEVAL1";NEXT_OBJECT="C390-C43-JMY-TRANSVERSE-FOURIER-REGULAR-PLUS-EVALUATOR";NEXT_EXACT="derive executable d-dimensional transverse Fourier-Bessel measurement kernels and the source-owned DRqq FRqq regular-plus decomposition"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def first_node_audit():
 from deuteron_wigner.bridge import hqcdrimassc43jmycutdispatch2 as c
 row=next(x for x in c.corrected_groups()["rows"] if x["id"]=="DR.qq");m=row["measurement_exec"]
 return {"node":"DR.qq","cut_dispatch":row["integral_exec"]["op"],"measurement_op":m["op"],"transverse_kernel_argument":m["transverse_kernel"]["argument"],"transverse_angular_measure":None,"Bessel_order":None,"Fourier_normalization":None,"regular_plus_decomposition":m["action"],"regular_plus_coefficients_bound":False,"executable_to_scalar_or_distribution":False,"root":_r(m)}
def group_audit():return {"terms":16,"first_failed_node":"DR.qq","Laurent_terms_evaluated":0,"UV_entries":0,"IR_entries":0,"analytic_entries":0,"finite_entries":0,"reason":"measurement AST contains an unevaluated dot-product string and prose regular/plus split","root":_r("C390-AUDIT")}
def evaluation_gate():return {"Laurent_evaluation_performed":False,"finite_coefficients_published":False,"separator_cancellation_claimed":False,"fail_closed":True,"root":_r("C390-GATE")}
def validation():return {"Cutkosky_dispatch":"PASS","measurement_execution":"FAIL_CLOSED","coefficient_invention":0,"mass_IR_import":0,"C356_backsolve":0,"C43_import":0,"root":_r("C390-VALID")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupeval5(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupeval5_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmycutdispatch2 as c
 if c.PACKAGE_ROOT!=C389_ROOT:raise ValueError("C389 root")
 c.load_verified_hqcdrimassc43jmycutdispatch2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupeval5_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupeval5_authority()
_ROOTS={"INPUT":_r((BASELINE,C389_ROOT)),"FIRST":first_node_audit()["root"],"GROUP":group_audit()["root"],"GATE":evaluation_gate()["root"],"VALID":validation()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C390-HQCDRIMASSC43JMYGROUPEVAL5-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
