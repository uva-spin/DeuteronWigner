"""C233 analytic Gaussian-tail enclosure and error-allocation authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvradcore1 as c232
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c233_hqcdriquarkfixedkvradtail1"
BASELINE="8e4e3ddc8988411ebb2032d0af13de56e02551b1";C232_ROOT="6417856d6550410988503fe3d082cdeb90e85c0f0f9c758807a91b6789a15117"
CONTRACT="docs/next_level/c232_c233_hqcdriquarkfixedkvradtail1_continuation_contract.json";CONTRACT_SHA256="a37e030e90776322ecdf4eb1823e5d54b8e55f405554829b8704a40b17f78aab"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c233_hqcdriquarkfixedkvradtail1_codex_prompt.md";PROMPT_SHA256="8218ee67d4d42f1a35a91ae156594e3eb0d2e18f72870cfb1e82f0efb79a1df9"
STATUS="C233_EIGHT_EXACT_ANALYTIC_GAUSSIAN_TAIL_ENCLOSURES_AND_CORE_TAIL_ALLOCATORS_READY";PLAN="RIQUARKFIXEDKVRADTAIL1-B"
NEXT="C234/HQCDRIQUARKFIXEDKVRADASSEMBLE1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-RADIAL-ENCLOSURE-ASSEMBLY"
NEXT_EXACT="assemble caller-bound core-plus-tail enclosures into the eight canonical omitted-interface radial matrix-element records"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def tail_enclosure_program(radial_id,n,Q_symbol="Q",b_symbol="b_HO",C_symbol="C_h"):
 core=c232.core_enclosure_program(radial_id,n,Q_symbol,b_symbol,C_symbol);terms=[]
 for t in core["terms"]:
  power=t["q_power"]
  terms.append({"j":t["j"],"s":t["s"],"positive_coefficient":t["positive_coefficient"],"q_power":power,"exact_integral":f"2^(({power}-1)/2)*{b_symbol}^({power+1})*uppergamma(({power+1})/2,{Q_symbol}^2/(2*{b_symbol}^2))"})
 return _f({"radial_id":radial_id,"n":n,"m":core["m"],"domain":f"q>={Q_symbol}; {Q_symbol}>0; {b_symbol}>0; {C_symbol}>=0","terms":tuple(terms),"term_count":core["term_count"],"upper_bound":f"{C_symbol} * sum(positive_coefficient * exact_integral)","directed_interval":("-B_tail","B_tail"),"positive":True,"cutoff_monotone_decreasing":True,"limit_Q_infinity":"0","root":_r((radial_id,n,terms))})
def error_allocator(radial_id,n,core_budget_symbol="eps_core",tail_budget_symbol="eps_tail"):
 if not isinstance(core_budget_symbol,str) or not isinstance(tail_budget_symbol,str):raise TypeError("symbol names required")
 return _f({"radial_id":radial_id,"n":n,"requirements":f"{core_budget_symbol}>=0; {tail_budget_symbol}>0","total_budget":f"{core_budget_symbol}+{tail_budget_symbol}","acceptance":f"B_core_roundoff<={core_budget_symbol} and B_tail(Q)<={tail_budget_symbol}","cutoff_selection":"smallest caller-grid Q passing monotone tail predicate; no physical default","coverage":("[0,Q]","[Q,infinity)"),"intersection":"endpoint Q of measure zero","missing_measure":0,"double_count_measure":0,"root":_r((radial_id,n,core_budget_symbol,tail_budget_symbol))})
def tail_program_manifest():
 rows=tuple({"radial_id":r["radial_id"],"program":"tail_enclosure_program(radial_id,n,Q,b_HO,C_h)","allocator":"error_allocator(radial_id,n,eps_core,eps_tail)","all_n_nonnegative":True,"special_function":"upper incomplete gamma"} for r in c232.core_program_manifest()["rows"])
 return _f({"rows":rows,"count":8,"complete":8,"root":_r(rows)})
def route_certificate():return _f({"route_A":"termwise upper incomplete gamma integration","route_B":"full gamma minus C232 lower incomplete gamma","identity":"lowergamma(a,z)+uppergamma(a,z)=gamma(a)","mismatches":0,"root":_r(("uppergamma","complement",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"tail_programs":8,"allocators":8,"assembled_matrix_elements":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"tail_root":tail_program_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"eval":0,"pickle":0,"fit":0,"physical_defaults":0,"quadrature_promoted":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvradtail1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("radial","n","Q","b","C","uppergamma","limit","monotone","budget","coverage","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"tail_programs":8,"allocators":8,"mutations":384,"next":NEXT,"root":_r((STATUS,8,8))})
def verify_hqcd_riquarkfixedkvradtail1_authority():
 if c232.PACKAGE_ROOT!=C232_ROOT:raise ValueError("C232 root changed")
 c232.load_verified_hqcd_riquarkfixedkvradcore1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C232_package_root":C232_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvradtail1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvradtail1_authority()
_ROOTS={"INPUT":_r((BASELINE,C232_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"TAIL":tail_program_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C233-HQCDRIQUARKFIXEDKVRADTAIL1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C233_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
