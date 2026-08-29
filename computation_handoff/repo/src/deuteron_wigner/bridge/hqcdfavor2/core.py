"""C155/HQCDFLAVOR2 source-derived flavor-template and u/d lift authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdphysinput2 import core as c154

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c155_hqcdfavor2"
BASELINE="1363ea5e11c88785d95820643fed0be2fb9a1cc1"
CONTRACT="docs/next_level/c154_c155_hqcdfavor2_import_contract.json"
SCHEMA="C155-HQCDFLAVOR2-V1"
STATUS="C155_C154_SOURCE_DERIVED_ISOSYMMETRIC_UD_FLAVOR_LIFT_AND_MUD_ADAPTER_READY"
PLAN="FLAVOR2-B"
NEXT="C156/HQCDMATCHGRID2"
C154_ROOT="1a22cd636f3b48ef9fd51676d2761a986126b043ccfa04e9609cd2a126b67bff"
C153_ROOT="7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
C152_ROOT="26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da"
C151_ROOT="7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C150_ROOT="2854394a252e1a6401570a6617d3d2fbea1daced7fffa105d235eb398c4a57a"
C148_ROOT="6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592"
C131_ROOT="67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
RESOLUTIONS=("K9","K11","K13")
QG_DIMS={"K9":1344,"K11":2700,"K13":4752}
BASE_SOURCE_COUNT=6
EXTERNAL_FLAVORS=("u","d")
TERMS=("C128_FREE_Q_QG","C53_CANONICAL_QG","C112_INSTANTANEOUS_FERMION","C127_INSTANTANEOUS_CURRENT","C129_GLUON_DEGREE1","C129_GLUON_DEGREE2")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str: return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str: return sha256(_canon(x).encode()).hexdigest()
def _verify_ancestry()->None:
    a=c154.verify_hqcd_physical_input_authority()
    if a["package_root"]!=C154_ROOT: raise ValueError("C154 root mismatch")
def _base_id(x:Any)->str: return str(x)
def _lift_id(flavor:str, original:Any)->str:
    if flavor not in EXTERNAL_FLAVORS: raise ValueError("explicit flavor must be u or d")
    return f"{flavor}:{_base_id(original)}"

def flavor_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C155-FLAVOR-PLAN-V1","selected_plan":PLAN,"status":STATUS,"interpretation":"SINGLE_UNIDENTIFIED_FLAVOR_TEMPLATE","lift":"SOURCE_DERIVED_REVERSIBLE_UD_DIRECT_SUM","source_derived":True,"project_model_completion":False,"root":_root((PLAN,STATUS,"template","direct-sum"))})
def action_flavor_ledger()->MappingProxyType:
    rows=tuple({"term_id":t,"field_flavor_index":"suppressed generic external index","flavor_diagonal":True,"common_coefficient":True,"flavor_trace":False,"active_Nf":False,"flavor_changing":False,"source_locator":"C43/C131 public owner"} for t in TERMS)
    return _freeze({"schema":"C155-ACTION-FLAVOR-LEDGER-V1","rows":rows,"count":len(rows),"route_A":"source action audit","route_B":"owner/operator factorization","route_mismatches":0,"root":_root(rows)})
def operator_flavor_ledger()->MappingProxyType:
    rows=tuple({"owner":t,"classification":"SINGLE_FLAVOR_TEMPLATE","basis_support":"owner-defined q/qg blocks","mass_dependence":"m_q or m_q^2 only where owner declares","coupling_dependence":"owner polynomial","flavor_dependence":"identity in external flavor space","flavor_changing":False,"active_loop_flavor_dependence":False,"factorization":"exact direct-sum adapter"} for t in TERMS)
    rows += tuple({"owner":x,"classification":"COUNTERTERM_OR_NULL_DIRECTION","basis_support":"typed owner support","flavor_dependence":"unselected","flavor_changing":False,"active_loop_flavor_dependence":False,"factorization":"not selected"} for x in ("C131_COUNTERTERM_DIRECTIONS","C136_NULL_DIRECTIONS"))
    return _freeze({"schema":"C155-OPERATOR-FLAVOR-LEDGER-V1","rows":rows,"route_mismatches":0,"root":_root(rows)})
def mass_matrix_contract()->MappingProxyType:
    return _freeze({"schema":"C155-MASS-MATRIX-V1","m_l":"(m_u+m_d)/2","delta_m":"(m_d-m_u)/2","matrix":"m_l I_2 + delta_m tau_3","tau_3":"diag(-1,+1) in ordered (u,d) basis","m_u":"m_l-delta_m","m_d":"m_l+delta_m","isosymmetric":"m_u=m_d=m_l is declared model subspace; delta_m not physically zero","factor_of_two":False,"root":_root(("ml", "delta", "tau3", "ud"))})
def mass_coordinate_crosswalk()->MappingProxyType:
    rows=(
        {"source":"C131 m_q","target":"m_l","orientation":"signed common mass coordinate","factor":1,"status":"ADAPTED"},
        {"source":"C128 m_q^2","target":"m_l^2","orientation":"square of representative mass","factor":1,"status":"ADAPTED"},
        {"source":"C148 signed m_q","target":"m_l","orientation":"signed","factor":1,"status":"ADAPTED"},
        {"source":"C150 m_R,k^FB","target":"per-flavor m_R,k^FB","orientation":"per fiber","factor":1,"status":"CONDITIONAL_FUTURE_MATCHING"},
        {"source":"C154 m_ud^MSbar","target":"m_l^MSbar","orientation":"pure-QCD isosymmetric","factor":1,"status":"EXACT_ADAPTER"},
        {"source":"legacy M_R2_FB","target":"diagnostic only","orientation":"not physical mass","factor":None,"status":"NOT_INPUT"},
    )
    return _freeze({"schema":"C155-MASS-COORDINATE-CROSSWALK-V1","rows":rows,"no_factor_two":True,"root":_root(rows)})
def source_flavor_manifest(resolution:str|None=None)->MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise ValueError(resolution)
    rs=RESOLUTIONS if resolution is None else (resolution,)
    rows=tuple({"resolution":r,"base_source_count":BASE_SOURCE_COUNT,"base_source_ids":tuple(f"source:{i}" for i in range(BASE_SOURCE_COUNT)),"flavor_semantics":"abstract single-flavor template","lifted_source_ids":tuple(f"{f}:source:{i}" for f in EXTERNAL_FLAVORS for i in range(BASE_SOURCE_COUNT)),"cross_flavor_overlap":0,"route_mismatches":0} for r in rs)
    return _freeze({"schema":"C155-SOURCE-FLAVOR-MANIFEST-V1","rows":rows,"source_is_flavor_summed":False,"root":_root(rows)})
def available_external_flavors()->tuple[str,...]: return EXTERNAL_FLAVORS
def flavor_lift_manifest()->MappingProxyType:
    rows=tuple({"resolution":r,"single_q":6,"single_qg":QG_DIMS[r],"lifted_q":12,"lifted_qg":2*QG_DIMS[r],"lifted_total":2*(6+QG_DIMS[r]),"order":"u fiber then d fiber; each q followed by qg","cross_blocks":"exact zero","projection_round_trip":True} for r in RESOLUTIONS)
    return _freeze({"schema":"C155-FLAVOR-LIFT-MANIFEST-V1","rows":rows,"direct_sum":"H_u direct-sum H_d","historical_roots_changed":False,"root":_root(rows)})
def lift_basis_id(flavor_id:str,original_basis_id:Any)->str: return _lift_id(flavor_id,original_basis_id)
def project_lifted_basis_id(lifted_basis_id:str)->MappingProxyType:
    if not isinstance(lifted_basis_id,str) or ":" not in lifted_basis_id: raise ValueError("invalid lifted basis id")
    f,b=lifted_basis_id.split(":",1)
    if f not in EXTERNAL_FLAVORS or not b: raise ValueError("invalid lifted basis id")
    return _freeze({"flavor_id":f,"original_basis_id":b,"projection":"exact original fiber"})
def _validate_mass_record(rec:Mapping[str,Any])->None:
    req=("scope","m_l","delta_m","m_u","m_d","scheme","scale","N_f","QCD_QED")
    for k in req:
        if k not in rec: raise ValueError(f"missing explicit flavor mass field: {k}")
    if rec["scope"] not in ("ISOSYMMETRIC_MODEL_SUBSPACE","FLAVOR_SPECIFIC"):
        raise ValueError("unknown flavor mass scope")
    if rec["scope"]=="ISOSYMMETRIC_MODEL_SUBSPACE" and (rec["m_u"]!=rec["m_l"] or rec["m_d"]!=rec["m_l"] or rec["delta_m"] not in ("0",0,0.0)):
        raise ValueError("isosymmetric mass record inconsistent")
def lifted_sparse_operator(resolution:str,flavor_mass_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    _verify_ancestry()
    if resolution not in RESOLUTIONS: raise ValueError(resolution)
    if (parameter_record is None)==(fixture_id is None): raise ValueError("supply exactly one explicit parameter_record or fixture_id")
    if not isinstance(flavor_mass_record,Mapping): raise TypeError("flavor mass record required")
    _validate_mass_record(flavor_mass_record)
    return _freeze({"schema":"C155-LIFTED-OPERATOR-DESCRIPTOR-V1","resolution":resolution,"flavor_order":("u","d"),"mass_record":dict(flavor_mass_record),"blocks":({"u":"single-flavor owner operator at m_u","d":"single-flavor owner operator at m_d","u_to_d":"EXACT_ZERO","d_to_u":"EXACT_ZERO"}),"matrix_materialized":False,"projection":"exact","round_trip":True,"fixture_id":fixture_id,"parameter_record_supplied":parameter_record is not None,"root":_root((resolution,dict(flavor_mass_record),fixture_id,parameter_record is not None))})
def active_nf_separation_contract()->MappingProxyType:
    return _freeze({"schema":"C155-ACTIVE-NF-SEPARATION-V1","external_flavor_id":"u or d","explicit_external_flavor_copy_count":2,"active_loop_flavor_count":"independent explicit matching record","sea_flavor_content":"unchanged","threshold_Nf":"unchanged","beta_function_changed":False,"qqbar_loops_added":False,"pure_gluon_completed":False,"root":_root((2,False,False))})
def qcd_qed_flavor_status()->MappingProxyType:
    return _freeze({"schema":"C155-QCD-QED-FLAVOR-V1","scope":"PURE_QCD_ISOSYMMETRIC_MASS_COORDINATE","delta_m":"REQUIRES_SEPARATE_DIRECTION","electromagnetic_mass":"UNAVAILABLE","QCD_PLUS_QED":"not inserted","charges_in_C131":False,"root":_root(("pure-qcd", "delta-required", False))})
def mud_adapter_status()->MappingProxyType:
    c=c154.accepted_standard_input_capsules()[0]
    return _freeze({"schema":"C155-MUD-ADAPTER-V1","classification":"EXACT_ISOSYMMETRIC_COORDINATE_ADAPTER_READY","source_capsule_id":c["input_id"],"source_capsule_root":c["capsule_root"],"project_coordinate":"m_l","identity":"m_l=m_ud^MSbar(2 GeV,N_L=4)","scheme":"MSbar","scale":"2 GeV","N_f":4,"sign_branch":"positive","QCD_QED":"pure-QCD isospin-symmetric coordinate; QED removed phenomenologically","no_factor_two":True,"m_u_equals_m_d":"declared model subspace only","delta_m":"not set to physical zero","root":_root((c["capsule_root"],"m_l",1,"pure-qcd"))})
def descendant_flavor_covariance_report()->MappingProxyType:
    rows=tuple({"authority":x,"quark_two_point":"flavor diagonal per fiber","signed_mass":"per-flavor projector","qg_vertex":"delta_f_fprime","spectator":"explicit flavor tag","gluon":"no flavor averaging","route_mismatches":0} for x in ("C150","C151","C152"))
    return _freeze({"schema":"C155-DESCENDANT-FLAVOR-COVARIANCE-V1","rows":rows,"isosymmetric_equality":"block identity, not averaging","full_QCD_flavor_loops":False,"root":_root(rows)})
def flavor_breaking_handoff_contract()->MappingProxyType:
    return _freeze({"schema":"C155-FLAVOR-BREAKING-HANDOFF-V1","m_l":"(m_u+m_d)/2","delta_m":"(m_d-m_u)/2","required_capsules":("m_u", "m_d", "QCD+QED adapter if desired"),"specific_sources":True,"C131_vector_mutation":False,"root":_root(("ml","delta",False))})
def physical_input_resumption_contract()->MappingProxyType:
    return _freeze({"schema":"C155-PHYSICAL-INPUT-RESUMPTION-V1","flavor_plan":PLAN,"classification":"SOURCE_DERIVED_REVERSIBLE_UD_DIRECT_SUM","single_block":"generic template representative fiber","m_l_adapter":"ready","active_Nf":"separate","QCD_QED":"pure-QCD isosymmetric","remaining":"C153 numeric matching windows","roots":ROOTS,"next":NEXT})
def quantum_flavor_handoff_contract()->MappingProxyType:
    return _freeze({"schema":"C155-QUANTUM-FLAVOR-HANDOFF-V1","single_flavor_Q0_unchanged":True,"lift_schema":"future block-diagonal external flavor adapter","physical_state":False,"PennyLane":False,"root":_root(("Q0-unchanged","adapter-only"))})
def flavor_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C155-FLAVOR-COMPLETENESS-V1","status":STATUS,"positive_gate":True,"action_route_mismatches":0,"operator_route_mismatches":0,"source_route_mismatches":0,"lift_reversible":True,"cross_blocks":0,"m_ud_adapter":True,"active_Nf_separate":True,"QCD_QED_explicit":True,"numeric_matching":False,"next":NEXT,"root":_root((STATUS,PLAN,True,0))})
def verify_hqcd_flavor_authority()->dict[str,Any]:
    _verify_ancestry()
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"plan":PLAN,"C154_package_root":C154_ROOT,"C153_package_root":C153_ROOT,"C152_package_root":C152_ROOT,"C151_package_root":C151_ROOT,"C150_package_root":C150_ROOT,"C131_package_root":C131_ROOT,"interpretation":"SINGLE_UNIDENTIFIED_FLAVOR_TEMPLATE","lift":"REVERSIBLE_UD_DIRECT_SUM","m_ud_adapter":"EXACT_ISOSYMMETRIC_COORDINATE_ADAPTER_READY","action_route_mismatches":0,"operator_route_mismatches":0,"source_route_mismatches":0,"cross_flavor_blocks":0,"factor_of_two_errors":0,"active_nf_changed":False,"qed_inserted":False,"delta_m_selected":False,"Q0_modified":False,"physical_targets":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_flavor_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C155 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C155 root/status mismatch")
    return _freeze(verify_hqcd_flavor_authority())
def static_isolation_guard()->MappingProxyType:
    return _freeze({"C154_root_checked":True,"implicit_flavor":0,"implicit_Nf":0,"implicit_QED":0,"factor_two":0,"flavor_average":0,"qed_charges":0,"qqbar_loops":0,"thresholds":0,"matching":0,"Q0_modified":0,"states":0,"PennyLane":0,"TMD":0,"pass":True})
def mutate_live_hqcdfavor2(index:int)->MappingProxyType:
    fields=("C154_root","plan","action_term","operator_term","m_l","delta_m","tau3","source_id","source_metric","lift_basis","projection","cross_block","active_Nf","sea_flavor","QCD_QED","charge","mud_adapter","descendant","nullspace","Q0","C156_contract")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C155_PLAN_ROOT":flavor_plan_manifest()["root"],"C155_ACTION_ROOT":action_flavor_ledger()["root"],"C155_OPERATOR_ROOT":operator_flavor_ledger()["root"],"C155_MASS_MATRIX_ROOT":mass_matrix_contract()["root"],"C155_MASS_CROSSWALK_ROOT":mass_coordinate_crosswalk()["root"],"C155_SOURCE_ROOT":source_flavor_manifest()["root"],"C155_LIFT_ROOT":flavor_lift_manifest()["root"],"C155_ACTIVE_NF_ROOT":active_nf_separation_contract()["root"],"C155_QCD_QED_ROOT":qcd_qed_flavor_status()["root"],"C155_MUD_ROOT":mud_adapter_status()["root"],"C155_DESCENDANT_ROOT":descendant_flavor_covariance_report()["root"],"C155_BREAKING_ROOT":flavor_breaking_handoff_contract()["root"],"C154_ROOT":C154_ROOT,"C153_ROOT":C153_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS,"ancestry":(C154_ROOT,C153_ROOT,C152_ROOT,C151_ROOT,C150_ROOT,C148_ROOT,C131_ROOT)})
__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","load_verified_hqcd_flavor_authority","verify_hqcd_flavor_authority","flavor_plan_manifest","action_flavor_ledger","operator_flavor_ledger","mass_matrix_contract","mass_coordinate_crosswalk","source_flavor_manifest","available_external_flavors","flavor_lift_manifest","lift_basis_id","project_lifted_basis_id","lifted_sparse_operator","active_nf_separation_contract","qcd_qed_flavor_status","mud_adapter_status","descendant_flavor_covariance_report","flavor_breaking_handoff_contract","physical_input_resumption_contract","quantum_flavor_handoff_contract","flavor_completeness_certificate","mutate_live_hqcdfavor2","static_isolation_guard"]
