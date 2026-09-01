from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import RESOLUTION_LABELS
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    EXPECTED_SCALARS,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.axis import (
    external_mode_axis,
    intermediate_axis,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.descendants import (
    same_species_weight_exact,
)
from deuteron_wigner.bridge.c409_c117_i2_derivative_density_reconciliation import (
    STATUS,
    apply_complete_c117_i2,
    apply_complete_jgjg_direct_sum,
    apply_jgjg_qg,
    apply_reduced_derivative_density_spatial,
    binding_update_summary,
    c114_inverse_square_exact,
    c396_binding_inventory_with_c409_reconciliation,
    c406_gluon_current_pair_exact,
    c409_reconstructed_jgjg_weight_exact,
    completion_record,
    derivative_count_authority,
    derivative_count_validation,
    extra_derivative_multiplier_exact,
    jgjg_qg_csr,
    jgjg_qg_linear_operator,
    jgjg_qg_validation,
    qg_partial_embedding_record,
    reduced_derivative_density_spatial_csr,
    reduced_transverse_authority,
    scale_power_reconciliation,
    scientific_boundary_record,
    source_hash_audit,
)


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_reduced_spatial_sparse_matches_independent_apply(resolution: str) -> None:
    matrix = reduced_derivative_density_spatial_csr(resolution)
    rng = np.random.default_rng(40910 + RESOLUTION_LABELS.index(resolution))
    vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
    residual = np.linalg.norm(
        matrix @ vector - apply_reduced_derivative_density_spatial(resolution, vector)
    )
    assert residual < 5e-11


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_jgjg_sparse_matches_matrix_free_and_is_hermitian(resolution: str) -> None:
    matrix = jgjg_qg_csr(resolution)
    rng = np.random.default_rng(40920 + RESOLUTION_LABELS.index(resolution))
    vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
    assert np.linalg.norm(matrix @ vector - apply_jgjg_qg(resolution, vector)) < 5e-10
    assert np.linalg.norm((matrix - matrix.getH()).data) < 5e-12


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_jgjg_linear_operator_adjoint_matches_sparse(resolution: str) -> None:
    matrix = jgjg_qg_csr(resolution)
    operator = jgjg_qg_linear_operator(resolution)
    rng = np.random.default_rng(40930 + RESOLUTION_LABELS.index(resolution))
    vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
    assert np.linalg.norm(operator @ vector - matrix @ vector) < 5e-10
    assert np.linalg.norm(operator.rmatvec(vector) - matrix.getH() @ vector) < 5e-10


def test_status_and_source_hash_audit_are_frozen() -> None:
    assert STATUS.startswith("C409_C117_I2_JGJG_DERIVATIVE_COUNT_RECONCILED")
    audit = source_hash_audit()
    assert audit["all_pass"] is True
    assert audit["row_count"] == 14
    assert {row["owner"] for row in audit["rows"]} == {
        "C45", "C47", "C114", "C115", "C117", "C119", "C124", "C126",
        "C192", "C403", "C404", "C406", "C407", "C408",
    }


def test_derivative_count_authority_counts_each_source_current_once() -> None:
    record = derivative_count_authority()
    row = next(item for item in record["products"] if item["product"] == "J_gJ_g")
    assert row["source_gluon_current_count"] == 2
    assert row["source_longitudinal_derivative_count"] == 2
    assert record["C119_extra_derivative_leaf_independent_on_C406_C407_route"] is False
    assert record["C124_C126_derivative_density_pi_k_over_L_independent_on_C406_C407_route"] is False


def test_inverse_square_and_current_pair_reconstruct_c407_exactly() -> None:
    for resolution in RESOLUTION_LABELS:
        for external_id, external_k in external_mode_axis(resolution, "GLUON", "qg->qg"):
            for row in intermediate_axis(
                resolution, "GLUON", "qg->qg", external_k, external_id
            ):
                expected = same_species_weight_exact(
                    "GLUON", external_k, row.intermediate_k
                )
                actual = c409_reconstructed_jgjg_weight_exact(
                    external_k, row.intermediate_k
                )
                assert actual == expected


def test_exact_factor_example() -> None:
    external = Fraction(1, 1)
    intermediate = Fraction(2, 1)
    assert c114_inverse_square_exact(external, intermediate) == 1
    assert c406_gluon_current_pair_exact(external, intermediate) == Fraction(9, 8)
    assert c409_reconstructed_jgjg_weight_exact(external, intermediate) == Fraction(27, 8)
    assert EXPECTED_SCALARS["J_gJ_g"] == 3


def test_q0_zero_transfer_is_rejected() -> None:
    with pytest.raises(ValueError, match="zero transfer"):
        c114_inverse_square_exact(Fraction(2), Fraction(2))


def test_noninteger_same_boundary_transfer_is_rejected() -> None:
    with pytest.raises(ValueError, match="integer"):
        c114_inverse_square_exact(Fraction(1), Fraction(3, 2))


def test_extra_derivative_multiplier_is_audit_only_and_changes_generic_weight() -> None:
    weight = c409_reconstructed_jgjg_weight_exact(Fraction(1), Fraction(2))
    assert extra_derivative_multiplier_exact(Fraction(2)) == 2
    assert weight * extra_derivative_multiplier_exact(Fraction(2)) != weight
    with pytest.raises(ValueError, match="positive"):
        extra_derivative_multiplier_exact(Fraction(0))


def test_scale_power_reconciliation_closes_dimensionless_subset() -> None:
    record = scale_power_reconciliation()
    assert record["source_derivative_count"] == 2
    assert record["net_pi_power"] == 0
    assert record["net_L_power"] == 0
    assert record["dimensionless_longitudinal_subset"] is True
    assert record["extra_factors_admitted"] is False


def test_reduced_transverse_authority_is_route_specific() -> None:
    record = reduced_transverse_authority()
    assert record["member_multiplier"] == 1
    assert record["C124_generic_derivative_density_semantics_mutated"] is False
    assert record["transverse_derivative_applied_again"] is False
    assert record["color_C_A_applied_again"] is False


def test_derivative_count_validation_has_exact_62_rows() -> None:
    record = derivative_count_validation()
    assert record["pass"] is True
    assert record["row_count"] == 62
    assert record["all_exact_C407_reconstructions"] is True
    assert record["extra_derivative_factors_used_in_C409"] == 0
    assert record["rows_changed_by_illicit_C119_extra_leaf"] > 0
    assert record["rows_changed_by_illicit_C124_extra_member_derivative"] > 0


def test_jgjg_validation_closes_three_qg_primitives_only() -> None:
    record = jgjg_qg_validation()
    assert record["pass"] is True
    assert record["row_count"] == 3
    assert record["source_routed_J_gJ_g_qg_paths"] == 3
    assert record["q_sector_zero_claimed"] is False
    assert record["extra_derivative_factors_applied"] == 0
    assert record["extra_color_Casimir_applied"] == 0
    assert record["complete_C117_action"] is False


def test_jgjg_partial_embedding_refuses_q_sector_zero_fill() -> None:
    record = qg_partial_embedding_record("K9")
    assert record["available_block"] == "qg->qg number-preserving product-block primitive"
    assert record["missing_q_block_zero_filled"] is False
    assert record["complete_direct_sum_operator"] is False
    assert "UNRESOLVED_NOT_ZERO" in record["q_sector_status"]


def test_nonfinite_vector_is_rejected() -> None:
    matrix = jgjg_qg_csr("K9")
    vector = np.zeros(matrix.shape[0], dtype=np.complex128)
    vector[0] = np.nan
    with pytest.raises(ValueError, match="nonfinite"):
        apply_jgjg_qg("K9", vector)


def test_wrong_vector_shape_is_rejected() -> None:
    with pytest.raises(ValueError, match="shape"):
        apply_jgjg_qg("K9", np.zeros(3))


def test_binding_overlay_preserves_six_complete_c396_paths() -> None:
    inventory = c396_binding_inventory_with_c409_reconciliation()
    assert inventory["total_rows"] == 57
    assert inventory["C409_C117_I2_reconciliation_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert inventory["source_routed_product_block_primitive_paths"] == 12
    rows = [row for row in inventory["rows"] if row["coordinate_id"] == "c_C117_1"]
    assert len(rows) == 3
    assert all("PRODUCT_BLOCK_PRIMITIVE_READY" in row["J_gJ_g_qg_status"] for row in rows)
    assert all(row["numerical_apply_path"] is None for row in rows)


def test_binding_summary_records_12_primitives_without_complete_action() -> None:
    summary = binding_update_summary()
    assert summary["derivative_count_rows"] == 62
    assert summary["source_routed_product_block_primitive_paths"] == 12
    assert summary["J_gJ_g_qg_validation_pass"] is True
    assert summary["J_gJ_g_q_sector_ready"] is False
    assert summary["current_complete_numerical_apply_paths"] == 6
    assert summary["complete_C117_numerical_apply_paths"] == 0


def test_scientific_boundary_is_truthful() -> None:
    record = scientific_boundary_record()
    assert record["source_routed_product_block_primitive_paths"] == 12
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["physical_fit_authorized"] is False
    assert record["activation_gate_status"] == "NOT_READY"


def test_completion_record_preserves_nonclaims() -> None:
    record = completion_record()
    assert record["J_gJ_g_number_preserving_qg_product_block_ready"] is True
    assert record["J_gJ_g_q_sector_complete"] is False
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["full_C117_I2_action_ready"] is False
    assert record["full_C396_forward_map_ready"] is False
    assert record["physical_fit_authorized"] is False


def test_complete_actions_fail_closed() -> None:
    with pytest.raises(RuntimeError, match="complete C117 I2"):
        apply_complete_c117_i2()
    with pytest.raises(RuntimeError, match="complete J_gJ_g"):
        apply_complete_jgjg_direct_sum()


def test_python39_static_compatibility_surface() -> None:
    root = Path(__file__).resolve().parents[1]
    package = root / "src/deuteron_wigner/bridge/c409_c117_i2_derivative_density_reconciliation"
    for path in sorted(package.glob("*.py")):
        text = path.read_text(encoding="utf-8")
        ast.parse(text)
        assert ".bit_count(" not in text
        assert "strict=" not in text
        # Reject runtime-evaluated module aliases of the form Name = A | B.
        tree = ast.parse(text)
        for node in tree.body:
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                assert not (
                    isinstance(value, ast.BinOp) and isinstance(value.op, ast.BitOr)
                ), path
