import pytest
from deuteron_wigner.bridge.ifsupport.core import assert_fail_closed_c60,mutate_live_c60,snapshot,validate_c60
def test_c60_blocks_tolerance_created_exact_support():
    v=assert_fail_closed_c60(); assert [x['subthreshold_nonzero_entries'] for x in v['embedding_audit']['records']]==[4032,15840,48048]; assert validate_c60(snapshot())
@pytest.mark.parametrize('fault_id',range(256))
def test_c60_live_mutations_fail(fault_id): assert not validate_c60(mutate_live_c60(fault_id))
