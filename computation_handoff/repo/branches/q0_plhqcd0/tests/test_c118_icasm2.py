import pytest
from deuteron_wigner.bridge.icasm2 import *

def test_program_freeze_and_zeros():
    out=verify_assembly_authority()
    assert len(component_program_freeze()) == 8
    assert out["C114_cross_sector_exact_zeros"] == 8
    assert out["diagonal_terminal"] == 0 and out["diagonal_blocked"] == 8
    assert out["missing_value_factor"]

def test_fail_closed_values():
    with pytest.raises(RuntimeError): component_sparse_matrix("J_qJ_q","q->q","K9_2_N8_b0.40")
    with pytest.raises(RuntimeError): instantaneous_current_sparse_matrix("K9_2_N8_b0.40")
    assert static_isolation_guard()["pass"]

def test_mutations():
    base=verify_assembly_authority()
    assert sum(mutate_live_icasm2(i) != base for i in range(384)) == 384
