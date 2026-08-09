import pytest
from deuteron_wigner.bridge.qgembed2.core import assert_fail_closed_c63,mutate_live_c63,snapshot,validate_c63
def test_c63_requires_immutable_c62_block_artifacts():
 v=assert_fail_closed_c63();assert v['C62_import']['residue_counts']==[4032,15840,48048];assert validate_c63(snapshot())
@pytest.mark.parametrize('fault_id',range(256))
def test_c63_live_mutations_fail(fault_id):assert not validate_c63(mutate_live_c63(fault_id))
