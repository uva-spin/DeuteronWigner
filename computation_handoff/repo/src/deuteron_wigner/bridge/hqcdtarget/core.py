"""C134/HQCDTARGET target-capsule and adapter audit.

All four C133 requests remain unavailable: methodological sources do not
provide regulator-identical finite-basis targets or proved conversions.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c134_hqcdtarget"
BASELINE="e0b2c8f93306b3129dc29dc66a3c64e2d21c65f8"; CONTRACT="docs/next_level/c133_c134_hqcdtarget_import_contract.json"
STATUS="C134_HQCDTARGET_SOURCE_TARGET_INCOMPLETE"; NEXT="C135/HQCDTARGET2"; SCHEMA="C134-HQCDTARGET-V1"
C133_ROOT="c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9"; C132_ROOT="192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"; C131_ROOT="67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"; C130_ROOT="d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"; C129_ROOT="4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"; C128_ROOT="d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"; C127_ROOT="0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"; C126_ROOT="84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"; C125_ROOT="a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
TARGETS=("DRESSED_QUARK_FINITE_LIGHT_FRONT" "FINITE_BASIS_QQG_VERTEX" "ONE_BODY_GLUON_SELF_ENERGY" "COUNTERTERM_SENSITIVE_WARD_CURRENT")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType):return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,dict):return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [_plain(v) for v in x]
    if isinstance(x,np.ndarray):return x.tolist()
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,dict):return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)):return tuple(_freeze(v) for v in x)
    if isinstance(x,np.ndarray):y=np.array(x,copy=True);y.setflags(write=False);return y
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def _check_target(t:str)->None:
    if t not in TARGETS:raise KeyError(t)
def _check_condition(c:str)->None:
    if c not in TARGETS:raise KeyError(c)

def target_source_manifest()->MappingProxyType:
    rows=({"source_id":"C133_PRIMARY_METHOD_AUTHORITY","version":"locked C133 inventory","sha256":"c63145b47c166736367384ea2afe62ca123046147b43d3db2ac2d77338eacc9d","tier":"TIER_4_METHODOLOGICAL_ONLY","usable_target":False},)
    return _freeze({"schema":"C134-TARGET-SOURCE-V1","sources":rows,"primary_sources":1,"usable_tier_1_to_3":0,"root":_root(rows)})
def target_manifest()->MappingProxyType:
    rows=tuple({"target_id":t,"condition_id":t,"target_class":"TARGET_AUTHORITY_UNAVAILABLE","source_tier":"TIER_4_METHOD_ONLY","source_file":None,"source_sha256":None,"locator":None,"state":"open color-triplet q+qg probe","kinematics":None,"resolution":("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50"),"scheme":None,"scale":None,"gauge":None,"regulator":"finite light-front HO target required","target":None,"units":None,"uncertainty":None,"finite_basis_adapter":"ADAPTER_UNAVAILABLE","counterterm_sensitivity":(),"first_omitted_effects":"Fock/zero-mode/basis truncation","calibration":False,"holdout":False,"root":_root((t,"unavailable"))} for t in TARGETS)
    return _freeze({"schema":"C134-TARGET-MANIFEST-V1","targets":rows,"count":len(rows),"target_backed_calibration":0,"root":_root(rows)})
def target_by_id(target_id:str)->MappingProxyType:
    _check_target(target_id)
    return next(x for x in target_manifest()["targets"] if x["target_id"]==target_id)
def target_for_condition(condition_id:str)->MappingProxyType:return target_by_id(condition_id)
def target_value_semantics(target_id:str)->MappingProxyType:
    t=target_by_id(target_id);return _freeze({"schema":"C134-TARGET-VALUE-V1","target_id":target_id,"class":t["target_class"],"value":None,"symbol":None,"numerical_default":False,"root":_root((target_id,"unavailable"))})
def scheme_adapter_manifest()->MappingProxyType:return _freeze({"schema":"C134-ADAPTER-MANIFEST-V1","adapters":tuple({"adapter_id":t,"status":"TARGET_ADAPTER_INCOMPLETE","source_scheme":None,"target_scheme":"C133 finite-basis scheme","round_trip":False,"remainder":None} for t in TARGETS),"unproved_numerical_adapters":4,"root":_root(TARGETS)})
def scheme_adapter(adapter_id:str)->MappingProxyType:
    _check_target(adapter_id);return next(x for x in scheme_adapter_manifest()["adapters"] if x["adapter_id"]==adapter_id)
def evaluate_target_condition(condition_id:str,resolution:str,*,parameter_point:dict|None=None,external_inputs:dict|None=None)->MappingProxyType:
    _check_condition(condition_id)
    return _freeze({"schema":"C134-JOINED-EVALUATOR-V1","condition_id":condition_id,"resolution":resolution,"target":None,"status":"TARGET_AUTHORITY_UNAVAILABLE","route_T_A_T_B_mismatch":0,"parameter_point_used":parameter_point is not None,"external_inputs_used":external_inputs is not None,"root":_root((condition_id,resolution,"unavailable"))})
def target_condition_sensitivity(condition_id:str,resolution:str,parameter_id:str,*,diagnostic_point:dict|None=None)->MappingProxyType:
    _check_condition(condition_id);return _freeze({"schema":"C134-TARGET-SENSITIVITY-V1","condition_id":condition_id,"resolution":resolution,"parameter_id":parameter_id,"value":0,"status":"TARGET_UNAVAILABLE","root":_root((condition_id,resolution,parameter_id,"unavailable"))})
def calibration_condition_manifest()->MappingProxyType:return _freeze({"schema":"C134-CALIBRATION-V1","conditions":(),"count":0,"root":_root(("empty",))})
def external_input_condition_manifest()->MappingProxyType:return _freeze({"schema":"C134-EXTERNAL-INPUT-V1","conditions":(),"count":0,"hidden_defaults":0,"root":_root(("empty",))})
def holdout_condition_manifest()->MappingProxyType:return _freeze({"schema":"C134-HOLDOUT-V1","conditions":TARGETS,"count":4,"promoted":0,"root":_root((TARGETS,"holdout"))})
def counterterm_target_crosswalk()->MappingProxyType:return _freeze({"schema":"C134-COUNTERTERM-CROSSWALK-V1","directions":tuple({"id":x,"target_conditions":(),"status":"NO_SOURCE_QUALIFIED_TARGET","zeroed":False} for x in ("mass","vacuum_energy","gluon_mass","sector","boundary","truncation")),"root":_root(("six-directions",))})
def target_backed_identifiability_report()->MappingProxyType:return _freeze({"schema":"C134-TARGET-RANK-V1","target_backed_conditions":0,"rank":0,"rank_deficit":11,"nullspace":("m_q","m_q^2","g_s","six_counterterms","vacuum","truncation"),"ridge":False,"pseudoinverse":False,"root":_root(("rank-zero",11))})
def remaining_rank_deficit_manifest()->MappingProxyType:return _freeze({"schema":"C134-RANK-DEFICIT-V1","rank_deficit":11,"missing_targets":TARGETS,"root":_root(("deficit",11))})
def target_authority_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C134-TARGET-COMPLETENESS-V1","target_backed_calibration":(),"symbolic_inputs":(),"identities":(),"strict_holdouts":TARGETS,"conversion_required":TARGETS,"finite_basis_adapter_required":TARGETS,"unavailable":TARGETS,"forbidden":(),"uncovered_directions":11,"numerical_solve_authorized":False,"symbolic_solve_authorized":False,"root":_root(("incomplete",TARGETS,11))})

ROOTS={"C134_TARGET_SOURCE_ROOT":_root(target_source_manifest()),"C134_TARGET_CAPSULE_ROOT":_root(target_manifest()),"C134_SCHEME_ADAPTER_ROOT":_root(scheme_adapter_manifest()),"C134_TARGET_CONDITION_JOIN_ROOT":_root(tuple(evaluate_target_condition(t,"K9_2_N8_b0.40") for t in TARGETS)),"C134_TARGET_BACKED_IDENTIFIABILITY_ROOT":_root(target_backed_identifiability_report()),"C134_CONDITION_ROLE_ROOT":_root((calibration_condition_manifest(),holdout_condition_manifest())),"C134_COUNTERTERM_COVERAGE_ROOT":_root(counterterm_target_crosswalk()),"C134_TARGET_COMPLETENESS_ROOT":_root(target_authority_completeness_certificate())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"C133":C133_ROOT,"C132":C132_ROOT})
def verify_hqcd_target_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"blocker":STATUS,"baseline":BASELINE,"contract":CONTRACT,"C133_package_root":C133_ROOT,"C132_package_root":C132_ROOT,"C131_package_root":C131_ROOT,"C130_package_root":C130_ROOT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"targets":4,"target_backed_calibration":0,"sources_usable":0,"adapters_complete":0,"joined_routes_mismatches":0,"rank":0,"rank_deficit":11,"counterterm_directions":6,"parameters_solved":0,"renormalized_matrices":0,"forbidden_targets_consumed":0,"hidden_defaults":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_target_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C134 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C134 root/status mismatch")
    return _freeze(verify_hqcd_target_authority())
def mutate_live_hqcdtarget(index:int)->MappingProxyType:
    fields=("source","version","hash","target","units","scheme","adapter","kinematics","triplet","sensitivity","role","rank","root","C135")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})
def static_isolation_guard()->MappingProxyType:return _freeze({"forbidden_targets":("TMD","ART25","effective-model","proton","deuteron"),"hidden_parameters":0,"counterterms_solved":0,"renormalized_matrices":0,"physical_states":0,"pass":True})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","TARGETS","target_source_manifest","target_manifest","target_by_id","target_for_condition","target_value_semantics","scheme_adapter_manifest","scheme_adapter","evaluate_target_condition","target_condition_sensitivity","calibration_condition_manifest","external_input_condition_manifest","holdout_condition_manifest","counterterm_target_crosswalk","target_backed_identifiability_report","remaining_rank_deficit_manifest","target_authority_completeness_certificate","verify_hqcd_target_authority","load_verified_hqcd_target_authority","mutate_live_hqcdtarget","static_isolation_guard"]
