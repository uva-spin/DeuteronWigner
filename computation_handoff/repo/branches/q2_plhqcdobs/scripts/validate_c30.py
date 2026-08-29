#!/usr/bin/env python3
"""Validate C30/B1 fail-closed distribution bridge evidence."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];D=ROOT/'docs/next_level'
def load(n):return json.loads((D/n).read_text())
def main():
    ext=load('c30_art25_tmd_definition_manifest.json');fl=load('c30_art25_flavor_convention_manifest.json')
    sel=load('c30_bridge_scheme_selection.json');ad=load('c30_finite_scheme_adapter_library.json')
    dom=load('c30_bridge_point_eligibility.json');micro=load('c30_microscopic_distribution_export.json')
    cov=load('c30_external_distribution_anomaly_factor_manifest.json');disc=load('c30_distribution_bridge_discrepancy_availability.json')
    cap=load('c30_distribution_bridge_capability_matrix.json');diag=load('c30_distribution_compatibility_diagnostic.json')
    role=load('c30_constraint_role_execution_report.json');rel=load('c30_cross_root_member_relation_regression.json')
    inj=load('c30_injection_manifest.json');req=load('c30_requirement_coverage.json');reg=load('c30_regression_report.json')
    norm=load('c30_normative_source_integration.json')
    assert ext['status']=='C30_ART25_TMD_DEFINITION_SOURCE_AUDITED' and len(ext['records'])==4
    assert fl['stored_scalar']=='f_not_xf' and fl['antiquarks_direct_slots']
    assert sel['selected']['plan_id']=='B1-SCHEME-ART25' and sel['selected_before_numerical_residuals'] and not sel['residuals_inspected']
    assert ad['source_audited_executable']==0 and not ad['records'][0]['source_hash']
    assert dom['count']==12 and dom['eligible']==0 and all(not x['eligible'] for x in dom['rows'])
    assert micro['completed']==0 and not micro['free_normalization']
    assert cov['shape']==[642,0] and cov['member_order_exact'] and cov['normalization']=='sqrt(641)'
    assert disc['available']==2 and disc['nonzero_unknown']==11
    assert cap['count']==12 and cap['ready']==0 and set(cap['status_counts'])=={'BRIDGE_COMMON_DOMAIN_ONLY'}
    assert not diag['executed'] and not diag['likelihood'] and not diag['optimization']
    assert role['roles_changed']==0 and not role['calibration_executed']
    assert rel['status']=='NO_JOINT_MEASURE' and not rel['index_pairing'] and not rel['cross_root_covariance']
    assert inj['count']>=1520 and inj['all_detected'] and req['all_covered']
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged']
    assert not any(reg[x] for x in ('fit_created','calibration_created','likelihood_created','posterior_created','optimization_created','reweighting_created','emulator_created','process_executed','status_promoted'))
    assert norm['missing']==['references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex']
    print('C30_VALIDATION_PASS')
if __name__=='__main__':main()
