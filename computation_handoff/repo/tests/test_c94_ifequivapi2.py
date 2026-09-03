from deuteron_wigner.bridge.ifequivapi2 import (
    expansion_theorem_specification, historical_pair_attestation, historical_pair_by_sequence,
    historical_pair_count, historical_pair_page, load_verified_c93_public_authority,
)

PAIR = "C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"


def test_c94_public_authority_and_bounded_page_are_authenticated():
    authority = load_verified_c93_public_authority()
    page = historical_pair_page(limit=2)
    assert authority["pass"] and historical_pair_count() == 154830
    assert len(page["records"]) == 2 and page["next_cursor"]


def test_c94_public_direct_lookup_and_theorem_access():
    first = historical_pair_by_sequence(0)
    assert historical_pair_attestation(PAIR, "K9_2_N8_b0.40")["sha256"] == first["sha256"]
    assert expansion_theorem_specification()["checker_api"] == "check_proof"
