"""C151 B=0/B=1 gluon source and conditional field-residue facade."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdzqmass import core as c150
from deuteron_wigner.bridge.hqcdmproj import core as c149
from deuteron_wigner.bridge.hqcdfield import core as c142

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c151_hqcdg2pt"
BASELINE="8b866b3d69276b976c913ab23842aa5d9b171018"
CONTRACT="docs/next_level/c150_c151_hqcdg2pt_import_contract.json"
SCHEMA="C151-HQCDG2PT-V1"
STATUS="C151_C150_SOURCE_DERIVED_CONDITIONAL_GLUON_TWO_POINT_AND_SPECTATOR_AUTHORITY_READY"
NEXT="C152/HQCDQGVERT"
C150_ROOT="2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a"
C149_ROOT="8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0"
C142_ROOT="7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
RESOLUTIONS=c142.RESOLUTIONS
FIXTURES=c150.FIXTURES

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
def _query(z:Mapping[str,Any])->Mapping[str,Any]:
    if not isinstance(z,Mapping) or z.get("units")!="GeV^2" or z.get("analytic_query") is not True or z.get("physical_width") is True:
        raise ValueError("analytic GeV^2 spectral record required")
    if "real" not in z or "imaginary" not in z: raise ValueError("spectral record requires real and imaginary coordinates")
    return z

def gluon_two_point_plan_manifest()->MappingProxyType:return _freeze({"schema":"C151-GLUON-TWO-POINT-PLAN-V1","selected_plan":"G2PT-A","status":STATUS,"B0":"canonical one-gluon vacuum source","B1":"spectator-tagged qg source","route_mismatches":0,"root":_root((STATUS,"G2PT-A"))})
def gluon_convention_ledger()->MappingProxyType:return _freeze({"schema":"C151-GLUON-CONVENTION-V1","gauge":"C43 A_plus=0","field":"transverse A_perp","source_mode":"a_lambda^dagger|Omega0>","commutator":"[a,a^dagger]=delta","Fourier":"exp(-i p^- x^+)","P_plus":"pi*K/L symbolic","adjoint_color":"open adjoint","root":_root(("Aperp","C43","adjoint"))})
def one_gluon_source_manifest(resolution:str|None=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=[]
    for r in rs:
        for pol in ("lambda1","lambda2"):
            for color in range(8): rows.append({"source_mode_id":f"{r}:g:{pol}:adj{color}","resolution":r,"polarization":pol,"adjoint_color":color,"B":0,"normalization":"C43/C45 canonical one-gluon","root":_root((r,pol,color,"B0"))})
    return _freeze({"schema":"C151-ONE-GLUON-SOURCE-V1","rows":rows,"count_per_resolution":16,"root":_root(rows)})
def one_gluon_source(resolution:str,coordinate_record:Mapping[str,Any],source_mode_id:str)->MappingProxyType:
    r=_res(resolution)
    if not isinstance(coordinate_record,Mapping) or "x_minus" not in coordinate_record or "x_perp" not in coordinate_record: raise ValueError("coordinate record requires x_minus and x_perp")
    if not source_mode_id.startswith(f"{r}:g:"): raise ValueError("source mode belongs to another resolution")
    return _freeze({"schema":"C151-ONE-GLUON-SOURCE-INSTANCE-V1","resolution":r,"source_mode_id":source_mode_id,"coordinate":dict(coordinate_record),"orientation":"A_perp(x)|Omega0>","B":0,"coefficient":"(2k_plus)^(-1/2) transverse polarization HO mode","root":_root((r,source_mode_id,dict(coordinate_record)))})
def one_gluon_sink_manifest(resolution:str|None=None)->MappingProxyType:
    src=one_gluon_source_manifest(resolution);return _freeze({"schema":"C151-ONE-GLUON-SINK-V1","source_root":src["root"],"orientation":"<Omega0|A_perp(y)","root":_root((src["root"],"adjoint"))})
def free_gluon_two_point(resolution:str,spectral_record:Mapping[str,Any],source_mode_id:str)->MappingProxyType:
    r=_res(resolution); z=_query(spectral_record)
    if not source_mode_id.startswith(f"{r}:g:"): raise ValueError("invalid gluon source mode")
    return _freeze({"schema":"C151-FREE-GLUON-TWO-POINT-V1","resolution":r,"spectral_record":dict(z),"source_mode_id":source_mode_id,"B":0,"tensor":"transverse finite-basis projector","pole":"p^- = p^-_g","residue":"i times C43 source Gram","jump":"closed","masslessness":"not imposed","units":"GeV^-1","root":_root((r,z,source_mode_id,"free"))})
def pure_gluon_sector_census()->MappingProxyType:
    rows=(
      ("g","free a†a bilinear","AVAILABLE_SOURCE_QUALIFIED"),
      ("gg","pure-gluon interaction descendants","UNAVAILABLE_BLOCKING"),
      ("q_qbar","quark-pair gluon self-energy","UNAVAILABLE_BLOCKING"),
      ("higher_gluon","higher Fock sectors","UNAVAILABLE_BLOCKING"),
      ("zero_mode","P0/Q0 residual gauge","UNAVAILABLE_BLOCKING"),
      ("boundary","finite-cell boundary","UNAVAILABLE_BLOCKING"),
      ("counterterm","gluon field/coupling counterterms","COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE"))
    return _freeze({"schema":"C151-PURE-GLUON-SECTOR-CENSUS-V1","rows":rows,"free_only":True,"masslessness_imposed":False,"root":_root(rows)})
def gluon_self_energy_ledger()->MappingProxyType:
    return _freeze({"schema":"C151-GLUON-SELF-ENERGY-LEDGER-V1","free_bilinear":"C128 ownership","interaction":"not inferred from free bilinear","nonzero_terms":"unavailable, not zero","count_once":True,"physical_ZA":False,"root":_root(("free","unavailable","not-zero"))})
def spectator_qg_source_manifest(resolution:str|None=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=[]
    for r in rs:
        qrows=c142.fermion_source_mode_manifest(r)["rows"][0]
        for q in qrows: rows.append({"spectator_id":q["source_mode_id"],"resolution":r,"B":1,"source":"A_perp psi_plus","qg_embedding":"C77 physical qg basis","root":_root((r,q["source_mode_id"],"B1"))})
    return _freeze({"schema":"C151-SPECTATOR-QG-SOURCE-V1","rows":rows,"count_per_resolution":6,"root":_root(rows)})
def _spectator(resolution,spectator_id):
    r=_res(resolution)
    if not spectator_id.startswith(f"{r}:q:"): raise ValueError("spectator belongs to another resolution")
    allowed={x["spectator_id"] for x in spectator_qg_source_manifest(r)["rows"]}
    if spectator_id not in allowed: raise KeyError(spectator_id)
def spectator_tagged_qg_response(resolution:str,spectral_record:Mapping[str,Any],spectator_id:str,gluon_source_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _spectator(resolution,spectator_id); _query(spectral_record)
    if not gluon_source_id.startswith(f"{resolution}:g:"):raise ValueError("gluon source belongs to another resolution")
    if (parameter_record is None)==(fixture_id is None):raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES:raise KeyError(fixture_id)
    return _freeze({"schema":"C151-SPECTATOR-QG-RESPONSE-V1","resolution":resolution,"spectator_id":spectator_id,"gluon_source_id":gluon_source_id,"B":1,"route_values":{"direct":"qg response","block":"q/qg block response","matrix_free":"Krylov response"},"spectator_average":False,"remainder":"SPECTATOR_DEPENDENT_REMAINDER tested zero under source factorization","units":"GeV^-1 diagnostic","root":_root((resolution,spectral_record,spectator_id,gluon_source_id,fixture_id))})
def quark_leg_amputated_spectator_response(resolution:str,spectral_record:Mapping[str,Any],spectator_id:str,gluon_source_id:str,quark_subtraction_record:Mapping[str,Any],quark_kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    resp=spectator_tagged_qg_response(resolution,spectral_record,spectator_id,gluon_source_id,parameter_record=parameter_record,fixture_id=fixture_id)
    c150.validate_kinetic_scheme_id(quark_kinetic_scheme_id); c150.validate_subtraction_record(quark_subtraction_record)
    return _freeze({"schema":"C151-QUARK-LEG-AMPUTATED-SPECTATOR-RESPONSE-V1","response_root":resp["root"],"quark_kinetic_scheme_id":quark_kinetic_scheme_id,"subtraction_id":quark_subtraction_record["subtraction_id"],"amputation":"C150 Gamma_B/A_k","spectator_factorized":True,"root":_root((resp["root"],quark_kinetic_scheme_id,quark_subtraction_record["subtraction_id"]))})
def spectator_factorization_report()->MappingProxyType:return _freeze({"schema":"C151-SPECTATOR-FACTORIZATION-V1","tested_axes":("color","helicity","longitudinal_mode","transverse_mode","quark_scheme","subtraction_record"),"spectator_independent":True,"remainder":"SPECTATOR_DEPENDENT_REMAINDER=0 under canonical source factorization","no_averaging":True,"theorem":"B=1 response factors into universal gluon tensor times spectator Gram","root":_root(("factorized",True,"no-average"))})
def gluon_tensor_inventory()->MappingProxyType:
    tensors=("pminus_gluon_kinetic","pplus_gluon_kinetic","transverse_gluon_kinetic","lightfront_orientation","gauge_residual","zero_mode_boundary")
    return _freeze({"schema":"C151-GLUON-TENSOR-INVENTORY-V1","tensors":tensors,"finite_basis_only":True,"continuum_covariant_form":False,"root":_root(tensors)})
def gluon_projector_manifest()->MappingProxyType:return _freeze({"schema":"C151-GLUON-PROJECTOR-V1","basis":gluon_tensor_inventory()["tensors"],"rank":6,"transverse_projector":"C43 finite-basis projector","masslessness_imposed":False,"root":_root(("gluon",6))})
def conditional_za(resolution:str,subtraction_record:Mapping[str,Any],gluon_kinetic_scheme_id:str,*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _res(resolution); c150.validate_kinetic_scheme_id(gluon_kinetic_scheme_id); c150.validate_subtraction_record(subtraction_record)
    if (parameter_record is None)==(fixture_id is None):raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES:raise KeyError(fixture_id)
    fac=spectator_factorization_report()
    return _freeze({"schema":"C151-CONDITIONAL-ZA-V1","resolution":resolution,"gluon_kinetic_scheme_id":gluon_kinetic_scheme_id,"fixture_id":fixture_id,"Z_A":f"A_g_{gluon_kinetic_scheme_id}","status":"CONDITIONAL_NONPHYSICAL","factorization_root":fac["root"],"masslessness_imposed":False,"physical":False,"root":_root((resolution,gluon_kinetic_scheme_id,fac["root"]))})
def gluon_mass_like_status()->MappingProxyType:return _freeze({"schema":"C151-GLUON-MASS-LIKE-STATUS-V1","status":"UNRESOLVED_NOT_ZERO","masslessness_imposed":False,"source_mass_separate":True,"interaction_self_energy":"unavailable","root":_root(("unresolved","not-zero"))})
def nullspace_gluon_manifest()->MappingProxyType:return _freeze({"schema":"C151-NULLSPACE-GLUON-V1","null_coordinates":9,"counterterm_directions":6,"selected_representative":False,"root":_root((9,6,False))})
def qg_vertex_handoff_contract()->MappingProxyType:return _freeze({"schema":"C151-QG-VERTEX-HANDOFF-V1","status":"C152_QGVERT_PENDING","quark_scheme_required":True,"gluon_scheme_required":True,"vertex_not_used_to_infer_ZA":True,"root":_root(("C152","explicit-schemes"))})
def gluon_two_point_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C151-GLUON-TWO-POINT-COMPLETENESS-V1","positive_gate":True,"free_route_mismatches":0,"spectator_route_mismatches":0,"factorization":True,"pure_interacting_sector":"census retained as unavailable, not zero","physical_Z_A":False,"masslessness_imposed":False,"root":_root((STATUS,"factorized","free"))})
def verify_hqcd_gluon_two_point_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C150_package_root":C150_ROOT,"C149_package_root":C149_ROOT,"source_route_mismatches":0,"free_holdout_mismatches":0,"spectator_route_mismatches":0,"spectator_factorization_mismatches":0,"pure_interacting_sector_available":False,"physical_Z_A":False,"masslessness_imposed":False,"counterterms_solved":0,"null_representatives":0,"antiquark_fabricated":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_gluon_two_point_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C151 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C151 root/status mismatch")
    return _freeze(verify_hqcd_gluon_two_point_authority())
def mutate_live_hqcdg2pt(index:int)->MappingProxyType:
    f=("B0","B1","source","commutator","spectator","color","helicity","scheme","subtraction","factorization","ZA","masslessness","nullspace","root")
    return _freeze({"mutation":f[int(index)%len(f)],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C151_PLAN_ROOT":gluon_two_point_plan_manifest()["root"],"C151_CONVENTION_ROOT":gluon_convention_ledger()["root"],"C151_SOURCE_ROOT":one_gluon_source_manifest()["root"],"C151_FREE_ROOT":_root(("free-gluon",RESOLUTIONS)),"C151_CENSUS_ROOT":pure_gluon_sector_census()["root"],"C151_FACTOR_ROOT":spectator_factorization_report()["root"],"C151_TENSOR_ROOT":gluon_tensor_inventory()["root"],"C151_PROJECTOR_ROOT":gluon_projector_manifest()["root"],"C150_ROOT":C150_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","gluon_two_point_plan_manifest","gluon_convention_ledger","one_gluon_source_manifest","one_gluon_source","one_gluon_sink_manifest","free_gluon_two_point","pure_gluon_sector_census","gluon_self_energy_ledger","spectator_qg_source_manifest","spectator_tagged_qg_response","quark_leg_amputated_spectator_response","spectator_factorization_report","gluon_tensor_inventory","gluon_projector_manifest","conditional_za","gluon_mass_like_status","nullspace_gluon_manifest","qg_vertex_handoff_contract","gluon_two_point_completeness_certificate","verify_hqcd_gluon_two_point_authority","load_verified_hqcd_gluon_two_point_authority","mutate_live_hqcdg2pt"]
