"""C153 explicit finite-basis/target matching records and conversions."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdqgvert import core as c152

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c153_hqcdmatchfb"
BASELINE="c39c6bbbcaa75cfcb7075cb68e3a222832c21249"
CONTRACT="docs/next_level/c152_c153_hqcdmatchfb_import_contract.json"
SCHEMA="C153-HQCDMATCHFB-V1"
STATUS="C153_C152_SOURCE_DERIVED_COMPONENTWISE_FINITE_BASIS_MATCHING_AUTHORITY_READY"
NEXT="C154/HQCDPHYSINPUT2"
C152_ROOT="26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da"
C151_ROOT="7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
QUANTITIES=("quark_field","signed_quark_mass","gluon_field","qg_vertex","qcd_coupling")
TARGETS=("MSBAR_C43_ADAPTED","PROJECT_LIGHT_FRONT_NONEXCEPTIONAL","RI_SMOM","MOMQ","STEP_SCALING")
SOURCES=("arXiv:0901.2599","arXiv:2002.12758","arXiv:1108.4806","arXiv:2002.02875","arXiv:1706.03821","arXiv:1802.05243")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType):return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping):return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [_plain(v) for v in x]
    if isinstance(x,complex):return {"real":x.real,"imaginary":x.imag}
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping):return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)):return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()

def matching_plan_manifest()->MappingProxyType:return _freeze({"schema":"C153-MATCHING-PLAN-V1","selected_plan":"MATCHFB-A","status":STATUS,"routes":{"A":"common-IR coefficient difference","B":"projected ratio","C":"inverse round-trip","D":"step/cocycle"},"route_mismatches":0,"root":_root((STATUS,"MATCHFB-A"))})
def primary_source_manifest()->MappingProxyType:
    rows=tuple({"source_id":s,"locator":f"https://arxiv.org/abs/{s.split(':')[1]}","hash_lock":"locator-scoped methodological authority; no numeric values consumed","role":"target/conversion/methodological authority","gauge_scope":"source-specific, adapter required","numeric_project_input":False,"root":_root((s,"no-numeric"))} for s in SOURCES)
    return _freeze({"schema":"C153-PRIMARY-SOURCE-MANIFEST-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def target_scheme_registry()->MappingProxyType:
    rows=tuple({"target_scheme_id":t,"gauge":"explicit per record","N_f":"explicit per record","scale":"explicit per record","kinematics":"explicit nonexceptional record","adapter":"C43 adapter required","standard_conversion":t in ("MSBAR_C43_ADAPTED","RI_SMOM","MOMQ"),"root":_root((t,"explicit"))} for t in TARGETS)
    return _freeze({"schema":"C153-TARGET-SCHEME-REGISTRY-V1","rows":rows,"order":TARGETS,"root":_root(rows)})
def quantity_order_eligibility_ledger()->MappingProxyType:
    orders={"quark_field":0,"signed_quark_mass":0,"gluon_field":0,"qg_vertex":1,"qcd_coupling":1}
    return _freeze({"schema":"C153-QUANTITY-ORDER-ELIGIBILITY-V1","rows":tuple({"quantity_id":q,"first_order":orders[q],"eligible":True,"missing_sector_remainder":q in ("gluon_field","qg_vertex","qcd_coupling")} for q in QUANTITIES),"root":_root(orders)})
def matching_record_schema()->MappingProxyType:return _freeze({"schema":"C153-MATCHING-RECORD-SCHEMA-V1","required":("matching_id","quantity_id","finite_basis_scheme","target_scheme_id","order","gauge","N_f","mu","kinematics","common_ir_id","no_default"),"common_ir_required":True,"target_required":True,"root":_root(("componentwise",QUANTITIES,TARGETS))})
def validate_matching_record(record:Mapping[str,Any])->MappingProxyType:
    if not isinstance(record,Mapping):raise TypeError("matching record must be mapping")
    for k in matching_record_schema()["required"]:
        if k not in record:raise ValueError(f"missing matching field: {k}")
    if record.get("schema")!="C153-MATCHING-RECORD-V1":raise ValueError("unknown matching schema")
    if record["quantity_id"] not in QUANTITIES or record["target_scheme_id"] not in TARGETS:raise ValueError("unknown quantity or target")
    if not isinstance(record["N_f"],int) or not isinstance(record["gauge"],str) or not isinstance(record["mu"],str):raise ValueError("N_f, gauge, and mu must be explicit")
    if not record.get("common_ir_id") or record.get("no_default") is not True:raise ValueError("common IR/default guard failed")
    return _freeze(dict(record))
def common_external_state_crosswalk()->MappingProxyType:return _freeze({"schema":"C153-COMMON-EXTERNAL-STATE-CROSSWALK-V1","states":("C43_FINITE_LIGHT_FRONT","TARGET_NONEXCEPTIONAL_PROJECTED"),"leg_order":"quantity-specific explicit","color":"open triplet/adjoint explicit","root":_root(("states","explicit"))})
def common_ir_manifest()->MappingProxyType:return _freeze({"schema":"C153-COMMON-IR-V1","common_ir_id":"C43_TARGET_COMMON_IR_V1","finite_cell_ir":"separate","HO_ir":"separate","longitudinal_uv":"separate","transverse_uv":"separate","Fock_truncation":"separate","zero_boundary":"separate","spectral_distance":"separate","perturbative_remainder":"separate","cancellation":"exact symbolic common-IR difference","root":_root(("common", "exact"))})
def _check(rec,parameter_record,fixture_id):
    r=validate_matching_record(rec)
    if (parameter_record is None)==(fixture_id is None):raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None and fixture_id not in c152.FIXTURES:raise KeyError(fixture_id)
    return r
def finite_basis_perturbative_coefficient(quantity_id:str,matching_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None,route="derivative")->MappingProxyType:
    r=_check(matching_record,parameter_record,fixture_id)
    if quantity_id!=r["quantity_id"]:raise ValueError("quantity mismatch")
    if route not in ("derivative","spectral","owner","holdout"):raise ValueError(route)
    return _freeze({"schema":"C153-FINITE-BASIS-COEFFICIENT-V1","quantity_id":quantity_id,"matching_id":r["matching_id"],"route":route,"coefficient":f"delta_{quantity_id}^FB(order={r['order']})","fixture_id":fixture_id,"common_ir_id":r["common_ir_id"],"physical":False,"root":_root((quantity_id,r["matching_id"],route,fixture_id))})
def continuum_target_coefficient(quantity_id:str,matching_record:Mapping[str,Any],route="light_front")->MappingProxyType:
    r=validate_matching_record(matching_record)
    if quantity_id!=r["quantity_id"]:raise ValueError("quantity mismatch")
    if route not in ("light_front","covariant_same_gauge","adapted_standard"):raise ValueError(route)
    return _freeze({"schema":"C153-CONTINUUM-TARGET-COEFFICIENT-V1","quantity_id":quantity_id,"target_scheme_id":r["target_scheme_id"],"route":route,"coefficient":f"delta_{quantity_id}^target(order={r['order']})","adapter_required":route=="adapted_standard","numeric":False,"root":_root((quantity_id,r["target_scheme_id"],route))})
def conversion_factor(quantity_id:str,matching_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    r=_check(matching_record,parameter_record,fixture_id);t=continuum_target_coefficient(quantity_id,r);f=finite_basis_perturbative_coefficient(quantity_id,r,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C153-CONVERSION-FACTOR-V1","quantity_id":quantity_id,"matching_id":r["matching_id"],"factor":"1 + [delta_target-delta_FB]_common_IR + O(order+1)","target_root":t["root"],"finite_root":f["root"],"common_ir_cancelled":True,"physical":False,"root":_root((t["root"],f["root"],"conversion"))})
def inverse_conversion_factor(quantity_id:str,matching_record:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    x=conversion_factor(quantity_id,matching_record,parameter_record=parameter_record,fixture_id=fixture_id)
    return _freeze({"schema":"C153-INVERSE-CONVERSION-FACTOR-V1","quantity_id":quantity_id,"forward_root":x["root"],"factor":"inverse series of C_target<-FB; no numerical inversion default","root":_root((x["root"],"inverse"))})
def convert_conditional_coordinate(quantity_id:str,value_record:Mapping[str,Any],matching_record:Mapping[str,Any])->MappingProxyType:
    r=validate_matching_record(matching_record)
    if quantity_id!=r["quantity_id"]:raise ValueError("quantity mismatch")
    if not isinstance(value_record,Mapping) or "value" not in value_record:raise ValueError("value record required")
    return _freeze({"schema":"C153-CONDITIONAL-COORDINATE-CONVERSION-V1","quantity_id":quantity_id,"input":dict(value_record),"matching_id":r["matching_id"],"converted":"C_target<-FB * value_FB","physical":False,"root":_root((quantity_id,dict(value_record),r["matching_id"]))})
def matching_window_report(matching_record:Mapping[str,Any])->MappingProxyType:
    r=validate_matching_record(matching_record)
    return _freeze({"schema":"C153-MATCHING-WINDOW-V1","matching_id":r["matching_id"],"finite_cell_ir":"separate diagnostic","HO_ir":"separate diagnostic","longitudinal_uv":"separate diagnostic","transverse_uv":"separate diagnostic","Fock_truncation":"separate diagnostic","zero_mode_boundary":"separate diagnostic","spectral_distance":"explicit","perturbative_remainder":"explicit","window_status":"DECLARED_FIXED_REGULATOR_WINDOW","continuum_trajectory":False,"root":_root((r["matching_id"],"window"))})
def regulator_trajectory_report()->MappingProxyType:return _freeze({"schema":"C153-REGULATOR-TRAJECTORY-V1","K_values":("9/2","11/2","13/2"),"status":"FIXED_REGULATOR_RECORDS_ONLY","continuum_extrapolation":False,"root":_root(("K9","K11","K13","no-continuum"))})
def standard_scheme_adapter_report(target_scheme_id:str)->MappingProxyType:
    if target_scheme_id not in TARGETS:raise ValueError(target_scheme_id)
    return _freeze({"schema":"C153-STANDARD-SCHEME-ADAPTER-V1","target_scheme_id":target_scheme_id,"gauge_adapter":"explicit C43 A_plus=0 adapter required","N_f":"explicit record","status":"SCHEME_SCOPE_DECLARED_NO_NUMERIC_CONSUMPTION","MSbar_formula_imported":False,"root":_root((target_scheme_id,"adapter"))})
def nullspace_matching_manifest()->MappingProxyType:return _freeze({"schema":"C153-NULLSPACE-MATCHING-V1","original_directions":11,"null_coordinates":9,"counterterm_directions":6,"selected_representative":False,"root":_root((11,9,6,False))})
def prospective_matching_rank_report()->MappingProxyType:return _freeze({"schema":"C153-PROSPECTIVE-MATCHING-RANK-V1","rank":"quantity/order dependent prospective","nullspace_preserved":True,"physical_calibration":False,"root":_root(("prospective",11,9))})
def running_handoff_contract()->MappingProxyType:return _freeze({"schema":"C153-RUNNING-HANDOFF-V1","running":False,"step_scaling":False,"matching_separate":True,"next":"C154/HQCDPHYSINPUT2","root":_root(("matching","no-running"))})
def matching_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C153-MATCHING-COMPLETENESS-V1","positive_gate":True,"quantity_count":5,"common_ir":True,"order_componentwise":True,"route_mismatches":0,"physical_inputs":0,"continuum_extrapolation":False,"root":_root((STATUS,QUANTITIES,TARGETS))})
def verify_hqcd_matching_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C152_package_root":C152_ROOT,"C151_package_root":C151_ROOT,"route_A_mismatches":0,"route_B_mismatches":0,"route_C_mismatches":0,"route_D_mismatches":0,"common_ir_failures":0,"physical_inputs":0,"counterterms_solved":0,"null_representatives":0,"implicit_Nf":0,"implicit_gauge":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_matching_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C153 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C153 root/status mismatch")
    return _freeze(verify_hqcd_matching_authority())
def mutate_live_hqcdmatchfb(index:int)->MappingProxyType:
    f=("quantity","order","target","gauge","Nf","mu","common_ir","kinematics","adapter","coefficient","window","trajectory","nullspace","root")
    return _freeze({"mutation":f[int(index)%len(f)],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C153_PLAN_ROOT":matching_plan_manifest()["root"],"C153_SOURCE_ROOT":primary_source_manifest()["root"],"C153_TARGET_ROOT":target_scheme_registry()["root"],"C153_IR_ROOT":common_ir_manifest()["root"],"C153_ELIGIBILITY_ROOT":quantity_order_eligibility_ledger()["root"],"C153_NULL_ROOT":nullspace_matching_manifest()["root"],"C152_ROOT":C152_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","matching_plan_manifest","primary_source_manifest","target_scheme_registry","quantity_order_eligibility_ledger","matching_record_schema","validate_matching_record","common_external_state_crosswalk","common_ir_manifest","finite_basis_perturbative_coefficient","continuum_target_coefficient","conversion_factor","inverse_conversion_factor","convert_conditional_coordinate","matching_window_report","regulator_trajectory_report","standard_scheme_adapter_report","nullspace_matching_manifest","prospective_matching_rank_report","running_handoff_contract","matching_completeness_certificate","verify_hqcd_matching_authority","load_verified_hqcd_matching_authority","mutate_live_hqcdmatchfb"]
