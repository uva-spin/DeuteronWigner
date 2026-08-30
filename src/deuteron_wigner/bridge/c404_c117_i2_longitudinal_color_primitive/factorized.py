"""C404 factorized qg longitudinal/spatial/spin/color skeletons.

These matrices are algebraic tensor-product stress tests of factors that have
independent numerical authority.  They are deliberately named *skeletons*:
C114/C115/C119 do not yet provide the product-specific normal-ordering and
external-mode contraction map that would identify these tensor products with
physical current-product matrix elements.  The source coefficient, finite-cell
normalization, ordered gluon-current momentum factor, member/target aggregation,
g_s^2, and c_C117_1 coefficient also remain absent.  No skeleton is a source-
qualified C117 or C396 coordinate action.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix, identity, kron
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    apply_single_member_kernel,
    external_modes,
    single_member_kernel_csr,
)

from .color_spin import (
    PRODUCTS,
    combined_spin_selection_matrix,
    triplet_color_product_matrix,
)
from .longitudinal import (
    STATUS,
    apply_partition_transfer,
    c47_relative_modes,
    c47_to_c403_mode_permutation,
    partition_axis,
    partition_transfer_matrix_csr,
    qg_factorized_axis_record,
)


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

def qg_skeleton_csr(resolution: str, product: str, internal_mode: HOMode | Sequence[int]) -> csr_matrix:
    if product not in PRODUCTS:
        raise KeyError(product)
    mode = _mode(internal_mode)
    longitudinal = partition_transfer_matrix_csr(resolution)
    spatial = _spatial_kernel_c47_order(resolution, mode)
    spin = csr_matrix(combined_spin_selection_matrix())
    color = csr_matrix(triplet_color_product_matrix(product))
    return kron(kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"), color, format="csr")


def apply_qg_skeleton(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    vector: np.ndarray,
) -> np.ndarray:
    """Independent tensor action in C47 order, without building the CSR matrix."""
    if product not in PRODUCTS:
        raise KeyError(product)
    mode = _mode(internal_mode)
    pcount = len(partition_axis(resolution))
    mcount = len(c47_relative_modes(resolution))
    values = np.asarray(vector, dtype=np.complex128)
    dimension = pcount * mcount * 4 * 3
    if values.ndim != 1 or values.shape != (dimension,):
        raise ValueError(f"vector must have shape ({dimension},)")
    tensor = values.reshape(pcount, mcount, 4, 3)
    # Apply color, then spin (identity today but kept route-explicit), then
    # spatial, then longitudinal.  Each route is independent of scipy.kron.
    color = triplet_color_product_matrix(product)
    spin = combined_spin_selection_matrix()
    work = np.einsum("ab,pmsb->pmsa", color, tensor, optimize=True)
    work = np.einsum("ab,pmbc->pmac", spin, work, optimize=True)
    spatial_applied = np.empty_like(work)
    for p in range(pcount):
        for h in range(4):
            for c in range(3):
                spatial_applied[p, :, h, c] = _apply_spatial_kernel_c47_order(
                    resolution, mode, work[p, :, h, c]
                )
    result = np.empty_like(spatial_applied)
    for m in range(mcount):
        for h in range(4):
            for c in range(3):
                result[:, m, h, c] = apply_partition_transfer(
                    resolution, spatial_applied[:, m, h, c]
                )
    return result.reshape(dimension)


def qg_skeleton_linear_operator(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
) -> LinearOperator:
    axis = qg_factorized_axis_record(resolution)
    dimension = int(axis["dimension"])
    mode = _mode(internal_mode)
    return LinearOperator(
        shape=(dimension, dimension),
        matvec=lambda vector: apply_qg_skeleton(resolution, product, mode, vector),
        rmatvec=lambda vector: apply_qg_skeleton(resolution, product, mode, vector),
        dtype=np.complex128,
    )


def skeleton_record(resolution: str, product: str, internal_mode: HOMode | Sequence[int]) -> Mapping[str, Any]:
    mode = _mode(internal_mode)
    axis = qg_factorized_axis_record(resolution)
    matrix = qg_skeleton_csr(resolution, product, mode)
    payload = {
        "schema": "C404-C117-I2-QG-FACTORIZED-SKELETON-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product,
        "internal_mode": mode.to_record(),
        "shape": matrix.shape,
        "nonzero_entries": int(matrix.nnz),
        "units": "GeV^2 times unresolved C114/C119 source-normalization factors",
        "basis_order": axis["ordering"],
        "included_factors": (
            "C114 dimensionless Q0 nonzero-transfer 1/n^2",
            "C403 I2 transverse spatial kernel",
            "C115 J+ helicity/polarization selection",
            "C45/C47 triplet color-charge product",
        ),
        "missing_factors": (
            "product-specific C114/C115/C119 normal-ordering and external-mode contraction map",
            "C114 source coefficient -1/2",
            "C119 field and state finite-cell normalization",
            "C119 ordered gluon-current derivative momentum factor",
            "C115/C119 source phase bridge for the adjoint current",
            "C115 exact Pminus-to-M2 scale cancellation",
            "C124/C125 member and target count-once aggregation",
            "q-sector normal-ordering/contraction branch",
            "Hermitian source-order reverse at the complete-current level",
            "g_s^2 and c_C117_1 coefficients",
        ),
        "source_qualified_product_topology": False,
        "classification": "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING",
        "complete_C117_action": False,
        "complete_C396_action": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def skeleton_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(404)
    rows = []
    maximum_residual = 0.0
    maximum_hermiticity_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        modes = external_modes(resolution)
        representatives = tuple(dict.fromkeys((modes[0], modes[len(modes) // 2], modes[-1])))
        dimension = qg_factorized_axis_record(resolution)["dimension"]
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        for product in PRODUCTS:
            for mode in representatives:
                matrix = qg_skeleton_csr(resolution, product, mode)
                direct = apply_qg_skeleton(resolution, product, mode, vector)
                residual = float(np.linalg.norm(matrix @ vector - direct))
                hermiticity = float(np.linalg.norm((matrix - matrix.getH()).data)) if matrix.nnz else 0.0
                maximum_residual = max(maximum_residual, residual)
                maximum_hermiticity_residual = max(maximum_hermiticity_residual, hermiticity)
                rows.append(
                    {
                        "resolution": resolution,
                        "product": product,
                        "internal_mode": mode.to_record(),
                        "dimension": dimension,
                        "nonzero_entries": int(matrix.nnz),
                        "sparse_matrix_free_residual": residual,
                        "hermiticity_residual": hermiticity,
                    }
                )
    payload = {
        "schema": "C404-C117-I2-QG-SKELETON-VALIDATION-V1",
        "status": STATUS,
        "rows": rows,
        "maximum_sparse_matrix_free_residual": maximum_residual,
        "maximum_hermiticity_residual": maximum_hermiticity_residual,
        "pass": bool(maximum_residual < 2e-11 and maximum_hermiticity_residual < 2e-11),
        "source_qualified_product_topology": False,
        "classification": "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING",
        "complete_C117_action": False,
        "rank_status": "RANK_NOT_EVALUATED",
    }
    return {**payload, "root": content_root(payload)}


def apply_complete_c117_i2(*_args, **_kwargs):
    raise RuntimeError(
        "C404 primitive is not a complete C117 I2 coordinate action; C114/C119 normalization, "
        "ordered gluon derivative, aggregation, q-sector contractions, and coefficients remain unavailable"
    )


__all__ = [
    "qg_skeleton_csr",
    "apply_qg_skeleton",
    "qg_skeleton_linear_operator",
    "skeleton_record",
    "skeleton_validation",
    "apply_complete_c117_i2",
]
