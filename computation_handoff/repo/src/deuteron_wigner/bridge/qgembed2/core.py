"""C63 fails closed when C62's immutable block artifact contract is absent."""
from __future__ import annotations
from copy import deepcopy
from functools import lru_cache
import json
from pathlib import Path
from typing import Any
from ..qgtm.core import STATUS as C62_STATUS, build as c62_build

ROOT=Path(__file__).resolve().parents[4]
BASELINE='cfe1680c381b9531a88e27571e3898a75f6ba784'
STATUS='C63_QGEMBED_C62_IMPORT_INCOMPLETE'
NEXT='C64/QGTM2 — exact TM artifact and support-certificate integrity completion'
REQUIRED=('expression_hash','support_hash','array_hash','error_bound','runtime_path','basis_order_hash')
def canonical_json(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(',',':'),default=str)
def _read(n:str)->dict[str,Any]:return json.loads((ROOT/'docs'/'next_level'/n).read_text())
def c62_import_audit()->dict[str,Any]:
    readiness=_read('c62_readiness_report.json');contract=_read('c62_c63_qgembed2_import_contract.json');inventory=_read('c62_numerical_object_inventory.json')
    live=c62_build();assert readiness['status']==C62_STATUS==live['status']
    present={k:(k in inventory) for k in REQUIRED}
    return {'C62_status':readiness['status'],'plan':readiness['plan'],'residue_counts':[r['EXACT_ZERO_QUADRATURE_NOISE'] for r in readiness['residue']['rows']],
            'genuine_small':[r['GENUINE_SMALL_EXACT_NONZERO'] for r in readiness['residue']['rows']],
            'unresolved':[r['UNRESOLVED_BLOCKING'] for r in readiness['residue']['rows']],
            'contract_hash_fields':present,'contract_result':contract.get('result'),'inventory_object_count':len(inventory.get('objects',[])),
            'blocker':'C62 committed import artifacts do not serialize each finite-shell block expression/support hash, certified numerical array/error bound, basis-order hash, or runtime path. C63 may not rebuild these mutable values while claiming a read-only import.'}
@lru_cache(maxsize=1)
def preflight()->dict[str,Any]:
    a=c62_import_audit();assert not all(a['contract_hash_fields'].values()) and a['inventory_object_count']==0
    return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'C62_import':a,'unavailable':{'CM_ground_injection':True,'CM_projector':True,'kinematic_embedding':True,'triplet_embedding':True,'historical_adapter':True,'impact_audit':True},'no_threshold':True,'no_endpoint_or_contact':True}
def validate_c63(v:dict[str,Any])->bool:return canonical_json(v)==canonical_json(preflight()) and v['status']==STATUS
def snapshot()->dict[str,Any]:return preflight()
def mutate_live_c63(i:int)->dict[str,Any]:
    v=deepcopy(snapshot());c=i%16
    if c==0:v['C62_import']['C62_status']='bad'
    elif c==1:v['C62_import']['residue_counts'][0]=0
    elif c==2:v['C62_import']['contract_hash_fields']['expression_hash']=True
    elif c==3:v['C62_import']['inventory_object_count']=1
    elif c==4:v['C62_import']['blocker']='none'
    elif c==5:v['unavailable']['CM_ground_injection']=False
    elif c==6:v['unavailable']['triplet_embedding']=False
    elif c==7:v['no_threshold']=False
    elif c==8:v['no_endpoint_or_contact']=False
    elif c==9:v['C62_import']['plan']='quadrature'
    elif c==10:v['C62_import']['genuine_small'][0]=1
    elif c==11:v['C62_import']['unresolved'][0]=1
    elif c==12:v['next']='C64/IFSUPPORT2'
    elif c==13:v['status']='C63_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY'
    elif c==14:v['C62_import']['contract_result']='PASS'
    else:v['baseline']='wrong'
    return v
def assert_fail_closed_c63()->dict[str,Any]:
    v=preflight();assert v['status']==STATUS and not all(v['C62_import']['contract_hash_fields'].values());return v
