from __future__ import annotations

from fractions import Fraction
import inspect

import numpy as np
import pytest

from deuteron_wigner.bridge import c404_c117_i2_longitudinal_color_primitive as c404
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    external_modes,
)


EXPECTED_PARTITIONS = {"K9": 4, "K11": 5, "K13": 6}
EXPECTED_DIMENSIONS = {"K9": 1344, "K11": 2700, "K13": 4752}


def test_partition_axis_is_exact_positive_and_k_local():
    for resolution, count in EXPECTED_PARTITIONS.items():
        rows = c404.partition_axis(resolution)
        assert len(rows) == count
        for index, row in enumerate(rows):
            assert row.partition_id == index
            assert row.k_q > 0 and row.k_g > 0
            assert row.x_q > 0 and row.x_g > 0
            assert row.x_q + row.x_g == 1
            assert row.k_q + row.k_g in {Fraction(9, 2), Fraction(11, 2), Fraction(13, 2)}


def test_q0_transfer_records_are_exact_and_conserve_total_k():
    record = c404.transfer_record("K9", 0, 3)
    assert record["n_q"]["exact"] == "3"
    assert record["n_g"]["exact"] == "-3"
    assert record["conservation_residual"] == 0
    assert record["Q0_admitted"] is True
    assert record["inverse_partial_plus_squared_dimensionless"]["exact"] == "1/9"

    zero = c404.transfer_record("K9", 2, 2)
    assert zero["Q0_admitted"] is False
    assert zero["zero_mode_status"] == "Q0_EXCLUDED_EXACT_ZERO_TRANSFER"
    assert zero["inverse_partial_plus_squared_dimensionless"]["exact"] == "0"
    assert "NOT_A_CERTIFICATE" in zero["q_sector_direct_exchange_scope"]


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_partition_transfer_sparse_matrix_free_and_symmetry(resolution):
    matrix = c404.partition_transfer_matrix_dense(resolution)
    exact = c404.partition_transfer_matrix_exact(resolution)
    count = EXPECTED_PARTITIONS[resolution]
    assert matrix.shape == (count, count)
    assert len(exact) == count
    assert np.array_equal(matrix, matrix.T)
    assert np.array_equal(np.diag(matrix), np.zeros(count))
    for bra in range(count):
        for ket in range(count):
            expected = 0.0 if bra == ket else 1.0 / float((bra - ket) ** 2)
            assert matrix[bra, ket] == expected

    rng = np.random.default_rng(count)
    vector = rng.normal(size=count) + 1j * rng.normal(size=count)
    sparse = c404.partition_transfer_matrix_csr(resolution)
    direct = c404.apply_partition_transfer(resolution, vector)
    assert np.linalg.norm(sparse @ vector - direct) == 0.0


def test_c47_axis_order_and_c403_permutation_are_explicit():
    for resolution in EXPECTED_PARTITIONS:
        record = c404.qg_factorized_axis_record(resolution)
        assert record["dimension"] == EXPECTED_DIMENSIONS[resolution]
        assert record["C47_ordering_verified"] is True
        assert record["q_sector_external_axis_in_this_primitive"] is False
        modes = c404.c47_relative_modes(resolution)
        permutation = c404.c47_to_c403_mode_permutation(resolution)
        assert len(modes) == len(permutation) == len(external_modes(resolution))
        assert sorted(permutation) == list(range(len(permutation)))
        assert tuple(external_modes(resolution)[index] for index in permutation) == modes
    # C47 begins with the CM-ground relative mode; C403's generic support list
    # has a different deterministic ordering, so an explicit permutation is required.
    assert c404.c47_relative_modes("K9")[0] == HOMode(0, 0)
    assert c404.c47_to_c403_mode_permutation("K9")[0] != 0


def test_triplet_color_products_match_exact_su3_casimirs():
    expected = {
        "J_qJ_q": 4.0 / 3.0,
        "J_qJ_g": -3.0 / 2.0,
        "J_gJ_q": -3.0 / 2.0,
        "J_gJ_g": 3.0,
    }
    matrices = {}
    for product, scalar in expected.items():
        matrix = c404.triplet_color_product_matrix(product)
        matrices[product] = matrix
        assert matrix.shape == (3, 3)
        assert np.linalg.norm(matrix - scalar * np.eye(3)) < 2e-12
        assert np.linalg.norm(matrix - matrix.conj().T) < 2e-12
        record = c404.triplet_color_product_record(product)
        assert record["source_phase_and_gluon_derivative_bound"] is False
        assert record["complete_C115_current_factor"] is False
    total = sum(matrices.values())
    assert np.linalg.norm(total - (4.0 / 3.0) * np.eye(3)) < 2e-12
    assert np.linalg.norm(matrices["J_qJ_g"] - matrices["J_gJ_q"]) < 2e-12


