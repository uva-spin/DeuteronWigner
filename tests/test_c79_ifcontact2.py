import pytest

from deuteron_wigner.bridge.ifcontact2 import core


def test_c79_authenticates_c78_but_refuses_to_fabricate_contact_values():
    audit = core.evaluate_readiness()
    assert audit["status"] == core.STATUS
    assert audit["matrix_status"] == "NOT_CONSTRUCTED"
    assert audit["matrix_free_status"] == "NOT_CONSTRUCTED"
    assert audit["C78_freeze"]["public_api_only"] is True
    assert audit["blocked_coordinate_domains"] == {
        "K9_2_N8_b0.40": 28606464,
        "K11_2_N10_b0.45": 165991250,
        "K13_2_N12_b0.50": 697394304,
    }
    assert sum(row["classification"] == "ABSENT_BLOCKING" for row in audit["inventory"]) == 4
    with pytest.raises(core.DirectContactKernelUnavailable):
        core.require_evaluable_contact_kernel()


def test_c79_rejects_operator_substitution_routes():
    audit = core.evaluate_readiness()
    forbidden = set(audit["prohibited_substitutions"])
    assert "C50 three-mode q-to-qg vertex" in forbidden
    assert "C53 physical vertex values or propagators" in forbidden
    assert "C58 self-induced-inertia primitive" in forbidden
    assert audit["operator_routes"]["coefficient_routes_agree"] is True
