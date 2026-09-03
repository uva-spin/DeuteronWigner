from deuteron_wigner.bridge.ifcoeffval import STATUS, verify_projected_coefficient_authority
from deuteron_wigner.bridge.ifcoeffval.core import evaluate_projected_coefficient

def test_c106_reports_unbound_symbol_blocker():
    out = verify_projected_coefficient_authority()
    assert out["status"] == STATUS
    assert out["pass"] is False
    assert out["audit"]["pairs"] == 154830
    assert out["audit"]["logical_records"] == 891992018
    assert tuple(out["audit"]["unbound_symbols"]) == ("C77COMP_bra", "C77COMP_ket", "U3_bra", "U3_ket")
    assert tuple(out["audit"]["unbound_bound_symbols"]) == ("C77_bounds", "color_bounds")
    assert out["audit"]["C80_evaluator_calls"] == 0

def test_c106_refuses_inferred_values():
    try:
        evaluate_projected_coefficient("C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0", "K9_2_N8_b0.40", 0)
    except RuntimeError as exc:
        assert "unbound" in str(exc)
    else:
        raise AssertionError("C106 must fail closed")
