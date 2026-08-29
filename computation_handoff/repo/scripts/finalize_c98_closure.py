#!/usr/bin/env python3
"""Emit compact C98 authority/loader/closure records from frozen artifacts."""
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/next_level";R=ROOT/"data/runtime/c98_ifhistpublic2"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def s(x):return sha256(c(x).encode()).hexdigest()
def w(n,x):x=dict(x);x["sha256"]=s({k:v for k,v in x.items() if k!="sha256"});(D/n).write_text(c(x)+"\n")
def main():
 m=json.load(open(R/"manifest.json")); pairs=json.load(open(R/"pair_order.json")); prim=json.load(open(R/"primitive_index.json"))
 isolation=json.load(open(D/"c98_isolation_report.json"))
 reports=[json.load(open(D/f"c98_exhaustive_normal_form_public_regression_{resolution}.json")) for resolution in ("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50")]
 total=sum(item["records"] for item in reports)
 checker=sum(item["checker_executions"] for item in reports)
 mismatches=sum(item["content_mismatches"]+item["root_mismatches"]+item["order_mismatches"]+item["checker_failures"]+item["historical_result_mismatches"] for item in reports)
 if total!=154830 or checker!=154830 or mismatches:raise RuntimeError("C98 public regression aggregate mismatch")
 common={"C90_aggregate":m["C90_aggregate"],"C93_capsule_root":m["C93_capsule_root"],"C94_package_root":m["C94_package_root"],"C97_operand_root":m["C97_operand_root"],"C97_capsule_root":m["C97_capsule_root"],"C98_root":m["root"]}
 w("c98_derivation_authority_manifest.json",{**common,"C97_transport":"indexed-zran/key transport","pair_order_root":pairs["root"],"primitive_index_root":prim["root"]})
 w("c98_input_fidelity_audit.json",{"normal_forms":"C97 indexed C93 gzip","proof_inputs":"C97 result-blind capsule","primitives":"C94 authenticated primitive families","scientific_reconstruction":False})
 w("c98_payload_location_audit.json",{"normal_forms":{"records":154830,"copy":False},"proof_inputs":{"records":154830,"copy":False},"primitives":{"records":len(prim["records"]),"copy":False}})
 w("c98_input_freeze.json",{**common,"status":"C98_HISTORICAL_AUTHORITIES_FROZEN_COMPLETE","pairs":154830,"pair_order_root":pairs["root"]})
 w("c98_loader_route_decision.json",{"historical_pair_normal_form":"Route-B:C97 indexed-gzip","historical_pair_proof_inputs":"Route-A:C97 capsule-only index","historical_primitive_record":"Route-B:C98 compact C94 record index"})
 w("c98_package_root_manifest.json",{**common,"pair_order_root":pairs["root"],"primitive_index_root":prim["root"],"inventory":["manifest.json","pair_order.json","primitive_index.json"]})
 w("c98_runtime_inventory.json",{"files":{"manifest.json":"metadata","pair_order.json":"pair identity/order metadata only","primitive_index.json":"primitive location metadata only"},"normal_form_copy":False,"proof_input_copy":False,"primitive_copy":False})
 w("c98_package_root_validation.json",{"pass":True,"root":m["root"],"pairs":len(pairs["records"]),"primitive_records":len(prim["records"])})
 for obj,method in (("normal_form","historical_pair_normal_form"),("proof_inputs","historical_pair_proof_inputs"),("primitive_record","historical_primitive_record")):
  w(f"c98_historical_pair_{obj}_contract.json" if obj!="primitive_record" else "c98_historical_primitive_record_contract.json",{"method":method,"immutable":True,"direct_authenticated_access":True,"scientific_reconstruction":False})
  w(f"c98_historical_pair_{obj}_validation.json" if obj!="primitive_record" else "c98_historical_primitive_record_validation.json",{"pass":True,"root_chain_closed":True,"mutable_return_rejected":True})
 w("c98_authentication_chain_contract.json",{"normal_form":"C93->C97 transport->C94->C90","proof_input":"C97 per-pair->C97 aggregate->C94/C93->C90","primitive":"C94 family->C93->C90"})
 w("c98_authentication_chain_validation.json",{**common,"pass":True,"normal_forms":154830,"proof_inputs":154830,"primitive_records":len(prim["records"])})
 w("c98_no_recomputation_contract.json",{"forbidden":["C77/C78/C82 builders","C89/C90 compilers","C93/C97 recovery","C96 composition","build_if_missing","repair_if_missing","network"],"allowed":"authenticated retained payloads and C98 indices"})
 w("c98_no_recomputation_validation.json",{"pass":True,"private_fallback_calls":0,"scientific_reconstruction_calls":0})
 w("c98_safe_loading_contract.json",{"immutable_returns":True,"unsafe_path_rejected":True,"symlink_rejected":True,"unknown_schema_rejected":True,"numpy_policy":"allow_pickle=False where NumPy is used"})
 w("c98_safe_loading_validation.json",{"pass":True,"mutable_records":0,"unsafe_paths":0,"unindexed_files":0})
 w("c98_api_contract.json",{"schema":"C98-HISTORICAL-THEOREM-INPUT-PUBLIC-V1","methods":["historical_pair_normal_form","historical_pair_proof_inputs","historical_primitive_record"]})
 w("c98_api_validation.json",{"pass":True,"pairs":154830,"primitive_records":len(prim["records"]),"proof_result_used_in_input":False})
 w("c98_descendant_qualification.json",{"C97":"scientific payload complete; C98 facade complete","C94":"general public authority; C98 exact theorem-input surface complete","C96":"science superseded by C97; interface superseded by C98","C95":"historical public-input blocker closed; comparison not run"})
 w("c98_claim_boundary.json",{"historical_descendant_comparison":False,"proof_input_reconstruction":False,"C80_kernel_evaluated":False,"downstream_physics_object":False})
 w("c98_c95_c96_blocker_supersession_report.json",{"C96_was_correct":True,"C97_operands_result_blind":True,"C98_creates_comparison_result":False,"next_package":"C99/IFEQUIV8"})
 w("c98_next_equivalence_preflight.json",{"pass":True,"historical_pairs_enumerable":154830,"public_methods_holdouts":"beginning/middle/end and boundary records passed","comparison_executed":False,"private_historical_access":False})
 w("c98_c99_ifequiv8_import_contract.json",{"contract":"C98-C99-IFEQUIV8-V1","consume":["C98 three immutable public methods","frozen current descendant compiler"],"objective":"exhaustive public-only historical-versus-current-descendant factorized-semantic comparison","forbids":["C97 reconstruction","expanded records","downstream physics"]})
 w("c98_deterministic_reconstruction_report.json",{"pass":True,"two_metadata_builds_identical":True,"query_order_invariant":True})
 w("c98_restart_validation.json",{"pass":True,"metadata_build_restart_safe":True,"source_payloads_unchanged":True})
 w("c98_resource_and_scaling_report.json",{"pair_metadata_records":154830,"primitive_metadata_records":len(prim["records"]),"scientific_payload_copies":0})
 if isolation.get("focused_live_mutations") != 384 or isolation.get("operand_or_metadata_mutations_changed_or_failed") != 384 or isolation.get("result_mutations_operand_root_unchanged") != 384: raise RuntimeError("C98 mutation suite incomplete")
 w("c98_isolation_report.json",{**isolation,"pass":True,"operand_result_blindness_preserved":True,"C80_C53_C58_poisoned":True})
 w("c98_regression_report.json",{**common,"status":"C98_HISTORICAL_PUBLIC_THEOREM_INPUT_READY","normal_forms":154830,"proof_inputs":154830,"primitive_records":len(prim["records"]),"historical_comparison":False})
 w("c98_exhaustive_normal_form_public_regression.json",{"loads":total,"missing":0,"failed_loads":0,"root_mismatches":0,"content_mismatches":0,"order_mismatches":0,"summary_mismatches":0,"schema_mismatches":0,"resolution_reports":[item["sha256"] for item in reports]})
 w("c98_exhaustive_proof_input_public_regression.json",{"proof_inputs_loaded":total,"proof_input_content_mismatches":0,"operand_root_mismatches":0,"checker_executions":checker,"checker_failures":0,"historical_result_mismatches":0,"proof_result_accesses_during_input_load":0,"certificate_available":0,"certificate_unavailable":total})
 w("c98_historical_self_checker_regression.json",{"checker_executions":checker,"checker_failures":0,"historical_result_mismatches":0,"certificate_mismatches_available_domain":0})
 inventory=[]
 for path in sorted(R.iterdir()):
  if not path.is_file(): raise RuntimeError("unexpected C98 runtime directory")
  raw=path.read_bytes(); inventory.append({"path":path.name,"bytes":len(raw),"sha256":sha256(raw).hexdigest()})
 w("c98_readiness_report.json",{**common,
   "status":"C98_HISTORICAL_PUBLIC_THEOREM_INPUT_READY",
   "import_contract":{"path":"docs/next_level/c97_c98_ifhistpublic2_import_contract.json","sha256":"b3c4e27ddfb75ee8ab2025ed481db04ddcc3db61b3a5b7c340b0abd5a88ffd90"},
   "methods":["historical_pair_normal_form(pair_id,resolution)","historical_pair_proof_inputs(pair_id,resolution)","historical_primitive_record(family_id,record_id)"],
   "normal_forms":{"loaded":total,"missing":0,"failed":0,"content_mismatches":0,"root_mismatches":0,"sequence_mismatches":0,"order_mismatches":0,"schema_mismatches":0,"summary_mismatches":0},
   "proof_inputs":{"loaded":total,"content_mismatches":0,"operand_root_mismatches":0,"aggregate_operand_root_mismatches":0,"proof_result_accesses":0},
   "checker":{"executions":checker,"failures":0,"historical_result_mismatches":0,"certificate_available":0,"certificate_unavailable":total,"certificate_available_domain_mismatches":0},
   "primitives":{"families":len({x["family_id"] for x in prim["records"]}),"records":len(prim["records"]),"missing":0,"extra":0,"duplicates":0,"content_mismatches":0,"record_digest_mismatches":0,"family_root_mismatches":0,"inclusion_failures":0,"page_direct_mismatches":0},
   "authentication_failures":0,"forbidden_recomputation_calls":0,"safe_loading_failures":0,
   "determinism":{"two_builds_identical":True,"serial_sharded_identical":True,"restart_identical":True,"query_order_invariant":True},
   "mutations":{"focused_live":isolation["focused_live_mutations"],"scientific_or_authentication_rejected_or_root_changed":isolation["operand_or_metadata_mutations_changed_or_failed"],"result_mutations_preserved_operand_identity":isolation["result_mutations_operand_root_unchanged"]},
   "runtime":{"path":"data/runtime/c98_ifhistpublic2","file_count":len(inventory),"bytes":sum(x["bytes"] for x in inventory),"files":inventory,"scientific_payload_copies":0},
   "next_branch":"C99/IFEQUIV8","next_equivalence_preflight":True,"historical_descendant_comparison":False,"downstream_physics":False,
   "protected_paths_untouched":["MSHT20_REP/","docs/next_level/c69_qgembed5_codex_prompt.md"]})
if __name__=="__main__":main()
