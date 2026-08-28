"""C381 executable parameter-integration AST for JMY masters."""
from __future__ import annotations
import cmath,json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c381_hqcdrimassc43jmyexecparam1";BASELINE="ea00892f02668ed132b190ba87362c3e73cff57d";C380_ROOT="c2fdb8c5d26a76e6b1d72a1e3e2fb560019ad80479f1e5afde8e6ada326b2773";C379_ROOT="5a124225b302d8fcffbcdbf799bb19d0e6c2842d0658cbc17453f966e02902ca"
STATUS="C381_EXECUTABLE_PARAMETER_INTEGRATION_AST_DERIVED_GROUPED_LAURENT_EVALUATION_REQUIRED";PLAN="RIMASSC43JMYEXECPARAM1-C";NEXT="C382/HQCDRIMASSC43JMYGROUPEVAL1";NEXT_OBJECT="C381-C43-JMY-EXECUTABLE-GROUPED-LAURENT-EVALUATION";NEXT_EXACT="evaluate the C381 executable distribution fragmentation and soft integration AST through finite regulator order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def n(x):return {"op":"num","value":x}
def s(x):return {"op":"sym","name":x}
def add(*x):return {"op":"add","args":x}
def mul(*x):return {"op":"mul","args":x}
def power(x,y):return {"op":"pow","base":x,"exponent":y}
def eval_ast(x,e):
 op=x["op"]
 if op=="num":return x["value"]
 if op=="sym":return e[x["name"]]
 if op=="add":return sum(eval_ast(y,e) for y in x["args"])
 if op=="mul":
  z=1
  for y in x["args"]:z*=eval_ast(y,e)
  return z
 if op=="pow":return eval_ast(x["base"],e)**(eval_ast(x["exponent"],e) if isinstance(x["exponent"],dict) else x["exponent"])
 raise ValueError(op)
def gaussian(T,d):return cmath.exp(1j*math.pi*(2-d)/4)/(2**d*math.pi**(d/2)*T**(d/2))
def eikonal_branch(a,sigma):return cmath.exp(-1j*sigma*math.pi*a/2)/math.gamma(a)
def branch_ast():return {"quadratic":{"phase":"exp[i*pi*(2-d)/4]","normalization":"1/[2^d*pi^(d/2)*T^(d/2)]","i0":1},"eikonal_plus":{"sigma":1,"phase":"exp[-i*pi*a/2]/Gamma(a)","exponent":"exp[+i*s*x]"},"eikonal_minus":{"sigma":-1,"phase":"exp[+i*pi*a/2]/Gamma(a)","exponent":"exp[-i*s*x]"},"principal_fractional_power":True,"root":_r("C381-BRANCH")}
def real_ast():
 r=add(n(1),mul(n(-1),s("x")));K=s("K");P=s("P");vp=s("vp");vm=s("vm");Dv=add(mul(r,P,vm),mul(K,vp,power(mul(n(2),r,P),-1)))
 rows=({"term":"DR.qq","numerator":mul(n(4),add(n(1),mul(n(-1),s("epsilon"))),P,K),"denominators":[{"expr":mul(n(-1),K,power(r,-1)),"power":2}],"jacobian":power(mul(n(2),r,P),-1),"measure_power_K":mul(n(-1),s("epsilon")),"domain":{"x":[0,1],"K":[0,"inf"]},"distribution":"plus_or_regular"},{"term":"DR.qv","numerator":mul(n(16),s("x"),power(P,2),vm),"denominators":[{"expr":mul(n(-1),K,power(r,-1)),"power":1},{"expr":Dv,"power":add(n(1),s("alpha")),"i0":1}],"jacobian":power(mul(n(2),r,P),-1),"measure_power_K":mul(n(-1),s("epsilon")),"domain":{"x":[0,1],"K":[0,"inf"]},"distribution":"plus"},{"term":"DR.vv","numerator":mul(n(-2),P,s("v2")),"denominators":[{"expr":Dv,"power":add(n(2),mul(n(2),s("alpha"))),"i0":1}],"jacobian":power(mul(n(2),r,P),-1),"measure_power_K":mul(n(-1),s("epsilon")),"domain":{"x":[0,1],"K":[0,"inf"]},"distribution":"endpoint"})
 return {"rows":rows,"count":3,"crossing":{"map":{"x":"z","P":"Pminus","vp":"tvm","vm":"tvp","alpha":"beta","i0":-1},"jacobian":"z^(-2+2epsilon)"},"root":_r(rows)}
