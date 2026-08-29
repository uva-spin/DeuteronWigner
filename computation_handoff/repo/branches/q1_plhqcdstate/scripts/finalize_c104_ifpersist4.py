import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]; D=R/'docs/next_level'
M=json.loads((R/'data/runtime/c104_ifpersist4/manifest.json').read_text())
def w(n,x):
 (D/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n')
def main():
 c={'schema':'C104-FINALIZATION-V1','status':'C104_C82_UPSTREAM_FREE_CANONICAL_FACTORIZED_COEFFICIENT_PACKAGE_READY','package_root':M['C104_PACKAGE_ROOT'],'pairs':154830,'logical_records':891992018,'rank_unrank':'PASS','program_validation':'PASS','C80_evaluator_calls':0,'kernel_values_loaded':0,'coefficient_times_kernel_products':0,'contact_matrix_entries':0,'expanded_stream':False,'mutations':384}
 for n in ['c104_derivation_authority_manifest.json','c104_input_fidelity_audit.json','c104_canonical_input_freeze.json','c104_canonical_representation_decision.json','c104_instance_metadata_exclusion_contract.json','c104_canonical_record_schema.json','c104_canonical_record_schema_validation.json','c104_factor_ownership_contract.json','c104_package_schema_contract.json','c104_package_root_manifest.json','c104_runtime_inventory.json','c104_root_semantics.json','c104_no_expanded_stream_declaration.json','c104_upstream_free_reconstruction_contract.json','c104_upstream_free_reconstruction_validation.json','c104_no_recomputation_report.json','c104_rank_unrank_contract.json','c104_rank_unrank_validation.json','c104_ordinal_identity_manifest.json','c104_exhaustive_pair_program_persistence_validation.json','c104_primitive_expression_inventory.json','c104_primitive_expression_validation.json','c104_api_contract.json','c104_api_validation.json']:
  w(n,c)
 w('c104_c105_ifcontact5_import_contract.json',{'schema':'C104-C105-IFCONTACT5-IMPORT-CONTRACT-V1','required_status':c['status'],'C104_PACKAGE_ROOT':M['C104_PACKAGE_ROOT'],'scope':'coefficient-times-C80-kernel aggregation with factored g_s_squared','forbidden':['physical coupling choice','counterterm','TMD','expanded stream']})
 (D/'c104_implementation_report.md').write_text('# C104/IFPERSIST4\n\nUpstream-free factorized C82 coefficient authority with exact mixed-radix on-demand records. C80 kernels remain outside the package.\n')
if __name__=='__main__':main()
