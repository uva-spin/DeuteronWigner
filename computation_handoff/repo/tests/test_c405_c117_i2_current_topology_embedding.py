from __future__ import annotations

import inspect

import numpy as np
import pytest
from scipy.sparse import csr_matrix, eye

from deuteron_wigner.bridge import c405_c117_i2_current_topology_embedding as c405
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    external_modes,
)


EXPECTED_DIMENSIONS = {
    "K9": (6, 1344, 1350),
    "K11": (6, 2700, 2706),
    "K13": (6, 4752, 4758),
}
EXPECTED_ASSIGNMENTS = {
    "J_qJ_q": ((),),
    "J_qJ_g": (("BRA",), ("KET",)),
    "J_gJ_q": (("BRA",), ("KET",)),
    "J_gJ_g": (
        ("BRA", "BRA"),
        ("BRA", "KET"),
        ("KET", "BRA"),
        ("KET", "KET"),
    ),
}


def test_frozen_source_hashes_and_topology_conflicts_are_explicit():
    hashes = c405.source_file_hashes()
    audit = c405.topology_authority_audit()
    assert hashes["all_match"] is True
    assert len(hashes["rows"]) == 13
    assert audit["product_count"] == 4
    assert audit["program_count"] == 8
    assert audit["graph_mapping_conflicts"] == 3
    assert audit["C119_incomplete_current_pair_programs"] == 8
    assert audit["C119_leaf_programs_with_derivative_overlap_risk"] == 4
    assert audit["C126_product_level_single_current_reference_defects"] == 4
    assert audit["C192_source_gluon_derivative_field_slot_bound"] is True
    assert audit["C192_external_BRA_KET_leg_mapping_bound"] is False
    assert audit["C192_mixed_current_orders_kept_separate"] is True
    assert audit["C192_factor_two_merge_forbidden"] is True
    source_slot = c405.gluon_source_slot_authority()
    assert source_slot["derivative_source_field_slot"] == 2
    assert source_slot["derivative_source_color_slot"] == "c"
    assert source_slot["mixed_current_orders_kept_separate"] is True
    assert source_slot["factor_two_merge_forbidden"] is True
    assert source_slot["external_BRA_KET_leg_mapping"] == "MISSING_NOT_ZERO"
    assert source_slot["normal_ordering_descendant_bound"] is False
    assert source_slot["complete_numerical_gluon_current_matrix"] is False
    assert all(source_slot["source_checks"].values())
    assert audit["source_qualified_product_topology_rows"] == 0
    assert audit["C125_witness_count_once_identity_bound"] is True
    assert audit["C405_conditional_kernel_to_C125_witness_map_bound"] is False
    assert audit["complete_C117_action"] is False
    rows = {row["product"]: row for row in audit["products"]}
    assert rows["J_qJ_g"]["C115_C125_graph_agreement"] is True
    for product in ("J_qJ_q", "J_gJ_q", "J_gJ_g"):
        assert rows[product]["C115_C125_graph_agreement"] is False


def test_current_pair_grammar_uses_two_ordered_current_identities():
    grammar = c405.current_pair_grammar()
    assert grammar["all_products_have_two_current_ids"] is True
    source_slot = c405.gluon_source_slot_authority()
    assert source_slot["classification"] == (
        "SOURCE_FIELD_SLOT_ORDER_CLOSED_EXTERNAL_LEG_NORMAL_ORDER_MAPPING_UNRESOLVED"
    )
    rows = {row["product"]: row for row in grammar["rows"]}
    assert rows["J_qJ_q"]["currents"] == ("quark_current", "quark_current")
    assert rows["J_qJ_g"]["currents"] == ("quark_current", "gluon_current")
    assert rows["J_gJ_q"]["currents"] == ("gluon_current", "quark_current")
    assert rows["J_gJ_g"]["currents"] == ("gluon_current", "gluon_current")
    assert rows["J_qJ_g"]["adjoint_product"] == "J_gJ_q"
    assert rows["J_gJ_q"]["adjoint_product"] == "J_qJ_g"
    assert all(not row["normal_ordered_matrix_element_complete"] for row in rows.values())


def test_derivative_candidate_axis_is_complete_and_has_no_default():
    for product, expected in EXPECTED_ASSIGNMENTS.items():
        assert c405.derivative_assignments(product) == expected
    inventory = c405.ordered_derivative_inventory()
    assert inventory["row_count"] == 27
    assert inventory["assignments_per_resolution"] == 9
    assert inventory["maximum_adjoint_residual"] == 0.0
    assert inventory["all_zero_mode_diagonals_exact"] is True
    assert inventory["no_default_derivative_leg"] is True
    assert inventory["source_ordered_c_field_mapped_to_external_leg"] is False
    with pytest.raises(RuntimeError, match="no default ordered gluon derivative leg"):
        c405.apply_unqualified_gluon_derivative()


