"""C154/HQCDPHYSINPUT2 immutable physical-input boundary.

The standard numerical records are authenticated source coordinates.  The
project mass direction remains generic-flavor, so no finite-basis physical
condition is activated until that identity is supplied explicitly.
"""
from __future__ import annotations
import json
from decimal import Decimal, getcontext
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping
from deuteron_wigner.bridge.hqcdmatchfb import core as c153

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c154_hqcdphysinput2"
BASELINE = "a33d3b5b3fd719ca33df8c8385769af67e43cae1"
CONTRACT = "docs/next_level/c153_c154_hqcdphysinput2_import_contract.json"
CONTRACT_SHA256 = "3998893de2ab012b033d0312abc4f793b50adbfdb0af569d68410ee06b4feb3d"
SCHEMA = "C154-HQCDPHYSINPUT2-V1"
STATUS = "C154_HQCDPHYSINPUT2_FLAVOR_IDENTITY_INCOMPLETE"
PLAN = "PHYSINPUT2-B"
NEXT = "C155/HQCDFLAVOR2"
C153_ROOT = "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
C152_ROOT = "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da"
C151_ROOT = "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C150_ROOT = "2854394a252e1a6401570a6617d3d2fbea1daced7fffa105d235eb398c4a57a"
C149_ROOT = "8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0"
C144_ROOT = "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635"
C131_ROOT = "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
RESOLUTIONS = ("K9", "K11", "K13")

SOURCE_ROWS = (
    {"source_id":"PDG2026_QCD", "edition":"2026", "path":"data/raw/c140_sources/pdg2026_qcd.pdf", "sha256":"c04c628d76b18610c5fa2a919c6081918a25b55fb971b6af5829f4ca2baa386f", "role":"STANDARD_COORDINATE_AGGREGATE_AUTHORITY", "locator":"p.42, Eq. (9.25)", "numeric":True},
    {"source_id":"PDG2026_QUARK_MASSES", "edition":"2026", "path":"data/raw/c140_sources/pdg2026_quark_masses.pdf", "sha256":"90b4d001694b6bc6addf1e31a0685fca8f54bec3da3530c4122c96a0b1f8a8e7", "role":"STANDARD_COORDINATE_AGGREGATE_AUTHORITY", "locator":"p.6, Eq. (60.4)", "numeric":True},
    {"source_id":"ALPHA_COUPLING_STEP", "edition":"arXiv:1706.03821", "path":"data/raw/c140_sources/arxiv_1706.03821.pdf", "sha256":"e41e01642d69d9bf5bdbb7395043f4f50b128ac9d8956450d0aecd612c7b0d5a", "role":"RUNNING_AND_THRESHOLD_AUTHORITY", "locator":"source-defined step scaling", "numeric":False},
    {"source_id":"ALPHA_MASS_STEP", "edition":"arXiv:1802.05243", "path":"data/raw/c140_sources/arxiv_1802.05243.pdf", "sha256":"f71625e7561840626ac66ae590f6cac20f027a9ab3b45c27f1e0542267d28c31", "role":"RUNNING_AND_THRESHOLD_AUTHORITY", "locator":"source-defined mass step scaling", "numeric":False},
    {"source_id":"FLAG_REVIEW_2024", "edition":"published 2026", "path":None, "sha256":None, "role":"INDEPENDENT_NUMERICAL_HOLDOUT", "locator":"not present in authorized source cache", "numeric":False},
)

