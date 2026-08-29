from deuteron_wigner.bridge.ifcontact6 import STATUS, verify_qg_direct_contact_authority

def test_c108_fails_closed_on_missing_pplus():
    out = verify_qg_direct_contact_authority()
    assert out["status"] == STATUS
    assert out["pass"] is False
    assert out["authority"]["P_plus_value"] is None
    assert out["authority"]["P_plus_bound"] is None
    assert out["products_formed"] == 0
    assert out["contact_entries"] == 0
    assert out["authority"]["C107_pairs"] == 154830
    assert out["authority"]["C107_logical_records"] == 891992018
