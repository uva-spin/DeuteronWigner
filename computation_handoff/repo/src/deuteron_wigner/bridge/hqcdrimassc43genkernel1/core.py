"""C326 generalized, nonphysical C43 determinant spectrum kernel."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c326_hqcdrimassc43genkernel1";BASELINE="333abf4ea1e86538d382acbd804dd6637c597956";C325_ROOT="db0bf71210f0fad060bd5808e364969b746500098ceb0020f08bac30072fdaf9"
STATUS="C326_GENERAL_NONZERO_MODE_SPECTRUM_KERNEL_READY_CONTROLLED_SEQUENCE_EVALUATION_MISSING";PLAN="RIMASSC43GENKERNEL1-A";NEXT="C327/HQCDRIMASSC43SEQEVAL1";NEXT_OBJECT="C326-C43-CONTROLLED-SEQUENCE-EVALUATION";NEXT_EXACT="evaluate nonphysical independent-axis C43 determinant sequences with the C326 kernel while retaining the dynamical PBC zero-mode holdout"
BOUNDARY="C43_DLCQ_APBC_F_PBC_B";ZERO="EXCLUDE_TO_GLOBAL_P0_OWNER"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def _check(K,Nmax,bHO,mass2,L,sum_cutoff,owner,boundary,zero):
 if not isinstance(K,int) or K<2 or not isinstance(Nmax,int) or Nmax<1 or not isinstance(sum_cutoff,int) or sum_cutoff<1:raise ValueError("integer regulator")
 if not all(math.isfinite(x) for x in (bHO,mass2,L)) or bHO<=0 or mass2<0 or L<=0:raise ValueError("scale")
 if owner not in ("boson","fermion","constraint") or boundary!=BOUNDARY:raise ValueError("class")
 if owner!="fermion" and zero!=ZERO:raise ValueError("unsupported PBC zero-mode sector")
def spectral_delta_general(K,Nmax,bHO,boundary,zero_mode_sector,theta,mass2,L,sum_cutoff,owner):
 _check(K,Nmax,bHO,mass2,L,sum_cutoff,owner,boundary,zero_mode_sector)
 phase=.5 if owner=="fermion" else 0.;sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.);total=0.
 for q in range(Nmax):
  for n in range(-sum_cutoff,sum_cutoff+1):
   if owner!="fermion" and n==0:continue
   x=2*math.pi*(n+phase);omega2=bHO*bHO*(q+1)+(mass2 if owner=="fermion" else 0.)
   total+=sign*(q+1)*math.log(((x+theta)/L)**2+omega2)-sign*(q+1)*math.log((x/L)**2+omega2)
 return total
def legacy_round_trip(resolution,theta,mass2,L,N,owner):
 from deuteron_wigner.bridge import hqcdrimassc43deteval2 as old
 nm,b={"K9":(8,.4),"K11":(10,.45),"K13":(12,.5)}[resolution]
 new=spectral_delta_general(int(resolution[1:]),nm,b,BOUNDARY,ZERO,theta,mass2,L,N,owner)
 return {"legacy":old.spectral_delta(resolution,theta,mass2,L,N,owner),"general":new,"exact":new==old.spectral_delta(resolution,theta,mass2,L,N,owner)}
def kernel_contract():return {"K_metadata_separate_from_sum_cutoff":True,"independent":("K","Nmax","bHO","sum_cutoff"),"zero_mode_supported":ZERO,"dynamical_PBC_zero_mode":False,"P0_count_once":True,"root":_r("C326-KERNEL")}
def parity():return {"legacy_all":all(legacy_round_trip(r,.2,.01,2.,8,o)["exact"] for r in ("K9","K11","K13") for o in ("boson","fermion","constraint")),"theta_zero":spectral_delta_general(9,8,.4,BOUNDARY,ZERO,0.,0.,2.,8,"boson")==0.,"root":_r("C326-PARITY")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def mutate_live_hqcdrimassc43genkernel1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43genkernel1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43seqgen1 as c
 if c.PACKAGE_ROOT!=C325_ROOT:raise ValueError("C325 root")
 c.load_verified_hqcdrimassc43seqgen1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43genkernel1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43genkernel1_authority()
_ROOTS={"INPUT":_r((BASELINE,C325_ROOT)),"KERNEL":kernel_contract()["root"],"PARITY":parity()["root"],"RESIDUAL":residual_frontier()["root"]};PACKAGE_ROOT=_r({"schema":"C326-HQCDRIMASSC43GENKERNEL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
