"""C46 must not turn a one-particle library into unsupported QCD matrices."""
from copy import deepcopy
import pytest

from deuteron_wigner.bridge.hqcd.c46_preflight import (
    STATUS, assert_physical_basis_assembly_incomplete, source_to_matrix_audit,
    validate_source_to_matrix_audit,
)


def test_c46_source_to_matrix_gate_is_exact_and_fail_closed():
    audit = assert_physical_basis_assembly_incomplete()
    assert audit["status"] == STATUS
    assert [x["id"] for x in audit["missing_physical_matrix_element_contracts"]] == [
        "C46.MULTIBODY_X_SCALED_HO", "C46.CENTER_OF_MASS_PROJECTOR", "C46.FREE_OPERATOR_REPRESENTATION", "C46.CANONICAL_VERTEX_MODE_KERNEL", "C46.BOUNDARY_GLOBAL_ZERO_MODE",
    ]


@pytest.mark.parametrize("fault_id", range(192))
def test_192_live_source_to_matrix_mutations_fail(fault_id):
    audit = deepcopy(source_to_matrix_audit())
    if fault_id % 6 == 0:
        audit["status"] = "READY"
    elif fault_id % 6 == 1:
        audit["baseline_checks"]["C43_mode_status"] = "CORRUPTED"
    elif fault_id % 6 == 2:
        audit["baseline_checks"]["C45_contract_rows"]["TRANSVERSE_2D_HO_AND_PHASE"] = "MUTATED"
    elif fault_id % 6 == 3:
        audit["missing_physical_matrix_element_contracts"][0]["observed"] = "x-scaled fabricated mode"
    elif fault_id % 6 == 4:
        audit["missing_physical_matrix_element_contracts"][2]["blocking_reason"] = "arbitrary L selected"
    else:
        audit["missing_physical_matrix_element_contracts"].pop()
    assert not validate_source_to_matrix_audit(audit)
