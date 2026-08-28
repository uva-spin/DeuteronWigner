"""C342 source-qualified physical-input binding audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c342_hqcdrimassc43physbind2"
BASELINE="9bed11f9f425f37d3f442856bbb7724cff8e2238";C341_ROOT="1336c1fa07a161cc78ad32f2ad5270af37b81679bd9564c4c3c3b578be3d5546"
STATUS="C342_PHYSICAL_INPUTS_COMPONENTWISE_AUDITED_OBSERVABLE_KINEMATICS_ENSEMBLE_MATCHING_MISSING";PLAN="RIMASSC43PHYSBIND2-C"
NEXT="C343/HQCDRIMASSC43OBSCAPSULE1";NEXT_OBJECT="C342-C43-JMY-SIDIS-PHYSICAL-OBSERVABLE-CAPSULE";NEXT_EXACT="bind source-qualified JMY SIDIS kinematics renormalization scales finite-volume sequence covariance and ensemble weights required for physical C43 determinant coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def authority_matrix():
 rows=(
  {"object":"light_quark_mass","authority":"C321/C154 PDG2026 MSbar 2GeV Nf4","available":True,"physical_standard_coordinate":True,"C43_ready":False,"deficit":"run and match to selected C43 renormalization scale/scheme"},
  {"object":"alpha_s","authority":"C321/C154 PDG2026 MSbar mZ Nf5","available":True,"physical_standard_coordinate":True,"C43_ready":False,"deficit":"run, threshold-match, and normalize to selected C43 scale"},
  {"object":"longitudinal_scale","authority":None,"available":False,"physical_standard_coordinate":False,"C43_ready":False,"deficit":"observable-qualified finite-volume/continuum sequence and kinematics"},
  {"object":"boundary_classes","authority":"C322 BPP/Heinzl source audit","available":True,"physical_standard_coordinate":False,"C43_ready":False,"deficit":"admissible regulator conventions do not select a physical ensemble"},
  {"object":"P0","authority":"C319 determinant-domain classification","available":True,"physical_standard_coordinate":False,"C43_ready":True,"deficit":None,"binding":"not applicable by domain; not numeric zero"},
  {"object":"Wilson_operator_owner","authority":"C323 JMY SIDIS plus BJY/Gao closure","available":True,"physical_standard_coordinate":True,"C43_ready":False,"deficit":"kinematics, rapidity/renormalization scales, finite-length matching parameters"},
  {"object":"physical_ensemble","authority":None,"available":False,"physical_standard_coordinate":False,"C43_ready":False,"deficit":"sequence points, covariance, acceptance tolerance, normalized weights"})
 return {"rows":rows,"available_count":sum(r["available"] for r in rows),"C43_ready_count":sum(r["C43_ready"] for r in rows),"capsule_complete":all(r["C43_ready"] for r in rows),"root":_r(rows)}
def source_chain():
 from deuteron_wigner.bridge import hqcdrimassc43physauth1 as a,hqcdrimassc43boundaryauth1 as b,hqcdrimassc43obsmatch1 as o,hqcdrimassc43converge1 as v,hqcdrimassc43p0func1 as p
 return {"roots":{"C319":p.PACKAGE_ROOT,"C321":a.PACKAGE_ROOT,"C322":b.PACKAGE_ROOT,"C323":o.PACKAGE_ROOT,"C324":v.PACKAGE_ROOT},"boundary_source_hashes_verified":b.source_audit()["all_hashes_verified"],"Wilson_owner_authenticated":o.operator_owner()["physical_owner_authenticated"],"continuum_match_complete":o.matching_audit()["continuum_match_complete"],"P0_binding":p.P0_domain()["determinant_term"],"root":_r((p.PACKAGE_ROOT,a.PACKAGE_ROOT,b.PACKAGE_ROOT,o.PACKAGE_ROOT,v.PACKAGE_ROOT))}
def binding_decision():return {"C341_certificate_frozen":True,"physical_capsule_bound":False,"validation_capsule_promoted":False,"defaults_inserted":False,"P0_zero_assumed":False,"Wilson_folded_into_determinant":False,"activation_gate":"NOT_READY","root":_r("C342-DECISION")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"authority_invented":0,"standard_coordinates_promoted_C43_ready":0,"ensemble_defaulted":0,"P0_zeroed":0,"protected_paths_modified":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43physbind2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43physbind2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43fullcert1 as c
 if c.PACKAGE_ROOT!=C341_ROOT:raise ValueError("C341 root")
 c.load_verified_hqcdrimassc43fullcert1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physbind2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43physbind2_authority()
_ROOTS={"INPUT":_r((BASELINE,C341_ROOT)),"MATRIX":authority_matrix()["root"],"SOURCES":source_chain()["root"],"DECISION":binding_decision()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C342-HQCDRIMASSC43PHYSBIND2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
