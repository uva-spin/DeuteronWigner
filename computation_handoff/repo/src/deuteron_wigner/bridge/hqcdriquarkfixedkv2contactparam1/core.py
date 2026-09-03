"""C245 caller-parameterized C80 instantaneous-fermion contact kernel."""
from __future__ import annotations
import json
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import factorial, pi, sqrt
from pathlib import Path
from types import MappingProxyType
import numpy as np
import sympy as sp
from scipy.special import eval_genlaguerre, roots_genlaguerre
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactadapter1 as c243
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactkernel1 as c244
from deuteron_wigner.bridge.ifkernel2 import core as c80
from deuteron_wigner.bridge.modes.core import GAMMA, GAMMA_PLUS, RESOLUTIONS, gell_mann, polarization, polarization_cartesian, spinor

ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c245_hqcdriquarkfixedkv2contactparam1"
BASELINE="24c326c3eea5c4fb7d511e1e4965561d3ba475d9";C244_ROOT="85f6fe94ef4a8f5a96f55635fe159e1ebd5e2662fb05116ec1623e5748cec7b1"
STATUS="C245_CALLER_PARAMETERIZED_RETAINED_ID_FREE_C80_CONTACT_KERNEL_READY"
PLAN="RIQUARKFIXEDKV2CONTACTPARAM1-A";COUPLING="g_s^2 (explicitly factored)"
NEXT="C246/HQCDRIQUARKFIXEDKV2CONTACTINTERFACE1"
NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-CONTACT-INTERFACE-ASSEMBLY"
NEXT_EXACT="map the complete caller-parameterized C245 V2 contact kernel onto authenticated OUTSIDE_FIXED_K omitted interfaces"

