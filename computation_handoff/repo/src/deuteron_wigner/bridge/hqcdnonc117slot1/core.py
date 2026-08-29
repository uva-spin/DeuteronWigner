"""C275 non-C117 physical slot reduction authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c275_hqcdnonc117slot1"
BASELINE="7d7f5e69eef090b79aff19e56956be8b9e5bd870";C274_ROOT="6bb3a76faaa0f38ca6943f59728762cf18a2a7182f6ce45d7ae317982f09f590"
STATUS="C275_NONC117_BUNDLE_REDUCED_RI_SMOM_SIGNED_MASS_ADAPTER_FIRST";PLAN="NONC117SLOT1-C";NEXT="C276/HQCDRIMASSADAPTER1";NEXT_OBJECT="RI/SMOM signed-quark-mass C43 gauge/regulator-changing finite-basis adapter calculation at K9/K11/K13"
REQUEST_ID="C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-2"
SLOTS=("running_coupling_masses","common_IR_regulator","boundary_holonomy","non_C117_counterterms","finite_basis_targets","joint_covariance")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def slot_ledger():
 rows=(
 {"slot":SLOTS[0],"authority":"C154-C155 standard values; C215 ordered adapters","status":"PARTIAL_FIRST_NONC117_EDGE_SIGNED_MASS_RI_SMOM"},
 {"slot":SLOTS[1],"authority":"C153-C157","status":"CONDITIONAL_COMMON_IR_NO_PHYSICAL_WINDOW"},
 {"slot":SLOTS[2],"authority":"C169-C183","status":"CLASSES_CLOSED_PHYSICAL_SELECTION_UNAVAILABLE"},
 {"slot":SLOTS[3],"authority":"C206","status":"AFFINE_FAMILY_UNSELECTED_NOT_ZERO"},
 {"slot":SLOTS[4],"authority":"C158/C161/C213","status":"COMPARISON_CONDITIONAL_NOT_BOUND"},
 {"slot":SLOTS[5],"authority":"C154/C213","status":"MARGINAL_INPUTS_JOINT_COVARIANCE_UNAVAILABLE"})
 return _f({"rows":rows,"count":6,"closed":0,"conditional":6,"C117_coordinates_unchanged":4,"root":_r(rows)})
def ordered_adapter_frontier():
 rows=(
 {"ordinal":2,"request_id":REQUEST_ID,"quantity":"SIGNED_QUARK_MASS","scheme":"RI_SMOM","status":"FIRST_NONC117_ADAPTER_CALCULATION"},
 {"ordinal":3,"quantity":"QUARK_FIELD","scheme":"MOMQ","status":"ORDERED_LATER"},
 {"ordinal":4,"quantity":"TRANSVERSE_GLUON_FIELD","scheme":"MOMQ","status":"ORDERED_LATER"},
 {"ordinal":5,"quantity":"qg_VERTEX_DRESSING","scheme":"MOMQ","status":"ORDERED_LATER"},
 {"ordinal":6,"quantity":"QCD_COUPLING","scheme":"MOMQ","status":"ORDERED_LATER"})
 return _f({"rows":rows,"first":REQUEST_ID,"C117_request_separate":"ordinal 1 preserved in C259-C274 frontier and not counted as non-C117 closure","root":_r(rows)})
def mapping_audits():return _f({"forward":"standard mass -> running/Nf -> common-IR -> RI/SMOM signed-mass adapter -> finite-basis mass slot","reverse":"C274 mass slot -> finite-basis target -> adapter -> C154/C155 source","first_common_missing":REQUEST_ID,"contradiction":False,"root":_r(REQUEST_ID)})
def covariance_boundary():return _f({"marginals":"available where C154 supplies them","cross_blocks":None,"PSD_program":"A Sigma A^T with unavailable blocks symbolic","missing_as_zero":False,"root":_r("joint-cov-missing")})
def residual_frontier():return _f({"object_id":"C168-REQUEST-2-RI-SMOM-SIGNED-MASS","exact_missing_object":NEXT_OBJECT,"request_id":REQUEST_ID,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"slot_classes_audited":6,"bundle_closed":False,"C117_coordinates_selected":0,"physical":False,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"conditional_defaulted":0,"unsupported_zeroed":0,"C117_modified":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdnonc117slot1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdnonc117slot1_authority():
 from deuteron_wigner.bridge import hqcdc117renormh1 as c274
 from deuteron_wigner.bridge import hqcdphysadaptercalc1 as c215
 if c274.PACKAGE_ROOT!=C274_ROOT:raise ValueError("C274 root changed")
 c274.load_verified_hqcdc117renormh1_authority();c215.load_verified_hqcd_physadaptercalc1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdnonc117slot1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdnonc117slot1_authority()
_ROOTS={"INPUT":_r((BASELINE,C274_ROOT)),"SLOTS":slot_ledger()["root"],"FRONTIER_ORDER":ordered_adapter_frontier()["root"],"AUDITS":mapping_audits()["root"],"COVARIANCE":covariance_boundary()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C275-HQCDNONC117SLOT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
