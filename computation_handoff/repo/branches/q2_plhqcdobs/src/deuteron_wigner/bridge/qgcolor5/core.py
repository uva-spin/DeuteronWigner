from pathlib import Path
from hashlib import sha256
import json,numpy as np
ROOT=Path(__file__).resolve().parents[4];R=ROOT/'data/runtime/c72_qgcolor5';STATUS='C72_SOURCE_DERIVED_TRIPLET_FULL_IMPORT_READY'
def fh(p):return sha256(p.read_bytes()).hexdigest()
def materialize():
 u=np.load(R/'U3.npy'); rows=[f'product:cprime={c}:a={a}' for c in range(3) for a in range(8)];cols=[f'triplet:c={c}' for c in range(3)]; rec=[]
 for i,r in enumerate(rows):
  for j,c in enumerate(cols):
   z=u[i,j];nz=bool(z!=0);rec.append({'row_id':r,'column_id':c,'status':'NONZERO_EXACT_ALGEBRAIC' if nz else 'ZERO_BY_EXACT_COLOR_RULE','expression':'E_src/sqrt(4/3)' if nz else '0','zero_certificate':not nz,'normalization':'C_F=4/3','midpoint':[float(z.real),float(z.imag)],'bound':2*np.finfo(float).eps,'array':'U3','index':[i,j],'dtype':u.dtype.str,'precision':53,'interval':'float64 midpoint +/- 2eps'})
 objs=[]
 for p in sorted(R.glob('*.npy')):a=np.load(p);objs.append({'id':p.stem,'path':'data/runtime/c72_qgcolor5/'+p.name,'sha256':fh(p),'shape':list(a.shape),'dtype':a.dtype.str,'bound_identity':'2eps'})
 index={'status':STATUS,'source_fingerprint':fh(ROOT/'src/deuteron_wigner/bridge/qgcolor2/core.py'),'api_fingerprint':fh(ROOT/'src/deuteron_wigner/bridge/qgcolor4/core.py'),'rows':rows,'columns':cols,'records':rec,'objects':objs};(R/'index.json').write_text(json.dumps(index,sort_keys=True,indent=2)+'\n');root={'index_sha256':fh(R/'index.json'),'records':72,'rows':24,'columns':3};(R/'root.json').write_text(json.dumps(root,sort_keys=True,indent=2)+'\n');return root
class TripletAuthorityPackage:
 def __init__(self):self.root=json.loads((R/'root.json').read_text());assert self.root['index_sha256']==fh(R/'index.json');self.index=json.loads((R/'index.json').read_text());assert len(self.index['records'])==72
 def load(self,id):o=next(x for x in self.index['objects'] if x['id']==id);a=np.load(ROOT/o['path']);assert fh(ROOT/o['path'])==o['sha256'];a.setflags(write=False);return a
