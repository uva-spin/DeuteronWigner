"""C408 source-routed J_qJ_q direct-sum product-block primitive."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import block_diag, csr_matrix
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.embedding import (
    direct_sum_axis_record,
)

from .authority import STATUS
from .i4_q import apply_q_sector_jqjq, q_sector_i4_validation, q_sector_jqjq_csr
from .weights import (
    apply_source_weighted_jqjq_qg,
    i2_source_weight_validation,
    source_weighted_jqjq_qg_csr,
)


@lru_cache(maxsize=None)
def source_routed_jqjq_direct_sum_csr(resolution: str) -> csr_matrix:
    return block_diag(
        (q_sector_jqjq_csr(resolution), source_weighted_jqjq_qg_csr(resolution)),
        format="csr",
    )


def apply_source_routed_jqjq_direct_sum(resolution: str, vector: np.ndarray) -> np.ndarray:
    axis = direct_sum_axis_record(resolution)
    qdim = int(axis["q_dimension"])
    total = int(axis["direct_sum_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (total,):
        raise ValueError("vector must have shape ({},)".format(total))
    result = np.zeros_like(values)
    result[:qdim] = apply_q_sector_jqjq(resolution, values[:qdim])
    result[qdim:] = apply_source_weighted_jqjq_qg(resolution, values[qdim:])
    return result


def source_routed_jqjq_linear_operator(resolution: str) -> LinearOperator:
    dimension = int(direct_sum_axis_record(resolution)["direct_sum_dimension"])
    return LinearOperator(
        (dimension, dimension),
        matvec=lambda vector: apply_source_routed_jqjq_direct_sum(resolution, vector),
        rmatvec=lambda vector: apply_source_routed_jqjq_direct_sum(resolution, vector),
        dtype=np.complex128,
    )


def jqjq_product_block_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(40803)
    rows = []
    maximum = 0.0
    for resolution in ("K9", "K11", "K13"):
        matrix = source_routed_jqjq_direct_sum_csr(resolution)
        vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
        residual = float(
            np.linalg.norm(matrix @ vector - apply_source_routed_jqjq_direct_sum(resolution, vector))
        )
        maximum = max(maximum, residual)
        rows.append(
            {
                "resolution": resolution,
                "shape": matrix.shape,
                "nonzero_entries": int(matrix.nnz),
                "sparse_matrix_free_residual": residual,
                "hermiticity_residual": float(np.linalg.norm((matrix - matrix.getH()).data)),
                "q_sector_ready": True,
                "qg_sector_ready": True,
            }
        )
    q_validation = q_sector_i4_validation()
    i2_validation = i2_source_weight_validation()
    payload = {
        "schema": "C408-JQJQ-SOURCE-ROUTED-DIRECT-SUM-PRODUCT-BLOCK-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "maximum_sparse_matrix_free_residual": maximum,
        "q_sector_validation_root": q_validation["root"],
        "i2_weight_validation_root": i2_validation["root"],
        "source_routed_J_qJ_q_product_block_paths": 3,
        "common_product_normalization_bound": False,
        "target_count_once_aggregation_bound": False,
        "g_s_squared_bound": False,
        "c_C117_1_bound": False,
        "classification": "SOURCE_ROUTED_JQJQ_PRODUCT_BLOCK_PRIMITIVE_NOT_COMPLETE_C117_ACTION",
        "pass": bool(maximum < 5e-10 and q_validation["pass"] and i2_validation["pass"]),
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "source_routed_jqjq_direct_sum_csr",
    "apply_source_routed_jqjq_direct_sum",
    "source_routed_jqjq_linear_operator",
    "jqjq_product_block_validation",
]
