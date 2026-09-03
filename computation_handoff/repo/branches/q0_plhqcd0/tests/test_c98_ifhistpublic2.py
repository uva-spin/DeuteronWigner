from deuteron_wigner.bridge.ifhistpublic2 import (
    historical_pair_normal_form, historical_pair_proof_inputs,
    historical_primitive_record,
)
from deuteron_wigner.bridge.ifhistpublic2.core import load_verified_historical_theorem_input_authority
from deuteron_wigner.bridge.ifhistpublic2 import core
import pytest

PAIR = "C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"

def test_c98_three_public_methods_are_authenticated_and_immutable():
    authority = load_verified_historical_theorem_input_authority()
    normal = historical_pair_normal_form(PAIR, "K9_2_N8_b0.40")
    proof = historical_pair_proof_inputs(PAIR, "K9_2_N8_b0.40")
    primitive = historical_primitive_record("C77", "primitives/C77/K11_2_N10_b0.45/kin_bounds.npy")
    assert normal["normal_form_root"] == proof["proof_input"]["route_b_normal_form"]["root"]
    assert proof["proof_input"]["pair"]["id"] == PAIR
    assert normal["resolution_sequence"] == proof["proof_input"]["pair"]["resolution_sequence"]
    assert normal["transport"]["key"]["pair_id"] == PAIR
    assert primitive["family_id"] == "C77"
    assert authority["C98_root"] == normal["C98_root"] == proof["C98_root"] == primitive["C98_root"]
    assert set(__import__("deuteron_wigner.bridge.ifhistpublic2", fromlist=["__all__"]).__all__) == {
        "historical_pair_normal_form", "historical_pair_proof_inputs", "historical_primitive_record"}

def test_c98_missing_compact_index_fails_closed_without_a_builder(monkeypatch, tmp_path):
    original = core.RUNTIME
    core._c98_manifest.cache_clear()
    core.load_verified_historical_theorem_input_authority.cache_clear()
    monkeypatch.setattr(core, "RUNTIME", tmp_path)
    with pytest.raises(ValueError):
        core.load_verified_historical_theorem_input_authority()
    monkeypatch.setattr(core, "RUNTIME", original)
    core._c98_manifest.cache_clear()
    core.load_verified_historical_theorem_input_authority.cache_clear()
