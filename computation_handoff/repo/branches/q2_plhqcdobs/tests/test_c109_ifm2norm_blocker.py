from deuteron_wigner.bridge.ifm2norm import STATUS, classify_c80_kernel_semantics, verify_contact_m2_normalization_authority
from deuteron_wigner.bridge.ifm2norm.core import symbolic_total_pplus, m2_kernel_record

def test_c109_classifies_incomplete_pminus_normalization():
    assert classify_c80_kernel_semantics()["classification"] == "NORMALIZATION_INCOMPLETE"
    out = verify_contact_m2_normalization_authority()
    assert out["status"] == STATUS and out["pass"] is False
    assert out["authority"]["convention"]["L"] == "symbolic"
    assert out["authority"]["products"] == 0
    assert out["authority"]["contact_entries"] == 0

def test_c109_keeps_pplus_symbolic_and_m2_fail_closed():
    assert symbolic_total_pplus("K9_2_N8_b0.40") == "pi*9/2/L"
    try: m2_kernel_record("C80:KAPPA:blocked")
    except RuntimeError as exc: assert "normalization" in str(exc)
    else: raise AssertionError("M2 must not be fabricated")
