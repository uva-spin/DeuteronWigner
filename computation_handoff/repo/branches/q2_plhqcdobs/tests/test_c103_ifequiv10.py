from deuteron_wigner.bridge.ifequiv10 import *
import pytest

PAIR="C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"
RES="K9_2_N8_b0.40"
def test_c103_package_and_pair_proof_are_authenticated():
    p=load_verified_historical_descendant_equivalence(); assert p["records"]==154830
    assert verify_historical_descendant_equivalence_root()["pass"]
    assert scientific_equivalence_decision()=="SCIENTIFICALLY_EQUIVALENT_WITH_INSTANCE_ONLY_DIFFERENCES"
    e=pair_equivalence(PAIR,RES); assert e["comparison_status"]=="EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF"
    assert pair_equivalence_proof(PAIR,RES)["status"]==e["comparison_status"]
    assert diagnose_pair_difference(PAIR,RES,max_bytes=256)["difference"] is None
    with pytest.raises(TypeError): e["logical_count"]=0
def test_c103_primitive_lookup_is_compact_and_immutable():
    x=primitive_equivalence("C80","primitives/C80/index.json")
    assert x["relation"]=="CANONICALLY_IDENTICAL_SCIENTIFIC_RECORD"
    with pytest.raises(KeyError): primitive_equivalence("C80","missing")
