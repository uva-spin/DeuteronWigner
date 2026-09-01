"""C409 number-preserving ``J_gJ_g:qg->qg`` product-block primitive.

The C407 longitudinal descendant already contains the product of both full
C406 one-gluon current matrix elements, the C114 nonzero-transfer inverse
square, and the adjoint color Casimir ``C_A=3``.  C409 therefore composes it
with the reduced transverse density-member sum, the spin identity, and a
residual triplet-color identity.  No extra derivative or color factor is
multiplied.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix, diags, eye, kron
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
)
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    apply_single_member_kernel,
    external_modes,
    weighted_spatial_kernel_csr,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    combined_spin_selection_matrix,
    triplet_color_product_matrix,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    c47_to_c403_mode_permutation,
    qg_factorized_axis_record,
)
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import (
    direct_sum_axis_record,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.descendants import (
    apply_longitudinal_diagonal,
    longitudinal_diagonal_exact,
)
from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure.weights import (
    source_i2_unit_weights,
)

from .authority import STATUS, reduced_transverse_authority
from .derivative_count import derivative_count_validation

PRODUCT = "J_gJ_g"
SECTOR = "qg->qg"


@lru_cache(maxsize=None)
def reduced_derivative_density_spatial_csr(resolution: str) -> csr_matrix:
    """Return the C409 reduced derivative-density spatial matrix in C47 order."""
    raw = weighted_spatial_kernel_csr(
        resolution, source_i2_unit_weights(resolution)
    )
    permutation = np.asarray(
        c47_to_c403_mode_permutation(resolution), dtype=np.int64
    )
    result = raw[permutation, :][:, permutation].tocsr().astype(np.complex128)
    if result.shape[0] == 0:
        raise RuntimeError("C409 reduced spatial kernel is empty")
    if result.data.size and not np.all(np.isfinite(result.data)):
        raise ValueError("C409 reduced spatial kernel contains nonfinite entries")
    return result


def apply_reduced_derivative_density_spatial(
    resolution: str,
    vectors: np.ndarray,
) -> np.ndarray:
    """Independent matrix-free application of the reduced spatial sum.

    Input and output use C47 intrinsic-mode order.  Individual C403 member
    actions are evaluated on the C403 axis, then mapped back.  This does not
    call ``reduced_derivative_density_spatial_csr``.
    """
    permutation = np.asarray(
        c47_to_c403_mode_permutation(resolution), dtype=np.int64
    )
    values = np.asarray(vectors, dtype=np.complex128)
    was_vector = values.ndim == 1
    if was_vector:
        values = values[:, None]
    if values.ndim != 2 or values.shape[0] != len(permutation):
        raise ValueError(
            "spatial vectors must have leading dimension {}".format(len(permutation))
        )
    if not np.all(np.isfinite(values)):
        raise ValueError("spatial vectors contain nonfinite entries")

    source = np.empty_like(values)
    source[permutation, :] = values
    result_source = np.zeros_like(source)
    for mode in external_modes(resolution):
        for column in range(source.shape[1]):
            result_source[:, column] += apply_single_member_kernel(
                resolution, mode, source[:, column]
            )
    result = result_source[permutation, :]
    return result[:, 0] if was_vector else result


@lru_cache(maxsize=None)
def jgjg_qg_csr(resolution: str) -> csr_matrix:
    longitudinal_values = np.asarray(
        [
            float(value)
            for value in longitudinal_diagonal_exact(
                resolution, "GLUON", SECTOR
            )
        ],
        dtype=np.float64,
    )
    longitudinal = diags(longitudinal_values, offsets=0, format="csr")
    spatial = reduced_derivative_density_spatial_csr(resolution)
    spin = csr_matrix(combined_spin_selection_matrix())
    # C_A=3 is already in the C407 longitudinal descendant.
    residual_color = eye(3, format="csr", dtype=np.complex128)
    return kron(
        kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"),
        residual_color,
        format="csr",
    )


def apply_jgjg_qg(resolution: str, vector: np.ndarray) -> np.ndarray:
    axis = qg_factorized_axis_record(resolution)
    pcount = int(axis["partition_count"])
    mcount = int(axis["transverse_mode_count"])
    dimension = int(axis["dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (dimension,):
        raise ValueError("vector must have shape ({},)".format(dimension))
    if not np.all(np.isfinite(values)):
        raise ValueError("vector contains nonfinite entries")

    tensor = values.reshape(pcount, mcount, 4, 3)
    spatial = np.empty_like(tensor)
    for partition in range(pcount):
        batch = tensor[partition].reshape(mcount, 12)
        spatial[partition] = apply_reduced_derivative_density_spatial(
            resolution, batch
        ).reshape(mcount, 4, 3)

    result = np.empty_like(spatial)
    for mode_index in range(mcount):
        for spin_index in range(4):
            for color_index in range(3):
                result[:, mode_index, spin_index, color_index] = (
                    apply_longitudinal_diagonal(
                        resolution,
                        "GLUON",
                        SECTOR,
                        spatial[:, mode_index, spin_index, color_index],
                    )
                )
    return result.reshape(dimension)


def jgjg_qg_linear_operator(resolution: str) -> LinearOperator:
    dimension = int(qg_factorized_axis_record(resolution)["dimension"])
    return LinearOperator(
        (dimension, dimension),
        matvec=lambda vector: apply_jgjg_qg(resolution, vector),
        rmatvec=lambda vector: apply_jgjg_qg(resolution, vector),
        dtype=np.complex128,
    )


def qg_partial_embedding_record(resolution: str) -> Mapping[str, Any]:
    axis = direct_sum_axis_record(resolution)
    payload = {
        "schema": "C409-C117-I2-JGJG-QG-PARTIAL-EMBEDDING-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": PRODUCT,
        "available_block": "qg->qg number-preserving product-block primitive",
        "available_path": (
            "deuteron_wigner.bridge.c409_c117_i2_derivative_density_reconciliation."
            "jgjg.jgjg_qg_csr"
        ),
        "qg_dimension": int(axis["qg_dimension"]),
        "q_sector_status": (
            "NUMBER_PRESERVING_BRANCH_NOT_APPLICABLE_BUT_PAIR_AND_VACUUM_BRANCHES_"
            "UNRESOLVED_NOT_ZERO"
        ),
        "q_to_qg_status": "EXACT_ZERO_WITH_C114_EVEN_GLUON_NUMBER_PARITY",
        "qg_to_q_status": "EXACT_ZERO_WITH_C114_EVEN_GLUON_NUMBER_PARITY",
        "missing_q_block_zero_filled": False,
        "complete_direct_sum_operator": False,
    }
    return dict(payload, root=content_root(payload))


def apply_complete_jgjg_direct_sum(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C409 cannot apply a complete J_gJ_g direct-sum block: q-sector gluon "
        "pair/vacuum branches and the common C117 normalization remain unavailable, not zero"
    )


def _single_counted_color_equivalence(resolution: str) -> float:
    """Compare C_A-in-longitudinal with C_A-in-color representations."""
    exact = longitudinal_diagonal_exact(resolution, "GLUON", SECTOR)
    no_color = diags(
        np.asarray([float(value / 3) for value in exact], dtype=np.float64),
        offsets=0,
        format="csr",
    )
    spatial = reduced_derivative_density_spatial_csr(resolution)
    spin = csr_matrix(combined_spin_selection_matrix())
    color = csr_matrix(triplet_color_product_matrix(PRODUCT))
    alternative = kron(
        kron(kron(no_color, spatial, format="csr"), spin, format="csr"),
        color,
        format="csr",
    )
    difference = (jgjg_qg_csr(resolution) - alternative).tocsr()
    return float(np.linalg.norm(difference.data))


@lru_cache(maxsize=1)
def jgjg_qg_validation() -> Mapping[str, Any]:
    derivative = derivative_count_validation()
    transverse = reduced_transverse_authority()
    rng = np.random.default_rng(40901)
    rows = []
    maximum_sparse_matrix_free = 0.0
    maximum_hermiticity = 0.0
    maximum_color_equivalence = 0.0
    minimum_spatial_eigenvalue = float("inf")
    minimum_longitudinal_value = float("inf")
    for resolution in RESOLUTION_LABELS:
        matrix = jgjg_qg_csr(resolution)
        axis = qg_factorized_axis_record(resolution)
        if matrix.shape != (int(axis["dimension"]), int(axis["dimension"])):
            raise RuntimeError("C409 qg product-block dimension mismatch")
        vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(
            size=matrix.shape[0]
        )
        direct = apply_jgjg_qg(resolution, vector)
        residual = float(np.linalg.norm(matrix @ vector - direct))
        hermiticity = float(np.linalg.norm((matrix - matrix.getH()).data))
        color_equivalence = _single_counted_color_equivalence(resolution)
        spatial = reduced_derivative_density_spatial_csr(resolution).toarray()
        spatial_minimum = float(np.min(np.linalg.eigvalsh(spatial)))
        longitudinal_values = tuple(
            float(value)
            for value in longitudinal_diagonal_exact(
                resolution, "GLUON", SECTOR
            )
        )
        longitudinal_minimum = min(longitudinal_values)
        maximum_sparse_matrix_free = max(maximum_sparse_matrix_free, residual)
        maximum_hermiticity = max(maximum_hermiticity, hermiticity)
        maximum_color_equivalence = max(
            maximum_color_equivalence, color_equivalence
        )
        minimum_spatial_eigenvalue = min(
            minimum_spatial_eigenvalue, spatial_minimum
        )
        minimum_longitudinal_value = min(
            minimum_longitudinal_value, longitudinal_minimum
        )
        rows.append(
            {
                "resolution": resolution,
                "shape": matrix.shape,
                "nonzero_entries": int(matrix.nnz),
                "partition_count": int(axis["partition_count"]),
                "transverse_mode_count": int(axis["transverse_mode_count"]),
                "sparse_matrix_free_residual": residual,
                "hermiticity_residual": hermiticity,
                "single_counted_C_A_equivalence_residual": color_equivalence,
                "minimum_spatial_eigenvalue_GeV2": spatial_minimum,
                "minimum_longitudinal_weight": longitudinal_minimum,
                "positive_semidefinite_from_factorization": bool(
                    spatial_minimum >= -1e-12 and longitudinal_minimum > 0
                ),
                "qg_partial_embedding": qg_partial_embedding_record(resolution),
            }
        )
    payload = {
        "schema": "C409-C117-I2-JGJG-QG-PRODUCT-BLOCK-VALIDATION-V1",
        "status": STATUS,
        "derivative_count_validation_root": derivative["root"],
        "reduced_transverse_authority_root": transverse["root"],
        "rows": tuple(rows),
        "row_count": len(rows),
        "maximum_sparse_matrix_free_residual": maximum_sparse_matrix_free,
        "maximum_hermiticity_residual": maximum_hermiticity,
        "maximum_single_counted_C_A_equivalence_residual": maximum_color_equivalence,
        "minimum_spatial_eigenvalue_GeV2": minimum_spatial_eigenvalue,
        "minimum_longitudinal_weight": minimum_longitudinal_value,
        "q_sector_zero_claimed": False,
        "extra_derivative_factors_applied": 0,
        "extra_color_Casimir_applied": 0,
        "source_routed_J_gJ_g_qg_paths": 3,
        "pass": bool(
            derivative["pass"]
            and maximum_sparse_matrix_free < 5e-10
            and maximum_hermiticity < 5e-12
            and maximum_color_equivalence < 5e-10
            and minimum_spatial_eigenvalue >= -1e-12
            and minimum_longitudinal_value > 0
        ),
        "classification": (
            "SOURCE_ROUTED_NUMBER_PRESERVING_JGJG_QG_PRODUCT_BLOCK_PRIMITIVE_"
            "NOT_COMPLETE_C117_ACTION"
        ),
        "complete_C117_action": False,
    }
    if not payload["pass"]:
        raise RuntimeError("C409 J_gJ_g qg validation failed")
    return dict(payload, root=content_root(payload))


__all__ = [
    "PRODUCT",
    "SECTOR",
    "reduced_derivative_density_spatial_csr",
    "apply_reduced_derivative_density_spatial",
    "jgjg_qg_csr",
    "apply_jgjg_qg",
    "jgjg_qg_linear_operator",
    "qg_partial_embedding_record",
    "apply_complete_jgjg_direct_sum",
    "jgjg_qg_validation",
]
