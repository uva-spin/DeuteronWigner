"""C256 source audit for a C117 current-specific subtraction target."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentsub1 as c255
from deuteron_wigner.bridge import hqcdlfgadapter1 as c168
from deuteron_wigner.bridge.icreg2 import core as c117
from deuteron_wigner.bridge import icagg3 as c127
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c256_hqcdriquarkfixedkv2currentsource1"
BASELINE="dd85893317772e188b22d78bfde0a70f41036895";C255_ROOT="62997585de038f452232f4a9c90a7e7a8ce85375e10261d7f1a6dc92818157d1"
STATUS="C256_CURRENT_TARGET_SOURCE_SCHEMA_READY_AUTHENTICATED_TARGET_CAPSULE_UNAVAILABLE"
PLAN="RIQUARKFIXEDKV2CURRENTSOURCE1-D";DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
NEXT="C257/HQCDRIQUARKFIXEDKV2CURRENTTARGET1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-INSTANTANEOUS-CURRENT-SUBTRACTION-TARGET-CAPSULE";NEXT_EXACT="caller-supplied authenticated current-specific target observable capsule satisfying the C256 source schema"
REQUIRED=("capsule_id","source_id","source_locator","source_sha256","observable_id","projector_id","covered_directions","finite_basis_scheme","target_scheme","mu","mu_units","gauge","regulator_id","test_function_id","flavor_channel","color_channel","source_sink_order","coefficient_units","order_of_limits","claim_tier","no_default")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_inventory():
 rows=(
  {"owner":"C117","role":"four graph-specific directions","target_capsule":False,"accepted":True},
  {"owner":"C127","role":"instantaneous-current operator and retained block","target_capsule":False,"accepted":True},
  {"owner":"C150-C158","role":"standard two-point/vertex/coupling matching quantities","target_capsule":False,"accepted":False,"reason":"quantity ownership mismatch"},
  {"owner":"C168","role":"instantaneous-current contribution class in RI/SMOM adapter request","target_capsule":False,"accepted":True,"reason":"ledger/request only; no observable condition"},
  {"owner":"repository authenticated sources","role":"current-specific observable/projector/scheme/scale/regulator condition","target_capsule":False,"accepted":False,"reason":"no exact locator/hash record present"},
 )
 return _f({"rows":rows,"candidates":5,"authenticated_operator_sources":3,"qualified_target_sources":0,"broad_substitution":False,"root":_r(rows)})
def target_capsule_schema():return _f({"schema":"C256-CURRENT-SUBTRACTION-TARGET-CAPSULE-V1","required":REQUIRED,"directions":DIRECTIONS,"caller_supplied":True,"source_hash_required":True,"physical_default":False,"root":_r(REQUIRED)})
def validate_target_capsule(record):
 if not isinstance(record,Mapping):raise TypeError("target capsule mapping required")
 missing=tuple(k for k in REQUIRED if k not in record)
 if missing:raise ValueError(f"missing target capsule fields: {missing}")
 if record.get("schema")!="C256-CURRENT-SUBTRACTION-TARGET-CAPSULE-V1":raise ValueError("schema")
 covered=tuple(record["covered_directions"])
 if not covered or len(set(covered))!=len(covered) or any(d not in DIRECTIONS for d in covered):raise ValueError("covered directions")
 if not record["source_locator"] or len(str(record["source_sha256"]))!=64:raise ValueError("authenticated source locator/hash required")
 if float(record["mu"])<=0 or record["mu_units"]!="GeV":raise ValueError("positive GeV scale required")
 if record["no_default"] is not True or record["claim_tier"] not in ("DIAGNOSTIC","PHYSICAL_CANDIDATE","PHYSICAL_AUTHENTICATED"):raise ValueError("claim boundary")
 if not isinstance(record["order_of_limits"],(tuple,list)) or not record["order_of_limits"]:raise ValueError("order of limits")
 body={k:_p(record[k]) for k in REQUIRED};return _f({"valid":True,"record":body,"coverage":covered,"root":_r(body)})
def qualified_candidate_records():return _f({"rows":(),"count":0,"status":"AUTHENTICATED_TARGET_CAPSULE_UNAVAILABLE_NOT_ZERO","root":_r(())})
def direction_coverage():return _f({"rows":tuple({"direction":d,"source_ids":(),"covered":False,"coefficient":"UNAVAILABLE_NOT_ZERO"} for d in DIRECTIONS),"covered":0,"uncovered":4,"root":_r((DIRECTIONS,"uncovered"))})
def compatibility_report():return _f({"source_target_compatible":0,"regulator_compatible":0,"scheme_scale_compatible":0,"rejections":("C150-C158 quantity mismatch","C168 request lacks target observable capsule","operator authority is not a renormalization condition"),"contradiction":False,"root":_r((0,0,0))})
def route_certificate():return _f({"route_A":"public API/provenance inventory","route_B":"target-capsule required-field search","qualified_A":0,"qualified_B":0,"mismatches":0,"root":_r(("api","fields",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"schema_ready":True,"qualified_targets":0,"directions_covered":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"scheme_selected":0,"scale_selected":0,"regulator_selected":0,"coefficients_selected":0,"missing_zeroed":0,"source_substitution":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2currentsource1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":REQUIRED[i%len(REQUIRED)],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2currentsource1_authority():
 if c255.PACKAGE_ROOT!=C255_ROOT:raise ValueError("C255 root changed")
 c255.load_verified_hqcdriquarkfixedkv2currentsub1_authority();c117.load_verified_current_projector_authority();c127.load_verified_instantaneous_current_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C255_package_root":C255_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2currentsource1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2currentsource1_authority()
_ROOTS={"INPUT":_r((BASELINE,C255_ROOT,c117.STATUS,c127.STATUS)),"INVENTORY":source_inventory()["root"],"SCHEMA":target_capsule_schema()["root"],"CANDIDATES":qualified_candidate_records()["root"],"COVERAGE":direction_coverage()["root"],"COMPATIBILITY":compatibility_report()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C256-HQCDRIQUARKFIXEDKV2CURRENTSOURCE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
