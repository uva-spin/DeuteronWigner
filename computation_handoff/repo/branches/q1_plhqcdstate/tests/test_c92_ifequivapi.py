from deuteron_wigner.bridge.ifequivapi import audit_existing_c90_payload, select_packaging_route


def test_c92_audits_persisted_c90_payload_without_calling_a_builder():
    audit = audit_existing_c90_payload()
    assert audit["historical_public_aggregate_verified"]
    assert audit["private_builder_called"] is False
    assert audit["upstream_scientific_reconstruction_called"] is False
    assert "normal_form_content" in audit["missing_pair_fields"]


def test_c92_selects_route_c_when_required_historical_objects_are_absent():
    route = select_packaging_route()
    assert route["route"] == "C_UNAVAILABLE"
    assert route["status"] == "C92_IFEQUIVAPI_C90_PAYLOAD_INCOMPLETE"
