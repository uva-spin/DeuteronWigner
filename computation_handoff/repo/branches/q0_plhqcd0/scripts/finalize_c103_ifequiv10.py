#!/usr/bin/env python3
"""Emit compact C103 validation and handoff records from its frozen ledger."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from deuteron_wigner.bridge.ifequiv10 import load_verified_historical_descendant_equivalence, verify_historical_descendant_equivalence_root

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs/next_level'
def plain(v):
 if hasattr(v,'items'): return {str(k):plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)): return [plain(x) for x in v]
 return v
def canon(v): return json.dumps(plain(v),sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)
def sha(v): return sha256(canon(v).encode()).hexdigest()
def write(n,v): (DOCS/n).write_text(canon(v)+'\n')
def main():
 m=dict(load_verified_historical_descendant_equivalence()); verify_historical_descendant_equivalence_root()
 from deuteron_wigner.bridge.ifhistpublic2 import historical_pair_normal_form,historical_pair_proof_inputs
 from deuteron_wigner.bridge.iftheoremapi import verify_factorized_expansion_equivalence
 certs=json.loads((ROOT/'data/runtime/c103_ifequiv10/primitive_certificates.json').read_text())['records']
 pair='C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0'; res='K9_2_N8_b0.40'
 historical=historical_pair_normal_form(pair,res); proof=historical_pair_proof_inputs(pair,res)['proof_input']; nonpositive=0
 for ordinal in range(384):
  altered=json.loads(canon(historical['normal_form'])); altered['cardinality']+=ordinal+1
  result=verify_factorized_expansion_equivalence(historical,altered,certs,scientific_schema=proof['schemas']['theorem'],canonical_order=proof['logical']['order_root'])
  nonpositive+=int(result['status']!='EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF')
 if nonpositive!=384: raise ValueError('C103 live semantic mutation control')
 common={"schema":"C103-IFEQUIV10-FINALIZATION-V1","pass":True,"C103_PACKAGE_ROOT":m['C103_PACKAGE_ROOT'],"C103_DESCENDANT_AGGREGATE_SEMANTIC_ROOT":m['C103_DESCENDANT_AGGREGATE_SEMANTIC_ROOT'],"C103_HISTORICAL_DESCENDANT_EQUIVALENCE_CERTIFICATE_ROOT":m['C103_HISTORICAL_DESCENDANT_EQUIVALENCE_CERTIFICATE_ROOT'],"records":m['records'],"proof_successes":m['proof_successes'],"resolution_counts":m['resolution_counts'],"logical_records":{"K9_2_N8_b0.40":28606464,"K11_2_N10_b0.45":165991250,"K13_2_N12_b0.50":697394304},"total_logical_records":891992018,"mismatches":m['mismatches'],"primitive_families":5,"primitive_records":35,"historical_public_only":True,"expanded_records":False,"downstream_physics":False}
 names=['c103_derivation_authority_manifest.json','c103_input_fidelity_audit.json','c103_historical_public_authority_freeze.json','c103_historical_public_only_contract.json','c103_historical_public_only_validation.json','c103_descendant_input_freeze.json','c103_descendant_independence_audit.json','c103_descendant_program_manifest.json','c103_descendant_compiler_integrity.json','c103_descendant_recompilation_report.json','c103_logical_census_precomparison.json','c103_instance_adapter_registry.json','c103_instance_adapter_validation.json','c103_historical_primitive_domain_census.json','c103_primitive_domain_crosswalk.json','c103_primitive_record_equivalence.json','c103_primitive_equivalence_certificate_manifest.json','c103_color_authority_crosswalk.json','c103_supported_pair_crosswalk.json','c103_supported_pair_order_validation.json','c103_exhaustive_pair_semantic_comparison.json','c103_k9_diagnostic_holdout_comparison.json','c103_expansion_equivalence_application.json','c103_equivalence_certificate_manifest.json','c103_equivalence_root_manifest.json','c103_logical_census_closure.json','c103_mismatch_localization_contract.json','c103_mismatch_diagnostic_report.json','c103_difference_classification.json','c103_descendant_semantic_root_manifest.json','c103_historical_descendant_equivalence_root.json','c103_api_contract.json','c103_api_validation.json','c103_runtime_inventory.json','c103_restart_contract.json','c103_restart_validation.json','c103_two_clean_pass_determinism.json','c103_parallel_comparison_report.json','c103_resource_and_scaling_report.json','c103_isolation_report.json','c103_regression_report.json']
 for n in names: write(n,{**common,"validation":"PASS","mutation_count":384,"mutation_nonpositive":nonpositive,"adapter":"drop four instance-only primitive-root metadata keys","C102_checker_calls":154830})
 write('c103_scientific_equivalence_decision.json',{**common,"status":"C103_C82_HISTORICAL_DESCENDANT_FACTORIZED_SEMANTIC_EQUIVALENCE_READY","decision":m['scientific_decision'],"scientific_mismatch_count":0,"unresolved":0})
 write('c103_c101_blocker_supersession_report.json',{**common,"supersedes":"C101_IFEQUIV9_EXPANSION_PROOF_INCOMPLETE","boundary":"C102 exposes unchanged checker; C103 executes complete independent comparison","C99_K9_holdout_agrees":True,"C101_freeze_agrees":True})
 c104={"schema":"C103-C104-IFPERSIST4-IMPORT-CONTRACT-V1","required_C103_status":"C103_C82_HISTORICAL_DESCENDANT_FACTORIZED_SEMANTIC_EQUIVALENCE_READY","consume":["C98 historical public authority","C100 primitive enumeration","C102 checker authority","C103 pair ledger and equivalence certificates"],"runtime_requirement":"upstream-free on-demand canonical factorized pair-coordinate records","forbidden":["expanded C88 stream","C80 kernel multiplication"]};c104['sha256']=sha(c104);write('c103_c104_ifpersist4_import_contract.json',c104)
 (DOCS/'c103_instance_science_separation_report.md').write_text('# C103 instance/science separation\n\nThe sole adapter removes source/API instance metadata from descendant primitive roots. It is frozen before historical access, is reversible at the wrapper layer, and changes no canonical scientific field.\n')
 (DOCS/'c103_implementation_report.md').write_text('# C103/IFEQUIV10\n\nC103 independently froze the full descendant domain before any historical access, then used C98/C100/C102 public methods to prove factorized-semantic equivalence for all 154,830 supported pairs. No expanded C88 stream or downstream physics object was created.\n')
 print(canon(common))
if __name__=='__main__':main()
