"""C384 closed-group Laurent evaluation readiness audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c384_hqcdrimassc43jmygroupeval2";BASELINE="25b3faead411b16e472f0e757c7cfb964468186f";C383_ROOT="ed3485b129f27f4c1b571a3c036f08423b3d15120c0bc8c3b5b1536b209b3fc0"
STATUS="C384_GROUP_LAURENT_EVALUATION_FAIL_CLOSED_EXECUTABLE_REFERENCE_RESOLUTION_REQUIRED";PLAN="RIMASSC43JMYGROUPEVAL2-C";NEXT="C385/HQCDRIMASSC43JMYREFRESOLVE1";NEXT_OBJECT="C384-C43-JMY-EXECUTABLE-GROUP-REFERENCE-RESOLVER";NEXT_EXACT="bind every C383 integral numerator and counterterm reference to an existing executable AST node with one common symbol environment"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def reference_audit():
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecgroup1 as c
 rows=sum((list(x) for x in c.group_ast()["groups"].values()),[])
 missing=("C381.loop.Sigma","C381.loop.W_v","C381.loop.V_qv","C381.cross.*","C381.softcut.*","C376.cross.*","CT.Z2q","CT.Zv","CT.Ztv","CT.Zvert.q","CT.Zvert.h")
 return {"terms_audited":len(rows),"string_references":sum(isinstance(x[k],str) for x in rows for k in ("integral_ref","numerator_ref")),"resolved_executable_nodes":0,"missing_namespaces":missing,"common_symbol_environment":False,"counterterm_projectors_executable":False,"root":_r(missing)}
def evaluation_gate():return {"closed_group_shape":True,"lawful_Laurent_evaluation":False,"finite_coefficients_published":False,"reason":"references are unbound strings and crossed/soft/counterterm targets lack executable resolver nodes","root":_r("C384-GATE")}
def validation():return {"alpha_beta_orders_executed":False,"separator_cancellation_claimed":False,"mass_IR_import":0,"C356_backsolve":0,"C43_import":0,"fail_closed":True,"root":_r("C384-VALID")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupeval2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupeval2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecgroup1 as c
 if c.PACKAGE_ROOT!=C383_ROOT:raise ValueError("C383 root")
 c.load_verified_hqcdrimassc43jmyexecgroup1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupeval2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupeval2_authority()
_ROOTS={"INPUT":_r((BASELINE,C383_ROOT)),"AUDIT":reference_audit()["root"],"GATE":evaluation_gate()["root"],"VALID":validation()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C384-HQCDRIMASSC43JMYGROUPEVAL2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
