"""C53 exact SU(3) physical canonical vertex closes without historical tuples."""
import numpy as np
import pytest

from deuteron_wigner.bridge.vdim2.core import M2_COEFFICIENT, resolutions
from deuteron_wigner.bridge.vertex3.core import (
    CF, STATUS, apply_physical_canonical_emission, assemble_physical_vertex,
    color_data, color_validation, generated_adjoint_and_block,
    matrix_free_physical_columns, mutate_live_c53, poisoning_report,
    run_c53_checks, static_dependency_guard, triplet_rotation_holdout,
    validate_c53,
)


def test_c53_end_to_end_source_to_physical_vertex():
    result = run_c53_checks()
    assert result["status"] == STATUS and result["pass"]
    assert static_dependency_guard()["pass"] and poisoning_report()["pass"]


def test_c53_raw_emission_image_is_exact_frozen_triplet():
    result = color_validation()
    assert result["E_shape"] == [24, 3] and result["E_rank"] == 3 and result["triplet_rank"] == 3
    assert result["E_casimir"] < 2e-12 and result["intertwining"] < 2e-12
    assert max(result[x] for x in ("commutator", "anticommutator", "f_contraction", "d_contraction", "adjoint_algebra")) < 2e-12
    assert result["projector_equivalence"] < 2e-12 and result["leakage"] < 2e-12
    assert result["C_left"] < 2e-12 and result["C_right"] < 2e-12 and result["C_covariance"] < 2e-12
    assert np.isclose(CF, 4.0 / 3.0)


@pytest.mark.parametrize("resolution", [x.label for x in resolutions()])
def test_c53_full_product_and_reduced_physical_assemblies_agree(resolution):
    family = assemble_physical_vertex(resolution)
    assert family["shape"] == (family["colorless"]["primitive"].shape[0] * 3, family["colorless"]["primitive"].shape[1] * 3)
    assert family["primitive"].nnz > 0 and family["diagnostic"].nnz > 0
    assert family["assembly_residual"] < 2e-12
    assert M2_COEFFICIENT.sha256


def test_c53_matrix_free_columns_and_both_color_routes_are_independent_of_stored_vertex():
    label = resolutions()[0].label
    family = assemble_physical_vertex(label)
    reduced = matrix_free_physical_columns(label, route="reduced")
    full = matrix_free_physical_columns(label, route="full_product")
    assert np.linalg.norm(reduced-full) < 2e-12
    assert np.linalg.norm(reduced-family["diagnostic"].toarray()) < 2e-12
    vector = np.array([1+.2j, -.3+.4j, .2-.1j, .5+.3j, -.6+.2j, .1-.4j])
    assert np.linalg.norm(apply_physical_canonical_emission(vector,label,route="reduced") - apply_physical_canonical_emission(vector,label,route="full_product")) < 2e-12


def test_c53_adjoint_is_generated_and_phase_holdout_is_covariant():
    label = resolutions()[0].label
    block = generated_adjoint_and_block(label)
    assert block["adjoint_residual"] < 2e-12 and block["hermiticity"] < 2e-12
    rotated = triplet_rotation_holdout()
    assert rotated["covariance"] < 2e-12 and rotated["projector"] < 2e-12 and rotated["norm"] < 2e-12
    assert color_data()["C"].shape == (3, 3)


@pytest.mark.parametrize("fault_id", range(224))
def test_c53_224_live_physical_vertex_mutations_fail(fault_id):
    assert not validate_c53(mutate_live_c53(fault_id))
