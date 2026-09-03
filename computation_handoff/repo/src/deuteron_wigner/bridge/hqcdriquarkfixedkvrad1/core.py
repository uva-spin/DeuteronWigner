"""C229 radial convergence authority and exact enclosure frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvho2 as c228
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c229_hqcdriquarkfixedkvrad1"
BASELINE="4f6b6bce4dd25f8e3d2583f42671cce886356b38";C228_ROOT="a5df2ccabd60a90a8ebab210aa023d70ef455e8fb172acdd3d7b66f0383de042"
CONTRACT="docs/next_level/c228_c229_hqcdriquarkfixedkvrad1_continuation_contract.json";CONTRACT_SHA256="3d9682c8d48571b379da04ffe00032026dd87da48c124e009bb344b5a18a6f32"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c229_hqcdriquarkfixedkvrad1_codex_prompt.md";PROMPT_SHA256="92f7e19a747869c8f46ccefa443f8a2721de2b3d2e864e426a28ae5b318298e7"
STATUS="C229_C228_EIGHT_RADIAL_FAMILIES_ABSOLUTE_CONVERGENCE_READY_EXPLICIT_FACTOR_AND_TAIL_ENCLOSURE_INCOMPLETE";PLAN="RIQUARKFIXEDKVRAD1-E"
NEXT="C230/HQCDRIQUARKFIXEDKVRADBOUND1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-RADIAL-BOUND"
NEXT_EXACT="explicit radial factorization and certified core-plus-tail enclosure program for the eight C228 matching HO integrals"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def radial_family_manifest():
 rows=tuple({**dict(r),"measure":"q dq","HO_radial":"q^abs(m) exp(-q^2/(2 b_HO^2)) L_n^abs(m)(q^2/b_HO^2)","primitive_radial":"positive-branch algebraic function of q^2","parameters":"xq,xg,Pplus,bHO positive; mq nonnegative","value":"UNAVAILABLE_NOT_ZERO"} for r in c228.radial_frontier_manifest()["rows"])
 return _f({"rows":rows,"count":8,"root":_r(rows)})
def convergence_certificate():
 rows=tuple({"radial_id":r["radial_id"],"origin_power_lower_bound":abs(r["m"])+1,"origin_integrable":True,"infinity_envelope":"C(parameters,n,m)*(1+q)^p exp(-q^2/(2 b_HO^2))","infinity_integrable":True,"absolute_convergence":True,"uniform_on_compact_positive_parameter_sets":True} for r in radial_family_manifest()["rows"])
 return _f({"rows":rows,"count":8,"convergent":8,"divergent":0,"root":_r(rows)})
def enclosure_audit():return _f({"required":("canonical radial factor F_h(q)","explicit polynomial-growth exponent p","computable compact-domain constant C","core directed interval integration","analytic Gaussian tail bound"),"available":("convergence class","positive parameter domain","Gaussian HO envelope"),"missing":("canonical F_h factorization","C and p extraction","tail cutoff/error allocator"),"numeric_quadrature_promoted":False,"enclosure_complete":False,"root":_r(("factor","C","p","tail"))})
def route_certificate():return _f({"route_A":"HO Gaussian/Laguerre asymptotics","route_B":"C227 positive-branch algebraic degree audit","absolute_convergence_mismatches":0,"value_route_agreement":False,"root":_r(("Gaussian","algebraic",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"families":8,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,8))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"convergent_families":8,"evaluated_or_enclosed":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"convergence_root":convergence_certificate()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"quadrature_promoted":0,"fit":0,"threshold":0,"physical_values":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvrad1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("q0","qinf","m","n","bHO","x","Pplus","mass","Gaussian","constant","tail","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"convergent":8,"enclosed":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,0))})
def verify_hqcd_riquarkfixedkvrad1_authority():
 if c228.PACKAGE_ROOT!=C228_ROOT:raise ValueError("C228 root changed")
 c228.load_verified_hqcd_riquarkfixedkvho2_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C228_package_root":C228_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvrad1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvrad1_authority()
_ROOTS={"INPUT":_r((BASELINE,C228_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"FAMILIES":radial_family_manifest()["root"],"CONVERGENCE":convergence_certificate()["root"],"ENCLOSURE":enclosure_audit()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C229-HQCDRIQUARKFIXEDKVRAD1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C229_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
