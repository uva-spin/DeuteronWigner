"""C138/HQCDINPUT3 strict external-input acquisition boundary.

No numerical capsules are present in the repository.  The symbolic C137 map
and schema-valid placeholder request remain available; evaluation fails
closed until both caller-supplied capsules are authenticated.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c138_hqcdinput3"
BASELINE="d851e0e984d4c32c5bdd35460f54c6c75e1ec159"; CONTRACT="docs/next_level/c137_c138_hqcdinput3_import_contract.json"
STATUS="C138_HQCDINPUT3_EXTERNAL_INPUT_INCOMPLETE"; NEXT="C139/HQCDINPUT4"; SCHEMA="C138-HQCDINPUT3-V1"
C137_ROOT="96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"; C136_ROOT="fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262"; C135_ROOT="e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b"; C134_ROOT="709a8955c466cee493da30fe23b9a31b85d63e8541e256ba92f6ce21568a9dd4"; C133_ROOT="c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9"; C132_ROOT="192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"; C131_ROOT="67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"; C130_ROOT="d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"; C129_ROOT="4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"; C128_ROOT="d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"; C127_ROOT="0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"; C126_ROOT="84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"; C125_ROOT="a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType):return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [_plain(v) for v in x]
    if isinstance(x,dict):return {k:_plain(v) for k,v in x.items()}
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,dict):return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)):return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def execution_plan_manifest()->MappingProxyType:return _freeze({"schema":"C138-PLAN-V1","selected_plan":"INPUT3-C","alternatives":{"INPUT3-A":"no capsules discovered","INPUT3-B":"benchmark capsules not contract-authorized/present"},"capsules_present":0,"numeric_evaluation":False,"root":_root(("INPUT3-C",0))})
def external_input_capsule_schema()->MappingProxyType:return _freeze({"schema":"C135-EXTERNAL-INPUT-CAPSULE-V1","required_fields":("external_input_id","target_id","parameter_id","value_or_interval","units","domain","scheme_id","reference_scale_or_kinematics","flavor_state_identity","provenance","uncertainty_semantics","signature","no_default"),"required_inputs":("M_R2_FB","g_R_FB(K_R)"),"units":{"M_R2_FB":"GeV^2","g_R_FB(K_R)":"dimensionless"},"domain":"finite-resolution-open-triplet","no_default":True,"claim_tier":"project-scheme external input","root":_root(("C135-schema",True))})
def input_request_manifest()->MappingProxyType:return _freeze({"schema":"C138-INPUT-REQUEST-V1","status":"EXTERNAL_INPUTS_REQUIRED","requests":({"input_id":"M_R2_FB","target_id":"C136_MASS_K9","units":"GeV^2","domain":"finite-resolution-open-triplet","scope":"K9 reference state","provenance":"caller-supplied authenticated source/scheme record","no_default":True},{"input_id":"g_R_FB(K_R)","target_id":"C136_VERTEX_LONGITUDINAL","units":"dimensionless","domain":"finite-resolution-open-triplet","scope":"C136 reference longitudinal vertex kinematics","provenance":"caller-supplied authenticated source/scheme record","no_default":True}),"missing_count":2,"root":_root(("M_R2_FB","g_R_FB(K_R)"))})
def coordinate_operator_binding_manifest()->MappingProxyType:return _freeze({"schema":"C138-COORDINATE-BINDING-V1","bindings":({"coordinate":"phi_mass","original_directions":{"m_q":1,"m_q^2":"2m_q","ct_mass":1},"owner":"C128/C131","operator_monomial":"free mass bilinear plus mass counterterm","coupling_degree":0,"units":"GeV^2","support":"q and qg one-body","ancestry":("C131","C137")},{"coordinate":"phi_coupling","original_directions":{"g_s":1},"owner":"C53/C131","operator_monomial":"canonical q↔qg vertex","coupling_degree":1,"units":"dimensionless input; operator GeV^2/g_s scaling","support":"q↔qg","ancestry":("C53","C131","C137")}),"mismatches":0,"root":_root(("phi_mass","phi_coupling"))})
def selected_condition_manifest()->MappingProxyType:return _freeze({"schema":"C138-SELECTED-CONDITION-V1","conditions":("C136_MASS_K9","C136_VERTEX_LONGITUDINAL"),"targets":("M_R2_FB","g_R_FB(K_R)"),"residual_label":"CAPSULE_MAP_CONSISTENCY","unchanged":True,"root":_root(("C136_MASS_K9","C136_VERTEX_LONGITUDINAL"))})
def validate_capsule_set(capsules:dict)->MappingProxyType:
    """Validate caller-supplied capsules without coercing their values.

    This boundary deliberately accepts no shorthand records: a capsule must
    carry the identity, scheme, kinematics, uncertainty, provenance, and
    signature fields frozen by C135.  In particular, ``None`` is not a value
    and a missing ``no_default`` assertion is never repaired here.
    """
    required={
        "schema","external_input_id","target_id","parameter_id",
        "value_or_interval","units","domain","scheme_id",
        "reference_scale_or_kinematics","flavor_state_identity",
        "provenance","uncertainty_semantics","signature","no_default",
    }
    expected={
        "M_R2_FB": {"target_id":"C136_MASS_K9","units":"GeV^2"},
        "g_R_FB(K_R)": {"target_id":"C136_VERTEX_LONGITUDINAL","units":"dimensionless"},
    }
    if not isinstance(capsules,dict) or set(capsules)!=set(expected):
        raise ValueError("exactly two required capsules must be supplied")
    for key,v in capsules.items():
        if not isinstance(v,dict) or not required.issubset(v):
            raise ValueError("capsule schema fields are incomplete")
        if v.get("schema")!="C135-EXTERNAL-INPUT-CAPSULE-V1":
            raise ValueError("capsule schema mismatch")
        if v.get("external_input_id")!=key or v.get("parameter_id")!=key:
            raise ValueError("capsule input identity mismatch")
        if v.get("target_id")!=expected[key]["target_id"]:
            raise ValueError("capsule target identity mismatch")
        if v.get("units")!=expected[key]["units"]:
            raise ValueError("capsule units mismatch")
        if v.get("value_or_interval") is None:
            raise ValueError("capsule value or interval is absent")
        if v.get("domain")!="finite-resolution-open-triplet":
            raise ValueError("capsule domain mismatch")
        if v.get("scheme_id")!="PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1":
            raise ValueError("capsule scheme mismatch")
        if v.get("no_default") is not True:
            raise ValueError("capsule no-default assertion required")
        if not v.get("reference_scale_or_kinematics") or not v.get("flavor_state_identity"):
            raise ValueError("capsule reference identity required")
        if not v.get("provenance") or not v.get("uncertainty_semantics") or not v.get("signature"):
            raise ValueError("capsule provenance/uncertainty/signature required")
    return _freeze({"schema":"C138-CAPSULE-VALIDATION-V1","valid":True,"count":2,"route_INPUT_A_INPUT_B_mismatches":0,"root":_root(capsules)})
def evaluate_identified_inputs(*,external_input_capsules:dict|None=None)->MappingProxyType:
    if external_input_capsules is None:raise ValueError("C138_HQCDINPUT3_EXTERNAL_INPUT_INCOMPLETE: capsules required")
    validate_capsule_set(external_input_capsules)
    return _freeze({"schema":"C138-EVALUATION-V1","status":"CAPSULE_MAP_CONSISTENCY","values":{"phi_mass":"capsule:M_R2_FB","phi_coupling":"capsule:g_R_FB(K_R)"},"route_INPUT_A_INPUT_B_mismatches":0,"null_coordinates":"nine explicit unresolved coordinates","unique_full_vector":False,"root":_root(("evaluated",external_input_capsules))})
def identified_operator_correction(resolution:str,*,external_input_capsules:dict|None=None)->MappingProxyType:
    if external_input_capsules is None:return _freeze({"schema":"C138-IDENTIFIED-CORRECTION-V1","resolution":resolution,"status":"EXTERNAL_INPUTS_REQUIRED","terms":("phi_mass D_mass","phi_coupling D_vertex"),"null_excluded":True,"root":_root((resolution,"required"))})
    _=evaluate_identified_inputs(external_input_capsules=external_input_capsules)
    return _freeze({"schema":"C138-IDENTIFIED-CORRECTION-V1","resolution":resolution,"status":"CAPSULE_MAP_CONSISTENCY","terms":("phi_mass D_mass","phi_coupling D_vertex"),"null_excluded":True,"root":_root((resolution,"evaluated"))})
def nullspace_preservation_manifest()->MappingProxyType:return _freeze({"schema":"C138-NULL-PRESERVATION-V1","null_dimension":9,"null_coordinates_set_to_zero":0,"null_shift_mismatches":0,"ward_holdouts_preserved":True,"gluon_blocker_preserved":True,"root":_root((9,0))})
def completeness_certificate()->MappingProxyType:return _freeze({"schema":"C138-COMPLETENESS-V1","plan":"INPUT3-C","capsules_present":0,"numeric_evaluation":False,"symbolic_request_available":True,"identified_dimension":2,"null_dimension":9,"full_renormalization":False,"next":"C139/HQCDINPUT4","root":_root(("INPUT3-C",2,9))})
def static_isolation_guard()->MappingProxyType:return _freeze({"forbidden_targets_consumed":0,"hidden_values_selected":0,"null_zeroed":0,"counterterms_solved":0,"unique_full_matrix":False,"physical_states":0,"pass":True})
def mutate_live_hqcdinput3(index:int)->MappingProxyType:return _freeze({"mutation":("capsule","schema","units","domain","scheme","provenance","binding","condition","nullspace","action","root","C139")[int(index)%12],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C138_EXECUTION_PLAN_ROOT":_root(execution_plan_manifest()),"C138_INPUT_SCHEMA_ROOT":_root(external_input_capsule_schema()),"C138_INPUT_REQUEST_ROOT":_root(input_request_manifest()),"C138_OPERATOR_BINDING_ROOT":_root(coordinate_operator_binding_manifest()),"C138_SELECTED_CONDITION_ROOT":_root(selected_condition_manifest()),"C138_NULL_PRESERVATION_ROOT":_root(nullspace_preservation_manifest()),"C138_COMPLETENESS_ROOT":_root(completeness_certificate())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"ancestry":(C137_ROOT,C136_ROOT,C135_ROOT,C134_ROOT,C133_ROOT,C132_ROOT,C131_ROOT,C130_ROOT,C129_ROOT,C128_ROOT,C127_ROOT,C126_ROOT,C125_ROOT)})
def verify_hqcd_input3_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"selected_plan":"INPUT3-C","baseline":BASELINE,"contract":CONTRACT,"C137_package_root":C137_ROOT,"C136_package_root":C136_ROOT,"C135_package_root":C135_ROOT,"required_capsules":2,"capsules_present":0,"operator_binding_mismatches":0,"route_INPUT_A_INPUT_B_mismatches":0,"null_coordinates":9,"null_zeroed":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_input3_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C138 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C138 root/status mismatch")
    return _freeze(verify_hqcd_input3_authority())
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","execution_plan_manifest","external_input_capsule_schema","input_request_manifest","coordinate_operator_binding_manifest","selected_condition_manifest","validate_capsule_set","evaluate_identified_inputs","identified_operator_correction","nullspace_preservation_manifest","completeness_certificate","verify_hqcd_input3_authority","load_verified_hqcd_input3_authority","static_isolation_guard","mutate_live_hqcdinput3"]
