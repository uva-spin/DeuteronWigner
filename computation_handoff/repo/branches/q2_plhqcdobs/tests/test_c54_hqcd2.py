"""C54 must stop before a schematic instantaneous term becomes a matrix."""
import pytest

from deuteron_wigner.bridge.hqcd3.core import (
    BLOCKER, STATUS, assert_fail_closed_c54, c53_read_only_import,
    input_fidelity_audit, local_projection_preflight, mutate_live_c54,
    static_isolation_guard, validate_c54,
)


def test_c54_imports_c53_read_only_and_byte_identically():
    imported = c53_read_only_import()
    assert imported["status"] == "C53_READ_ONLY_IMPORT_VERIFIED"
    assert imported["checks"]["primitive_runtime_hashes"]
    assert imported["checks"]["matrix_free_zero_residual"] and imported["checks"]["poisoning_pass"]
    assert imported["no_c53_builder_called"] and imported["no_rescale_or_color_reconstruction"]


def test_c54_fidelity_finds_the_first_required_projection_absence():
    audit = input_fidelity_audit()
    missing = [x["id"] for x in audit["inputs"] if x["classification"] == "ABSENT_BLOCKING"]
    assert missing == ["IFERM_FINITE_VOLUME_NORMAL_ORDERED_KERNEL", "ICURRENT_FINITE_VOLUME_NORMAL_ORDERED_KERNEL"]
    result = assert_fail_closed_c54()
    assert result["status"] == STATUS and result["input_audit"]["first_blocker"] == BLOCKER
    assert result["no_C54_local_matrices_created"] and not result["positive_gate"]
    assert static_isolation_guard()["pass"]


@pytest.mark.parametrize("fault_id", range(256))
def test_c54_256_live_audit_mutations_fail(fault_id):
    assert not validate_c54(mutate_live_c54(fault_id))
