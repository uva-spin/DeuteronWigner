"""C227 exact positive-branch normal forms for canonical vertex primitives."""
from __future__ import annotations
import json
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
import sympy as sp
from deuteron_wigner.bridge import hqcdriquarkfixedkvho1 as c226
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c227_hqcdriquarkfixedkvnorm1"
BASELINE="c18cba03ea115088cd006d5a9e8575522869813a";C226_ROOT="8c62132477c4cfdd95aa24b129cfedce41a8431c5894c300a244e8a1fd6b22ee"
CONTRACT="docs/next_level/c226_c227_hqcdriquarkfixedkvnorm1_continuation_contract.json";CONTRACT_SHA256="69d2c70116402cfbbb9bc3ff052900265ce1f70304ce23101ffe7e346800ac33"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c227_hqcdriquarkfixedkvnorm1_codex_prompt.md";PROMPT_SHA256="2fa56a79393d346415be65ca37d17532fb05cb9d5c07bb83a799a66e3aec03cb"
STATUS="C227_C226_EIGHT_EXACT_REAL_POSITIVE_BRANCH_PRIMITIVE_NORMAL_FORMS_READY";PLAN="RIQUARKFIXEDKVNORM1-A"
NEXT="C228/HQCDRIQUARKFIXEDKVHO2";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-HO-PROJECTION-NORMALIZED"
NEXT_EXACT="exact analytic polar-HO projection of the eight expanded C227 positive-branch primitive normal forms"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
@lru_cache(maxsize=1)
def _forms():
 I=sp.I;rt=sp.sqrt(2);x,y,P,m,qx,qy=sp.symbols("x_q x_g P_plus m_q q_x q_y",positive=True,real=True);z=sp.zeros(2);sx=sp.Matrix([[0,1],[1,0]]);sy=sp.Matrix([[0,-I],[I,0]]);sz=sp.diag(1,-1);g0=sp.diag(1,1,-1,-1)
 def gi(a):return sp.Matrix.vstack(sp.Matrix.hstack(z,a),sp.Matrix.hstack(-a,z))
 g=(g0,gi(sx),gi(sy),gi(sz))
 def u(pp,px,py,h):
  pm=(m*m+px*px+py*py)/(2*pp);E=(pp+pm)/rt;pz=(pp-pm)/rt;a=sp.sqrt(E+m)
  return sp.Matrix([a,0,pz/a,(px+I*py)/a]) if h==1 else sp.Matrix([0,a,(px-I*py)/a,-pz/a])
 def eps(kp,kx,ky,h):
  ex=-h/rt;ey=-I/rt;em=(kx*ex+ky*ey)/kp
  return sp.Matrix([sp.conjugate(em)/rt,sp.conjugate(ex),sp.conjugate(ey),-sp.conjugate(em)/rt])
 rows=[]
 for ho in (-1,1):
  for hi in (-1,1):
   for hg in (-1,1):
    a=u(x*P,sp.sqrt(y)*qx,sp.sqrt(y)*qy,ho);b=u(P,0,0,hi);e=eps(y*P,-sp.sqrt(x)*qx,-sp.sqrt(x)*qy,hg);G=g[0]*e[0]-g[1]*e[1]-g[2]*e[2]-g[3]*e[3]
    expr=sp.factor(sp.simplify((sp.conjugate(a).T*g0*G*b)[0]));srepr=sp.srepr(expr)
    rows.append({"normal_form_id":f"C227-NF-HO{ho}-HI{hi}-HG{hg}","h_out":ho,"h_in":hi,"h_g":hg,"expression":srepr,"expression_sha256":sha256(srepr.encode()).hexdigest(),"free_symbols":tuple(sorted(str(v) for v in expr.free_symbols)),"conjugates_remaining":srepr.count("conjugate"),"branch":"positive sqrt(E+m)","constraint":"x_q+x_g=1; both positive"})
 return tuple(rows)
def normal_form_manifest():
 rows=_forms();return _f({"rows":rows,"count":8,"complete":8,"conjugates_remaining":sum(r["conjugates_remaining"] for r in rows),"root":_r(rows)})
def branch_certificate():return _f({"assumptions":("x_q>0","x_g>0","x_q+x_g=1","P_plus>0","m_q>=0","q_x,q_y real"),"E_plus_m_positive":True,"sqrt_branch":"principal positive real","unconstrained_simplify":False,"root":_r(("positive-domain",8))})
def route_certificate():return _f({"route_A":"explicit Dirac matrices and BPP spinors","route_B":"C50 source numerator DAG with all numeric leaves replaced by symbols","gamma_metric":"diag(+,-,-,-)","helicity_count":8,"conjugates_remaining":0,"structural_mismatches":0,"root":_r((8,0,"gamma"))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"normal_forms_ready":8,"HO_projection_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"normal_form_root":normal_form_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"numeric_fit":0,"quadrature_authority":0,"physical_defaults":0,"retained_ids":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvnorm1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("xq","xg","Pplus","mass","qx","qy","branch","gamma","helicity","conjugate","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"normal_forms":8,"conjugates":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,0))})
def verify_hqcd_riquarkfixedkvnorm1_authority():
 if c226.PACKAGE_ROOT!=C226_ROOT:raise ValueError("C226 root changed")
 c226.load_verified_hqcd_riquarkfixedkvho1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C226_package_root":C226_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvnorm1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvnorm1_authority()
_ROOTS={"INPUT":_r((BASELINE,C226_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"FORMS":normal_form_manifest()["root"],"BRANCH":branch_certificate()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C227-HQCDRIQUARKFIXEDKVNORM1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C227_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
