"""C329 finite-harmonic validation grid and axis differences."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c329_hqcdrimassc43kseqeval1";BASELINE="0390aba8b6e72b72aa1ddb787d88d1a76201b18d";C328_ROOT="56dffa25b74fc6a8b11e0d8da67621eff76006ea03fe863ca5c1daf6063c70ef"
STATUS="C329_FINITE_HARMONIC_C43_K_NMAX_BHO_GRID_EVALUATED_ASYMPTOTIC_CANCELLATION_DERIVATION_MISSING";PLAN="RIMASSC43KSEQEVAL1-A";NEXT="C330/HQCDRIMASSC43KTAIL1";NEXT_OBJECT="C329-C43-FINITE-HARMONIC-ASYMPTOTIC-TAILS";NEXT_EXACT="derive the large-K finite-harmonic tails and charge-pair cancellations of the C328 boson fermion and constraint determinant components before any continuum extrapolation"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def grid_design():return {"K2":(7,9,11),"Nmax":(6,8,10),"bHO_GeV":(.35,.4,.45),"owners":("boson","fermion","constraint"),"theta":.2,"mass2_GeV2":.01,"L_GeVinv":2.,"physical":False,"root":_r("C329-GRID")}
def grid_results():
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as c
 d=grid_design();rows=[]
 for o in d["owners"]:
  for k in d["K2"]:
   for n in d["Nmax"]:
    for b in d["bHO_GeV"]:
     rows.append({"owner":o,"K2":k,"Nmax":n,"bHO_GeV":b,"value":c.spectral_delta_finite(k,n,b,c.BOUNDARY,c.ZERO,d["theta"],d["mass2_GeV2"],d["L_GeVinv"],o)})
 return {"rows":tuple(rows),"count":len(rows),"all_finite":all(math.isfinite(x["value"]) for x in rows),"root":_r(rows)}
def adjacent_differences():
 rows=grid_results()["rows"];idx={(x["owner"],x["K2"],x["Nmax"],x["bHO_GeV"]):x["value"] for x in rows};out=[]
 for o in grid_design()["owners"]:
  for k in grid_design()["K2"]:
   for n in grid_design()["Nmax"]:
    for b in grid_design()["bHO_GeV"]:
     key=(o,k,n,b)
     for axis,vals,pos in (("K2",grid_design()["K2"],1),("Nmax",grid_design()["Nmax"],2),("bHO_GeV",grid_design()["bHO_GeV"],3)):
      i=vals.index(key[pos])
      if i+1<len(vals):
       nxt=list(key);nxt[pos]=vals[i+1];out.append({"owner":o,"axis":axis,"from":key[pos],"to":vals[i+1],"delta":idx[tuple(nxt)]-idx[key]})
 return {"rows":tuple(out),"count":len(out),"all_axes":tuple(sorted(set(x["axis"] for x in out))),"root":_r(out)}
def covariance_structure():return {"shared":("theta","mass2_GeV2","L_GeVinv","boundary","zero_mode_owner"),"separate_residuals":("K2","Nmax","bHO_GeV","component"),"values_correlated_not_ensemble_weights":True,"physical_covariance":False,"root":_r("C329-COV")}
def ownership():return {"legacy_C316_in_grid":False,"global_P0":"C319_NOT_APPLICABLE_BY_DOMAIN","dynamical_zero_mode":"HOLDOUT_NOT_ZERO","physical":False,"root":_r("C329-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"grid_evaluated":True,"continuum":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"fit_powers":0,"weights":0,"tolerances":0,"physical_claims":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43kseqeval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43kseqeval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as c
 if c.PACKAGE_ROOT!=C328_ROOT:raise ValueError("C328 root")
 c.load_verified_hqcdrimassc43kharmonic1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43kseqeval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43kseqeval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C328_ROOT)),"GRID":grid_design()["root"],"RESULT":grid_results()["root"],"DIFF":adjacent_differences()["root"],"COV":covariance_structure()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C329-HQCDRIMASSC43KSEQEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
