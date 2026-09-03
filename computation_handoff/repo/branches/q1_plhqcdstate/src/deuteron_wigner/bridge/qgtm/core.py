"""Threshold-free exact two-dimensional HO/TM coefficient generator."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
import json
from typing import Any
import sympy as sp
import numpy as np

from ..basis1.core import partitions, tm_cm_ground_map
from ..ifqgembed.core import STATUS as C61_STATUS, preflight as c61_preflight
from ..modes.core import RESOLUTIONS, array_hash

BASELINE='c22c6ab04e79a591aacc5679efd2b0642c3ad4e8'
STATUS='C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY'
NEXT='C63/QGEMBED2 — exact physical qg embedding and descendant-impact closure'
PLAN='QGTM-CIRCULAR-LADDER-PRIMARY'

def canonical_json(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(',',':'),default=str)
def digest(v:Any)->str:return sha256(canonical_json(v).encode()).hexdigest()
def expr_hash(e:sp.Expr)->str:return sha256(sp.srepr(sp.factor(e)).encode()).hexdigest()

@dataclass(frozen=True)
class ExactCoefficient:
    status:str; expression:str; expression_hash:str; value_re:float; value_im:float; proof:str

def polar_to_circular_state(n:int,m:int)->dict[str,Any]:
    if n<0: raise ValueError('n must be nonnegative')
    plus=n+max(m,0); minus=n+max(-m,0)
    return {'n':n,'m':m,'n_plus':plus,'n_minus':minus,'shell':plus+minus,'phase':'(-1)^n','phase_value':-1 if n%2 else 1,
            'identity':'n_plus-n_minus=m; n_plus+n_minus=2n+abs(m)'}

def _polar_shell(total:int)->list[tuple[int,int]]:
    return [(n,m) for n in range(total//2+1) for m in range(-total,total+1) if 2*n+abs(m)==total]

def polar_product_shell(total:int)->list[tuple[int,int,int,int]]:
    return [(nq,mq,ng,mg) for nq_total in range(total+1) for nq,mq in _polar_shell(nq_total)
            for ng,mg in _polar_shell(total-nq_total)]

def _field_add(a:tuple[Fraction,...],b:tuple[Fraction,...])->tuple[Fraction,...]:return tuple(x+y for x,y in zip(a,b))
def _field_mul(a:tuple[Fraction,...],b:tuple[Fraction,...],x:Fraction,y:Fraction)->tuple[Fraction,...]:
    out=[Fraction() for _ in range(4)] # basis 1,s,c,sc; index 2*cpar+spar
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            cp,sp_=divmod(i,2); cq,sq=divmod(j,2); csum=cp+cq; ssum=sp_+sq
            out[(csum%2)*2+(ssum%2)] += u*v*(x if csum==2 else 1)*(y if ssum==2 else 1)
    return tuple(out)

def _one_poly(q:int,g:int,cm:int,x:Fraction)->tuple[Fraction,...]:
    """Exact unnormalised bracket in Q(x) + sqrt(x)Q + sqrt(1-x)Q + sqrt(x(1-x))Q."""
    rel=q+g-cm; out=[Fraction() for _ in range(4)]
    if rel<0:return tuple(out)
    y=1-x
    for r in range(q+1):
        t=cm-r
        if 0<=t<=g:
            # q†=c CM†+s rel†; g†=s CM†-c rel†
            cp=r+g-t; spow=q-r+t
            coeff=Fraction(comb(q,r)*comb(g,t)*((-1)**(g-t)))*x**(cp//2)*y**(spow//2)
            out[(cp%2)*2+(spow%2)] += coeff
    return tuple(out)

def _sym_from_poly(poly:tuple[Fraction,...],x:Fraction)->sp.Expr:
    c=sp.sqrt(sp.Rational(x.numerator,x.denominator));s=sp.sqrt(1-c*c)
    return sp.expand(poly[0]+poly[2]*c+poly[1]*s+poly[3]*c*s)

def one_dimensional_tm_bracket(q:int,g:int,rel:int,cm:int,xq:Fraction)->ExactCoefficient:
    if min(q,g,rel,cm)<0 or q+g!=rel+cm:
        return ExactCoefficient('ZERO_BY_EXACT_SHELL_RULE','0',expr_hash(sp.S.Zero),0.,0.,'q+g != rel+cm')
    poly=_one_poly(q,g,cm,xq); expr=sp.sqrt(sp.Rational(factorial(rel)*factorial(cm),factorial(q)*factorial(g)))*_sym_from_poly(poly,xq)
    expr=sp.simplify(expr)
    if expr==0:return ExactCoefficient('ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION','0',expr_hash(expr),0.,0.,'exact finite binomial cancellation')
    z=complex(sp.N(expr,60));return ExactCoefficient('NONZERO_EXACT_ALGEBRAIC',sp.srepr(expr),expr_hash(expr),float(z.real),float(z.imag),'finite exact binomial extraction')

def _co_status(expr:sp.Expr,proof:str)->ExactCoefficient:
    expr=sp.simplify(expr)
    if expr==0:return ExactCoefficient('ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION','0',expr_hash(expr),0.,0.,proof)
    z=complex(sp.N(expr,60));return ExactCoefficient('NONZERO_EXACT_ALGEBRAIC',sp.srepr(expr),expr_hash(expr),float(z.real),float(z.imag),proof)

def polar_tm_coefficient(out:tuple[int,int,int,int], inn:tuple[int,int,int,int], xq:Fraction)->ExactCoefficient:
    ncm,mcm,nrel,mrel=out; nq,mq,ng,mg=inn
    if mcm+mrel != mq+mg:
        return ExactCoefficient('ZERO_BY_EXACT_M_RULE','0',expr_hash(sp.S.Zero),0.,0.,'m_CM+m_rel != m_q+m_g')
    C=polar_to_circular_state(ncm,mcm); R=polar_to_circular_state(nrel,mrel); Q=polar_to_circular_state(nq,mq); G=polar_to_circular_state(ng,mg)
    if Q['n_plus']+G['n_plus']!=R['n_plus']+C['n_plus'] or Q['n_minus']+G['n_minus']!=R['n_minus']+C['n_minus']:
        return ExactCoefficient('ZERO_BY_EXACT_SHELL_RULE','0',expr_hash(sp.S.Zero),0.,0.,'separate circular occupation conservation')
    bp=one_dimensional_tm_bracket(Q['n_plus'],G['n_plus'],R['n_plus'],C['n_plus'],xq)
    bm=one_dimensional_tm_bracket(Q['n_minus'],G['n_minus'],R['n_minus'],C['n_minus'],xq)
    if bp.status.startswith('ZERO') or bm.status.startswith('ZERO'):
        return ExactCoefficient('ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION','0',expr_hash(sp.S.Zero),0.,0.,'one circular sector exactly zero')
    expr=(-1)**(nq+ng+ncm+nrel)*sp.sympify(bp.expression,locals={'Integer':sp.Integer,'Rational':sp.Rational,'Pow':sp.Pow,'Mul':sp.Mul,'Add':sp.Add,'sqrt':sp.sqrt})*sp.sympify(bm.expression,locals={'Integer':sp.Integer,'Rational':sp.Rational,'Pow':sp.Pow,'Mul':sp.Mul,'Add':sp.Add,'sqrt':sp.sqrt})
    return _co_status(expr,'C45 polar phase (-1)^n times independent plus/minus exact brackets')

def _transformed_shell(total:int)->list[tuple[int,int,int,int]]:
    return [(ncm,mcm,nrel,mrel) for ncm_total in range(total+1) for ncm,mcm in _polar_shell(ncm_total)
            for nrel,mrel in _polar_shell(total-ncm_total)]

@lru_cache(maxsize=64)
def exact_tm_block(xnum:int,xden:int,total:int)->dict[str,Any]:
    x=Fraction(xnum,xden); raw=polar_product_shell(total); out=_transformed_shell(total)
    entries=[]; numeric=np.zeros((len(out),len(raw)),complex); statuses={}
    for i,o in enumerate(out):
        for j,p in enumerate(raw):
            c=polar_tm_coefficient(o,p,x); statuses[c.status]=statuses.get(c.status,0)+1
            numeric[i,j]=c.value_re+1j*c.value_im
            entries.append({'out':o,'in':p,**asdict(c)})
    return {'total_shell':total,'x':[xnum,xden],'raw':raw,'out':out,'entries':entries,'numeric':numeric,'statuses':statuses,'expression_hash':digest([(e['out'],e['in'],e['expression_hash'],e['status']) for e in entries])}

def residue_reconciliation()->dict[str,Any]:
    rows=[]; totals=[]
    for r in RESOLUTIONS:
        count=zero_m=zero_shell=zero_alg=non=0
        for _kq,_kg,xq,_xg in partitions(r):
            intr,product,u=tm_cm_ground_map(xq,r.Nmax-2)
            for i,(nr,mr) in enumerate(intr):
                for j,(nq,mq,ng,mg) in enumerate(product):
                    if 0<abs(u[i,j])<1e-12:
                        count+=1;c=polar_tm_coefficient((0,0,nr,mr),(nq,mq,ng,mg),xq)
                        if c.status=='ZERO_BY_EXACT_M_RULE':zero_m+=1
                        elif c.status=='ZERO_BY_EXACT_SHELL_RULE':zero_shell+=1
                        elif c.status.startswith('ZERO'):zero_alg+=1
                        else:non+=1
        rows.append({'resolution':r.label,'historical_subthreshold':count,'EXACT_ZERO_QUADRATURE_NOISE':zero_m+zero_shell+zero_alg,'m_rule':zero_m,'shell_rule':zero_shell,'algebraic':zero_alg,'GENUINE_SMALL_EXACT_NONZERO':non,'UNRESOLVED_BLOCKING':0})
        totals.append(count)
    assert totals==[4032,15840,48048] and all(x['GENUINE_SMALL_EXACT_NONZERO']==0 for x in rows)
    return {'rows':rows,'status':'PASS_ALL_HISTORICAL_SUBTHRESHOLD_ARE_EXACT_ZEROS','historical_threshold':'diagnostic only'}

def circular_cartesian_shell(total:int)->dict[str,Any]:
    circ=[(a,total-a) for a in range(total+1)];cart=[(a,total-a) for a in range(total+1)];M=sp.zeros(total+1)
    for i,(np_,nm) in enumerate(circ):
        for j,(nx,ny) in enumerate(cart):
            v=sp.S(0)
            for r in range(np_+1):
                s=nx-r
                if 0<=s<=nm:
                    v+=sp.binomial(np_,r)*sp.binomial(nm,s)*sp.I**(np_-r)*(-sp.I)**(nm-s)
            M[j,i]=sp.simplify(v*sp.sqrt(sp.factorial(nx)*sp.factorial(ny)/(2**total*sp.factorial(np_)*sp.factorial(nm))))
    return {'shell':total,'circ':circ,'cart':cart,'matrix':M,'unitarity_residual':sp.simplify((M.conjugate().T*M-sp.eye(total+1)).norm())}

@lru_cache(maxsize=1)
def build()->dict[str,Any]:
    c61=c61_preflight();assert c61['status']==C61_STATUS
    residue=residue_reconciliation(); low=circular_cartesian_shell(2)
    assert low['unitarity_residual']==0
    manifests=[]
    for r in RESOLUTIONS:
        for pid,(_kq,_kg,xq,_xg) in enumerate(partitions(r)):
            manifests.append({'resolution':r.label,'partition':pid,'xq':[xq.numerator,xq.denominator],'shell_max':r.Nmax-2,'blocks':[{'shell':N,'shape':[len(_transformed_shell(N)),len(polar_product_shell(N))]} for N in range(r.Nmax-1)]})
    return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'plan':PLAN,'polar_phase':'|n,m>_polar=(-1)^n |n+max(m,0),n+max(-m,0)>_circ','Lz':'L_z=N_+-N_-','rotation':'q†=sqrt(xq) CM†+sqrt(xg) rel†; g†=sqrt(xg) CM†-sqrt(xq) rel†','residue':residue,'low_shell':{'matrix_hash':digest(str(low['matrix'])),'unitarity_residual':str(low['unitarity_residual'])},'manifests':manifests,'no_threshold':True,'no_physical_embedding':True,'no_endpoint_or_contact':True}

def validate_c62(v:dict[str,Any])->bool:return canonical_json(v)==canonical_json(serializable(build())) and v['status']==STATUS
def serializable(v:Any)->Any:
    if isinstance(v,np.ndarray):return {'shape':list(v.shape),'dtype':v.dtype.str,'hash':array_hash(v)}
    if isinstance(v,dict):return {str(k):serializable(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [serializable(x) for x in v]
    return v
def snapshot()->dict[str,Any]:return serializable(build())
def mutate_live_c62(i:int)->dict[str,Any]:
    v=json.loads(canonical_json(snapshot()));c=i%16
    if c==0:v['plan']='quadrature'
    elif c==1:v['polar_phase']='argmax'
    elif c==2:v['Lz']='N_- - N_+'
    elif c==3:v['rotation']='fitted'
    elif c==4:v['residue']['rows'][0]['EXACT_ZERO_QUADRATURE_NOISE']=0
    elif c==5:v['residue']['rows'][1]['GENUINE_SMALL_EXACT_NONZERO']=1
    elif c==6:v['low_shell']['unitarity_residual']='1'
    elif c==7:v['manifests'][0]['xq']=[1,3]
    elif c==8:v['no_threshold']=False
    elif c==9:v['no_physical_embedding']=False
    elif c==10:v['no_endpoint_or_contact']=False
    elif c==11:v['residue']['status']='UNRESOLVED'
    elif c==12:v['next']='C63/IFSUPPORT2'
    elif c==13:v['status']='C62_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY'
    elif c==14:v['low_shell']['matrix_hash']='bad'
    else:v['baseline']='wrong'
    return v
def assert_ready_c62()->dict[str,Any]:
    v=build();assert v['status']==STATUS and [r['historical_subthreshold'] for r in v['residue']['rows']]==[4032,15840,48048];return v
