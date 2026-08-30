from __future__ import annotations

from fractions import Fraction
import inspect
from math import pi
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive import (
    HOMode,
    admitted_transverse_modes,
    apply_single_member_kernel,
    apply_weighted_spatial_kernel,
    axis_summary,
    binding_update_summary,
    c396_binding_inventory_with_c403_i2_primitive,
    candidate_transverse_modes,
    external_modes,
    i2_spatial_element,
    i2_spatial_element_quadrature,
    member_by_rank,
    member_count,
    member_page,
    member_rank,
    radial_moment_fraction,
    rejected_transverse_modes,
    single_member_kernel_csr,
    single_member_kernel_dense,
    spatial_kernel_inventory,
    spatial_kernel_validation,
    support_theorem_certificate,
    support_theorem_rows,
    weighted_spatial_kernel_csr,
    witness_record,
)
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive import axis as axis_module
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive import spatial as spatial_module


EXPECTED = {
    "K9": {
        "candidate_modes": 36,
        "admitted_modes": 28,
        "rejected_modes": 8,
        "QUARK": (864, 672, 192),
        "GLUON": (2304, 1792, 512),
    },
    "K11": {
        "candidate_modes": 55,
        "admitted_modes": 45,
        "rejected_modes": 10,
        "QUARK": (1650, 1350, 300),
        "GLUON": (4400, 3600, 800),
    },
    "K13": {
        "candidate_modes": 78,
        "admitted_modes": 66,
        "rejected_modes": 12,
        "QUARK": (2808, 2376, 432),
        "GLUON": (7488, 6336, 1152),
    },
}


def test_axis_counts_and_exact_highest_shell_rejection():
    summary = axis_summary()
    assert summary["finite_axis_paths"] == 6
    assert summary["C64_runtime_required"] is False
    for row in summary["rows"]:
        expected = EXPECTED[row["resolution"]]
        assert row["transverse_candidate_count"] == expected["candidate_modes"]
        assert row["transverse_admitted_count"] == expected["admitted_modes"]
        assert row["transverse_rejected_count"] == expected["rejected_modes"]
        assert (
            row["candidate_member_count"],
            row["admitted_member_count"],
            row["rejected_member_count"],
        ) == expected[row["species"]]
        nmax = row["Nmax"]
        assert all(2 * n + abs(m) <= nmax - 2 for n, m in admitted_transverse_modes(row["resolution"]))
        assert all(2 * n + abs(m) == nmax - 1 for n, m in rejected_transverse_modes(row["resolution"]))


