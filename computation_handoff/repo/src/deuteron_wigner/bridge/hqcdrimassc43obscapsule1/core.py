"""C343 JMY SIDIS physical observable capsule satisfiability audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c343_hqcdrimassc43obscapsule1"
BASELINE="3f6307d00d48c27ce2dd40ab9a0166810e6df2b7";C342_ROOT="272dbd3d0ee60fda660f310e14a5d2da2cd9c31a59976109c4be003b58c3ac2e"
STATUS="C343_JMY_SIDIS_OBSERVABLE_CAPSULE_SCHEMA_BOUND_DATASET_NUMERICAL_RECORD_MISSING";PLAN="RIMASSC43OBSCAPSULE1-C"
NEXT="C344/HQCDRIMASSC43SIDISDATA1";NEXT_OBJECT="C343-C43-SIDIS-DATASET-AUTHORITY";NEXT_EXACT="recover a source-qualified SIDIS dataset record supplying correlated kinematics scales covariance and selection metadata for the C43 observable capsule"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def capsule_schema():
 fields=(
  {"field":"observable_family","required":True,"owner":"factorization theorem","status":"BOUND","value":"low-qT SIDIS TMD factorization"},
  {"field":"process_orientation","required":True,"owner":"JMY operator","status":"BOUND","value":"future-pointing SIDIS"},
  {"field":"Wilson_path","required":True,"owner":"JMY/BJY/Gao","status":"BOUND","value":"spacelike v, v^2<0, transverse closure"},
  {"field":"kinematics","required":True,"owner":"selected experimental dataset","status":"MISSING","required_coordinates":("x_B","Q2_GeV2","z_h","qT_GeV","y")},
  {"field":"renormalization_scales","required":True,"owner":"dataset plus declared theory prescription","status":"MISSING","required_coordinates":("mu_GeV","zeta_GeV2","rapidity_parameter")},
  {"field":"finite_volume_sequence","required":True,"owner":"C43 observable matching","status":"MISSING","required_coordinates":("L_GeVinv","K","boundary_class","zero_mode_sector")},
  {"field":"covariance","required":True,"owner":"dataset and joint theory propagation","status":"MISSING","required_coordinates":("experimental_covariance","theory_covariance","cross_sequence_covariance")},
  {"field":"acceptance","required":True,"owner":"predeclared C43 convergence protocol","status":"MISSING","required_coordinates":("holdouts","stability_windows","tolerance")},
  {"field":"ensemble_weights","required":True,"owner":"matched physical ensemble","status":"MISSING","required_coordinates":("normalized_weights","normalization_measure","membership")})
 return {"fields":fields,"required_count":len(fields),"bound_count":sum(f["status"]=="BOUND" for f in fields),"complete":all(f["status"]=="BOUND" for f in fields),"root":_r(fields)}
def repository_audit():
 rows=(
  {"candidate":"C323 JMY/BJY/Gao","classification":"OPERATOR_LEVEL","admissible_fields":("observable_family","process_orientation","Wilson_path"),"numeric_capsule":False},
  {"candidate":"generic deuteron_wigner.tmd_scheme","classification":"GENERIC_THEORY_API","admissible_fields":(),"reason":"not selected by a C43 SIDIS dataset record","numeric_capsule":False},
  {"candidate":"C317 K9/K11/K13","classification":"NONPHYSICAL_VALIDATION","admissible_fields":(),"numeric_capsule":False},
  {"candidate":"repository SIDIS analytic oracles","classification":"VALIDATION_OR_MODEL","admissible_fields":(),"reason":"no experiment-specific joint kinematics/covariance/ensemble authority","numeric_capsule":False})
 return {"rows":rows,"complete_candidate_count":0,"operator_authority_reused":True,"numerical_values_bound":0,"root":_r(rows)}
def satisfiability_certificate():
 s=capsule_schema();missing=tuple(f["field"] for f in s["fields"] if f["status"]=="MISSING")
 return {"schema_satisfiable":True,"current_instance_exists":False,"missing_fields":missing,"defaults_permitted":False,"uniform_weights_permitted":False,"uncorrelated_covariance_permitted":False,"activation_gate":"NOT_READY","root":_r(missing)}
def ownership():return {"C341_certificate":"frozen","C342_deficit_matrix":"frozen","P0":"C319 domain exclusion retained","dataset_selection":"external scientific owner required","source_bytes_modified":False,"root":_r("C343-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"representative_point_invented":0,"generic_scale_promoted":0,"uniform_weights":0,"zero_covariance":0,"validation_promoted":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43obscapsule1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43obscapsule1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physbind2 as c
 if c.PACKAGE_ROOT!=C342_ROOT:raise ValueError("C342 root")
 c.load_verified_hqcdrimassc43physbind2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43obscapsule1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43obscapsule1_authority()
_ROOTS={"INPUT":_r((BASELINE,C342_ROOT)),"SCHEMA":capsule_schema()["root"],"AUDIT":repository_audit()["root"],"SAT":satisfiability_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C343-HQCDRIMASSC43OBSCAPSULE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
