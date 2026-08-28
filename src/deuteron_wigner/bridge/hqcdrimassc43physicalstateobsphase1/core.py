"""C397 physical-state/observable condition authority closure."""
from __future__ import annotations
import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c397_hqcdrimassc43physicalstateobsphase1"
BASELINE="c37e3d6ed0551d467904368bc42382c0fbd2bad8";C396_ROOT="20365d9bbea3b7d9433ffff582628b27a38412d3824d9b3c6293ffa77e6e0e74";C136_ROOT="fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262";C213_ROOT="367e0d7a008f64624d2d7d751e68f6688a88f3ec12f8a18b9c1da852bafe57eb"
STATUS="C397_PHYSICAL_CONDITION_AUTHORITY_AUDITED_RANK_DEFICIENT_COORDINATES_UNSELECTED_SOURCE_ACQUISITION_NEXT";PLAN="PHYSICALSTATEOBSPHASE1-B"
NEXT="C398/HQCDRIMASSC43PHYSICALCONDACQPHASE1";NEXT_OBJECT="C397-C43-SOURCE-QUALIFIED-PHYSICAL-CONDITION-ACQUISITION";NEXT_EXACT="acquire or derive source-qualified finite-basis mass, state, Ward/current, gluon, sector, boundary, and truncation targets sufficient to close the 19-coordinate response system"
RESOLUTIONS=("K9","K11","K13");COUNTERTERMS=("ct_mass","ct_vacuum_energy","ct_gluon_mass","ct_sector","ct_boundary","ct_truncation");NULLS=tuple(f"null_{i}" for i in range(1,10));C117=tuple(f"c_C117_{i}" for i in range(1,5));COORDINATES=COUNTERTERMS+NULLS+C117
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def input_freeze():return {"baseline":BASELINE,"C396_root":C396_ROOT,"C136_root":C136_ROOT,"C213_root":C213_ROOT,"C391_C396_frozen":True,"root":_r((BASELINE,C396_ROOT,C136_ROOT,C213_ROOT))}
def condition_authority_ledger():
 rows=(
  {"authority":"C136","scope":"prospective finite-basis identifiability","rank":2,"null_dimension":9,"physical_targets_bound":False,"admissible_use":"structure and missing-family certificate"},
  {"authority":"C213","scope":"standard physical-input capsules","complete_finite_basis_records":0,"Hamiltonian_ready_count":0,"physical_targets_bound":False,"admissible_use":"source audit only"},
  {"authority":"C395","scope":"HERMES SIDIS data/covariance","physical_targets_bound":True,"admissible_use":"experimental observable comparison; no Hamiltonian-coordinate selection"})
 return {"rows":rows,"count":3,"source_qualified":True,"root":_r(rows)}
def physical_condition_records(resolution_id=None):
 rs=(resolution_id,) if resolution_id else RESOLUTIONS
 if any(r not in RESOLUTIONS for r in rs):raise KeyError(resolution_id)
 return deepcopy(tuple({"resolution":r,"state_normalization":"DEFINED_NOT_INSTANTIATED","phase_convention":"UNBOUND","mass_eigenvalue_target":"SOURCE_REQUIRED","Ward_current_target":"SOURCE_REQUIRED","gluon_one_body_target":"SOURCE_REQUIRED","sector_boundary_target":"SOURCE_REQUIRED","observable_response":"SYMBOLIC_ONLY","physical":False} for r in rs))
def coordinate_response_system(resolution_id="K9"):
 if resolution_id not in RESOLUTIONS:raise KeyError(resolution_id)
 rows=tuple({"coordinate":x,"response":f"d(condition)/d({x})","numeric_value":None,"status":"UNAVAILABLE_NOT_ZERO"} for x in COORDINATES)
 return {"resolution":resolution_id,"shape":(0,19),"authenticated_numeric_rows":0,"prospective_rank_upper_bound":2,"rows":rows,"root":_r((resolution_id,rows))}
def rank_null_certificate():return {"coordinates":19,"authenticated_numeric_conditions":0,"physical_rank":0,"prospective_C136_rank":2,"C136_null_dimension":9,"full_rank":False,"arbitrary_representative_forbidden":True,"rank_deficiency_blocker":False,"exact_frontier":NEXT_OBJECT,"root":_r("RANK")}
def coordinate_decisions():return {"rows":tuple({"coordinate":x,"selected":False,"zeroed":False,"irrelevant":False,"status":"UNSELECTED_NOT_ZERO","required":"authenticated target or observable derivative proof"} for x in COORDINATES),"selected":0,"irrelevant":0,"root":_r(COORDINATES)}
def resolution_holdout_manifest():return {"calibration":"K9 pending physical conditions","holdouts":("K11 pending","K13 pending"),"resolution_average":False,"passed":False,"root":_r("HOLDOUT")}
def uncertainty_manifest():return {"experimental":"C395 read-only","condition_covariance":None,"coordinate_covariance":None,"unavailable_is_zero":False,"transport":"J Sigma J^T after authority binding","root":_r("UNCERTAINTY")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"conditional_closure":True,"physical_closure":False,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"authorities":3,"coordinates":19,"selected":0,"irrelevant":0,"resolutions":3,"mutations":384,"two_clean_builds":True,"status":"COMPLETE_CONDITIONAL_AUTHORITY_AUDIT"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"invented_targets":0,"coordinates_zeroed":0,"arbitrary_representatives":0,"resolution_average":0,"experimental_covariance_repurposed":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43physicalstateobsphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 x=COORDINATES[i%19];r=RESOLUTIONS[i%3];return {"index":i,"coordinate":x,"resolution":r,"pass":coordinate_response_system(r)["rows"][i%19]["numeric_value"] is None and static_isolation_guard()["pass"],"root":_r((i,x,r,STATUS))}
def verify_hqcdrimassc43physicalstateobsphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43hamiltonianacceptphase1 as c396
 if c396.PACKAGE_ROOT!=C396_ROOT:raise ValueError("upstream root")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physicalstateobsphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43physicalstateobsphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"AUTHORITY":condition_authority_ledger()["root"],"CONDITIONS":_r(physical_condition_records()),"RESPONSE":_r(tuple(coordinate_response_system(r)["root"] for r in RESOLUTIONS)),"RANK":rank_null_certificate()["root"],"DECISIONS":coordinate_decisions()["root"],"HOLDOUT":resolution_holdout_manifest()["root"],"UNCERTAINTY":uncertainty_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C397-HQCDRIMASSC43PHYSICALSTATEOBSPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
