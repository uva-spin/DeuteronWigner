"""C57's regulator must be conditional, source-derived, and pre-contraction."""
import numpy as np
import pytest

from deuteron_wigner.bridge.ifreg.core import (
    ORDER, PLAN, STATUS, assert_ready_c57, build_regulator, mutate_live_c57,
    snapshot, static_isolation_guard, validate_c57,
)


def test_c57_builds_conditional_projectors_without_a_contraction_sum():
    value = assert_ready_c57()
    assert value["status"] == STATUS and value["plan"]["selected"] == PLAN
    assert value["operation_order"]["selected"] == ORDER
    for record in value["records"]:
        assert record["field_mask"].shape[0] == 6
        assert np.all(record["field_mask"] ** 2 == record["field_mask"])
        assert np.all(record["qg_mask"] ** 2 == record["qg_mask"])
        assert all(row["conditional_field_rank"] > 0 for row in record["parents"])
    assert value["no_self_induced_inertia_sum"] and value["no_contraction_matrices"]


def test_c57_marks_dlcq_to_ho_conversion_unavailable_not_equivalent():
    value = build_regulator()
    assert value["conversion"]["status"] == "CONVERSION_UNAVAILABLE"
    assert value["conversion"]["rank"] == 0
    assert static_isolation_guard()["pass"]
    assert validate_c57(snapshot())


@pytest.mark.parametrize("fault_id", range(224))
def test_c57_224_live_projector_and_source_mutations_fail(fault_id):
    assert not validate_c57(mutate_live_c57(fault_id))