def test_jplus_spin_selection_is_diagonal_but_derivative_factor_is_unbound():
    matrix = c404.combined_spin_selection_matrix()
    record = c404.spin_selection_record()
    assert np.array_equal(matrix, np.eye(4))
    assert record["spin_flip_entries"] == 0
    assert record["ordered_gluon_derivative_factor_included"] is False
    assert c404.color_spin_validation()["pass"] is True


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_factorized_stress_test_sparse_matrix_free_agreement(resolution):
    mode = external_modes(resolution)[0]
    dimension = EXPECTED_DIMENSIONS[resolution]
    rng = np.random.default_rng(dimension)
    vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    for product in c404.PRODUCTS:
        sparse = c404.qg_skeleton_csr(resolution, product, mode)
        direct = c404.apply_qg_skeleton(resolution, product, mode, vector)
        assert sparse.shape == (dimension, dimension)
        assert np.linalg.norm(sparse @ vector - direct) < 2e-11
        assert np.linalg.norm((sparse - sparse.getH()).data) < 2e-11
        record = c404.skeleton_record(resolution, product, mode)
        assert record["source_qualified_product_topology"] is False
        assert record["classification"] == "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING"
        assert record["complete_C117_action"] is False
        assert record["complete_C396_action"] is False


def test_full_c117_action_fails_closed():
    with pytest.raises(RuntimeError, match="not a complete C117"):
        c404.apply_complete_c117_i2("K9", np.zeros(1))


def test_binding_overlay_advances_primitives_not_complete_apply_count():
    inventory = c404.c396_binding_inventory_with_c404_primitives()
    summary = c404.binding_update_summary()
    assert inventory["total_rows"] == 57
    assert inventory["C404_C117_I2_primitive_binding_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert inventory["C396_19_coordinate_forward_map_ready"] is False
    assert summary["current_complete_numerical_apply_paths"] == 6
    assert summary["complete_apply_count_changed"] is False
    assert summary["skeleton_is_operator_binding"] is False
    assert summary["full_C117_I2_action_ready"] is False
    assert summary["rank_status"] == "RANK_NOT_EVALUATED"
    rows = [row for row in inventory["rows"] if row["coordinate_id"] == "c_C117_1"]
    assert len(rows) == 3
    for row in rows:
        assert row["longitudinal_Q0_status"].endswith("PRIMITIVE_READY")
        assert row["triplet_color_status"].endswith("PRODUCTS_READY")
        assert row["source_qualified_product_topology_bound"] is False
        assert row["numerical_apply_path"] is None
        assert row["selected"] is False and row["zeroed"] is False


def test_validation_surfaces_are_truthful_and_finite():
    longitudinal = c404.longitudinal_inventory()
    skeleton = c404.skeleton_validation()
    assert all(row["symmetry_residual"] == 0 for row in longitudinal["rows"])
    assert all(row["diagonal_residual"] == 0 for row in longitudinal["rows"])
    assert skeleton["pass"] is True
    assert skeleton["source_qualified_product_topology"] is False
    assert skeleton["classification"] == "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING"
    assert skeleton["maximum_sparse_matrix_free_residual"] < 2e-11
    assert skeleton["maximum_hermiticity_residual"] < 2e-11
    assert np.isfinite(skeleton["maximum_sparse_matrix_free_residual"])


def test_source_surface_does_not_import_proxies_or_select_parameters():
    modules = (c404.longitudinal, c404.color_spin, c404.factorized, c404.bindings)
    source = "\n".join(inspect.getsource(module) for module in modules)
    forbidden = (
        "c144",
        "minimum_norm",
        '"physical_fit_authorized": True',
        "parameter_value",
        "c_C117_1 =",
        "resolution_average",
    )
    for token in forbidden:
        assert token not in source
    assert "apply_complete_c117_i2" in source
    assert "raise RuntimeError" in source
