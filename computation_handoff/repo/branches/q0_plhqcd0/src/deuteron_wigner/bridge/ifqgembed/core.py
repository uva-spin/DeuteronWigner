"""C61 fails closed before an exact embedding can inherit a quadrature phase."""
from __future__ import annotations
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import inspect,json
from typing import Any
from ..ifsupport.core import STATUS as C60_STATUS, preflight as c60_preflight
from ..basis1 import core as basis1
from ..modes.core import RESOLUTIONS

BASELINE='0d74c218e304a9bdb9c13eaaaf8b0abdab2531f6'
STATUS='C61_EXACT_TM_ALGEBRA_INCOMPLETE'
NEXT='C62/QGTM — circular-ladder, Cartesian, or generating-function coefficient completion'

def canonical_json(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(',',':'),default=str)
def digest(v:Any)->str:return sha256(canonical_json(v).encode()).hexdigest()

def predecessor_audit()->dict[str,Any]:
 c60=c60_preflight(); assert c60['status']==C60_STATUS
 return {'C60_status':c60['status'],'subthreshold_counts':[4032,15840,48048],
         'C58_read_only':c60['predecessors']['read_only'],'C58_records':c60['predecessors']['C58_q_records']}

def phase_formula_audit()->dict[str,Any]:
 source=inspect.getsource(basis1.polar_to_cart_shell)+inspect.getsource(basis1.tm_blocks)
 assert 'roots_hermite' in source and 'argmax' in source
 return {'status':STATUS,'historical_algorithm':'polar_to_cart_shell obtains polar/cartesian amplitudes by Gauss-Hermite quadrature and then aligns each polar row to its numerically largest Cartesian component.',
         'exact_source_phase_needed':'An exact polar-C45 to circular-ladder phase map, including creation-operator ordering, must be locked before algebraic TM expressions can be assigned to the inherited raw/physical basis order.',
         'evidence':['basis1.polar_to_cart_shell uses scipy roots_hermite numerical quadrature','basis1.polar_to_cart_shell applies exp(-i angle(result[i,j])) at j=argmax(abs(result[i]))','C47 does not serialize an exact phase expression for that per-row alignment'],
         'candidate_plan':'QGEMBED-CIRCULAR-LADDER-ALGEBRA','candidate_formula':'two exact one-dimensional brackets for n_plus,n_minus after exact c=sqrt(x_q), s=sqrt(x_g) rotation',
         'blocker':'The candidate formula is phase-ambiguous relative to the inherited C47 raw/physical basis ordering. Choosing a phase by matching floating quadrature data would violate C61 exact-authority and poisoning requirements.',
         'prohibited':['infer polar/circular phase from floating argmax rows','fit a phase to C47 arrays','use 1e-12 support threshold','declare a quadrature near-zero exact']}

@lru_cache(maxsize=1)
def preflight()->dict[str,Any]:
 return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'predecessors':predecessor_audit(),'phase_audit':phase_formula_audit(),
         'exact_longitudinal':'Fractions are available in C47 partitions but no exact TM coefficient is issued before the phase contract.',
         'unavailable':{'exact_tm_coefficients':True,'CM_ground_projector':True,'kinematic_embedding':True,'triplet_embedding':True,'residue_classification':True,'impact_audit':True},
         'no_threshold_support':True,'no_endpoint_relation':True,'no_contact_value_or_matrix':True,'no_C53_values':True}
def serializable(v:Any)->Any:return v
def validate_c61(v:dict[str,Any])->bool:return canonical_json(v)==canonical_json(preflight()) and v['status']==STATUS
def snapshot()->dict[str,Any]:return preflight()
def mutate_live_c61(i:int)->dict[str,Any]:
 v=deepcopy(snapshot());c=i%16
 if c==0:v['predecessors']['C60_status']='READY'
 elif c==1:v['predecessors']['subthreshold_counts'][0]=0
 elif c==2:v['phase_audit']['historical_algorithm']='exact'
 elif c==3:v['phase_audit']['evidence'][0]='symbolic'
 elif c==4:v['phase_audit']['blocker']='none'
 elif c==5:v['phase_audit']['prohibited']=[]
 elif c==6:v['phase_audit']['candidate_plan']='quadrature'
 elif c==7:v['unavailable']['exact_tm_coefficients']=False
 elif c==8:v['unavailable']['kinematic_embedding']=False
 elif c==9:v['no_threshold_support']=False
 elif c==10:v['no_endpoint_relation']=False
 elif c==11:v['no_contact_value_or_matrix']=False
 elif c==12:v['no_C53_values']=False
 elif c==13:v['exact_longitudinal']='binary float'
 elif c==14:v['next']='C62/IFSUPPORT2'
 else:v['status']='C61_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY'
 return v
def assert_fail_closed_c61()->dict[str,Any]:
 v=preflight(); assert v['status']==STATUS and all(v['unavailable'].values());return v
