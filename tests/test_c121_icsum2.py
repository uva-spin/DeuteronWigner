import pytest

from deuteron_wigner.bridge.icsum2 import *


def test_c121_boundary_and_public_consumption():
    out = verify_current_witness_value_authority()
    assert out["status"] == STATUS
    assert out["program_count"] == 8
    assert out["records"] == 0
    assert out["public_authorities"]["C118_programs"] == 8
    assert out["public_authorities"]["C119_leaves"] == 36
    assert out["positive_gate"] is False
    assert witness_domain_manifest()["logical_witness_count"] is None


def test_c121_no_fabricated_records_or_targets():
    page = witness_record_page(limit=17)
    assert page["records"] == () and page["terminal"]
    assert matrix_target_manifest()["target_count"] == 0
    with pytest.raises(RuntimeError):
        witness_record("missing")
    with pytest.raises(RuntimeError):
        witness_record_by_rank(0)
    with pytest.raises(RuntimeError):
        matrix_target_witness_page("missing")


def test_c121_isolation_and_mutations():
    base = verify_current_witness_value_authority()
    assert static_isolation_guard()["pass"]
    assert sum(mutate_live_icsum2(i) != base for i in range(384)) == 384