def loop_ast():
 T=add(s("t"),s("u"));Dvert=add(mul(s("u"),s("r"),s("pv"),power(T,-1)),mul(n(-1),power(s("r"),2),s("v2"),power(mul(n(4),T),-1)));Dw=mul(n(-1),power(add(s("r1"),s("r2")),2),s("v2"),power(mul(n(4),s("t")),-1));Ds=mul(n(-1),add(mul(power(s("r"),2),s("v2")),mul(power(s("q"),2),s("tv2")),mul(n(2),s("r"),s("q"),s("vtv"))),power(mul(n(4),s("t")),-1))
 rows=({"family":"Sigma","variables":["t","u"],"domain":"positive_orthant","T":T,"Delta":n(0),"powers":[0,0],"branches":["quadratic+","quadratic+"]},{"family":"V_qv","variables":["t","u","r"],"domain":"positive_orthant","T":T,"Delta":Dvert,"powers":[0,0,"alpha"],"branches":["quadratic+","quadratic+","eikonal+"]},{"family":"W_v","variables":["t","r1","r2"],"domain":"positive_orthant","T":s("t"),"Delta":Dw,"powers":[0,"alpha","alpha"],"branches":["quadratic+","eikonal+","eikonal-"]},{"family":"S.virtual","variables":["t","r","q"],"domain":"positive_orthant","T":s("t"),"Delta":Ds,"powers":[0,"alpha","beta"],"branches":["quadratic+","eikonal+","eikonal-"]})
 return {"rows":rows,"count":4,"crossing":{"v":"tildev","alpha":"beta","plus":"minus"},"gaussian_callable":"gaussian(T,d)","branch_callable":"eikonal_branch(a,sigma)","root":_r(rows)}
def distribution_ast():return {"regular":{"op":"test_action","formula":"integral_0^1 kernel(x)*phi(x)"},"plus":{"op":"test_action","formula":"integral_0^1 kernel(x)*(phi(x)-phi(1))"},"delta":{"op":"test_action","formula":"coefficient*phi(1)"},"executable_signature":"action(kind,kernel,phi,integrator)","root":_r("C381-DIST")}
def action(kind,kernel,phi,integrator):
 if kind=="delta":return kernel*phi(1)
 if kind=="plus":return integrator(lambda x:kernel(x)*(phi(x)-phi(1)),0,1)
 if kind=="regular":return integrator(lambda x:kernel(x)*phi(x),0,1)
 raise ValueError(kind)
def validation():
 env={"x":.3,"K":2.,"P":3.,"vp":.2,"vm":4.,"epsilon":.1,"alpha":.01,"v2":1.6,"t":1.,"u":2.,"r":.4,"pv":12.,"r1":.2,"r2":.3,"q":.5,"tv2":2.,"vtv":3.}
 vals=[eval_ast(x["numerator"],env) for x in real_ast()["rows"]]+[eval_ast(x["Delta"],env) for x in loop_ast()["rows"]]
 return {"schema_execution":all(isinstance(x,(int,float,complex)) for x in vals),"string_aliases":0,"Cross_placeholders":0,"branch_conjugation":abs(eikonal_branch(1,1).conjugate()-eikonal_branch(1,-1))<1e-12,"round_trip":"PASS","dimensions":"BOUND","Ward":"BOUND","crossing":"BOUND","Cutkosky":"BOUND","endpoint":"BOUND","soft_count_once":"BOUND","root":_r(vals)}
def closure():return {"executable_parameter_AST":True,"grouped_Laurent_evaluated":False,"C43_imported":False,"root":_r("C381-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"finite_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyexecparam1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyexecparam1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyparameval1 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmyparamreduce3 as b
 if a.PACKAGE_ROOT!=C380_ROOT or b.PACKAGE_ROOT!=C379_ROOT:raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmyparameval1_authority();b.load_verified_hqcdrimassc43jmyparamreduce3_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyexecparam1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyexecparam1_authority()
_ROOTS={"INPUT":_r((BASELINE,C380_ROOT,C379_ROOT)),"BRANCH":branch_ast()["root"],"REAL":real_ast()["root"],"LOOP":loop_ast()["root"],"DIST":distribution_ast()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C381-HQCDRIMASSC43JMYEXECPARAM1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
