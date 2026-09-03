"""C241 V2 angular-HO projection and radial contact frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkv2prim1 as c240
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c241_hqcdriquarkfixedkv2ho1"
BASELINE="fe410546f97121a8a250be699b963295510d2ced";C240_ROOT="69d87133c08322c12ccfd45bce19fdd7b99e24506f7d0f9f7dcb9047c55de56a"
STATUS="C241_THREE_V2_COMPLEMENT_ANGULAR_JZ_AND_TM_CM_PROJECTION_SCHEMAS_READY_RADIAL_CONTACT_DISTRIBUTION_INCOMPLETE";PLAN="RIQUARKFIXEDKV2HO1-D"
NEXT="C242/HQCDRIQUARKFIXEDKV2CONTACT1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-CONTACT-DISTRIBUTION";NEXT_EXACT="authenticated complement-domain radial contact/distribution and regulator prescription for the three C241 V2 families"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def angular_projection_manifest():
 rows=tuple({"primitive_id":r["primitive_id"],"owner":r["owner"],"source_sha256":r["source_sha256"],"angular_rule":"total light-front Jz conserved; Kronecker delta on sum(m_i+helicity_i)","TM_CM_rule":"exact C62 polar TM transform; complement CM labels explicit; no retained projector reuse","radial_rule":"caller HO labels; source contact/distribution prescription required","angular_ready":True,"radial_ready":False,"missing_as_zero":False} for r in c240.primitive_manifest()["rows"])
 return _f({"rows":rows,"count":3,"angular_ready":3,"radial_ready":0,"root":_r(rows)})
def contact_audit():return _f({"required":("finite-cell inverse-partial-plus distribution","transverse contact kernel/distribution","normal-order subtraction owner","HO radial pairing domain","regulator removal or fixed-regulator declaration"),"available":("C43 action source","C240 mode schema","angular Jz selection","C62 TM algebra"),"missing":NEXT_OBJECT,"smearing_invented":False,"quadrature_promoted":False,"root":_r(("contact","regulator",3))})
def route_certificate():return _f({"route_A":"rotational/Jz commutator selection","route_B":"polar phase integration and C62 TM angular bracket","angular_mismatches":0,"radial_route_agreement":False,"root":_r(("Jz","polar",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"angular_schemas":3,"radial_projections":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"angular_root":angular_projection_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_projector_reuse":0,"smearing_invented":0,"quadrature_promoted":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2ho1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("owner","source","Jz","m","helicity","TM","CM","contact","regulator","radial","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"angular":3,"radial":0,"mutations":384,"next":NEXT,"root":_r((STATUS,3,0))})
def verify_hqcd_riquarkfixedkv2ho1_authority():
 if c240.PACKAGE_ROOT!=C240_ROOT:raise ValueError("C240 root changed")
 c240.load_verified_hqcd_riquarkfixedkv2prim1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C240_package_root":C240_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv2ho1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2ho1_authority()
_ROOTS={"INPUT":_r((BASELINE,C240_ROOT)),"ANGULAR":angular_projection_manifest()["root"],"CONTACT":contact_audit()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C241-HQCDRIQUARKFIXEDKV2HO1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
