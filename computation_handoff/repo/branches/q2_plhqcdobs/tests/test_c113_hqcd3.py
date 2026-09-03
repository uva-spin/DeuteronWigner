import pytest
from deuteron_wigner.bridge.hqcd3 import *

def test_c113_audit_blocks_without_silent_zero():
    out = verify_local_qcd_term_authority()
    assert out["pass"] and out["status"] == C113_STATUS
    decision = bare_term_completeness_decision()
    assert decision["decision"] == "MULTIPLE_LOCAL_QCD_TERMS_BLOCKING"
    assert len(decision["blockers"]) >= 4
    assert missing_term_manifest()["no_silent_zero"]

def test_c113_basis_and_counterterms():
    assert direct_sum_basis_manifest("K9_2_N8_b0.40")["total"] == 1350
    assert counterterm_direction_manifest()["coefficient"] == "UNAVAILABLE"
    with pytest.raises(RuntimeError): free_m2_sparse_matrix("K9_2_N8_b0.40")
    with pytest.raises(RuntimeError): bare_polynomial_manifest("K9_2_N8_b0.40")

def test_c113_mutations_fail_closed():
    failures = 0
    for i in range(384):
        try:
            if i % 2: free_m2_sparse_matrix("MUTATED")
            else: apply_order_gs2_coefficient("K9_2_N8_b0.40", None)
        except RuntimeError:
            failures += 1
    assert failures == 384
