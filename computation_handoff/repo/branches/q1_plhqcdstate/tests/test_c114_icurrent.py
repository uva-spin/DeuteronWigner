import pytest

from deuteron_wigner.bridge.icurrent import (
    STATUS, PRODUCTS, BLOCKS, current_source_manifest,
    inverse_partial_plus_squared, current_product_manifest,
    current_product_block_status, current_monomial_inventory,
    current_contraction_manifest, verify_instantaneous_current_authority,
    current_block_completeness_decision, instantaneous_current_sparse_matrix,
    static_isolation_guard, mutate_live_current,
)

def test_c114_source_and_two_route_kernel():
    src = current_source_manifest()
    assert "J_q,a^+" in src["J_q"]
    assert "J_g,a^+" in src["J_g"]
    assert src["operator"].startswith("P^-_IC = -(g_s^2/2)")
    k = inverse_partial_plus_squared()
    assert k["agreement"] and k["residual"] == "0"
    assert k["route_a"]["denominator"] == "L^2/(pi^2*n^2)"
    assert k["route_b"]["denominator"] == k["route_a"]["denominator"]

def test_c114_all_products_and_no_silent_zero():
    rows = current_product_manifest()
    assert len(rows) == 16
    assert len(current_monomial_inventory()) == 4
    assert len(current_contraction_manifest()) == 4
    assert sum(r["status"] == "EXACT_ZERO_WITH_OPERATOR_PROOF" for r in rows) == 8
    assert sum(r["status"] == "UNAVAILABLE_BLOCKING" for r in rows) == 8
    for product in PRODUCTS:
        out = current_product_block_status(product, "K9_2_N8_b0.40")
        assert len(out["blocks"]) == len(BLOCKS)
        assert not out["all_terminal"]

def test_c114_fail_closed_and_mutations():
    out = verify_instantaneous_current_authority()
    assert out["status"] == STATUS and not out["positive_gate"]
    assert current_block_completeness_decision()["complete_block"] is False
    with pytest.raises(RuntimeError): instantaneous_current_sparse_matrix("K9_2_N8_b0.40")
    assert static_isolation_guard()["pass"]
    for i in range(384):
        mutated = mutate_live_current(i)
        assert mutated != out
