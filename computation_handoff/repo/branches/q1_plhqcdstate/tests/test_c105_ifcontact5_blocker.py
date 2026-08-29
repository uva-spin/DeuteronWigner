from deuteron_wigner.bridge.ifcontact5 import (
    STATUS, verify_qg_direct_contact_authority, direct_contact_pair_entry,
)

def test_c105_fails_closed_on_symbolic_c104_coefficients():
    out = verify_qg_direct_contact_authority()
    assert out["status"] == STATUS
    assert out["pass"] is False
    assert out["products_formed"] == 0
    assert out["coefficient_values_missing"] == 154830

def test_c105_never_fabricates_pair_product():
    try:
        direct_contact_pair_entry("C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0", "K9_2_N8_b0.40")
    except RuntimeError as exc:
        assert "coefficient" in str(exc)
    else:
        raise AssertionError("symbolic coefficient must not be converted to a contact value")
