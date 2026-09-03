"""C49 must not turn a source gap into a normalisation convention."""
import pytest

from deuteron_wigner.bridge.vertex1.audit import (
    NEXT, STATUS, assert_canonical_source_chain_incomplete,
    mutate_live_vertex_input, raw_tuple_semantics_summary, tuple_semantics_records,
    validate_c49_summary,
)


def test_c49_audits_every_raw_tuple_without_mutation():
    summary = assert_canonical_source_chain_incomplete()
    rows = tuple_semantics_records()
    assert summary["status"] == STATUS
    assert len(rows) == 3618
    assert all(row["semantic_status"] == "AMBIGUOUS_BLOCKING" for row in rows)
    assert {row["mrel"] for row in rows} == {-1, 0, 1}


def test_c49_has_the_exact_source_chain_next_branch():
    assert raw_tuple_semantics_summary()["source_sufficiency"]["decision"].startswith("No source-qualified")
    assert NEXT == "C50/VSRC — exact finite-volume light-front canonical-vertex source and convention closure"


@pytest.mark.parametrize("fault_id", range(192))
def test_192_live_vertex_source_tuple_unit_mutations_fail(fault_id):
    assert not validate_c49_summary(mutate_live_vertex_input(fault_id))
