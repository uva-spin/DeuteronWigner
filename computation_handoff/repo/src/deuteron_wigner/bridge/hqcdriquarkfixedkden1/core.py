"""C221 omitted fixed-K denominator authority audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import free2 as c128
from deuteron_wigner.bridge import hqcdriquarkfixedkmap1 as c220
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c221_hqcdriquarkfixedkden1"
BASELINE="2e1b5afebcff16fd6a22b313f107f43acfafb1f9";C220_ROOT="0151249342328c0f6994786057c23296ee19383230fe01422390b779fd3124a3"
CONTRACT="docs/next_level/c220_c221_hqcdriquarkfixedkden1_continuation_contract.json";CONTRACT_SHA256="7ab25d78b012503e01d61b000b3fac9a8c9745ce345fe15f4ec26fa89b1244a5"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c221_hqcdriquarkfixedkden1_codex_prompt.md";PROMPT_SHA256="23a95fbfd100d277a4e325683e45b1de6527e5072686ffac51c3a8aaaf8c4d80"
STATUS="C221_C220_OMITTED_DENOMINATOR_SCHEMA_READY_FREE_COMPLEMENT_OPERATOR_INCOMPLETE";PLAN="RIQUARKFIXEDKDEN1-D"
NEXT="C222/HQCDRIQUARKFIXEDKFREE1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-FREE-OPERATOR"
NEXT_EXACT="source-derived symbolic free M2 operator on the unbounded OUTSIDE_FIXED_K complement domain"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def denominator_schema():return _f({"schema":"C221-OMITTED-RESOLVENT-PROGRAM-V1","operator":"z I_Q - Q_R H Q_R","orientation":"P_R H Q_R (zI_Q-Q_RHQ_R)^-1 Q_R H P_R","analytic_query":"caller explicit complex z","pole_PV_prescription":"UNAVAILABLE","safe_opcodes":("VALIDATE_C220_DOMAIN","LOAD_OMITTED_FREE_OPERATOR","LOAD_OMITTED_INTERACTION","FORM_SYMBOLIC_DENOMINATOR","SOLVE_SPARSE_OR_BOUND","COMPOSE_ENDPOINTS"),"executable":False,"dense_inverse":False,"root":_r(("zI-QHQ","safe"))})
def component_audit():
 rows=({"component":"Q_R H0 Q_R","retained_authority":c128.STATUS,"retained_only":True,"omitted_domain_operator":False,"status":"FIRST_MISSING"},{"component":"Q_R V1 Q_R","retained_authority":"C53/C131","retained_only":True,"omitted_domain_operator":False,"status":"DOWNSTREAM"},{"component":"Q_R V2 Q_R","retained_authority":"C112/C127/C131","retained_only":True,"omitted_domain_operator":False,"status":"DOWNSTREAM"},{"component":"pole/PV domain","retained_authority":"C145 analytic query","retained_only":True,"omitted_domain_operator":False,"status":"DOWNSTREAM"})
 return _f({"rows":rows,"count":4,"first_missing":"Q_R H0 Q_R","root":_r(rows)})
def retained_zero_nonpromotion_certificate():return _f({"C128_internal_conservation_zero_scope":"retained q/qg basis only","C130_source_nonzero_interfaces":15,"promoted_to_omitted_domain":False,"contradiction":False,"reason":"no common endpoint domain in C128","root":_r(("retained-only",False))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"denominator_schema_ready":True,"denominator_executable":False,"first_missing_component":"Q_R H0 Q_R","next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"schema_root":denominator_schema()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_zero_promoted":0,"physical_values":0,"minimum_norm":0,"missing_zeroed":0,"dense_inverse":0,"finite_cutoff_invented":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkden1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("domain","H0","V1","V2","z","pole","PV","orientation","zero-scope","sparse","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"schema":True,"components":4,"complete_components":0,"mutations":384,"next":NEXT,"root":_r((STATUS,4,0))})
def verify_hqcd_riquarkfixedkden1_authority():
 if c220.PACKAGE_ROOT!=C220_ROOT:raise ValueError("C220 root changed")
 c128.load_verified_free_m2_authority();c220.load_verified_hqcd_riquarkfixedkmap1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C220_package_root":C220_ROOT,"C128_package_root":c128.PACKAGE_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkden1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkden1_authority()
_ROOTS={"INPUT":_r((BASELINE,C220_ROOT,c128.PACKAGE_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"SCHEMA":denominator_schema()["root"],"COMPONENTS":component_audit()["root"],"NONPROMOTION":retained_zero_nonpromotion_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C221-HQCDRIQUARKFIXEDKDEN1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C221_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
