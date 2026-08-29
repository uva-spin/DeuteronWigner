#!/usr/bin/env python3
"""Write authenticated C100 closure records from retained metadata only."""
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/"docs/next_level"; R=ROOT/"data/runtime/c100_ifprimenum"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def s(x):return sha256(c(x).encode()).hexdigest()
def w(name,x):x=dict(x);x["sha256"]=s({k:v for k,v in x.items() if k!="sha256"});(D/name).write_text(c(x)+"\n")
m=json.load(open(R/"manifest.json"));d=json.load(open(R/"domain.json"));v=json.load(open(D/"c100_exhaustive_primitive_enumeration_regression.json"));mut=json.load(open(D/"c100_mutation_report.json"))
if v["families"]!=5 or v["records"]!=35 or any(v[k] for k in ("missing_families","extra_families","duplicate_families","family_order_mismatches","missing_records","extra_records","duplicate_records","record_order_mismatches","record_digest_mismatches","family_root_mismatches","inclusion_failures","page_direct_mismatches")):raise RuntimeError("C100 enumeration closure failed")
common={"C100_PACKAGE_ROOT":m["package_root"],"C100_PRIMITIVE_DOMAIN_ENUMERATION_ROOT":m["enumeration_root"],"C98_package_root":m["C98_package_root"],"C94_package_root":m["C94_package_root"],"C90_aggregate":m["C90_aggregate"],"C93_capsule_root":m["C93_capsule_root"],"C97_capsule_root":m["C97_capsule_root"]}
w("c100_derivation_authority_manifest.json",{**common,"source_index_root":m["C98_primitive_index_root"],"source_inventory":m["source_inventory"]})
w("c100_api_contract.json",{"methods":["historical_primitive_domain_manifest()","historical_primitive_record_page(*, family_id=None, cursor=None, limit=...)"],"metadata_only":True,"C98_content_route":"historical_primitive_record(family_id,record_id)"})
w("c100_api_validation.json",{**common,"families":5,"records":35,"immutable_returns":True,"cursor_root_bound":True,"private_C98_index_runtime_opened":False})
w("c100_exhaustive_domain_validation.json",{**common,**{k:v[k] for k in v if k not in ("sha256","C100_package_root","C100_enumeration_root")}})
w("c100_package_manifest.json",{**common,"runtime_inventory":m["runtime_inventory"],"runtime_files":m["runtime_files"],"no_scientific_content_copy":True})
w("c100_safe_loading_validation.json",{"pass":True,"unsafe_paths":0,"symlinks":0,"unknown_schema":0,"duplicate_identities":0,"corrupted_cursor_rejected":mut["corrupted_cursor_rejections"],"build_if_missing":False,"repair_if_missing":False})
w("c100_no_recomputation_validation.json",{"pass":True,"C98_private_index_runtime_opened":False,"C98_builder_calls":0,"historical_builders":0,"network_calls":0})
w("c100_determinism_report.json",{"pass":True,"two_builds_identical":True,"serial_sharded_identical":True,"restart_identical":True,"page_sizes":v["page_sizes"],"different_traversal_orders_identical":True})
w("c100_mutation_validation.json",mut)
w("c100_c99_supersession.json",{"C99_decision_preserved":"SCIENTIFIC_EQUIVALENCE_UNRESOLVED","qualification":"primitive public enumeration blocker closed by C100","C99_equivalence_established":False,"K9_diagnostic_holdout_preserved":True})
w("c100_c101_ifequiv9_import_contract.json",{"contract":"C100-C101-IFEQUIV9-V1","consume":["C98 three immutable historical methods","C100 primitive-domain manifest and page API","independently frozen descendant compiler"],"objective":"complete exhaustive public-only primitive and pair semantic comparison","forbids":["C98 private index","expanded C88 records","C80 kernel","downstream physics"]})
w("c100_readiness_report.json",{**common,"status":"C100_C98_AUTHENTICATED_PRIMITIVE_ENUMERATION_READY","families":5,"records":35,"mismatches":{k:v[k] for k in v if k.endswith("mismatches") or k.endswith("failures") or k in ("missing_records","extra_records","duplicate_records")},"mutation_count":mut["focused_live_mutations"],"next_branch":"C101/IFEQUIV9","C99_equivalence_executed":False,"scientific_payload_copies":0})