def test_derivative_assignment_adjoint_rule_and_exact_mode_factors():
    partner, legs = c405.adjoint_derivative_assignment("J_qJ_g", ("BRA",))
    assert (partner, legs) == ("J_gJ_q", ("KET",))
    bra = c405.ordered_partition_kernel_exact("K9", "J_qJ_g", ("BRA",))
    ket_partner = c405.ordered_partition_kernel_exact("K9", partner, legs)
    assert bra == tuple(tuple(ket_partner[j][i] for j in range(len(ket_partner))) for i in range(len(bra)))
    # K9 partitions have k_g = 1,2,3,4; kappa(0,1)=1.
    assert bra[0][1] == 1
    ket = c405.ordered_partition_kernel_exact("K9", "J_qJ_g", ("KET",))
    assert ket[0][1] == 2
    with pytest.raises(ValueError, match="requires exactly 1"):
        c405.ordered_partition_kernel_exact("K9", "J_qJ_g", ())
    with pytest.raises(ValueError, match="BRA or KET"):
        c405.ordered_partition_kernel_exact("K9", "J_qJ_g", ("LEFT",))


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_ordered_partition_kernels_sparse_matrix_free_and_adjoint(resolution):
    rng = np.random.default_rng(sum(EXPECTED_DIMENSIONS[resolution]))
    for product, assignments in EXPECTED_ASSIGNMENTS.items():
        for derivative_legs in assignments:
            matrix = c405.ordered_partition_kernel_csr(
                resolution, product, derivative_legs
            )
            vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
            direct = c405.apply_ordered_partition_kernel(
                resolution, product, derivative_legs, vector
            )
            assert np.linalg.norm(matrix @ vector - direct) == 0.0
            assert np.array_equal(matrix.diagonal(), np.zeros(matrix.shape[0]))
            partner, partner_legs = c405.adjoint_derivative_assignment(
                product, derivative_legs
            )
            partner_matrix = c405.ordered_partition_kernel_csr(
                resolution, partner, partner_legs
            )
            assert np.linalg.norm((matrix.getH() - partner_matrix).data) == 0.0


def test_literal_scale_ledger_exposes_product_dependent_unresolved_closure():
    expected = {
        "J_qJ_q": {"L": 0, "pi": -1, "K": 1},
        "J_qJ_g": {"L": -1, "pi": 0, "K": 1},
        "J_gJ_q": {"L": -1, "pi": 0, "K": 1},
        "J_gJ_g": {"L": -2, "pi": 1, "K": 1},
    }
    for product, exponents in expected.items():
        record = c405.literal_source_scale_ledger(product)
        assert record["known_post_exponents"] == exponents
        assert record["correction_required_for_historical_C126_zero_exponent_claim"] == {
            key: -value for key, value in exponents.items()
        }
        assert record["numerical_prefactor_ready"] is False
        assert record["classification"].endswith("NOT_NORMALIZATION_AUTHORITY")


def test_normalization_audit_is_fail_closed_and_two_current_aware():
    audit = c405.normalization_closure_audit()
    assert len(audit["rows"]) == 4
    assert audit["complete_numeric_prefactors"] == 0
    assert audit["no_default_normalization"] is True
    assert audit["literal_known_exponents_are_product_dependent"] is True
    assert audit["complete_C117_action"] is False
    qq = c405.symbolic_prefactor_program("J_qJ_q", ())
    assert qq["currents"] == ("quark_current", "quark_current")
    assert "LEFT_QUARK_CURRENT" in qq["program"] and "RIGHT_QUARK_CURRENT" in qq["program"]
    assert qq["ordered_derivative_factor_count"] == 0
    assert qq["derivative_factor_double_count_forbidden"] is True
    qg = c405.symbolic_prefactor_program("J_qJ_g", ("KET",))
    assert qg["ordered_derivative_factor_count"] == 1
    assert qg["current_slots_with_derivative_extracted_once"] == (
        "LEFT_QUARK_CURRENT",
        "RIGHT_GLUON_CURRENT[ORDERED_DERIVATIVE_MODE_FACTOR_EXTRACTED_ONCE]",
    )
    assert qg["derivative_factor_double_count_forbidden"] is True
    with pytest.raises(RuntimeError, match="cannot evaluate a complete C117 prefactor"):
        c405.evaluate_complete_prefactor()


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_conditional_qg_current_family_sparse_matrix_free_and_adjoint(resolution):
    mode = external_modes(resolution)[0]
    dimension = EXPECTED_DIMENSIONS[resolution][1]
    rng = np.random.default_rng(dimension + 405)
    vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    for product, assignments in EXPECTED_ASSIGNMENTS.items():
        for derivative_legs in assignments:
            matrix = c405.conditional_qg_kernel_csr(
                resolution, product, mode, derivative_legs
            )
            direct = c405.apply_conditional_qg_kernel(
                resolution, product, mode, derivative_legs, vector
            )
            assert matrix.shape == (dimension, dimension)
            assert np.linalg.norm(matrix @ vector - direct) < 2e-11
            partner, partner_legs = c405.adjoint_derivative_assignment(
                product, derivative_legs
            )
            partner_matrix = c405.conditional_qg_kernel_csr(
                resolution, partner, mode, partner_legs
            )
            assert np.linalg.norm((matrix.getH() - partner_matrix).data) < 2e-11
            record = c405.conditional_kernel_record(
                resolution, product, mode, derivative_legs
            )
            assert record["source_qualified_product_topology"] is False
            assert record["classification"].endswith("NOT_OPERATOR_BINDING")
            assert record["complete_C117_action"] is False


