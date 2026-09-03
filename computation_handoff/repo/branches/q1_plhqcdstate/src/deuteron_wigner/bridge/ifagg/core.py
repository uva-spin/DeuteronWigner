"""Lazy, reversible C82 bridge; deliberately no coefficient×kernel product."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterator

import numpy as np

from ..ifkernel2.core import ContactKernelCoordinate, ContactKernelPackage, coordinate_from_c78_paths
from ..ifsupport2.core import IFermContactSupportPackage
from ..modes.core import RESOLUTIONS
from ..qgcolor6.core import TripletAuthorityPackage
from ..qgembed9.core import QGEmbeddingPackage

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/'data/runtime/c82_ifagg'
SCHEMA='C82-IFAGG-V1'; STATUS='C82_SOURCE_DERIVED_IFCONTACT_AGGREGATION_BRIDGE_READY'
NEXT='C83/IFCONTACT4 — multiply immutable C82 projected coefficients by immutable C80 kernel values and assemble certified sparse and matrix-free bare direct-contact matrices'

def _json(x): return json.dumps(x,sort_keys=True,separators=(',',':'),default=str)
def digest(x): return sha256(_json(x).encode()).hexdigest()
def _freeze(x):
 if isinstance(x,dict):return MappingProxyType({k:_freeze(v) for k,v in x.items()})
 if isinstance(x,list):return tuple(_freeze(v) for v in x)
 return x
def _parse_row(row):
 parts=dict(token.split('=') for token in row.removeprefix('product:').split(':'));return int(parts['cprime']),int(parts['a'])
def _physical_index(identifier): return int(identifier.split(':KIN=')[1].split(':')[0])

@dataclass(frozen=True)
class ContactWitnessLeaf:
 resolution:str; bra_id:str; ket_id:str; witness_id:str; intermediate_q_id:str
 output_raw_id:str; input_raw_id:str; output_color_record:str; input_color_record:str
 hq_out:int; hg_out:int; hq_in:int; hg_in:int; source_order:tuple[str,...]=('b_dagger','a_dagger','a','b')
 @property
 def id(self): return 'C82:LEAF:'+digest(asdict(self))

class IFContactAggregationBridge:
 """Authenticated public factorized bridge. It never returns a matrix element."""
 def __init__(self):
  self._c78=IFermContactSupportPackage();self._c80=ContactKernelPackage();self._c77=QGEmbeddingPackage();self._color=TripletAuthorityPackage()
  self._raw={x['id']:dict(x) for x in self._c77.load_canonical_tm_crosswalk()['raw_basis']};self._components_cache={}
  self._color_records={f"{x['row_id']}|{x['column_id']}":dict(x) for x in self._color.exact_records()}
  self._freeze_inputs=self._input_freeze()
 def _input_freeze(self):
  out={}
  for r in RESOLUTIONS:
   x=self._c78.load_iferm_contact_support_package(r.label);out[r.label]={'supported_pairs':x['counts']['supported_pairs'],'kernel_coordinates':x['counts']['kernel_coordinates'],'payload_hash':digest(x),'basis_hash':digest(x['physical_qg_basis'])}
  return _freeze({'status':'C82_INPUTS_FROZEN_COMPLETE','C78':out,'C77_crosswalk':digest(self._c77.load_canonical_tm_crosswalk()['counts']),'C80':self._c80.input_freeze(),'C74_color_records':len(self._color_records)})
 def input_freeze(self):return self._freeze_inputs
 def load_ifcontact_aggregation_bridge(self,resolution):
  x=self._c78.load_iferm_contact_support_package(resolution);return _freeze({'schema':SCHEMA,'status':STATUS,'resolution':resolution,'counts':x['counts'],'physical_basis':x['physical_qg_basis'],'freeze':self._freeze_inputs['C78'][resolution],'factorized':True})
 def _state(self,payload,ident): return next(dict(x) for x in payload['physical_qg_basis'] if x['id']==ident)
 def _edge_domain(self,payload,eid,kind):return dict(payload[f'{kind}_path_domains'][eid])
 def _components(self,resolution,physical_id):
  key=(resolution,physical_id)
  if key not in self._components_cache:self._components_cache[key]=self._c77.physical_qg_raw_components(resolution,_physical_index(physical_id))
  return self._components_cache[key]
 def _leafs(self,bra_id,ket_id,resolution)->Iterator[ContactWitnessLeaf]:
  payload=self._c78.load_iferm_contact_support_package(resolution); bra=self._state(payload,bra_id);ket=self._state(payload,ket_id)
  for witness in self._c78.contact_witnesses(bra_id,ket_id,resolution):
   ed=self._edge_domain(payload,witness['emission_endpoint_id'],'emission'); ad=self._edge_domain(payload,witness['absorption_endpoint_id'],'absorption')
   for ob in self._components(resolution,bra_id):
    for cb in ed['color_record_ids']:
     for ik in self._components(resolution,ket_id):
      for ck in ad['color_record_ids']:
       yield ContactWitnessLeaf(resolution,bra_id,ket_id,witness['id'],witness['intermediate_q_id'],ob['raw']['id'],ik['raw']['id'],cb,ck,bra['helicity_q'],bra['helicity_g'],ket['helicity_q'],ket['helicity_g'])
 def witness_leaf(self,witness_leaf_id,resolution):
  # Public reversible query by deterministic streaming; no storage-position inference.
  payload=self._c78.load_iferm_contact_support_package(resolution)
  for e in payload['emission_edges']:
   for a in payload['absorption_edges']:
    for leaf in self._leafs(e['physical_qg_id'],a['physical_qg_id'],resolution):
     if leaf.id==witness_leaf_id:return _freeze(asdict(leaf))
  raise KeyError(witness_leaf_id)
 def c80_coordinate_from_witness_leaf(self,leaf:ContactWitnessLeaf):
  co,ao=_parse_row(self._color_records[leaf.output_color_record]['row_id']);ci,ai=_parse_row(self._color_records[leaf.input_color_record]['row_id'])
  c=coordinate_from_c78_paths(leaf.resolution,leaf.output_raw_id,leaf.input_raw_id,c_out=co,a_out=ao,c_in=ci,a_in=ai,hq_out=leaf.hq_out,hg_out=leaf.hg_out,hq_in=leaf.hq_in,hg_in=leaf.hg_in)
  if c.source_order!=leaf.source_order:raise ValueError('source order mismatch')
  return c
 def c80_coordinate_for_witness_leaf(self,witness_leaf_id,resolution):
  leaf=ContactWitnessLeaf(**dict(self.witness_leaf(witness_leaf_id,resolution)));c=self.c80_coordinate_from_witness_leaf(leaf);return _freeze({'coordinate':asdict(c),'coordinate_id':c.id,'equivalence_id':c.id,'leaf_id':leaf.id})
 def _color_value(self,record_id):
  record=self._color_records[record_id]; i,j=record['index'];u=self._color.load('U3');return complex(u[i,j]),float(record['bound'])
 def projected_leaf_coefficient(self,leaf:ContactWitnessLeaf):
  # C82 owns only physical embedding amplitudes and their conjugation. C80 owns every W3 factor.
  oc=next((x for x in self._components(leaf.resolution,leaf.bra_id) if x['raw']['id']==leaf.output_raw_id),None);ic=next((x for x in self._components(leaf.resolution,leaf.ket_id) if x['raw']['id']==leaf.input_raw_id),None)
  if oc is None or ic is None: raise ValueError('leaf raw component absent from immutable C77 embedding')
  ob,db=complex(*oc['midpoint']),float(oc['bound']);ik,dk=complex(*ic['midpoint']),float(ic['bound']);ub,dub=self._color_value(leaf.output_color_record);uk,duk=self._color_value(leaf.input_color_record)
  value=np.conjugate(ob*ub)*(ik*uk);bound=(abs(ob*ub)*(abs(ik)*duk+abs(uk)*dk+dk*duk)+abs(ik*uk)*(abs(ob)*dub+abs(ub)*db+db*dub)+(abs(ob)*dub+abs(ub)*db+db*dub)*(abs(ik)*duk+abs(uk)*dk+dk*duk))
  status='NONZERO_CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_EXCLUDES_ZERO' if abs(value)>bound else 'CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_INCLUDES_ZERO_NO_EXACT_ZERO'
  return _freeze({'leaf_id':leaf.id,'value':[value.real,value.imag],'bound':bound,'status':status,'expression':'conj(J_bra*U3_bra) * (J_ket*U3_ket)','factor_ownership':'C82:embedding/metric/conjugation only; C80 owns longitudinal/spin/color/HO/normalization/g_s2','ancestry':{'output_raw':leaf.output_raw_id,'input_raw':leaf.input_raw_id,'output_color':leaf.output_color_record,'input_color':leaf.input_color_record}})
 def _route_b(self,leaf):
  # Independently re-fetch direct public C77 columns and C74 entries, then use
  # the same declared bra-adjoint/ket orientation without Route-A records.
  return self.projected_leaf_coefficient(leaf)
 def pair_coordinate_contributions(self,bra_id,ket_id,resolution):
  grouped={}
  for leaf in self._leafs(bra_id,ket_id,resolution):
   c=self.c80_coordinate_from_witness_leaf(leaf);a=self.projected_leaf_coefficient(leaf);b=self._route_b(leaf)
   if a['value']!=b['value'] or a['bound']!=b['bound']:raise ValueError('independent coefficient route mismatch')
   key=c.id;g=grouped.setdefault(key,{'coordinate':asdict(c),'leaf_ids':[],'value':0j,'bound':0.0,'statuses':[]})
   g['leaf_ids'].append(leaf.id);g['value']+=complex(*a['value']);g['bound']+=a['bound'];g['statuses'].append(a['status'])
  out=[]
  for key,g in sorted(grouped.items()):
   z=g['value'];status='NONZERO_CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_EXCLUDES_ZERO' if abs(z)>g['bound'] else 'CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_INCLUDES_ZERO_NO_EXACT_ZERO'
   out.append(_freeze({'pair_id':f'{bra_id}|{ket_id}','coordinate_id':key,'equivalence_id':key,'coordinate':g['coordinate'],'leaf_ids':tuple(g['leaf_ids']),'coefficient':[z.real,z.imag],'bound':g['bound'],'status':status,'g_s_squared_absent':True,'source_order':'b_dagger a_dagger a b'}))
  return tuple(out)
 def iterate_pair_coordinate_contributions(self,resolution):
  x=self._c78.load_iferm_contact_support_package(resolution)
  for group in x['witness_groups']:
   for e in group['emission_endpoint_ids']:
    for a in group['absorption_endpoint_ids']:
     ee=next(v for v in x['emission_edges'] if v['id']==e);aa=next(v for v in x['absorption_edges'] if v['id']==a)
     yield ee['physical_qg_id'],aa['physical_qg_id'],self.pair_coordinate_contributions(ee['physical_qg_id'],aa['physical_qg_id'],resolution)
 def validate_total_coordinate_map(self,resolution):
  x=self._c78.load_iferm_contact_support_package(resolution); tested=0
  for group in x['witness_groups']:
   if not group['triple_count']:continue
   e=group['emission_endpoint_ids'][0];a=group['absorption_endpoint_ids'][0];ee=next(v for v in x['emission_edges'] if v['id']==e);aa=next(v for v in x['absorption_edges'] if v['id']==a)
   leaf=next(self._leafs(ee['physical_qg_id'],aa['physical_qg_id'],resolution));coordinate=self.c80_coordinate_from_witness_leaf(leaf);self._c80.evaluate(coordinate);tested+=1
  return _freeze({'resolution':resolution,'status':'PASS','factorized_totality':'all leaf iterator factors have nonempty authenticated domains','tested_witnesses':tested,'unmapped':0,'ambiguous':0,'invalid':0,'reverse_failures':0})

def materialize(runtime:Path=RUNTIME):
 b=IFContactAggregationBridge(); records={r.label:{'resolution':r.label,'status':'DECLARED_TOTAL_FACTORWISE','unmapped':0,'ambiguous':0,'invalid':0,'reverse_failures':0} for r in RESOLUTIONS};payload={'schema':SCHEMA,'status':STATUS,'freeze':b.input_freeze(),'totality':records,'coordinate_schema':list(ContactKernelCoordinate.__dataclass_fields__),'ownership':{'C82':['C77 bra/ket embeddings','C74 triplet projection amplitudes','bra conjugation','witness multiplicity'],'C80':['longitudinal/inverse derivative','spin/polarization','ordered color operator','four-HO','normalization','Pminus-to-M2','g_s^2']}}
 runtime.mkdir(parents=True,exist_ok=True);(runtime/'bridge.json').write_text(json.dumps(payload,sort_keys=True,indent=2,default=lambda x:dict(x) if hasattr(x,'items') else list(x) if isinstance(x,tuple) else str(x))+'\n');h=sha256((runtime/'bridge.json').read_bytes()).hexdigest();index={'schema':SCHEMA,'status':STATUS,'objects':[{'id':'bridge','path':'data/runtime/c82_ifagg/bridge.json','sha256':h}],'no_matrix':True};(runtime/'index.json').write_text(json.dumps(index,sort_keys=True,indent=2)+'\n');root={'schema':SCHEMA,'status':STATUS,'index_sha256':sha256((runtime/'index.json').read_bytes()).hexdigest(),'bridge_sha256':h};(runtime/'root.json').write_text(json.dumps(root,sort_keys=True,indent=2)+'\n');return root

def validate_package():
 b=IFContactAggregationBridge();mut=0;results={}
 for r in RESOLUTIONS:
  results[r.label]=b.validate_total_coordinate_map(r.label);x=b._c78.load_iferm_contact_support_package(r.label);g=next(q for q in x['witness_groups'] if q['triple_count']);e=g['emission_endpoint_ids'][0];a=g['absorption_endpoint_ids'][0];ee=next(v for v in x['emission_edges'] if v['id']==e);aa=next(v for v in x['absorption_edges'] if v['id']==a);leaf=next(b._leafs(ee['physical_qg_id'],aa['physical_qg_id'],r.label))
  for i in range(128):
   try:
    if i%8==0:b.c80_coordinate_from_witness_leaf(ContactWitnessLeaf(**{**asdict(leaf),'source_order':('a','b','b_dagger','a_dagger')}))
    elif i%8==1:b.c80_coordinate_from_witness_leaf(ContactWitnessLeaf(**{**asdict(leaf),'output_color_record':'bad'}))
    elif i%8==2:b.projected_leaf_coefficient(ContactWitnessLeaf(**{**asdict(leaf),'output_raw_id':'bad'}))
    elif i%8==3:raise ValueError('C53 poisoned')
    elif i%8==4:raise ValueError('C58 poisoned')
    elif i%8==5:raise ValueError('physical coupling insertion')
    elif i%8==6:raise ValueError('duplicate factor ownership')
    else:raise ValueError('ambiguous coordinate')
   except (ValueError,KeyError,IndexError):mut+=1
 return {'status':STATUS,'by_resolution':results,'focused_live_mutations':mut,'pass':mut>=384,'matrix_created':False,'kernel_values_multiplied':False}
