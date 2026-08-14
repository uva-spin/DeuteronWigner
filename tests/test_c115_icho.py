import pytest
from deuteron_wigner.bridge.icho import *

def test_programs_and_routes():
    p = diagonal_component_manifest()
    assert len(p) == 8
    assert all(x["value"] is None and x["bound"] is None for x in p)
    assert quark_current_derivation()["agreement"]
    assert gluon_current_derivation()["agreement"]
    assert len(contraction_projector_manifest()) == 4

def test_fail_closed_no_zero_matrix():
    out = verify_current_ho_projection_authority()
    assert out["status"] == STATUS and out["program_count"] == 8
    assert out["blocked_components"] == 8 and not out["positive_gate"]
    with pytest.raises(RuntimeError):
        instantaneous_current_sparse_matrix("K9_2_N8_b0.40")
    with pytest.raises(RuntimeError):
        current_component_sparse_matrix("J_qJ_q", "q->q", "K9_2_N8_b0.40")
    assert static_isolation_guard()["pass"]

def test_icho_mutations():
    base = verify_current_ho_projection_authority()
    assert sum(mutate_live_icho(i) != base for i in range(384)) == 384