MASS = {"input_id":"C154_STD_MUD_MSbar_2GeV_NL4", "quantity_id":"light_quark_mass", "central_value":"3.397", "units":"MeV", "uncertainty":{"kind":"SYMMETRIC_GAUSSIAN","value":"0.045","coverage":"combined stat+systematic envelope, Eq.(60.4)"}, "confidence":"source-reported combined uncertainty", "source_id":"PDG2026_QUARK_MASSES", "source_edition":"2026", "source_sha256":SOURCE_ROWS[1]["sha256"], "locator":"p.6, Eq. (60.4)", "source_role":"STANDARD_COORDINATE_AGGREGATE_AUTHORITY", "scheme":"MSbar", "scale":"2 GeV", "N_f":4, "flavor":"m_ud=(m_u+m_d)/2 in QCD mass convention", "isospin":"isospin-symmetric light average", "QED":"QED corrections removed phenomenologically; not a QED+QCD input", "sign_branch":"positive standard QCD mass branch", "threshold_policy":"Nf=4 source coordinate; explicit threshold adapter required", "running_authority":"ALPHA_MASS_STEP", "correlation_group":"PDG2026_QUARK_MASS_AVERAGE", "cross_covariance_status":"MARGINAL_INPUTS_ONLY", "date":"2026-06-01", "license":"source attribution retained", "no_default":True, "no_inference":True}
ALPHA = {"input_id":"C154_STD_ALPHA_S_MSbar_MZ", "quantity_id":"qcd_coupling", "central_value":"0.1180", "units":"1", "uncertainty":{"kind":"SYMMETRIC_GAUSSIAN","value":"0.0009","coverage":"PDG world-average uncertainty, Eq.(9.25)"}, "confidence":"source-reported world-average uncertainty", "source_id":"PDG2026_QCD", "source_edition":"2026", "source_sha256":SOURCE_ROWS[0]["sha256"], "locator":"p.42, Eq. (9.25)", "source_role":"STANDARD_COORDINATE_AGGREGATE_AUTHORITY", "scheme":"MSbar", "scale":"mZ", "N_f":5, "flavor":"active-flavor coupling coordinate; no light-flavor inference", "isospin":"not applicable", "QED":"QCD alpha_s coordinate; QED not included", "sign_branch":"positive g_s branch", "threshold_policy":"Nf=5 source coordinate; explicit threshold adapter required", "running_authority":"ALPHA_COUPLING_STEP", "correlation_group":"PDG2026_ALPHA_S_WORLD_AVERAGE", "cross_covariance_status":"MARGINAL_INPUTS_ONLY", "date":"2026-06-01", "license":"source attribution retained", "no_default":True, "no_inference":True}

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str: return json.dumps(_plain(x), sort_keys=True, separators=(",",":"), ensure_ascii=True)
def _root(x:Any)->str: return sha256(_canon(x).encode()).hexdigest()
def _capsule_root(c:Mapping[str,Any])->str: return _root({k:v for k,v in c.items() if k!="capsule_root"})
def _source_rows_verified() -> tuple[dict[str,Any], ...]:
    rows=[]
    for row in SOURCE_ROWS:
        x=dict(row)
        if x["path"] is not None:
            p=ROOT/x["path"]
            if not p.is_file(): raise FileNotFoundError(f"authenticated source missing: {x['path']}")
            digest=sha256(p.read_bytes()).hexdigest()
            if digest != x["sha256"]: raise ValueError(f"source hash mismatch: {x['source_id']}")
        rows.append(x)
    return tuple(rows)
def _assert_explicit(record:Mapping[str,Any]) -> None:
    required=("input_id","quantity_id","central_value","units","uncertainty","source_id","source_sha256","locator","scheme","scale","N_f","flavor","sign_branch","threshold_policy","no_default","no_inference")
    for k in required:
        if k not in record: raise ValueError(f"missing capsule field: {k}")
    if record["no_default"] is not True or record["no_inference"] is not True: raise ValueError("default/inference guard failed")
    if not isinstance(record["N_f"],int) or not record["scheme"] or not record["scale"]: raise ValueError("scheme/scale/N_f must be explicit")

def numerical_source_manifest()->MappingProxyType:
    rows=tuple(dict(x,root=_root(x)) for x in _source_rows_verified())
    return _freeze({"schema":"C154-NUMERICAL-SOURCE-MANIFEST-V1","rows":rows,"source_count":len(rows),"numeric_sources":2,"all_available_numeric_sources_hash_locked":True,"root":_root(rows)})
def numerical_source_role_audit()->MappingProxyType:
    return _freeze({"schema":"C154-NUMERICAL-SOURCE-ROLE-AUDIT-V1","roles":("STANDARD_COORDINATE_AGGREGATE_AUTHORITY","PRIMARY_LATTICE_OR_EXPERIMENTAL_DETERMINATION","RUNNING_AND_THRESHOLD_AUTHORITY","INDEPENDENT_NUMERICAL_HOLDOUT","COMPARISON_ONLY"),"PDG_role":"aggregate authority; exact page locators retained","FLAG_role":"holdout unavailable in authorized cache","ALPHA_role":"method/running authority only","secondary_summary_values_consumed":0,"root":_root(("PDG", "FLAG-unavailable", "ALPHA-method"))})
