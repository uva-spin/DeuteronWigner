import pytest

from deuteron_wigner.bridge.icasm3 import *


def test_c120_authority_and_exact_parity_zeros():
    out = verify_current_component_authority()
    assert out["status"] == STATUS
    assert out["program_count"] == 8
    assert out["diagonal_terminal"] == 0
    assert out["diagonal_blocked"] == 8
    assert out["C114_cross_sector_exact_zeros"] == 8
    for resolution in RESOLUTIONS:
        cert = cross_sector_zero_certificate(resolution)
        assert cert["count"] == 8
        assert all(x["status"] == "EXACT_ZERO_WITH_OPERATOR_PROOF" for x in cert["entries"])
        assert all(x["value"] == 0 and x["bound"] == 0 for x in cert["entries"])


def test_c120_c119_crosswalk_and_fail_closed_values():
    assert len(witness_current_factor_crosswalk()["program_rows"]) == 8
    assert witness_current_factor_validation()["missing_bindings"] == 0
    assert witness_current_factor_validation()["witness_value_records"] == 0
    status = component_status("J_qJ_q", "q->q", RESOLUTIONS[0])
    assert status["terminal_status"] == "UNAVAILABLE_BLOCKING"
    assert status["value"] is None and status["bound"] is None
    with pytest.raises(RuntimeError):
        component_sparse_matrix("J_qJ_q", "q->q", RESOLUTIONS[0])
    with pytest.raises(RuntimeError):
        instantaneous_current_sparse_matrix(RESOLUTIONS[0])


def test_c120_isolation_and_mutations():
    base = verify_current_component_authority()
    assert static_isolation_guard()["pass"]
    assert sum(mutate_live_icasm3(i) != base for i in range(384)) == 384
