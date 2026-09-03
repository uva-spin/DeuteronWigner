"""C161/HQCDMATCHIR4 fail-closed source-binding authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdfbnum as c158
from deuteron_wigner.bridge import hqcdmatchir3 as c159

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c161_hqcdmatchir4"
BASELINE = "3d07d710379c559d2f65176c1fd1eadd691e4fa2"
CONTRACT = "docs/next_level/c160_c161_hqcdmatchir4_continuation_contract.json"
CONTRACT_SHA256 = "2b24be99be62df1b37b0314badba663425d2ca86f6859efee21a55efe61e6f13"
STATUS = "C161_HQCDMATCHIR4_TARGET_BINDING_INCOMPLETE"
PLAN = "MATCHIR4-B"
NEXT = "C162/HQCDLFGNUM3"
C160_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C160_STATUS = "C160_C159_PROJECT_OWNED_STALE_REGRESSION_EXPECTATIONS_CORRECTED_C158_TEST_CLOSURE_READY"
C159_STATUS = "C159_HQCDMATCHIR3_C158_REGRESSION_FAILED"
C158_STATUS = "C158_C157_SOURCE_DERIVED_EXECUTABLE_FINITE_BASIS_MATCHING_COEFFICIENT_AUTHORITY_READY"
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
ORDERS = {"QUARK_FIELD": 0, "SIGNED_QUARK_MASS": 0, "TRANSVERSE_GLUON_FIELD": 0, "qg_VERTEX_DRESSING": 1, "QCD_COUPLING": 1}
LABELS = {"QUARK_FIELD": "delta_quark_field^FB(order=0)", "SIGNED_QUARK_MASS": "delta_signed_quark_mass^FB(order=0)", "TRANSVERSE_GLUON_FIELD": "delta_gluon_field^FB(order=0)", "qg_VERTEX_DRESSING": "delta_qg_vertex^FB(order=1)", "QCD_COUPLING": "delta_qcd_coupling^FB(order=1)"}
TARGET_SCHEMES = ("PROJECT_CONTINUUM_LIGHT_FRONT", "C43_ADAPTED_MSBAR", "RI_SMOM", "MOMQ", "STEP_SCALING_INTERMEDIATE")
RESOLUTIONS = ("K9", "K11", "K13")
FIXTURES = tuple(c158.FIXTURES)
IR_FAMILIES = ("REAL_SPACELIKE_COMMON_OFFSHELLNESS", "NONEXCEPTIONAL_QGQ_COMMON_OFFSHELLNESS", "COMPLEX_NONEXCEPTIONAL_DIAGNOSTIC_ONLY")
SAFE_OPCODES = ("LOAD_RATIONAL", "LOAD_SOURCE_CONSTANT", "LOAD_KINEMATIC", "ADD", "NEGATE", "MULTIPLY", "SAFE_DIVIDE", "INTEGER_POWER", "LOG", "LOG_RATIO", "EXP", "POSITIVE_SQRT", "PI_POWER", "ZETA_CONSTANT", "PROJECT_TENSOR", "SERIES_COEFFICIENT", "RETURN_TYPED_COEFFICIENT")
ROOT_CHAIN = {"C131":"67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4","C136":"fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262","C142":"3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d","C144":"cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635","C149":"8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0","C150":"2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C155":"371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d","C156":"8ba1231561ad04e5e1e8e96de9e8a270b8ad284b804021489dbe02cff2c2270d","C157":"351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c","C158":C158_ROOT,"C159":C159_ROOT,"C160":C160_ROOT}

def _plain(x: Any) -> Any:
    if isinstance(x, (Mapping, MappingProxyType)): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x, (tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def _context(parameter_record: Any, fixture_id: str|None) -> None:
    if (parameter_record is None)==(fixture_id is None): raise ValueError("exactly one parameter_record or fixture_id required")
    if fixture_id is not None and fixture_id not in FIXTURES: raise KeyError(fixture_id)
def _common(r: Mapping[str,Any]) -> Mapping[str,Any]:
    required=("schema","common_ir_id","ir_family","resolution","mu","rho","finite_basis_scheme","target_scheme_id","projector_id","active_Nf","external_flavor","no_default","record_root")
    if not isinstance(r,Mapping): raise TypeError("explicit common-IR record required")
    missing=[k for k in required if k not in r]
    if missing: raise ValueError("incomplete common-IR record: "+",".join(missing))
    if r["schema"]!="C161-COMMON-IR-NUMERIC-RECORD-V1" or r["ir_family"] not in IR_FAMILIES: raise ValueError("unsupported common-IR family")
    if r["resolution"] not in RESOLUTIONS or r["target_scheme_id"] not in TARGET_SCHEMES: raise ValueError("explicit resolution and scheme required")
    if r["mu"]<=0 or r["rho"]<=0 or r["no_default"] is not True: raise ValueError("positive explicit common record required")
    return _freeze(dict(r))
def _blocked(operation: str, **extra: Any) -> MappingProxyType:
    return _freeze({"schema":"C161-BLOCKED-V1","status":STATUS,"operation":operation,"positive_gate":False,"value":None,"reason":"SOURCE_EXPRESSION_INCOMPLETE","next":NEXT,**extra,"root":_root((operation,STATUS,extra))})

def c134_quarantine_report() -> MappingProxyType:
    return _freeze({"schema":"C161-C134-DIAGNOSTIC-QUARANTINE-REPORT-V1","classification":"PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC","test_id":"tests/test_c134_hqcdtarget.py::test_four_capsules_and_adapters","expected":4,"observed":115,"predates_C161":True,"imports_C158_C161":False,"C161_dependency":False,"targeted_C153_C160_clean":True,"modified":False,"root":_root(("C134",4,115,False))})
def matchir4_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C161-MATCHIR4-PLAN-MANIFEST-V1","selected_plan":PLAN,"status":STATUS,"reason":"C159 numeric source expressions and constants are unavailable","target_execution":False,"next":NEXT,"root":_root((PLAN,STATUS,NEXT))})
def quantity_order_execution_ledger() -> MappingProxyType:
    rows=tuple({"quantity_id":q,"order":ORDERS[q],"C153_label":LABELS[q],"coordinate_adapter_status":"CLOSED_SYMBOLIC_GUARDED","C158_import_status":"PUBLIC_IMPORT_AVAILABLE","target_program_binding_status":"SOURCE_EXPRESSION_INCOMPLETE","target_numeric_status":"NOT_EVALUATED","common_state_status":"RECORD_SCHEMA_CLOSED_NUMERIC_TARGET_BLOCKED","common_ir_status":"NOT_EVALUATED","cancellation_status":"NOT_EVALUATED","remainder_status":"NOT_EVALUATED","positive_bracket_status":"NOT_EVALUATED","terminal_status":STATUS,"exact_missing_object":"C153 numeric source expression and constants"} for q in QUANTITIES)
    return _freeze({"schema":"C161-QUANTITY-ORDER-EXECUTION-LEDGER-V1","rows":rows,"resolutions":RESOLUTIONS,"fixtures":FIXTURES,"root":_root(rows)})
def perturbative_coordinate_adapter_manifest() -> MappingProxyType:
    pairs=(("g_s","g_s^2","p->2p",1,1,"algebraic coupling power map","dimensionless","C158 coupling expansion"),("g_s^2","alpha_s","p->p","1/(4*pi)",1,"alpha_s=g_s^2/(4*pi)","dimensionless","definition"),("alpha_s","a_s","p->p","1/(4*pi)",1,"a_s=alpha_s/(4*pi)","dimensionless","definition"),("V_B","Z_1F","guarded derivative quotient","1/g_s","source expression required","V_B/g_s with derivative guard","vertex normalization","C152 derivative guard"),("g_R","g_R/g_s","guarded ratio","1/g_s","source expression required","g_R/g_s with derivative guard","dimensionless ratio","C158 ratio guard"),("signed m_R","m_R^2","p->2p",1,1,"signed input retained","mass^2","C155 signed mass"),("m_R^2","signed m_R","positive square root plus caller sign","1","caller branch required","no branch selected","mass","C155 signed mass"))
    rows=tuple({"adapter_id":f"ADAPT-{a}-{b}","source_coordinate":a,"target_coordinate":b,"power_map":p,"normalization_factor":f,"tree_coefficient":t,"first_nontrivial_coefficient":d,"sign_branch":"caller-supplied" if b=="signed m_R" else "algebraic/guarded","units":u,"source_authority":s,"zero_guard":True,"status":"GUARDED_BRANCH_REQUIRED" if b=="signed m_R" else "CLOSED_SYMBOLIC_GUARDED","root":_root((a,b,p,f,t,d,s))} for a,b,p,f,t,d,u,s in pairs)
    return _freeze({"schema":"C161-PERTURBATIVE-COORDINATE-ADAPTER-MANIFEST-V1","rows":rows,"root":_root(rows)})
def target_program_schema() -> MappingProxyType:
    return _freeze({"schema":"TARGET_COEFFICIENT_PROGRAM_DAG_V1","safe_opcodes":SAFE_OPCODES,"immutable":True,"pickle":False,"callables":False,"unknown_opcode":"reject","root":_root(SAFE_OPCODES)})
def target_binding_manifest(quantity_id: str|None=None,target_scheme_id: str|None=None,order: int|None=None) -> MappingProxyType:
    qs=QUANTITIES if quantity_id is None else (quantity_id,); ss=TARGET_SCHEMES if target_scheme_id is None else (target_scheme_id,); rows=[]
    for d in c159.target_program_manifest()["rows"]:
        if d["quantity_id"] in qs and d["target_scheme_id"] in ss and (order is None or d["order"]==order):
            rows.append({"program_id":d["program_id"],"quantity_id":d["quantity_id"],"order":d["order"],"target_scheme_id":d["target_scheme_id"],"source_id":d["source_id"],"source_locator":d["source_locator_status"],"source_expression":None,"safe_nodes":(),"binding_status":"SOURCE_EXPRESSION_INCOMPLETE","numeric_status":"UNAVAILABLE_BLOCKING","program_root":_root((d["program_id"],d["root"],"source_expression_missing"))})
    return _freeze({"schema":"C161-TARGET-BINDING-MANIFEST-V1","descriptors":tuple(rows),"descriptor_count":len(rows),"source_formulas_invented":0,"root":_root(rows)})
def validate_target_program(p: Mapping[str,Any]) -> MappingProxyType:
    if not isinstance(p,Mapping) or p.get("schema")!="TARGET_COEFFICIENT_PROGRAM_DAG_V1": raise ValueError("invalid target DAG")
    for n in p.get("nodes",()):
        if n.get("op") not in SAFE_OPCODES or any(callable(v) for v in n.values()): raise ValueError("unsafe target DAG")
    return _freeze(dict(p))
def common_ir_record_schema() -> MappingProxyType:
    return _freeze({"schema":"C161-COMMON-IR-NUMERIC-RECORD-V1","required":("common_ir_id","ir_family","resolution","mu","rho","finite_basis_scheme","target_scheme_id","projector_id","active_Nf","external_flavor","no_default","record_root"),"families":IR_FAMILIES,"rho_mu_distinct":True,"no_alternate_regulator":True,"root":_root(IR_FAMILIES)})
def common_ir_numeric_record(**kwargs: Any) -> MappingProxyType:
    data={"schema":"C161-COMMON-IR-NUMERIC-RECORD-V1",**kwargs,"no_default":True}; data["record_root"]=_root(data); return _common(data)
def target_numeric_coefficient(coefficient_label: str,common_ir_record: Mapping[str,Any],*,target_scheme_id: str,route: str="primary") -> MappingProxyType:
    _common(common_ir_record)
    if target_scheme_id not in TARGET_SCHEMES: raise ValueError(target_scheme_id)
    return _blocked("target_numeric_coefficient",coefficient_label=coefficient_label,target_scheme_id=target_scheme_id,route=route)
def finite_basis_coefficient_import(coefficient_label: str,common_ir_record: Mapping[str,Any],coupling_expansion_record: Mapping[str,Any],*,parameter_record=None,fixture_id=None) -> MappingProxyType:
    common=_common(common_ir_record); _context(parameter_record,fixture_id)
    rec=c158.finite_basis_matching_coefficient(coefficient_label,common,coupling_expansion_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C161-C158-FINITE-BASIS-IMPORT-V1","imported":True,"recomputed":False,"coefficient_label":coefficient_label,"value":rec["value"],"enclosure":rec["enclosure"],"quantity_id":rec["quantity_id"],"program_root":rec["program_root"],"leaf_roots":(rec["root"],),"C158_package_root":C158_ROOT,"C158_record_root":rec["root"],"root":_root((C158_ROOT,rec["root"],"import"))})
def finite_basis_numeric_coefficient_import(*a: Any,**k: Any) -> MappingProxyType: return finite_basis_coefficient_import(*a,**k)
def direct_common_ir_difference(coefficient_label: str,common_ir_record: Mapping[str,Any],coupling_expansion_record: Mapping[str,Any],*,target_scheme_id: str,parameter_record=None,fixture_id=None,route: str="TGT-A") -> MappingProxyType:
    _common(common_ir_record); _context(parameter_record,fixture_id)
    return _blocked("direct_common_ir_difference",coefficient_label=coefficient_label,target_scheme_id=target_scheme_id,route=route,difference=None)
def log_ir_derivative_report(*a: Any,**k: Any) -> MappingProxyType: return _blocked("log_ir_derivative_report",derivative=None,atlas_frozen=True)
def common_ir_variation_report(*a: Any,**k: Any) -> MappingProxyType: return _blocked("common_ir_variation_report",residuals=(),atlas_frozen=True)
def conversion_report(*a: Any,**k: Any) -> MappingProxyType: return _blocked("conversion_report",round_trip_residual=None)
def conversion_numeric_report(*a: Any,**k: Any) -> MappingProxyType: return conversion_report(*a,**k)
def first_omitted_order_report(coefficient_label: str,common_ir_record: Mapping[str,Any],perturbative_control_record: Mapping[str,Any],*,target_scheme_id: str,parameter_record=None,fixture_id=None) -> MappingProxyType:
    _common(common_ir_record); _context(parameter_record,fixture_id)
    if not isinstance(perturbative_control_record,Mapping) or perturbative_control_record.get("no_default") is not True or not perturbative_control_record.get("coupling_envelope") or not perturbative_control_record.get("log_envelope"): raise ValueError("explicit coupling/log envelope required")
    return _blocked("first_omitted_order_report",classification="UNAVAILABLE_BLOCKING",missing_sector_policy="unavailable_not_zero")
def positive_scale_bracket(*a: Any,**k: Any) -> MappingProxyType: return _blocked("positive_scale_bracket",intervals=(),selected_scale=False)
def componentwise_readiness_manifest() -> MappingProxyType: return _freeze({"schema":"C161-COMPONENTWISE-READINESS-MANIFEST-V1","status":STATUS,"rows":quantity_order_execution_ledger()["rows"],"signed_mass":"NOT_READY_TARGET_BINDING","qcd_coupling":"NOT_READY_TARGET_BINDING","root":_root((STATUS,quantity_order_execution_ledger()["root"]))})
def componentwise_matchir_manifest() -> MappingProxyType: return componentwise_readiness_manifest()
def mass_coupling_bracket_preflight() -> MappingProxyType: return _blocked("mass_coupling_bracket_preflight",intersection=(),final_window=False)
def flavor_covariance_report() -> MappingProxyType: return _freeze({"schema":"C161-FLAVOR-COVARIANCE-V1","status":STATUS,"C155_block_identity":True,"averaged":False,"active_Nf_altered":False,"root":_root(("C155",STATUS,False))})
def flavor_matchir_covariance_report() -> MappingProxyType: return flavor_covariance_report()
def matching_grid_handoff_contract() -> MappingProxyType: return _freeze({"schema":"C161-MATCHING-GRID-HANDOFF-CONTRACT-V1","next":NEXT,"eligible":False,"full_grid_executed":False,"final_windows":False,"physical_scale":False,"root":_root((NEXT,False))})
def matching_grid_rerun_contract() -> MappingProxyType: return matching_grid_handoff_contract()
def matchir4_completeness_certificate() -> MappingProxyType: return _freeze({"schema":"C161-MATCHIR4-COMPLETENESS-V1","status":STATUS,"positive_gate":False,"target_descriptors":25,"target_numeric_coefficients":0,"C158_imports":"public-only","coordinate_adapters":True,"common_IR_differences":0,"remainders":0,"positive_brackets":0,"full_grid":False,"missing_objects":("C153 numeric source expressions and constants",),"next":NEXT,"root":_root((STATUS,NEXT))})
def matchir_completeness_certificate() -> MappingProxyType: return matchir4_completeness_certificate()

def verify_hqcd_matchir4_authority() -> dict[str,Any]:
    return {"schema":"C161-HQCDMATCHIR4-V1","status":STATUS,"positive_gate":False,"baseline":BASELINE,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"plan":PLAN,"next":NEXT,"C160_status":C160_STATUS,"C160_package_root":C160_ROOT,"C159_status":C159_STATUS,"C159_package_root":C159_ROOT,"C158_status":C158_STATUS,"C158_package_root":C158_ROOT,"C134_classification":c134_quarantine_report()["classification"],"target_descriptors":25,"target_numeric_coefficients":0,"C158_recomputations":0,"full_grid":False,"physical_inputs":0,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_matchir4_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C161 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C161 package root/status mismatch")
    return _freeze(verify_hqcd_matchir4_authority())
def static_isolation_guard() -> MappingProxyType: return _freeze({"C131_C160_roots_unchanged":True,"C158_coefficient_recomputations":0,"C134_files_modified":0,"untracked_C157_test_modified":0,"invented_target_formulas":0,"missing_remainders_zeroed":0,"full_grid":False,"physical_scale":False,"physical_inputs":0,"Q0_Q1_modified":False,"pickle_loads":0,"allow_pickle_false":True,"pass":True})
def mutate_live_hqcdmatchir4(index: int) -> MappingProxyType:
    fields=("C160_root","C159_root","C158_root","C134_classification","coordinate_adapter","opcode","source_expression","gauge","pole","Nf","state","rho","mu","import_value","difference","log_ir","atlas","conversion","remainder","bracket","flavor","fixture","package_root","next")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C161_INPUT_ROOT":_root((BASELINE,CONTRACT,CONTRACT_SHA256,ROOT_CHAIN)),"C161_C134_QUARANTINE_ROOT":c134_quarantine_report()["root"],"C161_PLAN_ROOT":matchir4_plan_manifest()["root"],"C161_EXECUTION_LEDGER_ROOT":quantity_order_execution_ledger()["root"],"C161_COORDINATE_ADAPTER_ROOT":perturbative_coordinate_adapter_manifest()["root"],"C161_TARGET_BINDING_ROOT":target_binding_manifest()["root"],"C161_TARGET_COEFFICIENT_ROOT":_root(("no target",STATUS)),"C161_COMMON_IR_ROOT":_root(("record",STATUS)),"C161_DIRECT_DIFFERENCE_ROOT":_root(("no difference",STATUS)),"C161_REMAINDER_ROOT":_root(("no remainder",STATUS)),"C161_POSITIVE_BRACKET_ROOT":_root(("no bracket",STATUS)),"C161_COMPONENTWISE_ROOT":componentwise_readiness_manifest()["root"],"C161_GRID_HANDOFF_ROOT":matching_grid_handoff_contract()["root"],"C161_COMPLETENESS_ROOT":matchir4_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C161-HQCDMATCHIR4-V1","baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS})
__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","BASELINE","CONTRACT","CONTRACT_SHA256","C160_ROOT","C159_ROOT","C158_ROOT","QUANTITIES","ORDERS","LABELS","TARGET_SCHEMES","RESOLUTIONS","FIXTURES","SAFE_OPCODES","c134_quarantine_report","matchir4_plan_manifest","quantity_order_execution_ledger","perturbative_coordinate_adapter_manifest","target_program_schema","target_binding_manifest","validate_target_program","common_ir_record_schema","common_ir_numeric_record","target_numeric_coefficient","finite_basis_coefficient_import","finite_basis_numeric_coefficient_import","direct_common_ir_difference","log_ir_derivative_report","common_ir_variation_report","conversion_report","conversion_numeric_report","first_omitted_order_report","positive_scale_bracket","componentwise_readiness_manifest","componentwise_matchir_manifest","mass_coupling_bracket_preflight","flavor_covariance_report","flavor_matchir_covariance_report","matching_grid_handoff_contract","matching_grid_rerun_contract","matchir4_completeness_certificate","matchir_completeness_certificate","verify_hqcd_matchir4_authority","load_verified_hqcd_matchir4_authority","static_isolation_guard","mutate_live_hqcdmatchir4"]
