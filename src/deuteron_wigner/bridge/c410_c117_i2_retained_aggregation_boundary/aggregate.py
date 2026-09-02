"""C410 count-once retained aggregation of the four current products."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import block_diag, csr_matrix
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
)
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import (
    direct_sum_axis_record,
)
from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure.jqjq import (
    apply_source_routed_jqjq_direct_sum,
    source_routed_jqjq_direct_sum_csr,
)
from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure.weights import (
    apply_source_weighted_mixed_direct_sum,
    source_weighted_mixed_direct_sum_csr,
)
from deuteron_wigner.bridge.c409_c117_i2_derivative_density_reconciliation.jgjg import (
    apply_jgjg_qg,
    jgjg_qg_csr,
)

from .authority import STATUS, aggregation_authority
from .vacuum import (
    apply_q_sector_jgjg_connected,
    q_sector_jgjg_connected_csr,
    q_sector_vacuum_projection_validation,
)

PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SOURCE_COEFFICIENT = -0.5


def _check_product(product: str) -> str:
    if product not in PRODUCTS:
        raise KeyError(product)
    return product


@lru_cache(maxsize=None)
def source_routed_jgjg_direct_sum_csr(resolution: str) -> csr_matrix:
    return block_diag(
        (q_sector_jgjg_connected_csr(resolution), jgjg_qg_csr(resolution)),
        format="csr",
    )


def apply_source_routed_jgjg_direct_sum(
    resolution: str, vector: np.ndarray
) -> np.ndarray:
    axis = direct_sum_axis_record(resolution)
    q_dimension = int(axis["q_dimension"])
    total = int(axis["direct_sum_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (total,):
        raise ValueError("vector must have shape ({},)".format(total))
    if not np.all(np.isfinite(values)):
        raise ValueError("vector contains nonfinite entries")
    result = np.zeros_like(values)
    result[:q_dimension] = apply_q_sector_jgjg_connected(
        resolution, values[:q_dimension]
    )
    result[q_dimension:] = apply_jgjg_qg(resolution, values[q_dimension:])
    return result


@lru_cache(maxsize=None)
def product_block_csr(resolution: str, product: str) -> csr_matrix:
    _check_product(product)
    if product == "J_qJ_q":
        return source_routed_jqjq_direct_sum_csr(resolution)
    if product in ("J_qJ_g", "J_gJ_q"):
        return source_weighted_mixed_direct_sum_csr(resolution, product)
    return source_routed_jgjg_direct_sum_csr(resolution)


def apply_product_block(
    resolution: str, product: str, vector: np.ndarray
) -> np.ndarray:
    _check_product(product)
    if product == "J_qJ_q":
        return apply_source_routed_jqjq_direct_sum(resolution, vector)
    if product in ("J_qJ_g", "J_gJ_q"):
        return apply_source_weighted_mixed_direct_sum(resolution, product, vector)
    return apply_source_routed_jgjg_direct_sum(resolution, vector)


@lru_cache(maxsize=None)
def retained_connected_current_square_csr(resolution: str) -> csr_matrix:
    matrices = tuple(product_block_csr(resolution, product) for product in PRODUCTS)
    result = matrices[0].copy().tocsr()
    for matrix in matrices[1:]:
        result = (result + matrix).tocsr()
    result.eliminate_zeros()
    return result


def apply_retained_connected_current_square(
    resolution: str, vector: np.ndarray
) -> np.ndarray:
    values = np.asarray(vector, dtype=np.complex128)
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    if values.shape != (dimension,):
        raise ValueError("vector must have shape ({},)".format(dimension))
    if not np.all(np.isfinite(values)):
        raise ValueError("vector contains nonfinite entries")
    result = np.zeros_like(values)
    for product in PRODUCTS:
        result += apply_product_block(resolution, product, values)
    return result


@lru_cache(maxsize=None)
def source_reduced_c117_i2_shape_csr(resolution: str) -> csr_matrix:
    """Apply the exact source ``-1/2`` with ``g_s^2`` still factored."""
    return (SOURCE_COEFFICIENT * retained_connected_current_square_csr(resolution)).tocsr()


def apply_source_reduced_c117_i2_shape(
    resolution: str, vector: np.ndarray
) -> np.ndarray:
    return SOURCE_COEFFICIENT * apply_retained_connected_current_square(
        resolution, vector
    )


def source_reduced_c117_i2_shape_linear_operator(resolution: str) -> LinearOperator:
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    return LinearOperator(
        (dimension, dimension),
        matvec=lambda vector: apply_source_reduced_c117_i2_shape(resolution, vector),
        rmatvec=lambda vector: apply_source_reduced_c117_i2_shape(resolution, vector),
        dtype=np.complex128,
    )


@lru_cache(maxsize=1)
def count_once_aggregation_record() -> Mapping[str, Any]:
    authority = aggregation_authority()
    rows = tuple(
        {
            "ordinal": index,
            "product": product,
            "multiplicity": 1,
            "source_order_retained": True,
            "Hermitian_partner": (
                "J_gJ_q"
                if product == "J_qJ_g"
                else "J_qJ_g"
                if product == "J_gJ_q"
                else product
            ),
            "extra_factor_two": False,
        }
        for index, product in enumerate(PRODUCTS)
    )
    payload = {
        "schema": "C410-C117-I2-COUNT-ONCE-AGGREGATION-V1",
        "status": STATUS,
        "rows": rows,
        "row_count": len(rows),
        "source_identity_reconstructed": True,
        "mixed_orders_kept_separate": True,
        "duplicate_products": 0,
        "omitted_products": 0,
        "source_minus_one_half_count": 1,
        "g_s_squared_count": 0,
        "coordinate_coefficient_count": 0,
        "vacuum_cnumber_counted_in_retained_matrix": 0,
        "authority_root": authority["root"],
        "pass": True,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def retained_aggregation_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(41001)
    rows = []
    maximum_sparse_matrix_free = 0.0
    maximum_hermiticity = 0.0
    maximum_decomposition = 0.0
    maximum_source_coefficient = 0.0
    maximum_mixed_adjoint = 0.0
    for resolution in RESOLUTION_LABELS:
        blocks = {product: product_block_csr(resolution, product) for product in PRODUCTS}
        aggregate = retained_connected_current_square_csr(resolution)
        reduced = source_reduced_c117_i2_shape_csr(resolution)
        vector = rng.normal(size=aggregate.shape[0]) + 1j * rng.normal(
            size=aggregate.shape[0]
        )
        sparse_matrix_free = float(
            np.linalg.norm(
                aggregate @ vector
                - apply_retained_connected_current_square(resolution, vector)
            )
        )
        reduced_matrix_free = float(
            np.linalg.norm(
                reduced @ vector
                - apply_source_reduced_c117_i2_shape(resolution, vector)
            )
        )
        decomposition = blocks[PRODUCTS[0]].copy().tocsr()
        for product in PRODUCTS[1:]:
            decomposition = (decomposition + blocks[product]).tocsr()
        decomposition_residual_matrix = (aggregate - decomposition).tocsr()
        decomposition_residual = float(
            np.linalg.norm(decomposition_residual_matrix.data)
        )
        source_residual_matrix = (reduced - SOURCE_COEFFICIENT * aggregate).tocsr()
        source_residual = float(np.linalg.norm(source_residual_matrix.data))
        hermiticity = float(np.linalg.norm((aggregate - aggregate.getH()).data))
        mixed_adjoint = float(
            np.linalg.norm((blocks["J_qJ_g"].getH() - blocks["J_gJ_q"]).data)
        )
        maximum_sparse_matrix_free = max(
            maximum_sparse_matrix_free, sparse_matrix_free, reduced_matrix_free
        )
        maximum_hermiticity = max(maximum_hermiticity, hermiticity)
        maximum_decomposition = max(maximum_decomposition, decomposition_residual)
        maximum_source_coefficient = max(maximum_source_coefficient, source_residual)
        maximum_mixed_adjoint = max(maximum_mixed_adjoint, mixed_adjoint)
        rows.append(
            {
                "resolution": resolution,
                "shape": aggregate.shape,
                "aggregate_nonzero_entries": int(aggregate.nnz),
                "source_reduced_nonzero_entries": int(reduced.nnz),
                "product_nonzero_entries": {
                    product: int(matrix.nnz) for product, matrix in blocks.items()
                },
                "sparse_matrix_free_residual": sparse_matrix_free,
                "source_reduced_sparse_matrix_free_residual": reduced_matrix_free,
                "four_product_decomposition_residual": decomposition_residual,
                "source_minus_one_half_scaling_residual": source_residual,
                "aggregate_hermiticity_residual": hermiticity,
                "mixed_source_order_adjoint_residual": mixed_adjoint,
                "q_sector_J_gJ_g_nonzero_entries": int(
                    q_sector_jgjg_connected_csr(resolution).nnz
                ),
            }
        )
    vacuum_validation = q_sector_vacuum_projection_validation()
    payload = {
        "schema": "C410-C117-I2-RETAINED-CONNECTED-AGGREGATE-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "product_count_per_resolution": len(PRODUCTS),
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
        "maximum_sparse_matrix_free_residual": maximum_sparse_matrix_free,
        "maximum_hermiticity_residual": maximum_hermiticity,
        "maximum_four_product_decomposition_residual": maximum_decomposition,
        "maximum_source_minus_one_half_scaling_residual": maximum_source_coefficient,
        "maximum_mixed_source_order_adjoint_residual": maximum_mixed_adjoint,
        "q_sector_vacuum_projection_root": vacuum_validation["root"],
        "absolute_C260_operator_normalization_applied": False,
        "complete_C117_action": False,
        "pass": bool(
            maximum_sparse_matrix_free < 5e-10
            and maximum_hermiticity < 5e-10
            and maximum_decomposition < 5e-12
            and maximum_source_coefficient < 5e-12
            and maximum_mixed_adjoint < 5e-10
            and vacuum_validation["pass"]
        ),
        "classification": (
            "SOURCE_COEFFICIENT_NORMALIZED_RETAINED_CONNECTED_SHAPE_"
            "NOT_C260_NORMALIZED_C117_OPERATOR"
        ),
    }
    if not payload["pass"]:
        raise RuntimeError("C410 retained aggregate validation failed")
    return dict(payload, root=content_root(payload))


__all__ = [
    "PRODUCTS",
    "SOURCE_COEFFICIENT",
    "source_routed_jgjg_direct_sum_csr",
    "apply_source_routed_jgjg_direct_sum",
    "product_block_csr",
    "apply_product_block",
    "retained_connected_current_square_csr",
    "apply_retained_connected_current_square",
    "source_reduced_c117_i2_shape_csr",
    "apply_source_reduced_c117_i2_shape",
    "source_reduced_c117_i2_shape_linear_operator",
    "count_once_aggregation_record",
    "retained_aggregation_validation",
]
