from deuteron_wigner.bridge.ifequiv7 import audit_c94_public_inputs, recompile_descendant_census


def test_c95_detects_missing_c94_exported_theorem_inputs_without_private_access():
    audit = audit_c94_public_inputs()
    assert audit["authority_verified"]
    assert "historical_pair_normal_form" in audit["missing_operations"]
    assert audit["private_C94_core_imported"] is False


def test_c95_descendant_recompilation_preserves_frozen_census():
    census = recompile_descendant_census()
    assert census["K9_2_N8_b0.40"]["pairs"] == 16224
    assert sum(item["logical"] for item in census.values()) == 891992018
