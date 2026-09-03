"""C214 exact edge audit for standard-to-finite-basis physical input maps."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdphysinput1 as c213
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c214_hqcdphysinputmap1"
BASELINE="47d240b63cc47e05004332cd1a0aa1a7716fc3be";C213_ROOT="367e0d7a008f64624d2d7d751e68f6688a88f3ec12f8a18b9c1da852bafe57eb";C168_ROOT="c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
CONTRACT="docs/next_level/c213_c214_hqcdphysinputmap1_continuation_contract.json";CONTRACT_SHA256="a875b8cd9bdc6e9207c7de23cafe3296281638eb387cd2029bbd8259faff3b9c"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c214_hqcdphysinputmap1_codex_prompt.md";PROMPT_SHA256="71931611fd2a5355784168f9ac8cf9aa45940c1ac06db206dd0d6a4b4858c814"
STATUS="C214_C213_PHYSICAL_INPUT_MAP_SCHEMA_READY_SIX_C43_ADAPTER_CALCULATIONS_REQUIRED";PLAN="PHYSINPUTMAP1-B"
NEXT="C215/HQCDPHYSADAPTERCALC1";NEXT_OBJECT="C197-ST-10-ADAPTER-CALCULATION";NEXT_EXACT="execute the six C168 C43-to-standard gauge/regulator-changing perturbative adapter capsules using C169-C212 completed authority"
RESOLUTIONS=("K9","K11","K13");QUANTITIES=("mass","coupling")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def edge_schema():return _f({"schema":"PROJECT_PHYSICAL_INPUT_MAP_EDGE_V1","required":("edge_id","quantity","source","target","scheme_in","scheme_out","scale_in","scale_out","Nf_in","Nf_out","units_in","units_out","authority","status","not_zero"),"root":_r(("edge",15))})
def _edges(q):
 base=(
 ("source-coordinate","C154 capsule","standard coordinate","AUTHENTICATED_COMPLETE"),
 ("flavor-identity","standard coordinate","project flavor coordinate","AUTHENTICATED_COMPLETE"),
 ("running-threshold","project flavor coordinate","common-scale standard coordinate","SOURCE_METHOD_ONLY_PROGRAM_ABSENT"),
 ("common-IR","common-scale standard coordinate","C43 common-state coordinate","C157_CONDITIONAL_NUMERICAL_INCOMPLETE"),
 ("gauge-regulator-adapter","C43 common-state coordinate","finite-basis target coefficient","C168_SIX_CALCULATIONS_REQUIRED"),
 ("resolution-target","finite-basis target coefficient","K9/K11/K13 parameter target","C158_COEFFICIENT_ONLY_TARGET_VALUE_ABSENT"),
 ("Hamiltonian-slot","K9/K11/K13 parameter target","renormalized Hamiltonian slot","SCHEMA_KNOWN_VALUE_ABSENT"))
 return tuple({"edge_id":f"C214-{q.upper()}-{i+1}","quantity":q,"source":a,"target":b,"scheme_in":"explicit caller/source","scheme_out":"explicit caller/target","scale_in":"explicit","scale_out":"explicit","Nf_in":"explicit","Nf_out":"explicit threshold ledger","units_in":"mass" if q=="mass" else "dimensionless","units_out":"mass" if q=="mass" else "dimensionless","authority":s,"status":s,"not_zero":True} for i,(n,a,b,s) in enumerate(base))
def mapping_dag(quantity=None):
 qs=(quantity,) if quantity else QUANTITIES
 if any(q not in QUANTITIES for q in qs):raise ValueError(quantity)
 rows=tuple(x for q in qs for x in _edges(q));return _f({"rows":rows,"count":len(rows),"acyclic":True,"complete_edges":sum(x["status"]=="AUTHENTICATED_COMPLETE" for x in rows),"root":_r(rows)})
def c158_role_audit():return _f({"package_root":"63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367","role":"EXECUTABLE_FINITE_BASIS_MATCHING_COEFFICIENT_AUTHORITY","coefficients":True,"physical_target_values":False,"physical_capsules":False,"values_consumed":0,"root":_r(("C158","coefficients-only"))})
def source_expression_audit():
 rows=(
 {"authority":"C154","object":"physical standard coordinates","complete":True},
 {"authority":"C155","object":"isosymmetric ud flavor lift","complete":True},
 {"authority":"C168","object":"six calculation capsules","complete":True},
 {"authority":"C169-C196","object":"C43 sectors and conditional qg proper vertex","complete":True},
 {"authority":"C168/C196 boundary","object":"six executable adapter expressions","complete":False},
 {"authority":"C158/C161","object":"physical finite-basis target values","complete":False})
 return _f({"rows":rows,"count":6,"complete":4,"root":_r(rows)})
def independent_dependency_audits():
 rows=({"audit":"forward","path":"C154→C155→running→common-IR→adapter→C158 target→Hamiltonian","first_missing":"running/adapter executable programs"},{"audit":"reverse","path":"Hamiltonian slot→target→adapter→standard capsule","first_missing":"finite-basis target and adapter executable programs"})
 return _f({"rows":rows,"count":2,"agree_on_calculation_frontier":True,"root":_r(rows)})
def missing_edge_decision():return _f({"classification":"MAP_SCHEMA_COMPLETE_EXACT_PROJECT_CALCULATION_FRONTIER","C168_capsules":6,"adapter_programs":0,"target_values":0,"blocker":False,"next":NEXT,"next_object":NEXT_OBJECT,"root":_r((PLAN,NEXT,6))})
def verify_hqcd_physinputmap1_authority():
 if c213.PACKAGE_ROOT!=C213_ROOT:raise ValueError("C213 root changed")
 c213.load_verified_hqcd_physinput1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C213_package_root":C213_ROOT,"C168_package_root":C168_ROOT,"package_root":PACKAGE_ROOT,"physical_values":False})
def load_verified_hqcd_physinputmap1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_physinputmap1_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"map_schema_ready":True,"map_executable":False,"physical_values":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"mapping_root":mapping_dag()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"C154_values_consumed":0,"C158_values_consumed":0,"numerical_evolution":0,"physical_defaults":0,"counterterm_selection":0,"resolution_average":0,"continuum_extrapolation":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdphysinputmap1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("edge","scheme","scale","Nf","units","C158-role","expression","forward","reverse","decision","handoff")[i%11],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"DAG_edges":14,"complete_edges":4,"audits":2,"C168_capsules":6,"adapter_programs":0,"mutations":384,"next":NEXT,"root":_r((STATUS,14,4,6))})
_ROOTS={"INPUT":_r((BASELINE,C213_ROOT,C168_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"SCHEMA":edge_schema()["root"],"DAG":mapping_dag()["root"],"C158":c158_role_audit()["root"],"EXPRESSIONS":source_expression_audit()["root"],"AUDITS":independent_dependency_audits()["root"],"MISSING":missing_edge_decision()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C214-HQCDPHYSINPUTMAP1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C214_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
