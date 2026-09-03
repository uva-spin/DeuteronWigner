#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]; D=R/'docs/next_level'
def load(n): return json.loads((D/n).read_text())
assert load('c31_primary_source_manifest.json')['count']==14
assert load('c31_normative_source_integration.json')['all_required_present']
assert load('c31_three_layer_identity_manifest.json')['collapsed'] is False
assert load('c31_renormalization_component_ledger.json')['blocking']==15
assert load('c31_lf_to_tmd_matching_strategy.json')['selected']=='P-E_UNAVAILABLE'
assert load('c31_tree_level_limit_report.json')['renormalized_tmd_ready'] is False
assert load('c31_project_to_art25_adapter_library.json')['count']==1
assert load('c31_microscopic_renormalized_execution_report.json')['executed'] is False
cap=load('c31_distribution_bridge_capability_matrix.json'); assert cap['ready']==0 and cap['count']==12
assert load('c31_adapter_independence_report.json')['members_checked']==642
assert load('c31_injection_manifest.json')['count']==1680
assert load('c31_requirement_coverage.json')['all_covered']
r=load('c31_regression_report.json'); assert r['production_registry']==216 and r['authoritative_artifacts_unchanged']
assert not any(r[k] for k in ('fit_created','calibration_created','likelihood_created','posterior_created','optimization_created','reweighting_created','emulator_created','process_executed','status_promoted'))
print('C31_VALIDATION_PASS')
