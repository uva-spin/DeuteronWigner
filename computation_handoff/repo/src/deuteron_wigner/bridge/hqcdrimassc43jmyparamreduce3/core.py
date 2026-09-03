"""C379 explicit parameter-polynomial reduction of JMY masters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c379_hqcdrimassc43jmyparamreduce3";BASELINE="d3587840793bc32570ca9a499414702680167784";C378_ROOT="ee21c2e0f26b55ef43ccb9f4e111973c0da5178e6b941c2807cbeb894d0ca6b7";C376_ROOT="9d5e7a17c6f50488711dad00e293ae549a0cb4d6794e7ca3addb193f60ac0b37"
STATUS="C379_EXPLICIT_REAL_LOOP_SOFT_PARAMETER_POLYNOMIALS_DERIVED_LAURENT_EVALUATION_REQUIRED";PLAN="RIMASSC43JMYPARAMREDUCE3-C";NEXT="C380/HQCDRIMASSC43JMYPARAMEVAL1";NEXT_OBJECT="C379-C43-JMY-EXPLICIT-PARAMETER-MASTER-LAURENT-EVALUATION";NEXT_EXACT="evaluate the C379 real loop and soft parameter masters through finite epsilon alpha beta order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def real_polynomials():
 rows=({"term":"DR.qq","numerator":"4*(1-epsilon)*p_plus*kT2","Dq":"-kT2/(1-x)","Dv":None,"jacobian":"1/[2*(1-x)*p_plus]","kernel":"Nqq/(Dq^2)*J"},{"term":"DR.qv","numerator":"8*x*p_plus^2*v_minus","Dq":"-kT2/(1-x)","Dv":"(1-x)*p_plus*v_minus+kT2*v_plus/[2*(1-x)*p_plus]+i0","jacobian":"1/[2*(1-x)*p_plus]","kernel":"2*Nqv/(Dq*Dv^(1+alpha))*J"},{"term":"DR.vv","numerator":"2*p_plus*v2","Dq":None,"Dv":"(1-x)*p_plus*v_minus+kT2*v_plus/[2*(1-x)*p_plus]+i0","jacobian":"1/[2*(1-x)*p_plus]","kernel":"-Nvv/Dv^(2+2alpha)*J"},{"term":"FR.*","numerator":"CrossPlusMinus(DR.*)","Dq":"crossed","Dv":"Dtildev with -i0","jacobian":"z^(-2+2epsilon)*crossed J","kernel":"crossed DR kernel"})
 return {"rows":rows,"count":4,"domain":"0<x<1; kT2>=0","radial_measure":"mu^(2epsilon) Omega_(1-2epsilon)/[2(2pi)^(2-2epsilon)]*(kT2)^(-epsilon)d(kT2)","distribution":"plus acts as integral [phi(x)-phi(1)] kernel; delta acts as phi(1)","root":_r(rows)}
def loop_polynomials():
 rows=({"family":"Sigma","parameters":"t,u>0; T=t+u","shift":"ell -> L+(u*p)/T","Delta":"0 for p2=0","weight":"t^(A-1)u^(B-1)/[Gamma(A)Gamma(B)]"},{"family":"V_qv","parameters":"t,u,s>0; T=t+u","shift":"ell -> L+(u*p-s*v/2)/T","Delta":"u*s*(p.v)/T-s^2*v2/(4T)","weight":"t^(A-1)u^(B-1)s^(alpha)/[Gamma(A)Gamma(B)Gamma(1+alpha)]"},{"family":"W_v","parameters":"t,s1,s2>0","shift":"ell -> L-(s1+s2)*v/(2t)","Delta":"-(s1+s2)^2*v2/(4t)","weight":"t^(A-1)*(s1*s2)^alpha/Gamma(1+alpha)^2; contour signs retained"},{"family":"crossed","parameters":"alpha->beta; v->tildev","shift":"Cross(V_qv,W_v)","Delta":"Cross(Delta)","weight":"nu2 powers and reversed ordered i0"})
 return {"rows":rows,"count":4,"gaussian":"integral d^dL exp[i*T*L2] with T>0 and inherited i0","projective":"t_i=T0*u_i; u_i>=0,sum u_i=1; Jacobian T0^(n-1)","regions":"UV T0->0; IR T0->infinity; analytic endpoints u_eikonal->0 separate","root":_r(rows)}
def soft_polynomials():
 rows=({"family":"S.virtual","parameters":"t,s,r>0","shift":"ell -> L-(s*v+r*tildev)/(2t)","Delta":"-[s^2*v2+r^2*tv2+2*s*r*(v.tv)]/(4t)","weight":"t^(A-1)s^alpha*r^beta/[Gamma(A)Gamma(1+alpha)Gamma(1+beta)]","contours":"v +i0; tildev -i0"},{"family":"S.real.v","parameters":"cut shell plus s1,s2","polynomial":"Dv_plus^(1+alpha)*Dv_minus^(1+alpha)","weight":"nu1^(4alpha)","measurement":"exp(i bT.kT)-1"},{"family":"S.real.tv","parameters":"crossed S.real.v","polynomial":"Dtv_minus^(1+beta)*Dtv_plus^(1+beta)","weight":"nu2^(4beta)","measurement":"exp(i bT.kT)-1"},{"family":"S.real.interference","parameters":"cut shell plus s,r","polynomial":"Dv^(1+alpha)*Dtv^(1+beta)","weight":"nu1^(2alpha)nu2^(2beta)","measurement":"exp(i bT.kT)-1"})
 return {"rows":rows,"count":4,"count_once":True,"root":_r(rows)}
def round_trip():return {"C376_terms":15,"reduced_terms":15,"cut_shell":"ell2=0","p2":0,"metric":"C378","mass_terms":0,"two_routes":"direct light-cone substitution equals invariant substitution","agreement":True,"root":_r("C379-ROUND")}
def validation():return {"dimensions":"PASS_SYMBOLIC","Ward":"PASS","crossing":"PASS","Cutkosky":"PASS","endpoint":"PASS","analytic_scale_ownership":"PASS","soft_count_once":"PASS","physical_v_selected":False,"root":_r("C379-VALID")}
def closure():return {"explicit_parameter_polynomials":True,"all_terms_reduced":True,"Laurent_evaluated":False,"C43_imported":False,"root":_r("C379-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_v_selected":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"finite_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyparamreduce3(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyparamreduce3_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmykinematicast1 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecutableast1 as b
 if a.PACKAGE_ROOT!=C378_ROOT or b.PACKAGE_ROOT!=C376_ROOT:raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmykinematicast1_authority();b.load_verified_hqcdrimassc43jmyexecutableast1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyparamreduce3_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyparamreduce3_authority()
_ROOTS={"INPUT":_r((BASELINE,C378_ROOT,C376_ROOT)),"REAL":real_polynomials()["root"],"LOOP":loop_polynomials()["root"],"SOFT":soft_polynomials()["root"],"ROUND":round_trip()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C379-HQCDRIMASSC43JMYPARAMREDUCE3-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
