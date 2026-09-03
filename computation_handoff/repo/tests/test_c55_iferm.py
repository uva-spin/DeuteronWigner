"""C55 source algebra must retain, not fabricate or drop, self-induced inertia."""
import pytest

from deuteron_wigner.bridge.iferm.core import (
    BLOCKER, STATUS, assert_fail_closed_c55, input_fidelity_audit,
    instantaneous_fermion_preflight, mutate_live_c55, static_isolation_guard,
    validate_c55,
)


def test_c55_source_operator_and_two_g_squared_routes_close():
    value = assert_fail_closed_c55()
    assert value["status"] == STATUS and value["source"]["symbolic_residual"] == "Integer(0)"
    assert "complete right product" in value["source"]["derivative_placement"]
    assert value["C53_read_only_import"]["status"] == "C53_READ_ONLY_IMPORT_VERIFIED"


def test_c55_enumerates_all_normal_ordering_choices_and_preserves_contact_count_once():
    value = instantaneous_fermion_preflight()
    assert len(value["ledger"]) == 16
    assert sum(x["status"] != "EXACT_ZERO_BY_OPERATOR_ALGEBRA" for x in value["ledger"]) == 14
    assert value["blocks"][1]["status"] == "EXACT_ZERO_BY_GLUON_NUMBER_PARITY"
    assert value["blocks"][0]["reason"] == BLOCKER
    assert not value["count_once"]["double_count"]
    assert static_isolation_guard()["pass"]
    assert input_fidelity_audit()["C40_consumed"] is False


@pytest.mark.parametrize("fault_id", range(224))
def test_c55_224_live_source_and_normal_ordering_mutations_fail(fault_id):
    assert not validate_c55(mutate_live_c55(fault_id))
