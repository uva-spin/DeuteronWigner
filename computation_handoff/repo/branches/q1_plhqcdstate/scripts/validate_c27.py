#!/usr/bin/env python3
"""Validate C27/P1C machine-readable acceptance records."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
def load(n): return json.loads((D/n).read_text())
def main():
    s=load('c27_msht20_rep_source_lock.json'); j=load('c27_joint_member_validation.json')
    r=load('c27_full_member_execution_manifest.json'); c=load('c27_joint_covariance_manifest.json')
    g=load('c27_gate_delta_report.json'); reg=load('c27_regression_report.json'); inj=load('c27_injection_manifest.json')
    assert s['required_art25_indices_resolved']==642 and not s['substitution_used']
    assert j['all_executable'] and j['missing']==j['wrapped']==j['clipped']==0
    assert r['completed']==642 and r['failed']==0 and r['serial_parallel_max_abs_residual']==0 and r['restart_max_abs_residual']==0
    assert c['dimension']==39 and c['symmetry_max_abs_residual']==0 and c['minimum_eigenvalue']>=c['psd_tolerance']
    assert (g['external_art25_source_eligible'],g['microscopic_project_source_eligible'],g['physical_input_eligible'])==(0,0,0)
    assert len(inj['rows'])>=1120 and inj['all_detected']
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged'] and reg['frozen_grid_unchanged']
    print('C27_VALIDATION_PASS')
if __name__=='__main__': main()
