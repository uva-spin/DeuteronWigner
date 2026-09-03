"""C51 must fail closed instead of manufacturing C50 component matrices."""
import pytest

from deuteron_wigner.bridge.vertex2.audit import (
    NEXT, STATUS, assert_c51_dimensional_assembly_incomplete, mutate_live_c51,
    validate_c51_audit,
)


def test_c51_proves_raw_tuple_independence_but_stops_at_component_gap():
    audit = assert_c51_dimensional_assembly_incomplete()
    assert audit["status"] == STATUS
    assert audit["runtime_raw_tuple_poisoning"]["unchanged"]
    assert "VDIM2" in NEXT


@pytest.mark.parametrize("fault_id", range(224))
def test_c51_224_live_input_component_guard_mutations_fail(fault_id):
    assert not validate_c51_audit(mutate_live_c51(fault_id))
