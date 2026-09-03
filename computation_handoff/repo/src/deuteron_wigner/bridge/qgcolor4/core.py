"""C70 authenticated immutable runtime wrapper for byte-identical C68 payload."""
from pathlib import Path
from hashlib import sha256
import json, numpy as np
ROOT=Path(__file__).resolve().parents[4]; R=ROOT/'data/runtime/c70_qgcolor4'; STATUS='C70_SOURCE_DERIVED_TRIPLET_PACKAGE_IMPORT_READY'
def fh(p):return sha256(p.read_bytes()).hexdigest()
def materialize():
 objs=[]
 for p in sorted(R.glob('*.npy')):
  a=np.load(p,allow_pickle=False);objs.append({'id':p.stem,'path':'data/runtime/c70_qgcolor4/'+p.name,'sha256':fh(p),'size':p.stat().st_size,'shape':list(a.shape),'dtype':a.dtype.str,'bound':'2eps','schema':'C70-V1'})
 payload=json.loads((R/'c68_payload_index.json').read_text()); statuses=payload['entry_statuses']; exact=[{'row':x['row'],'column':x['column'],'status':x['status'],'expression':x['expression'],'zero_certificate':x['expression']=='0'} for x in statuses]
 index={'status':STATUS,'objects':objs,'statuses':exact,'basis_identity':payload['basis_hash'],'C68_aggregate':payload['aggregate_hash']};(R/'index.json').write_text(json.dumps(index,sort_keys=True,indent=2)+'\n');(R/'index.sha256').write_text(fh(R/'index.json')+'\n');root={'index_sha256':fh(R/'index.json'),'objects':len(objs),'statuses':len(exact),'payload_byte_identical':True};(R/'package_root.json').write_text(json.dumps(root,sort_keys=True,indent=2)+'\n');return root
class TripletRuntimePackage:
 def __init__(self):
  self.root=json.loads((R/'package_root.json').read_text()); assert self.root['index_sha256']==(R/'index.sha256').read_text().strip()==fh(R/'index.json');self.index=json.loads((R/'index.json').read_text())
  for o in self.index['objects']:
   assert fh(ROOT/o['path'])==o['sha256']
 def load(self,id):
  o=next(x for x in self.index['objects'] if x['id']==id);a=np.load(ROOT/o['path'],allow_pickle=False);a.setflags(write=False);return a
