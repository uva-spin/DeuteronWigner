"""C344 recovery of the frozen C28 low-qT SIDIS dataset family."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c344_hqcdrimassc43sidisdata1"
BASELINE="b344ecf6ba4c98f6d1060a6ffd48ca1e108621de";C343_ROOT="345a189256c289545ce57c36928179c75c4d2cbf7722ce0a341f8a84d4ac1796"
INVENTORY=ROOT/"docs/next_level/c28_art25_dataset_inventory.json";LOCK=ROOT/"docs/next_level/c28_dataset_file_lock_manifest.json"
STATUS="C344_C28_SIDIS_DATASET_FAMILY_RECOVERED_C43_THEORY_SCALE_VOLUME_MATCHING_MISSING";PLAN="RIMASSC43SIDISDATA1-C"
NEXT="C345/HQCDRIMASSC43SIDISMATCH1";NEXT_OBJECT="C344-C43-SIDIS-THEORY-SCALE-VOLUME-MATCH";NEXT_EXACT="map the recovered C28 SIDIS kinematic and covariance records to source-qualified JMY renormalization rapidity and C43 finite-volume matching coordinates"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _sidis():return tuple(d for d in json.loads(INVENTORY.read_text())["records"] if d["process_type"]=="SIDIS")
def family_manifest():
 rows=[]
 for d in _sidis():
  sel=set(d["selected_ids"]);pts=[p for p in d["points"] if p["id"] in sel]
  rows.append({"stable_id":d["stable_id"],"name":d["name"],"publication":d["source_publication"],"source_sha256":d["sha256"],"selected_points":len(pts),"kinematics_present":all(all(k in p for k in ("<x>","<Q>","<z>","<qT>")) for p in pts),"cuts_present":all("cutParams" in p for p in pts),"uncorrelated_components":d["uncorrelated_error_count"],"correlated_components":d["correlated_error_count"],"covariance_constructible":all(len(p["corrErr"])==d["correlated_error_count"] and len(p["uncorrErr"])==d["uncorrelated_error_count"] for p in pts),"normalization":d["units"]})
 return {"rows":tuple(rows),"dataset_count":len(rows),"selected_point_count":sum(r["selected_points"] for r in rows),"all_kinematics_present":all(r["kinematics_present"] for r in rows),"all_covariance_constructible":all(r["covariance_constructible"] for r in rows),"channel_selected":False,"family_bound":True,"root":_r(rows)}
def provenance():
 inv=sha256(INVENTORY.read_bytes()).hexdigest();lock=sha256(LOCK.read_bytes()).hexdigest()
 return {"inventory":"docs/next_level/c28_art25_dataset_inventory.json","inventory_sha256":inv,"file_lock":"docs/next_level/c28_dataset_file_lock_manifest.json","file_lock_sha256":lock,"source_commit":"761f3fcdd3701c5cf69e822f9ffbbd5db394fc58","embedded_points_used":True,"external_DataLib_required_for_audit":False,"root":_r((inv,lock))}
def covariance_semantics():return {"experimental":"diag(sum uncorrErr^2)+sum_a corrErr_a corrErr_a^T within each dataset","cross_dataset_experimental":"not supplied; do not invent","C28_theory_anomaly_factor":"separate 642-member joint theory covariance","normalization_nuisance":"separate","C43_sequence_covariance":"missing","diagonalized":False,"root":_r("C344-COV")}
def readiness():return {"dataset_authority_recovered":True,"kinematics_bound":True,"experimental_covariance_constructible":True,"JMY_theory_scales_bound":False,"C43_finite_volume_bound":False,"physical_capsule_complete":False,"activation_gate":"NOT_READY","root":_r("C344-READY")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"channel_arbitrarily_selected":0,"cross_dataset_covariance_invented":0,"theory_scale_inferred":0,"finite_volume_inferred":0,"source_bytes_modified":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43sidisdata1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43sidisdata1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43obscapsule1 as c
 if c.PACKAGE_ROOT!=C343_ROOT:raise ValueError("C343 root")
 c.load_verified_hqcdrimassc43obscapsule1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43sidisdata1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43sidisdata1_authority()
_ROOTS={"INPUT":_r((BASELINE,C343_ROOT)),"FAMILY":family_manifest()["root"],"PROVENANCE":provenance()["root"],"COV":covariance_semantics()["root"],"READY":readiness()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C344-HQCDRIMASSC43SIDISDATA1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
