import pytest
from deuteron_wigner.bridge.icho2 import *

def test_five_class_freeze_crosswalk():
    assert CLASSES == ("I4_local","I2_density_projector","derivative_density","CM_ground","triplet_projected")
    assert len(component_kernel_crosswalk()) == 8
    assert all(x["unmapped"] == 0 for x in component_kernel_crosswalk())
    assert len(five_class_derivations()) == 5
    assert evaluate_kernel("I4_local")["route_residual"] == 0

def test_fail_closed_projectors_and_components():
    out=verify_icho2_authority()
    assert out["status"] == STATUS and out["class_count"] == 5
    assert out["missing_projectors"] == 4 and out["unavailable_as_zero"] == 0
    assert out["terminal_programs"] == 1 and not out["complete_block"]
    with pytest.raises(RuntimeError): instantaneous_current_sparse_matrix("K9_2_N8_b0.40")
    with pytest.raises(RuntimeError): current_component_sparse_matrix("J_qJ_g","q->q","K9_2_N8_b0.40")
    assert static_isolation_guard()["pass"]

def test_mutations():
    base=verify_icho2_authority()
    assert sum(mutate_live_icho2(i) != base for i in range(384)) == 384
