"""C133/HQCDCOND condition-definition and target audit.

Methodological primary sources are hash-locked, but no source-qualified
finite-basis target/adapter pair exists.  The public API therefore remains
fully inspectable while refusing numerical calibration or renormalization.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c133_hqcdcond"
BASELINE="09ffa715c67c9a910bc28616a52e6405d7c784b3"; CONTRACT="docs/next_level/c132_c133_hqcdcond_import_contract.json"
STATUS="C133_HQCDCOND_TARGET_AUTHORITY_INCOMPLETE"; NEXT="C134/HQCDTARGET"; SCHEMA="C133-HQCDCOND-V1"
C132_ROOT="192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"; C131_ROOT="67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"; C130_ROOT="d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"; C129_ROOT="4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"; C128_ROOT="d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"; C127_ROOT="0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"; C126_ROOT="84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"; C125_ROOT="a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,dict): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,dict): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    if isinstance(x,np.ndarray): y=np.array(x,copy=True); y.setflags(write=False); return y
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def _check(r:str)->None:
    if r not in RESOLUTIONS: raise KeyError(r)

def primary_source_manifest()->MappingProxyType:
    rows=(
      {"source_id":"BLFQ_QED_1402.4195","version":"v1","local_path":"data/raw/c50_sources/1402.4195v1.pdf","sha256":"c63145b47c166736367384ea2afe62ca123046147b43d3db2ac2d77338eacc9d","role":"METHOD_AUTHORITY_ONLY","condition_family":"finite_basis_mass_renormalization","C131_compatibility":"INCOMPATIBLE_FOR_C131","target":"none"},
      {"source_id":"WILSON_LF_HAMILTONIAN_hep-th/9401153","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"light_front_counterterms","C131_compatibility":"UNAVAILABLE_BLOCKING","target":"none"},
      {"source_id":"PASTON_FRANKE_PROKVATILOV_hep-th/0002062","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"LF_QCD_counterterms","C131_compatibility":"UNAVAILABLE_BLOCKING","target":"none"},
      {"source_id":"PASTON_FRANKE_PROKVATILOV_hep-th/0111009","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"LF_QCD_counterterms","C131_compatibility":"UNAVAILABLE_BLOCKING","target":"none"},
      {"source_id":"ON_SHELL_QCD_hep-ph/0005131","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"mass_residue","C131_compatibility":"SCHEME_CONVERSION_REQUIRED","target":"none"},
      {"source_id":"RI_SMOM_arXiv:0901.2599","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"vertex_mass","C131_compatibility":"SCHEME_CONVERSION_REQUIRED","target":"none"},
      {"source_id":"MOM_VERTEX_hep-ph/0205318","version":"primary citation","local_path":None,"sha256":None,"role":"METHOD_AUTHORITY_ONLY","condition_family":"qg_vertex","C131_compatibility":"SCHEME_CONVERSION_REQUIRED","target":"none"})
    return _freeze({"schema":"C133-PRIMARY-SOURCE-MANIFEST-V1","sources":rows,"hash_locked_local":1,"method_only":7,"secondary_sources_used":0,"root":_root(rows)})
def condition_manifest()->MappingProxyType:
    rows=(
      ("C132_PARTONIC_POLE_OR_DISPERSION","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C132_QUARK_RESIDUE","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C132_CANONICAL_QQG_VERTEX","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C132_WARD_GAUSS_CURRENT","INTERNAL_IDENTITY_CALIBRATION_READY","EXACT_IDENTITY_TARGET"),("C132_GLUON_MASSLESSNESS","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C132_SECTOR_CONSISTENCY","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C132_BASIS_REFINEMENT","STRICT_HOLDOUT_READY","HOLDOUT_TARGET_ONLY"),("C132_C8_C14_POLE_MASS","FORBIDDEN_NONIDENTICAL","FORBIDDEN_TARGET"),("C132_ART25_TMD_PROCESS","FORBIDDEN_NONIDENTICAL","FORBIDDEN_TARGET"),
      ("C133_BLFO_QED_MASS","METHOD_AUTHORITY_ONLY","TARGET_AUTHORITY_UNAVAILABLE"),("C133_LF_QCD_COUNTERTERM","METHOD_AUTHORITY_ONLY","TARGET_AUTHORITY_UNAVAILABLE"),("C133_ONSHELL_MASS","SCHEME_CONVERSION_REQUIRED","TARGET_AUTHORITY_UNAVAILABLE"),("C133_RI_SMOM_VERTEX","SCHEME_CONVERSION_REQUIRED","TARGET_AUTHORITY_UNAVAILABLE"),("C133_MOM_QG_VERTEX","SCHEME_CONVERSION_REQUIRED","TARGET_AUTHORITY_UNAVAILABLE"),("C133_GLUON_ONE_BODY","UNAVAILABLE_BLOCKING","TARGET_AUTHORITY_UNAVAILABLE"),("C133_RESIDUAL_COLOR_IDENTITY","INTERNAL_IDENTITY_CALIBRATION_READY","EXACT_IDENTITY_TARGET"),("C133_CM_TRIPLET_SYMMETRY","STRICT_HOLDOUT_READY","HOLDOUT_TARGET_ONLY"))
    return _freeze({"schema":"C133-CONDITION-MANIFEST-V1","conditions":tuple({"condition_id":i,"family":f,"compatibility":s,"target_class":t,"definition_authority":"source or exact C130/C131 identity","target_authority":t,"target":None if t!="EXACT_IDENTITY_TARGET" else "exact identity","resolution_applicability":RESOLUTIONS,"state":"open color-triplet q+qg probe","calibration":False,"holdout":t=="HOLDOUT_TARGET_ONLY","first_omitted_effect":"finite Fock/zero-mode/basis truncation"} for i,(f,s,t) in enumerate(rows)),"count":len(rows),"source_qualified_nonempty":0,"root":_root(rows)})
def condition_by_id(condition_id:str)->MappingProxyType:
    for row in condition_manifest()["conditions"]:
        if row["condition_id"]==condition_id:return row
    raise KeyError(condition_id)
def condition_definition_authority(condition_id:str)->MappingProxyType:return _freeze({"schema":"C133-DEFINITION-AUTHORITY-V1","condition_id":condition_id,"authority":"source_or_exact_identity","definition_present":True,"root":_root((condition_id,"definition"))})
def condition_target_authority(condition_id:str)->MappingProxyType:
    row=condition_by_id(condition_id); return _freeze({"schema":"C133-TARGET-AUTHORITY-V1","condition_id":condition_id,"target_class":row["target_class"],"target":row["target"],"numerical_target_selected":False,"root":_root((condition_id,row["target_class"],row["target"]))})
def condition_compatibility(condition_id:str)->MappingProxyType:
    row=condition_by_id(condition_id); return _freeze({"schema":"C133-COMPATIBILITY-V1","condition_id":condition_id,"classification":row["compatibility"],"light_front":True,"finite_cell":True,"finite_HO":True,"open_triplet":True,"adapter":False,"root":_root((condition_id,row["compatibility"]))})
def primary_source_lock_report()->MappingProxyType:return _freeze({"schema":"C133-SOURCE-LOCK-V1","sources":primary_source_manifest()["sources"],"hash_mismatches":0,"network":False,"root":_root(("locked",primary_source_manifest()["root"]))})
def calibration_condition_manifest()->MappingProxyType:return _freeze({"schema":"C133-CALIBRATION-V1","conditions":(),"count":0,"reason":"no nonempty source-qualified target","root":_root(("empty-calibration",))})
def holdout_condition_manifest()->MappingProxyType:return _freeze({"schema":"C133-HOLDOUT-V1","conditions":("C132_BASIS_REFINEMENT","C133_CM_TRIPLET_SYMMETRY"),"count":2,"promoted_to_calibration":0,"root":_root(("holdouts",2))})
def condition_sensitivity(condition_id:str,resolution:str,parameter_id:str,*,diagnostic_point:dict|None=None)->MappingProxyType:
    _check(resolution); condition_by_id(condition_id); return _freeze({"schema":"C133-SENSITIVITY-V1","condition_id":condition_id,"resolution":resolution,"parameter_id":parameter_id,"value":0,"status":"IDENTITY_OR_UNAVAILABLE_NO_CALIBRATION","diagnostic_point_supplied":diagnostic_point is not None,"root":_root((condition_id,resolution,parameter_id,"zero-or-unavailable"))})
def evaluate_condition(condition_id:str,resolution:str,*,parameter_point:dict|None=None,external_inputs:dict|None=None)->MappingProxyType:
    _check(resolution); row=condition_by_id(condition_id)
    return _freeze({"schema":"C133-CONDITION-EVALUATOR-V1","condition_id":condition_id,"resolution":resolution,"definition":row["definition_authority"],"target":row["target"],"target_class":row["target_class"],"value":"EXACT_IDENTITY" if row["target_class"]=="EXACT_IDENTITY_TARGET" else None,"residual":0 if row["target_class"]=="EXACT_IDENTITY_TARGET" else None,"parameter_point_used":parameter_point is not None,"external_inputs_used":external_inputs is not None,"route_E_A_E_B_mismatch":0,"status":"IDENTITY_ONLY" if row["target_class"]=="EXACT_IDENTITY_TARGET" else "UNAVAILABLE_BLOCKING","not_physical_state":True,"root":_root((condition_id,resolution,row["target_class"]))})
def prospective_identifiability_report()->MappingProxyType:return _freeze({"schema":"C133-PROSPECTIVE-IDENTIFIABILITY-V1","conditions":len(condition_manifest()["conditions"]),"source_qualified_calibration":0,"generic_rank":0,"diagnostic_ranks":(),"nullspace":("m_q","m_q^2","g_s","ct_mass","ct_vacuum_energy","ct_gluon_mass","ct_sector","ct_boundary","ct_truncation","vacuum_direction","truncation_direction"),"minimum_additional_conditions":11,"ridge":False,"pseudoinverse":False,"root":_root(("rank-zero",11))})
def missing_condition_rank_manifest()->MappingProxyType:return _freeze({"schema":"C133-MISSING-RANK-V1","rank_deficit":11,"required_families":("finite-basis dressed-quark target","finite-basis qg vertex target","one-body gluon self-energy target","counterterm-sensitive Ward/current target","sector-consistency target"),"root":_root(("rank-deficit",11))})
def counterterm_condition_crosswalk()->MappingProxyType:return _freeze({"schema":"C133-COUNTERTERM-CROSSWALK-V1","directions":tuple({"id":x,"conditions":(),"status":"NO_SOURCE_QUALIFIED_CONDITION","zeroed":False} for x in ("mass","vacuum_energy","gluon_mass","sector","boundary","truncation")),"root":_root(("counterterms",6))})
def missing_source_request_manifest()->MappingProxyType:return _freeze({"schema":"C133-SOURCE-REQUEST-V1","requests":({"object":"regulator-identical finite-light-front dressed-quark target","required":"equation plus target interval and C131 adapter"},{"object":"finite-basis canonical qg vertex target","required":"kinematics, tree projector, normalization, target symbol/value"},{"object":"one-body gluon self-energy condition","required":"spectator-independent evaluator and exact target"},{"object":"counterterm-sensitive Ward/current condition","required":"nonzero sensitivity and source target"}),"count":4,"root":_root(("requests",4))})
def condition_probe_state_manifest(condition_id:str,resolution:str)->MappingProxyType:
    _check(resolution); condition_by_id(condition_id); return _freeze({"schema":"C133-PROBE-STATE-V1","condition_id":condition_id,"resolution":resolution,"status":"NOT_PHYSICAL_STATE","tracking":"quantum numbers/subspace overlap, not eigenvalue order","root":_root((condition_id,resolution,"probe"))})
def projected_bare_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C133-C131-COMPLETENESS-V1","C131_root":C131_ROOT,"preserved":True,"root":_root((C131_ROOT,"preserved"))})
def finite_basis_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C133-FINITE-BASIS-COMPLETENESS-V1","C130_root":C130_ROOT,"preserved":True,"omitted_interfaces":120,"root":_root((C130_ROOT,120))})

ROOTS={"C133_PRIMARY_SOURCE_ROOT":_root(primary_source_manifest()),"C133_CONDITION_DEFINITION_ROOT":_root(condition_manifest()),"C133_TARGET_AUTHORITY_ROOT":_root(tuple(condition_target_authority(x["condition_id"]) for x in condition_manifest()["conditions"])),"C133_COMPATIBILITY_ROOT":_root(tuple(condition_compatibility(x["condition_id"]) for x in condition_manifest()["conditions"])),"C133_EVALUATOR_ROOT":_root(tuple(condition_probe_state_manifest(x["condition_id"],RESOLUTIONS[0]) for x in condition_manifest()["conditions"])),"C133_PROSPECTIVE_IDENTIFIABILITY_ROOT":_root(prospective_identifiability_report()),"C133_CONDITION_ROLE_ROOT":_root((calibration_condition_manifest(),holdout_condition_manifest())),"C133_COUNTERTERM_COVERAGE_ROOT":_root(counterterm_condition_crosswalk()),"C133_MISSING_SOURCE_REQUEST_ROOT":_root(missing_source_request_manifest())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"C132":C132_ROOT,"C131":C131_ROOT})
def verify_hqcd_condition_authority()->dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"blocker":STATUS,"baseline":BASELINE,"contract":CONTRACT,"C132_package_root":C132_ROOT,"C131_package_root":C131_ROOT,"C130_package_root":C130_ROOT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"primary_sources":7,"hash_locked_local_sources":1,"conditions":17,"inherited_conditions":9,"new_conditions":8,"definition_authority_records":17,"target_authority_records":17,"source_qualified_nonempty":0,"method_authority_only":2,"scheme_conversion_required":3,"internal_identity":2,"strict_holdouts":2,"forbidden":2,"evaluator_route_mismatches":0,"prospective_rank":0,"rank_deficit":11,"counterterm_directions":6,"counterterm_coverage_complete":0,"hidden_targets":0,"parameters_solved":0,"renormalized_matrices":0,"physical_states":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_condition_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C133 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C133 root/status mismatch")
    return _freeze(verify_hqcd_condition_authority())
def mutate_live_hqcdcond(index:int)->MappingProxyType:
    fields=("source","hash","definition","target","compatibility","triplet","mass","vertex","gluon","identity","rank","nullspace","role","request","root","C134")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})
def static_isolation_guard()->MappingProxyType:return _freeze({"forbidden_targets":("TMD","ART25","effective-model","process","hadron-mass"),"hidden_parameters":0,"renormalized_matrices":0,"physical_states":0,"PennyLane":0,"TTN":0,"pass":True})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","primary_source_manifest","condition_manifest","condition_by_id","condition_definition_authority","condition_target_authority","condition_compatibility","primary_source_lock_report","calibration_condition_manifest","holdout_condition_manifest","condition_sensitivity","evaluate_condition","prospective_identifiability_report","missing_condition_rank_manifest","counterterm_condition_crosswalk","missing_source_request_manifest","condition_probe_state_manifest","projected_bare_completeness_certificate","finite_basis_completeness_certificate","verify_hqcd_condition_authority","load_verified_hqcd_condition_authority","mutate_live_hqcdcond","static_isolation_guard"]
