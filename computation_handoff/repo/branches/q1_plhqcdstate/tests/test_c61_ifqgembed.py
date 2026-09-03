import pytest
from deuteron_wigner.bridge.ifqgembed.core import assert_fail_closed_c61,mutate_live_c61,snapshot,validate_c61
def test_c61_requires_exact_phase_contract():
 v=assert_fail_closed_c61();assert 'argmax' in ' '.join(v['phase_audit']['evidence']);assert validate_c61(snapshot())
@pytest.mark.parametrize('fault_id',range(256))
def test_c61_live_mutations_fail(fault_id):assert not validate_c61(mutate_live_c61(fault_id))
