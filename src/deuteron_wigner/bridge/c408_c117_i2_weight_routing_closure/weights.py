"""C408 source-descendant unit-member sums for the C117 I2 graph.

The C124/C126 descendant assigns the member multiplier ``1`` to I2 members.
C408 applies that exact multiplier to the C403 finite transverse member axis.
The longitudinal, helicity and color contraction axes are already evaluated in
C406/C407, so the remaining spatial sum contains one term per canonical C403
transverse member, with no hidden multiplicity.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import block_diag, csr_matrix, eye, kron
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    apply_single_member_kernel,
    external_modes,
    single_member_kernel_dense,
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
from deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant.routing import (
    apply_mixed_partition_kernel,
    mixed_partition_kernel_csr,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.jqjq_qg import (
    apply_jqjq_qg_conditioned,
    jqjq_qg_conditioned_csr,
)

from .authority import STATUS, i2_member_weight_authority

MIXED_PRODUCTS = ("J_qJ_g", "J_gJ_q")


@lru_cache(maxsize=None)
def source_i2_unit_weights(resolution: str) -> Mapping[HOMode, float]:
    weights = {mode: 1.0 for mode in external_modes(resolution)}
    if not weights or any(value != 1.0 for value in weights.values()):
        raise RuntimeError("C408 I2 unit-member map construction failed")
    return weights


def source_i2_unit_weight_record(resolution: str) -> Mapping[str, Any]:
    weights = source_i2_unit_weights(resolution)
    payload = {
        "schema": "C408-C117-I2-SOURCE-DESCENDANT-UNIT-MEMBER-WEIGHTS-V1",
        "status": STATUS,
        "resolution": resolution,
        "member_count": len(weights),
        "members": tuple(
            {"mode": mode.to_record(), "multiplier": 1, "exact": "1"}
            for mode in sorted(weights)
        ),
        "authority_root": i2_member_weight_authority()["root"],
        "longitudinal_axis_counted_elsewhere": True,
        "helicity_axis_collapsed_by_exact_delta": True,
        "color_axis_collapsed_by_Casimir_or_triplet_product": True,
        "physical_coefficient_selected": False,
        "complete_product_normalization": False,
    }
    return dict(payload, root=content_root(payload))


def _spatial_c47_unit_csr(resolution: str) -> csr_matrix:
    raw = weighted_spatial_kernel_csr(resolution, source_i2_unit_weights(resolution))
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    return raw[permutation, :][:, permutation].tocsr()


def _apply_spatial_c47_unit(resolution: str, vectors: np.ndarray) -> np.ndarray:
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    values = np.asarray(vectors, dtype=np.complex128)
    if values.ndim == 1:
        values = values[:, None]
    if values.shape[0] != len(permutation):
        raise ValueError("spatial vector leading dimension mismatch")
    source = np.empty_like(values)
    source[permutation, :] = values
    result_source = np.zeros_like(source)
    for mode in external_modes(resolution):
        result_source += single_member_kernel_dense(resolution, mode) @ source
    return result_source[permutation, :]


def source_weighted_jqjq_qg_csr(resolution: str) -> csr_matrix:
    return jqjq_qg_conditioned_csr(resolution, source_i2_unit_weights(resolution))


def apply_source_weighted_jqjq_qg(resolution: str, vector: np.ndarray) -> np.ndarray:
    return apply_jqjq_qg_conditioned(resolution, source_i2_unit_weights(resolution), vector)


def source_weighted_mixed_qg_csr(resolution: str, product: str) -> csr_matrix:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    longitudinal = mixed_partition_kernel_csr(resolution, product)
    spatial = _spatial_c47_unit_csr(resolution)
    spin = csr_matrix(combined_spin_selection_matrix())
    color = csr_matrix(triplet_color_product_matrix(product))
    return kron(
        kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"),
        color,
        format="csr",
    )


def apply_source_weighted_mixed_qg(
    resolution: str,
    product: str,
    vector: np.ndarray,
) -> np.ndarray:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    axis = qg_factorized_axis_record(resolution)
    pcount = int(axis["partition_count"])
    mcount = int(axis["transverse_mode_count"])
    dimension = int(axis["dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (dimension,):
        raise ValueError("vector must have shape ({},)".format(dimension))
    tensor = values.reshape(pcount, mcount, 4, 3)
    color = triplet_color_product_matrix(product)
    spin = combined_spin_selection_matrix()
    work = np.einsum("ab,pmsb->pmsa", color, tensor, optimize=True)
    work = np.einsum("ab,pmbc->pmac", spin, work, optimize=True)
    spatial = np.empty_like(work)
    for partition in range(pcount):
        batch = work[partition].reshape(mcount, 12)
        spatial[partition] = _apply_spatial_c47_unit(resolution, batch).reshape(mcount, 4, 3)
    result = np.empty_like(spatial)
    for mode_index in range(mcount):
        for spin_index in range(4):
            for color_index in range(3):
                result[:, mode_index, spin_index, color_index] = apply_mixed_partition_kernel(
                    resolution,
                    product,
                    spatial[:, mode_index, spin_index, color_index],
                )
    return result.reshape(dimension)


def source_weighted_mixed_direct_sum_csr(resolution: str, product: str) -> csr_matrix:
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    q_zero = csr_matrix((qdim, qdim), dtype=np.complex128)
    return block_diag((q_zero, source_weighted_mixed_qg_csr(resolution, product)), format="csr")


def apply_source_weighted_mixed_direct_sum(
    resolution: str,
    product: str,
    vector: np.ndarray,
) -> np.ndarray:
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    total = int(axis["direct_sum_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (total,):
        raise ValueError("vector must have shape ({},)".format(total))
    result = np.zeros_like(values)
    result[qdim:] = apply_source_weighted_mixed_qg(resolution, product, values[qdim:])
    return result


def source_weighted_mixed_linear_operator(resolution: str, product: str) -> LinearOperator:
    if product not in MIXED_PRODUCTS:
        raise KeyError(product)
    partner = "J_gJ_q" if product == "J_qJ_g" else "J_qJ_g"
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    return LinearOperator(
        (dimension, dimension),
        matvec=lambda vector: apply_source_weighted_mixed_direct_sum(
            resolution, product, vector
        ),
        rmatvec=lambda vector: apply_source_weighted_mixed_direct_sum(
            resolution, partner, vector
        ),
        dtype=np.complex128,
    )


def i2_source_weight_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(40801)
    rows = []
    maximum = 0.0
    maximum_adjoint = 0.0
    minimum_spatial = float("inf")
    for resolution in ("K9", "K11", "K13"):
        weight_record = source_i2_unit_weight_record(resolution)
        jq = source_weighted_jqjq_qg_csr(resolution)
        jq_vector = rng.normal(size=jq.shape[0]) + 1j * rng.normal(size=jq.shape[0])
        jq_residual = float(
            np.linalg.norm(jq @ jq_vector - apply_source_weighted_jqjq_qg(resolution, jq_vector))
        )
        maximum = max(maximum, jq_residual)
        spatial = _spatial_c47_unit_csr(resolution).toarray()
        local_minimum = float(np.min(np.linalg.eigvalsh(spatial)))
        minimum_spatial = min(minimum_spatial, local_minimum)
        mixed_records = []
        matrices = {}
        for product in MIXED_PRODUCTS:
            matrix = source_weighted_mixed_direct_sum_csr(resolution, product)
            vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
            residual = float(
                np.linalg.norm(
                    matrix @ vector
                    - apply_source_weighted_mixed_direct_sum(resolution, product, vector)
                )
            )
            maximum = max(maximum, residual)
            matrices[product] = matrix
            mixed_records.append(
                {
                    "product": product,
                    "shape": matrix.shape,
                    "nonzero_entries": int(matrix.nnz),
                    "sparse_matrix_free_residual": residual,
                }
            )
        adjoint = float(
            np.linalg.norm(
                (matrices["J_qJ_g"].getH() - matrices["J_gJ_q"]).data
            )
        )
        maximum_adjoint = max(maximum_adjoint, adjoint)
        rows.append(
            {
                "resolution": resolution,
                "unit_member_count": weight_record["member_count"],
                "J_qJ_q_qg_shape": jq.shape,
                "J_qJ_q_qg_nonzero_entries": int(jq.nnz),
                "J_qJ_q_qg_sparse_matrix_free_residual": jq_residual,
                "unit_weighted_spatial_minimum_eigenvalue_GeV2": local_minimum,
                "mixed": tuple(mixed_records),
                "mixed_source_order_adjoint_residual": adjoint,
            }
        )
    payload = {
        "schema": "C408-C117-I2-SOURCE-DESCENDANT-WEIGHT-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_member_counts": {"K9": 28, "K11": 45, "K13": 66},
        "maximum_sparse_matrix_free_residual": maximum,
        "maximum_mixed_source_order_adjoint_residual": maximum_adjoint,
        "minimum_unit_weighted_spatial_eigenvalue_GeV2": minimum_spatial,
        "pass": bool(maximum < 5e-10 and maximum_adjoint < 5e-10 and minimum_spatial >= -1e-12),
        "classification": "SOURCE_DESCENDANT_MEMBER_WEIGHT_CLOSED_COMMON_PRODUCT_NORMALIZATION_FACTORED",
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "MIXED_PRODUCTS",
    "source_i2_unit_weights",
    "source_i2_unit_weight_record",
    "source_weighted_jqjq_qg_csr",
    "apply_source_weighted_jqjq_qg",
    "source_weighted_mixed_qg_csr",
    "apply_source_weighted_mixed_qg",
    "source_weighted_mixed_direct_sum_csr",
    "apply_source_weighted_mixed_direct_sum",
    "source_weighted_mixed_linear_operator",
    "i2_source_weight_validation",
]
