#!/usr/bin/env python3
"""Validate C28/P1D machine-readable acceptance records."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
def load(n):return json.loads((D/n).read_text())
def main():
    src=load('c28_dataprocessor_source_lock.json');cdf=load('c28_cdf1_regression_authority.json')
    inv=load('c28_art25_dataset_inventory.json');sel=load('c28_art25_selection_manifest.json')
    cen=load('c28_central_dataset_prediction_manifest.json');run=load('c28_full_dataset_member_execution.json')
    chk=load('c28_checkpoint_restart_manifest.json');fac=load('c28_theory_ensemble_factor_manifest.json')
    low=load('c28_lowqt_source_reproducibility_contract.json');wy=load('c28_wy_readiness_matrix.json')
    inj=load('c28_injection_manifest.json');req=load('c28_requirement_coverage.json');reg=load('c28_regression_report.json')
    assert src['historical_art25_commit']=='761f3fcdd3701c5cf69e822f9ffbbd5db394fc58' and src['bundle_complete_history']
    assert cdf['native']==3.4394876804377352 and cdf['loaded']==50 and cdf['selected']==33
    assert (inv['datasets'],inv['source_points'],inv['selected_points'])==(46,8675,1209)
    assert sel['retained']==1209 and sel['excluded']==7466 and sel['source_decision_residuals']==0
    assert cen['attempted']==cen['completed']==1209 and cen['failed']==0
    assert run['attempted']==run['completed']==642 and run['failed']==run['imputed']==0
    assert chk['serial_parallel_max_abs_residual']==chk['restart_max_abs_residual']==0
    assert fac['shape']==[642,1209] and fac['normalization']=='sqrt(641)'
    assert low['all_pass'] and not wy['source_wy_validated']
    assert len(inj['rows'])>=1200 and inj['all_detected'] and req['all_covered']
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged']
    print('C28_VALIDATION_PASS')
if __name__=='__main__':main()
