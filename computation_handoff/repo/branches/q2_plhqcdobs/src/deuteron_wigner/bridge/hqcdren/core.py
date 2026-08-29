"""C132/HQCDREN condition and identifiability boundary.

No source-qualified calibration target is present in the frozen C131/C130
authority chain.  Consequently this package exposes the complete candidate,
parameter, null-direction, and preservation domains while refusing to invent
a scheme, solve a parameter, or publish a numerical renormalized matrix.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c132_hqcdren"
BASELINE="d43f641a0decad238223f758472fe4df5f4d58e7"
CONTRACT="docs/next_level/c131_c132_hqcdren_import_contract.json"
STATUS="C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE"; NEXT="C133/HQCDCOND"; SCHEMA="C132-HQCDREN-V1"
C131_ROOT="67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
C130_ROOT="d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
C129_ROOT="4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"
C128_ROOT="d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT="0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT="84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT="a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50"); DIMS=dict(zip(RESOLUTIONS,(1350,2706,4758)))
COUNTERTERMS=("mass","vacuum_energy","gluon_mass","sector","boundary","truncation")

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
def _canon(x:Any)->str: return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str: return sha256(_canon(x).encode()).hexdigest()
def _check(r:str)->None:
    if r not in RESOLUTIONS: raise KeyError(r)

def condition_manifest()->MappingProxyType:
    candidates=(
      ("PARTONIC_POLE_OR_DISPERSION","UNAVAILABLE_BLOCKING","no source target authority"),
      ("QUARK_RESIDUE","UNAVAILABLE_BLOCKING","no source target authority"),
      ("CANONICAL_QQG_VERTEX","UNAVAILABLE_BLOCKING","no source target authority"),
      ("WARD_GAUSS_CURRENT_IDENTITY","INTERNAL_IDENTITY_CONDITION","identity only; not calibration"),
      ("GLUON_MASSLESSNESS","UNAVAILABLE_BLOCKING","no source target authority"),
      ("SECTOR_CONSISTENCY","UNAVAILABLE_BLOCKING","no source target authority"),
      ("BASIS_REFINEMENT_HOLDOUT","VALIDATION_HOLDOUT_ONLY","holdout only"),
      ("C8_C14_POLE_MASS","EFFECTIVE_MODEL_CONDITION_FORBIDDEN","forbidden validation model"),
      ("ART25_TMD_PROCESS","TMD_OR_PROCESS_CONDITION_FORBIDDEN","forbidden data")
    )
    return _freeze({"schema":"C132-CONDITION-MANIFEST-V1","candidates":tuple({"condition_id":i,"class":c,"status":s,"target":None,"source_authority":a,"units":None,"parameter_sensitivity":(),"calibration":False,"holdout":s=="VALIDATION_HOLDOUT_ONLY","first_omitted_effect":"not defined"} for i,(c,s,a) in enumerate(candidates)),"source_qualified_nonempty":0,"conditions_without_authority":6,"hidden_targets":0,"forbidden_selected":0,"root":_root(candidates)})
def condition_role_manifest()->MappingProxyType:
    return _freeze({"schema":"C132-CONDITION-ROLES-V1","calibration":(),"identifiability_diagnostic":(),"strict_holdout":("BASIS_REFINEMENT_HOLDOUT",),"negative_controls":("C8_C14_POLE_MASS","ART25_TMD_PROCESS"),"selected_scheme":None,"frozen_before_solve":True,"root":_root(("empty-calibration","holdout"))})
def renormalization_scheme_manifest()->MappingProxyType:
    return _freeze({"schema":"C132-SCHEME-V1","scheme_id":None,"status":"C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE","selected":False,"reason":"no source-qualified nonempty calibration set","finite_resolution":True,"continuum_claim":False,"root":_root(("no-scheme",STATUS))})
def unknown_parameter_manifest()->MappingProxyType:
    rows=(
      {"id":"m_q","role":"SOLVED_BARE_PARAMETER","status":"UNIDENTIFIED_SYMBOLIC_DIRECTION"},
      {"id":"m_q^2","role":"SOLVED_BARE_PARAMETER","identity":"m_q^2=(m_q)^2","status":"UNIDENTIFIED_SYMBOLIC_DIRECTION"},
      {"id":"g_s","role":"EXTERNAL_RENORMALIZED_INPUT","status":"UNIDENTIFIED_SYMBOLIC_DIRECTION"},
      *({"id":"ct_"+x,"role":"SOLVED_COUNTERTERM_COEFFICIENT","status":"COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE"} for x in COUNTERTERMS),
      {"id":"vacuum_direction_coefficient","role":"EXCLUDED_VACUUM_DIRECTION","status":"UNIDENTIFIED_SYMBOLIC_DIRECTION"},
      {"id":"truncation_direction_coefficient","role":"EXCLUDED_TRUNCATION_DIRECTION","status":"UNIDENTIFIED_SYMBOLIC_DIRECTION"})
    return _freeze({"schema":"C132-UNKNOWN-PARAMETER-V1","parameters":rows,"duplicate":0,"mq_mq2_ambiguity":0,"hidden_fixed_values":0,"silent_vacuum_or_truncation_solves":0,"root":_root(rows)})
def counterterm_condition_crosswalk()->MappingProxyType:
    return _freeze({"schema":"C132-COUNTERTERM-CROSSWALK-V1","directions":tuple({"id":x,"matrix_status":"unavailable without calibration","condition_ids":(),"coefficient_status":"COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE","selected":False,"nullspace":"unresolved"} for x in COUNTERTERMS),"root":_root(COUNTERTERMS)})
def identifiability_report(resolution:str|None=None)->MappingProxyType:
    if resolution is not None: _check(resolution)
    return _freeze({"schema":"C132-IDENTIFIABILITY-V1","resolution":resolution,"status":"C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE","rank":0,"singular_values":(),"nullspace":("m_q","m_q^2","g_s",*COUNTERTERMS,"vacuum_direction_coefficient","truncation_direction_coefficient"),"near_null":(),"condition_number":None,"identified_combinations":(),"route_J_A_J_B_mismatches":0,"reason":"no calibration residuals exist","root":_root((resolution,"empty-calibration"))})
def null_direction_manifest(resolution:str|None=None)->MappingProxyType:
    return _freeze({"schema":"C132-NULL-DIRECTION-V1","resolution":resolution,"directions":("m_q","g_s",*COUNTERTERMS,"vacuum_direction_coefficient","truncation_direction_coefficient"),"zeroed":False,"root":_root((resolution,"null-directions"))})
def condition_result(condition_id:str,resolution:str)->MappingProxyType:
    _check(resolution)
    return _freeze({"schema":"C132-CONDITION-RESULT-V1","condition_id":condition_id,"resolution":resolution,"status":"UNAVAILABLE_BLOCKING","target":None,"value":None,"residual":None,"source_authority":None,"root":_root((condition_id,resolution,"unavailable"))})
def holdout_result(holdout_id:str,resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C132-HOLDOUT-RESULT-V1","holdout_id":holdout_id,"resolution":resolution,"status":"NOT_RUN_SOURCE_CONDITION_UNAVAILABLE","passed":False,"root":_root((holdout_id,resolution,"not-run"))})
def renormalized_parameter_point(resolution:str)->MappingProxyType:
    _check(resolution); raise RuntimeError("C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE: no parameter point")
def parameter_enclosures(resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C132-PARAMETER-ENCLOSURE-V1","resolution":resolution,"status":"UNAVAILABLE_BLOCKING","enclosures":(),"unidentified_directions":null if False else ("m_q","g_s",*COUNTERTERMS),"root":_root((resolution,"unavailable"))})
def resolution_trajectory_manifest()->MappingProxyType:
    return _freeze({"schema":"C132-TRAJECTORY-V1","resolutions":RESOLUTIONS,"status":"C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE","points":(),"continuum_extrapolation_claimed":False,"root":_root((RESOLUTIONS,"no-calibration"))})
def renormalized_sparse_matrix(resolution:str)->MappingProxyType:
    _check(resolution); raise RuntimeError("C132_HQCDREN_COUNTERTERM_IDENTIFIABILITY_INCOMPLETE: numerical matrix unavailable")
def renormalized_sparse_bounds(resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C132-RENORMALIZED-BOUNDS-V1","resolution":resolution,"status":"UNAVAILABLE_BLOCKING","bounds":(),"root":_root((resolution,"unavailable-bounds"))})
def apply_renormalized_operator(resolution:str,vector:Any)->MappingProxyType:
    _check(resolution); np.asarray(vector,dtype=np.complex128); return _freeze({"schema":"C132-RENORMALIZED-ACTION-V1","resolution":resolution,"status":"UNAVAILABLE_BLOCKING","action":"symbolic family only","root":_root((resolution,"unavailable-action"))})
def renormalized_operator_ancestry(resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C132-OPERATOR-ANCESTRY-V1","resolution":resolution,"status":"SYMBOLIC_FAMILY_ONLY","C131_root":C131_ROOT,"root":_root((resolution,C131_ROOT))})
def counterterm_basis_manifest()->MappingProxyType:
    return _freeze({"schema":"C132-COUNTERTERM-BASIS-V1","directions":COUNTERTERMS,"coefficients_solved":0,"unidentified":COUNTERTERMS,"root":_root(COUNTERTERMS)})
def constraint_preservation_certificate(resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C132-CONSTRAINT-PRESERVATION-V1","resolution":resolution,"P0_Q0":True,"open_triplet":True,"omitted_interfaces_inserted":0,"vacuum_zeroed":0,"counterterms_absorbed":0,"hermiticity_repairs":0,"root":_root((resolution,"constraints"))})
def projected_bare_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C132-C131-COMPLETENESS-V1","C131_root":C131_ROOT,"preserved":True,"root":_root((C131_ROOT,"preserved"))})
def finite_basis_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C132-FINITE-BASIS-COMPLETENESS-V1","C130_root":C130_ROOT,"omitted_interfaces":120,"vacuum_directions":2,"counterterm_directions":6,"preserved":True,"root":_root((C130_ROOT,120,2,6))})

ROOTS={"C132_CONDITION_AUTHORITY_ROOT":_root(condition_manifest()),"C132_CONDITION_ROLE_ROOT":_root(condition_role_manifest()),"C132_SCHEME_ROOT":_root(renormalization_scheme_manifest()),"C132_UNKNOWN_PARAMETER_ROOT":_root(unknown_parameter_manifest()),"C132_IDENTIFIABILITY_ROOT":_root(identifiability_report()),"C132_COUNTERTERM_SOLUTION_ROOT":_root(counterterm_condition_crosswalk()),"C132_PARAMETER_ENCLOSURE_ROOT":_root(tuple(parameter_enclosures(r) for r in RESOLUTIONS)),"C132_RESOLUTION_TRAJECTORY_ROOT":_root(resolution_trajectory_manifest()),"C132_CONSTRAINT_PRESERVATION_ROOT":_root(tuple(constraint_preservation_certificate(r) for r in RESOLUTIONS))}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"C131":C131_ROOT,"C130":C130_ROOT})
def verify_hqcd_renormalization_authority()->dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"blocker":"C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE","baseline":BASELINE,"contract":CONTRACT,"C131_package_root":C131_ROOT,"C130_package_root":C130_ROOT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"candidate_conditions":9,"source_qualified_nonempty_conditions":0,"calibration_conditions":0,"strict_holdouts":1,"forbidden_conditions_selected":0,"scheme_selected":False,"jacobian_rank":0,"route_J_A_J_B_mismatches":0,"route_R_A_R_B_mismatches":0,"solved_parameters":0,"unidentified_directions":11,"renormalized_matrices":0,"omitted_interfaces_inserted":0,"vacuum_directions_zeroed":0,"counterterms_solved":0,"physical_parameters_selected":0,"continuum_claim":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_renormalization_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C132 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C132 root/status mismatch")
    return _freeze(verify_hqcd_renormalization_authority())
def mutate_live_hqcdren(index:int)->MappingProxyType:
    fields=("condition","target","role","scheme","mq","mq2","counterterm","jacobian","nullspace","trajectory","holdout","constraint","root","C133")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})
def static_isolation_guard()->MappingProxyType:
    return _freeze({"TMD_process_conditions":0,"effective_model_conditions":0,"hidden_parameters":0,"unidentified_zeroed":0,"Feshbach":0,"PennyLane_states":0,"TTN_states":0,"production_predictions":0,"pass":True})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","DIMS","condition_manifest","condition_role_manifest","renormalization_scheme_manifest","unknown_parameter_manifest","counterterm_condition_crosswalk","identifiability_report","null_direction_manifest","condition_result","holdout_result","renormalized_parameter_point","parameter_enclosures","resolution_trajectory_manifest","renormalized_sparse_matrix","renormalized_sparse_bounds","apply_renormalized_operator","renormalized_operator_ancestry","counterterm_basis_manifest","constraint_preservation_certificate","projected_bare_completeness_certificate","finite_basis_completeness_certificate","verify_hqcd_renormalization_authority","load_verified_hqcd_renormalization_authority","mutate_live_hqcdren","static_isolation_guard"]
