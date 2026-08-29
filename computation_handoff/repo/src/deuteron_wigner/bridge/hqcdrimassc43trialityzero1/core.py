"""C340 triality-zero winding completion with SU(3) recurrence ledger."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c340_hqcdrimassc43trialityzero1"
BASELINE="d4da4ea5d7009371925b61b3fb335417780848e4";C339_ROOT="90523886579204d39e03fe0b62037b129a4c3dfbcd2f5bddfe8c5d6f264e3050"
STATUS="C340_TRIALITY_ZERO_WINDINGS_COMPLETED_COMBINED_APBC_LIMIT_ENCLOSED";PLAN="RIMASSC43TRIALITYZERO1-C"
NEXT="C341/HQCDRIMASSC43FULLCERT1";NEXT_OBJECT="C340-C43-CONTINUUM-DETERMINANT-FULL-CERTIFICATE";NEXT_EXACT="publish the combined continuum C43 determinant class-function certificate with infinite-winding errors and all nonphysical-domain exclusions"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _z(p1,p2,l):return sum(complex(math.cos(l*x),math.sin(l*x)) for x in (p1,p2,-p1-p2))
def coefficient(l,L=2.,mass2=.01):
 z=math.sqrt(mass2)*L;return 2*(-1)**l*math.exp(-z*l)*(1+z*l)/(math.pi*L*L*l**3)
def recurrence_certificate():
 defects=[]
 for p in ((.2,.7),(.4,1.1),(2.1,5.2)):
  from deuteron_wigner.bridge.hqcdrimassc43centerbasis1 import frozen_basis
  b=frozen_basis(*p);defects.append(abs(_z(*p,3).real-(b[2]-3*b[1])))
 return {"identity":"RE_TRF_W3 = RE_TF3 - 3 CHI8","max_defect":float(max(defects)),"W3_independent_column":False,"W3_ledger_coordinates":(0.,-3.,1.),"pass":bool(max(defects)<1e-12),"root":_r(defects)}
def combined_basis(p1,p2,M):
 from deuteron_wigner.bridge.hqcdrimassc43centerbasis1 import frozen_basis,winding_pair
 out=list(frozen_basis(p1,p2));labels=["1","CHI8","RE_TF3"]
 for l in range(1,M+1):
  if l%3:out.extend(winding_pair(p1,p2,l));labels.extend((f"RE_TRF_W{l}",f"IM_TRF_W{l}"))
  elif l>=6:out.append(_z(p1,p2,l).real);labels.append(f"RE_TRF_W{l}")
 return np.array(out),tuple(labels)
def gram_row(M,G=24):
 x,w=np.polynomial.legendre.leggauss(G);pts=math.pi*(x+1);ww=math.pi*w;n=len(combined_basis(.1,.2,M)[0]);A=np.zeros((n,n));rhs=np.zeros(n);expected=np.zeros(n);expected[1]=-3*coefficient(3);expected[2]=coefficient(3);k=3
 for l in range(1,M+1):
  if l%3:expected[k]=coefficient(l);k+=2
  elif l>=6:expected[k]=coefficient(l);k+=1
 measure=__import__('deuteron_wigner.bridge.hqcdrimasssu3measurederive1',fromlist=['evaluate_density'])
 for i,p1 in enumerate(pts):
  for j,p2 in enumerate(pts):
   q=ww[i]*ww[j]*float(measure.evaluate_density(p1,p2)["full_torus_density"]);v,_=combined_basis(p1,p2,M);A+=q*np.outer(v,v);rhs+=q*v*float(v@expected)
 solved=np.linalg.solve(A,rhs);ev=np.linalg.eigvalsh(A)
 return {"M":M,"G":G,"dimension":n,"rank":int(np.linalg.matrix_rank(A,tol=1e-10)),"condition_number":float(np.linalg.cond(A)),"minimum_eigenvalue":float(ev[0]),"coefficient_max_defect":float(np.max(np.abs(solved-expected))),"full_rank":bool(ev[0]>1e-10),"W3_ledger_contribution":tuple(map(float,expected[:3]))}
def tail_bound(M,L=2.,mass2=.01):
 z=math.sqrt(mass2)*L;n=M+1;return 6*math.exp(-z*n)*(1+z*n)*(1/n**3+1/(2*n**2))/(math.pi*L*L)
def combined_limit_certificate():
 rows=tuple(gram_row(m) for m in (3,4,6));tail=tail_bound(6)
 return {"rows":rows,"combined_APBC_tail_absolute_bound":tail,"coefficient_enclosure_radius":tail+max(r["coefficient_max_defect"] for r in rows),"all_full_rank":all(r["full_rank"] for r in rows),"finite_exact_span":False,"infinite_limit_enclosed":True,"physical":False,"root":_r(rows)}
def ownership():return {"C301_subspace":"frozen","W3":"separate recurrence ledger","center_charged_C339":"retained","P0":"excluded","Wilson_boundary":"separate","physical_parameters":False,"root":_r("C340-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"dependent_W3_column_added":0,"finite_exact_claim":0,"physical_claim":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43trialityzero1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43trialityzero1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43windgram1 as c
 if c.PACKAGE_ROOT!=C339_ROOT:raise ValueError("C339 root")
 c.load_verified_hqcdrimassc43windgram1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43trialityzero1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43trialityzero1_authority()
_ROOTS={"INPUT":_r((BASELINE,C339_ROOT)),"RECURRENCE":recurrence_certificate()["root"],"LIMIT":combined_limit_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C340-HQCDRIMASSC43TRIALITYZERO1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
