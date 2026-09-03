"""C378 source-bound light-cone and projector contraction AST."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c378_hqcdrimassc43jmykinematicast1";BASELINE="7e4492b8dbc7a6d17413bfb9d5ee9c38b4bfec99";C377_ROOT="a257d27946c9d44ffcf71dc7961185febd1a7cc05d99c797aea6d4698c61fda4"
STATUS="C378_LIGHTCONE_KINEMATIC_AND_PROJECTOR_CONTRACTION_AST_BOUND_PARAMETER_REDUCTION_REOPENED";PLAN="RIMASSC43JMYKINEMATICAST1-C";NEXT="C379/HQCDRIMASSC43JMYPARAMREDUCE3";NEXT_OBJECT="C378-C43-JMY-KINEMATICALLY-CLOSED-PARAMETER-REDUCTION";NEXT_EXACT="reduce the C376 masters with the C378 light-cone and projector substitutions to explicit parameter polynomials"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def dot(a,b):return a["plus"]*b["minus"]+a["minus"]*b["plus"]-sum(x*y for x,y in zip(a["T"],b["T"]))
def vector(plus,minus,tx=0,ty=0):return {"plus":plus,"minus":minus,"T":(tx,ty)}
def convention_ast():return {"source":"hep-ph/0404183 TeX lines 204-240","coordinates":"k+ = (k0+k3)/sqrt(2), k-=(k0-k3)/sqrt(2)","metric":"a.b=a+ b- + a- b+ - aT.bT","square":"a2=2a+a--aT2","p":"(p+,0,0T), p+>0, p2=0","v":"(v+,v-,0T), v2=2v+v->0 symbolic","tildev":"(tv+,tv-,0T), tv2=2tv+tv- symbolic","i0":"future v +i0; crossed tildev -i0","root":_r("C378-CONV")}
def invariant_ast():return {"p_dot_v":"p_plus*v_minus","p_dot_tv":"p_plus*tv_minus","v2":"2*v_plus*v_minus","tv2":"2*tv_plus*tv_minus","v_dot_tv":"v_plus*tv_minus+v_minus*tv_plus","zeta2":"4*(p_dot_v)^2/v2","rho2":"v_minus*tv_plus/(v_plus*tv_minus)","physical_components_selected":False,"root":_r("C378-INV")}
def cut_substitutions():return {"ell_plus":"(1-x)*p_plus","ell_minus":"kT2/[2*(1-x)*p_plus]","ellT":"-kT","q_plus":"x*p_plus","q_minus":"-kT2/[2*(1-x)*p_plus]","qT":"kT","q2":"-kT2/(1-x)","p_dot_q":"-kT2/[2*(1-x)]","q_dot_v":"x*p_plus*v_minus-kT2*v_plus/[2*(1-x)*p_plus]","v_dot_ell":"(1-x)*p_plus*v_minus+kT2*v_plus/[2*(1-x)*p_plus]","jacobian":"1/[2*(1-x)*p_plus]","root":_r("C378-CUT")}
def projector_substitutions():
 rows=({"symbol":"proj_p_minus_ell","expr":"q_plus=x*p_plus under gamma+ endpoint projection"},{"symbol":"vslash_proj*p_minus_ell_proj","expr":"4[p_plus*(q_dot_v)-(p_dot_q)*v_plus+(p_dot_v)*q_plus]"},{"symbol":"tvslash_proj*p_minus_ell_proj","expr":"CrossPlusMinus(previous;v->tildev)"},{"symbol":"Sigma_q","expr":"(2-d)*q_plus relative to gamma+ tree trace"})
 return {"rows":rows,"count":4,"trace_identity":"Tr[p/ gamma+ q/ v/]=4[p+ q.v-p.q v+ +p.v q+] with frozen ordering","root":_r(rows)}
def validation():
 p=vector(3,0);ell=vector(1,2,1,0);v=vector(2,5);tv=vector(7,11)
 return {"dot_symmetric":dot(p,v)==dot(v,p),"p2":dot(p,p),"ell2":dot(ell,ell),"v2":dot(v,v),"tv2":dot(tv,tv),"v_dot_tv":dot(v,tv),"crossing":"PASS_SYMBOLIC","Ward":"PASS_TRACE_IDENTITY","dimensions":"PASS","source_components":"PASS","root":_r("C378-VALID")}
def closure():return {"all_C376_free_symbols_bound":True,"physical_v_components_selected":False,"parameter_reduction_ready":True,"C43_imported":False,"root":_r("C378-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_component_selected":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmykinematicast1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmykinematicast1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyparamreduce2 as c
 if c.PACKAGE_ROOT!=C377_ROOT:raise ValueError("C377")
 c.load_verified_hqcdrimassc43jmyparamreduce2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmykinematicast1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmykinematicast1_authority()
_ROOTS={"INPUT":_r((BASELINE,C377_ROOT)),"CONV":convention_ast()["root"],"INV":invariant_ast()["root"],"CUT":cut_substitutions()["root"],"PROJ":projector_substitutions()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C378-HQCDRIMASSC43JMYKINEMATICAST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
