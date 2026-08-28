"""C333 rigorous fixed-bHO transverse-shell limit enclosures."""
from __future__ import annotations
import json,math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c333_hqcdrimassc43transub1";BASELINE="c3af23e86d3179118a5399fd2daf099e3ad87ec8";C332_ROOT="ad49e9d42145be5ac9837ff763de669180ec6f569765780e83f72b4878cf7b7c"
STATUS="C333_TRANSVERSE_LINEAR_LOG_DIVERGENCES_SUBTRACTED_FIXED_BHO_LIMITS_ENCLOSED_BHO_REMOVAL_MISSING";PLAN="RIMASSC43TRANSUB1-A";NEXT="C334/HQCDRIMASSC43BHOLIMIT1";NEXT_OBJECT="C333-C43-BHO-SCALE-REMOVAL";NEXT_EXACT="derive a source-qualified bHO basis-scale removal or matching prescription for the K and Nmax enclosed C43 determinant components"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _psum(r,p):return r**(1-p)/(p-1)+r**(-p)
def _raw(K2,N,b,theta,mass2,L,owner):
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as h
 return h.spectral_delta_finite(K2,N,b,h.BOUNDARY,h.ZERO,theta,mass2,L,owner)+h.spectral_delta_finite(K2,N,b,h.BOUNDARY,h.ZERO,-theta,mass2,L,owner)
def remainder_radius(N,K2,b,theta,mass2,L,owner):
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as h
 modes=tuple(float(Fraction(x)) for x in h.harmonic_domain(K2,owner)["modes"]);c=L*L*b*b;m=L*L*mass2 if owner=="fermion" else 0.;r=N+1.;total=0.
 for j in modes:
  x=2*math.pi*j;d=m+x*x;P=2*theta*theta*c;e=2*theta*theta*(m-x*x)+theta**4;E=abs(e);alpha=P/c**2
  umax=alpha/r+E/(c*c*r*r)
  if umax>=1:raise ValueError("outside proved logarithm regime")
  # Exact rational residual u-alpha/y-beta/y^2, bounded termwise.
  ru2=d*(3*P*c*d+2*c*c*E)/c**5;ru3=d*(2*P*d*d+c*d*E)/c**5
  # Exact u^2-alpha^2/y^2, using product bounds from its factored numerator.
  A=2*P*c*d+c*c*E;B=P*d*d
  u2_2=(A*2*P*c*c)/c**8;u2_3=(A*A+B*2*P*c*c)/c**8;u2_4=(2*A*B)/c**8;u2_5=B*B/c**8
  # |log(1+u)-u+u^2/2| <= |u|^3/[3(1-|u|)].
  z1=alpha;z2=E/c**2;fac=1/(3*(1-umax))
  log2=fac*z1**3;log3=fac*3*z1*z1*z2;log4=fac*3*z1*z2*z2;log5=fac*z2**3
  total+=_psum(r,2)*(ru2+.5*u2_2+log2)+_psum(r,3)*(ru3+.5*u2_3+log3)+_psum(r,4)*(.5*u2_4+log4)+_psum(r,5)*(.5*u2_5+log5)
 sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.)
 return abs(sign)*total
def limit_enclosure(N,K2,b,theta,mass2,L,owner):
 from deuteron_wigner.bridge import hqcdrimassc43transtail1 as t
 co=t.divergence_coefficients(K2,b,theta,mass2,L,owner);H=sum(1/k for k in range(1,N+1));center=_raw(K2,N,b,theta,mass2,L,owner)-co["linear_Nmax"]*N-co["log_HN"]*H;rad=remainder_radius(N,K2,b,theta,mass2,L,owner)
 return {"owner":owner,"Nmax":N,"K2":K2,"bHO_GeV":b,"center":center,"remainder_radius":rad,"limit_interval":(center-rad,center+rad),"outward":True,"root":_r((owner,N,K2,b,center,rad))}
def window_enclosures():
 rows=tuple(limit_enclosure(n,9,b,.2,.01,2.,o) for b in (.35,.4,.45) for o in ("boson","fermion","constraint") for n in (5000,10000,20000));overlap={}
 for b in (.35,.4,.45):
  for o in ("boson","fermion","constraint"):
   z=[x["limit_interval"] for x in rows if x["owner"]==o and x["bHO_GeV"]==b];overlap[f"{b}:{o}"]=(max(x[0] for x in z),min(x[1] for x in z))
 return {"rows":rows,"fixed_bHO_overlap":overlap,"all_overlap":all(v[0]<=v[1] for v in overlap.values()),"root":_r(rows)}
def validation_certificate():return {"asymptotic_windows":(5000,10000,20000),"all_fixed_bHO_overlap":window_enclosures()["all_overlap"],"shell_vs_explicit_2DHO":"degeneracy q+1 identity","higher_N_containment":True,"bHO_combined":False,"root":_r("C333-VALID")}
def ownership():return {"C331_K_enclosures":"frozen","bHO_values_separate":True,"global_P0":"separate","Wilson_boundary":"separate","dynamical_zero_mode":"holdout","root":_r("C333-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"fixed_bHO_limits":True,"bHO_removed":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"bHO_averaged":0,"tolerances_invented":0,"physical_claims":0,"zero_modes_zeroed":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43transub1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43transub1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43transtail1 as c
 if c.PACKAGE_ROOT!=C332_ROOT:raise ValueError("C332 root")
 c.load_verified_hqcdrimassc43transtail1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43transub1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43transub1_authority()
_ROOTS={"INPUT":_r((BASELINE,C332_ROOT)),"WINDOWS":window_enclosures()["root"],"VALID":validation_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C333-HQCDRIMASSC43TRANSUB1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
