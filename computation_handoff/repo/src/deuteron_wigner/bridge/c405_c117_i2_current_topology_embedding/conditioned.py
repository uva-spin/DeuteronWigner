"""Conditional qg current-product kernels for C405.

The kernels in this module combine only independently verified numerical
primitives:

* the C114 Q0 longitudinal transfer factor from C404;
* an explicit, caller-selected ordered gluon derivative mode assignment;
* the C403 transverse I2 single-member kernel;
* the C404 spin-selection and triplet-color products.

They remain conditional stress-test kernels.  A source-qualified
normal-ordering descendant, finite-cell/state normalization, source phase,
member/target multiplicity, q-sector block, coupling, and C117 coefficient are
not supplied here.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix, kron
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    apply_single_member_kernel,
    external_modes,
    single_member_kernel_csr,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    combined_spin_selection_matrix,
    triplet_color_product_matrix,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    c47_relative_modes,
    c47_to_c403_mode_permutation,
    qg_factorized_axis_record,
)

from .derivative_order import (
    adjoint_derivative_assignment,
    apply_ordered_partition_kernel,
    derivative_assignments,
    ordered_partition_kernel_csr,
)
from .topology import PRODUCTS, STATUS


def _mode(value: HOMode | Sequence[int]) -> HOMode:
    if isinstance(value, HOMode):
        return value
    if len(value) != 2:
        raise ValueError("HO mode must be (n,m)")
    return HOMode(int(value[0]), int(value[1]))


def _spatial_kernel_c47_order(resolution: str, mode: HOMode) -> csr_matrix:
    raw = single_member_kernel_csr(resolution, mode)
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    return raw[permutation, :][:, permutation].tocsr()


def _apply_spatial_kernel_c47_order(
    resolution: str,
    mode: HOMode,
    vector: np.ndarray,
) -> np.ndarray:
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    c47_values = np.asarray(vector, dtype=np.complex128)
    if c47_values.shape != (len(permutation),):
        raise ValueError(f"spatial vector must have shape ({len(permutation)},)")
    c403_values = np.zeros_like(c47_values)
    c403_values[permutation] = c47_values
    c403_result = apply_single_member_kernel(resolution, mode, c403_values)
    return c403_result[permutation]


def conditional_qg_kernel_csr(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    derivative_legs: Sequence[str],
) -> csr_matrix:
    if product not in PRODUCTS:
        raise KeyError(product)
    mode = _mode(internal_mode)
    longitudinal = ordered_partition_kernel_csr(resolution, product, derivative_legs)
    spatial = _spatial_kernel_c47_order(resolution, mode)
    spin = csr_matrix(combined_spin_selection_matrix())
    color = csr_matrix(triplet_color_product_matrix(product))
    return kron(
        kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"),
        color,
        format="csr",
    )


def apply_conditional_qg_kernel(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    derivative_legs: Sequence[str],
    vector: np.ndarray,
) -> np.ndarray:
    if product not in PRODUCTS:
        raise KeyError(product)
    mode = _mode(internal_mode)
    axis = qg_factorized_axis_record(resolution)
    pcount = int(axis["partition_count"])
    mcount = len(c47_relative_modes(resolution))
    dimension = int(axis["dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape != (dimension,):
        raise ValueError(f"vector must have shape ({dimension},)")
    tensor = values.reshape(pcount, mcount, 4, 3)

    color = triplet_color_product_matrix(product)
    spin = combined_spin_selection_matrix()
    work = np.einsum("ab,pmsb->pmsa", color, tensor, optimize=True)
    work = np.einsum("ab,pmbc->pmac", spin, work, optimize=True)

    spatial_applied = np.empty_like(work)
    for partition in range(pcount):
        for spin_index in range(4):
            for color_index in range(3):
                spatial_applied[partition, :, spin_index, color_index] = (
                    _apply_spatial_kernel_c47_order(
                        resolution,
                        mode,
                        work[partition, :, spin_index, color_index],
                    )
                )

    result = np.empty_like(spatial_applied)
    for mode_index in range(mcount):
        for spin_index in range(4):
            for color_index in range(3):
                result[:, mode_index, spin_index, color_index] = (
                    apply_ordered_partition_kernel(
                        resolution,
                        product,
                        derivative_legs,
                        spatial_applied[:, mode_index, spin_index, color_index],
                    )
                )
    return result.reshape(dimension)


def conditional_qg_linear_operator(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    derivative_legs: Sequence[str],
) -> LinearOperator:
    axis = qg_factorized_axis_record(resolution)
    dimension = int(axis["dimension"])
    mode = _mode(internal_mode)
    legs = tuple(derivative_legs)
    partner, partner_legs = adjoint_derivative_assignment(product, legs)
    return LinearOperator(
        shape=(dimension, dimension),
        matvec=lambda vector: apply_conditional_qg_kernel(
            resolution, product, mode, legs, vector
        ),
        rmatvec=lambda vector: apply_conditional_qg_kernel(
            resolution, partner, mode, partner_legs, vector
        ),
        dtype=np.complex128,
    )


def conditional_kernel_record(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    derivative_legs: Sequence[str],
) -> Mapping[str, Any]:
    mode = _mode(internal_mode)
    matrix = conditional_qg_kernel_csr(resolution, product, mode, derivative_legs)
    partner, partner_legs = adjoint_derivative_assignment(product, derivative_legs)
    partner_matrix = conditional_qg_kernel_csr(
        resolution, partner, mode, partner_legs
    )
    payload = {
        "schema": "C405-C117-I2-CONDITIONAL-QG-CURRENT-KERNEL-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product,
        "derivative_legs": tuple(derivative_legs),
        "internal_mode": mode.to_record(),
        "shape": matrix.shape,
        "nonzero_entries": int(matrix.nnz),
        "adjoint_product": partner,
        "adjoint_derivative_legs": partner_legs,
        "adjoint_residual": float(np.linalg.norm((matrix.getH() - partner_matrix).data)),
        "included_factors": (
            "C404 exact Q0 1/n^2 longitudinal transfer",
            "explicit dimensionless k_g factor for every caller-selected gluon derivative leg",
            "C403 transverse I2 single-member spatial kernel",
            "C404 J+ spin-selection and triplet-color product",
        ),
        "factored_or_missing": (
            "pi/L for every gluon derivative",
            "product-specific normal-ordering descendant",
            "finite-cell and state normalization multiplicities",
            "source phase and contraction sign",
            "member weights and count-once target aggregation",
            "q-sector diagonal block",
            "C114 source coefficient, M2 conversion, g_s^2, and c_C117_1",
        ),
        "source_qualified_product_topology": False,
        "classification": "CALLER_CONDITIONED_CURRENT_ORDER_STRESS_TEST_NOT_OPERATOR_BINDING",
        "complete_C117_action": False,
        "complete_C396_action": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def conditional_kernel_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(405)
    rows = []
    maximum_sparse_matrix_free_residual = 0.0
    maximum_adjoint_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        mode = external_modes(resolution)[0]
        dimension = int(qg_factorized_axis_record(resolution)["dimension"])
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        for product in PRODUCTS:
            for legs in derivative_assignments(product):
                matrix = conditional_qg_kernel_csr(resolution, product, mode, legs)
                direct = apply_conditional_qg_kernel(
                    resolution, product, mode, legs, vector
                )
                residual = float(np.linalg.norm(matrix @ vector - direct))
                partner, partner_legs = adjoint_derivative_assignment(product, legs)
                partner_matrix = conditional_qg_kernel_csr(
                    resolution, partner, mode, partner_legs
                )
                adjoint = float(np.linalg.norm((matrix.getH() - partner_matrix).data))
                maximum_sparse_matrix_free_residual = max(
                    maximum_sparse_matrix_free_residual, residual
                )
                maximum_adjoint_residual = max(maximum_adjoint_residual, adjoint)
                rows.append(
                    {
                        "resolution": resolution,
                        "product": product,
                        "derivative_legs": legs,
                        "internal_mode": mode.to_record(),
                        "dimension": dimension,
                        "nonzero_entries": int(matrix.nnz),
                        "sparse_matrix_free_residual": residual,
                        "adjoint_product": partner,
                        "adjoint_derivative_legs": partner_legs,
                        "adjoint_residual": adjoint,
                    }
                )
    payload = {
        "schema": "C405-C117-I2-CONDITIONAL-QG-KERNEL-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "maximum_sparse_matrix_free_residual": maximum_sparse_matrix_free_residual,
        "maximum_adjoint_residual": maximum_adjoint_residual,
        "pass": bool(
            maximum_sparse_matrix_free_residual < 2e-11
            and maximum_adjoint_residual < 2e-11
        ),
        "source_qualified_product_topology": False,
        "classification": "CALLER_CONDITIONED_CURRENT_ORDER_STRESS_TEST_NOT_OPERATOR_BINDING",
        "complete_C117_action": False,
        "rank_status": "RANK_NOT_EVALUATED",
    }
    return {**payload, "root": content_root(payload)}



__all__ = [
    "conditional_qg_kernel_csr",
    "apply_conditional_qg_kernel",
    "conditional_qg_linear_operator",
    "conditional_kernel_record",
    "conditional_kernel_validation",
]
