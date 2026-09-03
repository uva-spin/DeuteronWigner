"""C58 must remain a source-ordered bare contraction, never a repaired one."""
import numpy as np
import pytest
from deuteron_wigner.bridge.ifnorm2.core import (
    PAIR_PLAN, QG_PLAN, STATUS, apply_direct, assert_ready_c58,
    build_contraction, mutate_live_c58, snapshot, validate_c58,
)

def test_c58_imports_c57_and_closes_ordered_q_contraction():
    value=assert_ready_c58()
    assert value['status']==STATUS and value['pair_support']['selected']==PAIR_PLAN
    assert value['qg_sector']['selected']==QG_PLAN
    assert [x['union'] for x in value['C57_import']['records']]==[1216,2320,3936]
    assert [x['envelope'] for x in value['C57_import']['records']]==[2304,4400,7488]
    assert [sum(x['qg_ranks']) for x in value['C57_import']['records']]==[312,510,756]
    for record in value['records']:
        vec=np.arange(1,7,dtype=float)+1j
        assert np.linalg.norm(record['matrix']@vec-apply_direct(record,vec))<1e-11
        assert np.linalg.norm(record['matrix']-record['matrix'].conj().T)<1e-11
        assert record['pair_counts']['admitted']==len(record['ledger'])
        assert record['pair_counts']['exact_zero']==30

def test_c58_snapshot_is_deterministic():
    assert validate_c58(snapshot())

@pytest.mark.parametrize('fault_id',range(256))
def test_c58_256_live_mutations_fail(fault_id):
    assert not validate_c58(mutate_live_c58(fault_id))