def test_conditional_validation_has_27_nonbinding_rows():
    validation = c405.conditional_kernel_validation()
    assert validation["row_count"] == 27
    assert validation["pass"] is True
    assert validation["maximum_sparse_matrix_free_residual"] < 2e-11
    assert validation["maximum_adjoint_residual"] < 2e-11
    assert validation["source_qualified_product_topology"] is False
    assert validation["rank_status"] == "RANK_NOT_EVALUATED"


def test_direct_sum_axis_and_exact_cross_sector_zero_certificate():
    for resolution, (q, qg, total) in EXPECTED_DIMENSIONS.items():
        axis = c405.direct_sum_axis_record(resolution)
        assert (axis["q_dimension"], axis["qg_dimension"], axis["direct_sum_dimension"]) == (
            q,
            qg,
            total,
        )
        assert axis["q_diagonal_block_status"] == "UNAVAILABLE_NOT_ZERO_FOR_C117_I2"
        certificate = c405.exact_cross_sector_zero_certificate(resolution)
        assert certificate["cross_sector_zero_blocks"] == 8
        assert certificate["q_diagonal_block_inferred_zero"] is False
        assert all(row["status"] == "EXACT_ZERO_WITH_OPERATOR_PROOF" for row in certificate["rows"])


def test_explicit_direct_sum_requires_both_blocks_and_rejects_bad_inputs():
    q, qg, total = EXPECTED_DIMENSIONS["K9"]
    q_block = eye(q, dtype=np.complex128, format="csr")
    qg_block = 2.0 * eye(qg, dtype=np.complex128, format="csr")
    matrix = c405.assemble_explicit_direct_sum_csr(
        "K9", q_block=q_block, qg_block=qg_block
    )
    vector = np.arange(total, dtype=np.float64).astype(np.complex128)
    direct = c405.apply_explicit_direct_sum(
        "K9", q_block=q_block, qg_block=qg_block, vector=vector
    )
    assert matrix.shape == (total, total)
    assert np.linalg.norm(matrix @ vector - direct) == 0.0
    assert matrix[:q, q:].nnz == 0 and matrix[q:, :q].nnz == 0
    with pytest.raises(ValueError, match="q_block must have shape"):
        c405.assemble_explicit_direct_sum_csr(
            "K9", q_block=eye(q + 1), qg_block=qg_block
        )
    bad = q_block.astype(np.complex128).copy()
    bad.data[0] = np.nan
    with pytest.raises(ValueError, match="nonfinite"):
        c405.assemble_explicit_direct_sum_csr(
            "K9", q_block=bad, qg_block=qg_block
        )
    with pytest.raises(RuntimeError, match="q->q diagonal block is unavailable"):
        c405.assemble_with_missing_q_block()


def test_direct_sum_linear_operator_rmatvec_matches_sparse_adjoint():
    q, qg, total = EXPECTED_DIMENSIONS["K9"]
    q_block = csr_matrix(np.diag(np.arange(1, q + 1) * (1.0 + 0.25j)))
    qg_diag = np.linspace(0.5, 1.5, qg) * (1.0 - 0.5j)
    qg_block = csr_matrix((qg_diag, (np.arange(qg), np.arange(qg))), shape=(qg, qg))
    matrix = c405.assemble_explicit_direct_sum_csr(
        "K9", q_block=q_block, qg_block=qg_block
    )
    operator = c405.explicit_direct_sum_linear_operator(
        "K9", q_block=q_block, qg_block=qg_block
    )
    rng = np.random.default_rng(4059)
    vector = rng.normal(size=total) + 1j * rng.normal(size=total)
    assert np.linalg.norm(operator @ vector - matrix @ vector) == 0.0
    assert np.linalg.norm(operator.rmatvec(vector) - matrix.getH() @ vector) == 0.0


