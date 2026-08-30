"""C405 exact q plus qg direct-sum embedding mechanics.

C114 proves q<->qg instantaneous-current blocks vanish by even gluon-number
parity.  It does not prove that the q->q diagonal block of the first C117 I2
direction is zero.  C405 therefore provides an explicit two-block assembler:
both diagonal blocks must be supplied, while the cross-sector blocks are exact
zeros by source proof.  A qg primitive alone is represented as a partial block
and cannot be promoted to a complete direct-sum operator.
"""
from __future__ import annotations

from typing import Any, Mapping, Tuple

import numpy as np
from scipy.sparse import block_diag, csr_matrix, issparse
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    content_root,
    resolution_record,
)

from .topology import PRODUCTS, STATUS


def direct_sum_axis_record(resolution: str) -> Mapping[str, Any]:
    record = resolution_record(resolution)
    q_dimension = int(record["q_dimension"])
    qg_dimension = int(record["qg_dimension"])
    direct_dimension = int(record["direct_sum_dimension"])
    if q_dimension + qg_dimension != direct_dimension:
        raise ValueError("q plus qg dimensions do not close the direct-sum basis")
    payload = {
        "schema": "C405-C117-I2-DIRECT-SUM-AXIS-V1",
        "status": STATUS,
        "resolution": record["resolution_label"],
        "full_resolution_id": record["full_resolution_id"],
        "q_dimension": q_dimension,
        "qg_dimension": qg_dimension,
        "direct_sum_dimension": direct_dimension,
        "q_slice": (0, q_dimension),
        "qg_slice": (q_dimension, direct_dimension),
        "basis_order": "C128/C112 q sector followed by C47 qg sector",
        "cross_sector_blocks": "EXACT_ZERO_BY_C114_EVEN_GLUON_NUMBER_PARITY",
        "q_diagonal_block_status": "UNAVAILABLE_NOT_ZERO_FOR_C117_I2",
        "qg_diagonal_block_status": "CONDITIONAL_PRIMITIVES_AVAILABLE_NOT_COMPLETE",
    }
    return {**payload, "root": content_root(payload)}


def _as_csr_finite(matrix: Any, shape: Tuple[int, int], name: str) -> csr_matrix:
    value = matrix.tocsr() if issparse(matrix) else csr_matrix(np.asarray(matrix))
    if value.shape != shape:
        raise ValueError(f"{name} must have shape {shape}")
    if value.data.size and not np.all(np.isfinite(value.data)):
        raise ValueError(f"{name} contains nonfinite entries")
    return value.astype(np.complex128)


def assemble_explicit_direct_sum_csr(
    resolution: str,
    *,
    q_block: Any,
    qg_block: Any,
) -> csr_matrix:
    axis = direct_sum_axis_record(resolution)
    q_dimension = int(axis["q_dimension"])
    qg_dimension = int(axis["qg_dimension"])
    q = _as_csr_finite(q_block, (q_dimension, q_dimension), "q_block")
    qg = _as_csr_finite(qg_block, (qg_dimension, qg_dimension), "qg_block")
    return block_diag((q, qg), format="csr")


