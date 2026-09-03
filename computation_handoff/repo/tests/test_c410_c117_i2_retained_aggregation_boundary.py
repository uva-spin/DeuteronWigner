from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re

import numpy as np
import pytest

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import RESOLUTION_LABELS
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import direct_sum_axis_record
from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    GluonPairMode,
    MISSING_NORMALIZATION_OBJECT,
    PRODUCTS,
    SOURCE_COEFFICIENT,
    STATUS,
    aggregation_authority,
    apply_complete_c117_i2,
    apply_product_block,
    apply_q_sector_jgjg_connected,
    apply_retained_connected_current_square,
    apply_source_reduced_c117_i2_shape,
    apply_source_routed_jgjg_direct_sum,
    binding_update_summary,
    complete_c117_i2_csr,
    completion_record,
    count_once_aggregation_record,
    c396_binding_inventory_with_c410_aggregation,
    normalization_boundary_record,
    normalization_capsule_schema,
    ordered_pair_creation_coefficient,
    pair_creation_state,
    product_block_csr,
    q_sector_jgjg_connected_csr,
    q_sector_vacuum_projection_certificate,
    q_sector_vacuum_projection_validation,
    retained_aggregation_validation,
    retained_connected_current_square_csr,
    scientific_boundary_record,
    source_hash_audit,
    source_reduced_c117_i2_shape_csr,
    source_reduced_c117_i2_shape_linear_operator,
    source_routed_jgjg_direct_sum_csr,
    validate_normalization_capsule,
    vacuum_pair_validation,
    vacuum_routing_authority,
)


def _vector(resolution: str, seed: int = 410) -> np.ndarray:
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    rng = np.random.default_rng(seed + RESOLUTION_LABELS.index(resolution))
    return rng.normal(size=dimension) + 1j * rng.normal(size=dimension)


def _valid_capsule() -> dict:
    return {
        "capsule_id": "C410-DIAGNOSTIC-STRUCTURAL-CAPSULE",
        "resolution": "K9",
        "scheme_id": "PROJECT_C117_RI_SMOM_V1",
        "operator_id": "O_C117_1",
        "finite_C43_adapter_definition": "future source-owned adapter",
        "field_normalization": "future source-owned field normalization",
        "external_state_normalization": "future source-owned state normalization",
        "Pminus_to_M2_conversion": "future source-owned M2 conversion",
        "wavepacket_definition": "future normalized finite-cell wavepacket",
        "units": "GeV^2",
        "source_locator": "diagnostic structural fixture only",
        "source_sha256": "a" * 64,
        "signature": "NOT-A-PHYSICAL-SIGNATURE",
        "no_default": True,
    }


def test_status_and_resolution_surface_are_exact() -> None:
    assert STATUS.startswith("C410_C117_I2_Q_SECTOR_VACUUM_ROUTING")
    assert RESOLUTION_LABELS == ("K9", "K11", "K13")
    assert PRODUCTS == ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
    assert SOURCE_COEFFICIENT == -0.5


def test_source_hash_audit_covers_all_frozen_owners() -> None:
    record = source_hash_audit()
    assert record["all_pass"] is True
    assert record["row_count"] == 12
    assert {row["owner"] for row in record["rows"]} == {
        "C114", "C117", "C119", "C129", "C131", "C136", "C192",
        "C259", "C260", "C274", "C408", "C409",
    }


def test_vacuum_routing_authority_does_not_claim_full_source_zero() -> None:
    record = vacuum_routing_authority()
    assert record["full_source_vacuum_cnumber_claimed_zero"] is False
    assert record["full_source_pair_branch_discarded"] is False
    assert "EXACT_ZERO" in record["retained_connected_status"]
    assert record["identity_shift_inserted"] is False
    assert record["complete_C117_action"] is False


def test_aggregation_authority_preserves_four_source_orders_once() -> None:
    record = aggregation_authority()
    assert record["product_count"] == 4
    assert tuple(row["product"] for row in record["products"]) == PRODUCTS
    assert all(row["multiplicity"] == 1 for row in record["products"])
    assert record["mixed_orders_kept_separate"] is True
    assert record["factor_two_substitution_used"] is False
    assert record["source_product_count_once_structure_closed"] is True
    assert record["complete_target_aggregation_closed"] is False


def test_scientific_boundary_is_truthful() -> None:
    record = scientific_boundary_record()
    assert record["source_routed_product_block_primitive_paths"] == 12
    assert record["retained_connected_aggregate_shape_paths"] == 3
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["activation_gate_status"] == "NOT_READY"


