"""C157/HQCDMATCHIR2 public numerical-authority boundary.

The C153 coefficient surfaces are public, immutable, and symbolic.  They do
not expose executable ASTs or numerical enclosures.  C157 therefore records
that exact blocker and refuses to manufacture numerical coefficients,
remainders, or scale brackets from fixture scans.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdmatchgrid2 as c156
from deuteron_wigner.bridge.hqcdmatchgrid2 import core as c156_core
from deuteron_wigner.bridge import hqcdfavor2 as c155
from deuteron_wigner.bridge.hqcdmatchfb import core as c153
from deuteron_wigner.bridge.hqcdopapi import core as c144
from deuteron_wigner.bridge.hqcdqgvert import core as c152
from deuteron_wigner.bridge.hqcdg2pt import core as c151
from deuteron_wigner.bridge.hqcdzqmass import core as c150

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c157_hqcdmatchir2"
BASELINE = "3fa30b92bcdaa3e8484181e06a14db45cce683cd"
CONTRACT = "docs/next_level/c156_c157_hqcdmatchir2_import_contract.json"
SCHEMA = "C157-HQCDMATCHIR2-V1"
PARENT_STATUS = "C156_HQCDMATCHGRID2_COMMON_IR_NUMERICAL_INCOMPLETE"
STATUS = "C157_HQCDMATCHIR2_FINITE_BASIS_NUMERICAL_INCOMPLETE"
PLAN = "MATCHIR2-B"
NEXT = "C158/HQCDFBNUM"
C156_ROOT = "8ba1231561ad04e5e1e8e96de9e8a270b8ad284b804021489dbe02cff2c2270d"
C155_ROOT = "371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d"
C154_ROOT = "1a22cd636f3b48ef9fd51676d2761a986126b043ccfa04e9609cd2a126b67bff"
C153_ROOT = "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
C152_ROOT = "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da"
C151_ROOT = "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C150_ROOT = "2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a"
C144_ROOT = "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635"
RESOLUTIONS = ("K9", "K11", "K13")
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
_C153_QUANTITY = {"QUARK_FIELD":"quark_field", "SIGNED_QUARK_MASS":"signed_quark_mass", "TRANSVERSE_GLUON_FIELD":"gluon_field", "qg_VERTEX_DRESSING":"qg_vertex", "QCD_COUPLING":"qcd_coupling"}
ORDERS = {"QUARK_FIELD":0, "SIGNED_QUARK_MASS":0, "TRANSVERSE_GLUON_FIELD":0, "qg_VERTEX_DRESSING":1, "QCD_COUPLING":1}
TARGET_SCHEMES = ("MSBAR_C43_ADAPTED", "PROJECT_LIGHT_FRONT_NONEXCEPTIONAL", "RI_SMOM", "MOMQ", "STEP_SCALING")
FIXTURES = tuple(c156_core.FIXTURES)
IR_FAMILIES = ("IR-FB-LF-1", "IR-FB-LF-2", "IR-FB-LF-3")
ROUTES_FB = ("derivative", "spectral", "owner", "holdout")
ROUTES_CONT = ("light_front", "covariant_same_gauge", "adapted_standard", "holdout")


def _plain(value: Any) -> Any:
    if isinstance(value, MappingProxyType): return {k:_plain(v) for k,v in value.items()}
    if isinstance(value, Mapping): return {k:_plain(v) for k,v in value.items()}
    if isinstance(value, (tuple,list)): return [_plain(v) for v in value]
    return value
def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k:_freeze(v) for k,v in value.items()})
    if isinstance(value, (tuple,list)): return tuple(_freeze(v) for v in value)
    return value
def _canon(value: Any) -> str: return json.dumps(_plain(value), sort_keys=True, separators=(",",":"), ensure_ascii=True)
def _root(value: Any) -> str: return sha256(_canon(value).encode()).hexdigest()
def _require_mapping(record: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(record, Mapping): raise TypeError(f"{label} must be a mapping")
    return record


def _verify_ancestry() -> None:
    checks = ((c156.verify_hqcd_matching_grid_authority()["package_root"],C156_ROOT,"C156"),(c155.verify_hqcd_flavor_authority()["package_root"],C155_ROOT,"C155"),(c153.verify_hqcd_matching_authority()["package_root"],C153_ROOT,"C153"),(c152.verify_hqcd_qg_vertex_authority()["package_root"],C152_ROOT,"C152"),(c151.verify_hqcd_gluon_two_point_authority()["package_root"],C151_ROOT,"C151"),(c144.verify_hqcd_operator_authority()["package_root"],C144_ROOT,"C144"))
    for actual, expected, label in checks:
        if actual != expected: raise ValueError(f"{label} public root mismatch")
    if c150.PACKAGE_ROOT != C150_ROOT: raise ValueError("C150 public root mismatch")


def common_ir_numeric_record_schema() -> MappingProxyType:
    fields = ("schema","common_ir_numeric_id","ir_family_id","quantity_id","resolution","C153_matching_record_id","C153_matching_record_root","finite_basis_scheme_ids","target_scheme_id","active_Nf_record","external_flavor_record","common_external_state_record","invariant_record","rho","rho_units","mu","mu_units","rho_mu_relation","rho_mu_independent","gauge","light_front_pole_prescription","zero_mode_policy","boundary_policy","mass_regulator_policy","order_of_limits","parameter_record","fixture_id","precision_solver_record","variation_family_record","claim_tier","no_default","no_physical_claim","record_root")
    return _freeze({"schema":"C157-COMMON-IR-NUMERIC-RECORD-V1","required":fields,"no_default":True,"rho_mu_distinct":True,"families":IR_FAMILIES,"root":_root(fields)})

def _explicit_context(parameter_record: Any, fixture_id: str | None) -> MappingProxyType:
    if (parameter_record is None) == (fixture_id is None): raise ValueError("supply exactly one parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES: raise KeyError(fixture_id)
    if parameter_record is not None and not isinstance(parameter_record, Mapping): raise TypeError("parameter_record must be a mapping")
    return _freeze({"parameter_record":dict(parameter_record) if parameter_record is not None else None,"fixture_id":fixture_id})

def validate_common_ir_numeric_record(record: Mapping[str, Any]) -> MappingProxyType:
    record = _require_mapping(record,"common-IR record")
    for key in common_ir_numeric_record_schema()["required"]:
        if key not in record: raise ValueError(f"missing common-IR field: {key}")
    if record["schema"] != "C157-COMMON-IR-NUMERIC-RECORD-V1": raise ValueError("unknown common-IR schema")
    if record["ir_family_id"] not in IR_FAMILIES or record["resolution"] not in RESOLUTIONS: raise ValueError("unknown common-IR family or resolution")
    if record["quantity_id"] not in QUANTITIES or record["target_scheme_id"] not in TARGET_SCHEMES: raise ValueError("unknown common-IR quantity or target scheme")
    if not record["C153_matching_record_id"] or not record["C153_matching_record_root"]: raise ValueError("explicit C153 matching-record ID and root required")
    try: rho, mu = float(record["rho"]), float(record["mu"])
    except (TypeError,ValueError) as exc: raise ValueError("rho and mu must be numeric") from exc
    if rho <= 0 or mu <= 0 or record["rho_units"] != "GeV" or record["mu_units"] != "GeV": raise ValueError("rho and mu require positive GeV coordinates")
    if record["rho_mu_independent"] is not True: raise ValueError("rho and mu must remain explicitly independent")
    if not isinstance(record["invariant_record"],Mapping): raise ValueError("explicit invariant record required")
    if not isinstance(record["active_Nf_record"],Mapping) or "N_f" not in record["active_Nf_record"]: raise ValueError("explicit active-N_f record required")
    if not isinstance(record["common_external_state_record"],Mapping): raise ValueError("explicit common external-state record required")
    _explicit_context(record["parameter_record"],record["fixture_id"])
    if record["no_default"] is not True or record["no_physical_claim"] is not True: raise ValueError("common-IR defaults/physical claims are forbidden")
    if record["record_root"] != _root({k:v for k,v in record.items() if k != "record_root"}): raise ValueError("common-IR record root mismatch")
    return _freeze(dict(record))

def common_ir_family_registry() -> MappingProxyType:
    rows = ({"family_id":"IR-FB-LF-1","kind":"real_spacelike_off_shellness","p2":"-rho^2","quantities":("QUARK_FIELD","SIGNED_QUARK_MASS","TRANSVERSE_GLUON_FIELD"),"tier":"PHYSICAL_CANDIDATE","authorized":True},{"family_id":"IR-FB-LF-2","kind":"nonexceptional_q_g_q_off_shellness","invariants":("p_in^2","p_out^2","k^2","q^2","orientation"),"quantities":("qg_VERTEX_DRESSING","QCD_COUPLING"),"tier":"PHYSICAL_CANDIDATE","authorized":True},{"family_id":"IR-FB-LF-3","kind":"complex_nonexceptional_diagnostic_atlas","quantities":QUANTITIES,"tier":"DIAGNOSTIC_HOLDOUT","physical_claim":False,"authorized":True})
    return _freeze({"schema":"C157-COMMON-IR-FAMILY-REGISTRY-V1","rows":rows,"unauthorized_regulators":("small_gluon_mass","finite_epsilon","analytic_IR_regulator"),"root":_root(rows)})

def threshold_manifest() -> MappingProxyType:
    rows=(
        {"threshold_id":"C157_COMMON_IR_RESIDUAL_MAX","value":"1e-10","units":"dimensionless","frozen":True},
        {"threshold_id":"C157_PERTURBATIVE_REMAINDER_MAX","value":"0.10","units":"relative","frozen":True},
        {"threshold_id":"C157_ROUTE_RESIDUAL_ABS","value":"1e-12","units":"dimensionless","frozen":True},
    )
    return _freeze({"schema":"C157-THRESHOLD-MANIFEST-V1","rows":rows,"post_scan_tuning":False,"root":_root(rows)})

def common_external_state_numeric_crosswalk() -> MappingProxyType:
    fields=("normalization","positive_frequency","external_flavor","color","helicity_polarization","longitudinal_fraction","transverse_probe","off_shell_invariants","vertex_orientation","source_sink_order","tensor_projector","units")
    rows=tuple({"quantity_id":q,"finite_basis":"C43_FINITE_LIGHT_FRONT","target":"TARGET_NONEXCEPTIONAL_PROJECTED","reversible":True,"fields":fields} for q in QUANTITIES)
    return _freeze({"schema":"C157-COMMON-EXTERNAL-STATE-NUMERIC-CROSSWALK-V1","rows":rows,"active_Nf_separate_from_external_flavor":True,"flavor_averaging":False,"root":_root(rows)})

def _record_context(record: Mapping[str,Any], parameter_record: Any, fixture_id: str | None):
    ir=validate_common_ir_numeric_record(record); supplied=_explicit_context(parameter_record,fixture_id)
    if supplied["fixture_id"] != ir["fixture_id"]: raise ValueError("caller fixture_id differs from common-IR record")
    if supplied["parameter_record"] is not None and supplied["parameter_record"] != ir["parameter_record"]: raise ValueError("caller parameter_record differs from common-IR record")
    return ir,supplied
def _blocked(kind: str, *, ir: Mapping[str,Any], context: Mapping[str,Any], missing: tuple[str,...], extra: Mapping[str,Any]|None=None) -> MappingProxyType:
    out={"schema":f"C157-{kind}-NUMERIC-REPORT-V1","status":"BLOCKED","quantity_id":ir["quantity_id"],"resolution":ir["resolution"],"common_ir_numeric_id":ir["common_ir_numeric_id"],"rho":ir["rho"],"mu":ir["mu"],"context":context,"value":None,"enclosure":None,"missing_objects":missing,"no_physical_claim":True}
    if extra: out.update(extra)
    out["root"]=_root(out); return _freeze(out)

def _c153_record(ir: Mapping[str,Any]) -> dict[str,Any]:
    return {"schema":"C153-MATCHING-RECORD-V1","matching_id":ir["C153_matching_record_id"],"quantity_id":_C153_QUANTITY[ir["quantity_id"]],"finite_basis_scheme":ir["finite_basis_scheme_ids"][0],"target_scheme_id":ir["target_scheme_id"],"order":ORDERS[ir["quantity_id"]],"gauge":ir["gauge"],"N_f":ir["active_Nf_record"]["N_f"],"mu":"explicit","kinematics":"explicit","common_ir_id":ir["common_ir_numeric_id"],"no_default":True}

def finite_basis_numeric_coefficient(quantity_id: str, common_ir_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None, route="derivative") -> MappingProxyType:
    ir,context=_record_context(common_ir_record,parameter_record,fixture_id)
    if quantity_id != ir["quantity_id"] or quantity_id not in QUANTITIES: raise ValueError("quantity mismatch")
    if route not in ROUTES_FB: raise ValueError(f"unsupported finite-basis route: {route}")
    source=c153.finite_basis_perturbative_coefficient(_C153_QUANTITY[quantity_id],_c153_record(ir),parameter_record=context["parameter_record"],fixture_id=context["fixture_id"],route=route)
    if not isinstance(source.get("coefficient"),Mapping):
        return _blocked("FINITE-BASIS",ir=ir,context=context,missing=("C153_EXECUTABLE_FINITE_BASIS_AST","C153_NUMERICAL_ENCLOSURE"),extra={"route":route,"source_root":source["root"],"source_status":"SYMBOLIC_COEFFICIENT_LABEL_ONLY","fit_from_fixtures":False})
    raise ValueError("unsupported finite-basis expression operation; fail closed")

def continuum_numeric_coefficient(quantity_id: str, common_ir_record: Mapping[str,Any], route="target") -> MappingProxyType:
    ir=validate_common_ir_numeric_record(common_ir_record)
    if quantity_id != ir["quantity_id"] or quantity_id not in QUANTITIES: raise ValueError("quantity mismatch")
    if route == "target": route="light_front"
    if route not in ROUTES_CONT: raise ValueError(f"unsupported continuum route: {route}")
    if route == "holdout":
        return _blocked("CONTINUUM",ir=ir,context={"parameter_record":ir["parameter_record"],"fixture_id":ir["fixture_id"]},missing=("C153_ADMITTED_CONTINUUM_HOLDOUT",),extra={"route":route,"source_status":"NO_PUBLIC_HOLDOUT_EXPRESSION"})
    source=c153.continuum_target_coefficient(_C153_QUANTITY[quantity_id],_c153_record(ir),route=route)
    return _blocked("CONTINUUM",ir=ir,context={"parameter_record":ir["parameter_record"],"fixture_id":ir["fixture_id"]},missing=("C153_EXECUTABLE_TARGET_AST","C153_NUMERICAL_ENCLOSURE"),extra={"route":route,"source_root":source["root"],"source_status":"SYMBOLIC_COEFFICIENT_LABEL_ONLY"})

def direct_common_ir_difference(quantity_id: str, common_ir_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    ir,context=_record_context(common_ir_record,parameter_record,fixture_id); fb=finite_basis_numeric_coefficient(quantity_id,ir,parameter_record=parameter_record,fixture_id=fixture_id); target=continuum_numeric_coefficient(quantity_id,ir)
    return _blocked("DIRECT-DIFFERENCE",ir=ir,context=context,missing=("FINITE_BASIS_NUMERICAL_COEFFICIENT","CONTINUUM_TARGET_NUMERICAL_COEFFICIENT"),extra={"finite_basis_root":fb["root"],"target_root":target["root"],"delta_definition":"c_target(mu,rho)-c_FB(mu,rho)","same_rho_required":True,"rho_tuned_point":False})
def log_ir_derivative_report(quantity_id: str, common_ir_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    ir,context=_record_context(common_ir_record,parameter_record,fixture_id); difference=direct_common_ir_difference(quantity_id,ir,parameter_record=parameter_record,fixture_id=fixture_id)
    return _blocked("LOG-IR-DERIVATIVE",ir=ir,context=context,missing=("DIRECT_COMMON_IR_DIFFERENCE","EXECUTABLE_LOG_RHO_DERIVATIVE"),extra={"difference_root":difference["root"],"admitted_rho_interval":None,"single_point_cancellation":False})
def common_ir_variation_report(quantity_id: str, variation_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    variation=_require_mapping(variation_record,"variation record")
    if variation.get("schema") != "C157-COMMON-IR-VARIATION-V1" or not isinstance(variation.get("points"),(tuple,list)): raise ValueError("explicit common-IR variation family required")
    points=tuple(validate_common_ir_numeric_record(p) for p in variation["points"])
    if not points: raise ValueError("nonempty rho variation atlas required")
    reports=tuple(direct_common_ir_difference(quantity_id,p,parameter_record=parameter_record,fixture_id=fixture_id) for p in points)
    return _freeze({"schema":"C157-COMMON-IR-VARIATION-REPORT-V1","status":"BLOCKED","points":reports,"rho_interval":(min(p["rho"] for p in points),max(p["rho"] for p in points)),"just_inside_outside_holdouts":bool(variation.get("endpoint_holdouts")),"threshold_tuning":False,"root":_root(reports)})
def conversion_numeric_report(quantity_id: str, common_ir_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    ir,context=_record_context(common_ir_record,parameter_record,fixture_id); direct=direct_common_ir_difference(quantity_id,ir,parameter_record=parameter_record,fixture_id=fixture_id)
    return _blocked("CONVERSION",ir=ir,context=context,missing=("DIRECT_COMMON_IR_DIFFERENCE","PROJECTED_GREEN_FUNCTION_RATIO","INVERSE_CONVERSION","ROUND_TRIP_FB_TARGET","ROUND_TRIP_TARGET_FB"),extra={"direct_root":direct["root"],"routes":("C-A","C-B","C-C","C-D","C-E"),"agreement":False})

def perturbative_control_record_schema() -> MappingProxyType:
    fields=("schema","perturbative_control_id","quantity_id","computed_order","first_omitted_order","coupling_coordinate","coupling_envelope","scale_log_envelope","known_next_coefficient","power_counting_authority","scale_variation_family","route_disagreement_policy","remainder_combination_policy","claim_tier","no_default","no_physical_claim","record_root")
    return _freeze({"schema":"C157-PERTURBATIVE-CONTROL-RECORD-V1","required":fields,"scale_variation_not_remainder_by_default":True,"root":_root(fields)})
def _validate_control(record: Mapping[str,Any],quantity_id:str) -> MappingProxyType:
    record=_require_mapping(record,"perturbative-control record")
    for key in perturbative_control_record_schema()["required"]:
        if key not in record: raise ValueError(f"missing perturbative-control field: {key}")
    if record["schema"] != "C157-PERTURBATIVE-CONTROL-RECORD-V1" or record["quantity_id"] != quantity_id: raise ValueError("quantity or perturbative-control schema mismatch")
    if not isinstance(record["coupling_envelope"],Mapping) or not isinstance(record["scale_log_envelope"],Mapping): raise ValueError("explicit coupling/log envelopes required")
    if record["no_default"] is not True or record["no_physical_claim"] is not True: raise ValueError("perturbative-control claim guard failed")
    if record["record_root"] != _root({k:v for k,v in record.items() if k != "record_root"}): raise ValueError("perturbative-control root mismatch")
    return _freeze(dict(record))
def first_omitted_order_report(quantity_id: str, common_ir_record: Mapping[str,Any], perturbative_control_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    ir,context=_record_context(common_ir_record,parameter_record,fixture_id); control=_validate_control(perturbative_control_record,quantity_id)
    return _blocked("FIRST-OMITTED-ORDER",ir=ir,context=context,missing=("FINITE_BASIS_NUMERICAL_COEFFICIENT","SOURCE_QUALIFIED_NEXT_COEFFICIENT_OR_POWER_COUNTING"),extra={"perturbative_control_root":control["record_root"],"classification":"UNAVAILABLE_BLOCKING","scale_variation_only":True,"missing_sector_remainder_zeroed":False})
def numerical_perturbative_remainder(quantity_id: str, common_ir_record: Mapping[str,Any], perturbative_control_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    report=first_omitted_order_report(quantity_id,common_ir_record,perturbative_control_record,parameter_record=parameter_record,fixture_id=fixture_id); out=dict(report); out.update({"schema":"C157-NUMERICAL-PERTURBATIVE-REMAINDER-REPORT-V1","missing_sector_remainder":None,"certified_bound":None}); out["root"]=_root(out); return _freeze(out)
def positive_scale_bracket(quantity_id: str, bracket_request_record: Mapping[str,Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    request=_require_mapping(bracket_request_record,"bracket request")
    if request.get("schema") != "C157-POSITIVE-SCALE-BRACKET-REQUEST-V1": raise ValueError("explicit bracket request schema required")
    ir=validate_common_ir_numeric_record(request.get("common_ir_record")); _explicit_context(parameter_record,fixture_id)
    if quantity_id != ir["quantity_id"]: raise ValueError("quantity mismatch")
    if request.get("preferred_scale_injected") is True: raise ValueError("preferred scale injection forbidden")
    return _freeze({"schema":"C157-POSITIVE-SCALE-BRACKET-REPORT-V1","status":"AUTHORITY_DERIVED_BRACKET_INCOMPLETE","quantity_id":quantity_id,"resolution":ir["resolution"],"intervals":(),"domain_intersection":request.get("public_domains",()),"endpoints_selected":False,"physical_scale_selected":False,"root":_root((quantity_id,ir["record_root"],"incomplete"))})
def flavor_ir_covariance_report() -> MappingProxyType:
    base=c155.descendant_flavor_covariance_report()
    return _freeze({"schema":"C157-U-D-IR-COVARIANCE-V1","status":"BLOCKED_BY_FINITE_BASIS_EVALUATOR","u_equals_d_by_block_identity":True,"block_identity_root":base["root"],"u_d_common_ir_residual":"transported, not averaged","u_d_remainder":"transported, not averaged","u_d_bracket":"transported, not averaged","active_Nf_changed":False,"flavor_averaging":False,"root":_root((base["root"],STATUS))})
def quantity_order_execution_ledger() -> MappingProxyType:
    rows=tuple({"quantity_id":q,"resolution":r,"computed_order":ORDERS[q],"finite_basis":"BLOCKED_PUBLIC_C153_SYMBOLIC_ONLY","continuum_target":"BLOCKED_PUBLIC_C153_SYMBOLIC_ONLY","common_external_state":"DECLARED_CROSSWALK_NOT_NUMERICALLY_EXECUTED","common_ir":"BLOCKED","cancellation":"BLOCKED","remainder":"BLOCKED","positive_bracket":"BLOCKED","missing_objects":("finite_basis_numeric_ast",)} for q in QUANTITIES for r in RESOLUTIONS)
    return _freeze({"schema":"C157-QUANTITY-ORDER-EXECUTION-LEDGER-V1","rows":rows,"quantity_count":5,"resolution_count":3,"averaging":False,"root":_root(rows)})
def matching_grid_rerun_contract() -> MappingProxyType:
    return _freeze({"schema":"C157-MATCHING-GRID-RERUN-CONTRACT-V1","full_grid_executed":False,"final_windows_published":False,"mass_coupling_intersections":False,"next":"C158/HQCDFBNUM","root":_root(("no-grid","HQCDFBNUM"))})

def physical_input_resumption_contract() -> MappingProxyType:
    return _freeze({"schema":"C157-PHYSICAL-INPUT-RESUMPTION-V1","C156_root":C156_ROOT,"numeric_evidence":"finite-basis evaluator missing","windows":"empty","running":False,"inverse_matching":False,"next":NEXT,"root":_root((C156_ROOT,"blocked",NEXT))})

def quantum_matching_handoff_contract() -> MappingProxyType:
    return _freeze({"schema":"C157-QUANTUM-MATCHING-HANDOFF-V1","Q0_modified":False,"Q1_modified":False,"PennyLane":False,"physical_scale_selected":False,"physical_state":False,"status":"NOT_ACTIVATED","root":_root((False,False,False,False))})
def matchir_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C157-MATCHIR-COMPLETENESS-CERTIFICATE-V1","status":STATUS,"positive_gate":False,"plan":PLAN,"finite_basis_numeric":False,"continuum_target_numeric":False,"common_external_state":False,"common_ir_numeric":False,"direct_difference":False,"log_ir_derivative":False,"rho_variation":False,"conversion_round_trip":False,"perturbative_control":True,"first_omitted_order":False,"numerical_remainder":False,"positive_scale_bracket":False,"u_d_covariance":True,"full_C156_grid_rerun":False,"physical_scale_selection":False,"running_threshold":False,"inverse_physical_matching":False,"physical_target":False,"parameter_solution":False,"missing_objects":("C153 executable finite-basis projected coefficient AST",),"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def matchir_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C157-MATCHIR-PLAN-V1","selected_plan":PLAN,"status":STATUS,"first_remaining_object":"FINITE_BASIS_NUMERICAL_EVALUATOR","root":_root((PLAN,STATUS))})

def verify_hqcd_matchir_authority() -> dict[str,Any]:
    _verify_ancestry()
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"baseline":BASELINE,"contract":CONTRACT,"plan":PLAN,"C156_package_root":C156_ROOT,"C155_package_root":C155_ROOT,"C154_package_root":C154_ROOT,"C153_package_root":C153_ROOT,"C152_package_root":C152_ROOT,"C151_package_root":C151_ROOT,"C150_package_root":C150_ROOT,"C144_package_root":C144_ROOT,"full_grid_executed":False,"physical_inputs_consumed":0,"PDG_FLAG_ALPHA_consumed":0,"running_thresholds":False,"Q0_Q1_modified":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_matchir_authority() -> MappingProxyType:
    path=RUNTIME/"manifest.json"
    if not path.exists(): raise FileNotFoundError("C157 runtime manifest missing")
    manifest=json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C157 root/status mismatch")
    return _freeze(verify_hqcd_matchir_authority())
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"physical_inputs_consumed":0,"implicit_ir":0,"implicit_scale":0,"implicit_scheme":0,"implicit_Nf":0,"implicit_flavor":0,"implicit_fixture":0,"implicit_parameter":0,"fit_from_fixtures":0,"unauthorized_regulators":0,"missing_remainders_zeroed":0,"full_grid":0,"physical_scale":0,"running":0,"thresholds":0,"inverse_physical_matching":0,"Q0_Q1_modified":0,"states":0,"TMD":0,"pass":True})
def mutate_live_hqcdmatchir2(index:int) -> MappingProxyType:
    fields=("C156_root","C155_root","C153_root","C152_root","C151_root","C150_root","C144_root","ir_family","rho","mu","rho_mu_relation","gauge","pole","zero_mode","boundary","external_state","finite_ast","target_ast","log_basis","derivative","atlas","conversion","coupling_envelope","next_coefficient","remainder_class","bracket","u_d_identity","fixture","resolution","package_root","C158_continuation")
    return _freeze({"mutation":fields[int(index)%len(fields)],"must_fail_or_change_root":True,"positive_gate":False})

# C157 stub compatibility: these remain explicitly blocked and never expose
# a scale window.  They are retained so old callers cannot bypass the new
# record/context guards by using the former gate names.
def numerical_evidence_schema() -> MappingProxyType:
    schema = dict(common_ir_numeric_record_schema())
    schema.update({"schema": "C157-NUMERICAL-EVIDENCE-V1", "numeric_fields_are_required": True,
                   "source_and_evaluator_hashes_required": True})
    schema["root"] = _root(schema)
    return _freeze(schema)

def validate_numerical_evidence(record: Mapping[str, Any]) -> MappingProxyType:
    record = _require_mapping(record, "numerical evidence")
    if record.get("schema") != "C157-NUMERICAL-EVIDENCE-V1":
        raise ValueError("unknown numerical evidence schema")
    for key in ("mu", "common_ir_residual", "perturbative_remainder", "route_residual",
                "spectral_distance", "projector_condition", "no_default", "no_physical_claim", "evidence_root"):
        if key not in record: raise ValueError(f"missing numerical evidence field: {key}")
    if record["no_default"] is not True or record["no_physical_claim"] is not True:
        raise ValueError("numerical-evidence claim guard failed")
    if record["evidence_root"] != _root({k:v for k,v in record.items() if k != "evidence_root"}):
        raise ValueError("numerical evidence root mismatch")
    return _freeze(dict(record))

def common_ir_gate_report(grid_record: Mapping[str, Any], mu: Any, *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    grid = c156.validate_matching_grid_record(grid_record)
    context = _explicit_context(parameter_record, fixture_id)
    scale = float(mu)
    if scale <= 0: raise ValueError("mu must be positive")
    return _freeze({"schema":"C157-COMMON-IR-GATE-V1","matching_grid_id":grid["matching_grid_id"],"resolution":grid["resolution"],"quantity_id":grid["quantity_id"],"mu":scale,"context":context,"common_ir_residual":None,"threshold_id":"C157_COMMON_IR_RESIDUAL_MAX","status":"NUMERICAL_COMMON_IR_AUTHORITY_MISSING","admitted":False,"root":_root((grid["grid_record_root"],scale,context,"blocked"))})

def perturbative_remainder_report(grid_record: Mapping[str, Any], mu: Any, *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    grid = c156.validate_matching_grid_record(grid_record)
    context = _explicit_context(parameter_record, fixture_id)
    scale = float(mu)
    if scale <= 0: raise ValueError("mu must be positive")
    return _freeze({"schema":"C157-PERTURBATIVE-REMAINDER-GATE-V1","matching_grid_id":grid["matching_grid_id"],"resolution":grid["resolution"],"quantity_id":grid["quantity_id"],"mu":scale,"context":context,"remainder":None,"threshold_id":"C157_PERTURBATIVE_REMAINDER_MAX","status":"NUMERICAL_PERTURBATIVE_REMAINDER_AUTHORITY_MISSING","admitted":False,"root":_root((grid["grid_record_root"],scale,context,"blocked"))})

def evaluate_matching_ir_gates(grid_record: Mapping[str, Any], mu: Any, *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    common = common_ir_gate_report(grid_record, mu, parameter_record=parameter_record, fixture_id=fixture_id)
    remainder = perturbative_remainder_report(grid_record, mu, parameter_record=parameter_record, fixture_id=fixture_id)
    return _freeze({"schema":"C157-MATCHING-IR-GATE-V1","common_ir_root":common["root"],"remainder_root":remainder["root"],"common_ir":common,"perturbative_remainder":remainder,"admitted":False,"failure_reasons":("COMMON_IR_NUMERICAL_AUTHORITY_MISSING","PERTURBATIVE_REMAINDER_NUMERICAL_AUTHORITY_MISSING"),"root":_root((common["root"],remainder["root"],"blocked"))})

def candidate_scale_domain(grid_record: Mapping[str, Any]) -> MappingProxyType:
    grid = c156.validate_matching_grid_record(grid_record)
    return _freeze({"schema":"C157-CANDIDATE-SCALE-DOMAIN-V1","matching_grid_id":grid["matching_grid_id"],"resolution":grid["resolution"],"quantity_id":grid["quantity_id"],"intervals":(),"status":"AUTHORITY_DERIVED_BRACKET_INCOMPLETE","arbitrary_endpoints":False,"preferred_scales_injected":False,"root":_root((grid["grid_record_root"],"blocked"))})

def componentwise_matching_window(grid_record: Mapping[str, Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    grid = c156.validate_matching_grid_record(grid_record)
    context = _explicit_context(parameter_record, fixture_id)
    return _freeze({"schema":"C157-COMPONENTWISE-WINDOW-V1","matching_grid_id":grid["matching_grid_id"],"resolution":grid["resolution"],"quantity_id":grid["quantity_id"],"context":context,"intervals":(),"disconnected_components":(),"status":"EMPTY_BECAUSE_NUMERICAL_GATES_UNAVAILABLE","root":_root((grid["grid_record_root"],context,"empty"))})

def cross_resolution_window_report(window_roots: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(window_roots, Mapping) or set(window_roots) != set(RESOLUTIONS):
        raise ValueError("explicit K9/K11/K13 window roots required")
    return _freeze({"schema":"C157-CROSS-RESOLUTION-WINDOW-V1","window_roots":dict(window_roots),"intersection":(),"status":"NO_COMMON_DOMAIN","resolution_averaging":False,"root":_root((dict(window_roots),"empty"))})

def _roots() -> dict[str,str]:
    return {"C157_INPUT_ROOT":_root((BASELINE,CONTRACT,C156_ROOT,C155_ROOT,C153_ROOT)),"C157_PLAN_ROOT":matchir_plan_manifest()["root"],"C157_EXECUTION_LEDGER_ROOT":quantity_order_execution_ledger()["root"],"C157_IR_SCHEMA_ROOT":common_ir_numeric_record_schema()["root"],"C157_IR_FAMILY_ROOT":common_ir_family_registry()["root"],"C157_EXTERNAL_STATE_ROOT":common_external_state_numeric_crosswalk()["root"],"C157_FB_NUMERIC_ROOT":_root(("finite-basis","blocked",C153_ROOT)),"C157_CONTINUUM_NUMERIC_ROOT":_root(("continuum","blocked",C153_ROOT)),"C157_DIRECT_DIFFERENCE_ROOT":_root(("delta","blocked")),"C157_LOG_IR_DERIVATIVE_ROOT":_root(("log-rho","blocked")),"C157_IR_VARIATION_ROOT":_root(("rho-atlas","blocked")),"C157_CONVERSION_NUMERIC_ROOT":_root(("conversion","blocked")),"C157_PERTURBATIVE_CONTROL_ROOT":perturbative_control_record_schema()["root"],"C157_FIRST_OMITTED_ORDER_ROOT":_root(("omitted-order","blocked")),"C157_NUMERICAL_REMAINDER_ROOT":_root(("remainder","blocked")),"C157_POSITIVE_BRACKET_ROOT":_root(("positive-bracket","blocked")),"C157_FLAVOR_COVARIANCE_ROOT":flavor_ir_covariance_report()["root"],"C157_PARAMETER_RESOLUTION_ROOT":_root((RESOLUTIONS,"fixtures-separate","blocked")),"C157_GRID_PREFLIGHT_ROOT":_root(("bounded-preflight","not-executed")),"C157_GRID_RERUN_HANDOFF_ROOT":matching_grid_rerun_contract()["root"],"C157_QUANTUM_HANDOFF_ROOT":_root(("Q0","Q1","unchanged")),"C157_SCOPE_ROOT":_root(("no-physical-claims","no-grid")),"C157_COMPLETENESS_ROOT":matchir_completeness_certificate()["root"]}
ROOTS=_roots()
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS,"ancestry":(C156_ROOT,C155_ROOT,C154_ROOT,C153_ROOT,C152_ROOT,C151_ROOT,C150_ROOT,C144_ROOT)})

# Compatibility names retained for callers of the earlier fail-closed stub.
matching_ir_completeness_certificate=matchir_completeness_certificate
matching_ir_plan_manifest=matchir_plan_manifest
verify_hqcd_matching_ir_authority=verify_hqcd_matchir_authority
load_verified_hqcd_matching_ir_authority=load_verified_hqcd_matchir_authority
__all__=[name for name in globals() if not name.startswith("_")]
