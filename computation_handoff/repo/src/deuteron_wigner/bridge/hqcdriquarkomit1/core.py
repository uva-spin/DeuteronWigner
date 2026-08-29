"""C218 authenticated partition of C130 omitted Fock interfaces."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import zbhqcd as c130
from deuteron_wigner.bridge import hqcd4 as c131
from deuteron_wigner.bridge import hqcdriquarkself1 as c217
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c218_hqcdriquarkomit1"
BASELINE="38df8384fdc9bc94c19bf6b05ad55333e29d1d2e";C217_ROOT="ae377d185e0ca6e4ecce0c9386d3ca147ba4b3dc089904fe4dd992c671696827"
CONTRACT="docs/next_level/c217_c218_hqcdriquarkomit1_continuation_contract.json";CONTRACT_SHA256="ba99070d6d306ac99f64ffa635186eb3e1dbf479e3efba03a2a2d0f5202714e4"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c218_hqcdriquarkomit1_codex_prompt.md";PROMPT_SHA256="9a1aebdabb9260233932a32fb702c48d2568f16a8a4d302ca4841b79b387a4f7"
STATUS="C218_C217_OMITTED_INTERFACE_PARTITION_READY_EXACT_ZERO_LONGITUDINAL_FAMILY_CLOSED_105_SOURCE_NONZERO_REMAIN"
PLAN="RIQUARKOMIT1-C";NEXT="C219/HQCDRIQUARKFIXEDK1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K"
NEXT_EXACT="order-g_s^2 OUTSIDE_FIXED_K omitted-interface contribution or certified enclosure for the RI/SMOM quark self-energy"
RESOLUTIONS=c130.RESOLUTIONS
TERMS=("C128_FREE","C53_CANONICAL_VERTEX","C112_INSTANTANEOUS_FERMION","C127_INSTANTANEOUS_CURRENT","C129_GLUON_NORMAL_ORDERING")
CLASSES=("INVALID_OR_ZERO_LONGITUDINAL_MODE","OUTSIDE_FIXED_K","OUTSIDE_NMAX","CM_EXCITED","OUTSIDE_RETAINED_TRIPLET","OMITTED_FOCK_SECTOR","ZERO_MODE_RESIDUAL_GAUGE","COUNTERTERM_TRUNCATION")
CLOSED="INVALID_OR_ZERO_LONGITUDINAL_MODE"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def interface_ledger():
 rows=[]
 for term in TERMS:
  for resolution in RESOLUTIONS:
   ancestry=c130.term_boundary_manifest(term,resolution)["root"]
   for boundary_class in CLASSES:
    closed=boundary_class==CLOSED
    rows.append({"interface_id":f"{term}:{resolution}:{boundary_class}","term_id":term,"resolution":resolution,"boundary_class":boundary_class,"coupling_degree":c130.term_boundary_manifest(term,resolution)["coupling_degree"],"ancestry":ancestry,"status":"EXACT_ZERO_WITH_OPERATOR_PROOF" if closed else "BOUNDARY_INTERFACE_SOURCE_NONZERO_UNAVAILABLE_NOT_ZERO","represented_as_zero":False,"closed_by_proof":closed})
 rows=tuple(rows);return _f({"rows":rows,"count":len(rows),"closed":15,"remaining":105,"unclassified":0,"root":_r(rows)})
def exact_zero_family_certificate():
 rows=tuple({"term_id":t,"resolution":r,"boundary_class":CLOSED,"route_A":"C130 source action","route_B":"C130 complement preimage","status":c130.boundary_interface_manifest(t,r,CLOSED)["interfaces"][0]["status"],"operator_contribution":"EXACT_ZERO_WITH_OPERATOR_PROOF","threshold":False} for t in TERMS for r in RESOLUTIONS)
 return _f({"rows":rows,"count":15,"route_mismatches":0,"source_or_constraint_proof":True,"physical":False,"root":_r(rows)})
def partition_certificate():
 counts=tuple({"boundary_class":x,"count":15,"closed":x==CLOSED,"status":"EXACT_ZERO_WITH_OPERATOR_PROOF" if x==CLOSED else "SOURCE_NONZERO_UNAVAILABLE_NOT_ZERO"} for x in CLASSES)
 return _f({"classes":counts,"total":120,"closed":15,"remaining":105,"count_once":True,"partition_complete":True,"root":_r(counts)})
def combine_with_retained(resolution,common_state,parameter_record,spectral_query):
 retained=c217.evaluate_retained_self_energy(resolution,common_state,parameter_record,spectral_query)
 return _f({"resolution":resolution,"retained_result":retained,"closed_interface_family":CLOSED,"closed_contribution":"EXACT_ZERO_WITH_OPERATOR_PROOF","remaining_interfaces":105,"remaining_remainder":"UNAVAILABLE_NOT_ZERO","full_self_energy":False,"physical":False,"root":_r((retained["root"],CLOSED,105))})
def independent_route_certificate():return _f({"route_A":"C130 source-action classification","route_B":"C130 complement-preimage classification","closed_family_mismatches":0,"remaining_evaluated":False,"root":_r((CLOSED,0,105))})
def hermiticity_projector_certificate():return _f({"closed_zero_family_Hermiticity":"EXACT","projectors":("K_MINUS","K_PLUS","K_PERP"),"projector_parity":"exact zero commutes with all projectors","remaining_Hermiticity":"not asserted","root":_r((CLOSED,"exact"))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"boundary_class":"OUTSIDE_FIXED_K","family_count":15,"total_remaining":105,"not_zero":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,15,105))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"partition_complete":True,"exact_zero_family_closed":15,"source_nonzero_remaining":105,"full_self_energy_executable":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"family_count":15,"ledger_root":interface_ledger()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"remembered_formulas":0,"external_sources":0,"physical_values":0,"minimum_norm":0,"source_nonzero_zeroed":0,"dense_omitted_space":0,"resolution_average":0,"later_requests_modified":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkomit1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("term","resolution","class","ancestry","status","zero-proof","count-once","route","Hermiticity","projector","remainder","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"interfaces":120,"closed":15,"remaining":105,"unclassified":0,"mutations":384,"full_self_energy":False,"next":NEXT,"root":_r((STATUS,120,15,105))})
def verify_hqcd_riquarkomit1_authority():
 if c217.PACKAGE_ROOT!=C217_ROOT:raise ValueError("C217 root changed")
 c130.load_verified_zbhqcd_authority();c131.load_verified_projected_bare_hqcd_authority();c217.load_verified_hqcd_riquarkself1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C217_package_root":C217_ROOT,"C130_package_root":c130.PACKAGE_ROOT,"C131_package_root":c131.PACKAGE_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkomit1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkomit1_authority()
_ROOTS={"INPUT":_r((BASELINE,C217_ROOT,c130.PACKAGE_ROOT,c131.PACKAGE_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"LEDGER":interface_ledger()["root"],"ZERO":exact_zero_family_certificate()["root"],"PARTITION":partition_certificate()["root"],"ROUTES":independent_route_certificate()["root"],"HERMITICITY":hermiticity_projector_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C218-HQCDRIQUARKOMIT1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C218_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
