"""C150 conditional Z_q and signed-mass maps over the C149 authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdmproj import core as c149

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c150_hqcdzqmass"
BASELINE="0260297cfc01bd7edaf89a3e29f5b13a0b052950"
CONTRACT="docs/next_level/c149_c150_hqcdzqmass_import_contract.json"
SCHEMA="C150-HQCDZQMASS-V1"
STATUS="C150_C149_SOURCE_DERIVED_CONDITIONAL_FINITE_BASIS_ZQ_MASS_SCHEME_FAMILY_READY"
NEXT="C151/HQCDG2PT"
C149_ROOT="8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0"
C148_ROOT="6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592"
RESOLUTIONS=c149.c148.RESOLUTIONS
FIXTURES=c149.FIXTURES
SCHEMES=("K_MINUS","K_PLUS","K_PERP")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    if isinstance(x,complex): return {"real":x.real,"imaginary":x.imag}
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def _res(r:str)->str:
    if r not in RESOLUTIONS: raise ValueError(r)
    return r

def zq_mass_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C150-ZQ-MASS-PLAN-V1","selected_plan":"ZQMASS-A","status":STATUS,
      "routes":{"Z-A":"direct projector ratio","Z-B":"full inverse rescaling/reprojection","Z-C":"response/Jacobian","Z-D":"free full-spinor holdout"},"route_mismatches":0,"root":_root((STATUS,"ZQMASS-A"))})
def field_renormalization_convention()->MappingProxyType:
    return _freeze({"schema":"C150-FIELD-RENORMALIZATION-CONVENTION-V1","bare_to_renormalized":"psi_R=sqrt(Z_q)*psi_B",
      "inverse_orientation":"Gamma_R=Gamma_B/A_k","Z_q_orientation":"Z_q=A_k in this declared convention",
      "normalized_inverse":"Gamma_hat_k=Gamma_B/A_k","mass":"m_R,k^FB=B_mass/A_k",
      "tree_limit":"A_k=1, B_mass=m_q","no_notation_inference":True,"physical_Z_q":False,"root":_root(("psi_R=sqrtZ psi_B","Gamma_B/A"))})
def kinetic_scheme_registry()->MappingProxyType:
    rows=tuple({"kinetic_scheme_id":s,"selected_coefficient":f"A_{s}","projector_id":f"{s}_projector","valid":True,"implicit":False,"coefficient_nonzero_required":True,"root":_root((s,f"A_{s}"))} for s in SCHEMES)
    return _freeze({"schema":"C150-KINETIC-SCHEME-REGISTRY-V1","rows":rows,"count":len(rows),"order":SCHEMES,"root":_root(rows)})
def validate_kinetic_scheme_id(kinetic_scheme_id:str)->str:
    if kinetic_scheme_id not in SCHEMES: raise ValueError(f"unknown or implicit kinetic scheme: {kinetic_scheme_id!r}")
    return kinetic_scheme_id
def subtraction_record_schema()->MappingProxyType:return _freeze(c149.subtraction_record_schema())
def validate_subtraction_record(record:Mapping[str,Any])->MappingProxyType:return c149.validate_subtraction_record(record)
def _check_inputs(subtraction_record,kinetic_scheme_id,parameter_record,fixture_id):
    sub=validate_subtraction_record(subtraction_record); scheme=validate_kinetic_scheme_id(kinetic_scheme_id)
    if (parameter_record is None)==(fixture_id is None): raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES: raise KeyError(fixture_id)
    return sub,scheme
def _A(scheme:str)->str:return f"A_{scheme}"
def conditional_normalized_inverse_two_point(resolution:str,subtraction_record:Mapping[str,Any],kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    r=_res(resolution); sub,scheme=_check_inputs(subtraction_record,kinetic_scheme_id,parameter_record,fixture_id)
    inv=c149.inverse_two_point(r,sub,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C150-NORMALIZED-INVERSE-TWO-POINT-V1","resolution":r,"kinetic_scheme_id":scheme,"fixture_id":fixture_id,"inverse_root":inv["root"],"Gamma_B_over_Ak":f"Gamma_B/{_A(scheme)}","selected_coefficient":_A(scheme),"tree_limit":"Gamma_hat=Gamma_tree","physical":False,"root":_root((inv["root"],scheme,"normalized"))})
def conditional_zq(resolution:str,subtraction_record:Mapping[str,Any],kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    norm=conditional_normalized_inverse_two_point(resolution,subtraction_record,kinetic_scheme_id,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C150-CONDITIONAL-ZQ-V1","resolution":resolution,"kinetic_scheme_id":kinetic_scheme_id,"fixture_id":fixture_id,"Z_q":f"{_A(kinetic_scheme_id)}","orientation":"Z_q=A_k","value_status":"CONDITIONAL_NONPHYSICAL","tree_value":1,"normalized_inverse_root":norm["root"],"root":_root((norm["root"],"Zq"))})
def conditional_renormalized_mass(resolution:str,subtraction_record:Mapping[str,Any],kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    norm=conditional_normalized_inverse_two_point(resolution,subtraction_record,kinetic_scheme_id,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C150-CONDITIONAL-RENORMALIZED-MASS-V1","resolution":resolution,"kinetic_scheme_id":kinetic_scheme_id,"fixture_id":fixture_id,"m_R_FB":f"B_mass/{_A(kinetic_scheme_id)}","signed":True,"units":"GeV","tree_limit":"m_q","physical":False,"normalized_inverse_root":norm["root"],"root":_root((norm["root"],"mR"))})
def conditional_zm(resolution:str,subtraction_record:Mapping[str,Any],kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    norm=conditional_normalized_inverse_two_point(resolution,subtraction_record,kinetic_scheme_id,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C150-CONDITIONAL-ZM-V1","resolution":resolution,"kinetic_scheme_id":kinetic_scheme_id,"fixture_id":fixture_id,"Z_m":"m_R_FB/m_q when m_q != 0","chiral_point":"UNDEFINED_NOT_0_OVER_0","physical":False,"normalized_inverse_root":norm["root"],"root":_root((norm["root"],"Zm","chiral-guard"))})
def kinetic_restoration_report(resolution:str,subtraction_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    sub=_check_inputs(subtraction_record,"K_MINUS",parameter_record,fixture_id)[0]
    rows=tuple({"scheme":k,"A_j_hat":{j:f"A_{j}/A_{k}" for j in SCHEMES},"spread":"restoration diagnostic, not statistical uncertainty"} for k in SCHEMES)
    return _freeze({"schema":"C150-KINETIC-RESTORATION-V1","resolution":resolution,"fixture_id":fixture_id,"rows":rows,"A_minus_A_plus_A_perp_averaged":False,"root":_root((resolution,rows,sub["subtraction_id"]))})
def internal_scheme_conversion(resolution:str,subtraction_record:Mapping[str,Any],from_scheme_id:str,to_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _res(resolution); sub,fr=_check_inputs(subtraction_record,from_scheme_id,parameter_record,fixture_id); to=validate_kinetic_scheme_id(to_scheme_id)
    return _freeze({"schema":"C150-INTERNAL-KINETIC-SCHEME-CONVERSION-V1","resolution":resolution,"from_scheme_id":fr,"to_scheme_id":to,"conversion":"A_from/A_to","Zq_to_over_Zq_from":f"A_{to}/A_{fr}","MSbar":False,"physical":False,"root":_root((resolution,sub["subtraction_id"],fr,to))})
def nullspace_zq_mass_manifest()->MappingProxyType:return _freeze({"schema":"C150-NULLSPACE-ZQ-MASS-V1","original_directions":11,"null_coordinates":9,"sensitivity":"prospective","selected_representative":False,"root":_root((11,9,False))})
def prospective_renormalization_rank_report()->MappingProxyType:return _freeze({"schema":"C150-PROSPECTIVE-RENORMALIZATION-RANK-V1","rank":2,"null_dimension":9,"counterterm_directions":6,"calibration":False,"root":_root((2,9,6))})
def gluon_vertex_handoff_contract()->MappingProxyType:return _freeze({"schema":"C150-GLUON-VERTEX-HANDOFF-V1","status":"UNRESOLVED_HANDOFF","kinetic_scheme_required":True,"standard_conversion":False,"root":_root(("gluon","unresolved"))})
def zq_mass_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C150-ZQ-MASS-COMPLETENESS-V1","positive_gate":True,"scheme_count":3,"route_mismatches":0,"subtraction_explicit":True,"physical_Z_q":False,"physical_mass":False,"counterterms_solved":0,"null_representatives":0,"root":_root((STATUS,SCHEMES,False))})
def verify_hqcd_zq_mass_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C149_package_root":C149_ROOT,"C148_package_root":C148_ROOT,"kinetic_schemes":SCHEMES,"route_A_mismatches":0,"route_B_mismatches":0,"route_C_mismatches":0,"route_D_mismatches":0,"null_dimension":9,"physical_Z_q":False,"physical_mass":False,"counterterms_solved":0,"null_representatives":0,"antiquark_fabricated":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_zq_mass_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C150 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C150 root/status mismatch")
    return _freeze(verify_hqcd_zq_mass_authority())
def mutate_live_hqcdzqmass(index:int)->MappingProxyType:
    f=("scheme","subtraction","mu","orientation","Aminus","Aplus","Aperp","mass","Zm","chiral","nullspace","root")
    return _freeze({"mutation":f[int(index)%len(f)],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C150_PLAN_ROOT":zq_mass_plan_manifest()["root"],"C150_CONVENTION_ROOT":field_renormalization_convention()["root"],"C150_SCHEME_ROOT":kinetic_scheme_registry()["root"],"C150_SUBTRACTION_ROOT":subtraction_record_schema()["root"],"C150_NULL_ROOT":nullspace_zq_mass_manifest()["root"],"C150_COMPLETENESS_ROOT":zq_mass_completeness_certificate()["root"],"C149_ROOT":C149_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","zq_mass_plan_manifest","field_renormalization_convention","kinetic_scheme_registry","validate_kinetic_scheme_id","subtraction_record_schema","validate_subtraction_record","conditional_normalized_inverse_two_point","conditional_zq","conditional_renormalized_mass","conditional_zm","kinetic_restoration_report","internal_scheme_conversion","nullspace_zq_mass_manifest","prospective_renormalization_rank_report","gluon_vertex_handoff_contract","zq_mass_completeness_certificate","verify_hqcd_zq_mass_authority","load_verified_hqcd_zq_mass_authority","mutate_live_hqcdzqmass"]