def test_member_rank_page_and_exact_longitudinal_records():
    for resolution in EXPECTED:
        for species in ("QUARK", "GLUON"):
            total = member_count(resolution, species)
            for rank in (0, total // 2, total - 1):
                member = member_by_rank(resolution, species, rank)
                assert member_rank(member) == rank
                assert member.k > 0 and 0 < member.x < 1
                assert member.selection_status in {"ADMITTED_MEMBER", "REJECTED_NOT_APPLICABLE"}
                record = member.to_record()
                assert record["numerical_factor_values_bound"] is False
                assert record["derivative_weight"] == "1"
            page = member_page(resolution, species, start=total - 3, limit=8)
            assert len(page["records"]) == 3
            assert page["terminal"] is True
            assert page["next_rank"] is None


def test_support_theorem_exhaustive_against_exact_c62_algebra():
    certificate = support_theorem_certificate()
    rows = support_theorem_rows()
    assert certificate["row_count"] == len(rows) == 1774
    assert certificate["admitted_witness_rows"] == 1466
    assert certificate["rejected_shell_rows"] == 308
    assert certificate["all_exact_matches"] is True
    assert certificate["maximum_numeric_residual"] == 0.0
    assert all(row["exact_match"] is True for row in rows)
    assert all(
        row["C62_status"] == "NONZERO_EXACT_ALGEBRAIC"
        for row in rows
        if row["selection_status"] == "ADMITTED_MEMBER"
    )


def test_selected_witness_closed_forms_and_signs():
    quark = witness_record("K9", "QUARK", 0, 0, 1)
    gluon = witness_record("K9", "GLUON", 0, 0, 1)
    assert quark["exact_match"] and gluon["exact_match"]
    # At the first C47 K9 partition xq=7/9 and xg=2/9.  Shell-one quark and
    # gluon witnesses have opposite signs under the exact C62 convention.
    assert abs(quark["C62_value"][0] - (2.0 / 9.0) ** 0.5) < 1e-15
    assert abs(gluon["C62_value"][0] + (7.0 / 9.0) ** 0.5) < 1e-15
    assert quark["absolute_numeric_residual"] == 0.0
    assert gluon["absolute_numeric_residual"] == 0.0
    even_gluon = witness_record("K9", "GLUON", 0, 1, 0)
    assert abs(even_gluon["C62_value"][0] - 7.0 / 9.0) < 1e-15
    assert even_gluon["exact_match"] is True


def test_spatial_ground_identity_angular_rule_and_exact_cancellation():
    with pytest.raises((TypeError, ValueError)):
        HOMode(0.5, 0)
    with pytest.raises((TypeError, ValueError)):
        i2_spatial_element("K9", (0.5, 0), (0, 0), (0, 0))
    ground = HOMode(0, 0)
    value = i2_spatial_element("K9", ground, ground, ground)
    assert abs(value.real - 0.4**2 / (2.0 * pi)) < 1e-15
    assert value.imag == 0.0
    assert i2_spatial_element("K9", (0, 1), (0, -1), ground) == 0j
    # This high-order radial moment cancels exactly; floating polynomial sums need not.
    assert radial_moment_fraction(3, 0, 2, 2, 1) == Fraction(0)


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_analytic_and_independent_quadrature_routes(resolution):
    labels = external_modes(resolution)
    internals = (labels[0], labels[len(labels) // 2], labels[-1])
    maximum = 0.0
    for internal in internals:
        for out in labels:
            for inn in labels:
                maximum = max(
                    maximum,
                    abs(
                        i2_spatial_element(resolution, out, inn, internal)
                        - i2_spatial_element_quadrature(resolution, out, inn, internal)
                    ),
                )
    assert maximum < 5e-13


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
def test_sparse_matrix_free_hermiticity_and_psd_for_all_internal_modes(resolution):
    rng = np.random.default_rng({"K9": 9, "K11": 11, "K13": 13}[resolution])
    labels = external_modes(resolution)
    vector = rng.normal(size=len(labels)) + 1j * rng.normal(size=len(labels))
    for internal in labels:
        dense = single_member_kernel_dense(resolution, internal)
        sparse = single_member_kernel_csr(resolution, internal)
        matrix_free = apply_single_member_kernel(resolution, internal, vector)
        assert np.linalg.norm(sparse @ vector - matrix_free) < 5e-13
        assert np.linalg.norm(dense - dense.conj().T) == 0.0
        assert np.linalg.eigvalsh(dense)[0] >= -1e-12


def test_weighted_aggregate_requires_explicit_values_and_matches_independent_action():
    with pytest.raises(ValueError):
        weighted_spatial_kernel_csr("K9", None)
    with pytest.raises(ValueError):
        weighted_spatial_kernel_csr("K9", {})
    with pytest.raises(ValueError):
        weighted_spatial_kernel_csr("K9", {HOMode(0, 0): 1.0, (0, 0): 2.0})
    weights = {HOMode(0, 0): 1.25, HOMode(0, 1): -0.5}
    vector = np.arange(len(external_modes("K9")), dtype=float) + 1j
    sparse = weighted_spatial_kernel_csr("K9", weights)
    direct = apply_weighted_spatial_kernel("K9", weights, vector)
    assert np.linalg.norm(sparse @ vector - direct) < 5e-13


def test_spatial_validation_and_inventory_are_source_narrow():
    validation = spatial_kernel_validation()
    inventory = spatial_kernel_inventory()
    assert validation["pass"] is True
    assert validation["maximum_quadrature_abs_residual"] < 5e-13
    assert inventory["row_count"] == 28 + 45 + 66
    assert inventory["spatial_kernel_paths"] == 3
    assert "C47 intrinsic/relative qg" in inventory["external_basis_scope"]
    assert inventory["q_sector_external_basis_assembled"] is False
    assert validation["q_sector_external_basis_assembled"] is False
    assert inventory["full_C117_operator_paths"] == 0
    assert inventory["C80_reuse"] is False
    assert inventory["single_member_kernel_positive_semidefinite"] is True
    assert inventory["weighted_aggregate_PSD_only_for_nonnegative_weights"] is True
    assert validation["quadrature_internal_modes_checked"] == 9
    assert all(row["positive_semidefinite_at_tolerance"] for row in inventory["rows"])


def test_c396_overlay_advances_primitive_not_complete_apply_count():
    inventory = c396_binding_inventory_with_c403_i2_primitive()
    summary = binding_update_summary()
    assert inventory["total_rows"] == 57
    assert inventory["C403_I2_primitive_binding_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert inventory["C396_19_coordinate_forward_map_ready"] is False
    assert summary["complete_apply_count_changed"] is False
    assert summary["full_C117_I2_action_ready"] is False
    assert summary["rank_status"] == "RANK_NOT_EVALUATED"
    for row in inventory["rows"]:
        if row["coordinate_id"] == "c_C117_1":
            assert row["spatial_kernel_status"].endswith("PRIMITIVE_READY")
            assert row["numerical_apply_path"] is None
            assert row["selected"] is False and row["zeroed"] is False


def test_source_surface_does_not_import_forbidden_proxy_or_runtime_paths():
    axis_source = inspect.getsource(axis_module)
    spatial_source = inspect.getsource(spatial_module)
    forbidden = (
        "qgtm2",
        "icmembers",
        "ifkernel2",
        "c144",
        "minimum_norm",
        "physical_coupling",
    )
    for token in forbidden:
        assert token not in axis_source
        assert token not in spatial_source
    assert "data/runtime/c64_qgtm2" not in axis_source
    assert "C80_imported_or_reused\": False" in spatial_source


def test_repository_does_not_need_c64_runtime_for_c403_import_or_support():
    c64 = Path(__file__).resolve().parents[1] / "data/runtime/c64_qgtm2/index.json"
    # The assertion is about dependency: it passes whether the optional artifact is present or absent.
    _ = c64.exists()
    assert axis_summary()["C64_runtime_required"] is False
    assert support_theorem_certificate()["all_exact_matches"] is True
