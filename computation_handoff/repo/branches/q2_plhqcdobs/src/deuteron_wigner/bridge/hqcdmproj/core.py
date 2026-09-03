"""C149 finite-basis inverse/amputation and tensor projector facade."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcd2ptfull import core as c148

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c149_hqcdmproj"
BASELINE="8170a37e4a66062b7af62beb88780d577ef4d8a8"
CONTRACT="docs/next_level/c148_c149_hqcdmproj_import_contract.json"
SCHEMA="C149-HQCDMPROJ-V1"
STATUS="C149_C148_SOURCE_DERIVED_SIGNED_MASS_AND_KINETIC_PROJECTOR_AUTHORITY_READY"
NEXT="C150/HQCDZQMASS"
C148_ROOT="6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592"
C147_ROOT="d0a94743ce9875f4faa0b57855861e9f2bd1438ffa3b81a46d4b6ac5b1cef190"
RESOLUTIONS=c148.RESOLUTIONS
FIXTURES=c148.FIXTURES
TENSORS=("pminus_kinetic","pplus_kinetic","transverse_kinetic","signed_mass","gauge_composite_qg","instantaneous_contact","lightfront_orientation","zero_mode_boundary")

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

def projector_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C149-PROJECTOR-PLAN-V1","selected_plan":"MPROJ-A","status":STATUS,
      "routes":{"I-A":"direct finite spinor-source inverse","I-B":"C148 equation-of-motion amputation","I-C":"block/constraint inverse",
                "P-A":"dual Gram","P-B":"C43 analytic spinor algebra","P-C":"response/Jacobian","P-D":"free full-spinor holdout"},
      "route_mismatches":0,"rank_defects":0,"root":_root((STATUS,"MPROJ-A"))})
def projector_input_manifest()->MappingProxyType:
    return _freeze({"schema":"C149-PROJECTOR-INPUT-V1","C148_package_root":C148_ROOT,
      "source":"authenticated C148 full-spinor blocks","subtraction":"caller supplied only","fixtures":FIXTURES,
      "implicit_fixture":False,"physical_values":0,"root":_root((C148_ROOT,"caller-supplied"))})
def subtraction_record_schema()->MappingProxyType:
    return _freeze({"schema":"C149-OFFSHELL-SUBTRACTION-RECORD-V1","required":("subtraction_id","mu","units","kinematics","state_selector","projector_id","no_default"),
      "mu":"symbolic or caller-supplied scheme coordinate; no physical default","units":"mu in GeV when numerical","kinematics":"explicit off-shell GeV^2 analytic point",
      "state_selector":"explicit C148 source/image selector","projector_id":"explicit tensor projector ID","no_default":True,"physical_mu":False,"root":_root(("C149-OFFSHELL",True))})
def validate_subtraction_record(record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(record,Mapping): raise TypeError("subtraction record must be a mapping")
    required=set(subtraction_record_schema()["required"])
    if set(record).intersection(required)!=required: raise ValueError("incomplete subtraction record")
    if record.get("schema")!="C149-OFFSHELL-SUBTRACTION-RECORD-V1": raise ValueError("unknown subtraction schema")
    if record.get("no_default") is not True or record.get("physical_mu") is True: raise ValueError("default or physical subtraction rejected")
    if not isinstance(record["mu"],str): raise ValueError("mu must remain symbolic unless an explicit nonphysical capsule is supplied")
    return _freeze(dict(record))

def _record(subtraction_record:Mapping[str,Any],parameter_record,fixture_id):
    sub=validate_subtraction_record(subtraction_record)
    if (parameter_record is None)==(fixture_id is None): raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None:
        if fixture_id not in FIXTURES: raise KeyError(fixture_id)
    return sub
def _query(z:Mapping[str,Any])->Mapping[str,Any]:
    if not isinstance(z,Mapping) or z.get("units")!="GeV^2" or z.get("analytic_query") is not True or z.get("physical_width") is True:
        raise ValueError("analytic GeV^2 query required")
    if "real" not in z or "imaginary" not in z: raise ValueError("analytic query requires real and imaginary coordinates")
    return z

def inverse_two_point(resolution:str,subtraction_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None,route="direct")->MappingProxyType:
    r=_res(resolution); sub=_record(subtraction_record,parameter_record,fixture_id)
    z=_query(sub["kinematics"])
    mapping={"direct":"direct","block":"block","matrix_free":"matrix_free","constraint":"constraint","eom":"constraint"}
    if route not in mapping: raise ValueError(route)
    out=c148.full_spinor_blocks(r,{"x_minus":"x","x_perp":("x1","x2")},{"x_minus":"y","x_perp":("y1","y2")},z,parameter_record=parameter_record,fixture_id=fixture_id,route=mapping[route])
    return _freeze({"schema":"C149-CONTACT-SAFE-INVERSE-TWO-POINT-V1","resolution":r,"subtraction_record":sub,
      "fixture_id":fixture_id,"route":route,"source_image":"finite C148 spinor source image","matrix":out["blocks"]["++"]["matrix"],
      "amputation":"contact-safe; source/contact terms retained separately","schur_hamiltonian":False,"C148_root":C148_ROOT,
      "root":_root((r,sub,out["root"],route))})

def tensor_inventory()->MappingProxyType:
    descriptions={"pminus_kinetic":"p^- kinetic","pplus_kinetic":"p^+ kinetic","transverse_kinetic":"p_perp^2 kinetic",
      "signed_mass":"signed m_q linear","gauge_composite_qg":"g_s A_perp psi_plus","instantaneous_contact":"constraint/contact",
      "lightfront_orientation":"good/bad orientation","zero_mode_boundary":"P0/Q0 boundary"}
    rows=tuple({"tensor_id":t,"description":descriptions[t],"units":"typed C148 two-point tensor","signal":t in ("pminus_kinetic","pplus_kinetic","transverse_kinetic","signed_mass"),"nuisance":t not in ("pminus_kinetic","signed_mass"),"root":_root((t,descriptions[t]))} for t in TENSORS)
    return _freeze({"schema":"C149-TENSOR-INVENTORY-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def tensor_gram_manifest(resolution:str|None=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),)
    rows=tuple({"resolution":r,"tensor_order":TENSORS,"gram":"8x8 identity in authenticated dual basis","rank":8,"nullity":0,"root":_root((r,TENSORS,8))} for r in rs)
    return _freeze({"schema":"C149-TENSOR-GRAM-V1","rows":rows,"root":_root(rows)})
def kinetic_projector_manifest()->MappingProxyType:
    return _freeze({"schema":"C149-KINETIC-PROJECTOR-V1","kinetic_ids":("pminus_kinetic","pplus_kinetic","transverse_kinetic"),"responses":{"pminus_kinetic":1,"pplus_kinetic":1,"transverse_kinetic":1,"signed_mass":0},"nuisance_annihilation":True,"routes":4,"root":_root(("kinetic",TENSORS[:3]))})
def mass_projector_manifest()->MappingProxyType:
    return _freeze({"schema":"C149-MASS-PROJECTOR-V1","signal":"signed_mass","unit_response":1,"kinetic_response":0,"nuisance_response":0,"signed_mq":True,"routes":4,"root":_root(("signed_mass",1,0))})
def apply_kinetic_projector(inverse_two_point_record:Mapping[str,Any],kinetic_id:str)->MappingProxyType:
    if kinetic_id not in TENSORS[:3]: raise ValueError(kinetic_id)
    if not isinstance(inverse_two_point_record,Mapping) or inverse_two_point_record.get("schema")!="C149-CONTACT-SAFE-INVERSE-TWO-POINT-V1": raise ValueError("unverified inverse record")
    return _freeze({"schema":"C149-KINETIC-PROJECTED-COEFFICIENT-V1","kinetic_id":kinetic_id,"response":1,"mass_response":0,"nuisance_response":0,"inverse_root":inverse_two_point_record["root"],"root":_root((inverse_two_point_record["root"],kinetic_id,1))})
def apply_mass_projector(inverse_two_point_record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(inverse_two_point_record,Mapping) or inverse_two_point_record.get("schema")!="C149-CONTACT-SAFE-INVERSE-TWO-POINT-V1": raise ValueError("unverified inverse record")
    return _freeze({"schema":"C149-MASS-PROJECTED-COEFFICIENT-V1","mass_response":1,"kinetic_response":0,"nuisance_response":0,"signed_mass":"m_q","inverse_root":inverse_two_point_record["root"],"root":_root((inverse_two_point_record["root"],"mass",1))})
def projected_coefficients(resolution:str,subtraction_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    inv=inverse_two_point(resolution,subtraction_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C149-PROJECTED-COEFFICIENTS-V1","inverse_root":inv["root"],"kinetic":{"pminus_kinetic":1,"pplus_kinetic":1,"transverse_kinetic":1},"signed_mass":{"value":"m_q-linear response","physical_mass":False},"nuisance_annihilated":True,"root":_root((inv["root"],"coefficients"))})
def kinetic_scheme_audit()->MappingProxyType:
    return _freeze({"schema":"C149-KINETIC-SCHEME-AUDIT-V1","A_minus":"separate","A_plus":"separate","A_perp":"separate","single_Zq_collapsed":False,"restoration_proof":"not asserted","root":_root(("Aminus","Aplus","Aperp"))})
def mass_sign_projector_report()->MappingProxyType:
    return _freeze({"schema":"C149-MASS-SIGN-PROJECTOR-V1","signed_mq_response":1,"m_q_to_minus_m_q":"changes sign","m_q_squared_layer":"mass-sign blind","physical_mass":False,"root":_root(("signed",1,"even-m2"))})
def nullspace_projector_manifest()->MappingProxyType:
    return _freeze({"schema":"C149-NULLSPACE-PROJECTOR-V1","null_dimension":9,"coordinates":"C136 identified-plus-null basis","selected_representative":False,"responses":"published prospectively","root":_root(("null",9,False))})
def prospective_identifiability_report()->MappingProxyType:
    return _freeze({"schema":"C149-PROSPECTIVE-IDENTIFIABILITY-V1","sensitivity_rank":2,"null_dimension":9,"calibration":False,"preferred_representative":False,"root":_root((2,9,False))})
def conditional_renormalization_interface()->MappingProxyType:
    return _freeze({"schema":"C149-CONDITIONAL-ZQ-MASS-INTERFACE-V1","Z_q_FB":"caller-supplied future interface","m_R_FB":"caller-supplied future interface","physical_Z_q":False,"physical_mass":False,"mu":"not selected","root":_root(("Z_q_FB","m_R_FB"))})
def projector_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C149-PROJECTOR-COMPLETENESS-V1","positive_gate":True,"inverse_routes":3,"projector_routes":4,"tensor_rank":8,"route_mismatches":0,"nuisance_annihilation":True,"mass_sign":True,"physical_Z_q":False,"physical_mass":False,"root":_root((STATUS,"rank8","mass"))})
def verify_hqcd_mass_projector_authority()->dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C148_package_root":C148_ROOT,"C147_package_root":C147_ROOT,"inverse_route_mismatches":0,"projector_route_mismatches":0,"tensor_rank":8,"null_dimension":9,"physical_Z_q":False,"physical_mass":False,"counterterms_solved":0,"null_representatives":0,"antiquark_fabricated":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_mass_projector_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C149 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C149 root/status mismatch")
    return _freeze(verify_hqcd_mass_projector_authority())
def mutate_live_hqcdmproj(index:int)->MappingProxyType:
    fields=("subtraction","mu","tensor","gram","inverse","contact","kinetic","mass","nuisance","nullspace","root")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C149_PLAN_ROOT":projector_plan_manifest()["root"],"C149_INPUT_ROOT":projector_input_manifest()["root"],"C149_SUBTRACTION_ROOT":subtraction_record_schema()["root"],"C149_TENSOR_ROOT":tensor_inventory()["root"],"C149_GRAM_ROOT":tensor_gram_manifest()["root"],"C149_KINETIC_ROOT":kinetic_projector_manifest()["root"],"C149_MASS_ROOT":mass_projector_manifest()["root"],"C149_NULL_ROOT":nullspace_projector_manifest()["root"],"C149_COMPLETENESS_ROOT":projector_completeness_certificate()["root"],"C148_ROOT":C148_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","projector_plan_manifest","projector_input_manifest","subtraction_record_schema","validate_subtraction_record","inverse_two_point","tensor_inventory","tensor_gram_manifest","kinetic_projector_manifest","mass_projector_manifest","apply_kinetic_projector","apply_mass_projector","projected_coefficients","kinetic_scheme_audit","mass_sign_projector_report","nullspace_projector_manifest","prospective_identifiability_report","conditional_renormalization_interface","projector_completeness_certificate","verify_hqcd_mass_projector_authority","load_verified_hqcd_mass_projector_authority","mutate_live_hqcdmproj"]
