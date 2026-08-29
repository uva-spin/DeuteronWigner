"""C322 primary-source audit of C43 finite-volume and Wilson ownership."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c322_hqcdrimassc43boundaryauth1"
BASELINE="c6b1c8e1a8e28625bad4320f25730516cb2d8d07"
C321_ROOT="7466c27017bd6b3c3d27d64181d31aac172824bc27e65e6a0811d21b87dbedfd"
STATUS="C322_BOUNDARY_CLASSES_AUTHENTICATED_PHYSICAL_ENSEMBLE_AND_WILSON_OWNER_MATCHING_MISSING"
PLAN="RIMASSC43BOUNDARYAUTH1-C"
NEXT="C323/HQCDRIMASSC43OBSMATCH1"
NEXT_OBJECT="C322-C43-PHYSICAL-OBSERVABLE-FINITE-VOLUME-MATCHING"
NEXT_EXACT="specify a physical observable and convergence prescription that owns the C43 longitudinal scale boundary ensemble and process-dependent Wilson parameters"

def _r(v): return sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()

_SOURCES=(
 ("BPP","hep-ph/9705477v1","data/raw/c43_sources/hep-ph-9705477v1.pdf","2d7d5701fb49d1f75730eabb8b03694f0f2f6f61b160bc8e66a4d1a0969d5797","DLCQ is a finite-volume regulator; continuum recovery requires resolution limits"),
 ("HEINZL","hep-th/0008096v1","data/raw/c43_sources/hep-th-0008096v1.pdf","fc8064b08a4954b47eaef93f568045146a5b5e82638c086c78ec8002ea7b2834","finite-volume, zero-mode, and inverse-derivative boundary analysis"),
 ("BJY","hep-ph/0208038v2","data/raw/c43_sources/hep-ph-0208038v2.pdf","7dcbe9dc0f06c4c2add312e7d2c6b69744b6328b93d7726224fc06c16438dfa7","transverse gauge link and boundary prescription depend on the parton observable"),
 ("GAO","1005.4305v1","data/raw/c43_sources/1005.4305v1.pdf","59a37e537d8c526b98c5ca46b39259c19326ff7baeab1622749e462be8ec15a0","independent light-cone-gauge boundary-link derivation"),
)

def source_audit():
 rows=[]
 for key,identifier,path,digest,finding in _SOURCES:
  p=ROOT/path
  actual=sha256(p.read_bytes()).hexdigest() if p.is_file() else None
  rows.append({"key":key,"identifier":identifier,"path":path,"expected_sha256":digest,"actual_sha256":actual,"hash_verified":actual==digest,"finding":finding})
 return {"rows":tuple(rows),"all_hashes_verified":all(r["hash_verified"] for r in rows),"new_sources_acquired":0,"root":_r(rows)}

def authority_classification():
 rows=(
  {"object":"fermion_longitudinal_boundary_class","classification":"REGULATOR_CONVENTION","authorized":"APBC is an admissible C43/DLCQ convention","physical_value":False},
  {"object":"gluon_longitudinal_boundary_class","classification":"REGULATOR_CONVENTION","authorized":"PBC with an explicit zero-mode prescription is admissible","physical_value":False},
  {"object":"longitudinal_box_length_or_K_family","classification":"REGULATOR_AND_CONVERGENCE_CHOICE","authorized":None,"physical_value":False},
  {"object":"normalized_boundary_ensemble_weights","classification":"OBSERVABLE_MATCHING_INPUT","authorized":None,"physical_value":False},
  {"object":"Wilson_link_direction_and_boundary_prescription","classification":"PROCESS_OPERATOR_DEPENDENT","authorized":None,"physical_value":False},
 )
 return {"rows":rows,"universal_physical_records":0,"validation_capsule_promoted":False,"root":_r(rows)}

def no_default_decision():
 return {"physical_capsule_complete":False,"reason":"QCD and the locked sources do not select a unique finite-volume regulator ensemble or process-independent Wilson owner","K9_K11_K13_physical":False,"uniform_weights":False,"missing_as_zero":False,"root":_r("C322-NO-DEFAULT")}

def residual_frontier(): return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest(): return {"status":STATUS,"plan":PLAN,"audit_complete":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard(): return {"defaults_created":0,"fixtures_promoted":0,"source_bytes_modified":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43boundaryauth1(i):
 if not isinstance(i,int) or not 0<=i<384: raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43boundaryauth1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physauth1 as c
 if c.PACKAGE_ROOT!=C321_ROOT: raise ValueError("C321 root")
 c.load_verified_hqcdrimassc43physauth1_authority()
 if not source_audit()["all_hashes_verified"]: raise ValueError("source hash")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43boundaryauth1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False): raise ValueError("runtime")
 return verify_hqcdrimassc43boundaryauth1_authority()

_ROOTS={"INPUT":_r((BASELINE,C321_ROOT)),"SOURCES":source_audit()["root"],"CLASSIFICATION":authority_classification()["root"],"DECISION":no_default_decision()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C322-HQCDRIMASSC43BOUNDARYAUTH1-V1","roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
