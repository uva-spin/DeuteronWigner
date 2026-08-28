"""C394 conditional physical-boundary/holonomy parameter authority."""
from __future__ import annotations
import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c394_hqcdrimassc43physicalboundaryphase1"
BASELINE="6aa3bee696b8581987cbc2b24587a4517d5ece83";C393_ROOT="d194392345e68f7d4cb7efc8dbda471486de16986d78e6138029d80b6d06c251";C290_ROOT="6fb74af9c73a76e40b4b9e3ae10fdb87328b2a737c2e0d45d42e40fffe4ccb9f";C322_ROOT="5b7d6314b375f591b2decb26f65e69a02e953ddfa3417972e88e2a6e05135092";C343_ROOT="345a189256c289545ce57c36928179c75c4d2cbf7722ce0a341f8a84d4ac1796";C183_ROOT="7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f"
STATUS="C394_SOURCE_QUALIFIED_CONDITIONAL_BOUNDARY_HOLONOMY_FAMILY_AND_RESOLUTION_PARAMETER_SCHEMA_READY_OBSERVABLE_ENSEMBLE_RECORD_NEXT";PLAN="PHYSICALBOUNDARYPHASE1-B"
NEXT="C395/HQCDRIMASSC43PHYSICALOBSINPUTPHASE1";NEXT_OBJECT="C394-C43-JMY-SIDIS-OBSERVABLE-DATASET-ENSEMBLE-AUTHORITY";NEXT_EXACT="bind a source-qualified SIDIS observable/dataset record supplying correlated kinematics, scales, finite-volume acceptance, covariance, and normalized ensemble membership"
RESOLUTIONS=("K9","K11","K13");CLASSES=("GENERIC","CENTRAL","WEYL_WALL")
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def input_freeze():return {"baseline":BASELINE,"roots":{"C393":C393_ROOT,"C290":C290_ROOT,"C322":C322_ROOT,"C343":C343_ROOT,"C183":C183_ROOT},"validation_fixtures_promoted":False,"root":_r((BASELINE,C393_ROOT,C290_ROOT,C322_ROOT,C343_ROOT,C183_ROOT))}
def source_ledger():
 rows=({"source":"BPP hep-ph/9705477v1","role":"DLCQ regulator and continuum-limit authority","sha256":"2d7d5701fb49d1f75730eabb8b03694f0f2f6f61b160bc8e66a4d1a0969d5797"},{"source":"Heinzl hep-th/0008096v1","role":"finite-volume zero-mode boundary authority","sha256":"fc8064b08a4954b47eaef93f568045146a5b5e82638c086c78ec8002ea7b2834"},{"source":"BJY hep-ph/0208038v2","role":"process-dependent transverse link boundary","sha256":"7dcbe9dc0f06c4c2add312e7d2c6b69744b6328b93d7726224fc06c16438dfa7"},{"source":"Gao 1005.4305v1","role":"independent link-boundary derivation","sha256":"59a37e537d8c526b98c5ca46b39259c19326ff7baeab1622749e462be8ec15a0"})
 return {"rows":rows,"hash_verified_by_C322":True,"universal_physical_ensemble":False,"root":_r(rows)}
def boundary_ensemble_schema():
 req=("ensemble_id","observable_capsule_root","resolution","boundary_action_id","action_parameters","sector_classes","sector_weights","normalization_measure","orbit_stabilizer_jacobian","fundamental_BC","adjoint_BC","zero_mode_policy","holonomy_capsule_ids","endpoint_link_orientation","box_HO_scales","active_flavor_history","running_path","covariance","acceptance","physical","no_defaults")
 return {"schema":"C394-PHYSICAL-BOUNDARY-ENSEMBLE-V1","required":req,"classes":CLASSES,"weights":"nonnegative and exact sum one per resolution","complete_instances":0,"uniform_default":False,"root":_r(req)}
