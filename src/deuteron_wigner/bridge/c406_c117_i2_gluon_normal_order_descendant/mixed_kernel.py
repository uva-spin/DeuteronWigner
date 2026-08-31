"""C406 source-derived mixed-current qg primitives and direct-sum embedding.

Only J_q K J_g and J_g K J_q are represented.  Their one-gluon derivative
ambiguity is closed by the C406 normal-ordering descendant.  The kernels still
factor the full field/state normalization, target-member aggregation, coupling,
and C117 coefficient and therefore are not complete Hamiltonian-coordinate
actions.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import block_diag, csr_matrix, kron
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
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import (
    direct_sum_axis_record,
)

from .normal_order import STATUS
from .routing import (
    MIXED_PRODUCTS,
    apply_mixed_partition_kernel,
    mixed_partition_kernel_csr,
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
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (len(permutation),):
        raise ValueError(f"spatial vector must have shape ({len(permutation)},)")
    c403_values = np.zeros_like(values)
    c403_values[permutation] = values
    result = apply_single_member_kernel(resolution, mode, c403_values)
    return result[permutation]


def mixed_qg_kernel_csr(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
) -> csr_matrix:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    mode = _mode(internal_mode)
    longitudinal = mixed_partition_kernel_csr(resolution, product)
    spatial = _spatial_kernel_c47_order(resolution, mode)
    spin = csr_matrix(combined_spin_selection_matrix())
    color = csr_matrix(triplet_color_product_matrix(product))
    return kron(
        kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"),
        color,
        format="csr",
    )


def apply_mixed_qg_kernel(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    vector: np.ndarray,
) -> np.ndarray:
    if product not in MIXED_PRODUCTS:
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
                    apply_mixed_partition_kernel(
                        resolution,
                        product,
                        spatial_applied[:, mode_index, spin_index, color_index],
                    )
                )
    return result.reshape(dimension)


def mixed_qg_linear_operator(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
) -> LinearOperator:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    partner = "J_gJ_q" if product == "J_qJ_g" else "J_qJ_g"
    mode = _mode(internal_mode)
    dimension = int(qg_factorized_axis_record(resolution)["dimension"])
    return LinearOperator(
        shape=(dimension, dimension),
        matvec=lambda vector: apply_mixed_qg_kernel(
            resolution, product, mode, vector
        ),
        rmatvec=lambda vector: apply_mixed_qg_kernel(
            resolution, partner, mode, vector
        ),
        dtype=np.complex128,
    )


def mixed_direct_sum_csr(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
) -> csr_matrix:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    axis = direct_sum_axis_record(resolution)
    q_zero = csr_matrix((int(axis["q_dimension"]), int(axis["q_dimension"])), dtype=np.complex128)
    qg = mixed_qg_kernel_csr(resolution, product, internal_mode)
    return block_diag((q_zero, qg), format="csr")


def apply_mixed_direct_sum(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
    vector: np.ndarray,
) -> np.ndarray:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    total = int(axis["direct_sum_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape != (total,):
        raise ValueError(f"vector must have shape ({total},)")
    result = np.zeros_like(values)
    result[qdim:] = apply_mixed_qg_kernel(
        resolution, product, internal_mode, values[qdim:]
    )
    return result


def mixed_kernel_record(
    resolution: str,
    product: str,
    internal_mode: HOMode | Sequence[int],
) -> Mapping[str, Any]:
    mode = _mode(internal_mode)
    matrix = mixed_qg_kernel_csr(resolution, product, mode)
    partner = "J_gJ_q" if product == "J_qJ_g" else "J_qJ_g"
    partner_matrix = mixed_qg_kernel_csr(resolution, partner, mode)
    payload = {
        "schema": "C406-C117-I2-MIXED-CURRENT-QG-PRIMITIVE-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product,
        "internal_mode": mode.to_record(),
        "shape": matrix.shape,
        "nonzero_entries": int(matrix.nnz),
        "adjoint_product": partner,
        "adjoint_residual": float(np.linalg.norm((matrix.getH() - partner_matrix).data)),
        "included_factors": (
            "C404 exact Q0 1/n^2 external mixed-current transfer",
            "C406 normal-ordered gluon source phase and -(k_bra+k_ket) factor",
            "C403 transverse I2 single-member spatial kernel",
            "C404 J+ spin-selection and triplet-color product",
            "C406 exact q-sector zero for one-gluon mixed-current products",
        ),
        "factored_or_missing": (
            "route-reconciled field/state normalization and finite-cell prefactor",
            "C405-to-C125 witness/target aggregation",
            "member weights and count-once target multiplicity",
            "C114 M2 conversion, g_s^2, and c_C117_1",
            "same-species JqJq/JgJg contraction descendants",
        ),
        "source_qualified_normal_ordering_class": True,
        "source_qualified_complete_product_matrix": False,
        "classification": "MIXED_CURRENT_NORMAL_ORDERED_NUMERICAL_PRIMITIVE_NOT_C117_OPERATOR",
        "complete_C117_action": False,
        "complete_C396_action": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def mixed_kernel_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(406)
    rows = []
    maximum_sparse_matrix_free_residual = 0.0
    maximum_adjoint_residual = 0.0
    maximum_direct_sum_residual = 0.0
    maximum_q_block_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        mode = external_modes(resolution)[0]
        qg_dimension = int(qg_factorized_axis_record(resolution)["dimension"])
        axis = direct_sum_axis_record(resolution)
        q_dimension = int(axis["q_dimension"])
        total = int(axis["direct_sum_dimension"])
        qg_vector = rng.normal(size=qg_dimension) + 1j * rng.normal(size=qg_dimension)
        direct_vector = rng.normal(size=total) + 1j * rng.normal(size=total)
        for product in MIXED_PRODUCTS:
            matrix = mixed_qg_kernel_csr(resolution, product, mode)
            direct = apply_mixed_qg_kernel(resolution, product, mode, qg_vector)
            residual = float(np.linalg.norm(matrix @ qg_vector - direct))
            partner = "J_gJ_q" if product == "J_qJ_g" else "J_qJ_g"
            partner_matrix = mixed_qg_kernel_csr(resolution, partner, mode)
            adjoint = float(np.linalg.norm((matrix.getH() - partner_matrix).data))
            full = mixed_direct_sum_csr(resolution, product, mode)
            full_direct = apply_mixed_direct_sum(
                resolution, product, mode, direct_vector
            )
            direct_sum_residual = float(np.linalg.norm(full @ direct_vector - full_direct))
            q_block_residual = float(np.linalg.norm(full[:q_dimension, :q_dimension].data))
            maximum_sparse_matrix_free_residual = max(
                maximum_sparse_matrix_free_residual, residual
            )
            maximum_adjoint_residual = max(maximum_adjoint_residual, adjoint)
            maximum_direct_sum_residual = max(
                maximum_direct_sum_residual, direct_sum_residual
            )
            maximum_q_block_residual = max(maximum_q_block_residual, q_block_residual)
            rows.append(
                {
                    "resolution": resolution,
                    "product": product,
                    "internal_mode": mode.to_record(),
                    "qg_dimension": qg_dimension,
                    "direct_sum_dimension": total,
                    "nonzero_entries": int(matrix.nnz),
                    "sparse_matrix_free_residual": residual,
                    "adjoint_residual": adjoint,
                    "direct_sum_residual": direct_sum_residual,
                    "q_sector_zero_residual": q_block_residual,
                }
            )
    payload = {
        "schema": "C406-C117-I2-MIXED-CURRENT-KERNEL-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "maximum_sparse_matrix_free_residual": maximum_sparse_matrix_free_residual,
        "maximum_adjoint_residual": maximum_adjoint_residual,
        "maximum_direct_sum_residual": maximum_direct_sum_residual,
        "maximum_q_sector_zero_residual": maximum_q_block_residual,
        "pass": bool(
            maximum_sparse_matrix_free_residual < 3e-11
            and maximum_adjoint_residual < 3e-11
            and maximum_direct_sum_residual < 3e-11
            and maximum_q_block_residual == 0.0
        ),
        "complete_C117_action": False,
        "rank_status": "RANK_NOT_EVALUATED",
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "mixed_qg_kernel_csr",
    "apply_mixed_qg_kernel",
    "mixed_qg_linear_operator",
    "mixed_direct_sum_csr",
    "apply_mixed_direct_sum",
    "mixed_kernel_record",
    "mixed_kernel_validation",
]