def numerical_input_capsule_schema()->MappingProxyType:
    return _freeze({"schema":"C154-NUMERICAL-INPUT-CAPSULE-V1","required":("input_id","quantity_id","central_value","units","uncertainty","source_id","source_edition","source_sha256","locator","source_role","scheme","scale","N_f","flavor","isospin","QED","sign_branch","threshold_policy","running_authority","correlation_group","cross_covariance_status","date","license","no_default","no_inference","capsule_root"),"uncertainty_kinds":("SYMMETRIC_GAUSSIAN","ASYMMETRIC_INTERVAL","SOURCE_REPLICA_OR_SAMPLE","SOURCE_COVARIANCE_MATRIX","MARGINAL_ONLY_CROSS_COVARIANCE_UNAVAILABLE","CENTRAL_VALUE_ONLY_WITH_EXPLICIT_LIMITATION"),"root":_root(("capsule", "no-default"))})
def validate_numerical_input_capsule(capsule:Mapping[str,Any])->MappingProxyType:
    if not isinstance(capsule,Mapping): raise TypeError("capsule must be a mapping")
    for key in numerical_input_capsule_schema()["required"]:
        if key not in capsule: raise ValueError(f"missing capsule field: {key}")
    _assert_explicit(capsule)
    source_by_id={x["source_id"]:x for x in _source_rows_verified()}
    if capsule["source_id"] not in source_by_id: raise ValueError("unknown source")
    if capsule["source_sha256"] != source_by_id[capsule["source_id"]]["sha256"]: raise ValueError("source hash mismatch")
    if capsule["capsule_root"] != _capsule_root(capsule): raise ValueError("capsule root mismatch")
    return _freeze(dict(capsule))
def _capsule(c:Mapping[str,Any])->MappingProxyType:
    x=dict(c); x["capsule_root"]=_capsule_root(x); return _freeze(x)
def accepted_standard_input_capsules()->tuple[MappingProxyType,...]: return (_capsule(MASS),_capsule(ALPHA))
def flavor_mapping_decision()->MappingProxyType:
    return _freeze({"schema":"C154-FLAVOR-MAPPING-DECISION-V1","classification":"PROJECT_FLAVOR_IDENTITY_INCOMPLETE","C131_mass_direction":"generic unresolved light-quark source","candidate_standard":"m_ud","identity_proved":False,"u_proxy_forbidden":True,"d_proxy_forbidden":True,"QCD_QED_adapter":"required and absent","status":"BLOCKING","root":_root(("generic", "m_ud", False))})
def input_covariance_manifest()->MappingProxyType:
    return _freeze({"schema":"C154-INPUT-COVARIANCE-V1","status":"MARGINAL_INPUTS_ONLY","mass_coupling_covariance":"unavailable","fabricated_zero":False,"joint_ellipse":False,"mass_group":"PDG2026_QUARK_MASS_AVERAGE","coupling_group":"PDG2026_ALPHA_S_WORLD_AVERAGE","root":_root(("marginal",False))})
def running_threshold_manifest()->MappingProxyType:
    return _freeze({"schema":"C154-RUNNING-THRESHOLD-V1","status":"INCOMPLETE_MATCHING_SCALE_AUTHORITY","mass_route_A":"declared, not executed without flavor adapter","coupling_route_A":"declared, not executed without admitted matching scale","route_B":"ALPHA step authority available as method only","route_C":"source table holdout unavailable","thresholds_explicit":False,"numeric_defaults":0,"root":_root(("incomplete", "no-scale"))})
def matching_scale_manifest(resolution: str|None=None)->MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise ValueError(resolution)
    rows=tuple({"resolution":r,"window_status":"DECLARED_FIXED_REGULATOR_WINDOW","admitted_interval":None,"selected_scale":None,"reason":"C153 exposes no numeric window/scale record","continuum_extrapolation":False} for r in (RESOLUTIONS if resolution is None else (resolution,)))
    return _freeze({"schema":"C154-MATCHING-SCALE-V1","rows":rows,"complete":False,"root":_root(rows)})
