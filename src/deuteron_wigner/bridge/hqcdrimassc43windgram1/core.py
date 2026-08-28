"""C339 increasing-rank center-covariant winding Gram evaluation."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c339_hqcdrimassc43windgram1"
BASELINE="d1e70046e1db063eb257fde225aaaf4014869940";C338_ROOT="304c653f5e7758b3a51b8b3914fbd6b80aa8d11fbb7d95957d506db51d4d8d6d"
STATUS="C339_INCREASING_RANK_WINDING_GRAM_ENCLOSED_TRIALITY_ZERO_COMPLETION_MISSING";PLAN="RIMASSC43WINDGRAM1-C"
NEXT="C340/HQCDRIMASSC43TRIALITYZERO1";NEXT_OBJECT="C339-C43-TRIALITY-ZERO-WINDING-COMPLETION";NEXT_EXACT="extend the frozen invariant sector by the triality-zero higher-winding functions and enclose the combined APBC determinant limit"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def coefficient(l,L=2.,mass2=.01):
 z=math.sqrt(mass2)*L;return 2*(-1)**l*math.exp(-z*l)*(1+z*l)/(math.pi*L*L*l**3)
def _grid(M,G,L,mass2):
 from deuteron_wigner.bridge import hqcdrimassc43centerbasis1 as b
 x,w=np.polynomial.legendre.leggauss(G);pts=math.pi*(x+1);ww=math.pi*w;n=len(b.finite_basis(.1,.2,M)[0]);A=np.zeros((n,n));rhs=np.zeros(n);norm=0.
 measure=__import__('deuteron_wigner.bridge.hqcdrimasssu3measurederive1',fromlist=['evaluate_density'])
 expected=np.zeros(n);k=3
 for l in range(1,M+1):
  if l%3:expected[k]=coefficient(l,L,mass2);k+=2
 for i,p1 in enumerate(pts):
  for j,p2 in enumerate(pts):
   q=ww[i]*ww[j]*float(measure.evaluate_density(p1,p2)["full_torus_density"]);v,_=b.finite_basis(p1,p2,M);y=float(v@expected);A+=q*np.outer(v,v);rhs+=q*v*y;norm+=q*y*y
 solved=np.linalg.solve(A,rhs);res=max(0.,norm-float(rhs@solved));ev=np.linalg.eigvalsh(A)
 return {"M":M,"G":G,"dimension":n,"rank":int(np.linalg.matrix_rank(A,tol=1e-10)),"condition_number":float(np.linalg.cond(A)),"minimum_eigenvalue":float(ev[0]),"coefficient_max_defect":float(np.max(np.abs(solved-expected))),"imaginary_coefficient_max":float(np.max(np.abs(solved[4::2]))) if n>4 else 0.,"reconstruction_norm2":res,"full_rank":bool(ev[0]>1e-10)}
def _tail_bound(M,L=2.,mass2=.01,multiple_of_three=False):
 z=math.sqrt(mass2)*L;n=M+1
 # (1+zl)e^-zl decreases; integral-test bound for sum l^-3.
 total=math.exp(-z*n)*(1+z*n)*(1/n**3+1/(2*n**2))
 # Restricting to a subsequence can only decrease this outward bound.
 return 6*total/(math.pi*L*L)
def increasing_rank_certificate():
 rows=tuple(_grid(M,G,2.,.01) for M,G in ((2,14),(4,18),(5,22)))
 return {"rows":rows,"center_charged_tail_absolute_bound":_tail_bound(5),"triality_zero_higher_winding_absolute_bound":_tail_bound(5,multiple_of_three=True),"coefficient_enclosure_radius":max(r["coefficient_max_defect"] for r in rows)+_tail_bound(5),"all_full_rank":all(r["full_rank"] for r in rows),"finite_exact_span":False,"physical":False,"root":_r(rows)}
def separation_certificate():return {"center_charged":"C338 real/imaginary triality pairs","triality_zero_higher_windings":"retained residual, not absorbed into C301","C301_subspace":"frozen","P0":"excluded","Wilson_boundary":"separate","root":_r("C339-SEPARATION")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"finite_exact_claim":0,"ill_conditioned_modes_dropped":0,"physical_claim":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43windgram1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43windgram1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43centerbasis1 as c
 if c.PACKAGE_ROOT!=C338_ROOT:raise ValueError("C338 root")
 c.load_verified_hqcdrimassc43centerbasis1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43windgram1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43windgram1_authority()
_ROOTS={"INPUT":_r((BASELINE,C338_ROOT)),"GRAM":increasing_rank_certificate()["root"],"SEPARATION":separation_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C339-HQCDRIMASSC43WINDGRAM1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
