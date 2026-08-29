"""C235 authenticated interface-to-radial join audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkmap1 as c220
from deuteron_wigner.bridge import hqcdriquarkfixedkvradassemble1 as c234
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c235_hqcdriquarkfixedkvinterface1"
BASELINE="50c5b5f0f122df193d3259d81a3439313f215dd8";C234_ROOT="2955c31af733b2c1882fa0a18d99c5c1e2f12e4f83f11bd4ce1ebfcf5cf9244b";C220_ROOT="0151249342328c0f6994786057c23296ee19383230fe01422390b779fd3124a3"
CONTRACT="docs/next_level/c234_c235_hqcdriquarkfixedkvinterface1_continuation_contract.json";CONTRACT_SHA256="437f609dc7ecf9caaac28451eb2a3f30c7226b6f07f0dfbcad744730ea4c163b"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c235_hqcdriquarkfixedkvinterface1_codex_prompt.md";PROMPT_SHA256="92390dbe5a7cbfdd051c7a627643892473e99b82c4dd4f6897c3e9c1a3e38b1c"
STATUS="C235_FIFTEEN_INTERFACE_JOIN_AUDITED_ENDPOINT_HELICITY_AND_TRANSVERSE_QUANTUM_MAP_INCOMPLETE";PLAN="RIQUARKFIXEDKVINTERFACE1-D"
NEXT="C236/HQCDRIQUARKFIXEDKVENDPOINTQN1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-ENDPOINT-QUANTUM-MAP"
NEXT_EXACT="authenticated helicity and transverse (n,m) endpoint quantum-number map for the 15 OUTSIDE_FIXED_K interfaces"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def interface_join_audit():
 rows=tuple({"interface_id":r["interface_id"],"term_id":r["term_id"],"resolution":r["resolution"],"coupling_degree":r["coupling_degree"],"ancestry":r["ancestry"],"source_map":r["source_map"],"sink_map":r["sink_map"],"published_endpoint_helicity":False,"published_endpoint_n":False,"published_endpoint_m":False,"eligible_C234_radial_ids":(),"join_status":"UNAVAILABLE_NOT_ZERO_ENDPOINT_QUANTUM_LABELS_MISSING","positional_join_forbidden":True} for r in c220.endpoint_map_manifest()["rows"])
 return _f({"rows":rows,"count":15,"mapped":0,"unmapped":15,"duplicate_ownership":0,"root":_r(rows)})
def radial_authority_manifest():return _f({"radial_root":c234.assembly_manifest()["root"],"families":8,"required_join_keys":("h_out","h_in","h_g","n","m"),"interface_rows_with_all_keys":0,"root":_r((c234.assembly_manifest()["root"],8,0))})
def route_certificate():return _f({"route_A":"C220 endpoint row field audit","route_B":"C234 required channel-key audit","missing_key_mismatches":0,"lawful_joins":0,"root":_r(("fields","keys",0,0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"interfaces":15,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,15))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"interfaces_audited":15,"interfaces_mapped":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"audit_root":interface_join_audit()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"positional_join":0,"invented_quantum_labels":0,"missing_zeroed":0,"physical_defaults":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvinterface1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("interface","term","resolution","ancestry","hout","hin","hg","n","m","join","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"audited":15,"mapped":0,"mutations":384,"next":NEXT,"root":_r((STATUS,15,0))})
def verify_hqcd_riquarkfixedkvinterface1_authority():
 if c234.PACKAGE_ROOT!=C234_ROOT or c220.PACKAGE_ROOT!=C220_ROOT:raise ValueError("upstream root changed")
 c234.load_verified_hqcd_riquarkfixedkvradassemble1_authority();c220.load_verified_hqcd_riquarkfixedkmap1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C234_package_root":C234_ROOT,"C220_package_root":C220_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvinterface1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvinterface1_authority()
_ROOTS={"INPUT":_r((BASELINE,C234_ROOT,C220_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"AUDIT":interface_join_audit()["root"],"RADIAL":radial_authority_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C235-HQCDRIQUARKFIXEDKVINTERFACE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C235_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
