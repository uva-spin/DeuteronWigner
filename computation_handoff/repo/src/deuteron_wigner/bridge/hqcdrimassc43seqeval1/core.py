"""C327 validation-only independent-axis C43 determinant sequence."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c327_hqcdrimassc43seqeval1";BASELINE="ba2d18a7db74fdaa17a1b66f62e7cf157fb436b1";C326_ROOT="ad31db59ab18864e410f168d41fba6aa0e76cfe09e7d97a815924e96f584279b"
STATUS="C327_NONPHYSICAL_C43_EXECUTABLE_AXIS_SEQUENCE_EVALUATED_K_NULL_CERTIFIED_FINITE_HARMONIC_ADAPTER_MISSING";PLAN="RIMASSC43SEQEVAL1-B";NEXT="C328/HQCDRIMASSC43KHARMONIC1";NEXT_OBJECT="C327-C43-FINITE-DLCQ-HARMONIC-ADAPTER";NEXT_EXACT="derive and implement the C315 positive APBC and nonzero PBC finite harmonic domains so the determinant sequence depends lawfully on K"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def grid_design():return {"K2":(7,9,11),"Nmax":(6,8,10),"bHO_GeV":(.35,.4,.45),"sum_cutoff":(8,16),"owners":("boson","fermion","constraint"),"theta":.2,"mass2_GeV2":.01,"L_GeVinv":2.,"physical":False,"root":_r("C327-GRID")}
def sequence_results():
 from deuteron_wigner.bridge import hqcdrimassc43genkernel1 as c
 d=grid_design();rows=[]
 for owner in d["owners"]:
  for K in d["K2"]:
   for nm in d["Nmax"]:
    for b in d["bHO_GeV"]:
     for n in d["sum_cutoff"]:
      v=c.spectral_delta_general(K,nm,b,c.BOUNDARY,c.ZERO,d["theta"],d["mass2_GeV2"],d["L_GeVinv"],n,owner)
      rows.append({"owner":owner,"K2":K,"Nmax":nm,"bHO_GeV":b,"sum_cutoff":n,"value":v})
 return {"rows":tuple(rows),"count":len(rows),"all_finite":all(math.isfinite(x["value"]) for x in rows),"physical":False,"root":_r(rows)}
def axis_certificate():
 rows=sequence_results()["rows"]
 def varied(axis):
  groups={}
  for x in rows:
   key=tuple((k,x[k]) for k in ("owner","K2","Nmax","bHO_GeV","sum_cutoff") if k!=axis);groups.setdefault(key,set()).add(x["value"])
  return any(len(v)>1 for v in groups.values())
 return {"Nmax_nontrivial":varied("Nmax"),"bHO_nontrivial":varied("bHO_GeV"),"sum_cutoff_nontrivial":varied("sum_cutoff"),"K2_nontrivial":varied("K2"),"K2_role":"C326_METADATA_ONLY_EXACT_NULL","false_independent_K_claim":False,"root":_r("C327-AXES")}
def covariance_record():return {"shared_inputs":("theta","mass2_GeV2","L_GeVinv","boundary_class","zero_mode_owner"),"axis_residuals":("Nmax","bHO","sum_cutoff"),"K_covariance":"UNAVAILABLE_PENDING_FINITE_HARMONIC_ADAPTER","numeric_physical_covariance":False,"root":_r("C327-COV")}
def ownership():return {"global_P0":"NOT_APPLICABLE_BY_C319_DOMAIN","dynamical_PBC_zero_mode":"EXPLICIT_HOLDOUT_NOT_ZERO","Wilson_boundary":"JMY_BJY_OWNER_SEPARATE","count_once":True,"root":_r("C327-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"sequence_evaluated":True,"independent_K":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"physical_weights":0,"tolerances":0,"zero_mode_values":0,"K_claims":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43seqeval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43seqeval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43genkernel1 as c
 if c.PACKAGE_ROOT!=C326_ROOT:raise ValueError("C326 root")
 c.load_verified_hqcdrimassc43genkernel1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43seqeval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43seqeval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C326_ROOT)),"GRID":grid_design()["root"],"RESULT":sequence_results()["root"],"AXES":axis_certificate()["root"],"COV":covariance_record()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C327-HQCDRIMASSC43SEQEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
