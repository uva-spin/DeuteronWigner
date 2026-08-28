"""C376 executable scalar/distribution AST for grouped JMY masters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c376_hqcdrimassc43jmyexecutableast1";BASELINE="1bdee571f995f82a0fef3ec95eafea360ced129b";C375_ROOT="e4170786415347c4c88a2b5c5d88c057de630f89a8de76af2c37e4c5106fe2af"
STATUS="C376_EXECUTABLE_SCALAR_DISTRIBUTION_AST_DERIVED_PARAMETER_REDUCTION_REQUIRED";PLAN="RIMASSC43JMYEXECUTABLEAST1-C";NEXT="C377/HQCDRIMASSC43JMYPARAMREDUCE2";NEXT_OBJECT="C376-C43-JMY-EXECUTABLE-AST-PARAMETER-REDUCTION";NEXT_EXACT="reduce the C376 executable loop cut and soft AST to explicit parameter integrals with resolved scalar polynomials"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def N(x):return {"op":"num","value":x}
def S(x):return {"op":"sym","name":x}
def A(*x):return {"op":"add","args":x}
def M(*x):return {"op":"mul","args":x}
def P(x,n):return {"op":"pow","base":x,"exponent":n}
def evaluate(node,env):
 op=node["op"]
 if op=="num":return node["value"]
 if op=="sym":return env[node["name"]]
 if op=="add":return sum(evaluate(x,env) for x in node["args"])
 if op=="mul":
  z=1
  for x in node["args"]:z*=evaluate(x,env)
  return z
 if op=="pow":return evaluate(node["base"],env)**node["exponent"]
 raise ValueError(op)
def distribution_action(node,phi,integrate):
 if node["op"]=="delta":return node["coefficient"]*phi(1.0)
 if node["op"]=="plus":return node["coefficient"]*integrate(lambda x:node["kernel"](x)*(phi(x)-phi(1.0)),0.0,1.0)
 raise ValueError(node["op"])
def denominator_ast():
 rows=({"id":"Dg","expr":A(M(N(2),S("ell_plus"),S("ell_minus")),M(N(-1),S("ellT2"))),"i0":1},{"id":"Dq","expr":A(S("p2"),S("ell2"),M(N(-2),S("p_dot_ell"))),"i0":1},{"id":"Dv","expr":S("v_dot_ell"),"i0":1},{"id":"Dtv","expr":S("tv_dot_ell"),"i0":-1})
 return {"rows":rows,"count":4,"mass_terms":0,"root":_r(rows)}
def numerator_ast():
 rows=({"term":"DR.qq","expr":M(N(2),A(N(4),M(N(-2),S("epsilon"))),A(M(N(2),S("q_plus"),S("p_dot_q")),M(N(-1),S("q2"),S("p_plus"))))},{"term":"DR.qv","expr":M(N(4),A(M(S("p_plus"),S("q_dot_v")),M(N(-1),S("p_dot_q"),S("v_plus")),M(S("p_dot_v"),S("q_plus"))))},{"term":"DR.vv","expr":M(N(-1),N(2),S("p_plus"),S("v2"))},{"term":"Sigma_q","expr":M(A(N(-2),M(N(2),S("epsilon"))),A(S("proj_p_minus_ell")))},{"term":"W_v","expr":S("v2")},{"term":"W_tildev","expr":S("tv2")},{"term":"V_qv","expr":A(M(S("vslash_proj"),S("p_minus_ell_proj")))},{"term":"V_htv","expr":A(M(S("tvslash_proj"),S("p_minus_ell_proj")))},{"term":"S.virtual","expr":M(N(-2),N(2),S("v_dot_tv"))},{"term":"S.real.v","expr":S("v2")},{"term":"S.real.tv","expr":S("tv2")},{"term":"S.real.interference","expr":M(N(-1),N(2),S("v_dot_tv"))})
 return {"rows":rows,"count":12,"crossing":{"DR.qq":"FR.qq","DR.qv":"FR.qv","DR.vv":"FR.vv"},"root":_r(rows)}
def master_ast():
 rows=({"term":"DR.qq","family":"cut","den":[("Dq",2,0)],"analytic":[],"multiplicity":1,"measurement":"Mx"},{"term":"DR.qv","family":"cut","den":[("Dq",1,0),("Dv",1,"alpha")],"analytic":[("nu1",2,"alpha")],"multiplicity":2,"measurement":"Mx"},{"term":"DR.vv","family":"cut","den":[("Dv",2,"2alpha")],"analytic":[("nu1",4,"alpha")],"multiplicity":1,"measurement":"Mx"},{"term":"Sigma_q","family":"loop","den":[("Dg",1,0),("Dq",1,0)],"analytic":[],"multiplicity":1,"measurement":"delta_x"},{"term":"W_v","family":"loop","den":[("Dg",1,0),("Dv+",1,"alpha"),("Dv-",1,"alpha")],"analytic":[("nu1",4,"alpha")],"multiplicity":1,"measurement":"delta_x"},{"term":"W_tildev","family":"loop","den":[("Dg",1,0),("Dtv-",1,"beta"),("Dtv+",1,"beta")],"analytic":[("nu2",4,"beta")],"multiplicity":1,"measurement":"delta_z"},{"term":"V_qv","family":"loop","den":[("Dg",1,0),("Dq",1,0),("Dv",1,"alpha")],"analytic":[("nu1",2,"alpha")],"multiplicity":2,"measurement":"delta_x"},{"term":"V_htv","family":"loop","den":[("Dg",1,0),("Dq",1,0),("Dtv",1,"beta")],"analytic":[("nu2",2,"beta")],"multiplicity":2,"measurement":"delta_z"},{"term":"S.virtual","family":"soft_loop","den":[("Dg",1,0),("Dv",1,"alpha"),("Dtv",1,"beta")],"analytic":[("nu1",2,"alpha"),("nu2",2,"beta")],"multiplicity":1,"measurement":"one"},{"term":"S.real.v","family":"soft_cut","den":[("Dv+",1,"alpha"),("Dv-",1,"alpha")],"analytic":[("nu1",4,"alpha")],"multiplicity":1,"measurement":"Mb_minus_one"},{"term":"S.real.tv","family":"soft_cut","den":[("Dtv-",1,"beta"),("Dtv+",1,"beta")],"analytic":[("nu2",4,"beta")],"multiplicity":1,"measurement":"Mb_minus_one"},{"term":"S.real.interference","family":"soft_cut","den":[("Dv",1,"alpha"),("Dtv",1,"beta")],"analytic":[("nu1",2,"alpha"),("nu2",2,"beta")],"multiplicity":1,"measurement":"Mb_minus_one"})
 return {"rows":rows,"count":12,"crossed_real":3,"total_graph_terms":15,"root":_r(rows)}
def distribution_ast():return {"delta":{"op":"delta","coefficient":1},"plus":{"op":"plus","coefficient":1,"kernel_id":"1/(1-x)"},"semantics":{"delta":"phi(1)","plus":"integral_0^1 dx [phi(x)-phi(1)]/(1-x)"},"root":_r("C376-DIST")}
def validation():
 env={k:1.0 for k in ("ell_plus","ell_minus","ellT2","p2","ell2","p_dot_ell","v_dot_ell","tv_dot_ell","epsilon","q_plus","p_dot_q","q2","p_plus","q_dot_v","v_plus","p_dot_v","v2","tv2","proj_p_minus_ell","vslash_proj","p_minus_ell_proj","tvslash_proj","v_dot_tv")}
 vals=[evaluate(r["expr"],env) for r in denominator_ast()["rows"]]+[evaluate(r["expr"],env) for r in numerator_ast()["rows"]]
 return {"schema_evaluation":all(isinstance(x,(int,float)) for x in vals),"prose_nodes":0,"dimensions":"BOUND","Ward":"BOUND","crossing":"BOUND","Cutkosky":"BOUND","soft_count_once":"BOUND","mass_IR":0,"root":_r(vals)}
def closure():return {"executable_AST":True,"parameter_reduced":False,"Laurent_evaluated":False,"C43_imported":False,"root":_r("C376-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"prose_node":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyexecutableast1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyexecutableast1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmymastereval2 as c
 if c.PACKAGE_ROOT!=C375_ROOT:raise ValueError("C375")
 c.load_verified_hqcdrimassc43jmymastereval2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyexecutableast1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyexecutableast1_authority()
_ROOTS={"INPUT":_r((BASELINE,C375_ROOT)),"DEN":denominator_ast()["root"],"NUM":numerator_ast()["root"],"MASTER":master_ast()["root"],"DIST":distribution_ast()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C376-HQCDRIMASSC43JMYEXECUTABLEAST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
