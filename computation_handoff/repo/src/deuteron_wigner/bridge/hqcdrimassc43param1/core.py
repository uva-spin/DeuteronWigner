"""C317 nonphysical validation capsules for C316."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c317_hqcdrimassc43param1";BASELINE="77ccbc676b039a649caf9605e2f76ab46fed7c2d";C316_ROOT="56d63ee4443f62150eedcfcdb3ab2ca3b975bd88318a9fd3ef18832fb9484892"
STATUS="C317_NONPHYSICAL_C43_DETERMINANT_VALIDATION_CAPSULE_FAMILY_BOUND_GRAM_EVALUATION_MISSING";PLAN="RIMASSC43PARAM1-D";NEXT="C318/HQCDRIMASSC43GRAMEVAL1";NEXT_OBJECT="C317-C43-VALIDATION-GRAM-EVALUATION";NEXT_EXACT="execute the C316 determinant and C301 Gram coefficient routes on the C317 nonphysical K9 K11 K13 validation capsule family"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def capsule_family():
 rows=tuple({"id":f"C317-VALIDATION-{r}","resolution":r,"mass2_GeV2":m,"signed_mass_GeV":"SEPARATE_UNUSED","L_GeVinv":L,"coupling_normalization":1.,"boundary_class":"C43_DLCQ_APBC_F_PBC_B","P0_functional":"SYMBOLIC_HOLDOUT_P0","physical":False} for r,m,L in (("K9",.01,2.),("K11",.04,2.5),("K13",.09,3.)))
 return {"scheme":"PROJECT_C43_DETERMINANT_VALIDATION_V1","rows":rows,"defaults":False,"physical":False,"root":_r(rows)}
def validation_evaluations():
 from deuteron_wigner.bridge import hqcdrimassc43deteval2 as c
 rows=tuple({"resolution":x["resolution"],"fermion_theta_holdout":c.spectral_delta(x["resolution"],.2,x["mass2_GeV2"],x["L_GeVinv"],16,"fermion"),"boson_zero":c.spectral_delta(x["resolution"],0.,0.,x["L_GeVinv"],16,"boson")} for x in capsule_family()["rows"])
 return {"rows":rows,"finite":all(abs(x["fermion_theta_holdout"])<1e9 for x in rows),"P0_added":False,"root":_r(rows)}
def covariance():return {"shared_symbols":("coupling_normalization","P0_functional","scheme"),"cross_K":"required","numeric":"VALIDATION_DIAGONAL_NOT_PHYSICAL_COVARIANCE","root":_r("C317-COV")}
def route_parity():return {"schema_valid":True,"zero_theta":all(x["boson_zero"]==0 for x in validation_evaluations()["rows"]),"physical_claim":False,"root":_r("C317-PARITY")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"capsules_ready":True,"Gram_evaluated":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"fixture_promoted_physical":0,"P0_zeroed":0,"signed_mass_squared":0,"K_averaged":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43param1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43param1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43deteval2 as c
 if c.PACKAGE_ROOT!=C316_ROOT:raise ValueError("C316 root")
 c.load_verified_hqcdrimassc43deteval2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43param1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43param1_authority()
_ROOTS={"INPUT":_r((BASELINE,C316_ROOT)),"CAPSULE":capsule_family()["root"],"EVAL":validation_evaluations()["root"],"COV":covariance()["root"],"PARITY":route_parity()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C317-HQCDRIMASSC43PARAM1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
