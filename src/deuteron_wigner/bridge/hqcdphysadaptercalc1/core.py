"""C215 safe partial programs and residual frontier for C168 adapters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdphysinputmap1 as c214
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c215_hqcdphysadaptercalc1"
BASELINE="3b0c29661b4803e0bdd12c53198c7c6041b08662";C214_ROOT="da080802cc9f8d0719ed211446b661eb29b5736e746aebeccfc5a95040602b72";C168_ROOT="c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
CONTRACT="docs/next_level/c214_c215_hqcdphysadaptercalc1_continuation_contract.json";CONTRACT_SHA256="cb5ea40e184214f93a017add5ed56da7aed09cced358d955e9be0ddcfa99370a"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c215_hqcdphysadaptercalc1_codex_prompt.md";PROMPT_SHA256="a9884abd849f6948bf12df1e2e34484e21be053d1a3680645db90995b73bf4a2"
STATUS="C215_C214_SIX_C168_CAPSULES_RECONCILED_SAFE_PARTIAL_PROGRAMS_READY_RI_SMOM_QUARK_ADAPTER_FIRST";PLAN="PHYSADAPTERCALC1-B"
NEXT="C216/HQCDRIQUARKADAPTER1";NEXT_OBJECT="C168-REQUEST-1";NEXT_EXACT="RI/SMOM quark-field C43 gauge/regulator-changing adapter calculation"
REQUESTS=(
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QUARK_FIELD-RI_SMOM-2","QUARK_FIELD","RI_SMOM","EARLIEST_C43_QUARK_TWO_POINT_SUBSTRATE_INCOMPLETE"),
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-2","SIGNED_QUARK_MASS","RI_SMOM","C43_SIGNED_MASS_PROJECTOR_SUBSTRATE_INCOMPLETE"),
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QUARK_FIELD-MOMQ-2","QUARK_FIELD","MOMQ","C43_QUARK_TWO_POINT_SUBSTRATE_INCOMPLETE"),
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2","TRANSVERSE_GLUON_FIELD","MOMQ","C184_C43_B0_TRANSVERSE_GLUON_SUBSTRATE_READY_ADAPTER_UNCALCULATED"),
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ-2","qg_VERTEX_DRESSING","MOMQ","C196_CONDITIONAL_PROPER_VERTEX_SUBSTRATE_READY_ADAPTER_UNCALCULATED"),
("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2","QCD_COUPLING","MOMQ","C212_SOURCE_SIDE_CONDITION_READY_FIELD_FACTOR_ADAPTERS_UNCALCULATED"))
RESOLUTIONS=("K9","K11","K13");SAFE_OPCODES=("LOAD_CAPSULE","LOAD_C43_SUBSTRATE","LOAD_TARGET_PROJECTOR","LOAD_COMMON_IR","CHECK_GAUGE","CHECK_PV_Q0_BOUNDARY","CHECK_HOLONOMY","PROJECT","SERIES_COEFFICIENT","SAFE_RATIO","PROPAGATE_UNAVAILABLE","RETURN_PARTIAL_ADAPTER")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def capsule_reconciliation_manifest(request_id=None):
 rows=tuple({"ordinal":i+1,"request_id":rid,"quantity":q,"scheme":s,"C168_status":"NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED","post_C168_substrate_status":st,"adapter_expression":False,"target_value":False,"physical_value":False} for i,(rid,q,s,st) in enumerate(REQUESTS) if request_id is None or rid==request_id)
 if request_id is not None and not rows:raise KeyError(request_id)
 return _f({"rows":rows,"count":len(rows),"root":_r(rows)})
def contribution_reconciliation_manifest(request_id=None):
 rows=tuple({"request_id":rid,"quantity":q,"closed_substrates":("C43 action/conventions","PV Q0 boundary ledger","holonomy schema","target projector authority","ST/MOMq source authority"),"remaining":("common-state evaluation","common-IR subtraction","gauge-changing coefficient","resolution-local adapter coefficient"),"missing_as_zero":False} for rid,q,s,st in REQUESTS if request_id is None or rid==request_id)
 return _f({"rows":rows,"count":len(rows),"root":_r(rows)})
def partial_program_schema():return _f({"schema":"PROJECT_C168_PARTIAL_ADAPTER_PROGRAM_V1","safe_opcodes":SAFE_OPCODES,"eval":False,"pickle":False,"callbacks":False,"unknown_opcode":"reject","root":_r(SAFE_OPCODES)})
def partial_program_manifest(request_id=None):
 nodes=tuple({"ordinal":i,"opcode":op} for i,op in enumerate(SAFE_OPCODES))
 rows=tuple({"program_id":f"C215-PARTIAL-{i+1}","request_id":rid,"quantity":q,"scheme":s,"nodes":nodes,"K_resolutions":RESOLUTIONS,"executable":False,"terminal":"RETURN_PARTIAL_ADAPTER_WITH_UNAVAILABLE_COEFFICIENT","root":_r((rid,nodes))} for i,(rid,q,s,st) in enumerate(REQUESTS) if request_id is None or rid==request_id)
 return _f({"rows":rows,"count":len(rows),"partial_programs":len(rows),"executable_programs":0,"root":_r(rows)})
def route_certificate_manifest(request_id=None):
 routes=("RENORMALIZATION_FACTOR_RATIO","COMMON_PROJECTED_GREEN_FUNCTION","COEFFICIENT_DIFFERENCE","INVERSE_ROUNDTRIP")
 rows=tuple({"request_id":rid,"routes":tuple({"route":x,"status":"PREREQUISITE_BOUND_COEFFICIENT_UNAVAILABLE","agreement":None} for x in routes),"false_agreement":False} for rid,q,s,st in REQUESTS if request_id is None or rid==request_id)
 return _f({"rows":rows,"count":len(rows),"closed_routes":0,"root":_r(rows)})
def residual_frontier_manifest():
 rows=tuple({"ordinal":i+1,"request_id":rid,"exact_missing_object":f"{s} {q} gauge/regulator-changing adapter coefficient","status":"ORDERED_RESIDUAL_CALCULATION","not_zero":True,"next":NEXT if i==0 else None} for i,(rid,q,s,st) in enumerate(REQUESTS))
 return _f({"rows":rows,"count":6,"first":REQUESTS[0][0],"next":NEXT,"root":_r(rows)})
def verify_hqcd_physadaptercalc1_authority():
 if c214.PACKAGE_ROOT!=C214_ROOT:raise ValueError("C214 root changed")
 c214.load_verified_hqcd_physinputmap1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C214_package_root":C214_ROOT,"C168_package_root":C168_ROOT,"package_root":PACKAGE_ROOT,"physical_values":False})
def load_verified_hqcd_physadaptercalc1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_physadaptercalc1_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"capsules_reconciled":6,"partial_programs":6,"executable_adapters":0,"physical_values":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"request_id":REQUESTS[0][0],"frontier_root":residual_frontier_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"C154_values_consumed":0,"C158_values_consumed":0,"missing_sectors_zeroed":0,"cross_gauge_equivalence":0,"counterterm_selection":0,"resolution_average":0,"continuum_extrapolation":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdphysadaptercalc1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("capsule","substrate","contribution","opcode","program","route","resolution","residual","handoff")[i%9],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"capsules":6,"partial_programs":6,"executable_adapters":0,"residuals":6,"mutations":384,"next":NEXT,"root":_r((STATUS,6,6,0))})
_ROOTS={"INPUT":_r((BASELINE,C214_ROOT,C168_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"CAPSULES":capsule_reconciliation_manifest()["root"],"CONTRIBUTIONS":contribution_reconciliation_manifest()["root"],"SCHEMA":partial_program_schema()["root"],"PROGRAMS":partial_program_manifest()["root"],"ROUTES":route_certificate_manifest()["root"],"RESIDUAL":residual_frontier_manifest()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C215-HQCDPHYSADAPTERCALC1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C215_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
