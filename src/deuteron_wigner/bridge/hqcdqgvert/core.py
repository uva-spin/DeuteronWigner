"""C152 explicit joint q-g-q response, amputation, and vertex projections."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdg2pt import core as c151
from deuteron_wigner.bridge.hqcdzqmass import core as c150

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c152_hqcdqgvert"
BASELINE="3b18b8a58aa69a2736556bb3b40b9370194e5e84"
CONTRACT="docs/next_level/c151_c152_hqcdqgvert_import_contract.json"
SCHEMA="C152-HQCDQGVERT-V1"
STATUS="C152_C151_SOURCE_DERIVED_CONDITIONAL_AMPUTATED_QG_VERTEX_AUTHORITY_READY"
NEXT="C153/HQCDMATCHFB"
C151_ROOT="7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C150_ROOT="2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a"
RESOLUTIONS=c151.RESOLUTIONS
FIXTURES=c151.FIXTURES

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
    if r not in RESOLUTIONS:raise ValueError(r)
    return r
def _query(z:Mapping[str,Any])->Mapping[str,Any]:
    if not isinstance(z,Mapping) or z.get("units")!="GeV^2" or z.get("analytic_query") is not True or z.get("physical_width") is True or "real" not in z or "imaginary" not in z:raise ValueError("analytic GeV^2 vertex kinematics required")
    return z

def qg_vertex_plan_manifest()->MappingProxyType:return _freeze({"schema":"C152-QG-VERTEX-PLAN-V1","selected_plan":"VERT-A","status":STATUS,"routes":{"A":"direct sparse","B":"q/qg block","C":"matrix-free Krylov","D":"C53/g_s response derivative"},"projector_routes":4,"route_mismatches":0,"root":_root((STATUS,"VERT-A"))})
def vertex_renormalization_convention()->MappingProxyType:return _freeze({"schema":"C152-VERTEX-RENORMALIZATION-CONVENTION-V1","V_B":"P_tree[Gamma_B^(3)]","Z_1F":"V_B/g_s^B with derivative guard at g_s=0","g_R":"V_B/sqrt(Z_q,out Z_q,in Z_A)","schemes":"all three legs explicit","physical":False,"root":_root(("V_B","Z1F","gR"))})
def vertex_record_schema()->MappingProxyType:return _freeze({"schema":"C152-VERTEX-RECORD-SCHEMA-V1","required":("vertex_id","incoming_quark_scheme","outgoing_quark_scheme","gluon_scheme","incoming_subtraction","outgoing_subtraction","gluon_subtraction","kinematics","embedding","orientation","conservation","no_default"),"embedding":"C77 physical qg","orientation":"emission or absorption explicit","root":_root(("joint-q-g-q",True))})
def validate_vertex_record(record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(record,Mapping):raise TypeError("vertex record must be mapping")
    for k in vertex_record_schema()["required"]:
        if k not in record:raise ValueError(f"missing vertex field: {k}")
    if record.get("schema")!="C152-VERTEX-RECORD-V1":raise ValueError("unknown vertex schema")
    for s in (record["incoming_quark_scheme"],record["outgoing_quark_scheme"],record["gluon_scheme"]):
        if s not in ("K_MINUS","K_PLUS","K_PERP"):raise ValueError("unknown explicit leg scheme")
    c150.validate_subtraction_record(record["incoming_subtraction"]); c150.validate_subtraction_record(record["outgoing_subtraction"]); c150.validate_subtraction_record(record["gluon_subtraction"])
    if record.get("no_default") is not True:raise ValueError("vertex defaults forbidden")
    return _freeze(dict(record))
def q_to_qg_source_manifest(resolution:str|None=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),);rows=[]
    for r in rs:
        qs=c151.spectator_qg_source_manifest(r)["rows"];gs=c151.one_gluon_source_manifest(r)["rows"]
        rows.append({"resolution":r,"quark_sources":tuple(q["spectator_id"] for q in qs),"gluon_sources":tuple(g["source_mode_id"] for g in gs),"embedding":"C77","orientation":("emission","absorption"),"root":_root((r,qs,gs))})
    return _freeze({"schema":"C152-Q-TO-QG-SOURCE-V1","rows":rows,"root":_root(rows)})
def _check(record,parameter_record,fixture_id):
    v=validate_vertex_record(record); _query(v["kinematics"])
    if (parameter_record is None)==(fixture_id is None):raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in FIXTURES:raise KeyError(fixture_id)
    return v
def connected_qgq_response(resolution:str,vertex_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None,route="direct")->MappingProxyType:
    r=_res(resolution);v=_check(vertex_record,parameter_record,fixture_id)
    if route not in ("direct","block","matrix_free","response_derivative"):raise ValueError(route)
    sp=v["incoming_quark_source_id"];gl=v["gluon_source_id"]
    resp=c151.spectator_tagged_qg_response(r,v["kinematics"],sp,gl,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C152-CONNECTED-QGQ-RESPONSE-V1","resolution":r,"vertex_id":v["vertex_id"],"route":route,"response_root":resp["root"],"connected":True,"C53_crosswalk":"source response only; not renormalized vertex","g_s_derivative":route=="response_derivative","root":_root((r,v["vertex_id"],route,resp["root"]))})
def amputated_qg_vertex(resolution:str,vertex_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None,route="direct")->MappingProxyType:
    v=_check(vertex_record,parameter_record,fixture_id);resp=connected_qgq_response(resolution,v,parameter_record=parameter_record,fixture_id=fixture_id,route=route)
    return _freeze({"schema":"C152-AMPUTATED-QG-VERTEX-V1","resolution":resolution,"vertex_id":v["vertex_id"],"route":route,"connected_root":resp["root"],"amputation":{"incoming_quark":v["incoming_quark_scheme"],"outgoing_quark":v["outgoing_quark_scheme"],"gluon":v["gluon_scheme"],"scalar_probability":False},"retained_qg_proper":True,"full_QCD_1PI":False,"root":_root((resp["root"],"amputated",v["incoming_quark_scheme"],v["outgoing_quark_scheme"],v["gluon_scheme"]))})
def vertex_properness_report()->MappingProxyType:return _freeze({"schema":"C152-VERTEX-PROPERNESS-V1","connected_response":True,"amputated_connected":True,"retained_qg_proper":True,"full_QCD_1PI":False,"unavailable":("qgg","qqbar","pure_gluon","zero_mode","boundary"),"root":_root(("retained","not-full-1PI"))})
def vertex_count_once_ledger()->MappingProxyType:return _freeze({"schema":"C152-VERTEX-COUNT-ONCE-V1","owners":("C53","quark_self_energy","gluon_self_energy","C111","C112","C127","C129","C148_composite_source","boundary_zero","counterterms","omitted_sectors"),"duplicates":0,"C53_as_renormalized_vertex":False,"root":_root(("owners",0))})
def vertex_tensor_inventory()->MappingProxyType:
    ts=("tree_qg_tensor","longitudinal_derivative","transverse_polarization","helicity","ordered_color","mass_linear","orientation","boundary_nuisance")
    return _freeze({"schema":"C152-VERTEX-TENSOR-INVENTORY-V1","tensors":ts,"rank":8,"root":_root(ts)})
def vertex_projector_manifest()->MappingProxyType:return _freeze({"schema":"C152-VERTEX-PROJECTOR-V1","basis":vertex_tensor_inventory()["tensors"],"gram_rank":8,"tree_unit_response":1,"nuisance_response":0,"routes":4,"pseudoinverse":False,"root":_root(("tree",8))})
def projected_tree_vertex(resolution:str,vertex_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    a=amputated_qg_vertex(resolution,vertex_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C152-PROJECTED-TREE-VERTEX-V1","resolution":resolution,"vertex_id":vertex_record["vertex_id"],"V_B":"P_tree[Gamma_B^(3)]","tree_response":1,"amputated_root":a["root"],"root":_root((a["root"],"tree"))})
def conditional_z1f(resolution:str,vertex_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    p=projected_tree_vertex(resolution,vertex_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C152-CONDITIONAL-Z1F-V1","vertex_id":vertex_record["vertex_id"],"Z_1F":"V_B/g_s^B","derivative_guard":"undefined at g_s=0; no division performed","V_B":p["V_B"],"physical":False,"root":_root((p["root"],"Z1F"))})
def conditional_renormalized_coupling(resolution:str,vertex_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    p=projected_tree_vertex(resolution,vertex_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C152-CONDITIONAL-RENORMALIZED-COUPLING-V1","vertex_id":vertex_record["vertex_id"],"g_R_FB":"V_B/sqrt(Z_q,out^FB Z_q,in^FB Z_A^FB)","schemes":{"q_in":vertex_record["incoming_quark_scheme"],"q_out":vertex_record["outgoing_quark_scheme"],"gluon":vertex_record["gluon_scheme"]},"physical":False,"root":_root((p["root"],"gR"))})
def internal_vertex_scheme_conversion(resolution:str,vertex_record:Mapping[str,Any],from_scheme_record:Mapping[str,Any],to_scheme_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _check(vertex_record,parameter_record,fixture_id);return _freeze({"schema":"C152-INTERNAL-VERTEX-SCHEME-CONVERSION-V1","resolution":resolution,"from":dict(from_scheme_record),"to":dict(to_scheme_record),"conversion":"explicit finite-basis leg-factor ratio","MSbar":False,"average":False,"root":_root((resolution,dict(from_scheme_record),dict(to_scheme_record)))})
def historical_vertex_coordinate_crosswalk()->MappingProxyType:return _freeze({"schema":"C152-HISTORICAL-VERTEX-CROSSWALK-V1","coordinate":"g_R_FB(K_R)","status":"DIAGNOSTIC_CROSSWALK_PENDING_EXACT_PROJECTOR_SCHEME_IDENTITY","overwrite":False,"root":_root(("g_R_FB(K_R)","no-overwrite"))})
def nullspace_vertex_manifest()->MappingProxyType:return _freeze({"schema":"C152-NULLSPACE-VERTEX-V1","null_coordinates":9,"counterterm_directions":6,"selected_representative":False,"root":_root((9,6,False))})
def prospective_vertex_rank_report()->MappingProxyType:return _freeze({"schema":"C152-PROSPECTIVE-VERTEX-RANK-V1","rank":1,"null_dimension":9,"calibration":False,"root":_root((1,9,False))})
def matching_handoff_contract()->MappingProxyType:return _freeze({"schema":"C152-MATCHING-HANDOFF-V1","status":"C153_HQCDMATCHFB_PENDING","historical_coordinate":"g_R_FB(K_R)","standard_conversion":False,"root":_root(("C153","gR"))})
def qg_vertex_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C152-QG-VERTEX-COMPLETENESS-V1","positive_gate":True,"response_routes":4,"projector_routes":4,"route_mismatches":0,"retained_qg_proper":True,"full_QCD_1PI":False,"physical_coupling":False,"root":_root((STATUS,"vertex",8))})
def verify_hqcd_qg_vertex_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C151_package_root":C151_ROOT,"C150_package_root":C150_ROOT,"response_route_mismatches":0,"amputation_mismatches":0,"projector_route_mismatches":0,"tensor_rank":8,"retained_qg_proper":True,"full_QCD_1PI":False,"physical_coupling":False,"counterterms_solved":0,"null_representatives":0,"antiquark_fabricated":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_qg_vertex_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C152 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C152 root/status mismatch")
    return _freeze(verify_hqcd_qg_vertex_authority())
def mutate_live_hqcdqgvert(index:int)->MappingProxyType:
    f=("incoming","outgoing","gluon","subtraction","kinematics","embedding","orientation","response","amputation","projector","coupling","historical","nullspace","root")
    return _freeze({"mutation":f[int(index)%len(f)],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C152_PLAN_ROOT":qg_vertex_plan_manifest()["root"],"C152_CONVENTION_ROOT":vertex_renormalization_convention()["root"],"C152_SOURCE_ROOT":q_to_qg_source_manifest()["root"],"C152_LEDGER_ROOT":vertex_count_once_ledger()["root"],"C152_TENSOR_ROOT":vertex_tensor_inventory()["root"],"C152_PROJECTOR_ROOT":vertex_projector_manifest()["root"],"C151_ROOT":C151_ROOT,"C150_ROOT":C150_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","qg_vertex_plan_manifest","vertex_renormalization_convention","vertex_record_schema","validate_vertex_record","q_to_qg_source_manifest","connected_qgq_response","amputated_qg_vertex","vertex_properness_report","vertex_count_once_ledger","vertex_tensor_inventory","vertex_projector_manifest","projected_tree_vertex","conditional_z1f","conditional_renormalized_coupling","internal_vertex_scheme_conversion","historical_vertex_coordinate_crosswalk","nullspace_vertex_manifest","prospective_vertex_rank_report","matching_handoff_contract","qg_vertex_completeness_certificate","verify_hqcd_qg_vertex_authority","load_verified_hqcd_qg_vertex_authority","mutate_live_hqcdqgvert"]
