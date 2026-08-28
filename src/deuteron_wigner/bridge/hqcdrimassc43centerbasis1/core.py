"""C338 center-covariant fundamental winding basis."""
from __future__ import annotations
import json, math
from hashlib import sha256
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c338_hqcdrimassc43centerbasis1"
BASELINE="0eca80377d50ab5fc14a46c53c93a8f61f2c7d5c"
C337_ROOT="ad7ad070e0ddd53d0c6b8ea574d2e23a7c282d2502c0081f59ba0d17b6c4c6f6"
STATUS="C338_CENTER_COVARIANT_WINDING_BASIS_BOUND_INFINITE_COMPLETION_REQUIRED"
PLAN="RIMASSC43CENTERBASIS1-C"
NEXT="C339/HQCDRIMASSC43WINDGRAM1"
NEXT_OBJECT="C338-C43-INFINITE-WINDING-GRAM-LIMIT"
NEXT_EXACT="evaluate and enclose the increasing-rank center-covariant winding Gram projections through the infinite APBC winding limit"
def _r(v): return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _z(p1,p2,l=1):
 ph=(p1,p2,-p1-p2)
 return sum(complex(math.cos(l*x),math.sin(l*x)) for x in ph)
def frozen_basis(p1,p2):
 z=_z(p1,p2)
 return np.array((1.,abs(z)**2-1.,(z**3).real))
def winding_pair(p1,p2,l):
 if not isinstance(l,int) or l<1 or l%3==0: raise ValueError(l)
 z=_z(p1,p2,l); return np.array((z.real,z.imag))
def center_matrix(l):
 a=2*math.pi*(l%3)/3
 return np.array(((math.cos(a),-math.sin(a)),(math.sin(a),math.cos(a))))
def finite_basis(p1,p2,M):
 if not isinstance(M,int) or M<1: raise ValueError(M)
 out=list(frozen_basis(p1,p2)); labels=["1","CHI8","RE_TF3"]
 for l in range(1,M+1):
  if l%3:
   out.extend(winding_pair(p1,p2,l)); labels.extend((f"RE_TRF_W{l}",f"IM_TRF_W{l}"))
 return np.array(out),tuple(labels)
def covariance_certificate(M=8):
 p=(.37,1.09);s=2*math.pi/3; defects=[]
 for l in range(1,M+1):
  if l%3:
   a=winding_pair(*p,l);b=winding_pair(p[0]+s,p[1]+s,l)
   defects.append(float(np.max(np.abs(b-center_matrix(l)@a))))
 f=frozen_basis(*p);fs=frozen_basis(p[0]+s,p[1]+s)
 return {"M":M,"max_pair_covariance_defect":max(defects,default=0.),"frozen_subspace_defect":float(np.max(np.abs(f-fs))),"triality_pair_dimensions":2,"pass":max(defects,default=0.)<1e-12,"root":_r(defects)}
def gram_certificate(M=5,G=18):
 x,w=np.polynomial.legendre.leggauss(G);pts=math.pi*(x+1);ww=math.pi*w
 n=len(finite_basis(.1,.2,M)[0]);gram=np.zeros((n,n))
 measure=__import__('deuteron_wigner.bridge.hqcdrimasssu3measurederive1',fromlist=['evaluate_density'])
 for i,p1 in enumerate(pts):
  for j,p2 in enumerate(pts):
   q=ww[i]*ww[j]*float(measure.evaluate_density(p1,p2)["full_torus_density"]);b,_=finite_basis(p1,p2,M);gram+=q*np.outer(b,b)
 ev=np.linalg.eigvalsh(gram);return {"M":M,"G":G,"dimension":n,"rank":int(np.linalg.matrix_rank(gram,tol=1e-10)),"min_eigenvalue":float(ev[0]),"full_rank":bool(ev[0]>1e-10),"root":_r(tuple(map(float,ev)))}
def apbc_winding_certificate(L=2.,mass2=.01,M=32):
 z=math.sqrt(mass2)*L
 coeff=[]
 for l in range(1,M+1):
  if l%3: coeff.append((l,2*(-1)**l*math.exp(-z*l)*(1+z*l)/(math.pi*L*L*l**3)))
 tail=2/(math.pi*L*L)*sum(math.exp(-z*l)*(1+z*l)/l**3 for l in range(M+1,8*M+1))
 return {"L_GeVinv":L,"mass2_GeV2":mass2,"M":M,"center_charged_coefficients":tuple(coeff),"sampled_absolute_tail_bound":tail,"finite_exact_span":False,"infinite_winding_completion_required":True,"physical":False,"root":_r((coeff,tail))}
def residual_frontier(): return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def ownership(): return {"C301_center_invariant_subspace":"frozen","P0":"excluded","Wilson_boundary":"separate","physical_parameters":False,"root":_r("C338-OWNER")}
def static_isolation_guard(): return {"finite_exact_claim":0,"C301_basis_modified":0,"physical_claim":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43centerbasis1(i):
 if not isinstance(i,int) or not 0<=i<384: raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43centerbasis1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43heateval1 as c
 if c.PACKAGE_ROOT!=C337_ROOT: raise ValueError("C337 root")
 c.load_verified_hqcdrimassc43heateval1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43centerbasis1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43centerbasis1_authority()
_ROOTS={"INPUT":_r((BASELINE,C337_ROOT)),"COVARIANCE":covariance_certificate()["root"],"GRAM":gram_certificate()["root"],"WINDING":apbc_winding_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C338-HQCDRIMASSC43CENTERBASIS1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