def test_gluon_pair_mode_record_is_exact() -> None:
    record = GluonPairMode(Fraction(3, 2), 4).to_record()
    assert record["k"]["exact"] == "3/2"
    assert record["k"]["numerator"] == 3
    assert record["k"]["denominator"] == 2
    assert record["color"] == 4


def test_ordered_pair_creation_rejects_invalid_generator() -> None:
    mode = GluonPairMode(Fraction(1), 0)
    with pytest.raises(ValueError):
        ordered_pair_creation_coefficient(-1, mode, mode)
    with pytest.raises(ValueError):
        ordered_pair_creation_coefficient(8, mode, mode)


def test_pair_creation_rejects_nonpositive_or_duplicate_modes() -> None:
    with pytest.raises(ValueError):
        pair_creation_state(0, 3, (0, 3))
    with pytest.raises(ValueError):
        pair_creation_state(0, 3, (1, 1, 2))
    with pytest.raises(ValueError):
        pair_creation_state(0, 0, (1, 2))


def test_equal_momentum_pair_state_cancels_exactly() -> None:
    for generator in range(8):
        record = pair_creation_state(generator, 2, (1,))
        assert record["vacuum_pair_norm_squared"] == 0.0
        assert record["nonzero_pair_count"] == 0


def test_unequal_momentum_pair_state_is_nonzero_for_su3_generators() -> None:
    norms = [pair_creation_state(generator, 3, (1, 2))["vacuum_pair_norm_squared"] for generator in range(8)]
    assert all(value > 0.0 for value in norms)
    assert np.isclose(sum(norms), 3.0, rtol=0.0, atol=2e-14)


def test_pair_creation_source_order_reduces_to_antisymmetric_momentum_difference() -> None:
    first = GluonPairMode(Fraction(1), 1)
    second = GluonPairMode(Fraction(2), 2)
    forward = ordered_pair_creation_coefficient(0, first, second)
    reverse = ordered_pair_creation_coefficient(0, second, first)
    expected = (forward + reverse)
    record = pair_creation_state(0, 3, (1, 2))
    matches = [row for row in record["nonzero_pair_amplitudes"] if row["first"]["color"] == 1 and row["second"]["color"] == 2]
    assert len(matches) == 1
    actual = complex(matches[0]["real"], matches[0]["imag"])
    assert np.isclose(actual, expected, rtol=0.0, atol=2e-14)


def test_vacuum_pair_validation_passes_and_retains_nonzero_branch() -> None:
    record = vacuum_pair_validation()
    assert record["pass"] is True
    assert record["row_count"] == 8
    assert record["pair_creation_branch_nonzero_witness"] is True
    assert record["physical_vacuum_cnumber_computed"] is False
    assert record["summed_unequal_momentum_vacuum_pair_norm_squared"] > 0.0
    assert record["summed_equal_momentum_vacuum_pair_norm_squared"] == 0.0


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_q_sector_vacuum_projection_certificate_is_explicit_not_absence(resolution: str) -> None:
    record = q_sector_vacuum_projection_certificate(resolution)
    assert record["pass"] is True
    assert record["full_source_pair_branch_status"] == "SOURCE_PRESENT_AND_NONZERO_WITNESS"
    assert record["production_vacuum_scalar_evaluated"] is False
    assert record["retained_connected_block"] == "EXACT_ZERO_WITH_VACUUM_PROJECTION_PROOF"
    assert record["zero_by_absence_or_truncation"] is False
    assert record["identity_shift_inserted"] is False


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_q_sector_connected_matrix_and_action_are_exact_zero(resolution: str) -> None:
    matrix = q_sector_jgjg_connected_csr(resolution)
    vector = np.arange(matrix.shape[0], dtype=np.float64) + 1j
    assert matrix.shape == (6, 6)
    assert matrix.nnz == 0
    assert np.array_equal(apply_q_sector_jgjg_connected(resolution, vector), np.zeros_like(vector))


def test_q_sector_connected_action_fails_closed_on_bad_vectors() -> None:
    with pytest.raises(ValueError):
        apply_q_sector_jgjg_connected("K9", np.ones(5))
    vector = np.ones(6, dtype=np.complex128)
    vector[0] = np.nan
    with pytest.raises(ValueError):
        apply_q_sector_jgjg_connected("K9", vector)


def test_q_sector_projection_validation_passes_at_all_k() -> None:
    record = q_sector_vacuum_projection_validation()
    assert record["pass"] is True
    assert record["row_count"] == 3
    assert record["retained_q_sector_zero_paths"] == 3
    assert record["maximum_sparse_matrix_free_residual"] == 0.0


