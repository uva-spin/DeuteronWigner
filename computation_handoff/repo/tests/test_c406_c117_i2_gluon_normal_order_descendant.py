from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge import c406_c117_i2_gluon_normal_order_descendant as c406
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    adjoint_generators,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    partition_axis,
    qg_factorized_axis_record,
)
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.derivative_order import (
    BRA,
    KET,
    ordered_partition_kernel_exact,
)


def _boson_annihilation(cutoff: int) -> np.ndarray:
    matrix = np.zeros((cutoff + 1, cutoff + 1), dtype=np.complex128)
    for n in range(1, cutoff + 1):
        matrix[n - 1, n] = np.sqrt(n)
    return matrix


def _mode_operator(mode: int, operator: np.ndarray, modes: int, cutoff: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    identity = np.eye(cutoff + 1, dtype=np.complex128)
    for index in range(modes):
        result = np.kron(result, operator if index == mode else identity)
    return result


def _one_particle_indices(modes: int, cutoff: int) -> list[int]:
    indices = []
    for mode in range(modes):
        occupation = [0] * modes
        occupation[mode] = 1
        value = 0
        for number in occupation:
            value = value * (cutoff + 1) + number
        indices.append(value)
    return indices


def test_source_authority_and_mode_conventions_are_bound():
    record = c406.source_authority_record()
    assert record["source_expression"] == "- f_abc A_perp^b partial_- A_perp^c"
    assert record["derivative_placement"] == "partial_- acts on second slot"
    assert record["number_preserving_branch"]["pattern"] == "a†a"
    assert record["C45_longitudinal_mode"].endswith("/sqrt(2L)")
    assert record["C151_commutator"] == "[a,a^dagger]=delta"
    assert not record["complete_C117_action"]


def test_normal_order_terms_add_to_symmetric_momentum_sum_and_commutator_zero():
    record = c406.normal_ordered_mode_terms(Fraction(3, 1), Fraction(2, 1))
    assert record["creation_first_derivative_annihilation"]["coefficient_multiplying_Fa_bc"]["exact"] == "-2"
    assert record["annihilation_first_derivative_creation_after_boson_reorder"]["coefficient_multiplying_Fa_bc"]["exact"] == "-3"
    assert record["total_dimensionless_coefficient_multiplying_Fa_bc"]["exact"] == "-5"
    assert record["bosonic_commutator"]["coefficient"] == 0
    assert record["source_phase_and_sign_bound"]


def test_invalid_zero_or_negative_modes_fail_closed():
    with pytest.raises(ValueError, match="positive nonzero"):
        c406.dimensionless_descendant_factor_exact(0, 1)
    with pytest.raises(ValueError, match="positive nonzero"):
        c406.c151_canonical_one_gluon_factor(1, -1)


def test_c151_canonical_factor_is_symmetric_and_box_independent():
    value = c406.c151_canonical_one_gluon_factor(Fraction(3), Fraction(2))
    reverse = c406.c151_canonical_one_gluon_factor(Fraction(2), Fraction(3))
    assert value == pytest.approx(reverse, abs=0.0)
    assert value == pytest.approx(-5.0 / (2.0 * np.sqrt(6.0)))


def test_color_matrix_uses_source_minus_and_is_hermitian():
    F = adjoint_generators()[0]
    matrix = c406.adjoint_color_current_matrix(0, 3, 2)
    assert np.allclose(matrix, -5.0 * F)
    assert np.linalg.norm(matrix - matrix.conj().T) < 1e-13
    with pytest.raises(ValueError, match="generator_index"):
        c406.adjoint_color_current_matrix(8, 3, 2)


def test_direct_bosonic_mode_expansion_matches_c406_descendant():
    # Two colors (b=1,c=2) and two longitudinal modes.  SU(3) f^{0,1,2}=1.
    # The finite Fock cutoff is sufficient because the comparison is restricted
    # to the one-particle subspace.
    cutoff = 2
    colors = (1, 2)
    momenta = (2.0, 3.0)
    mode_labels = [(color, momentum) for momentum in momenta for color in colors]
    modes = len(mode_labels)
    annihilator = _boson_annihilation(cutoff)
    a = [_mode_operator(i, annihilator, modes, cutoff) for i in range(modes)]
    adag = [value.conj().T for value in a]

    structure = 1.0  # f^{0,1,2}
    current = np.zeros_like(a[0])
    # Build -f^{0bc} A_b dA_c at x=0.  Include both nonzero ordered color pairs.
    for b, cidx, fabc in ((1, 2, structure), (2, 1, -structure)):
        A_b = sum(
            a[i] + adag[i]
            for i, (color, _momentum) in enumerate(mode_labels)
            if color == b
        )
        dA_c = sum(
            -1j * momentum * a[i] + 1j * momentum * adag[i]
            for i, (color, momentum) in enumerate(mode_labels)
            if color == cidx
        )
        current += -fabc * (A_b @ dA_c)

    one = _one_particle_indices(modes, cutoff)
    restricted = current[np.ix_(one, one)]
    expected = np.zeros_like(restricted)
    F = adjoint_generators()[0]
    for out_index, (out_color, out_momentum) in enumerate(mode_labels):
        for in_index, (in_color, in_momentum) in enumerate(mode_labels):
            expected[out_index, in_index] = -(
                out_momentum + in_momentum
            ) * F[out_color, in_color]
    assert np.linalg.norm(restricted - expected) < 2e-13


def test_inventory_covers_all_external_mode_pairs():
    inventory = c406.one_gluon_descendant_inventory()
    assert inventory["row_count"] == 77
    assert inventory["row_count"] == inventory["expected_row_count"]
    assert all(row["vacuum_commutator_zero"] for row in inventory["rows"])


def test_normal_ordering_validation_passes_all_generators_and_resolutions():
    record = c406.normal_ordering_validation()
    assert record["pass"]
    assert record["maximum_adjoint_generator_hermiticity_residual"] < 2e-12
    assert record["maximum_mode_color_hermiticity_residual"] < 2e-12
    assert record["maximum_vacuum_commutator_color_trace"] < 2e-12
    assert not record["pair_creation_annihilation_branches_promoted"]


@pytest.mark.parametrize("resolution", ("K9", "K11", "K13"))
@pytest.mark.parametrize("product", c406.MIXED_PRODUCTS)
def test_mixed_kernel_exactly_collapses_c405_bra_ket_candidates(resolution, product):
    exact = c406.mixed_partition_kernel_exact(resolution, product)
    bra = ordered_partition_kernel_exact(resolution, product, (BRA,))
    ket = ordered_partition_kernel_exact(resolution, product, (KET,))
    for i, row in enumerate(exact):
        for j, value in enumerate(row):
            assert value == -(bra[i][j] + ket[i][j])
    record = c406.mixed_c405_collapse_record(resolution, product)
    assert record["maximum_exact_residual"] == 0
    assert record["zero_mode_diagonal_exact"]


def test_mixed_partition_sparse_and_independent_apply_agree():
    rng = np.random.default_rng(4061)
    for resolution in ("K9", "K11", "K13"):
        count = len(partition_axis(resolution))
        vector = rng.normal(size=count) + 1j * rng.normal(size=count)
        for product in c406.MIXED_PRODUCTS:
            matrix = c406.mixed_partition_kernel_csr(resolution, product)
            direct = c406.apply_mixed_partition_kernel(resolution, product, vector)
            assert np.linalg.norm(matrix @ vector - direct) < 1e-13


def test_mixed_q_sector_is_exact_zero_not_zero_fill():
    for product in c406.MIXED_PRODUCTS:
        record = c406.mixed_q_sector_zero_certificate(product)
        assert record["status_value"] == "EXACT_ZERO_WITH_NORMAL_ORDERING_COLOR_TRACE_PROOF"
        assert not record["zero_filled_by_convenience"]


def test_same_species_products_require_intermediate_contraction_axis():
    for product in c406.SAME_SPECIES_PRODUCTS:
        record = c406.same_species_intermediate_requirement(product)
        assert record["numerical_apply_path"] is None
        assert "intermediate" in record["required_object"]
        with pytest.raises(RuntimeError, match="intermediate contraction axis"):
            c406.mixed_partition_kernel_exact("K9", product)


def test_product_routing_audit_has_six_mixed_and_six_same_species_rows():
    audit = c406.product_routing_audit()
    assert audit["row_count"] == 12
    assert audit["mixed_product_rows"] == 6
    assert audit["same_species_rows"] == 6
    assert audit["mixed_derivative_ambiguity_closed"]
    assert not audit["same_species_contraction_axes_closed"]


def test_mixed_qg_sparse_matrix_free_and_adjoint_validation_passes():
    record = c406.mixed_kernel_validation()
    assert record["row_count"] == 6
    assert record["pass"]
    assert record["maximum_sparse_matrix_free_residual"] < 3e-11
    assert record["maximum_adjoint_residual"] < 3e-11
    assert record["maximum_q_sector_zero_residual"] == 0.0


def test_mixed_direct_sum_has_exact_zero_q_block():
    mode = (0, 0)
    for resolution in ("K9", "K11", "K13"):
        axis = qg_factorized_axis_record(resolution)
        qdim = 6
        for product in c406.MIXED_PRODUCTS:
            matrix = c406.mixed_direct_sum_csr(resolution, product, mode)
            assert matrix.shape[0] == qdim + int(axis["dimension"])
            assert matrix[:qdim, :qdim].nnz == 0
            assert matrix[:qdim, qdim:].nnz == 0
            assert matrix[qdim:, :qdim].nnz == 0


def test_binding_overlay_advances_descendant_boundary_not_complete_count():
    inventory = c406.c396_binding_inventory_with_c406_descendant()
    assert inventory["C406_C117_I2_descendant_rows"] == 3
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["complete_C117_numerical_apply_paths"] == 0
    rows = [row for row in inventory["rows"] if row["coordinate_id"] == "c_C117_1"]
    assert len(rows) == 3
    assert all(row["one_gluon_descendant_status"].endswith("READY") for row in rows)
    assert all(row["numerical_apply_path"] is None for row in rows)


def test_completion_record_is_truthful_and_complete_action_fails_closed():
    completion = c406.completion_record()
    assert completion["one_gluon_normal_order_descendant_ready"]
    assert completion["mixed_product_derivative_routing_ready"]
    assert completion["mixed_qg_numerical_primitives_ready"]
    assert not completion["same_species_contraction_axes_ready"]
    assert completion["complete_C117_numerical_apply_paths"] == 0
    assert completion["complete_C396_numerical_apply_paths"] == 6
    assert completion["rank_status"] == "RANK_NOT_EVALUATED"
    assert not completion["physical_fit_authorized"]
    with pytest.raises(RuntimeError, match="cannot apply a complete C117 I2 action"):
        c406.apply_complete_c117_i2("K9", np.zeros(1))


def test_source_has_no_forbidden_shortcuts():
    root = Path(c406.__file__).resolve().parent
    text = "\n".join(path.read_text(encoding="utf-8") for path in root.glob("*.py"))
    forbidden = (
        "minimum_norm",
        "physical_rank =",
        "c_C117_1 = 0",
        "complete_C117_action\": True",
        "source_qualified_complete_product_matrix\": True",
    )
    assert all(token not in text for token in forbidden)


def test_c406_generator_is_deterministic_and_self_excluding(tmp_path: Path):
    import json
    import os
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[1]
    outputs = (tmp_path / "first", tmp_path / "second")
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(root / "src")
    environment.setdefault("OMP_NUM_THREADS", "1")
    environment.setdefault("OPENBLAS_NUM_THREADS", "1")
    environment.setdefault("MKL_NUM_THREADS", "1")
    for output in outputs:
        result = subprocess.run(
            [
                sys.executable,
                str(root / "tools/generate_c406_c117_i2_gluon_normal_order_descendant.py"),
                "--output-dir",
                str(output),
            ],
            cwd=root,
            env=environment,
            text=True,
            capture_output=True,
            timeout=180,
            check=False,
        )
        assert result.returncode == 0, result.stderr
    names_first = sorted(path.name for path in outputs[0].iterdir() if path.is_file())
    names_second = sorted(path.name for path in outputs[1].iterdir() if path.is_file())
    assert names_first == names_second
    assert names_first
    for name in names_first:
        assert (outputs[0] / name).read_bytes() == (outputs[1] / name).read_bytes()
    generated = json.loads((outputs[0] / "generation_result.json").read_text())
    artifact_names = {row["path"] for row in generated["artifacts"]}
    assert "generation_result.json" not in artifact_names
    assert generated["one_gluon_descendant_rows"] == 77
    assert generated["mixed_product_rows"] == 6
    assert generated["same_species_rows"] == 6
    assert generated["complete_C117_numerical_apply_paths"] == 0
    assert generated["complete_C396_numerical_apply_paths"] == 6