def standard_to_fb_target(quantity_id:str,resolution:str,matching_record:Mapping[str,Any],input_capsule_id:str)->MappingProxyType:
    if resolution not in RESOLUTIONS: raise ValueError(resolution)
    if input_capsule_id not in {x["input_id"] for x in accepted_standard_input_capsules()}: raise KeyError(input_capsule_id)
    if not isinstance(matching_record,Mapping) or not matching_record.get("common_ir_id"): raise ValueError("explicit C153 matching record required")
    raise RuntimeError("C154 matching scale/inverse conversion unavailable; fail closed")
def physical_condition_manifest(resolution: str|None=None)->MappingProxyType:
    rows=tuple({"resolution":r,"rows":("F_mass","F_coupling"),"status":"TARGET_UNAVAILABLE","mass_target":None,"coupling_target":None} for r in (RESOLUTIONS if resolution is None else (resolution,)))
    return _freeze({"schema":"C154-PHYSICAL-CONDITION-V1","rows":rows,"root":_root(rows)})
def physical_jacobian_manifest(resolution: str|None=None)->MappingProxyType:
    return _freeze({"schema":"C154-PHYSICAL-JACOBIAN-V1","resolution":resolution or "all","original_directions":11,"identified_coordinates":2,"null_coordinates":9,"counterterm_directions":6,"rank":None,"status":"NOT_EVALUATED_TARGET_BLOCKED","minimum_norm":False,"root":_root((resolution or "all",11,2,9,6))})
def identified_coordinate_solution(resolution:str,*,input_record_ids,matching_record_ids):
    raise RuntimeError("identified solution unavailable: flavor/matching targets incomplete")
def conditional_solution_manifold(resolution:str)->MappingProxyType:
    if resolution not in RESOLUTIONS: raise ValueError(resolution)
    return _freeze({"schema":"C154-CONDITIONAL-SOLUTION-MANIFOLD-V1","resolution":resolution,"dimension":11,"identified_solution":None,"null_coordinates":9,"counterterm_directions":6,"representative_selected":False,"status":"BLOCKED_TARGET_AUTHORITY","root":_root((resolution,"blocked",11,9,6))})
def derived_renormalization_coordinates(resolution:str,solution_record:Mapping[str,Any])->MappingProxyType:
    raise RuntimeError("derived coordinates unavailable without finite-basis target")
def resolution_parameter_flow()->MappingProxyType:
    return _freeze({"schema":"C154-RESOLUTION-PARAMETER-FLOW-V1","resolutions":RESOLUTIONS,"status":"FIXED_REGULATOR_FLOW_NOT_COMPUTED","averaged":False,"continuum_extrapolation":False,"root":_root((RESOLUTIONS,"not-computed"))})
def quantum_activation_handoff_contract()->MappingProxyType:
    return _freeze({"schema":"C154-QUANTUM-ACTIVATION-HANDOFF-V1","Q0_modified":False,"PennyLane":False,"physical_state":False,"requires_full_parameter_record":True,"status":"NOT_ACTIVATED","root":_root((False,False,False))})
def physical_input_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C154-COMPLETENESS-V1","status":STATUS,"positive_gate":False,"plan":PLAN,"mass_capsule":True,"coupling_capsule":True,"flavor_identity":False,"running_threshold":False,"matching_scales":False,"targets":False,"jacobian":False,"solution_manifold":False,"next":NEXT,"root":_root((STATUS,PLAN,False))})
def physical_input_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C154-PLAN-V1","selected_plan":PLAN,"status":STATUS,"alternatives":{"A":"not selected; flavor identity incomplete","C":"not selected; coupling transport is downstream","D":"not selected; target authority follows flavor","F":"not selected; no covariance claim attempted"},"root":_root((PLAN,STATUS))})
def verify_hqcd_physical_input_authority()->dict[str,Any]:
    c153_authority=c153.verify_hqcd_matching_authority()
    if c153_authority["package_root"] != C153_ROOT or not c153_authority["positive_gate"]:
        raise ValueError("C153 public authority mismatch")
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"baseline":BASELINE,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"plan":PLAN,"C153_package_root":C153_ROOT,"C152_package_root":C152_ROOT,"C151_package_root":C151_ROOT,"C150_package_root":C150_ROOT,"C149_package_root":C149_ROOT,"C144_package_root":C144_ROOT,"C131_package_root":C131_ROOT,"standard_capsules":2,"accepted_project_targets":0,"flavor_identity":"PROJECT_FLAVOR_IDENTITY_INCOMPLETE","covariance":"MARGINAL_INPUTS_ONLY","running_threshold":"INCOMPLETE_MATCHING_SCALE_AUTHORITY","matching_scales":False,"nullspace":9,"counterterm_directions":6,"null_representatives":0,"counterterms_solved":0,"Q0_modified":0,"physical_states":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_physical_input_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C154 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C154 root/status mismatch")
    return _freeze(verify_hqcd_physical_input_authority())
