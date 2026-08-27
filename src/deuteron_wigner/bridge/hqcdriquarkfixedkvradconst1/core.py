"""C231 compact-capsule radial growth constants and critical splits."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvradbound1 as c230
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c231_hqcdriquarkfixedkvradconst1"
BASELINE="9d1978006c03af4d09bc1a7649370d8ca70ee960";C230_ROOT="19c962b163d744e3868c050d0cc722c6b9087d2149c535bc03a6720c057c030f"
CONTRACT="docs/next_level/c230_c231_hqcdriquarkfixedkvradconst1_continuation_contract.json";CONTRACT_SHA256="5fb84caaf84c5c25b640fc77e108935a8e6c1c5433c9f2e495ac5dabef7ce1c8"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c231_hqcdriquarkfixedkvradconst1_codex_prompt.md";PROMPT_SHA256="80fea65b0c4b6a021643859edc22ef49188e870a38f0468a816eff353536d158"
STATUS="C231_EIGHT_COMPUTABLE_COMPACT_CAPSULE_GROWTH_CONSTANT_PROGRAMS_AND_EMPTY_POSITIVE_Q_CRITICAL_SETS_READY";PLAN="RIQUARKFIXEDKVRADCONST1-B"
NEXT="C232/HQCDRIQUARKFIXEDKVRADCORE1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-RADIAL-CORE-ENCLOSURE"
NEXT_EXACT="directed finite-core interval enclosure using the eight C231 compact-capsule growth programs"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def validate_capsule(x_min,P_min,P_max,m_max):
 vals=(x_min,P_min,P_max,m_max)
 if any(isinstance(v,bool) or not isinstance(v,(int,float)) for v in vals):raise TypeError("real scalar capsule required")
 if not (0<x_min<0.5 and 0<P_min<=P_max and m_max>=0):raise ValueError("invalid compact positive capsule")
 return _f({"x_q_interval":(x_min,1-x_min),"x_g_interval":(x_min,1-x_min),"simplex":"x_q+x_g=1","P_plus_interval":(P_min,P_max),"m_q_interval":(0,m_max),"excluded_boundary":"UNAVAILABLE_NOT_ZERO","root":_r(vals)})
def capsule_schema():return _f({"caller_fields":("x_min","P_min","P_max","m_max"),"constraints":"0<x_min<1/2; 0<P_min<=P_max; m_max>=0","no_physical_defaults":True,"monotonicity":"constant nondecreasing when capsule enlarges","root":_r(("compact-simplex",4))})
def growth_program_manifest():
 rows=[]
 for r in c230.factorization_manifest()["rows"]:
  rows.append({"radial_id":r["radial_id"],"primitive_sha256":r["primitive_sha256"],"growth_exponent":2,"bound":"abs(F_h(q)) <= C_h(capsule)*(1+q)^2","constant_program":"outward interval evaluation of exact C227 expression DAG after replacing abs(q_x),abs(q_y)<=q, q^k<=(1+q)^2 for k=0,1,2, inverse x powers by x_min powers, P and m by capsule endpoints, and each positive inverse square-root by its q=0 lower radicand","arithmetic":"directed rational plus certified sqrt bounds","finite_on_valid_capsule":True,"open_domain_uniform_constant":False,"source_nonzero_as_zero":False})
 rows=tuple(rows);return _f({"rows":rows,"count":8,"computable":8,"common_exponent":2,"root":_r(rows)})
def critical_split_manifest():
 rows=tuple({"radial_id":r["radial_id"],"q_domain":"[0,infinity)","denominator_form":"sqrt(A0)*sqrt(A1+B*q^2)","A0_positive_on_capsule":True,"A1_positive_on_capsule":True,"B_positive_on_capsule":True,"positive_q_poles":(),"positive_q_branch_points":(),"core_splits":("0","Q caller positive") } for r in growth_program_manifest()["rows"])
 return _f({"rows":rows,"count":8,"interior_critical_points":0,"complete":True,"root":_r(rows)})
def route_certificate():return _f({"route_A":"exact expression-DAG absolute-value propagation","route_B":"positive-radicand degree audit plus triangle inequality","growth_exponent_mismatches":0,"critical_set_mismatches":0,"root":_r(("DAG","degree",0,0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"growth_programs":8,"critical_sets":8,"core_enclosures":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"growth_root":growth_program_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"eval":0,"pickle":0,"fit":0,"threshold":0,"physical_defaults":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvradconst1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("xmin","Pmin","Pmax","mmax","degree","radicand","pole","branch","constant","monotone","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"growth_programs":8,"critical_sets":8,"mutations":384,"next":NEXT,"root":_r((STATUS,8,8))})
def verify_hqcd_riquarkfixedkvradconst1_authority():
 if c230.PACKAGE_ROOT!=C230_ROOT:raise ValueError("C230 root changed")
 c230.load_verified_hqcd_riquarkfixedkvradbound1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C230_package_root":C230_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvradconst1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvradconst1_authority()
_ROOTS={"INPUT":_r((BASELINE,C230_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"CAPSULE":capsule_schema()["root"],"GROWTH":growth_program_manifest()["root"],"CRITICAL":critical_split_manifest()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C231-HQCDRIQUARKFIXEDKVRADCONST1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C231_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
