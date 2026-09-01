from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    external_modes,
    i2_spatial_element,
)
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import (
    direct_sum_axis_record,
)
from deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant.mixed_kernel import (
    apply_mixed_qg_kernel,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.jqjq_qg import (
    diagnostic_spatial_weight_fixture,
    jqjq_qg_conditioned_csr,
)
from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure import (
    apply_complete_c117_i2,
    apply_q_sector_jqjq,
    apply_source_routed_jqjq_direct_sum,
    apply_source_weighted_jqjq_qg,
    apply_source_weighted_mixed_direct_sum,
    apply_source_weighted_mixed_qg,
    binding_update_summary,
    c396_binding_inventory_with_c408_closure,
    completion_record,
    derivative_density_conflict_record,
    i2_member_weight_authority,
    i2_source_weight_validation,
    jqjq_product_block_validation,
    q_i4_intermediate_modes,
    q_i4_member_quadrature,
    q_i4_member_value,
    q_sector_i4_inventory,
    q_sector_i4_validation,
    q_sector_jqjq_csr,
    routing_authority_record,
    scientific_boundary_record,
    source_hash_audit,
    source_i2_unit_weight_record,
    source_i2_unit_weights,
    source_routed_jqjq_direct_sum_csr,
    source_weighted_jqjq_qg_csr,
    source_weighted_mixed_direct_sum_csr,
    source_weighted_mixed_qg_csr,
)

RESOLUTIONS = ("K9", "K11", "K13")


def test_source_hash_audit_and_authority_records_close() -> None:
    audit = source_hash_audit()
    assert audit["all_pass"] is True
    assert audit["row_count"] == 12
    routing = routing_authority_record()
    assert routing["C408_route"] == "I4_local"
    assert routing["routing_conflict_closed"] is True
    assert routing["historical_C125_modified"] is False
    weights = i2_member_weight_authority()
    assert weights["C124_descendant_member_multiplier"] == "1"
    assert weights["C126_value_program_member_multiplier"] == "1"
    assert weights["unit_multiplier_is_physical_coefficient"] is False


def test_c125_overbroad_route_is_not_used_for_jqjq_q_sector() -> None:
    record = routing_authority_record()
    statuses = {row["owner"]: row["status"] for row in record["authorities"]}
    assert statuses["C125"] == "CONFLICTING_OVERBROAD_HELPER"
    assert statuses["C116"] == "SOURCE_QUALIFIED"
    assert statuses["C126"] == "SOURCE_QUALIFIED"


@pytest.mark.parametrize("resolution,expected", [("K9", 28), ("K11", 45), ("K13", 66)])
def test_i2_source_member_weights_are_exact_unit_maps(resolution: str, expected: int) -> None:
    weights = source_i2_unit_weights(resolution)
    record = source_i2_unit_weight_record(resolution)
    assert len(weights) == expected
    assert record["member_count"] == expected
    assert set(weights) == set(external_modes(resolution))
    assert set(weights.values()) == {1.0}
    assert record["physical_coefficient_selected"] is False


def test_source_unit_weights_are_not_the_c407_nonphysical_fixture() -> None:
    source = source_i2_unit_weights("K9")
    fixture = diagnostic_spatial_weight_fixture("K9")
    assert source != fixture
    assert set(source.values()) == {1.0}
    assert len(set(fixture.values())) > 1


@pytest.mark.parametrize("resolution", RESOLUTIONS)
def test_source_weighted_jqjq_qg_matches_explicit_c407_unit_map(resolution: str) -> None:
    expected = jqjq_qg_conditioned_csr(resolution, source_i2_unit_weights(resolution))
    actual = source_weighted_jqjq_qg_csr(resolution)
    assert actual.shape == expected.shape
    assert np.linalg.norm((actual - expected).data) < 1e-14
    rng = np.random.default_rng(100 + len(resolution))
    vector = rng.normal(size=actual.shape[0]) + 1j * rng.normal(size=actual.shape[0])
    assert np.linalg.norm(actual @ vector - apply_source_weighted_jqjq_qg(resolution, vector)) < 5e-10


@pytest.mark.parametrize("product", ["J_qJ_g", "J_gJ_q"])
def test_source_weighted_mixed_k9_matches_explicit_sum_over_c406_members(product: str) -> None:
    resolution = "K9"
    matrix = source_weighted_mixed_qg_csr(resolution, product)
    rng = np.random.default_rng(408)
    vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
    explicit = np.zeros_like(vector)
    for mode in external_modes(resolution):
        explicit += apply_mixed_qg_kernel(resolution, product, mode, vector)
    assert np.linalg.norm(matrix @ vector - explicit) < 5e-10
    assert np.linalg.norm(matrix @ vector - apply_source_weighted_mixed_qg(resolution, product, vector)) < 5e-10


def test_source_weighted_mixed_direct_sum_has_exact_q_sector_zero_and_adjoint() -> None:
    resolution = "K9"
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    left = source_weighted_mixed_direct_sum_csr(resolution, "J_qJ_g")
    right = source_weighted_mixed_direct_sum_csr(resolution, "J_gJ_q")
    assert left[:qdim, :].nnz == 0
    assert left[:, :qdim].nnz == 0
    assert np.linalg.norm((left.getH() - right).data) < 5e-10
    rng = np.random.default_rng(409)
    vector = rng.normal(size=left.shape[0]) + 1j * rng.normal(size=left.shape[0])
    assert np.linalg.norm(left @ vector - apply_source_weighted_mixed_direct_sum(resolution, "J_qJ_g", vector)) < 5e-10


@pytest.mark.parametrize("resolution,expected", [("K9", 36), ("K11", 55), ("K13", 78)])
def test_q_sector_i4_uses_complete_c45_shell(resolution: str, expected: int) -> None:
    modes = q_i4_intermediate_modes(resolution)
    assert len(modes) == expected
    assert max(mode.shell for mode in modes) == {"K9": 7, "K11": 9, "K13": 11}[resolution]


def test_q_sector_i4_agrees_with_c403_route_on_shared_admitted_domain() -> None:
    resolution = "K9"
    ground = HOMode(0, 0)
    for mode in external_modes(resolution):
        assert abs(q_i4_member_value(resolution, mode) - i2_spatial_element(resolution, ground, ground, mode).real) < 1e-15


def test_q_sector_i4_analytic_and_quadrature_routes_agree_for_all_modes() -> None:
    for resolution in RESOLUTIONS:
        for mode in q_i4_intermediate_modes(resolution):
            assert abs(q_i4_member_value(resolution, mode) - q_i4_member_quadrature(resolution, mode)) < 5e-13


@pytest.mark.parametrize("resolution", RESOLUTIONS)
def test_q_sector_jqjq_is_scalar_identity_with_independent_action(resolution: str) -> None:
    matrix = q_sector_jqjq_csr(resolution)
    assert matrix.shape == (6, 6)
    assert matrix.nnz == 6
    diagonal = matrix.diagonal()
    assert np.all(diagonal > 0)
    assert np.max(np.abs(diagonal - diagonal[0])) == 0
    rng = np.random.default_rng(410)
    vector = rng.normal(size=6) + 1j * rng.normal(size=6)
    assert np.linalg.norm(matrix @ vector - apply_q_sector_jqjq(resolution, vector)) < 1e-14


@pytest.mark.parametrize("resolution", RESOLUTIONS)
def test_jqjq_direct_sum_shape_and_action(resolution: str) -> None:
    matrix = source_routed_jqjq_direct_sum_csr(resolution)
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    assert matrix.shape == (dimension, dimension)
    rng = np.random.default_rng(411)
    vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    assert np.linalg.norm(matrix @ vector - apply_source_routed_jqjq_direct_sum(resolution, vector)) < 5e-10
    assert np.linalg.norm((matrix - matrix.getH()).data) < 5e-10


def test_aggregate_validation_records_pass_without_promoting_complete_action() -> None:
    assert q_sector_i4_inventory()["pass"] is True
    assert q_sector_i4_validation()["pass"] is True
    assert i2_source_weight_validation()["pass"] is True
    assert jqjq_product_block_validation()["pass"] is True
    boundary = scientific_boundary_record()
    assert boundary["complete_C117_numerical_apply_paths"] == 0
    assert boundary["complete_C396_numerical_apply_paths"] == 6


def test_derivative_density_stays_fail_closed() -> None:
    record = derivative_density_conflict_record()
    assert record["numerical_derivative_density_action"] is None
    assert record["unavailable_not_zero"] is True
    with pytest.raises(RuntimeError):
        apply_complete_c117_i2(None)


def test_binding_overlay_preserves_six_complete_c396_paths() -> None:
    inventory = c396_binding_inventory_with_c408_closure()
    summary = binding_update_summary()
    assert inventory["total_rows"] == 57
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert inventory["source_routed_product_block_primitive_paths"] == 9
    assert summary["current_complete_numerical_apply_paths"] == 6
    assert summary["source_routed_product_block_primitive_paths"] == 9


def test_completion_record_is_truthful() -> None:
    record = completion_record()
    assert record["J_qJ_q_q_sector_I4_ready"] is True
    assert record["I2_source_descendant_member_weights_ready"] is True
    assert record["J_qJ_q_direct_sum_product_block_ready"] is True
    assert record["mixed_current_source_weighted_product_blocks_ready"] is True
    assert record["J_gJ_g_derivative_density_ready"] is False
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["physical_fit_authorized"] is False
    assert record["activation_gate_status"] == "NOT_READY"


def test_c408_python39_static_compatibility() -> None:
    root = Path(__file__).resolve().parents[1]
    package = root / "src/deuteron_wigner/bridge/c408_c117_i2_weight_routing_closure"
    for path in sorted(package.glob("*.py")):
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, feature_version=9)
        assert ".bit_count(" not in text
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                assert not (isinstance(value, ast.BinOp) and isinstance(value.op, ast.BitOr))
