"""C60 fail-closed audit: C47 numerical TM/CM maps cannot define exact paths."""
from __future__ import annotations
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import json
from typing import Any
import numpy as np

from ..basis1.core import partitions, q_basis, tm_cm_ground_map
from ..iferm2.core import STATUS as C59_STATUS, preflight as c59_preflight
from ..ifnorm2.core import QG_PLAN, STATUS as C58_STATUS, build_contraction, serializable
from ..ifreg.core import THRESHOLD
from ..modes.core import RESOLUTIONS, array_hash

BASELINE="3174722ee1fc2d0045ee10273b4338f335b262b9"
STATUS="C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE"
NEXT="C61/IFQGEMBED — raw product, intrinsic/CM, CM-ground, and triplet endpoint-map completion"

def canonical_json(value:Any)->str: return json.dumps(value,sort_keys=True,separators=(',',':'),default=str)
def digest(value:Any)->str: return sha256(canonical_json(value).encode()).hexdigest()

def import_predecessors() -> dict[str,Any]:
    c59=c59_preflight(); c58=build_contraction()
    assert c59['status']==C59_STATUS and c58['status']==C58_STATUS
    assert c58['qg_sector']['selected']==QG_PLAN
    rows=[]
    for rec, modes in zip(c58['records'],(4216,8330,14484)):
        assert rec['matrix'].shape==(6,6) and int(np.count_nonzero(rec['matrix']))==6 and len(rec['ledger'])==modes
        rows.append({'resolution':rec['resolution'],'shape':[6,6],'nnz':6,'mode_count':modes,'array_hash':array_hash(rec['matrix'])})
    return {'C59_status':c59['status'],'C58_status':c58['status'],'C58_qg_SII':c58['qg_sector']['status'],'C58_q_records':rows,'read_only':True}

def embedding_audit() -> dict[str,Any]:
    records=[]
    for r in RESOLUTIONS:
        maps=[]; sub=0; smallest=None
        for pid,(_kq,_kg,xq,_xg) in enumerate(partitions(r)):
            intr,product,u=tm_cm_ground_map(xq,r.Nmax-2)
            flat=np.abs(u.ravel()); n=int(np.count_nonzero((flat>0)&(flat<THRESHOLD)))
            sub+=n
            vals=flat[(flat>0)&(flat<THRESHOLD)]
            if vals.size: smallest=float(vals.min()) if smallest is None else min(smallest,float(vals.min()))
            maps.append({'partition':pid,'raw_dimension':len(product),'intrinsic_CM_ground_dimension':len(intr),'shape':list(u.shape),'array_hash':array_hash(u),'subthreshold_nonzero_entries':n})
        records.append({'resolution':r.label,'intermediate_q_dimension':len(q_basis(r)),'physical_qg_dimension':sum(m['intrinsic_CM_ground_dimension']*12 for m in maps),'maps':maps,'subthreshold_nonzero_entries':sub,'smallest_nonzero_float':smallest})
    assert [x['subthreshold_nonzero_entries'] for x in records]==[4032,15840,48048]
    return {'status':STATUS,'threshold_used_by_C57':THRESHOLD,'records':records,
            'blocker':'C47 TM/CM maps are quadrature-derived complex floating arrays. Their structural support was previously threshold-classified, but C60 requires exact raw-component and projected-cancellation semantics without a tolerance.',
            'forbidden_repairs':['reuse C57 threshold as exact-zero proof','treat all nonzero floats as exact raw paths','threshold a direct-contact endpoint relation','collapse raw and physical support']}

@lru_cache(maxsize=1)
def preflight()->dict[str,Any]:
    pred=import_predecessors(); emb=embedding_audit()
    return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'predecessors':pred,'embedding_audit':emb,
            'source_topology':{'C55_direct_term':'b_dagger a_dagger a b','endpoint_roles':'absorption/emission not built because exact physical embedding is blocking','C57_relation':'canonical q-to-qg support only; not relabeled as direct-contact support'},
            'unavailable':{'raw_physical_embedding':True,'absorption_relation':True,'emission_relation':True,'witness_relation':True,'boolean_adjacency':True,'direct_contact_kernel':True,'direct_contact_matrix':True},
            'no_C53_values':True,'no_C58_values_as_support':True,'no_anonymous_mask_product':True,'no_direct_contact_value':True}

def validate_c60(value:dict[str,Any])->bool: return canonical_json(value)==canonical_json(serializable(preflight())) and value['status']==STATUS
def snapshot()->dict[str,Any]: return serializable(preflight())
def mutate_live_c60(i:int)->dict[str,Any]:
    v=deepcopy(snapshot()); c=i%16
    if c==0:v['predecessors']['C58_q_records'][0]['array_hash']='bad'
    elif c==1:v['predecessors']['C58_qg_SII']='ZERO'
    elif c==2:v['embedding_audit']['threshold_used_by_C57']=0
    elif c==3:v['embedding_audit']['records'][0]['subthreshold_nonzero_entries']=0
    elif c==4:v['embedding_audit']['blocker']='exact embedding available'
    elif c==5:v['embedding_audit']['forbidden_repairs']=[]
    elif c==6:v['source_topology']['C55_direct_term']='a a_dagger'
    elif c==7:v['source_topology']['C57_relation']='direct contact'
    elif c==8:v['unavailable']['raw_physical_embedding']=False
    elif c==9:v['unavailable']['absorption_relation']=False
    elif c==10:v['no_C53_values']=False
    elif c==11:v['no_C58_values_as_support']=False
    elif c==12:v['no_anonymous_mask_product']=False
    elif c==13:v['no_direct_contact_value']=False
    elif c==14:v['next']='C61/IFCONTACT'
    else:v['status']='C60_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY'
    return v

def assert_fail_closed_c60()->dict[str,Any]:
    v=preflight(); assert v['status']==STATUS
    assert [x['subthreshold_nonzero_entries'] for x in v['embedding_audit']['records']]==[4032,15840,48048]
    assert all(v['unavailable'].values())
    return v
