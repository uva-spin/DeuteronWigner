"""C56 must not invent a finite-HO virtual contraction regulator."""
import pytest

from deuteron_wigner.bridge.ifnorm.core import (
    BLOCKER, PLAN, STATUS, assert_fail_closed_c56, contraction_preflight,
    mutate_live_c56, static_isolation_guard, validate_c56,
)


def test_c56_retains_exact_c55_one_pair_contraction_and_vacuum_reference():
    value = assert_fail_closed_c56()
    assert value["status"] == STATUS
    assert value["contraction_identity"]["field_ordering"] == ["b_dagger", "a", "a_dagger", "b"]
    assert "perturbative light-front Fock vacuum" in value["normal_ordering_reference"]["vacuum_identity"]
    assert value["preserved_exact_zeros"] == {"q_to_qg": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY", "qg_to_q": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY"}


def test_c56_rejects_every_positive_plan_without_field_level_ho_projector():
    value = contraction_preflight()
    assert value["regulator_plan"]["selected_plan"] == PLAN
    assert value["input_audit"]["rows"][6]["status"] == BLOCKER
    assert all(row["status"] != "SELECTED" for row in value["regulator_plan"]["plans"][:-1])
    assert value["no_mode_sum"] and value["no_contraction_matrix"]
    assert static_isolation_guard()["pass"]


@pytest.mark.parametrize("fault_id", range(224))
def test_c56_224_live_regulator_ownership_mutations_fail(fault_id):
    assert not validate_c56(mutate_live_c56(fault_id))