def test_unknown_product_is_rejected() -> None:
    with pytest.raises(KeyError):
        product_block_csr("K9", "J_bad")
    with pytest.raises(KeyError):
        apply_product_block("K9", "J_bad", _vector("K9"))


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_all_product_blocks_share_exact_direct_sum_shape(resolution: str) -> None:
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    for product in PRODUCTS:
        assert product_block_csr(resolution, product).shape == (dimension, dimension)


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_jgjg_direct_sum_has_exact_q_zero_and_c409_qg_block(resolution: str) -> None:
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    matrix = source_routed_jgjg_direct_sum_csr(resolution)
    assert matrix[:qdim, :qdim].nnz == 0
    vector = _vector(resolution, seed=1410)
    assert np.allclose(matrix @ vector, apply_source_routed_jgjg_direct_sum(resolution, vector), atol=5e-10, rtol=0.0)


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_aggregate_equals_exact_sum_of_four_products(resolution: str) -> None:
    aggregate = retained_connected_current_square_csr(resolution)
    explicit = product_block_csr(resolution, PRODUCTS[0]).copy().tocsr()
    for product in PRODUCTS[1:]:
        explicit = (explicit + product_block_csr(resolution, product)).tocsr()
    difference = (aggregate - explicit).tocsr()
    assert np.linalg.norm(difference.data) == 0.0


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_aggregate_sparse_and_matrix_free_routes_agree(resolution: str) -> None:
    vector = _vector(resolution, seed=2410)
    matrix = retained_connected_current_square_csr(resolution)
    assert np.allclose(matrix @ vector, apply_retained_connected_current_square(resolution, vector), atol=5e-10, rtol=0.0)


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_source_reduced_shape_applies_minus_one_half_once(resolution: str) -> None:
    aggregate = retained_connected_current_square_csr(resolution)
    reduced = source_reduced_c117_i2_shape_csr(resolution)
    difference = (reduced - SOURCE_COEFFICIENT * aggregate).tocsr()
    assert np.linalg.norm(difference.data) == 0.0
    vector = _vector(resolution, seed=3410)
    assert np.allclose(reduced @ vector, apply_source_reduced_c117_i2_shape(resolution, vector), atol=5e-10, rtol=0.0)


def test_source_reduced_linear_operator_agrees_with_sparse() -> None:
    resolution = "K11"
    vector = _vector(resolution, seed=4410)
    operator = source_reduced_c117_i2_shape_linear_operator(resolution)
    sparse = source_reduced_c117_i2_shape_csr(resolution)
    assert np.allclose(operator @ vector, sparse @ vector, atol=5e-10, rtol=0.0)
    assert np.allclose(operator.rmatvec(vector), sparse.getH() @ vector, atol=5e-10, rtol=0.0)


def test_aggregate_actions_fail_closed_on_bad_vectors() -> None:
    dimension = int(direct_sum_axis_record("K9")["direct_sum_dimension"])
    with pytest.raises(ValueError):
        apply_retained_connected_current_square("K9", np.ones(dimension - 1))
    bad = np.ones(dimension, dtype=np.complex128)
    bad[-1] = np.inf
    with pytest.raises(ValueError):
        apply_retained_connected_current_square("K9", bad)


def test_count_once_record_excludes_factor_two_and_unselected_coefficients() -> None:
    record = count_once_aggregation_record()
    assert record["pass"] is True
    assert record["row_count"] == 4
    assert record["duplicate_products"] == 0
    assert record["omitted_products"] == 0
    assert record["source_minus_one_half_count"] == 1
    assert record["g_s_squared_count"] == 0
    assert record["coordinate_coefficient_count"] == 0
    assert all(row["extra_factor_two"] is False for row in record["rows"])


def test_retained_aggregation_validation_closes_only_shape_boundary() -> None:
    record = retained_aggregation_validation()
    assert record["pass"] is True
    assert record["row_count"] == 3
    assert record["source_routed_product_block_primitive_paths"] == 12
    assert record["retained_connected_aggregate_shape_paths"] == 3
    assert record["absolute_C260_operator_normalization_applied"] is False
    assert record["complete_C117_action"] is False
    assert record["maximum_hermiticity_residual"] < 5e-10
    assert record["maximum_sparse_matrix_free_residual"] < 5e-10


