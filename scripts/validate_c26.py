#!/usr/bin/env python3
"""Validate C26 acquisition, index, gate, and isolation contracts."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
def load(n):return json.loads((D/n).read_text())
def main():
    pi=load('c26_mapff_pion_source_lock.json'); ka=load('c26_mapff_kaon_source_lock.json')
    ms=load('c26_msht20_rep_source_lock.json'); joint=load('c26_joint_member_validation.json')
    gate=load('c26_gate_delta_report.json'); inj=load('c26_injection_manifest.json'); reg=load('c26_regression_report.json')
    assert pi['all_201_members_hash_locked'] and ka['all_201_members_hash_locked']
    assert pi['data_version']==ka['data_version']==1 and pi['num_members']==ka['num_members']==201
    assert ms['status']=='EXACT_CUSTOM_SOURCE_UNAVAILABLE' and not ms['standard_negative_control']['substituted']
    assert joint['stochastic_rows']==642 and joint['ff_indices_resolved']==1284 and joint['pdf_indices_resolved']==0
    assert gate['external_source_count']==gate['microscopic_source_count']==gate['physical_count']==0
    assert inj['count']>=1040 and inj['all_detected']
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged']
    print('C26/P1B validation: PASS')
if __name__=='__main__':main()