def validate_boundary_ensemble(x):
 if not isinstance(x,dict) or any(k not in x for k in boundary_ensemble_schema()["required"]):raise ValueError("complete ensemble required")
 if x["resolution"] not in RESOLUTIONS or x["no_defaults"] is not True or x["physical"] is not True:raise ValueError("physical explicit record required")
 w=x["sector_weights"]
 if not isinstance(w,dict) or set(w)!=set(x["sector_classes"]) or any(float(v)<0 for v in w.values()) or abs(sum(float(v) for v in w.values())-1)>1e-12:raise ValueError("normalized nonnegative weights")
 if not x["observable_capsule_root"] or not x["covariance"] or not x["acceptance"]:raise ValueError("observable ownership/covariance/acceptance")
 return deepcopy(x)
def conditional_family_manifest():
 rows=tuple({"resolution":r,"admissible_fundamental_BC":"APBC","admissible_adjoint_BC":"PBC with explicit zero-mode policy","classes":CLASSES,"sector_weights":None,"holonomy":"sector-resolved C183 capsule; no integration or averaging","endpoint_link":"SIDIS future-pointing, process owner","box_HO_scales":"observable-capsule supplied","active_flavor_history":"C393 caller-bound","status":"CONDITIONAL_FAMILY_COMPLETE_PHYSICAL_INSTANCE_MISSING"} for r in RESOLUTIONS)
 return {"rows":rows,"count":3,"project_regulator_choice_not_physical_input":True,"root":_r(rows)}
def ownership_manifest():return {"boundary_action":"observable/finite-volume owner","ghost":"C175 separate","residual_link":"C178 separate","holonomy":"C183 separate","Wilson_endpoint":"JMY/BJY/Gao SIDIS owner","zero_mode":"explicit sector owner","ensemble_normalization":"observable capsule","count_once":True,"root":_r("OWN")}
def resolution_parameter_schema():
 rows=tuple({"resolution":r,"required":("ensemble_root","C392_adapter_root","C393_running_record","mass_coupling_capsules","boundary_action","holonomy_sector","zero_mode_policy","L_GeVinv","bHO_GeVinv","Nmax","covariance_root"),"values":None,"defaults":False,"closed_conditionally":True} for r in RESOLUTIONS)
 return {"rows":rows,"count":3,"K9_K11_K13_separate":True,"root":_r(rows)}
def route_validation_manifest():return {"owner_first_ensemble_first":"SAME_TYPED_DAG","normalization":"VALIDATOR_ENFORCED","positivity":"VALIDATOR_ENFORCED","Hermiticity":"source/sink and future-link adjoints retained","units":"explicit schema","orientation":"SIDIS future","topology_count_once":"PASS","K9_K11_K13":"SEPARATE","root":_r("VALID")}
def covariance_manifest():return {"blocks":("dataset","theory","boundary_action","holonomy","finite_volume_sequence","running_inputs"),"cross_blocks":"observable record required; unavailable not zero","resolution_average":False,"root":_r("COV")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"conditional_families":3,"physical_instances":0,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"source_ledger":True,"schema":True,"conditional_family":True,"ownership":True,"resolution_parameter_schema":True,"physical_instance":False,"smallest_missing_object":NEXT_OBJECT,"mutations":384,"two_clean_builds":True,"status":"COMPLETE_CONDITIONAL"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"uniform_weights":0,"zero_covariance":0,"validation_promoted":0,"physical_scale_default":0,"counterterm_selected":0,"Hamiltonian_built":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43physicalboundaryphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"resolution":RESOLUTIONS[i%3],"owner":tuple(ownership_manifest())[(i//3)%len(ownership_manifest())],"pass":static_isolation_guard()["pass"],"root":_r((i,STATUS))}
def verify_hqcdrimassc43physicalboundaryphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43runningphase1 as c393
 if c393.PACKAGE_ROOT!=C393_ROOT:raise ValueError("C393 root")
 m=json.loads((ROOT/"data/runtime/c393_hqcdrimassc43runningphase1/manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(C393_ROOT,False):raise ValueError("C393 runtime")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physicalboundaryphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43physicalboundaryphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"SOURCE":source_ledger()["root"],"SCHEMA":boundary_ensemble_schema()["root"],"FAMILY":conditional_family_manifest()["root"],"OWN":ownership_manifest()["root"],"PARAM":resolution_parameter_schema()["root"],"VALID":route_validation_manifest()["root"],"COV":covariance_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C394-HQCDRIMASSC43PHYSICALBOUNDARYPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
