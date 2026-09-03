#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'docs/next_level'
L=lambda n:json.loads((D/n).read_text())
assert L('c32_normative_source_integration.json')['all_required_present']
assert L('c32_primary_source_manifest.json')['count']==14
assert L('c32_operator_identity_decision.json')['decision']=='TREE_LEVEL_REDUCES_TO_C11'
tree=L('c32_c11_tree_reduction_report.json');assert tree['residual']==0 and len(tree['oracle']['rows'])==12 and all(x['nonvacuous_parent'] for x in tree['oracle']['rows'])
assert L('c32_regulator_plan_manifest.json')['frozen_before_one_loop']
reg=L('c32_regulator_plan_manifest.json');assert reg['primary']=='C7:H0:RESOLUTION:b8196017a6bde7c88eda' and [x['K'] for x in reg['trajectory']]==[[9,2],[11,2],[13,2]]
assert L('c32_partonic_diagram_ledger.json')['count']==25
assert L('c32_partonic_diagram_ledger.json')['calculated_one_loop']==0
assert L('c32_soft_sector_capability_report.json')['status']=='C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED'
assert L('c32_microscopic_export_execution_report.json')['executed'] is False
assert L('c32_distribution_bridge_capability_matrix.json')['ready']==0
assert L('c32_distribution_bridge_rerun.json')['executed'] is False
cl=L('c32_distribution_bridge_closure_report.json');assert cl['preserved_source_bridge_covariance']['rank']==10 and cl['preserved_source_bridge_covariance']['nullity']==1
assert L('c32_source_sufficiency_decision.json')['outcome_branch']=='C33/S0'
assert L('c32_injection_manifest.json')['count']==1840
assert L('c32_requirement_coverage.json')['all_covered']
r=L('c32_regression_report.json');assert r['production_registry']==216 and r['authoritative_artifacts_unchanged']
for x in ('fit_created','calibration_created','likelihood_created','posterior_created','optimization_created','reweighting_created','emulator_created','process_executed','status_promoted'):assert not r[x]
print('C32_VALIDATION_PASS')
