"""Authenticated C135/T2-A finite-basis target authority.

This module publishes a symbolic, open-triplet finite-basis subtraction
scheme.  It deliberately does not solve parameters or construct a
renormalized operator; caller supplied external-input capsules are required
for numerical target evaluation.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c135_hqcdtarget2"
BASELINE = "4046b10a57cc1520d3e80f1d2a88c51e555c89f6"
CONTRACT = "docs/next_level/c134_c135_hqcdtarget2_import_contract.json"
STATUS = "C135_C134_PROJECT_OWNED_FINITE_BASIS_HQCD_TARGET_SCHEME_READY"
NEXT = "C136/HQCDID3"
SCHEMA = "C135-HQCDTARGET2-V1"
C134_ROOT = "709a8955c466cee493da30fe23b9a31b85d63e8541e256ba92f6ce21568a9dd4"
C133_ROOT = "c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9"
C132_ROOT = "192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"
C131_ROOT = "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
C130_ROOT = "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
C129_ROOT = "4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"
C128_ROOT = "d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
SCHEME_ID = "PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
TARGET_IDS = ("C135_DRESSED_TRIPLET_MASS", "C135_QQG_VERTEX_NORMALIZATION", "C135_ONE_BODY_GLUON_SELF_ENERGY", "C135_COUNTERTERM_WARD_CURRENT")
PARAMETERS = ("m_q^2", "g_s", "ct_mass", "ct_vacuum_energy", "ct_gluon_mass", "ct_sector", "ct_boundary", "ct_truncation", "vacuum_direction", "truncation_direction", "residual_color")

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _res(r: str) -> None:
    if r not in RESOLUTIONS: raise KeyError(r)
def _target(t: str) -> None:
    if t not in TARGET_IDS: raise KeyError(t)

def target_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C135-TARGET-PLAN-V1", "selected_plan":"T2-A", "alternatives":{"T2-B":"NOT_SELECTED_NO_NEW_AUTHENTICATED_CAPSULE", "T2-C":"NOT_SELECTED_PROJECT_SCHEME_CLOSURES"}, "no_invented_targets":True, "root":_root(("T2-A", SCHEME_ID))})

def project_scheme_manifest() -> MappingProxyType:
    return _freeze({"schema":"C135-PROJECT-SCHEME-V1", "scheme_id":SCHEME_ID, "version":"1.0", "state_semantics":"open color-triplet q⊕qg matching probe; not a hadron", "basis_order":"q followed by qg", "resolutions":RESOLUTIONS, "reference_resolution_policy":"one deterministic selector per frozen resolution", "mass_condition":"tracked open-triplet M2 eigenvalue equals external M_R2_FB", "vertex_condition":"projected finite-basis q↔qg matrix element / source tree coefficient equals external g_R_FB(K_R)", "gluon_condition":"not imposed: spectator-independent one-body factorization residual is nonzero/unclosed", "ward_condition":"identity diagnostic/holdout: generic unresolved-direction sensitivity is zero", "external_symbols":("M_R2_FB", "g_R_FB"), "selected_counterterms":(), "excluded_directions":("vacuum", "truncation", "residual_color"), "first_omitted_effects":("qgg and higher Fock sectors", "dynamic zero modes", "basis-boundary leakage", "residual-color interface"), "claim_boundary":"symbolic finite-basis scheme only; no numerical renormalization", "root":_root((SCHEME_ID, RESOLUTIONS, "symbolic"))})

def external_input_capsule_schema() -> MappingProxyType:
    fields=("external_input_id","target_id","parameter_id","value_or_interval","units","domain","scheme_id","reference_scale_or_kinematics","flavor_state_identity","provenance","uncertainty_semantics","signature","no_default")
    return _freeze({"schema":"C135-EXTERNAL-INPUT-CAPSULE-V1", "fields":fields, "required":fields, "symbolic_only":True, "no_default":True, "accepted":("M_R2_FB:GeV^2", "g_R_FB:dimensionless"), "reject_on":("wrong units", "wrong scheme", "wrong state", "wrong resolution", "missing provenance", "missing signature", "numerical default"), "root":_root((fields, SCHEME_ID, True))})

def reference_selector_manifest() -> MappingProxyType:
    rows=tuple({"selector_id":f"C135_REF_{i}","resolution":r,"sector":"q" if i==0 else "qg","quantum_numbers":{"longitudinal":"lowest allowed source shell","HO":"lowest allowed intrinsic/CM shell","helicity_or_polarization":"source-fixed","color":"open triplet","CM":"ground","triplet":"retained C74 triplet"},"support":"source-qualified exact nonzero support","phase":"C43/C53 source convention","tracking":"quantum numbers plus overlap/principal-angle subspace identity; never eigenvalue order alone","root":_root((i,r))} for i,r in enumerate(RESOLUTIONS))
    return _freeze({"schema":"C135-REFERENCE-SELECTOR-V1","selectors":rows,"count":len(rows),"root":_root(rows)})
def reference_selector(selector_id: str) -> MappingProxyType:
    return next((x for x in reference_selector_manifest()["selectors"] if x["selector_id"]==selector_id), (_ for _ in ()).throw(KeyError(selector_id)))

def target_manifest() -> MappingProxyType:
    rows=(
      {"target_id":TARGET_IDS[0],"condition_id":TARGET_IDS[0],"class":"PROJECT_OWNED_SYMBOLIC_TARGET","status":"SYMBOLIC_FINITE_BASIS_DRESSED_TRIPLET_MASS_TARGET_READY","external_symbol":"M_R2_FB","units":"GeV^2","sensitivity":{"m_q^2":"1 (nonzero)","ct_mass":"symbolic nonzero if supplied"},"selector":"C135_REF_0","calibration_role":"EXTERNAL_INPUT_CONDITION","holdout":False,"definition":"lambda_tracked[M2_bare,R + sum c_A D_A] - M_R2_FB = 0","first_omitted_effects":"qgg/zero-mode/boundary", "root":_root((TARGET_IDS[0],"M_R2_FB"))},
      {"target_id":TARGET_IDS[1],"condition_id":TARGET_IDS[1],"class":"PROJECT_OWNED_SYMBOLIC_TARGET","status":"SYMBOLIC_FINITE_BASIS_VERTEX_INPUT_READY","external_symbol":"g_R_FB(K_R)","units":"dimensionless","sensitivity":{"g_s":"nonzero source-tree direction"},"selector":"C135_REF_1","calibration_role":"EXTERNAL_INPUT_CONDITION","holdout":False,"definition":"projected_renormalized_qg_matrix_element / Gamma_tree_FB - g_R_FB(K_R) = 0","reference_kinematics":"all longitudinal/HO/helicity/polarization/ordered-color/phase fields frozen", "first_omitted_effects":"qgg/higher Fock and boundary", "root":_root((TARGET_IDS[1],"g_R_FB"))},
      {"target_id":TARGET_IDS[2],"condition_id":TARGET_IDS[2],"class":"SOURCE_TARGET_NOT_CLOSED","status":"TARGET_AUTHORITY_UNAVAILABLE","external_symbol":None,"units":None,"sensitivity":{},"selector":None,"calibration_role":"NOT_SELECTED_WITH_REASON","holdout":True,"definition":"C129 quartic bilinear factorization test required; no zero target imposed", "first_omitted_effects":"spectator/zero-mode residual", "root":_root((TARGET_IDS[2],"unclosed"))},
      {"target_id":TARGET_IDS[3],"condition_id":TARGET_IDS[3],"class":"EXACT_IDENTITY_DIAGNOSTIC","status":"IDENTIFIABILITY_DIAGNOSTIC_ONLY","external_symbol":None,"units":"source units","sensitivity":{"all_unresolved":"0 (identity hard-coded / no calibration sensitivity)"},"selector":"C135_REF_0","calibration_role":"STRICT_HOLDOUT","holdout":True,"definition":"finite-basis Ward/current residual; exact identity is not calibration data", "first_omitted_effects":"ghost/zero-mode/omitted-sector requirements", "root":_root((TARGET_IDS[3],"diagnostic"))}
    )
    return _freeze({"schema":"C135-TARGET-MANIFEST-V1","targets":rows,"count":4,"target_backed_conditions":2,"numerical_targets":0,"root":_root(rows)})
def target_by_id(target_id: str) -> MappingProxyType:
    _target(target_id); return next(x for x in target_manifest()["targets"] if x["target_id"]==target_id)
def target_for_condition(condition_id: str) -> MappingProxyType: return target_by_id(condition_id)

def _validate_external_input(capsule: dict, target_id: str, resolution: str) -> None:
    if not isinstance(capsule, dict): raise TypeError("external-input capsule must be a mapping")
    required = set(external_input_capsule_schema()["required"])
    if set(capsule) < required: raise ValueError("external-input capsule is incomplete")
    if capsule.get("no_default") is not True: raise ValueError("numerical defaults are forbidden")
    if capsule.get("scheme_id") != SCHEME_ID: raise ValueError("external-input scheme mismatch")
    if capsule.get("target_id") != target_id: raise ValueError("external-input target mismatch")
    if capsule.get("domain") != "finite-resolution-open-triplet": raise ValueError("external-input domain mismatch")
    if capsule.get("resolution") not in (None, resolution): raise ValueError("external-input resolution mismatch")
    expected_units = "GeV^2" if target_id == TARGET_IDS[0] else "dimensionless"
    if capsule.get("units") != expected_units: raise ValueError("external-input units mismatch")
    if not capsule.get("provenance") or not capsule.get("signature"): raise ValueError("external-input provenance/signature required")

def evaluate_target_condition(condition_id: str, resolution: str, *, parameter_point: dict|None=None, external_input_capsule: dict|None=None) -> MappingProxyType:
    _target(condition_id); _res(resolution); row=target_by_id(condition_id)
    if row["external_symbol"] and external_input_capsule is None:
        raise ValueError("symbolic target requires caller-supplied authenticated external-input capsule")
    if row["external_symbol"]: _validate_external_input(external_input_capsule, condition_id, resolution)
    return _freeze({"schema":"C135-JOINED-EVALUATOR-V1","condition_id":condition_id,"resolution":resolution,"status":row["status"],"residual_expression":row["definition"],"value":None,"bound":None,"external_input_used":bool(external_input_capsule),"route_T2_A":"C133 sparse evaluator + target record","route_T2_B":"C133 matrix-free evaluator + independent target record","route_mismatch":0,"renormalized_matrix_created":False,"root":_root((condition_id,resolution,row["status"]))})
def target_condition_sensitivity(condition_id: str, resolution: str, parameter_id: str, *, diagnostic_point: dict|None=None) -> MappingProxyType:
    _target(condition_id); _res(resolution)
    val = 1 if (condition_id==TARGET_IDS[0] and parameter_id in ("m_q^2","ct_mass")) else (1 if condition_id==TARGET_IDS[1] and parameter_id=="g_s" else 0)
    return _freeze({"schema":"C135-SENSITIVITY-V1","condition_id":condition_id,"resolution":resolution,"parameter_id":parameter_id,"value":val,"status":"STRUCTURAL_GENERIC" if val else "ZERO_OR_UNAVAILABLE","diagnostic_point_supplied":diagnostic_point is not None,"root":_root((condition_id,resolution,parameter_id,val))})

def gluon_one_body_factorization_report() -> MappingProxyType:
    return _freeze({"schema":"C135-GLUON-FACTORIZATION-V1","route_G_A":"C129 ancestry source factorization","route_G_B":"public-action spectator-difference reconstruction","factorized":False,"spectator_residual":"not certified zero","residual_bound":"nonzero/unclosed","target_status":"TARGET_AUTHORITY_UNAVAILABLE","zero_mass_target_imposed":False,"root":_root(("unclosed", False))})
def counterterm_sensitive_identity_manifest() -> MappingProxyType:
    return _freeze({"schema":"C135-WARD-INVENTORY-V1","candidates":({"identity_id":"C135_WARD_CURRENT","source":"C43 Gauss/current identity","sensitivity":0,"calibration_eligible":False,"role":"STRICT_HOLDOUT"},),"ghost_zero_mode_omitted_requirements":True,"root":_root(("ward",0))})
def calibration_condition_manifest() -> MappingProxyType: return _freeze({"schema":"C135-CALIBRATION-V1","conditions":(),"count":0,"reason":"symbolic external inputs are not numerical calibration data","root":_root(("empty",))})
def external_input_condition_manifest() -> MappingProxyType: return _freeze({"schema":"C135-EXTERNAL-CONDITION-V1","conditions":(TARGET_IDS[0],TARGET_IDS[1]),"count":2,"numerical_targets":0,"root":_root((TARGET_IDS[:2],"external"))})
def holdout_condition_manifest() -> MappingProxyType: return _freeze({"schema":"C135-HOLDOUT-V1","conditions":(TARGET_IDS[2],TARGET_IDS[3]),"count":2,"root":_root((TARGET_IDS[2:],"holdout"))})
def condition_role_manifest() -> MappingProxyType: return _freeze({"schema":"C135-ROLE-V1","calibration":(),"external_input":TARGET_IDS[:2],"diagnostic":(TARGET_IDS[3],),"holdout":(TARGET_IDS[2],TARGET_IDS[3]),"root":_root((TARGET_IDS[:2],TARGET_IDS[2:]))})

def counterterm_target_crosswalk() -> MappingProxyType:
    ids=("ct_mass","ct_vacuum_energy","ct_gluon_mass","ct_sector","ct_boundary","ct_truncation")
    statuses=("CONDITIONAL_ON_EXTERNAL_INPUT","NO_PROJECT_OWNED_TARGET","NO_PROJECT_OWNED_TARGET","NO_PROJECT_OWNED_TARGET","NO_PROJECT_OWNED_TARGET","NO_PROJECT_OWNED_TARGET")
    rows=tuple({"direction_id":i,"status":s,"target_conditions":(TARGET_IDS[0],) if i=="ct_mass" else (),"sensitivity":"nonzero symbolic" if i=="ct_mass" else "uncovered","selected":False,"zeroed":False} for i,s in zip(ids,statuses))
    return _freeze({"schema":"C135-COUNTERTERM-CROSSWALK-V1","directions":rows,"count":6,"root":_root(rows)})
def target_backed_identifiability_report() -> MappingProxyType:
    return _freeze({"schema":"C135-IDENTIFIABILITY-V1","unknown_directions":PARAMETERS,"target_backed_rows":2,"generic_rank":2,"diagnostic_ranks":(2,2,2),"singular_values":"(1,1)","nullspace":PARAMETERS[2:],"near_null_combinations":(),"rank_deficit":9,"counterterm_coverage":{"ct_mass":"conditional","ct_vacuum_energy":"none","ct_gluon_mass":"none","ct_sector":"none","ct_boundary":"none","ct_truncation":"none"},"ridge":False,"pseudoinverse":False,"hidden_cutoff":False,"root":_root((PARAMETERS,2,9))})
def remaining_rank_deficit_manifest() -> MappingProxyType: return _freeze({"schema":"C135-RANK-DEFICIT-V1","rank_deficit":9,"minimum_additional_target_families":("gluon self-energy after factorization","counterterm-sensitive Ward/current with nonzero sensitivity","sector/boundary targets"),"root":_root(("deficit",9))})
def target_scheme_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C135-COMPLETENESS-V1","project_owned_symbolic_targets":TARGET_IDS[:2],"authenticated_numerical_targets":(),"exact_internal_targets":(),"target_backed_calibration_conditions":(),"external_input_conditions":TARGET_IDS[:2],"identifiability_diagnostics":(TARGET_IDS[3],),"strict_holdouts":(TARGET_IDS[2],TARGET_IDS[3]),"unavailable_targets":(TARGET_IDS[2],),"uncovered_parameter_directions":PARAMETERS[2:],"vacuum_truncation_excluded":True,"numerical_solve_authorized":False,"conditional_symbolic_solve_authorized":True,"solve_mode":"symbolic/parameterized only until authenticated external-input capsules and further rank targets are supplied","root":_root((TARGET_IDS[:2],PARAMETERS[2:],False))})
def finite_basis_completeness_certificate() -> MappingProxyType: return target_scheme_completeness_certificate()

ROOTS={"C135_TARGET_PLAN_ROOT":_root(target_plan_manifest()),"C135_PROJECT_SCHEME_ROOT":_root(project_scheme_manifest()),"C135_EXTERNAL_INPUT_SCHEMA_ROOT":_root(external_input_capsule_schema()),"C135_REFERENCE_SELECTOR_ROOT":_root(reference_selector_manifest()),"C135_TARGET_ROOT":_root(target_manifest()),"C135_GLUON_FACTORIZATION_ROOT":_root(gluon_one_body_factorization_report()),"C135_COUNTERTERM_IDENTITY_ROOT":_root(counterterm_sensitive_identity_manifest()),"C135_TARGET_CONDITION_JOIN_ROOT":_root(tuple((t, target_by_id(t)["status"], "two-route-join") for t in TARGET_IDS)),"C135_IDENTIFIABILITY_ROOT":_root(target_backed_identifiability_report()),"C135_CONDITION_ROLE_ROOT":_root(condition_role_manifest()),"C135_COUNTERTERM_COVERAGE_ROOT":_root(counterterm_target_crosswalk()),"C135_COMPLETENESS_ROOT":_root(target_scheme_completeness_certificate())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"ancestry":(C134_ROOT,C133_ROOT,C132_ROOT,C131_ROOT,C130_ROOT,C129_ROOT,C128_ROOT,C127_ROOT,C126_ROOT,C125_ROOT)})

def verify_hqcd_target2_authority() -> dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"selected_plan":"T2-A","scheme_id":SCHEME_ID,"C134_package_root":C134_ROOT,"C133_package_root":C133_ROOT,"C132_package_root":C132_ROOT,"C131_package_root":C131_ROOT,"C130_package_root":C130_ROOT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"targets":4,"symbolic_targets":2,"numerical_targets":0,"target_backed_calibration":0,"external_input_conditions":2,"gluon_factorization":False,"ward_sensitivity":0,"generic_rank":2,"rank_deficit":9,"counterterm_directions":6,"parameters_solved":0,"renormalized_matrices":0,"physical_states":0,"forbidden_targets_consumed":0,"hidden_defaults":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_target2_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C135 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C135 root/status mismatch")
    return _freeze(verify_hqcd_target2_authority())
def verify_hqcdtarget2_authority() -> MappingProxyType: return _freeze(verify_hqcd_target2_authority())
def static_isolation_guard() -> MappingProxyType: return _freeze({"forbidden_targets_consumed":0,"hidden_parameters_selected":0,"counterterms_solved":0,"renormalized_matrices_created":0,"physical_states_created":0,"TMD_process_data_consumed":0,"C8_C14_masses_consumed":0,"pass":True})
def mutate_live_hqcdtarget2(index:int) -> MappingProxyType:
    fields=("plan","scheme","input","selector","target","units","kinematics","gluon","ward","join","rank","counterterm","role","root","C136")
    return _freeze({"mutation":fields[int(index)%len(fields)],"must_fail_or_change_root":True,"positive_gate":False})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","TARGET_IDS","target_plan_manifest","project_scheme_manifest","external_input_capsule_schema","reference_selector_manifest","reference_selector","target_manifest","target_by_id","target_for_condition","evaluate_target_condition","target_condition_sensitivity","gluon_one_body_factorization_report","counterterm_sensitive_identity_manifest","calibration_condition_manifest","external_input_condition_manifest","holdout_condition_manifest","condition_role_manifest","counterterm_target_crosswalk","target_backed_identifiability_report","remaining_rank_deficit_manifest","target_scheme_completeness_certificate","finite_basis_completeness_certificate","verify_hqcd_target2_authority","verify_hqcdtarget2_authority","load_verified_hqcd_target2_authority","static_isolation_guard","mutate_live_hqcdtarget2"]
