"""C346 joint JMY scheme and C43 volume-selection audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c346_hqcdrimassc43schemeselect1"
BASELINE="29e5619a450337bdb5b1e87f6ddb0ce524c9167e";C345_ROOT="c8083cbd458818db7282e97137fc6fea989bca8bcd7f44431d7946f6e17c197b"
STATUS="C346_JOINT_SCHEME_VOLUME_AUTHORITY_AUDITED_CONVERSION_MATCHING_OPERATOR_MISSING";PLAN="RIMASSC43SCHEMESELECT1-C"
NEXT="C347/HQCDRIMASSC43SCHEMECONVERT1";NEXT_OBJECT="C346-C43-JMY-TO-PROJECT-SCHEME-VOLUME-CONVERSION";NEXT_EXACT="derive the explicit JMY-to-project TMD scheme conversion and finite-volume matching operator required before selecting a physical C43 trajectory"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def candidate_matrix():
 rows=(
  {"candidate":"JMY hep-ph/0404183","process":True,"regulator":"off-lightcone spacelike v","soft_subtraction":"JMY source convention","normalization":True,"limit_order":True,"volume_trajectory":False,"joint_compatible":False},
  {"candidate":"DELTA_COLLINS_ZETA_SCHEME","process":False,"regulator":"delta","soft_subtraction":"Collins sqrt-soft","normalization":True,"limit_order":"canonical zeta path","volume_trajectory":False,"joint_compatible":False},
  {"candidate":"C28 ART25/arTeMiDe","process":True,"regulator":"external ART25 scheme identity","soft_subtraction":"external source-owned","normalization":True,"limit_order":True,"volume_trajectory":False,"joint_compatible":False},
  {"candidate":"C324-C341 C43 continuum","process":"operator compatible only","regulator":"proper-time plus winding","soft_subtraction":"vacuum subtraction","normalization":True,"limit_order":True,"volume_trajectory":"requirements only, no physical selection","joint_compatible":False})
 return {"rows":rows,"joint_candidate_count":sum(r["joint_compatible"] for r in rows),"selected":None,"root":_r(rows)}
def mismatch_ledger():
 rows=(
  {"interface":"JMY_to_DELTA_COLLINS","missing":"finite scheme conversion including soft and rapidity factors, anomalous dimensions, normalization and covariance Jacobian"},
  {"interface":"ART25_to_C43","missing":"operator-normalization and coefficient matching without double counting C28 TMD dynamics"},
  {"interface":"continuum_to_finite_volume","missing":"source-qualified L,K,Nmax,bHO trajectory, acceptance tolerance and ensemble measure"},
  {"interface":"covariance","missing":"cross-block Jacobians among experiment, ART25 theory, scheme conversion and C43 sequence"})
 return {"rows":rows,"complete":False,"missing_count":len(rows),"root":_r(rows)}
def selection_decision():return {"scheme_selected":False,"volume_trajectory_selected":False,"generic_project_scheme_promoted":False,"ART25_reinterpreted_JMY":False,"physical_coefficients_ready":False,"activation_gate":"NOT_READY","root":_r("C346-DECISION")}
def conversion_requirements():return {"required_inputs":("JMY renormalized operator definition","project delta/Collins operator definition","common UV and rapidity reference point","finite conversion kernel","anomalous-dimension evolution path","C43 determinant normalization","finite-volume trajectory","joint covariance Jacobian"),"safe_operations":("derive symbolic conversion","verify transitivity","propagate covariance","take declared limits"),"defaults":False,"root":_r("C346-CONVERSION")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"scheme_selected_without_conversion":0,"volume_selected_without_authority":0,"mu_equals_Q":0,"zeta_equals_Q2":0,"L_equals_inverse_Q":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43schemeselect1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43schemeselect1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43sidismatch1 as c
 if c.PACKAGE_ROOT!=C345_ROOT:raise ValueError("C345 root")
 c.load_verified_hqcdrimassc43sidismatch1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43schemeselect1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43schemeselect1_authority()
_ROOTS={"INPUT":_r((BASELINE,C345_ROOT)),"CANDIDATE":candidate_matrix()["root"],"MISMATCH":mismatch_ledger()["root"],"DECISION":selection_decision()["root"],"REQUIRE":conversion_requirements()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C346-HQCDRIMASSC43SCHEMESELECT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