def static_isolation_guard()->MappingProxyType:
    return _freeze({"secondary_values":0,"implicit_source":0,"implicit_scheme":0,"implicit_scale":0,"implicit_Nf":0,"implicit_flavor":0,"fabricated_covariance_zero":0,"legacy_inputs":0,"field_factors_as_inputs":0,"resolution_averages":0,"counterterms_solved":0,"null_representatives":0,"full_parameter_vectors":0,"Q0_modified":0,"states":0,"TMD":0,"pass":True})
def mutate_live_hqcdphysinput2(index:int)->MappingProxyType:
    fields=("C153_root","source_hash","locator","central_value","uncertainty","scheme","scale","N_f","flavor","sign","alpha_branch","threshold","matching_window","target","condition","jacobian","nullspace","counterterm","covariance","Q0","C155_contract")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={
    "C154_INPUT_ROOT":_root((MASS,ALPHA)), "C154_PLAN_ROOT":physical_input_plan_manifest()["root"],
    "C154_NUMERICAL_SOURCE_ROOT":numerical_source_manifest()["root"], "C154_STANDARD_MASS_INPUT_ROOT":_capsule_root(MASS),
    "C154_STANDARD_COUPLING_INPUT_ROOT":_capsule_root(ALPHA), "C154_COVARIANCE_ROOT":input_covariance_manifest()["root"],
    "C154_FLAVOR_MAPPING_ROOT":flavor_mapping_decision()["root"], "C154_RUNNING_THRESHOLD_ROOT":running_threshold_manifest()["root"],
    "C154_MATCHING_SCALE_ROOT":matching_scale_manifest()["root"], "C154_FB_MASS_TARGET_ROOT":_root(("blocked","mass")),
    "C154_FB_COUPLING_TARGET_ROOT":_root(("blocked","coupling")), "C154_PHYSICAL_CONDITION_ROOT":physical_condition_manifest()["root"],
    "C154_JACOBIAN_ROOT":physical_jacobian_manifest()["root"], "C154_SOLUTION_MANIFOLD_ROOT":_root(("blocked",11,9,6)),
    "C154_IDENTIFIED_SOLUTION_ROOT":_root(("unavailable",)), "C154_UNCERTAINTY_ROOT":_root(("marginal",)),
    "C154_RESOLUTION_FLOW_ROOT":resolution_parameter_flow()["root"], "C154_DERIVED_COORDINATE_ROOT":_root(("derived","unavailable")),
    "C154_QUANTUM_HANDOFF_ROOT":quantum_activation_handoff_contract()["root"], "C154_SCOPE_ROOT":_root(("no-state","no-TMD")),
    "C154_COMPLETENESS_ROOT":physical_input_completeness_certificate()["root"], "C153_ROOT":C153_ROOT,
}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS,"ancestry":(C153_ROOT,C152_ROOT,C151_ROOT,C150_ROOT,C149_ROOT,C144_ROOT,C131_ROOT)})
__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","load_verified_hqcd_physical_input_authority","verify_hqcd_physical_input_authority","physical_input_plan_manifest","numerical_source_manifest","numerical_source_role_audit","numerical_input_capsule_schema","validate_numerical_input_capsule","accepted_standard_input_capsules","flavor_mapping_decision","input_covariance_manifest","running_threshold_manifest","matching_scale_manifest","standard_to_fb_target","physical_condition_manifest","physical_jacobian_manifest","identified_coordinate_solution","conditional_solution_manifold","derived_renormalization_coordinates","resolution_parameter_flow","quantum_activation_handoff_contract","physical_input_completeness_certificate","mutate_live_hqcdphysinput2","static_isolation_guard"]
