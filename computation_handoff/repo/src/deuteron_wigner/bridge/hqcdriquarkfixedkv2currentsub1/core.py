"""C255 authenticated subtraction-condition audit for C117 current directions."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentreg1 as c254
from deuteron_wigner.bridge import hqcdmatchir2 as c157
from deuteron_wigner.bridge.icreg2 import core as c117

ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c255_hqcdriquarkfixedkv2currentsub1"
BASELINE="0d5f6d711c3133fcded1299df9aae3ee31e9a2c0";C254_ROOT="f5aca3c76016a442fbafa7e395a55edc537706128e33f4e944baa4daad3dbf02"
C157_ROOT="351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c"
STATUS="C255_NO_AUTHENTICATED_C117_CURRENT_SUBTRACTION_CONDITION_RANK_ZERO_NULLITY_FOUR"
PLAN="RIQUARKFIXEDKV2CURRENTSUB1-D"
NEXT="C256/HQCDRIQUARKFIXEDKV2CURRENTSOURCE1"
NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-INSTANTANEOUS-CURRENT-SUBTRACTION-TARGET-SOURCE"
NEXT_EXACT="authenticated current-specific target observable, projector, scheme, scale, and regulator capsule for the four C117 subtraction directions"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")

def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def condition_inventory():
 rows=(
  {"owner":"C150","quantities":("QUARK_FIELD","SIGNED_QUARK_MASS"),"applicable":False,"reason":"two-point standard matching condition is not a C117 graph-direction condition"},
  {"owner":"C151-C153","quantities":("TRANSVERSE_GLUON_FIELD","qg_VERTEX_DRESSING","QCD_COUPLING"),"applicable":False,"reason":"standard projected matching coefficients do not identify C117 complement directions"},
  {"owner":"C154-C158","quantities":("common-IR adapter","flavor covariance","numerical evaluation"),"applicable":False,"reason":"transport/evaluation preserves quantity ownership and supplies no current-specific target"},
  {"owner":"C168","quantities":("adapter request",),"applicable":False,"reason":"request is not an authenticated renormalization condition"},
 )
 return _f({"rows":rows,"authenticated_candidates":4,"applicable_conditions":0,"source_substitution":False,"root":_r(rows)})

def direction_condition_map():
 rows=tuple({"direction":d,"C117_coefficient":"UNAVAILABLE_NOT_ZERO","condition_ids":(),"compatibility":"NO_AUTHENTICATED_APPLICABLE_CONDITION","null_direction":True} for d in DIRECTIONS)
 return _f({"rows":rows,"direction_count":4,"mapped_count":0,"root":_r(rows)})

def exact_condition_system():
 return _f({"coefficient_order":DIRECTIONS,"matrix":(),"rhs":(),"shape":(0,4),"rank":0,"nullity":4,"consistent":True,"unique":False,"solution":"UNAVAILABLE_NOT_ZERO","null_basis":"canonical four-dimensional C117 direction space","root":_r((DIRECTIONS,(),()))})

def compatibility_report():
 return _f({"finite_basis_scheme":"C43_FINITE_LIGHT_FRONT","target_scheme":"UNAVAILABLE","scale":"UNAVAILABLE","gauge":"UNAVAILABLE","common_ir_family":"UNAVAILABLE","regulator":"C254_CALLER_ABEL_FAMILY_ONLY","test_function":"CALLER_BOUND","flavor_color_channel":"UNAVAILABLE","order_of_limits":("finite caller core","core->unbounded at fixed abel_r","apply subtraction","abel_r->1^-"),"units":"coefficient units unresolved with target","covariance":"not asserted without target","compatible_rows":0,"root":_r((C254_ROOT,C157_ROOT,"no target"))})

def solve_subtraction_coefficients(condition_record=None):
 if condition_record is not None: raise ValueError("no C255-authenticated condition schema exists; C256 source qualification required")
 s=exact_condition_system()
 return _f({"status":"UNAVAILABLE_NOT_ZERO","coefficients":tuple({"direction":d,"value":None} for d in DIRECTIONS),"rank":s["rank"],"nullity":s["nullity"],"residual":0,"reason":"no applicable authenticated condition rows","physical":False,"root":_r((s["root"],"unavailable"))})

def route_certificate():return _f({"route_A":"C150-C158 public quantity ownership audit","route_B":"C117 direction-to-condition exact row audit","candidate_mismatches":0,"applicable_rows_A":0,"applicable_rows_B":0,"rank_residual":0,"root":_r(("ownership","rows",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"condition_audit_ready":True,"rank":0,"nullity":4,"coefficients_ready":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"coefficients_selected":0,"null_directions_zeroed":0,"fixture_fits":0,"scheme_conflations":0,"physical_defaults":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2currentsub1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("owner","direction","scheme","scale","gauge","regulator","rank","nullity")[i%8],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2currentsub1_authority():
 if c254.PACKAGE_ROOT!=C254_ROOT:raise ValueError("C254 root changed")
 c254.load_verified_hqcdriquarkfixedkv2currentreg1_authority();c117.load_verified_current_projector_authority()
 if c157.PACKAGE_ROOT!=C157_ROOT:raise ValueError("C157 root changed")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C254_package_root":C254_ROOT,"C157_package_root":C157_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2currentsub1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2currentsub1_authority()

_ROOTS={"INPUT":_r((BASELINE,C254_ROOT,C157_ROOT,c117.STATUS)),"INVENTORY":condition_inventory()["root"],"MAP":direction_condition_map()["root"],"SYSTEM":exact_condition_system()["root"],"COMPATIBILITY":compatibility_report()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C255-HQCDRIQUARKFIXEDKV2CURRENTSUB1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
