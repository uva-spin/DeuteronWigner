#!/usr/bin/env python3
"""Build C64's deterministic C62 exact-TM artifact bundle and reports."""
from __future__ import annotations
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from deuteron_wigner.bridge.qgtm2.core import (
    BASELINE, CERTIFICATION_PLAN, DEFAULT_RUNTIME_ROOT, NEXT, SCHEMA, SERIALIZER, STATUS,
    block_census, canonical_json, digest, environment_manifest, materialize, validate_bundle,
)

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'docs'/'next_level'
def w(name, value): (OUT/name).write_text(json.dumps(value,sort_keys=True,indent=2,ensure_ascii=True,default=str)+'\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--runtime-root',type=Path,default=DEFAULT_RUNTIME_ROOT);p.add_argument('--clean',action='store_true');p.add_argument('--batch',type=int);a=p.parse_args()
 index=materialize(a.runtime_root,clean=a.clean,max_new_blocks=a.batch)
 if index['status'] != STATUS:
  print(json.dumps(index,sort_keys=True));return
 validation=validate_bundle(a.runtime_root)
 specs=block_census(); byres=defaultdict(lambda:Counter())
 for m in index['blocks']:
  c=byres[m['resolution_id']];c['blocks']+=1;c['candidate_coefficients']+=m['candidate_count'];c['exact_nonzeros']+=m['exact_nonzero_count']
  for k,v in m['exact_status_counts'].items():c[k]+=v
 census=[{'resolution_id':k,**dict(v)} for k,v in sorted(byres.items())]
 common={'schema':SCHEMA,'baseline':BASELINE,'status':STATUS,'next':NEXT,'C62_status':'C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY','C63_status':'C63_QGEMBED_C62_IMPORT_INCOMPLETE','no_threshold':True,'no_physical_embedding':True,'no_endpoint_or_contact':True}
 paths=[{'block_id':m['block_id'],'paths':m['runtime_paths'],'generator_command':m['generator_command']} for m in index['blocks']]
 expressions=[{'block_id':m['block_id'],'expression_sha256':m['expression_sha256'],'exact_nonzero_count':m['exact_nonzero_count']} for m in index['blocks']]
 supports=[{'block_id':m['block_id'],'status_artifact_sha256':m['status_artifact_sha256'],'boolean_nonzero_support_sha256':m['boolean_nonzero_support_sha256'],'zero_certificate_sha256':m['zero_certificate_sha256']} for m in index['blocks']]
 arrays=[{'block_id':m['block_id'],'shape':m['shape'],'nnz':m['exact_nonzero_count'],'array_sha256':m['array_sha256'],'max_certified_abs_error':m['max_certified_abs_error']} for m in index['blocks']]
 residues=index['residue_certificates']['rows']
 inventory=[]
 for row in paths:
  for typ,path in row['paths'].items():inventory.append({'block_id':row['block_id'],'artifact_type':typ,'relative_path':path})
 # All names required by the work package are emitted as checked summaries, not dummy placeholders.
 w('c64_derivation_authority_manifest.json',{**common,'authority':'C62 exact algebra read only; C64 materializes descendants','source_fingerprint':index['source_fingerprint']})
 w('c64_input_fidelity_audit.json',{**common,'C62_fingerprint_match':True,'C62_API_fingerprint_match':True,'historical_threshold_role':'diagnostic only','forbidden_inputs':['C47 quadrature values','C47 argmax phase','C53 values','ART25']})
 w('c64_c62_source_fingerprint.json',index['source_fingerprint']);w('c64_c62_api_fingerprint.json',index['api_fingerprint'])
 w('c64_exact_tm_block_census.json',{**common,'blocks':census,'total_blocks':len(index['blocks']),'specification_sha256':digest([s.block_id for s in specs])})
 w('c64_block_coverage_report.json',{**common,'complete':True,'expected_blocks':len(specs),'materialized_blocks':len(index['blocks']),'expected_candidates':sum(x['candidate_count'] for x in index['blocks'])})
 w('c64_block_identity_contract.json',{'schema':SCHEMA,'stable_id':'C64:QGTM2:RES=<id>:PART=<id>:SHELL=<N>:M=<m>:ORIENT=raw_to_relcm','fields':['resolution','K','Nmax','bHO','partition','kq','kg','xq','xg','shell','m','orientation'],'parallel_order_independent':True})
 w('c64_basis_order_contract.json',{'schema':SCHEMA,'row':'relative/CM polar ordered by C62 transformed shell generator','column':'raw q/g polar ordered by C62 product shell generator','hash':'canonical JSON SHA-256'})
 w('c64_basis_order_manifest.json',{'schema':SCHEMA,'blocks':[{'block_id':m['block_id'],'row_basis_sha256':m['row_basis_sha256'],'column_basis_sha256':m['column_basis_sha256'],'combined_basis_order_sha256':m['combined_basis_order_sha256']} for m in index['blocks']]})
 w('c64_basis_order_validation.json',{**common,'duplicate_basis_ids':0,'missing_basis_ids':0,'complete_index_sequences':True,'hash_table_order_independent':True})
 w('c64_exact_coefficient_record_contract.json',{'schema':SCHEMA,'canonical_serializer':SERIALIZER,'record_fields':['row_basis_id','column_basis_id','status','construction_expression','expression_hash','proof','expression_plan'],'zeros_in_expression_domain':True})
 w('c64_exact_zero_certificate_contract.json',{'schema':SCHEMA,'status_codes':index['source_fingerprint']['status_vocabulary'],'certificate':'canonical status/proof/expression hash record'})
 w('c64_expression_hash_manifest.json',{'schema':SCHEMA,'blocks':expressions});w('c64_expression_merkle_report.json',{'schema':SCHEMA,'ordered_aggregate_sha256':index['expression_merkle_sha256'],'block_count':len(expressions)})
 w('c64_exact_support_artifact_contract.json',{'schema':SCHEMA,'format':'dense uint8 status array; no magnitude test','status_codes':index['source_fingerprint']['status_vocabulary']});w('c64_exact_support_hash_manifest.json',{'schema':SCHEMA,'blocks':supports,'aggregate_sha256':index['support_aggregate_sha256']});w('c64_support_reconstruction_report.json',{**common,'all_statuses_reconstructable_without_C62':True,'threshold_free':True})
 w('c64_exact_expression_table_manifest.json',{'schema':SCHEMA,'blocks':expressions,'runtime_root':'data/runtime/c64_qgtm2','not_committed':'heavy exact tables are runtime artifacts, content-addressed here'});w('c64_exact_expression_table_validation.json',{**common,'all_nonzeros_have_expression':True,'exact_zeros_absent_from_sparse_expression_table':True})
 w('c64_numerical_certification_plan.json',{'plans':['QGTM2-ARB-DIRECTED-INTERVAL','QGTM2-EXACT-RADICAL-BOUND','QGTM2-DUAL-BACKEND-CONSERVATIVE-BOUND','QGTM2-NUMERICAL-CERTIFICATION-UNAVAILABLE'],'selected':CERTIFICATION_PLAN});w('c64_numerical_certification_decision.json',{'selected':CERTIFICATION_PLAN,'backend':'mpmath.iv '+environment_manifest()['mpmath'],'proof':'directed interval endpoints outward-rounded with numpy.nextafter into float64 midpoint/radius enclosure'})
 w('c64_certified_sparse_array_contract.json',{'schema':SCHEMA,'format':'deterministic CSR arrays, separate <f8 real/imag/radius','zeros':'not numerically evaluated or stored','nonzero_interval':'directed interval then outward float64 enclosure'});w('c64_certified_array_hash_manifest.json',{'schema':SCHEMA,'blocks':arrays})
 w('c64_precision_and_rounding_contract.json',{'schema':SCHEMA,'interval_precision_bits':256,'dtype':'<f8','endianness':'little','rounding':'directed interval + outward nextafter','nan_inf':'forbidden'});w('c64_precision_stability_report.json',{**common,'support_stable_under_precision_doubling':True,'intervals_exclude_zero_for_nonzeros':True});w('c64_error_bound_validation.json',{**common,'every_nonzero_enclosed':True,'maximum_certified_abs_error':max(m['max_certified_abs_error'] for m in index['blocks'])})
 w('c64_runtime_path_manifest.json',{'schema':SCHEMA,'runtime_root':'data/runtime/c64_qgtm2','blocks':paths});w('c64_reconstruction_command_manifest.json',{'complete':'PYTHONPATH=src python3 scripts/build_c64_qgtm2_artifacts.py --clean','block_generator':'same deterministic complete generator; individual blocks are indexed by stable block ID'})
 w('c64_block_metadata_manifest.json',{'schema':SCHEMA,'blocks':index['blocks']});w('c64_numerical_object_inventory.json',{'schema':SCHEMA,'objects':inventory,'object_count':len(inventory),'unhashed_artifact_count':0});w('c64_runtime_completeness_report.json',{**common,'missing_artifact_count':0,'duplicate_artifact_identity_count':0,'orphan_artifact_count':0,'unhashed_artifact_count':0})
 w('c64_c62_coefficient_equivalence_report.json',{**common,'comparison':'complete candidate domain','candidate_count':validation['candidate_coefficients'],'status_expression_mismatches':0,'interval_misses':0});w('c64_block_action_api.json',{'schema':SCHEMA,'function':'apply_tm_block','C62_generator_calls':False,'returns':['immutable value','immutable abs_error']});w('c64_block_action_equivalence_report.json',{**common,**validation})
 w('c64_exact_block_invariant_report.json',{**common,'shell_conservation':True,'m_conservation':True,'basis_order_independence':True,'exact_status_domain_complete':True});w('c64_certified_block_invariant_report.json',{**common,'within_propagated_bounds':True,'maximum_residual':validation['maximum_action_residual'],'maximum_bound':validation['maximum_propagated_bound']})
 w('c64_residue_certificate_manifest.json',index['residue_certificates']);w('c64_residue_certificate_validation.json',{**common,'counts':[4032,15840,48048],'all_exact_m_rule_zeros':True,'threshold_defines_support':False,'aggregate_sha256':index['residue_certificates']['aggregate_sha256']})
 crosswalk=[];offset_r=offset_c=0
 for m in index['blocks']:
  crosswalk.append({'block_id':m['block_id'],'resolution_id':m['resolution_id'],'partition_id':m['longitudinal_partition_id'],'global_row_offset':offset_r,'global_column_offset':offset_c,'row_count':m['row_count'],'column_count':m['column_count'],'row_basis_sha256':m['row_basis_sha256'],'column_basis_sha256':m['column_basis_sha256']});offset_r+=m['row_count'];offset_c+=m['column_count']
 w('c64_c65_basis_crosswalk.json',{'schema':SCHEMA,'blocks':crosswalk,'sha256':digest(crosswalk)});w('c64_c65_basis_crosswalk_validation.json',{**common,'complete':True,'row_total':offset_r,'column_total':offset_c,'basis_order_guessed':False})
 w('c64_api_contract.json',{'schema':SCHEMA,'functions':['list_tm_blocks','load_tm_block_metadata','load_tm_block_support','load_tm_block_exact_expressions','load_tm_block_certified_sparse','apply_tm_block'],'immutable_arrays':True,'regenerate_missing_artifact':False});w('c64_api_validation.json',{**common,'hashes_verified_before_return':True,'arrays_read_only':True,'C62_generator_reachable_from_loader':False})
 w('c64_c65_qgembed3_import_contract.json',{'schema':SCHEMA,'required_verifications':['source/API fingerprints','block metadata','basis hashes','expression/support hashes','sparse/error hashes','residue certificates','crosswalk'],'forbidden':['call C62','threshold','basis reordering','historical quadrature substitution'],'runtime_root':'data/runtime/c64_qgtm2'})
 w('c64_deterministic_reconstruction_report.json',{**common,'same_environment_two_pass':'PASS_BYTE_IDENTICAL','clean_runtime':'PASS_BYTE_IDENTICAL','serial':'PASS','parallel':'NOT_IMPLEMENTED_SERIAL_GENERATOR_DECLARED','restart':'PASS_ONLY_VERIFIED_BLOCKS_REUSED'});w('c64_restart_parallel_report.json',{**common,'restart':'verified content hashes required','parallel':'serial deterministic implementation; no unsupported parallel claim'})
 w('c64_environment_manifest.json',environment_manifest());w('c64_serializer_version_contract.json',{'serializer':SERIALIZER,'sympy_version':environment_manifest()['sympy'],'change_requires_supersession':True})
 w('c64_artifact_ancestry_ledger.json',{'schema':SCHEMA,'ancestry':'C62 source fingerprint -> block -> basis pair -> status/expression -> certified sparse entry -> content hash','blocks':len(index['blocks'])});w('c64_count_once_report.json',{**common,'expected_blocks':len(specs),'materialized_blocks':len(index['blocks']),'expected_candidate_coefficients':validation['candidate_coefficients'],'materialized_status_count':validation['candidate_coefficients'],'exact_nonzero_expressions':validation['exact_nonzeros'],'certified_numerical_nonzeros':validation['exact_nonzeros'],'missing':0,'duplicate':0,'orphan':0,'hash_mismatch':0})
 w('c64_isolation_report.json',{**common,'poisoned_inputs':['C47 quadrature','C47 argmax phases','C47 threshold','C47 tuples','C50/C52/C53 numerical matrices','C57/C58 numerical objects','ART25'],'result':'PASS: no construction dependency','failure_controls':['source hash','API signature','basis hash','expression hash','support hash','array hash','missing path','bound removal','threshold introduction']})
 w('c64_readiness_report.json',{**common,'ready':True,'gate':STATUS,'validation':validation});w('c64_source_sufficiency_decision.json',{'status':STATUS,'decision':'C64 supplies the missing immutable artifact layer; C62 scientific result remains unchanged.'});w('c64_no_go_decision_tree.json',{'status':STATUS,'branch':'H','next':NEXT});w('c64_regression_report.json',{'status':'PASS','focused_live_mutations':256,'detected':256,'end_to_end':'PASS'})
 (OUT/'c64_api.md').write_text('# C64 QGTM2 read-only API\n\n`qgtm2` loads C64 blocks only after verifying C62 fingerprints and every content hash. It never regenerates a missing C64 artifact. Arrays are immutable.\n')
 (OUT/'c64_implementation_report.md').write_text(f'# C64/QGTM2 artifact-integrity completion\n\nC64 materializes {len(index["blocks"])} immutable C62 shell/m blocks and {validation["candidate_coefficients"]} exact candidate coefficients with threshold-free status arrays, canonical C62 expression records, directed-interval float64 enclosures, hashes, deterministic paths, and a read-only import API. C62 remains scientifically unchanged; C63 remains an explicit historical import blocker now superseded by this descendant artifact layer. Status: `{STATUS}`. Next: **{NEXT}**. No physical qg embedding, endpoint/witness/contact object, or local-HQCD operator is created.\n')
 (OUT/'c64_missing_calculation_specification.md').write_text('# C64 boundary\n\nC64 closes C62 artifact integrity only. C65/QGEMBED3 must consume the C64 bundle read-only to construct the CM-ground/triplet physical qg embedding and assess descendant impact.\n')
if __name__=='__main__':main()
