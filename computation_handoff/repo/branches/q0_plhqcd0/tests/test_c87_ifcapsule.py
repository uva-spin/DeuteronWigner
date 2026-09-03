from deuteron_wigner.bridge.ifcapsule.core import (
    CLAIM, CAPSULE, candidate_stream, materialize_capsule, source_chain_arrays,
    scientific_stream, verify_canonical_c72_authority_capsule,
)


def test_c87_source_chain_capsule_is_scientifically_equivalent_to_local_candidate():
    materialize_capsule()
    source = scientific_stream(source_chain_arrays())
    candidate = candidate_stream(CAPSULE / "payload")
    assert source["scientific_root"] == candidate["scientific_root"]
    assert verify_canonical_c72_authority_capsule()["claim"] == CLAIM
