#!/usr/bin/env python3
"""Validate C29/B0 bridge acceptance records."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];D=ROOT/'docs/next_level'
def load(name):return json.loads((D/name).read_text())
def main():
    roots=load('c29_root_identity_manifest.json');ops=load('c29_operator_crosswalk.json')
    targets=load('c29_target_crosswalk.json');grid=load('c29_frozen_bridge_grid.json')
    af=load('c29_external_bridge_anomaly_factor_manifest.json');cov=load('c29_external_bridge_covariance_blocks.json')
    micro=load('c29_microscopic_bridge_execution_report.json');rel=load('c29_cross_root_member_relation.json')
    ancestry=load('c29_data_ancestry_graph.json');roles=load('c29_constraint_role_split.json')
    disc=load('c29_discrepancy_interface.json');diag=load('c29_compatibility_diagnostic_manifest.json')
    cap=load('c29_bridge_capability_matrix.json');future=load('c29_future_inference_prerequisite_contract.json')
    inj=load('c29_injection_manifest.json');req=load('c29_requirement_coverage.json');reg=load('c29_regression_report.json')
    v19=load('c29_volume_xix_requirement_crosswalk.json');norm=load('c29_normative_source_integration.json')
    assert roots['immutable'] and roots['disjoint'] and roots['root_pair']['external']['value']!=roots['root_pair']['microscopic']['value']
    assert ops['count']>=14 and all(x['matched_by_complete_identity'] and not x['matched_by_name_only'] for x in ops['rows'])
    assert not load('c29_nuclear_bridge_scope.json')['phenomenological_deuterium_is_microscopic_deuteron']
    assert not load('c29_nuclear_bridge_scope.json')['nn_is_matched_total']
    assert grid['frozen_before_microscopic_execution'] and not grid['selection_used_residuals']
    assert af['shape'][0]==642 and af['member_order_exact'] and af['normalization']=='sqrt(641)'
    assert cov['dense_reconstruction_residual']<1e-15 and cov['symmetry_residual']==0 and cov['psd'] and cov['null_space_preserved']
    assert micro['common_scheme_numeric_exports']==0 and not micro['microscopic_model_mutated']
    assert rel['status']=='NO_JOINT_MEASURE' and not rel['index_pairing'] and not rel['cross_root_covariance']
    assert ancestry['retained_points']==1209 and ancestry['complete']
    assert roles['frozen_before_diagnostics'] and roles['moved_after_diagnostics']==0
    assert not disc['fitted'] and not disc['external_covariance_inflated'] and all(not x['zero_justified'] for x in disc['rows'])
    assert not diag['p_values'] and not diag['optimization'] and not diag['reweighting']
    assert cap['distribution_ready']==cap['one_leg_ready']==0
    assert not future['all_satisfied'] and not future['inference_api_created']
    assert len(inj['rows'])>=1400 and inj['all_detected'] and req['all_covered']
    assert v19['count']==50 and v19['all_mapped'] and not v19['status_promotion_authorized']
    assert [x['stable_id'] for x in v19['rows']]==[f'V19.{i:03d}' for i in range(1,51)]
    v19_source=next(x for x in norm['records'] if x['path']=='references/volume_xix_source_qualified_process_inputs.tex')
    assert v19_source['available'] and v19_source['sha256']==v19['source_sha256']
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged'] and not any(reg[x] for x in ('fit_created','likelihood_created','posterior_created','reweighting_created','calibration_executed','emulator_created','status_promoted'))
    print('C29_VALIDATION_PASS')
if __name__=='__main__':main()
