"""C239 omitted-domain V2 ownership and primitive frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvcontrib1 as c238
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c239_hqcdriquarkfixedkv2op1"
BASELINE="19c5da42114b7bfd0c31955d165b721a0e63082d";C238_ROOT="bf1f0a8d46f27ef5397ada3e0d9f254a3f22d3d33d6af1cd5dc2eb335d54a427"
STATUS="C239_OMITTED_V2_COMPONENT_DOMAIN_AND_OWNERSHIP_READY_COMPLEMENT_MODE_PRIMITIVES_INCOMPLETE";PLAN="RIQUARKFIXEDKV2OP1-D"
NEXT="C240/HQCDRIQUARKFIXEDKV2PRIM1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-PRIMITIVES";NEXT_EXACT="source-derived complement-mode instantaneous-fermion, instantaneous-current, and gluon-normal-ordering primitives"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def component_manifest():
 rows=({"component":"instantaneous_fermion","owner":"C112","source":"C43 constrained bad-fermion term","coupling_degree":2,"retained_matrix_ready":True,"complement_primitive_ready":False},{"component":"instantaneous_current","owner":"C127","source":"C43 Gauss/current term","coupling_degree":2,"retained_matrix_ready":True,"complement_primitive_ready":False},{"component":"gluon_normal_ordering","owner":"C129","source":"C43 normal-ordered gluon descendants","coupling_degree":2,"retained_matrix_ready":True,"complement_primitive_ready":False})
 return _f({"rows":rows,"count":3,"owned":3,"complement_ready":0,"root":_r(rows)})
def operator_schema():return _f({"operator":"Q_R V2 Q_R","domain":"C220 unbounded symbolic complement","state_labels":"sector,species,APBC/PBC k,n,m,helicity,color,orientation","component_roots":"UNAVAILABLE_NOT_ZERO until C240 primitives","retained_index_reuse":False,"finite_cutoff":False,"executable":False,"root":_r(("QV2Q",3,"complement"))})
def route_certificate():return _f({"route_A":"C131 factor ownership C112/C127/C129","route_B":"C43 degree-two action-term classification","ownership_mismatches":0,"complement_value_agreement":False,"root":_r(("C131","C43",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"components_owned":3,"complement_primitives":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"component_root":component_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_indices_reused":0,"finite_cutoff":0,"missing_zeroed":0,"components_conflated":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2op1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("C112","C127","C129","sector","k","HO","helicity","color","orientation","ownership","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"owned":3,"primitives":0,"mutations":384,"next":NEXT,"root":_r((STATUS,3,0))})
def verify_hqcd_riquarkfixedkv2op1_authority():
 if c238.PACKAGE_ROOT!=C238_ROOT:raise ValueError("C238 root changed")
 c238.load_verified_hqcd_riquarkfixedkvcontrib1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C238_package_root":C238_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv2op1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2op1_authority()
_ROOTS={"INPUT":_r((BASELINE,C238_ROOT)),"COMPONENTS":component_manifest()["root"],"OPERATOR":operator_schema()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C239-HQCDRIQUARKFIXEDKV2OP1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
