import pytest

from deuteron_wigner.bridge.icdomain import *


def test_c122_taxonomy_and_authority_boundary():
    out = verify_current_logical_domain()
    assert out["status"] == STATUS
    assert out["programs"]["program_count"] == 8
    assert out["domain"]["logical_witness_count"] is None
    assert out["public_authorities"]["C119_leaves"] == 36
    assert out["witness_values_formed"] == 0
    assert out["component_sums"] == 0


def test_c122_cross_sector_empty_domains():
    zero = cross_sector_zero_domain_manifest()
    assert zero["class_count"] == 8
    assert zero["logical_witnesses"] == 0
    assert zero["numerical_zero_records"] == 0
    assert all(x["empty_domain"] for x in zero["classes"])
    assert matrix_target_manifest(PROGRAMS[0], RESOLUTIONS[0])["target_count"] == 0
    assert witness_page(limit=9)["records"] == ()


def test_c122_no_inference_and_mutations():
    base = verify_current_logical_domain()
    assert static_isolation_guard()["pass"]
    with pytest.raises(RuntimeError):
        witness_identity("inferred")
    with pytest.raises(RuntimeError):
        witness_by_rank(PROGRAMS[0], RESOLUTIONS[0], 0)
    assert sum(mutate_live_icdomain(i) != base for i in range(384)) == 384
