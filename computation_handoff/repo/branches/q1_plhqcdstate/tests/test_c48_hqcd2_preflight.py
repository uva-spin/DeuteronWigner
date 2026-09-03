"""C48 must fail before it can fabricate a source-derived local vertex."""
import pytest

from deuteron_wigner.bridge.hqcd2.preflight import (
    NEXT,
    STATUS,
    assert_canonical_vertex_assembly_incomplete,
    input_fidelity_audit,
    mutate_live_canonical_input,
    validate_canonical_vertex_audit,
)


def test_c48_consumes_real_c47_runtime_objects_but_not_c40():
    audit = input_fidelity_audit()
    assert audit["all_required_runtime_hashes_match"]
    assert len(audit["required_runtime_records"]) == 11
    assert audit["c40"] == "EXECUTABLE_METHOD_ORACLE_ONLY; not consumed"


def test_c48_canonical_gate_is_targeted_and_fail_closed():
    audit = assert_canonical_vertex_assembly_incomplete()
    assert audit["status"] == STATUS
    assert audit["next"] == NEXT
    assert [x["id"] for x in audit["blockers"]] == [
        "C48.CANONICAL.UNIFORM_OPERATOR_UNITS",
        "C48.CANONICAL.M2_CONVERSION",
        "C48.CANONICAL.EXHAUSTIVE_MATRIX_ELEMENT_CONTRACT",
    ]


@pytest.mark.parametrize("fault_id", range(224))
def test_224_live_canonical_source_to_matrix_mutations_fail(fault_id):
    # Each case changes an actual numerical tuple fingerprint, tuple accounting,
    # m-sector support, unit contract, free-M2 conversion, or a concrete
    # blocking proof.  Exact validation rejects every mutation.
    assert not validate_canonical_vertex_audit(mutate_live_canonical_input(fault_id))
