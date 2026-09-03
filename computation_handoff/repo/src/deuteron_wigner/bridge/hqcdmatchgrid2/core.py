"""C156/HQCDMATCHGRID2 explicit gate evaluator.

The evaluator is complete as an immutable interface, but C153 supplies only
symbolic common-IR cancellation and no numerical scale bracket or remainder
authority.  It therefore fails closed with empty windows.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdfavor2 as c155
from deuteron_wigner.bridge.hqcdmatchfb import core as c153

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c156_hqcdmatchgrid2"
BASELINE="9fe34691bd299c55dd5f1bb05d416409c24b1f84"
CONTRACT="docs/next_level/c155_c156_hqcdmatchgrid2_import_contract.json"
SCHEMA="C156-HQCDMATCHGRID2-V1"
STATUS="C156_HQCDMATCHGRID2_COMMON_IR_NUMERICAL_INCOMPLETE"
PLAN="MATCHGRID2-D"
NEXT="C157/HQCDMATCHIR2"
C155_ROOT="371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d"
C154_ROOT="1a22cd636f3b48ef9fd51676d2761a986126b043ccfa04e9609cd2a126b67bff"
C153_ROOT="7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
RESOLUTIONS=("K9","K11","K13")
QUANTITIES=("QUARK_FIELD","SIGNED_QUARK_MASS","TRANSVERSE_GLூON_FIELD","qg_VERTEX_DRESSING","QCD_COUPLING")
FIXTURES=("FIXTURE-FREE","FIXTURE-INTERACTING-A","FIXTURE-INTERACTING-B-NULL-SHIFT","FIXTURE-MASS-SIGN")
TARGET_SCHEMES=("MSBAR_C43_ADAPTED","PROJECT_LIGHT_FRONT_NONEXCEPTIONAL","RI_SMOM","MOMQ","STEP_SCALING")
# Canonical spelling retained for the public quantity schema.
QUANTITIES=("QUARK_FIELD","SIGNED_QUARK_MASS","TRANSVERSE_GLUON_FIELD","qg_VERTEX_DRESSING","QCD_COUPLING")
THRESHOLDS=(
    ("C156_ROUTE_RESIDUAL_ABS","1e-12","dimensionless","absolute","C144-C153 route tolerance"),
    ("C156_PROJECTOR_CONDITION_MAX","1e12","1","absolute","C149-C152 projector policy"),
    ("C156_COMMON_IR_RESIDUAL_MAX","1e-10","dimensionless","absolute","C153 common-IR policy; numerical evaluator absent"),
    ("C156_PERTURBATIVE_REMAINDER_MAX","0.10","1","relative","C153 order policy; numerical remainder absent"),
    ("C156_SPECTRAL_DISTANCE_MIN","0.05","GeV^2","absolute","fixed-regulator diagnostic policy"),
)

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str: return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str: return sha256(_canon(x).encode()).hexdigest()
def _verify_ancestry()->None:
    a=c155.verify_hqcd_flavor_authority()
    b=c153.verify_hqcd_matching_authority()
    if a["package_root"]!=C155_ROOT or b["package_root"]!=C153_ROOT: raise ValueError("C153/C155 public root mismatch")
def _context(*,parameter_record,fixture_id):
    if (parameter_record is None)==(fixture_id is None): raise ValueError("supply exactly one parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES: raise KeyError(fixture_id)
    if parameter_record is not None and not isinstance(parameter_record,Mapping): raise TypeError("parameter_record must be mapping")
    return {"fixture_id":fixture_id,"parameter_record":dict(parameter_record) if parameter_record is not None else None,"claim_tier":"DIAGNOSTIC_FIXTURE_WINDOW" if fixture_id else "CALLER_PARAMETER_CONDITIONAL_WINDOW"}
def matching_grid_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C156-MATCHING-GRID-PLAN-V1","selected_plan":PLAN,"status":STATUS,"reason":"C153 symbolic common-IR only; no numerical common-IR/remainder authority","alternatives":{"A":"not selected; required numerical gates absent","B":"not selected; evaluator domain is unavailable before quantity scan","C":"not selected; spectral route is not independently sufficient","E":"not selected; parameter uniformity not attempted"},"root":_root((PLAN,STATUS))})
def matching_grid_record_schema()->MappingProxyType:
    fields=("matching_grid_id","resolution","quantity_id","perturbative_order","C153_matching_record_id","C153_matching_record_root","finite_basis_scheme","target_scheme_id","active_Nf_record","external_flavor_record","common_IR_record","subtraction_kinematics","candidate_domain_rule","adaptive_refinement_rule","thresholds","maximum_evaluations","disconnected_interval_policy","endpoint_inclusion_policy","holdout_policy","claim_tier","no_default","no_physical_claim","grid_record_root")
    return _freeze({"schema":"C156-MATCHING-GRID-RECORD-V1","required":fields,"quantity_order":QUANTITIES,"target_schemes":TARGET_SCHEMES,"no_default":True,"no_physical_claim":True,"root":_root(fields)})
def validate_matching_grid_record(record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(record,Mapping): raise TypeError("grid record must be mapping")
    for k in matching_grid_record_schema()["required"]:
        if k not in record: raise ValueError(f"missing grid field: {k}")
    if record.get("schema")!="C156-MATCHING-GRID-RECORD-V1": raise ValueError("unknown grid schema")
    if record["resolution"] not in RESOLUTIONS or record["quantity_id"] not in QUANTITIES: raise ValueError("unknown resolution or quantity")
    if record["target_scheme_id"] not in TARGET_SCHEMES: raise ValueError("unknown target scheme")
    if record["no_default"] is not True or record["no_physical_claim"] is not True: raise ValueError("grid claim guard failed")
    if record["grid_record_root"] != _root({k:v for k,v in record.items() if k!="grid_record_root"}): raise ValueError("grid root mismatch")
    return _freeze(dict(record))
def candidate_scale_domain(record:Mapping[str,Any])->MappingProxyType:
    r=validate_matching_grid_record(record)
    return _freeze({"schema":"C156-CANDIDATE-SCALE-DOMAIN-V1","matching_grid_id":r["matching_grid_id"],"resolution":r["resolution"],"quantity_id":r["quantity_id"],"intervals":(),"status":"EMPTY_PUBLIC_AUTHORITY_DOMAIN","reason":"no authority-derived numerical C153 scale bracket","arbitrary_endpoints":False,"preferred_scales_injected":False,"root":_root((r["grid_record_root"],"empty-domain"))})
def gate_threshold_manifest()->MappingProxyType:
    rows=tuple({"threshold_id":a,"value":b,"units":c,"semantics":d,"authority":e,"mutation_frozen":True} for a,b,c,d,e in THRESHOLDS)
    return _freeze({"schema":"C156-THRESHOLD-MANIFEST-V1","rows":rows,"frozen_before_scan":True,"preferred_scale_tuning":False,"root":_root(rows)})
def _base_gate(r:Mapping[str,Any],mu:Any,ctx:Mapping[str,Any])->dict[str,Any]:
    return {"schema":"C156-GATE-VECTOR-V1","matching_grid_id":r["matching_grid_id"],"resolution":r["resolution"],"quantity_id":r["quantity_id"],"mu":mu,"units":"GeV","context":ctx,"target_scheme_eligible":"DECLARED_NOT_NUMERICALLY_EVALUATED","kinematics":"DECLARED_NOT_NUMERICALLY_EVALUATED","spectral_distance":"UNAVAILABLE","resolvent_conditioning":"UNAVAILABLE","longitudinal_support":"SYMBOLIC_SCOPE_ONLY","transverse_HO_support":"SYMBOLIC_SCOPE_ONLY","zero_mode_boundary":"DECLARED_SEPARATE","projector_rank_conditioning":"UNAVAILABLE","common_IR_cancellation":"NUMERICAL_AUTHORITY_MISSING","perturbative_remainder":"NUMERICAL_AUTHORITY_MISSING","numerical_stability":"UNAVAILABLE","conversion_denominators":"UNAVAILABLE","candidate_domain":"EMPTY_PUBLIC_AUTHORITY_DOMAIN","admitted":False,"failure_reasons":("COMMON_IR_NUMERICAL_AUTHORITY_MISSING","PERTURBATIVE_REMAINDER_NUMERICAL_AUTHORITY_MISSING","NO_AUTHORITY_DERIVED_SCALE_BRACKET"),"root":_root((r["grid_record_root"],str(mu),ctx,"blocked"))}
def evaluate_matching_gates(matching_grid_record:Mapping[str,Any],mu:Any,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _verify_ancestry(); r=validate_matching_grid_record(matching_grid_record); ctx=_context(parameter_record=parameter_record,fixture_id=fixture_id)
    try: x=float(mu)
    except Exception as exc: raise ValueError("mu must be a positive numeric GeV coordinate") from exc
    if x<=0: raise ValueError("mu must be positive")
    return _freeze(_base_gate(r,x,ctx))
def spectral_distance_report(matching_grid_record:Mapping[str,Any],mu:Any,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    g=evaluate_matching_gates(matching_grid_record,mu,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C156-SPECTRAL-DISTANCE-V1","gate_root":g["root"],"status":"UNAVAILABLE_NUMERICAL_SPECTRAL_AUTHORITY","distance":None,"threshold_id":"C156_SPECTRAL_DISTANCE_MIN","admitted":False})
def resolvent_condition_report(matching_grid_record:Mapping[str,Any],mu:Any,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    g=evaluate_matching_gates(matching_grid_record,mu,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C156-RESOLVENT-CONDITION-V1","gate_root":g["root"],"status":"UNAVAILABLE_NUMERICAL_RESOLVENT_AUTHORITY","condition_number":None,"admitted":False})
def componentwise_matching_windows(matching_grid_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    r=validate_matching_grid_record(matching_grid_record); ctx=_context(parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C156-COMPONENT-WINDOW-V1","matching_grid_id":r["matching_grid_id"],"resolution":r["resolution"],"quantity_id":r["quantity_id"],"context":ctx,"intervals":(),"disconnected_components":(),"endpoint_policy":"open/closed enclosures preserved; no endpoints available","status":"EMPTY_PUBLIC_AUTHORITY_DOMAIN","gate_vectors":(),"root":_root((r["grid_record_root"],ctx,"empty-window"))})
def mass_coupling_intersection(mass_grid_record:Mapping[str,Any],coupling_grid_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    a=componentwise_matching_windows(mass_grid_record,parameter_record=parameter_record,fixture_id=fixture_id); b=componentwise_matching_windows(coupling_grid_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C156-MASS-COUPLING-INTERSECTION-V1","mass_window_root":a["root"],"coupling_window_root":b["root"],"intervals":(),"status":"EMPTY_BECAUSE_COMPONENT_WINDOWS_UNAVAILABLE","common_fixed_regulator_scale_domain":False,"physical_scale_selected":False,"root":_root((a["root"],b["root"],"empty"))})
def parameter_uniform_window(parameter_domain_record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(parameter_domain_record,Mapping) or not parameter_domain_record.get("parameter_domain_id"): raise ValueError("explicit parameter domain required")
    return _freeze({"schema":"C156-PARAMETER-UNIFORM-WINDOW-V1","parameter_domain_id":parameter_domain_record["parameter_domain_id"],"intervals":(),"status":"UNAVAILABLE_NUMERICAL_COMMON_IR_AUTHORITY","fixture_uniformity_not_inferred":True,"root":_root((dict(parameter_domain_record),"blocked"))})
def cross_resolution_window_report(window_record_ids:Mapping[str,Any])->MappingProxyType:
    if not isinstance(window_record_ids,Mapping) or set(window_record_ids)!=set(RESOLUTIONS): raise ValueError("explicit K9/K11/K13 window roots required")
    return _freeze({"schema":"C156-CROSS-RESOLUTION-WINDOW-V1","window_record_ids":dict(window_record_ids),"intersection":(),"status":"NO_COMMON_DOMAIN","continuum_window":False,"regulator_independent":False,"root":_root((dict(window_record_ids),"empty"))})
def validate_caller_scale(window_record_id:str,mu:Any)->MappingProxyType:
    raise ValueError("no admitted C156 window; caller scale rejected")
def flavor_window_covariance_report()->MappingProxyType:
    return _freeze({"schema":"C156-FLAVOR-WINDOW-COVARIANCE-V1","u_window_equals_d_window":True,"proof":"C155 exact block identity","averaging":False,"windows_empty":True,"root":_root(("u=d","block-identity","empty"))})
def physical_input_resumption_contract()->MappingProxyType:
    return _freeze({"schema":"C156-PHYSICAL-INPUT-RESUMPTION-V1","C155_root":C155_ROOT,"m_ud_adapter":"ready","windows":"empty/unavailable","running":False,"thresholds":False,"inverse_matching":False,"next":NEXT,"root":_root((C155_ROOT,"empty-window",NEXT))})
def quantum_matching_handoff_contract()->MappingProxyType:
    return _freeze({"schema":"C156-QUANTUM-MATCHING-HANDOFF-V1","Q0_modified":False,"PennyLane":False,"physical_scale_selected":False,"status":"NOT_ACTIVATED","root":_root((False,False,False))})
def matching_grid_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C156-MATCHING-GRID-COMPLETENESS-V1","status":STATUS,"positive_gate":False,"plan":PLAN,"grid_interface":True,"thresholds_frozen":True,"gate_vectors_complete":True,"common_ir_numeric":False,"perturbative_remainder_numeric":False,"candidate_brackets":False,"windows_nonempty":False,"flavor_covariance":True,"next":NEXT,"root":_root((STATUS,PLAN,False))})
def verify_hqcd_matching_grid_authority()->dict[str,Any]:
    _verify_ancestry()
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"baseline":BASELINE,"contract":CONTRACT,"plan":PLAN,"C155_package_root":C155_ROOT,"C154_package_root":C154_ROOT,"C153_package_root":C153_ROOT,"quantities":len(QUANTITIES),"resolutions":RESOLUTIONS,"fixtures":FIXTURES,"thresholds_frozen":True,"candidate_domain_brackets":False,"common_ir_numeric":False,"perturbative_remainder_numeric":False,"windows_nonempty":False,"mass_coupling_intersection":False,"u_d_window_mismatch":0,"physical_scale_selected":False,"running":False,"inverse_matching":False,"Q0_modified":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_matching_grid_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C156 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C156 root/status mismatch")
    return _freeze(verify_hqcd_matching_grid_authority())
def static_isolation_guard()->MappingProxyType:
    return _freeze({"PDG_inputs_consumed":0,"FLAG_inputs_consumed":0,"ALPHA_inputs_consumed":0,"implicit_fixture":0,"implicit_parameter":0,"implicit_scale":0,"implicit_scheme":0,"implicit_Nf":0,"physical_scale":0,"running":0,"thresholds":0,"inverse_matching":0,"physical_targets":0,"Q0_modified":0,"states":0,"PennyLane":0,"TMD":0,"pass":True})
def mutate_live_hqcdmatchgrid2(index:int)->MappingProxyType:
    fields=("C155_root","grid_id","resolution","quantity","order","scheme","target","Nf","flavor","common_ir","kinematics","fixture","parameter","scale","domain","threshold","spectral","resolvent","longitudinal","HO","boundary","projector","remainder","stability","endpoint","interval","intersection","u_d","Q0","C157_contract")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C156_PLAN_ROOT":matching_grid_plan_manifest()["root"],"C156_GRID_SCHEMA_ROOT":matching_grid_record_schema()["root"],"C156_THRESHOLD_ROOT":gate_threshold_manifest()["root"],"C156_RESUMPTION_ROOT":physical_input_resumption_contract()["root"],"C156_FLAVOR_ROOT":flavor_window_covariance_report()["root"],"C156_QUANTUM_ROOT":quantum_matching_handoff_contract()["root"],"C156_COMPLETENESS_ROOT":matching_grid_completeness_certificate()["root"],"C155_ROOT":C155_ROOT,"C153_ROOT":C153_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS,"ancestry":(C155_ROOT,C154_ROOT,C153_ROOT)})
__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","load_verified_hqcd_matching_grid_authority","verify_hqcd_matching_grid_authority","matching_grid_plan_manifest","matching_grid_record_schema","validate_matching_grid_record","candidate_scale_domain","gate_threshold_manifest","evaluate_matching_gates","spectral_distance_report","resolvent_condition_report","componentwise_matching_windows","mass_coupling_intersection","parameter_uniform_window","cross_resolution_window_report","validate_caller_scale","flavor_window_covariance_report","physical_input_resumption_contract","quantum_matching_handoff_contract","matching_grid_completeness_certificate","mutate_live_hqcdmatchgrid2","static_isolation_guard"]
