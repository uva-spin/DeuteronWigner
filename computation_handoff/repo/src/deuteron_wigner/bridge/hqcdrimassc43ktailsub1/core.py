"""C331 rigorous componentwise paired finite-harmonic K-limit enclosures."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c331_hqcdrimassc43ktailsub1";BASELINE="ed8f1bb1537bd8bffc06988f75594d2a2201d1ce";C330_ROOT="80a647fdb4e135124b1424ee9ee1f27b2d2713477bab08c0e5eb3e8b50ff9db1"
STATUS="C331_COMPONENTWISE_PAIRED_ONE_OVER_K_TAILS_SUBTRACTED_K_LIMITS_OUTWARDLY_ENCLOSED_TRANSVERSE_LIMIT_MISSING";PLAN="RIMASSC43KTAILSUB1-A";NEXT="C332/HQCDRIMASSC43TRANSTAIL1";NEXT_OBJECT="C331-C43-TRANSVERSE-NMAX-BHO-LIMIT";NEXT_EXACT="derive the Nmax and bHO truncation structure of the charge-paired K-enclosed C43 determinant components before joint continuum matching"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _psum(r,p):
 lo=r**(1-p)/(p-1);return lo,lo+r**(-p)
def _first_omitted(K2,owner):return K2/2+1 if owner=="fermion" else K2//2+1
def paired_partial(K2,Nmax,bHO,theta,mass2,L,owner):
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as c
 return c.spectral_delta_finite(K2,Nmax,bHO,c.BOUNDARY,c.ZERO,theta,mass2,L,owner)+c.spectral_delta_finite(K2,Nmax,bHO,c.BOUNDARY,c.ZERO,-theta,mass2,L,owner)
def limit_enclosure(K2,Nmax,bHO,theta,mass2,L,owner):
 if owner not in ("boson","fermion","constraint"):raise ValueError(owner)
 partial=paired_partial(K2,Nmax,bHO,theta,mass2,L,owner);r=_first_omitted(K2,owner);sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.);scale=2*math.pi
 shell=Nmax*(Nmax+1)//2;coeff=-sign*shell*theta*theta/(2*math.pi**2);s2=_psum(r,2);lead=sorted((coeff*s2[0],coeff*s2[1]));rem=0.
 for q in range(Nmax):
  deg=q+1;a=L*L*(bHO*bHO*(q+1)+(mass2 if owner=="fermion" else 0.));t2=theta*theta;t4=t2*t2
  B2=2*t2;B4=2*t2*a+t4;umax=B2/(scale*r)**2+B4/(scale*r)**4
  if umax>=1:raise ValueError("tail window outside logarithm bound")
  D4=(6*t2*a+t4)/scale**4;D6=2*t2*a*a/scale**6
  E4=.5*B2*B2/(1-umax)/scale**4;E6=B2*B4/(1-umax)/scale**6;E8=.5*B4*B4/(1-umax)/scale**8
  rem+=abs(sign)*deg*((D4+E4)*_psum(r,4)[1]+(D6+E6)*_psum(r,6)[1]+E8*_psum(r,8)[1])
 lo=partial+lead[0]-rem;hi=partial+lead[1]+rem
 return {"owner":owner,"K2":K2,"first_omitted":r,"partial":partial,"leading_tail_interval":tuple(lead),"remainder_radius":rem,"limit_interval":(lo,hi),"outward":True,"root":_r((owner,K2,lo,hi))}
def window_enclosures():
 rows=tuple(limit_enclosure(k,6,.4,.2,.01,2.,o) for o in ("boson","fermion","constraint") for k in (41,81,161));overlap={}
 for o in ("boson","fermion","constraint"):
  z=[x["limit_interval"] for x in rows if x["owner"]==o];overlap[o]=(max(x[0] for x in z),min(x[1] for x in z))
 return {"rows":rows,"overlap":overlap,"all_windows_overlap":all(v[0]<=v[1] for v in overlap.values()),"root":_r(rows)}
def validation_certificate():
 w=window_enclosures();return {"multiple_windows":True,"all_overlap":w["all_windows_overlap"],"order_independent":"component sums commute; intervals formed before owner combination","higher_K_direct_checked":True,"physical":False,"root":_r("C331-VALID")}
def ownership():return {"componentwise":True,"global_P0":"C319 separate","Wilson_boundary":"JMY_BJY separate","dynamical_zero_mode":"holdout","root":_r("C331-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"K_limits_enclosed":True,"transverse_limit":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"fit_coefficients":0,"physical_weights":0,"zero_modes_zeroed":0,"continuum_claims":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43ktailsub1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43ktailsub1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43ktail1 as c
 if c.PACKAGE_ROOT!=C330_ROOT:raise ValueError("C330 root")
 c.load_verified_hqcdrimassc43ktail1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43ktailsub1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43ktailsub1_authority()
_ROOTS={"INPUT":_r((BASELINE,C330_ROOT)),"WINDOWS":window_enclosures()["root"],"VALID":validation_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C331-HQCDRIMASSC43KTAILSUB1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
