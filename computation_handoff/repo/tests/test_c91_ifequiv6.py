from deuteron_wigner.bridge.ifequiv6.core import (
    compile_descendant_programs,
    historical_public_api_audit,
    verify_historical_authority_public_boundary,
)


def test_c91_descendant_compiler_constructs_a_current_program_without_c90_pair_output():
    program = next(compile_descendant_programs("K9_2_N8_b0.40"))
    assert program["normal_form"] == "C90-NORMAL-FORM-V1"
    assert program["primitive_roots"]["current_source_commit"] == "ac622ab358b83f090717d7e7fa179b58f18f526d"


def test_c91_public_boundary_audit_finds_no_historical_pair_enumerator():
    audit = verify_historical_authority_public_boundary()
    assert audit["authority_verified"]
    assert not audit["complete_historical_pair_domain_available"]
    assert "C90_PUBLIC_API_MISSES_AUTHENTICATED_PAIR_ENUMERATION" in audit["blocker"]
    assert historical_public_api_audit()["private_C90_runtime_opened"] is False
