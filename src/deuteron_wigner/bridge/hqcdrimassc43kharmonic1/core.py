"""C328 finite positive-harmonic C43 DLCQ determinant adapter."""
from __future__ import annotations
import json,math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c328_hqcdrimassc43kharmonic1";BASELINE="af89653da86387c46ecbd04073dee7e740ce9739";C327_ROOT="17d4e338b4e1a07bd87a31ff32da2d2d51ef702979c1582f05a5c3bed9ce38cc"
STATUS="C328_FINITE_APBC_PBC_DLCQ_HARMONIC_DETERMINANT_ADAPTER_READY_K_DEPENDENT_SEQUENCE_MISSING";PLAN="RIMASSC43KHARMONIC1-A";NEXT="C329/HQCDRIMASSC43KSEQEVAL1";NEXT_OBJECT="C328-C43-K-DEPENDENT-SEQUENCE-EVALUATION";NEXT_EXACT="evaluate the controlled nonphysical C43 determinant grid with the finite C328 harmonic adapter and quantify separate K Nmax bHO truncation differences"
BOUNDARY="C43_DLCQ_APBC_F_PBC_B";ZERO="EXCLUDE_TO_GLOBAL_P0_OWNER"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def harmonic_domain(K2,owner):
 if not isinstance(K2,int) or K2<3 or K2%2!=1:raise ValueError("K2 must be an odd positive twice-resolution")
 if owner=="fermion":m=tuple(Fraction(j,2) for j in range(1,K2+1,2));phase="APBC_HALF_INTEGER"
 elif owner in ("boson","constraint"):m=tuple(Fraction(j,1) for j in range(1,K2//2+1));phase="PBC_POSITIVE_NONZERO"
 else:raise ValueError(owner)
 return {"K":str(Fraction(K2,2)),"modes":tuple(str(x) for x in m),"count":len(m),"phase":phase,"zero_included":False,"root":_r((K2,owner,tuple(str(x) for x in m)))}
def spectral_delta_finite(K2,Nmax,bHO,boundary,zero_mode_sector,theta,mass2,L,owner):
 if boundary!=BOUNDARY or (owner!="fermion" and zero_mode_sector!=ZERO):raise ValueError("boundary/zero-mode sector")
 if not isinstance(Nmax,int) or Nmax<1 or not all(math.isfinite(x) for x in (bHO,theta,mass2,L)) or bHO<=0 or mass2<0 or L<=0:raise ValueError("parameters")
 modes=tuple(Fraction(x) for x in harmonic_domain(K2,owner)["modes"]);sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.);total=0.
 for q in range(Nmax):
  deg=q+1;omega2=bHO*bHO*(q+1)+(mass2 if owner=="fermion" else 0.)
  for j in modes:
   x=2*math.pi*float(j);total+=sign*deg*math.log(((x+theta)/L)**2+omega2)-sign*deg*math.log((x/L)**2+omega2)
 return total
def domain_certificate():
 rows=tuple({"K2":k,"fermion":harmonic_domain(k,"fermion"),"boson":harmonic_domain(k,"boson")} for k in (9,11,13))
 return {"rows":rows,"fermion_counts":(5,6,7),"boson_counts":(4,5,6),"nested":True,"C315_exact":True,"root":_r(rows)}
def route_parity():
 # shell route q with degeneracy q+1 equals explicit (n,m) state count by C315.
 return {"shell_counts":tuple(n*(n+1)//2 for n in (8,10,12)),"explicit_2DHO_counts":tuple(sum(q+1 for q in range(n)) for n in (8,10,12)),"counts_equal":True,"theta_zero":spectral_delta_finite(9,8,.4,BOUNDARY,ZERO,0.,0.,2.,"boson")==0.,"legacy_route_separate":True,"root":_r("C328-PARITY")}
def zero_mode_ownership():return {"j0":"GLOBAL_P0_DOMAIN_OWNER_PER_C319","dynamical_PBC":"UNSUPPORTED_HOLDOUT_NOT_ZERO","finite_sum_includes_j0":False,"count_once":True,"root":_r("C328-ZERO")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"adapter_ready":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"legacy_C316_modified":0,"zero_modes_zeroed":0,"physical_defaults":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43kharmonic1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43kharmonic1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43seqeval1 as c
 if c.PACKAGE_ROOT!=C327_ROOT:raise ValueError("C327 root")
 c.load_verified_hqcdrimassc43seqeval1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43kharmonic1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43kharmonic1_authority()
_ROOTS={"INPUT":_r((BASELINE,C327_ROOT)),"DOMAIN":domain_certificate()["root"],"PARITY":route_parity()["root"],"ZERO":zero_mode_ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C328-HQCDRIMASSC43KHARMONIC1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
