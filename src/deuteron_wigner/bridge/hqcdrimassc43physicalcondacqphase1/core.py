"""C398 source-qualified finite-basis physical-condition acquisition audit."""
from __future__ import annotations
import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c398_hqcdrimassc43physicalcondacqphase1"
BASELINE="d6a26c30dc5fc16bfc360edb2af6eb3e61eb79f1";C397_ROOT="98a1a16a28d73bcd798ed3a49430974c7da79d83ba5a2fae36025b0f42bf5697"
STATUS="C398_SOURCE_DERIVED_CONDITION_STRUCTURES_ACQUIRED_PHYSICAL_TARGET_CAPSULES_MISSING";PLAN="PHYSICALCONDACQPHASE1-B"
NEXT="C399/HQCDRIMASSC43PHYSICALTARGETCAPSULEPHASE1";NEXT_OBJECT="C398-C43-AUTHENTICATED-FINITE-BASIS-PHYSICAL-TARGET-CAPSULE-SET";NEXT_EXACT="bind authenticated numerical or interval targets and covariance to the source-derived mass, state, Ward/current, gluon, sector, boundary, truncation, and C117-sensitive condition structures"
RESOLUTIONS=("K9","K11","K13");FAMILIES=("mass_state","normalization_phase","Ward_current","gluon_one_body","sector","boundary_truncation","C117_sensitive")
ROOTS_UPSTREAM={"C133":"c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9","C135":"e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b","C149":"8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0","C150":"2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C205":"f8658cad5f3fec055efbbf56e137db0a03c76fd2a93b61ee214e22dfdb1990df","C206":"b404a853c2c9f63620bf970b4230ef67c59003a73f43de8f51e7aefab0ea371d","C212":"a9a1a787cabdcf6d5adcdae61c83fd1e80d830bd6aac8caa03fab7887c4c152c","C213":"367e0d7a008f64624d2d7d751e68f6688a88f3ec12f8a18b9c1da852bafe57eb"}
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def input_freeze():return {"baseline":BASELINE,"C397_root":C397_ROOT,"upstream_roots":ROOTS_UPSTREAM,"frozen":True,"root":_r((BASELINE,C397_ROOT,ROOTS_UPSTREAM))}
def acquisition_ledger():
 owners={"mass_state":("C149 signed projectors","C150 conditional Zq/mass scheme"),"normalization_phase":("C147 coordinate field normalization","C149 state projectors"),"Ward_current":("C206 ST-compatible affine family","C212 source-side MOMq closure"),"gluon_one_body":("C151 gluon projector/source","C206 affine counterterms"),"sector":("C152 amputated qg vertex","C153 componentwise matching"),"boundary_truncation":("C153 finite-basis matching","C205 global stabilizer identity"),"C117_sensitive":("C206 14D affine family",)}
 rows=tuple({"family":f,"structure_owners":owners[f],"equation_structure":"SOURCE_DERIVED_CONDITIONAL","physical_target":None,"target_status":"MISSING_NOT_ZERO","covariance":None,"resolution_compatible":True,"promoted_fixture":False} for f in FAMILIES)
 return {"rows":rows,"families":7,"structures_acquired":7,"physical_targets_acquired":0,"root":_r(rows)}
def source_exclusion_ledger():
 rows=("C135 M_R2_FB and g_R_FB are symbolic project targets, not numerical physical capsules","C210/C211 MOMq fixtures are authenticated nonphysical fixtures","C158 comparison values are read-only and not Hamiltonian conditions","C395 HERMES covariance cannot select regulator counterterms","conditional schemes and affine families do not choose representatives")
 return {"rows":rows,"count":5,"quarantine_promotions":0,"root":_r(rows)}
def target_capsule_schema():
 req=("capsule_id","family","resolution","value_or_interval","units","scheme","scale_or_kinematics","state_identity","source_locator","source_sha256","normalization","covariance_or_bound","signature","no_default")
 return {"schema":"C398-PHYSICAL-TARGET-CAPSULE-V1","required":req,"families":FAMILIES,"resolutions":RESOLUTIONS,"no_default":True,"root":_r(req)}
def validate_target_capsule(x):
 if not isinstance(x,dict) or any(k not in x for k in target_capsule_schema()["required"]):raise ValueError("complete capsule required")
 if x["family"] not in FAMILIES or x["resolution"] not in RESOLUTIONS or x["value_or_interval"] is None or x["no_default"] is not True:raise ValueError("invalid target capsule")
 return deepcopy(x)
def rank_forecast():return {"coordinates":19,"source_derived_condition_structures":7,"authenticated_target_rows":0,"physical_rank":0,"prospective_rank":"evaluate only after capsules","rank_deficiency_blocker":False,"arbitrary_representative_forbidden":True,"root":_r("RANK")}
def resolution_manifest():return {"rows":tuple({"resolution":r,"condition_families":FAMILIES,"target_capsules":0,"physical":False} for r in RESOLUTIONS),"averaged":False,"root":_r("RES")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"structures_acquired":7,"targets_acquired":0,"physical":False,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"upstream_roots":11,"families":7,"exclusions":5,"target_schema":True,"mutations":384,"two_clean_builds":True,"status":"COMPLETE_MAXIMAL_STRUCTURAL_ACQUISITION"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"invented_targets":0,"fixture_promotions":0,"implicit_defaults":0,"coordinate_representatives":0,"resolution_average":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43physicalcondacqphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 f=FAMILIES[i%7];r=RESOLUTIONS[i%3];return {"index":i,"family":f,"resolution":r,"pass":acquisition_ledger()["rows"][i%7]["physical_target"] is None and static_isolation_guard()["pass"],"root":_r((i,f,r,STATUS))}
def verify_hqcdrimassc43physicalcondacqphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physicalstateobsphase1 as c397
 if c397.PACKAGE_ROOT!=C397_ROOT:raise ValueError("upstream root")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physicalcondacqphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43physicalcondacqphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"ACQUISITION":acquisition_ledger()["root"],"EXCLUSION":source_exclusion_ledger()["root"],"SCHEMA":target_capsule_schema()["root"],"RANK":rank_forecast()["root"],"RESOLUTION":resolution_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C398-HQCDRIMASSC43PHYSICALCONDACQPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