def test_embedding_validation_and_partial_records_do_not_zero_missing_q_block():
    validation = c405.direct_sum_embedding_validation()
    assert validation["pass"] is True
    assert validation["maximum_sparse_direct_residual"] == 0.0
    assert validation["maximum_cross_sector_zero_residual"] == 0.0
    assert validation["qg_only_promoted_to_complete_operator"] is False
    partial = c405.qg_partial_embedding_record("K9", "J_qJ_g")
    assert partial["zero_fill_missing_q_block"] is False
    assert partial["complete_direct_sum_operator"] is False
    assert partial["classification"].endswith("NOT_COMPLETE_OPERATOR")


def test_binding_overlay_advances_boundary_not_complete_action_count():
    inventory = c405.c396_binding_inventory_with_c405_boundary()
    summary = c405.binding_update_summary()
    assert inventory["total_rows"] == 57
    assert inventory["C405_C117_I2_boundary_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert inventory["C396_19_coordinate_forward_map_ready"] is False
    assert summary["current_complete_numerical_apply_paths"] == 6
    assert summary["complete_apply_count_changed"] is False
    assert summary["historical_graph_mapping_conflicts"] == 3
    assert summary["historical_incomplete_C119_programs"] == 8
    assert summary["historical_derivative_overlap_programs"] == 4
    assert summary["C126_program_level_single_current_reference_defects"] == 8
    assert summary["C126_programs_with_extra_derivative_reference"] == 4
    assert summary["C250_two_current_reference_repairs_pair_identity"] is True
    assert summary["ordered_derivative_candidate_rows"] == 27
    assert summary["conditional_qg_kernel_rows"] == 27
    assert summary["complete_numeric_prefactors"] == 0
    assert summary["source_qualified_product_topology_rows"] == 0
    rows = [row for row in inventory["rows"] if row["coordinate_id"] == "c_C117_1"]
    assert len(rows) == 3
    for row in rows:
        assert row["qg_partial_block_available"] is True
        assert row["q_sector_diagonal_block_status"] == "UNAVAILABLE_NOT_ZERO"
        assert row["numerical_apply_path"] is None
        assert row["selected"] is False and row["zeroed"] is False


def test_complete_c117_action_fails_closed_and_source_has_no_forbidden_shortcuts():
    with pytest.raises(RuntimeError, match="cannot apply a complete C117 I2 action"):
        c405.apply_complete_c117_i2("K9", np.zeros(1))
    modules = (
        c405.topology,
        c405.derivative_order,
        c405.normalization,
        c405.conditioned,
        c405.embedding,
        c405.bindings,
    )
    source = "\n".join(inspect.getsource(module) for module in modules)
    forbidden = (
        "c144",
        "minimum_norm",
        '"physical_fit_authorized": True',
        "resolution_average",
        "zero_fill_missing_q_block\": True",
    )
    for token in forbidden:
        assert token not in source


def test_conditional_linear_operator_rmatvec_matches_source_order_adjoint():
    resolution = "K9"
    mode = external_modes(resolution)[0]
    product = "J_qJ_g"
    legs = ("BRA",)
    matrix = c405.conditional_qg_kernel_csr(resolution, product, mode, legs)
    operator = c405.conditional_qg_linear_operator(resolution, product, mode, legs)
    rng = np.random.default_rng(40517)
    vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
    assert np.linalg.norm(operator @ vector - matrix @ vector) < 2e-11
    assert np.linalg.norm(operator.rmatvec(vector) - matrix.getH() @ vector) < 2e-11


def test_completion_record_is_truthful_and_fail_closed():
    completion = c405.completion_record()
    assert completion["phase_result"] == (
        "PHASE_COMPLETE_AT_CONDITIONAL_PRIMITIVE_AND_SOURCE_AUDIT_SCOPE"
    )
    assert completion["source_files_hash_verified"] is True
    assert completion["historical_graph_mapping_conflicts"] == 3
    assert completion["historical_incomplete_C119_programs"] == 8
    assert completion["historical_derivative_overlap_programs"] == 4
    assert completion["C126_program_level_single_current_reference_defects"] == 8
    assert completion["C126_programs_with_extra_derivative_reference"] == 4
    assert completion["C250_two_current_reference_repairs_pair_identity"] is True
    assert completion["ordered_derivative_assignment_rows"] == 27
    assert completion["conditional_qg_kernel_rows"] == 27
    assert completion["complete_numeric_prefactors"] == 0
    assert completion["complete_C117_numerical_apply_paths"] == 0
    assert completion["complete_C396_numerical_apply_paths"] == 6
    assert completion["full_C117_I2_action_ready"] is False
    assert completion["full_C396_forward_map_ready"] is False
    assert completion["rank_status"] == "RANK_NOT_EVALUATED"
    assert completion["activation_gate_status"] == "NOT_READY"
