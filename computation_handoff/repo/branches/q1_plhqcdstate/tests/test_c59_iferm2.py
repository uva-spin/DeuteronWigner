import pytest
from deuteron_wigner.bridge.iferm2.core import assert_fail_closed_c59, mutate_live_c59, snapshot, validate_c59

def test_c59_imports_c58_but_does_not_fabricate_direct_contact_support():
    value=assert_fail_closed_c59()
    assert [r['mode_count'] for r in value['C58_import']['records']]==[4216,8330,14484]
    assert value['direct_source_ledger'][0]['status']=='DIRECT_QG_CONTACT_REQUIRED'
    assert value['support_audit']['selected']=='IFERM2-DIRECT-CONTACT-SUPPORT-UNAVAILABLE'
    assert validate_c59(snapshot())

@pytest.mark.parametrize('fault_id',range(256))
def test_c59_live_contract_mutations_fail(fault_id):
    assert not validate_c59(mutate_live_c59(fault_id))
