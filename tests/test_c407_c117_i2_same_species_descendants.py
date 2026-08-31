from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Union, get_args, get_origin

import numpy as np
import pytest

from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import HOMode
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants import (
    STATUS,
    aggregate_weight_exact,
    apply_complete_c117_i2,
    apply_jgjg_qg_primitive,
    apply_jqjq_q_sector_primitive,
    apply_jqjq_qg_conditioned,
    apply_longitudinal_diagonal,
    binding_update_summary,
    c396_binding_inventory_with_c407_descendants,
    canonical_spatial_weights,
    completion_record,
    descendant_inventory,
    diagnostic_spatial_weight_fixture,
    direct_fock_contraction_validation,
    external_mode_axis,
    gluon_current_pair_factor_exact,
    intermediate_axis,
    intermediate_axis_inventory,
    jqjq_qg_conditioned_csr,
    jqjq_qg_conditioned_validation,
    longitudinal_diagonal_csr,
    longitudinal_diagonal_exact,
    longitudinal_validation,
    same_species_weight_exact,
    scientific_boundary_record,
    source_hash_audit,
    species_mode_axis,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.descendants import (
    _population_count,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.jqjq_qg import (
    SpatialWeightKey,
)


def test_python39_compatible_runtime_type_alias() -> None:
    """The module-level alias must remain evaluable on Python 3.9."""
    assert get_origin(SpatialWeightKey) is Union
    arguments = get_args(SpatialWeightKey)
    assert HOMode in arguments
    assert len(arguments) == 2


def test_python39_population_count_compatibility() -> None:
    """The fermion sign route must not depend on ``int.bit_count``."""
    assert [_population_count(value) for value in (0, 1, 2, 3, 7, 8, 15)] == [
        0, 1, 1, 2, 3, 1, 4
    ]
    source = Path(__file__).resolve().parents[1] / (
        "src/deuteron_wigner/bridge/c407_c117_i2_same_species_descendants/descendants.py"
    )
    assert ".bit_count(" not in source.read_text(encoding="utf-8")


def test_source_authority_and_boundary_are_fail_closed() -> None:
    audit = source_hash_audit()
    boundary = scientific_boundary_record()
    assert audit["all_pass"] and audit["row_count"] == 12
    assert boundary["complete_C117_action"] is False
    assert boundary["complete_C396_numerical_apply_paths"] == 6
    assert boundary["rank_status"] == "RANK_NOT_EVALUATED"
    assert boundary["activation_gate_status"] == "NOT_READY"
    assert "source-authorized C117 I2 graph-member weights for J_qJ_q" in boundary["open"]


@pytest.mark.parametrize(
    ("resolution", "quark_count", "gluon_count"),
    (("K9", 5, 4), ("K11", 6, 5), ("K13", 7, 6)),
)
def test_c45_species_axes(resolution: str, quark_count: int, gluon_count: int) -> None:
    quarks = species_mode_axis(resolution, "QUARK")
    gluons = species_mode_axis(resolution, "GLUON")
    assert len(quarks) == quark_count
    assert len(gluons) == gluon_count
    assert all(value.denominator == 2 for value in quarks)
    assert all(value.denominator == 1 for value in gluons)
    assert all(value > 0 for value in quarks + gluons)


def test_intermediate_axis_inventory_closes_exact_finite_Q0_domain() -> None:
    inventory = intermediate_axis_inventory()
    assert inventory["row_count"] == 154
    assert inventory["zero_transfer_rows"] == 0
    assert inventory["noninteger_transfer_rows"] == 0
    assert inventory["duplicates"] == 0
    assert all(row["Q0_admitted"] for row in inventory["rows"])


def test_q_sector_and_qg_external_axes() -> None:
    assert external_mode_axis("K9", "QUARK", "q->q") == (("K9:q", Fraction(9, 2)),)
    assert len(external_mode_axis("K9", "QUARK", "qg->qg")) == 4
    assert len(external_mode_axis("K9", "GLUON", "qg->qg")) == 4
    assert external_mode_axis("K9", "GLUON", "q->q") == tuple()


def test_intermediate_axis_rejects_zero_and_invalid_external_mode() -> None:
    axis = intermediate_axis("K9", "QUARK", "qg->qg", Fraction(7, 2), "P0")
    assert len(axis) == 4
    assert all(row.intermediate_k != Fraction(7, 2) for row in axis)
    assert all(row.transfer_q.denominator == 1 for row in axis)
    with pytest.raises(ValueError, match="outside"):
        intermediate_axis("K9", "QUARK", "qg->qg", Fraction(1, 1), "bad")


def test_exact_quark_and_gluon_weights() -> None:
    assert same_species_weight_exact("QUARK", Fraction(7, 2), Fraction(5, 2)) == Fraction(4, 3)
    assert gluon_current_pair_factor_exact(Fraction(1), Fraction(2)) == Fraction(9, 8)
    assert same_species_weight_exact("GLUON", Fraction(1), Fraction(2)) == Fraction(27, 8)


def test_same_species_weights_are_exchange_symmetric_and_positive() -> None:
    for species, left, right in (
        ("QUARK", Fraction(1, 2), Fraction(5, 2)),
        ("GLUON", Fraction(1), Fraction(4)),
    ):
        forward = same_species_weight_exact(species, left, right)
        reverse = same_species_weight_exact(species, right, left)
        assert forward == reverse
        assert forward > 0
    with pytest.raises(ValueError, match="Q0"):
        same_species_weight_exact("QUARK", Fraction(1, 2), Fraction(1, 2))


def test_aggregate_weights_are_exact_finite_sums() -> None:
    value = aggregate_weight_exact("K9", "QUARK", "q->q", "K9:q", Fraction(9, 2))
    expected = Fraction(4, 3) * sum(Fraction(1, q * q) for q in (1, 2, 3, 4))
    assert value == expected


@pytest.mark.parametrize(
    ("resolution", "species", "sector"),
    (
        ("K9", "QUARK", "q->q"),
        ("K11", "QUARK", "qg->qg"),
        ("K13", "GLUON", "qg->qg"),
    ),
)
def test_longitudinal_sparse_and_matrix_free_agree(
    resolution: str, species: str, sector: str
) -> None:
    exact = longitudinal_diagonal_exact(resolution, species, sector)
    vector = np.arange(1, len(exact) + 1, dtype=np.complex128) * (1 + 0.25j)
    assert np.allclose(
        longitudinal_diagonal_csr(resolution, species, sector) @ vector,
        apply_longitudinal_diagonal(resolution, species, sector, vector),
        atol=1e-14,
    )
    assert all(value > 0 for value in exact)


def test_longitudinal_and_direct_fock_validations_pass_with_correct_boundaries() -> None:
    fock = direct_fock_contraction_validation()
    assert fock["pass"]
    assert all("/" in row["source_mode"] for row in fock["rows"] if row["species"] == "QUARK")
    assert all("/" not in row["source_mode"] for row in fock["rows"] if row["species"] == "GLUON")
    validation = longitudinal_validation()
    assert validation["pass"]
    assert validation["maximum_sparse_matrix_free_residual"] < 1e-14
    assert validation["minimum_weight"] > 0


def test_descendant_inventory_has_source_derived_counts_and_nonclaims() -> None:
    inventory = descendant_inventory()
    assert inventory["row_count"] == 154
    assert inventory["fundamental_Casimir_residual"] < 2e-12
    assert inventory["adjoint_Casimir_residual"] < 2e-12
    assert inventory["source_overall_minus_g2_over_2_factored"] is True
    assert inventory["complete_product_normalization"] is False
    assert inventory["complete_C117_action"] is False


def test_graph_member_weights_have_no_default_and_must_be_complete() -> None:
    with pytest.raises(ValueError, match="no unit-weight or minimum-norm default"):
        canonical_spatial_weights("K9", None)
    fixture = dict(diagnostic_spatial_weight_fixture("K9"))
    fixture.pop(next(iter(fixture)))
    with pytest.raises(ValueError, match="complete explicit"):
        canonical_spatial_weights("K9", fixture)


def test_graph_member_weight_validation_rejects_duplicates_nonfinite_and_outside_axis() -> None:
    fixture = dict(diagnostic_spatial_weight_fixture("K9"))
    first = next(iter(fixture))
    duplicate = dict(fixture)
    duplicate[(first.n, first.m)] = 2.0
    with pytest.raises(ValueError, match="duplicate canonical"):
        canonical_spatial_weights("K9", duplicate)
    nonfinite = dict(fixture)
    nonfinite[first] = np.nan
    with pytest.raises(ValueError, match="finite real"):
        canonical_spatial_weights("K9", nonfinite)
    outside = dict(fixture)
    outside.pop(first)
    outside[HOMode(100, 0)] = 1.0
    with pytest.raises(ValueError, match="outside"):
        canonical_spatial_weights("K9", outside)


def test_diagnostic_spatial_weight_fixture_is_explicit_nonuniform_and_nonphysical() -> None:
    for resolution, count in (("K9", 28), ("K11", 45), ("K13", 66)):
        fixture = diagnostic_spatial_weight_fixture(resolution)
        rows = canonical_spatial_weights(resolution, fixture)
        assert len(rows) == count
        assert len(set(fixture.values())) == count
        assert set(fixture.values()) != {1.0}


@pytest.mark.parametrize(("resolution", "dimension"), (("K9", 1344), ("K11", 2700), ("K13", 4752)))
def test_jqjq_qg_conditioned_composition_dimensions_and_action(
    resolution: str, dimension: int
) -> None:
    fixture = diagnostic_spatial_weight_fixture(resolution)
    matrix = jqjq_qg_conditioned_csr(resolution, fixture)
    assert matrix.shape == (dimension, dimension)
    vector = np.linspace(0.0, 1.0, dimension) + 1j * np.linspace(1.0, 0.0, dimension)
    assert np.allclose(
        matrix @ vector,
        apply_jqjq_qg_conditioned(resolution, fixture, vector),
        atol=2e-10,
    )
    assert np.linalg.norm((matrix - matrix.getH()).data) < 1e-12


def test_jqjq_qg_conditioned_validation_is_not_an_operator_binding() -> None:
    validation = jqjq_qg_conditioned_validation()
    assert validation["pass"]
    assert validation["row_count"] == 3
    assert validation["classification"].endswith("NOT_OPERATOR_BINDING")
    assert validation["source_authorized_graph_member_weights"] is False
    assert validation["unit_weight_default"] is False
    assert validation["minimum_norm_default"] is False
    assert validation["complete_C117_action"] is False


def test_unavailable_same_species_surfaces_fail_closed() -> None:
    with pytest.raises(RuntimeError, match="I4-local"):
        apply_jqjq_q_sector_primitive()
    with pytest.raises(RuntimeError, match="derivative-density"):
        apply_jgjg_qg_primitive()
    with pytest.raises(RuntimeError, match="complete C117"):
        apply_complete_c117_i2()


def test_binding_overlay_preserves_six_complete_C396_paths() -> None:
    inventory = c396_binding_inventory_with_c407_descendants()
    summary = binding_update_summary()
    assert inventory["total_rows"] == 57
    assert inventory["C407_C117_I2_descendant_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    assert summary["current_complete_numerical_apply_paths"] == 6
    assert summary["J_qJ_q_qg_conditioned_composition_rows"] == 3
    assert summary["source_authorized_graph_member_weight_sets"] == 0
    assert summary["J_gJ_g_longitudinal_primitive_paths"] == 3
    assert summary["full_C117_I2_action_ready"] is False


def test_completion_record_is_truthful() -> None:
    record = completion_record()
    assert record["status"] == STATUS
    assert record["same_species_intermediate_axes_ready"] is True
    assert record["same_species_longitudinal_descendants_ready"] is True
    assert record["J_qJ_q_qg_caller_conditioned_composition_ready"] is True
    assert record["J_qJ_q_qg_source_authorized_graph_weights_ready"] is False
    assert record["J_qJ_q_q_sector_ready"] is False
    assert record["J_gJ_g_qg_full_transverse_descendant_ready"] is False
    assert record["complete_C117_numerical_apply_paths"] == 0
    assert record["complete_C396_numerical_apply_paths"] == 6
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["activation_gate_status"] == "NOT_READY"


def test_C407_source_has_no_forbidden_shortcuts_or_hidden_unit_weight_default() -> None:
    root = Path(__file__).resolve().parents[1] / "src/deuteron_wigner/bridge/c407_c117_i2_same_species_descendants"
    text = "\n".join(path.read_text(encoding="utf-8") for path in root.glob("*.py"))
    assert "mixed_partition_kernel" not in text
    assert "c144" not in text.lower()
    assert '"minimum_norm_default": True' not in text
    assert "minimum_norm_selection" not in text.lower()
    assert "{mode: 1.0 for mode" not in text
    assert "source_authorized_graph_member_weights" in text
    assert "physical_fit" in text
