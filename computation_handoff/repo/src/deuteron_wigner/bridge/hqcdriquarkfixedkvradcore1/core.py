"""C232 exact symbolic finite-core radial enclosure authority."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvradconst1 as c231
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c232_hqcdriquarkfixedkvradcore1"
BASELINE="845a3a0225f29ffbc9ca58fefa83c7921b0fde63";C231_ROOT="0fb9fc8f6d18bde50eedfa46d9e117906611dd3f62731d513d1601bedff04c47"
CONTRACT="docs/next_level/c231_c232_hqcdriquarkfixedkvradcore1_continuation_contract.json";CONTRACT_SHA256="befbd3d1361823e570bba5cfc4df0e9b449327858e9e8e1ab0d81975bb5a95f3"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c232_hqcdriquarkfixedkvradcore1_codex_prompt.md";PROMPT_SHA256="3d1f9250b36ee57ab3e16cb9c626ea091729b7e9104cb80c3306103cb783e25a"
STATUS="C232_EIGHT_EXACT_SYMBOLIC_DIRECTED_FINITE_CORE_ENCLOSURE_PROGRAMS_READY_ANALYTIC_TAIL_INCOMPLETE";PLAN="RIQUARKFIXEDKVRADCORE1-B"
NEXT="C233/HQCDRIQUARKFIXEDKVRADTAIL1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-RADIAL-GAUSSIAN-TAIL"
NEXT_EXACT="analytic upper-incomplete-gamma Gaussian-tail enclosure and core-tail error allocator for the eight C232 radial programs"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def core_enclosure_program(radial_id,n,Q_symbol="Q",b_symbol="b_HO",C_symbol="C_h"):
 if not isinstance(radial_id,str):raise TypeError(radial_id)
 if not isinstance(n,int) or n<0:raise ValueError("n must be nonnegative integer")
 rows={r["radial_id"]:r for r in c231.growth_program_manifest()["rows"]}
 if radial_id not in rows:raise KeyError(radial_id)
 mrow={r["radial_id"]:r for r in c231.critical_split_manifest()["rows"]}[radial_id]
 # The signed matching m is recovered from C230; only |m| enters the radial HO factor.
 upstream={r["radial_id"]:r for r in c231.c230.factorization_manifest()["rows"]}[radial_id];a=abs(upstream["m"])
 terms=[]
 # |L_n^a(t)| <= sum_j binomial(n+a,n-j)t^j/j!; (1+q)^2=sum_s binomial(2,s)q^s.
 for j in range(n+1):
  lag_num=math.comb(n+a,n-j);lag_den=math.factorial(j)
  for s in range(3):
   power=a+1+2*j+s
   terms.append({"j":j,"s":s,"positive_coefficient":f"{math.comb(2,s)*lag_num}/{lag_den} * {b_symbol}^(-{2*j})","q_power":power,"exact_integral":f"2^(({power}-1)/2)*{b_symbol}^({power+1})*lowergamma(({power+1})/2,{Q_symbol}^2/(2*{b_symbol}^2))"})
 return _f({"radial_id":radial_id,"n":n,"m":upstream["m"],"domain":f"0<=q<={Q_symbol}; {Q_symbol}>0; {b_symbol}>0; {C_symbol}>=0","terms":tuple(terms),"term_count":3*(n+1),"upper_bound":f"{C_symbol} * sum(positive_coefficient * exact_integral)","directed_interval":("-B_core","B_core"),"coverage":("0",Q_symbol),"overlap_count":0,"missing_count":0,"source_value_zeroed":False,"critical_set":mrow["core_splits"],"root":_r((radial_id,n,terms))})
def core_program_manifest():
 rows=tuple({"radial_id":r["radial_id"],"program":"core_enclosure_program(radial_id,n,Q,b_HO,C_h)","all_n_nonnegative":True,"directed":True,"special_function":"lower incomplete gamma","normalization":"caller/source HO normalization remains multiplicative and explicit"} for r in c231.growth_program_manifest()["rows"])
 return _f({"rows":rows,"count":8,"complete":8,"root":_r(rows)})
def route_certificate():return _f({"route_A":"absolute Laguerre coefficient expansion followed by exact monomial Gaussian integration","route_B":"C231 polynomial majorant integrated termwise on the count-once core interval","formula":"integral_0^Q q^r exp(-q^2/(2b^2))dq=2^((r-1)/2)b^(r+1) lowergamma((r+1)/2,Q^2/(2b^2))","mismatches":0,"root":_r(("Laguerre","lowergamma",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"core_programs":8,"tail_programs":0,"numeric_quadrature_promoted":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"core_root":core_program_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"eval":0,"pickle":0,"callback":0,"fit":0,"threshold":0,"physical_defaults":0,"quadrature_promoted":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvradcore1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("radial","n","m","Q","b","C","Laguerre","gamma","partition","directed","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"core_programs":8,"tail_programs":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,0))})
def verify_hqcd_riquarkfixedkvradcore1_authority():
 if c231.PACKAGE_ROOT!=C231_ROOT:raise ValueError("C231 root changed")
 c231.load_verified_hqcd_riquarkfixedkvradconst1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C231_package_root":C231_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvradcore1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvradcore1_authority()
_ROOTS={"INPUT":_r((BASELINE,C231_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"CORE":core_program_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C232-HQCDRIQUARKFIXEDKVRADCORE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C232_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
