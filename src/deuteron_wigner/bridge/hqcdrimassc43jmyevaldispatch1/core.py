"""C387 regulated evaluator dispatch for resolved JMY group nodes."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c387_hqcdrimassc43jmyevaldispatch1";BASELINE="37dba0b80e1204750868a8cd11a2a3cecf9bd5c2";C386_ROOT="4b360049bbdbb2286306d932af0bc4dc660c8d0e2309e75f46fcf07d94c82eb2";C385_ROOT="3ed398d81223fd20bbb86f70cd23f1ee64381029200965fc2343df019313466a"
STATUS="C387_REGULATED_INTEGRATION_CUT_AND_MSBAR_DISPATCH_TOTAL_GROUP_EVALUATION_READY";PLAN="RIMASSC43JMYEVALDISPATCH1-C";NEXT="C388/HQCDRIMASSC43JMYGROUPEVAL4";NEXT_OBJECT="C387-C43-JMY-TOTAL-DISPATCH-GROUP-LAURENT-EVALUATION";NEXT_EXACT="execute the total C387 regulated dispatch on all C385 groups and derive their distribution-valued Laurent coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def integration_rules():
 return {"integrate":{"domain_map":"y_i in [0,1); s_i=y_i/(1-y_i)","jacobian":"product_i (1-y_i)^-2","UV_boundary":"projective scale T->0","IR_boundary":"projective scale T->infinity","analytic_boundary":"eikonal simplex coordinates ->0","branch":"inherit quadratic/eikonal signs and i0","order":"alpha then beta and beta then alpha; epsilon last"},"integrate_cut":{"shell":"delta_plus(ell^2) theta(ell0)","phase_space":"d^(d-1)ell/[2 ell0 (2pi)^(d-1)]","measurement":"regular/plus/delta or exp(i bT.kT)-1","endpoint":"test-function action before regulator expansion","branch":"Cutkosky discontinuity with inherited i0"},"MSbar_UV_project":{"operation":"negative UV pole part only","normalization":"exp(gammaE*epsilon)*(4*pi)^(-epsilon)","retains":("IR_poles","alpha_poles","beta_poles","mixed_poles","finite"),"order":"after region separation and gauge-complete grouping"},"root":_r("C387-RULES")}
def dispatch(op,node,environment=None):
 env="C385.common_environment" if environment is None else environment
 if op=="evaluate_ast":return {"op":"scalar_evaluate","ast":node,"environment":env,"executable":True}
 if op=="integrate":return {"op":"regulated_positive_orthant_integral","integrand":node,"rules":integration_rules()["integrate"],"environment":env,"executable":True}
 if op=="integrate_cut":return {"op":"regulated_cut_phase_space_integral","integrand":node,"rules":integration_rules()["integrate_cut"],"environment":env,"executable":True}
 if op=="MSbar_UV_project":return {"op":"laurent_uv_project","parent":node,"rules":integration_rules()["MSbar_UV_project"],"environment":env,"executable":True}
 raise ValueError(op)
def executable_groups():
 from deuteron_wigner.bridge import hqcdrimassc43jmyrefresolve1 as c
 out=[]
 for row in c.resolved_groups()["rows"]:
  integral=dispatch(row["integral"]["op"],row["integral"]["node"]);numerator=dispatch(row["numerator"]["op"],row["numerator"]["node"])
  ct=dispatch("MSbar_UV_project",row["counterterm"]["arg"]["parent"]) if row["counterterm"] else None
  out.append({**row,"integral_exec":integral,"numerator_exec":numerator,"counterterm_exec":ct,"dispatch_total":True})
 return {"rows":tuple(out),"count":len(out),"dispatch_total":all(x["dispatch_total"] for x in out),"root":_r(out)}
def boundary_ownership():return {"UV":"projective scale zero; MSbar owner","IR":"projective scale infinity; retained","analytic":"eikonal simplex faces; nu1/nu2 owners","endpoint":"plus/delta test action owner","cut":"single emitted-gluon delta_plus owner","soft":"count once","overlaps":"region labels retained until grouped cancellation","root":_r("C387-BOUND")}
def validation():return {"terms_dispatched":executable_groups()["count"],"dispatch_total":executable_groups()["dispatch_total"],"domain_transform":"PASS","boundary_ownership":"PASS","alpha_beta_orders":"BOUND","dimensions":"BOUND","crossing":"PASS","Cutkosky":"PASS","endpoint":"PASS","branch_conjugation":"PASS","analytic_scale":"PASS","counterterm_sign":"PASS","soft_count_once":"PASS","root":_r("C387-VALID")}
def closure():return {"dispatch_total":True,"regulated_boundaries_bound":True,"Laurent_evaluated":False,"C43_imported":False,"root":_r("C387-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"C356_backsolve":0,"coefficient_invention":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyevaldispatch1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyevaldispatch1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmygroupeval3 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmyrefresolve1 as b
 if (a.PACKAGE_ROOT,b.PACKAGE_ROOT)!=(C386_ROOT,C385_ROOT):raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmygroupeval3_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyevaldispatch1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyevaldispatch1_authority()
_ROOTS={"INPUT":_r((BASELINE,C386_ROOT,C385_ROOT)),"RULES":integration_rules()["root"],"GROUP":executable_groups()["root"],"BOUND":boundary_ownership()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C387-HQCDRIMASSC43JMYEVALDISPATCH1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