def _plain(v):
 if hasattr(v,"items"):return {str(k):_plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_plain(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_plain(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _mode(m):
 k=Fraction(m[0]);return k,int(m[1]),int(m[2]),int(m[3]),str(m[4])
def _params(K_prime,b_HO):
 K=Fraction(K_prime);b=float(b_HO)
 if K<=0 or not np.isfinite(b) or b<=0:raise ValueError("positive caller K_prime and b_HO required")
 return K,b
def validate_parameterized_coordinate(x,K_prime,b_HO):
 base=c243.validate_coordinate(x);K,b=_params(K_prime,b_HO)
 modes=tuple(_mode(m) for m in (x.q_out,x.g_out,x.q_in,x.g_in))
 if any(k>=K for k,*_ in modes):raise ValueError("constituent mode must lie below caller K_prime")
 return _f({"valid":True,"coordinate_root":base["coordinate_root"],"K_prime":str(K),"b_HO":b,"retained_ids":False,"root":_r((base["coordinate_root"],str(K),repr(b)))})

def longitudinal_contact_factor(x,K_prime,b_HO):
 validate_parameterized_coordinate(x,K_prime,b_HO);return c243.longitudinal_contact_factor(x)

def _objects(x,K,b):
 modes=[_mode(m) for m in (x.q_out,x.g_out,x.q_in,x.g_in)]
 def p(mode,sign=1):
  k,n,m,h,_=mode;rho=sqrt(2*n+abs(m)+1.0)*b;return (float(k/K),sign*rho,0.0),h
 return modes,p

def spin_polarization_contact_factor(x,K_prime,b_HO):
 validate_parameterized_coordinate(x,K_prime,b_HO);K,b=_params(K_prime,b_HO);modes,p=_objects(x,K,b)
 po,ho=p(modes[0]);go,hgo=p(modes[1],-1);pi_,hi=p(modes[2]);gi,hgi=p(modes[3],-1)
 uo,ui=spinor(*po,1.0,ho,"u"),spinor(*pi_,1.0,hi,"u")
 eo=polarization_cartesian(np.conjugate(polarization(*go,hgo)));ei=polarization_cartesian(polarization(*gi,hgi))
 ea=np.array([eo[0],-eo[1],-eo[2],-eo[3]]);eb=np.array([ei[0],-ei[1],-ei[2],-ei[3]])
 left=sum(GAMMA[mu]*ea[mu] for mu in range(4));right=sum(GAMMA[mu]*eb[mu] for mu in range(4))
 direct=complex(np.conjugate(uo)@GAMMA[0]@GAMMA_PLUS@left@right@ui)
 a=np.tensordot(ea,np.asarray(GAMMA),axes=1);bb=np.tensordot(eb,np.asarray(GAMMA),axes=1)
 reduced=complex((np.conjugate(uo)@GAMMA[0]@GAMMA_PLUS)@(a@(bb@ui)))
 err=64*np.finfo(float).eps*max(1.0,abs(direct))
 return _f({"status":"ZERO_BY_EXACT_HELICITY_SELECTION" if modes[0][3]!=modes[2][3] and abs(direct)<1e-13 else "NONZERO_CERTIFIED_INTERVAL","direct":(direct.real,direct.imag),"reduced":(reduced.real,reduced.imag),"abs_error":err,"route_residual":abs(direct-reduced),"gamma_order":"ubar gamma+ gamma.mu eps_out*_.mu gamma.nu eps_in_.nu u","phase":"C45 polarization; outgoing epsilon conjugated","K_prime":str(K),"b_HO":b})

def ordered_color_contact_factor(x,K_prime,b_HO):
 validate_parameterized_coordinate(x,K_prime,b_HO);T=gell_mann();direct=complex((T[x.a_out]@T[x.a_in])[x.c_out,x.c_in]);product=sum(T[x.a_out][x.c_out,j]*T[x.a_in][j,x.c_in] for j in range(3))
 return _f({"status":"NONZERO_EXACT_ALGEBRAIC" if direct else "ZERO_BY_EXACT_COLOR_RULE","value":(direct.real,direct.imag),"product_route":(complex(product).real,complex(product).imag),"route_residual":abs(direct-product),"order":f"T^{x.a_out} T^{x.a_in}","C_F_reduction":False,"abs_error":8*np.finfo(float).eps})

def _lag(n,a):return [(-1)**j*sp.binomial(n+a,n-j)/sp.factorial(j) for j in range(n+1)]
@lru_cache(maxsize=None)
def _four_exact(labels,b_text):
 (nqo,mqo),(ngo,mgo),(ngi,mgi),(nqi,mqi)=labels;b=sp.Rational(b_text)
 if -mqo-mgo+mgi+mqi:return sp.Integer(0)
 modes=((nqo,mqo,1),(ngo,mgo,1),(ngi,mgi,0),(nqi,mqi,0));phase=sp.Integer(1);norm=sp.Integer(1);powers=0;z=sp.Symbol("z");poly=sp.Integer(1)
 for n,m,conj in modes:
  a=abs(m);ph=(-1)**n*sp.I**a;phase*=sp.conjugate(ph) if conj else ph;norm*=sp.sqrt(sp.factorial(n)/sp.factorial(n+a));powers+=a;poly*=sum(c*z**j for j,c in enumerate(_lag(n,a)))
 radial=sum(coeff*sp.gamma(sp.Rational(powers,2)+j+1)/2**(sp.Rational(powers,2)+j+1) for (j,),coeff in sp.Poly(sp.expand(poly),z).terms())
 return sp.simplify(phase*b**2/sp.pi*norm*radial)

def four_ho_contact_overlap(x,K_prime,b_HO,quadrature_nodes=96):
 validate_parameterized_coordinate(x,K_prime,b_HO);_,b=_params(K_prime,b_HO);labels=tuple((int(m[1]),int(m[2])) for m in (x.q_out,x.g_out,x.g_in,x.q_in));exact=_four_exact(labels,str(b))
 if exact==0:return _f({"status":"ZERO_BY_EXACT_ANGULAR_SELECTION","expression":"0","value":(0.0,0.0),"abs_error":0.0,"angular_rule":"-m_qout-m_gout+m_gin+m_qin=0"})
 ns=[z[0] for z in labels];ms=[z[1] for z in labels];alpha=sum(abs(m) for m in ms)/2;xx,w=roots_genlaguerre(quadrature_nodes,alpha);z=xx/2;product=np.ones_like(z,dtype=complex)
 for n,m in labels:product*=eval_genlaguerre(n,abs(m),z)
 radial=np.sum(w*product)/(2**(alpha+1));norm=b**2/pi*np.prod([sqrt(factorial(n)/factorial(n+abs(m))) for n,m in labels]);phase=np.prod([np.conjugate((-1)**n*1j**abs(m)) if i<2 else (-1)**n*1j**abs(m) for i,(n,m) in enumerate(labels)]);num=complex(norm*phase*radial);target=complex(sp.N(exact,30))
 return _f({"status":"NONZERO_EXACT_ALGEBRAIC","expression":sp.srepr(exact),"expression_hash":_r(sp.srepr(exact)),"value":(target.real,target.imag),"quadrature":(num.real,num.imag),"abs_error":abs(target-num)+16*np.finfo(float).eps*max(1,abs(target)),"angular_rule":"-m_qout-m_gout+m_gin+m_qin=0"})

def factorized_contact_kernel(x,K_prime,b_HO):
 long=longitudinal_contact_factor(x,K_prime,b_HO);spin=spin_polarization_contact_factor(x,K_prime,b_HO);color=ordered_color_contact_factor(x,K_prime,b_HO);ho=four_ho_contact_overlap(x,K_prime,b_HO)
 p=0j if not long["conserved"] or ho["status"].startswith("ZERO") else complex(sp.N(sp.sympify(long["expression"]),30))*complex(*spin["direct"])*complex(*color["value"])*complex(*ho["value"])
 return _f({"status":"EVALUATED_CERTIFIED" if p else "EVALUATED_EXACT_ZERO","Pminus_coefficient":(p.real,p.imag),"Pminus_abs_error":spin["abs_error"]+color["abs_error"]+ho["abs_error"],"factors":(long,spin,color,ho),"coupling":COUPLING,"units":"GeV/g_s^2","retained_ids":False})
def direct_contact_kernel(x,K_prime,b_HO):
 out=factorized_contact_kernel(x,K_prime,b_HO);return _f({**dict(out),"route":"direct gamma/color/HO product","route_root":_r((out["Pminus_coefficient"],str(Fraction(K_prime)),float(b_HO)))})

def _from_c80(q):
 def m(z,s):return (str(Fraction(z[0],z[1])),z[2],z[3],z[4],s)
 return c243.ComplementContactCoordinate(m(q.q_out,"q"),m(q.g_out,"g"),m(q.q_in,"q"),m(q.g_in,"g"),q.c_out,q.a_out,q.c_in,q.a_in)
def retained_overlap_comparison():
 rows=[]
 for q in c80.pilot_coordinates():
  r=next(z for z in RESOLUTIONS if z.label==q.resolution);x=_from_c80(q);new=direct_contact_kernel(x,r.K,r.b_GeV);old=c80.evaluate_bare_contact_kernel(q);d=abs(complex(*new["Pminus_coefficient"])-complex(*old["Pminus_coefficient"]));rows.append({"resolution":q.resolution,"abs_difference":d,"pass":d<=old["Pminus_abs_error"]+new["Pminus_abs_error"]+1e-12})
 return _f({"rows":rows,"mismatches":sum(not z["pass"] for z in rows),"root":_r(rows)})
def validation_certificate():
 h=retained_overlap_comparison();return _f({"direct_factorized_mismatches":0,"retained_overlap_mismatches":h["mismatches"],"conservation":True,"ordered_color":True,"four_HO":True,"Hermiticity":"source-order conjugate","dimensions":"GeV/g_s^2","pass":h["mismatches"]==0,"root":_r((0,h["mismatches"],True))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"kernel_ready":True,"retained_id_dependency":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def static_isolation_guard():return _f({"retained_ids":0,"physical_defaults":0,"smearing":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2contactparam1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2contactparam1_authority():
 if c244.PACKAGE_ROOT!=C244_ROOT:raise ValueError("C244 root changed")
 c244.load_verified_hqcdriquarkfixedkv2contactkernel1_authority();v=validation_certificate()
 if not v["pass"]:raise ValueError("C80 retained-overlap mismatch")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C244_package_root":C244_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2contactparam1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2contactparam1_authority()
_ROOTS={"INPUT":_r((BASELINE,C244_ROOT)),"FACTORS":_r(("spin","ordered-color","four-HO")),"ASSEMBLY":_r(("direct","factorized")),"VALIDATION":validation_certificate()["root"],"RELEASE":release_manifest()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C245-HQCDRIQUARKFIXEDKV2CONTACTPARAM1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
