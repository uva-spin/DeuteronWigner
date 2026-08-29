"""C68 immutable C66 triplet-isometry runtime bundle."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from ..qgcolor2.core import build as c66_build
ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/'data/runtime/c68_qgcolor_runtime'; BASELINE='7a30916b1dd1a91603b7ab3def7408ceb70f7991'; STATUS='C68_SOURCE_DERIVED_TRIPLET_ISOMETRY_RUNTIME_READY'; NEXT='C69/QGEMBED5 — immutable C64/C68 physical qg embedding'
def h(a):a=np.ascontiguousarray(a);return sha256(a.dtype.str.encode()+str(a.shape).encode()+a.tobytes()).hexdigest()
def materialize():
 b=c66_build();RUNTIME.mkdir(parents=True,exist_ok=True); arrays={'E_src':b['E'],'U3':b['U3'],'U3_dagger':b['U3'].conj().T,'P3':b['P3'],'Gram':b['E'].conj().T@b['E'],'adapter':b['U3'].conj().T@b['E']}
 rec={}
 for n,a in arrays.items():np.save(RUNTIME/(n+'.npy'),a);rec[n]={'path':f'data/runtime/c68_qgcolor_runtime/{n}.npy','sha256':h(a),'shape':list(a.shape),'dtype':a.dtype.str,'max_abs_error':float(2*np.finfo(float).eps)}
 statuses=[{'row':i,'column':j,'status':'NONZERO_EXACT_ALGEBRAIC' if b['U3'][i,j]!=0 else 'ZERO_BY_EXACT_COLOR_RULE','expression':'E_src/sqrt(4/3)' if b['U3'][i,j]!=0 else '0'} for i in range(24) for j in range(3)]
 index={'baseline':BASELINE,'status':STATUS,'next':NEXT,'C66_U3_hash':b['U3_hash'],'arrays':rec,'entry_statuses':statuses,'basis_hash':sha256(b'product(cprime,a);triplet(c)').hexdigest(),'aggregate_hash':sha256(json.dumps(rec,sort_keys=True).encode()).hexdigest(),'validation':b['validation']};(RUNTIME/'index.json').write_text(json.dumps(index,sort_keys=True,indent=2)+'\n');return index
def load(name):
 i=json.loads((RUNTIME/'index.json').read_text());r=i['arrays'][name];a=np.load(ROOT/r['path'],allow_pickle=False)
 if h(a)!=r['sha256']:raise ValueError('C68 hash mismatch')
 a.setflags(write=False);return a
