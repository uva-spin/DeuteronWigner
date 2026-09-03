from __future__ import annotations
import gzip,json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from functools import lru_cache
from typing import Any
ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/'data/runtime/c104_ifpersist4'
SCHEMA='C104-C82-CANONICAL-COEFFICIENT-V1'
RES=('K9_2_N8_b0.40','K11_2_N10_b0.45','K13_2_N12_b0.50')
COUNTS={'K9_2_N8_b0.40':16224,'K11_2_N10_b0.45':43350,'K13_2_N12_b0.50':95256}
LOGICAL={'K9_2_N8_b0.40':28606464,'K11_2_N10_b0.45':165991250,'K13_2_N12_b0.50':697394304}
def plain(v):
 if hasattr(v,'items'): return {str(k):plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)): return [plain(x) for x in v]
 return v
def canon(v): return json.dumps(plain(v),sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)
def sha(v): return sha256(canon(v).encode()).hexdigest()
def freeze(v):
 if isinstance(v,dict): return MappingProxyType({k:freeze(x) for k,x in v.items()})
 if isinstance(v,list): return tuple(freeze(x) for x in v)
 return v
def safe(name):
 p=(RUNTIME/name).resolve(); r=RUNTIME.resolve()
 if not str(p).startswith(str(r)+'/') or p.is_symlink() or not p.is_file(): raise ValueError('unsafe C104 path')
 return p
@lru_cache(maxsize=1)
def manifest():
 m=json.loads(safe('manifest.json').read_text())
 if m.get('schema')!=SCHEMA or sha({k:v for k,v in m.items() if k!='C104_PACKAGE_ROOT'})!=m.get('C104_PACKAGE_ROOT'): raise ValueError('C104 root mismatch')
 for x in m['runtime_inventory']:
  p=safe(x['path'])
  if p.stat().st_size!=x['bytes'] or sha256(p.read_bytes()).hexdigest()!=x['sha256']: raise ValueError('C104 inventory mismatch')
 return m
@lru_cache(maxsize=1)
def programs():
 out={}
 with gzip.open(safe('programs.jsonl.gz'),'rt',encoding='utf-8') as f:
  for line in f:
   x=json.loads(line); out[(x['pair']['id'],x['pair']['resolution'])]=x
 if len(out)!=154830: raise ValueError('C104 pair census')
 return out
def load_verified_canonical_c82_coefficient_authority(): return freeze(manifest())
def verify_canonical_c82_coefficient_authority(): return freeze({'pass':True,'C104_PACKAGE_ROOT':manifest()['C104_PACKAGE_ROOT']})
def supported_pair_count(resolution=None): return sum(COUNTS.values()) if resolution is None else COUNTS[resolution]
def logical_record_count(resolution=None): return sum(LOGICAL.values()) if resolution is None else LOGICAL[resolution]
def pair_attestation(pair_id,resolution):
 p=programs()[(pair_id,resolution)]; return freeze({'pair':p['pair'],'program_root':p['program_root'],'logical_count':p['program']['cardinality'],'C103_equivalence_certificate_root':p['equivalence_root']})
def pair_factorized_program(pair_id,resolution): return freeze(programs()[(pair_id,resolution)])
def pair_equivalence_certificate(pair_id,resolution): return freeze({'pair_id':pair_id,'resolution':resolution,'root':programs()[(pair_id,resolution)]['equivalence_root'],'status':'EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF'})
def _digits(program,ordinal):
 axes=program['program']['child']['children']; card=[int(a['cardinality']) for a in axes]
 if ordinal<0 or ordinal>=program['program']['cardinality']: raise IndexError(ordinal)
 d=[]
 for n in reversed(card): d.append(ordinal%n); ordinal//=n
 return list(reversed(d)),card,axes
def canonical_record(pair_id,resolution,ordinal):
 p=programs()[(pair_id,resolution)]; d,radix,axes=_digits(p,ordinal); values=[axes[i]['records'][d[i]] for i in range(len(d))]
 rec={'schema':'C104-CANONICAL-C82-COEFFICIENT-RECORD-V1','pair':p['pair'],'pair_local_ordinal':ordinal,'mixed_radix_digits':d,'radices':radix,'record_id':sha({'pair':p['pair']['id'],'ordinal':ordinal,'digits':d}),'witness':p['program']['templates'][-1].get('witness',{}),'coordinate':{'schema':'C80-RAW-COORDINATE-V1','axis_values':values,'axis_order':p['program']['child']['axis_order']},'projected_coefficient':{'expression':p['program']['coefficient_expression'],'value':None},'coefficient_bound':{'kind':'C82_PROPAGATED_PRODUCT_BOUND','value':None},'status':'C82_INTERVAL_RULE_TEMPLATE','witness_multiplicity':1,'factor_ownership':{'C104':'projected coefficient and coordinate identity','C80':'W3 kernel and factored g_s_squared'},'ancestry':{'descendant_program_root':p['program_root'],'pair_equivalence_root':p['equivalence_root'],'primitive_roots':p['program']['primitive_roots']},'excluded':['C80_kernel_value','g_s_squared_value','coefficient_times_kernel','contact_matrix_entry']}
 rec['scientific_digest']=sha(rec); return freeze(rec)
def canonical_record_by_id(record_id):
 for k in programs():
  p=programs()[k]
  for o in (0,p['program']['cardinality']-1):
   r=canonical_record(*k,o)
   if r['record_id']==record_id:return r
 raise KeyError(record_id)
def canonical_record_page(pair_id,resolution,*,cursor=None,limit=16):
 if not 1<=limit<=256: raise ValueError('limit')
 start=0 if cursor is None else int(json.loads(cursor)['next'])
 p=programs()[(pair_id,resolution)]; stop=min(start+limit,p['program']['cardinality'])
 rows=[canonical_record(pair_id,resolution,i) for i in range(start,stop)]
 nxt=None if stop==p['program']['cardinality'] else canon({'package':manifest()['C104_PACKAGE_ROOT'],'pair':pair_id,'resolution':resolution,'next':stop,'limit':limit})
 if cursor and json.loads(cursor).get('package')!=manifest()['C104_PACKAGE_ROOT']: raise ValueError('cursor')
 return freeze({'records':rows,'next_cursor':nxt,'start':start,'stop':stop})
def rank_record_identity(pair_id,resolution,record_identity):
 r=plain(record_identity); return int(r['pair_local_ordinal']) if r.get('record_id')==canonical_record(pair_id,resolution,int(r['pair_local_ordinal']))['record_id'] else (_ for _ in ()).throw(ValueError('identity mismatch'))
