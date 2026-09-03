import json
from pathlib import Path
import pytest

from deuteron_wigner.process.p1c.core import *

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
def load(name): return json.loads((D/name).read_text())

def test_exact_source_and_all_indices_are_locked():
    lock=load('c27_msht20_rep_source_lock.json')
    assert lock['set_name']=='MSHT20_REP' and lock['data_version']==3
    assert lock['required_art25_indices_resolved']==642
    assert lock['missing_required_indices']==[] and lock['substitution_used'] is False

def test_complete_execution_and_covariance():
    run=load('c27_full_member_execution_manifest.json')
    assert (run['attempted'],run['completed'],run['failed'])==(642,642,0)
    assert run['serial_parallel_max_abs_residual']==0
    assert run['restart_max_abs_residual']==0
    cov=load('c27_joint_covariance_manifest.json')
    assert cov['dimension']==39 and cov['symmetry_max_abs_residual']==0
    assert cov['minimum_eigenvalue'] >= cov['psd_tolerance']

def test_fail_closed_types_and_injections():
    s=MSHT20RepSourceId('MSHT20_REP',3,27400,'AUTHOR_DIRECT_TRANSFER_RESEARCH_VALIDATION_ONLY','x')
    e=MSHT20RepEnsemble(s,{i:str(i) for i in range(1000)})
    assert e.resolve(999).index==999
    with pytest.raises(ValueError,match='OUT_OF_RANGE'): e.resolve(1000)
    rows=injection_rows(); assert len(rows)==1120
    assert [r['ordinal'] for r in rows]==list(range(1,1121))

def test_capability_separation_and_wy_closed():
    gate=load('c27_gate_delta_report.json'); wy=load('c27_source_wy_status.json')
    assert gate['external_art25_source_eligible']==0
    assert gate['microscopic_project_source_eligible']==0
    assert gate['physical_input_eligible']==0
    assert wy['source_w']=='SOURCE_TMD_W_TERM_REPRODUCED'
    assert wy['source_wy']=='SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE'
    assert wy['analytic_y_mixed'] is False