def apply_explicit_direct_sum(
    resolution: str,
    *,
    q_block: Any,
    qg_block: Any,
    vector: np.ndarray,
) -> np.ndarray:
    axis = direct_sum_axis_record(resolution)
    q_dimension = int(axis["q_dimension"])
    qg_dimension = int(axis["qg_dimension"])
    direct_dimension = int(axis["direct_sum_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape != (direct_dimension,):
        raise ValueError(f"vector must have shape ({direct_dimension},)")
    q = _as_csr_finite(q_block, (q_dimension, q_dimension), "q_block")
    qg = _as_csr_finite(qg_block, (qg_dimension, qg_dimension), "qg_block")
    result = np.zeros_like(values)
    result[:q_dimension] = q @ values[:q_dimension]
    result[q_dimension:] = qg @ values[q_dimension:]
    return result


def explicit_direct_sum_linear_operator(
    resolution: str,
    *,
    q_block: Any,
    qg_block: Any,
) -> LinearOperator:
    matrix = assemble_explicit_direct_sum_csr(
        resolution, q_block=q_block, qg_block=qg_block
    )
    return LinearOperator(
        shape=matrix.shape,
        matvec=lambda vector: apply_explicit_direct_sum(
            resolution, q_block=q_block, qg_block=qg_block, vector=vector
        ),
        rmatvec=lambda vector: apply_explicit_direct_sum(
            resolution,
            q_block=matrix[: direct_sum_axis_record(resolution)["q_dimension"],
                           : direct_sum_axis_record(resolution)["q_dimension"]].getH(),
            qg_block=matrix[direct_sum_axis_record(resolution)["q_dimension"] :,
                            direct_sum_axis_record(resolution)["q_dimension"] :].getH(),
            vector=vector,
        ),
        dtype=np.complex128,
    )


def qg_partial_embedding_record(
    resolution: str,
    product: str,
) -> Mapping[str, Any]:
    if product not in PRODUCTS:
        raise KeyError(product)
    axis = direct_sum_axis_record(resolution)
    payload = {
        "schema": "C405-C117-I2-QG-PARTIAL-DIRECT-SUM-EMBEDDING-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product,
        "axis": axis,
        "available_diagonal_block": "qg->qg conditional primitive",
        "missing_diagonal_block": "q->q product-specific normal-ordering/contraction action",
        "q_to_qg_block": "EXACT_ZERO_WITH_C114_OPERATOR_PROOF",
        "qg_to_q_block": "EXACT_ZERO_WITH_C114_OPERATOR_PROOF",
        "zero_fill_missing_q_block": False,
        "complete_direct_sum_operator": False,
        "classification": "PARTIAL_BLOCK_EMBEDDING_MAP_NOT_COMPLETE_OPERATOR",
    }
    return {**payload, "root": content_root(payload)}


def exact_cross_sector_zero_certificate(resolution: str) -> Mapping[str, Any]:
    axis = direct_sum_axis_record(resolution)
    rows = tuple(
        {
            "product": product,
            "q_to_qg_shape": (axis["qg_dimension"], axis["q_dimension"]),
            "qg_to_q_shape": (axis["q_dimension"], axis["qg_dimension"]),
            "proof": "C114 even-gluon-number parity",
            "status": "EXACT_ZERO_WITH_OPERATOR_PROOF",
        }
        for product in PRODUCTS
    )
    payload = {
        "schema": "C405-C117-I2-CROSS-SECTOR-ZERO-CERTIFICATE-V1",
        "status": STATUS,
        "resolution": resolution,
        "rows": rows,
        "cross_sector_zero_blocks": len(rows) * 2,
        "q_diagonal_block_inferred_zero": False,
    }
    return {**payload, "root": content_root(payload)}


def direct_sum_embedding_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(4051)
    rows = []
    maximum_sparse_direct_residual = 0.0
    maximum_cross_block_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        axis = direct_sum_axis_record(resolution)
        q_dimension = int(axis["q_dimension"])
        qg_dimension = int(axis["qg_dimension"])
        q = csr_matrix(np.diag(np.arange(1, q_dimension + 1, dtype=np.float64)))
        qg_diag = np.linspace(0.5, 1.5, qg_dimension, dtype=np.float64)
        qg = csr_matrix((qg_diag, (np.arange(qg_dimension), np.arange(qg_dimension))), shape=(qg_dimension, qg_dimension))
        matrix = assemble_explicit_direct_sum_csr(
            resolution, q_block=q, qg_block=qg
        )
        vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
        direct = apply_explicit_direct_sum(
            resolution, q_block=q, qg_block=qg, vector=vector
        )
        residual = float(np.linalg.norm(matrix @ vector - direct))
        cross = max(
            float(np.linalg.norm(matrix[:q_dimension, q_dimension:].data)),
            float(np.linalg.norm(matrix[q_dimension:, :q_dimension].data)),
        )
        maximum_sparse_direct_residual = max(maximum_sparse_direct_residual, residual)
        maximum_cross_block_residual = max(maximum_cross_block_residual, cross)
        rows.append(
            {
                "resolution": resolution,
                "q_dimension": q_dimension,
                "qg_dimension": qg_dimension,
                "direct_sum_dimension": matrix.shape[0],
                "sparse_direct_residual": residual,
                "cross_sector_zero_residual": cross,
                "explicit_q_block_required": True,
            }
        )
    payload = {
        "schema": "C405-C117-I2-DIRECT-SUM-EMBEDDING-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "maximum_sparse_direct_residual": maximum_sparse_direct_residual,
        "maximum_cross_sector_zero_residual": maximum_cross_block_residual,
        "pass": bool(
            maximum_sparse_direct_residual == 0.0
            and maximum_cross_block_residual == 0.0
        ),
        "qg_only_promoted_to_complete_operator": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def assemble_with_missing_q_block(*_args: Any, **_kwargs: Any) -> csr_matrix:
    raise RuntimeError(
        "C405 cannot embed a qg primitive as a complete direct-sum action; the q->q diagonal block is unavailable, not zero"
    )


__all__ = [
    "direct_sum_axis_record",
    "assemble_explicit_direct_sum_csr",
    "apply_explicit_direct_sum",
    "explicit_direct_sum_linear_operator",
    "qg_partial_embedding_record",
    "exact_cross_sector_zero_certificate",
    "direct_sum_embedding_validation",
    "assemble_with_missing_q_block",
]
