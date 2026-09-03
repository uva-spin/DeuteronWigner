from deuteron_wigner.bridge.ifhistpublic import STATUS, audit_authenticated_proof_input_payload


def test_c96_audit_verifies_authenticated_payload_but_refuses_private_proof_recovery():
    audit = audit_authenticated_proof_input_payload()
    assert STATUS == "C96_IFHISTPUBLIC_PROOF_INPUT_LOADER_INCOMPLETE"
    assert audit["authority_verified"]
    assert audit["pair_attestations"]["records"] == 154830
    assert audit["normal_forms"]["records"] == 154830
    assert audit["persisted_proof_input_domain"] is False
    assert audit["forbidden_private_recovery_called"] is False
