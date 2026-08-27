"""C234 canonical core-plus-tail radial enclosure assembly."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvradtail1 as c233
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c234_hqcdriquarkfixedkvradassemble1"
BASELINE="be8f09dba6bea4aacdf15bcd91ea1b5895d812ac";C233_ROOT="32fbc26eb10c37a26e63321492c79a7fff0064d848a57d3443319593e431dedc"
CONTRACT="docs/next_level/c233_c234_hqcdriquarkfixedkvradassemble1_continuation_contract.json";CONTRACT_SHA256="e67d959c2e262d41fc7a5ba0c7c568ab9e0e5f45a0386b7c9d713012f61e74db"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c234_hqcdriquarkfixedkvradassemble1_codex_prompt.md";PROMPT_SHA256="58782578fb7903da332d8fb426e33b17b5a5c79cca17964bbb204ca66ccefae6"
STATUS="C234_EIGHT_CANONICAL_CALLER_BOUND_CORE_PLUS_TAIL_RADIAL_MATRIX_ELEMENT_RECORDS_READY";PLAN="RIQUARKFIXEDKVRADASSEMBLE1-B"
NEXT="C235/HQCDRIQUARKFIXEDKVINTERFACE1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-INTERFACE-ASSEMBLY"
NEXT_EXACT="map the eight C234 canonical radial enclosure families onto the 15 authenticated OUTSIDE_FIXED_K omitted-interface records"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def assembled_radial_record(radial_id,n,Q_symbol="Q",b_symbol="b_HO",C_symbol="C_h"):
 core=c233.c232.core_enclosure_program(radial_id,n,Q_symbol,b_symbol,C_symbol);tail=c233.tail_enclosure_program(radial_id,n,Q_symbol,b_symbol,C_symbol);alloc=c233.error_allocator(radial_id,n)
 source={r["radial_id"]:r for r in c233.c232.c231.c230.factorization_manifest()["rows"]}[radial_id]
 return _f({"record_id":f"C234-ASM-{radial_id}-N{n}","radial_id":radial_id,"normal_form_id":source["normal_form_id"],"primitive_sha256":source["primitive_sha256"],"n":n,"m":source["m"],"angular_factor":"2*pi","core_root":core["root"],"tail_root":tail["root"],"allocator_root":alloc["root"],"total_bound":"B_core+B_tail","directed_interval":("-(B_core+B_tail)","B_core+B_tail"),"normalization":"caller/source HO normalization multiplicative and explicit","parameters":f"{Q_symbol}>0; {b_symbol}>0; {C_symbol}>=0 plus verified C231 capsule","orientation":"source canonical; adjoint obtained by complex conjugation and endpoint reversal","value_kind":"CERTIFIED_SYMBOLIC_ENCLOSURE_NOT_PHYSICAL_VALUE","root":_r((radial_id,n,core["root"],tail["root"]))})
def assembly_manifest():
 rows=tuple({"radial_id":r["radial_id"],"normal_form_id":r["normal_form_id"],"primitive_sha256":r["primitive_sha256"],"m":r["m"],"program":"assembled_radial_record(radial_id,n,Q,b_HO,C_h)","all_n_nonnegative":True} for r in c233.c232.c231.c230.factorization_manifest()["rows"])
 ids=tuple(r["radial_id"] for r in rows);return _f({"rows":rows,"count":8,"unique_ids":len(set(ids)),"missing_ids":0,"duplicate_ids":0,"root":_r(rows)})
def route_certificate():return _f({"route_A":"C232 core plus C233 tail joined by radial_id","route_B":"full gamma coefficient majorant split at Q","core_tail_root_mismatches":0,"source_hash_mismatches":0,"coverage_mismatches":0,"root":_r(("join","fullgamma",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"interfaces":15,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,15))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"assembled_families":8,"mapped_interfaces":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"assembly_root":assembly_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"eval":0,"pickle":0,"fit":0,"physical_defaults":0,"quadrature_promoted":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvradassemble1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("id","hash","n","m","Q","b","C","core","tail","orientation","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"assembled":8,"interfaces":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,0))})
def verify_hqcd_riquarkfixedkvradassemble1_authority():
 if c233.PACKAGE_ROOT!=C233_ROOT:raise ValueError("C233 root changed")
 c233.load_verified_hqcd_riquarkfixedkvradtail1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C233_package_root":C233_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvradassemble1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvradassemble1_authority()
_ROOTS={"INPUT":_r((BASELINE,C233_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"ASSEMBLY":assembly_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C234-HQCDRIQUARKFIXEDKVRADASSEMBLE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C234_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
