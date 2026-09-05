from __future__ import annotations

import numpy as np
import pytest

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    source_reduced_c117_i2_shape_csr,
)
from deuteron_wigner.bridge import hqcdc117rismom1 as c260
from deuteron_wigner.bridge.c411_c117_i2_finite_c43_adapter import (
    AVAILABLE_SOURCE_DIRECTIONS,
    C260_RESOLUTION_BY_LABEL,
    MISSING_CERTIFICATE,
    RESOLUTION_LABELS,
    SCHEME,
    STATUS,
    TARGET_OPERATOR,
    adapter_certificate_schema,
    adapter_contract_record,
    apply_c117_1,
    completion_record,
    fail_closed_apply_complete_c117_i2,
    fail_closed_complete_c117_i2,
    mutate_live_c411,
    normalization_ownership_record,
    validate_adapter_certificate,
)


def _certificate(resolution: str = "K9") -> dict:
    source_authority = next(
        row["source_shape_authority"]
        for row in adapter_contract_record()["rows"]
        if row["resolution"] == resolution
    )
    return {
        "certificate_id": "C411-EXPLICIT-TEST-CERTIFICATE",
        "resolution": resolution,
        "scheme_id": SCHEME,
        "operator_id": TARGET_OPERATOR,
        "source_basis_hash": source_authority,
        "target_basis_hash": c260.operator_basis()["root"],
        "mixing_matrix": (
            (2.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        ),
        "normalization_scalar": 0.5,
        "units": "GeV^2",
        "Pminus_to_M2_conversion": {
            "formula": "delta M^2 = 2*pi*K/L * delta P^-",
            "applied_once": True,
        },
        "source_locator": "explicit test authority; not physical",
        "source_sha256": "c" * 64,
        "source_authority_status": "SOURCE_QUALIFIED_NUMERICAL_CERTIFICATE",
        "no_default": True,
    }


def test_contract_is_k_local_and_fail_closed() -> None:
    record = adapter_contract_record()
    assert STATUS in record["status"]
    assert tuple(row["resolution"] for row in record["rows"]) == RESOLUTION_LABELS
    assert tuple(row["target_resolution_id"] for row in record["rows"]) == tuple(
        C260_RESOLUTION_BY_LABEL[label] for label in RESOLUTION_LABELS
    )
    assert record["available_source_directions"] == AVAILABLE_SOURCE_DIRECTIONS
    assert record["mixing_values_evaluated"] is False
    assert record["identity_mixing_assumed"] is False
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["smallest_missing_object"] == MISSING_CERTIFICATE


def test_m2_conversion_formula_is_fixed_but_not_applied_by_contract() -> None:
    rows = adapter_contract_record()["rows"]
    for row in rows:
        conversion = row["Pminus_to_M2"]
        assert conversion["formula"] == "delta M^2 = 2 P^+ delta P^-"
        assert conversion["result"] == "delta M^2 = 2*pi*K/L * delta P^-"
        assert conversion["applied"] is False
        assert conversion["ownership"] == "SOURCE_QUALIFIED_CERTIFICATE_REQUIRED"


def test_ownership_counts_prevent_double_application() -> None:
    record = normalization_ownership_record()
    assert record["double_counting_guard"]["source_minus_one_half"] == 1
    assert record["double_counting_guard"]["g_s_squared"] == 0
    assert record["double_counting_guard"]["c_C117_1"] == 0
    assert record["complete"] is False


def test_schema_requires_explicit_authority_and_no_default() -> None:
    schema = adapter_certificate_schema()
    assert "mixing_matrix" in schema["required"]
    assert "source_authority_status" in schema["required"]
    assert schema["no_default"] is True


def test_structural_contract_does_not_validate_as_numerical_certificate() -> None:
    with pytest.raises(ValueError):
        validate_adapter_certificate(adapter_contract_record()["rows"][0])


def test_nonzero_mixing_into_unavailable_source_is_rejected() -> None:
    record = _certificate()
    record["mixing_matrix"] = ((1.0, 0.25, 0.0, 0.0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    with pytest.raises(ValueError, match="unavailable"):
        validate_adapter_certificate(record)


def test_undocumented_zero_target_row_is_rejected() -> None:
    record = _certificate()
    record["mixing_matrix"] = ((0.0, 0.0, 0.0, 0.0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    with pytest.raises(ValueError, match="undocumented zero"):
        validate_adapter_certificate(record)


def test_basis_hash_mismatch_is_rejected() -> None:
    record = _certificate()
    record["source_basis_hash"] = "a" * 64
    with pytest.raises(ValueError, match="source basis hash"):
        validate_adapter_certificate(record)


def test_conversion_must_be_owned_exactly_once() -> None:
    record = _certificate()
    record["Pminus_to_M2_conversion"]["applied_once"] = False
    with pytest.raises(ValueError, match="exactly once"):
        validate_adapter_certificate(record)


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_explicit_certificate_applies_only_first_coordinate(resolution: str) -> None:
    certificate = _certificate(resolution)
    validation = validate_adapter_certificate(certificate)
    assert validation["numerical_authority_certified"] is True
    source = source_reduced_c117_i2_shape_csr(resolution)
    vector = np.ones(source.shape[1], dtype=np.complex128)
    result = apply_c117_1(resolution, vector, certificate)
    assert np.allclose(result, source @ vector)


def test_full_four_direction_action_remains_fail_closed() -> None:
    with pytest.raises(RuntimeError, match="full four-direction"):
        fail_closed_complete_c117_i2()
    with pytest.raises(RuntimeError, match="full four-direction"):
        fail_closed_apply_complete_c117_i2()


def test_completion_record_preserves_counts_and_nonclaims() -> None:
    record = completion_record()
    assert record["K_local_rows"] == 3
    assert record["source_qualified_numerical_certificates"] == 0
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["full_C117_I2_action_ready"] is False
    assert record["physical_fit_authorized"] is False


def test_source_hash_audit_is_live_and_passes() -> None:
    from deuteron_wigner.bridge.c411_c117_i2_finite_c43_adapter import source_hash_audit

    record = source_hash_audit()
    assert record["all_pass"] is True
    assert record["C410_all_pass"] is True


def test_mutation_surface_has_384_entries() -> None:
    rows = [mutate_live_c411(i) for i in range(384)]
    assert len(rows) == 384
    assert all(row["pass"] for row in rows)
    assert len({row["root"] for row in rows}) == 384


def test_content_root_is_deterministic_for_contract() -> None:
    record = adapter_contract_record()
    assert record["root"] == content_root({key: value for key, value in record.items() if key != "root"})
