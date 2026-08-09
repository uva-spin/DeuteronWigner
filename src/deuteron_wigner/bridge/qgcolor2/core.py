"""C66 frozen C53-convention 24x3 triplet-isometry artifact."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from ..vertex3.core import color_data, color_validation, array_hash, CF

ROOT=Path(__file__).resolve().parents[4]
BASELINE='fd459d8114224de78ba562f904f39ba7d42b6ddc'
STATUS='C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY'
NEXT='C67/QGEMBED4 — resume exact physical qg embedding using C64 and C66'
def digest(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def build():
 d=color_data();U=np.asarray(d['U']);E=np.asarray(d['E']);T=np.asarray(d['T']);total=np.asarray(d['total']);P=U@U.conj().T
 v=color_validation(); residual=max(np.linalg.norm(U.conj().T@U-np.eye(3)),max(np.linalg.norm(total[a]@U-U@T[a]) for a in range(8)),np.linalg.norm(P-P.conj().T),np.linalg.norm(P@P-P))
 assert U.shape==(24,3) and residual<1e-10 and np.linalg.norm(E.conj().T@E-CF*np.eye(3))<1e-10
 return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'normalization':'QGCOLOR2-CASIMIR-NORMALIZATION; U3=E_src/sqrt(C_F), C_F=4/3','U3':U,'E':E,'P3':P,'T':T,'total':total,'U3_hash':array_hash(U),'E_hash':array_hash(E),'P3_hash':array_hash(P),'support_hash':digest(np.abs(U)>0),'validation':{'UdaggerU':float(np.linalg.norm(U.conj().T@U-np.eye(3))),'intertwiner':float(max(np.linalg.norm(total[a]@U-U@T[a]) for a in range(8))),'P_hermiticity':float(np.linalg.norm(P-P.conj().T)),'P_idempotence':float(np.linalg.norm(P@P-P)),'rank':int(np.linalg.matrix_rank(P)),'trace':float(np.trace(P).real),'C53_validation':{k:v[k] for k in ('projector_equivalence','leakage','W_unitary')},'pass':True}}
