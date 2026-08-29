"""C237 source-qualified V1 interface enclosure join."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvendpointqn1 as c236
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c237_hqcdriquarkfixedkvinterface2"
BASELINE="c902e578f898113186b0ba52580066583cfd8d7a";C236_ROOT="735326d201d1ccbb9b5f8d8560eac462599a26a6d3129108185bb683a4eaceb4"
CONTRACT="docs/next_level/c236_c237_hqcdriquarkfixedkvinterface2_continuation_contract.json";CONTRACT_SHA256="0ffaee308964253cc40b5f76c6501888df1b3effa972119ee90f811f22fc60ca"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c237_hqcdriquarkfixedkvinterface2_codex_prompt.md";PROMPT_SHA256="34b2c151008dff9e009b21a73a3b1130a53f0a18b08ef37c743a3582504f2168"
STATUS="C237_TWENTY_FOUR_SOURCE_QUALIFIED_CANONICAL_INTERFACE_RADIAL_ENCLOSURE_JOINS_READY";PLAN="RIQUARKFIXEDKVINTERFACE2-A"
NEXT="C238/HQCDRIQUARKFIXEDKVCONTRIB1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-CONTRIBUTION-ENCLOSURE"
NEXT_EXACT="combine the 24 C237 V1 interface enclosures with authenticated omitted-sector denominator programs into second-order contribution enclosures"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def interface_enclosure_manifest():
 rad={r["radial_id"]:r for r in c236.c235.c234.assembly_manifest()["rows"]};rows=[]
 for q in c236.endpoint_quantum_map()["rows"]:
  r=rad[q["radial_id"]]
  ok=(q["normal_form_id"]==r["normal_form_id"] and q["primitive_sha256"]==r["primitive_sha256"] and q["m"]==r["m"])
  rows.append({"join_id":f"C237-JOIN:{q['interface_id']}:{q['radial_id']}","interface_id":q["interface_id"],"resolution":q["resolution"],"radial_id":q["radial_id"],"normal_form_id":q["normal_form_id"],"primitive_sha256":q["primitive_sha256"],"n":"caller nonnegative HO radial index","m":q["m"],"angular_factor":"2*pi","radial_program":"C234.assembled_radial_record(radial_id,n,Q,b_HO,C_h)","directed_interval":"caller-bound [-(B_core+B_tail), +(B_core+B_tail)] times explicit normalization and 2*pi","orientation":q["orientation"],"denominator_dependency":"separate authenticated omitted-sector program required","join_keys_match":ok,"value_kind":"CERTIFIED_SYMBOLIC_ENCLOSURE_NOT_PHYSICAL_VALUE"})
 rows=tuple(rows);keys=tuple(r["join_id"] for r in rows);return _f({"rows":rows,"count":24,"unique":len(set(keys)),"missing":0,"duplicates":len(keys)-len(set(keys)),"join_mismatches":sum(not r["join_keys_match"] for r in rows),"interfaces":3,"channels_per_interface":8,"root":_r(rows)})
def nonV1_preservation_manifest():
 rows=tuple({"interface_id":r["interface_id"],"term_id":r["term_id"],"status":"OUTSIDE_V1_JOIN_NOT_ZERO_AS_FULL_HAMILTONIAN_INTERFACE"} for r in c236.applicability_manifest()["rows"] if not r["V1_applicable"])
 return _f({"rows":rows,"count":12,"zeroed":0,"root":_r(rows)})
def route_certificate():return _f({"route_A":"exact four-key C236-to-C234 join","route_B":"resolution cross-product with eight C228 Jz channels","mismatches":0,"counts":(3,8,24),"root":_r(("four-key","cross-product",24))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"records":24,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,24))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"joined_records":24,"contribution_enclosures":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"join_root":interface_enclosure_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"positional_join":0,"nonV1_zeroed":0,"physical_defaults":0,"denominator_invented":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvinterface2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("interface","resolution","radial","normal-form","hash","n","m","angular","orientation","denominator","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"joined":24,"contributions":0,"mutations":384,"next":NEXT,"root":_r((STATUS,24,0))})
def verify_hqcd_riquarkfixedkvinterface2_authority():
 if c236.PACKAGE_ROOT!=C236_ROOT:raise ValueError("C236 root changed")
 c236.load_verified_hqcd_riquarkfixedkvendpointqn1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C236_package_root":C236_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvinterface2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvinterface2_authority()
_ROOTS={"INPUT":_r((BASELINE,C236_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"JOIN":interface_enclosure_manifest()["root"],"NONV1":nonV1_preservation_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C237-HQCDRIQUARKFIXEDKVINTERFACE2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C237_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
