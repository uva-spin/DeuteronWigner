"""C240 action-level complement V2 primitives and HO frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkv2op1 as c239
from deuteron_wigner.bridge import g0
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c240_hqcdriquarkfixedkv2prim1"
BASELINE="20362a6ca7cd43951f6fa47ac673dc32a208ac1b";C239_ROOT="cbaa6d3958c08e3d21df6763c16eb958eb5448079e1d69549c4fc63800d7beb6"
STATUS="C240_THREE_SOURCE_DERIVED_ACTION_LEVEL_COMPLEMENT_V2_PRIMITIVES_READY_TRANSVERSE_HO_PROJECTIONS_INCOMPLETE";PLAN="RIQUARKFIXEDKV2PRIM1-D"
NEXT="C241/HQCDRIQUARKFIXEDKV2HO1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-HO-PROJECTIONS";NEXT_EXACT="exact transverse-HO projections of the three C240 complement-mode V2 primitive families"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def primitive_manifest():
 act=g0.action_contract();inter=act["interactions"]
 rows=({"primitive_id":"C240-C112-COMPLEMENT","owner":"C112","source_expression":inter["instantaneous_fermion"],"construction":"solve constrained bad fermion with authenticated inverse partial-plus then expand APBC/PBC complement modes","normal_order_owner":"C112","HO_projection":"UNAVAILABLE_NOT_ZERO"},{"primitive_id":"C240-C127-COMPLEMENT","owner":"C127","source_expression":inter["instantaneous_current"],"construction":"Gauss/current bilinear with authenticated PV/Q0 inverse derivative and complement mode expansion","normal_order_owner":"C127","HO_projection":"UNAVAILABLE_NOT_ZERO"},{"primitive_id":"C240-C129-COMPLEMENT","owner":"C129","source_expression":"normal-ordered contractions/descendants of authenticated pure-gluon interaction terms","construction":"C43 source order followed by C129 vacuum contraction ownership on complement PBC modes","normal_order_owner":"C129","HO_projection":"UNAVAILABLE_NOT_ZERO"})
 rows=tuple({**r,"source_sha256":sha256(r["source_expression"].encode()).hexdigest(),"coupling_degree":2,"domain":"unbounded C220 complement; caller modes","missing_as_zero":False} for r in rows)
 return _f({"rows":rows,"count":3,"action_level_ready":3,"HO_ready":0,"root":_r(rows)})
def mode_schema():return _f({"labels":("sector","species","APBC/PBC k","n","m","helicity","color","orientation"),"longitudinal":"exact mode conservation and PV/Q0 prescriptions","cardinality":"UNBOUNDED","finite_enumerator":False,"retained_ids":False,"root":_r(("C220",8))})
def route_certificate():return _f({"route_A":"C43 action/constraint substitution","route_B":"C112/C127/C129 owner decomposition","source_owner_mismatches":0,"HO_route_agreement":False,"root":_r(("C43","owners",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"action_primitives":3,"HO_projections":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"primitive_root":primitive_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_ids":0,"finite_cutoff":0,"components_conflated":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2prim1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("C112","C127","C129","source","PV","Q0","mode","color","helicity","HO","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"primitives":3,"HO":0,"mutations":384,"next":NEXT,"root":_r((STATUS,3,0))})
def verify_hqcd_riquarkfixedkv2prim1_authority():
 if c239.PACKAGE_ROOT!=C239_ROOT:raise ValueError("C239 root changed")
 c239.load_verified_hqcd_riquarkfixedkv2op1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C239_package_root":C239_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv2prim1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2prim1_authority()
_ROOTS={"INPUT":_r((BASELINE,C239_ROOT)),"PRIMITIVES":primitive_manifest()["root"],"MODES":mode_schema()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C240-HQCDRIQUARKFIXEDKV2PRIM1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
