"""C50 regression: source-to-basis canonical vertex is individual-only."""
import pytest

from deuteron_wigner.bridge.vsrc.core import (
    STATUS, evaluate_canonical_vertex, mutate_live_c50, run_c50_checks, validate_c50,
)


def test_c50_end_to_end_source_derived_contract_closes():
    result = run_c50_checks()
    assert result["status"] == STATUS
    assert result["pass"]
    assert result["historical_factor_two_detected"]
    assert result["m2_route_residual"] < 1e-12


def test_c50_evaluator_uses_basis_ids_but_not_raw_c47_values():
    result = run_c50_checks()
    s = result["samples"][0]
    direct = evaluate_canonical_vertex(s["incoming_q_basis_id"], s["outgoing_qg_basis_id"], s["resolution"])
    assert direct["raw_C47_tuple_value_consumed"] is False
    assert direct["pminus_GeV"] == s["pminus_GeV"]


@pytest.mark.parametrize("fault_id", range(192))
def test_c50_192_live_convention_operator_evaluator_mutations_fail(fault_id):
    assert not validate_c50(mutate_live_c50(fault_id))