def test_normalization_boundary_names_exact_smallest_missing_object() -> None:
    record = normalization_boundary_record()
    assert record["smallest_missing_object"] == MISSING_NORMALIZATION_OBJECT
    assert "C260/C262" in MISSING_NORMALIZATION_OBJECT
    assert record["g_s_squared_factored"] is True
    assert record["c_C117_1_selected"] is False
    assert record["complete_C117_action"] is False


def test_normalization_capsule_schema_excludes_coefficient_and_gs_values() -> None:
    record = normalization_capsule_schema()
    assert record["no_default"] is True
    assert record["g_s_squared"] == "FACTORED_NOT_NUMERIC_FIELD"
    assert record["c_C117_1"] == "NOT_PART_OF_OPERATOR_NORMALIZATION_CAPSULE"
    assert "source_sha256" in record["required"]


def test_structurally_valid_normalization_capsule_is_not_certified_by_c410() -> None:
    record = validate_normalization_capsule(_valid_capsule())
    assert record["structurally_valid"] is True
    assert record["numerical_authority_certified_by_C410"] is False
    assert record["physical"] is False


@pytest.mark.parametrize("mutation", ("missing", "resolution", "scheme", "operator", "default", "hash"))
def test_normalization_capsule_rejects_invalid_records(mutation: str) -> None:
    record = _valid_capsule()
    if mutation == "missing":
        record.pop("wavepacket_definition")
    elif mutation == "resolution":
        record["resolution"] = "K15"
    elif mutation == "scheme":
        record["scheme_id"] = "OTHER"
    elif mutation == "operator":
        record["operator_id"] = "O_C117_2"
    elif mutation == "default":
        record["no_default"] = False
    elif mutation == "hash":
        record["source_sha256"] = "XYZ"
    with pytest.raises(ValueError):
        validate_normalization_capsule(record)


def test_complete_operator_apis_fail_closed() -> None:
    for fn in (complete_c117_i2_csr, apply_complete_c117_i2):
        with pytest.raises(RuntimeError, match="C260/C262"):
            fn("K9")


def test_c396_binding_overlay_updates_exactly_three_rows_without_increasing_count() -> None:
    record = c396_binding_inventory_with_c410_aggregation()
    assert record["total_rows"] == 57
    assert record["C410_C117_I2_aggregation_rows"] == 3
    assert record["complete_numerical_apply_paths"] == 6
    assert record["complete_C117_numerical_apply_paths"] == 0
    rows = [row for row in record["rows"] if row["coordinate_id"] == "c_C117_1"]
    assert len(rows) == 3
    assert all(row["complete_C117_action"] is False for row in rows)
    assert all(row["numerical_apply_path"] is None for row in rows)


def test_binding_summary_preserves_nonclaims() -> None:
    record = binding_update_summary()
    assert record["current_complete_numerical_apply_paths"] == 6
    assert record["complete_apply_count_changed"] is False
    assert record["source_product_count_once_aggregation_closed"] is True
    assert record["complete_target_aggregation_closed"] is False
    assert record["C260_operator_normalization_closed"] is False
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["activation_gate_status"] == "NOT_READY"


def test_completion_record_is_truthful_and_fail_closed() -> None:
    record = completion_record()
    assert record["source_hash_audit_pass"] is True
    assert record["vacuum_pair_validation_pass"] is True
    assert record["retained_aggregation_validation_pass"] is True
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["full_C117_I2_action_ready"] is False
    assert record["full_C396_forward_map_ready"] is False
    assert record["physical_fit_authorized"] is False


def test_c410_source_is_python39_compatible_and_avoids_forbidden_shortcuts() -> None:
    root = Path(__file__).resolve().parents[1]
    source_root = root / "src" / "deuteron_wigner" / "bridge" / "c410_c117_i2_retained_aggregation_boundary"
    files = sorted(source_root.glob("*.py"))
    assert len(files) == 7
    for path in files:
        text = path.read_text(encoding="utf-8")
        compile(text, str(path), "exec")
        assert ".bit_count(" not in text
        assert "strict=" not in text
        assert not re.search(r"^[A-Za-z_][A-Za-z0-9_]*\s*=.*\|.*$", text, re.MULTILINE)
        assert "c144" not in text.lower()
        assert "minimum_norm" not in text.lower()


def test_content_roots_are_deterministic() -> None:
    assert vacuum_pair_validation()["root"] == vacuum_pair_validation()["root"]
    assert retained_aggregation_validation()["root"] == retained_aggregation_validation()["root"]
    assert completion_record()["root"] == completion_record()["root"]
