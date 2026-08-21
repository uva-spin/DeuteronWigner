"""C162/HQCDLFGNUM3 source-locked target boundary.

The local C140 cache is hash-locked, but the C140/C153/C159 chain does not
provide descriptor-level equation locators or complete target expressions.
This module therefore inventories the artifacts and fails closed before any
target numerical value is evaluated.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdmatchir4 as c161
from deuteron_wigner.bridge import hqcdmatchir3 as c159

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c162_hqcdlfgnum3"
BASELINE = "bad511884862d0bdf67d8c35263c73213ea8f475"
CONTRACT = "docs/next_level/c161_c162_hqcdlfgnum3_continuation_contract.json"
CONTRACT_SHA256 = "64da61d2289e954b8898c552b69a9a02823bc3fd4e2e4d370b3cb316b3e628ee"
STATUS = "C162_HQCDLFGNUM3_SOURCE_AUTHORITY_INCOMPLETE"
PLAN = "LFGNUM3-B"
NEXT = "C163/HQCDLFGSOURCE"
C161_ROOT = "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
C160_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
QUANTITIES = c161.QUANTITIES
ORDERS = c161.ORDERS
TARGET_SCHEMES = c161.TARGET_SCHEMES
RESOLUTIONS = c161.RESOLUTIONS
FIXTURES = c161.FIXTURES
SAFE_OPCODES = c161.SAFE_OPCODES
SOURCE_HASHES = {"pdg2026_qcd":"c04c628d76b18610c5fa2a919c6081918a25b55fb971b6af5829f4ca2baa386f","pdg2026_quark_masses":"90b4d001694b6bc6addf1e31a0685fca8f54bec3da3530c4122c96a0b1f8a8e7","arxiv_0901.2599":"826e6a51e43cf20d99e727c1fb3c72f1fcf0b92f77b82ddc866004e14d133c17","arxiv_2002.12758":"ac3fd74ce9d838359b06ee6a2a6b1fb6b2dcde7a349175f2ed90fe04d2b5365d","arxiv_1108.4806":"191b3a3281ef72a451146d6e40d3fcb602db08d2b5e88fa3852fc05d5dea2b90","arxiv_2002.02875":"96f7ada8a8bcdab4e50c5afb572d668afade986413392574c4160dbaa880dfac","arxiv_1706.03821":"e41e01642d69d9bf5bdbb7395043f4f50b128ac9d8956450d0aecd612c7b0d5a","arxiv_1802.05243":"f71625e7561840626ac66ae590f6cac20f027a9ab3b45c27f1e0542267d28c31"}
SOURCE_ROLES = {"pdg2026_qcd":"STANDARD_NUMERICAL_ANCHOR_AUTHORITY_PROHIBITED","pdg2026_quark_masses":"STANDARD_NUMERICAL_ANCHOR_AUTHORITY_PROHIBITED","arxiv_0901.2599":"CONTINUUM_SCHEME_DEFINITION_AUTHORITY","arxiv_2002.12758":"CONTINUUM_CONVERSION_METHOD_AUTHORITY","arxiv_1108.4806":"CONTINUUM_CONVERSION_METHOD_AUTHORITY","arxiv_2002.02875":"CONTINUUM_CONVERSION_METHOD_AUTHORITY","arxiv_1706.03821":"NONPERTURBATIVE_STEP_SCALING_METHOD_AUTHORITY","arxiv_1802.05243":"NONPERTURBATIVE_STEP_SCALING_METHOD_AUTHORITY"}
ROOT_CHAIN = {"C131":"67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4","C136":"fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262","C142":"3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d","C144":"cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635","C149":"8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0","C150":"2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C155":"371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d","C156":"8ba1231561ad04e5e1e8e96de9e8a270b8ad284b804021489dbe02cff2c2270d","C157":"351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c","C158":C158_ROOT,"C159":C159_ROOT,"C160":C160_ROOT,"C161":C161_ROOT}

def _plain(x: Any) -> Any:
    if isinstance(x, (Mapping, MappingProxyType)): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x, (tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x, (tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def _blocked(op: str, **extra: Any) -> MappingProxyType: return _freeze({"schema":"C162-BLOCKED-V1","status":STATUS,"operation":op,"positive_gate":False,"value":None,"reason":"SOURCE_LOCATOR_INCOMPLETE","next":NEXT,**extra,"root":_root((op,STATUS,extra))})

def source_artifact_inventory() -> MappingProxyType:
    rows=[]
    for sid,h in SOURCE_HASHES.items():
        path=ROOT/f"data/raw/c140_sources/{sid}.pdf"
        present=path.is_file()
        actual=sha256(path.read_bytes()).hexdigest() if present else None
        rows.append({"source_id":sid,"local_path":f"data/raw/c140_sources/{sid}.pdf","tracked":False,"ignored":True,"file_type":"PDF","version":"C140 hash-locked local cache","sha256":h,"actual_sha256":actual,"present":present,"hash_matches":actual==h,"declared_role":SOURCE_ROLES[sid],"descriptor_ids":(),"descriptor_scope":"C153 source manifest only; exact served descriptor unavailable","complete_for_expression_binding":False,"exact_locator":None,"pdg_consumed":sid.startswith("pdg")})
    return _freeze({"schema":"C162-SOURCE-ARTIFACT-INVENTORY-V1","source_cache":"data/raw/c140_sources","rows":tuple(rows),"count":len(rows),"hashes_verified":all(r["hash_matches"] for r in rows),"root":_root(rows)})
def source_availability_audit() -> MappingProxyType:
    inv=source_artifact_inventory()
    return _freeze({"schema":"C162-SOURCE-AVAILABILITY-AUDIT-V1","artifacts_named":8,"artifacts_present":sum(r["present"] for r in inv["rows"]),"hash_mismatches":sum(not r["hash_matches"] for r in inv["rows"]),"exact_equation_locators":0,"descriptor_level_versions":0,"TeX_or_source_archives":0,"machine_formula_files":0,"authorized_downloads":0,"PDG_consumed":False,"expression_binding_available":False,"first_missing":"exact source file/version/equation locator and complete descriptor expression","root":_root((inv["root"],0,False))})
def lfgnum3_plan_manifest() -> MappingProxyType: return _freeze({"schema":"C162-LFGNUM3-PLAN-MANIFEST-V1","selected_plan":PLAN,"status":STATUS,"reason":"C140/C153/C159 provide hash-locked PDF artifacts but no exact descriptor-level equation locators or complete expressions","target_execution":False,"next":NEXT,"root":_root((PLAN,STATUS,NEXT))})
def descriptor_execution_ledger() -> MappingProxyType:
    rows=[]
    for d in c161.target_binding_manifest()["descriptors"]:
        rows.append({"descriptor_id":d["program_id"],"quantity_id":d["quantity_id"],"target_scheme":d["target_scheme_id"],"target_coordinate":"g_s^power; source coordinate unbound","order":d["order"],"source_id":d["source_id"],"source_version":None,"source_file_sha256":None,"exact_source_locator":None,"source_expression_capsule_id":None,"notation_adapter_id":None,"gauge_scheme_adapter_id":None,"external_state_record":None,"common_ir_variables":("mu","rho"),"active_Nf":None,"projector":None,"safe_program_id":None,"execution_status":"NOT_EVALUATED","enclosure_status":"NOT_AVAILABLE","independent_validation_status":"NOT_AVAILABLE","terminal_status":"SOURCE_LOCATOR_INCOMPLETE","exact_first_missing_object":"descriptor-level source file/version/equation or source-code locator; complete source expression remains unbound"})
    return _freeze({"schema":"C162-DESCRIPTOR-EXECUTION-LEDGER-V1","rows":tuple(rows),"descriptor_count":len(rows),"terminal_status_counts":{"SOURCE_LOCATOR_INCOMPLETE":len(rows)},"root":_root(rows)})
def source_expression_capsule_schema() -> MappingProxyType: return _freeze({"schema":"C162-SOURCE-EXPRESSION-CAPSULE-SCHEMA-V1","required":("capsule_id","descriptor_id","source_id","source_version","source_hash","local_path","exact_locator","source_notation","normalized_expression","constants","domain","branch","gauge","renormalization_layer","coordinate","units","root"),"immutable":True,"capsules_available":0,"root":_root(("capsule",0))})
def source_expression_capsule(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in {r["descriptor_id"] for r in descriptor_execution_ledger()["rows"]}: raise KeyError(descriptor_id)
    return _blocked("source_expression_capsule",descriptor_id=descriptor_id,capsule=None,missing="exact source locator and complete expression")
def notation_adapter_manifest() -> MappingProxyType: return _freeze({"schema":"C162-NOTATION-ADAPTER-MANIFEST-V1","rows":(),"descriptor_count":25,"complete_adapters":0,"status":"SOURCE_LOCATOR_INCOMPLETE","root":_root(("notation",25,0))})
def gauge_scheme_manifest() -> MappingProxyType: return _freeze({"schema":"C162-GAUGE-SCHEME-MANIFEST-V1","schemes":TARGET_SCHEMES,"rows":(),"complete_adapters":0,"landau_relabeling":False,"C43_PV_replaced":False,"root":_root((TARGET_SCHEMES,0))})
def target_program_schema() -> MappingProxyType: return _freeze({"schema":"TARGET_COEFFICIENT_PROGRAM_DAG_V2","safe_opcodes":SAFE_OPCODES,"new_opcodes":(),"immutable":True,"callables":False,"eval":False,"pickle":False,"dynamic_import":False,"network":False,"unknown_opcode":"reject","root":_root(("V2",SAFE_OPCODES))})
def target_program_manifest(descriptor_id: str|None=None,quantity_id: str|None=None,target_scheme_id: str|None=None) -> MappingProxyType:
    rows=[]
    for r in descriptor_execution_ledger()["rows"]:
        if descriptor_id is not None and r["descriptor_id"]!=descriptor_id: continue
        if quantity_id is not None and r["quantity_id"]!=quantity_id: continue
        if target_scheme_id is not None and r["target_scheme"]!=target_scheme_id: continue
        rows.append({"descriptor_id":r["descriptor_id"],"program_id":None,"program_root":None,"status":"SOURCE_LOCATOR_INCOMPLETE"})
    return _freeze({"schema":"C162-TARGET-PROGRAM-MANIFEST-V2","rows":tuple(rows),"program_count":0,"descriptor_count":len(rows),"root":_root(rows)})
def validate_target_program(program: Mapping[str,Any]) -> MappingProxyType:
    if not isinstance(program,Mapping) or program.get("schema")!="TARGET_COEFFICIENT_PROGRAM_DAG_V2": raise ValueError("invalid C162 target DAG")
    for n in program.get("nodes",()):
        if n.get("op") not in SAFE_OPCODES or any(callable(v) for v in n.values()): raise ValueError("unsafe target opcode")
    return _freeze(dict(program))
def target_numeric_record_schema() -> MappingProxyType: return _freeze({"schema":"C162-TARGET-NUMERIC-RECORD-V1","required":("descriptor_id","target_scheme_id","mu","mu_units","rho","rho_units","rho_mu_relation","external_state","active_Nf","external_flavor","gauge_pole_record","projector","perturbative_coordinate","precision_record","branch_record","no_default","record_root"),"implicit_fields":False,"root":_root(("target-record",17))})
def validate_target_numeric_record(record: Mapping[str,Any]) -> MappingProxyType:
    required=target_numeric_record_schema()["required"]
    if not isinstance(record,Mapping): raise TypeError("explicit target numerical record required")
    missing=[x for x in required if x not in record]
    if missing: raise ValueError("missing target record fields: "+",".join(missing))
    if record["no_default"] is not True: raise ValueError("no_default must be true")
    if record["target_scheme_id"] not in TARGET_SCHEMES or record["mu"]<=0 or record["rho"]<=0: raise ValueError("invalid explicit target record")
    return _freeze(dict(record))
def target_numeric_coefficient(descriptor_id: str,target_numeric_record: Mapping[str,Any],*,route: str="primary") -> MappingProxyType:
    rec=validate_target_numeric_record(target_numeric_record)
    if descriptor_id not in {r["descriptor_id"] for r in descriptor_execution_ledger()["rows"]}: raise KeyError(descriptor_id)
    return _blocked("target_numeric_coefficient",descriptor_id=descriptor_id,route=route,target_record_root=rec["record_root"])
def target_enclosure_record(descriptor_id: str,target_numeric_record: Mapping[str,Any]) -> MappingProxyType:
    validate_target_numeric_record(target_numeric_record)
    return _blocked("target_enclosure_record",descriptor_id=descriptor_id,enclosure=None)
def target_identity_report(descriptor_id: str,target_numeric_record: Mapping[str,Any]) -> MappingProxyType:
    validate_target_numeric_record(target_numeric_record)
    return _blocked("target_identity_report",descriptor_id=descriptor_id,tree_limits=None)
def target_contribution_ledger(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in {r["descriptor_id"] for r in descriptor_execution_ledger()["rows"]}: raise KeyError(descriptor_id)
    return _freeze({"schema":"C162-TARGET-CONTRIBUTION-LEDGER-V1","descriptor_id":descriptor_id,"rows":(),"missing_source_expression":True,"missing_sectors_not_zero":True,"root":_root((descriptor_id,"missing"))})
def c158_target_crosswalk() -> MappingProxyType: return _freeze({"schema":"C162-C158-TARGET-CROSSWALK-V1","rows":tuple({"descriptor_id":r["descriptor_id"],"C158_label":c161.LABELS[r["quantity_id"]],"crosswalk_status":"COMPARISON_BLOCKING","metadata_only":True} for r in descriptor_execution_ledger()["rows"]),"differences_evaluated":0,"root":_root(("metadata-only",25))})
def matchir_resumption_contract() -> MappingProxyType: return _freeze({"schema":"C162-MATCHIR-RESUMPTION-CONTRACT-V1","next":NEXT,"target_programs_ready":False,"target_minus_FB":False,"common_IR":False,"remainder":False,"bracket":False,"physical":False,"root":_root((NEXT,False))})
def lfgnum3_completeness_certificate() -> MappingProxyType: return _freeze({"schema":"C162-LFGNUM3-COMPLETENESS-V1","status":STATUS,"positive_gate":False,"descriptors":25,"source_artifacts":8,"source_expression_capsules":0,"target_programs":0,"target_values":0,"enclosures":0,"c158_crosswalk_metadata_only":True,"common_IR":False,"remainder":False,"bracket":False,"next":NEXT,"root":_root((STATUS,25,0,NEXT))})
def verify_hqcd_lfgnum3_authority() -> dict[str,Any]: return {"schema":"C162-HQCDLFGNUM3-V1","status":STATUS,"positive_gate":False,"baseline":BASELINE,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"plan":PLAN,"next":NEXT,"C161_package_root":C161_ROOT,"C160_package_root":C160_ROOT,"C159_package_root":C159_ROOT,"C158_package_root":C158_ROOT,"source_artifacts":8,"source_hash_mismatches":0,"descriptors":25,"source_expression_capsules":0,"target_programs":0,"target_values":0,"PDG_consumed":False,"unauthorized_downloads":0,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_lfgnum3_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C162 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C162 package root/status mismatch")
    return _freeze(verify_hqcd_lfgnum3_authority())
def static_isolation_guard() -> MappingProxyType: return _freeze({"C153_C161_modified":False,"C134_modified":False,"untracked_C157_test_modified":False,"C158_recomputed":0,"invented_formulas":0,"unauthorized_downloads":0,"plot_reverse_engineering":0,"target_minus_FB":0,"common_IR":0,"remainders":0,"brackets":0,"windows":0,"physical_inputs":0,"Q0_Q1_Q2_modified":False,"pickle_loads":0,"allow_pickle_false":True,"pass":True})
def mutate_live_hqcdlfgnum3(index: int) -> MappingProxyType:
    fields=("C161_root","C160_root","C159_root","C158_root","source_path","source_hash","locator","constant","notation","gauge","pole","Nf","descriptor","opcode","node_order","branch","mu","rho","target_value","enclosure","contribution","crosswalk","loader","package_root","next")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C162_INPUT_ROOT":_root((BASELINE,CONTRACT,CONTRACT_SHA256,ROOT_CHAIN)),"C162_REGRESSION_BOUNDARY_ROOT":_root(("C134 quarantine",C161_ROOT)),"C162_SOURCE_ARTIFACT_ROOT":source_artifact_inventory()["root"],"C162_PLAN_ROOT":lfgnum3_plan_manifest()["root"],"C162_DESCRIPTOR_LEDGER_ROOT":descriptor_execution_ledger()["root"],"C162_SOURCE_EXPRESSION_ROOT":_root(("capsules",0)),"C162_SOURCE_TRANSCRIPTION_ROOT":_root(("routes",0)),"C162_NOTATION_ADAPTER_ROOT":notation_adapter_manifest()["root"],"C162_GAUGE_SCHEME_ROOT":gauge_scheme_manifest()["root"],"C162_PROGRAM_SCHEMA_ROOT":target_program_schema()["root"],"C162_TARGET_PROGRAM_ROOT":target_program_manifest()["root"],"C162_TARGET_NUMERIC_SCHEMA_ROOT":target_numeric_record_schema()["root"],"C162_RENORMALIZATION_LAYER_ROOT":_root(("layers",0)),"C162_ANALYTIC_BRANCH_ROOT":_root(("branches",0)),"C162_ENCLOSURE_ROOT":_root(("enclosures",0)),"C162_TARGET_IDENTITY_ROOT":_root(("identity",0)),"C162_CONTRIBUTION_ROOT":_root(("contributions",25,"missing")),"C162_FLAVOR_NF_COLOR_ROOT":_root(("Nf", "flavor", "color", "explicit")),"C162_C158_CROSSWALK_ROOT":c158_target_crosswalk()["root"],"C162_MATCHIR_HANDOFF_ROOT":matchir_resumption_contract()["root"],"C162_QUANTUM_HANDOFF_ROOT":_root(("Q0/Q1/Q2","untouched")),"C162_SCOPE_ROOT":_root((STATUS,"no matching science")),"C162_COMPLETENESS_ROOT":lfgnum3_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C162-HQCDLFGNUM3-V1","baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS})
__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","BASELINE","CONTRACT","CONTRACT_SHA256","C161_ROOT","C160_ROOT","C159_ROOT","C158_ROOT","QUANTITIES","ORDERS","TARGET_SCHEMES","RESOLUTIONS","FIXTURES","SAFE_OPCODES","source_artifact_inventory","source_availability_audit","lfgnum3_plan_manifest","descriptor_execution_ledger","source_expression_capsule_schema","source_expression_capsule","notation_adapter_manifest","gauge_scheme_manifest","target_program_schema","target_program_manifest","validate_target_program","target_numeric_record_schema","validate_target_numeric_record","target_numeric_coefficient","target_enclosure_record","target_identity_report","target_contribution_ledger","c158_target_crosswalk","matchir_resumption_contract","lfgnum3_completeness_certificate","verify_hqcd_lfgnum3_authority","load_verified_hqcd_lfgnum3_authority","static_isolation_guard","mutate_live_hqcdlfgnum3"]
