from deuteron_wigner.bridge.ifproofinput import (
    proof_input_by_sequence,
    proof_input_count,
    proof_input_for_pair,
    verify_c90_proof_input_capsule,
)

PAIR = "C78:QG:K11_2_N10_b0.45:KIN=27:TRIP=0|C78:QG:K11_2_N10_b0.45:KIN=27:TRIP=0"

def test_c97_capsule_loader_uses_frozen_result_blind_transport():
    assert proof_input_count() == 154830
    value = proof_input_for_pair(PAIR, "K11_2_N10_b0.45")
    assert value["pair"]["global_sequence"] == 16224
    assert proof_input_by_sequence(16224)["proof_input_root"] == value["proof_input_root"]
    assert dict(verify_c90_proof_input_capsule())["proof_result_used_to_construct_input"] is False
