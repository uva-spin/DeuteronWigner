from deuteron_wigner.bridge.ifc90payload import (
    load_verified_c90_semantic_payload_capsule, recovered_normal_form, recovered_pair_binding,
)


PAIR = "C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"


def test_c93_capsule_is_verified_and_declares_descendant_preimage_boundary():
    capsule = load_verified_c90_semantic_payload_capsule()
    assert capsule["pass"]
    assert capsule["original_c90_runtime_identity"] == "NOT_CLAIMED"


def test_c93_capsule_loader_answers_from_payload_only():
    binding = recovered_pair_binding(PAIR, "K9_2_N8_b0.40")
    form = recovered_normal_form(binding["normal_form_root"])
    assert form["normal_form_root"] == binding["normal_form_root"]
