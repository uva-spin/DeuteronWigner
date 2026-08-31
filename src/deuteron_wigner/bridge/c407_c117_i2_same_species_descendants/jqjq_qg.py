"""Caller-conditioned C407 ``J_q J_q`` qg-sector composition interface.

C407 closes the same-species longitudinal contraction.  C403 supplies the
individual spatial member kernels for the C117 ``I2_density_projector`` graph,
but the source chain still represents the graph-member coefficients as
explicit weights ``w_r``.  This module therefore requires a complete,
caller-supplied weight mapping.  It has no unit-weight or minimum-norm default.

For an explicit weight map the C47 qg factorized order is

    partition, intrinsic_HO, quark_helicity, gluon_helicity, triplet_color.

The source overall coefficient, graph-member weight authority, finite-cell /
field / state normalization, M2 conversion, target count-once aggregation,
``g_s^2`` and ``c_C117_1`` remain factored.  The result is a numerical
composition interface and diagnostic stress test, not an operator binding.
"""
from __future__ import annotations

from fractions import Fraction
from math import isfinite
from functools import lru_cache
from typing import Any, Mapping, Sequence, Union

import numpy as np
from scipy.sparse import csr_matrix, diags, eye, kron
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    external_modes,
    single_member_kernel_dense,
    weighted_spatial_kernel_csr,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    c47_to_c403_mode_permutation,
    partition_axis,
    qg_factorized_axis_record,
)

from .authority import STATUS
from .descendants import longitudinal_diagonal_exact

SpatialWeightKey = Union[HOMode, Sequence[int]]
SpatialWeights = Mapping[SpatialWeightKey, float]


def _canonical_mode(value: SpatialWeightKey) -> HOMode:
    if isinstance(value, HOMode):
        return value
    if isinstance(value, (str, bytes)) or len(value) != 2:
        raise ValueError("spatial weight key must be HOMode or exact (n,m)")
    return HOMode(value[0], value[1])


def canonical_spatial_weights(
    resolution: str,
    weights: SpatialWeights | None,
) -> tuple[tuple[HOMode, float], ...]:
    """Validate and canonicalize an explicit complete C403 member-weight map."""
    if weights is None or len(weights) == 0:
        raise ValueError(
            "explicit nonempty C117 graph-member weights are required; "
            "C407 has no unit-weight or minimum-norm default"
        )
    admitted = set(external_modes(resolution))
    canonical: dict[HOMode, float] = {}
    for key, raw in weights.items():
        mode = _canonical_mode(key)
        if mode not in admitted:
            raise ValueError(f"spatial weight mode {mode} is outside the admitted C403 axis")
        if mode in canonical:
            raise ValueError(f"duplicate canonical spatial weight mode: {mode}")
        value = float(raw)
        if not isfinite(value):
            raise ValueError("spatial weights must be finite real numbers")
        canonical[mode] = value
    missing = tuple(sorted(admitted - set(canonical)))
    if missing:
        raise ValueError(
            "complete explicit C117 graph-member weights are required; "
            f"missing {len(missing)} admitted modes"
        )
    return tuple(sorted(canonical.items()))


def diagnostic_spatial_weight_fixture(resolution: str) -> Mapping[HOMode, float]:
    """Deterministic nonphysical fixture used only for composition validation."""
    modes = external_modes(resolution)
    count = len(modes)
    return {
        mode: float(Fraction(index + 1, count + 1))
        for index, mode in enumerate(modes)
    }


def _weight_mapping(rows: tuple[tuple[HOMode, float], ...]) -> dict[HOMode, float]:
    return {mode: value for mode, value in rows}


@lru_cache(maxsize=None)
def _spatial_c47_order_cached(
    resolution: str,
    rows: tuple[tuple[HOMode, float], ...],
) -> csr_matrix:
    raw = weighted_spatial_kernel_csr(resolution, _weight_mapping(rows))
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    return raw[permutation, :][:, permutation].tocsr()


def _spatial_c47_order(
    resolution: str,
    weights: SpatialWeights | None,
) -> csr_matrix:
    return _spatial_c47_order_cached(resolution, canonical_spatial_weights(resolution, weights))


def _apply_spatial_c47_order_batch(
    resolution: str,
    rows: tuple[tuple[HOMode, float], ...],
    vectors: np.ndarray,
) -> np.ndarray:
    """Independent batched member-kernel action in C47 ordering."""
    permutation = np.asarray(c47_to_c403_mode_permutation(resolution), dtype=np.int64)
    values = np.asarray(vectors, dtype=np.complex128)
    if values.ndim == 1:
        values = values[:, None]
    if values.shape[0] != len(permutation):
        raise ValueError(f"spatial vectors must have leading dimension {len(permutation)}")
    source_order = np.empty_like(values)
    source_order[permutation, :] = values
    result_source = np.zeros_like(source_order)
    for mode, weight in rows:
        # This route sums independently materialized single-member kernels; it
        # does not call the weighted sparse aggregate under test.
        result_source += weight * (single_member_kernel_dense(resolution, mode) @ source_order)
    return result_source[permutation, :]


def _apply_spatial_c47_order(
    resolution: str,
    weights: SpatialWeights | None,
    vector: np.ndarray,
) -> np.ndarray:
    rows = canonical_spatial_weights(resolution, weights)
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1:
        raise ValueError("spatial vector must be one-dimensional")
    return _apply_spatial_c47_order_batch(resolution, rows, values)[:, 0]


@lru_cache(maxsize=None)
def _jqjq_qg_conditioned_csr_cached(
    resolution: str,
    rows: tuple[tuple[HOMode, float], ...],
) -> csr_matrix:
    axis = qg_factorized_axis_record(resolution)
    partition_weights = np.asarray(
        [float(value) for value in longitudinal_diagonal_exact(resolution, "QUARK", "qg->qg")],
        dtype=np.float64,
    )
    if len(partition_weights) != axis["partition_count"]:
        raise RuntimeError("partition-weight axis mismatch")
    longitudinal = diags(partition_weights, offsets=0, format="csr")
    spatial = _spatial_c47_order_cached(resolution, rows)
    spin = eye(4, dtype=np.complex128, format="csr")
    color = eye(3, dtype=np.complex128, format="csr")
    result = kron(
        kron(kron(longitudinal, spatial, format="csr"), spin, format="csr"),
        color,
        format="csr",
    )
    if result.shape != (axis["dimension"], axis["dimension"]):
        raise RuntimeError("C407 qg conditioned composition dimension mismatch")
    return result.tocsr()


def jqjq_qg_conditioned_csr(
    resolution: str,
    spatial_weights: SpatialWeights | None,
) -> csr_matrix:
    return _jqjq_qg_conditioned_csr_cached(
        resolution,
        canonical_spatial_weights(resolution, spatial_weights),
    )


def apply_jqjq_qg_conditioned(
    resolution: str,
    spatial_weights: SpatialWeights | None,
    vector: np.ndarray,
) -> np.ndarray:
    axis = qg_factorized_axis_record(resolution)
    # Validate once at the public boundary, then the independent spatial route
    # validates again rather than reusing a sparse matrix.
    canonical_spatial_weights(resolution, spatial_weights)
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (axis["dimension"],):
        raise ValueError(f"vector must have shape ({axis['dimension']},)")
    pcount = axis["partition_count"]
    mcount = axis["transverse_mode_count"]
    tensor = values.reshape(pcount, mcount, 4, 3)
    result = np.zeros_like(tensor)
    longitudinal = longitudinal_diagonal_exact(resolution, "QUARK", "qg->qg")
    rows = canonical_spatial_weights(resolution, spatial_weights)
    for partition in range(pcount):
        factor = float(longitudinal[partition])
        batch = tensor[partition].reshape(mcount, 12)
        result[partition] = (
            factor * _apply_spatial_c47_order_batch(resolution, rows, batch)
        ).reshape(mcount, 4, 3)
    return result.reshape(-1)


def jqjq_qg_conditioned_linear_operator(
    resolution: str,
    spatial_weights: SpatialWeights | None,
) -> LinearOperator:
    canonical_spatial_weights(resolution, spatial_weights)
    dimension = int(qg_factorized_axis_record(resolution)["dimension"])
    return LinearOperator(
        (dimension, dimension),
        matvec=lambda vector: apply_jqjq_qg_conditioned(resolution, spatial_weights, vector),
        rmatvec=lambda vector: apply_jqjq_qg_conditioned(resolution, spatial_weights, vector),
        dtype=np.complex128,
    )


def apply_jqjq_q_sector_primitive(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C407 does not substitute the C403 I2 kernel for the source-owned J_qJ_q q-sector "
        "I4-local transverse kernel; that q-sector action remains unavailable, not zero"
    )


def apply_jgjg_qg_primitive(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C407 closes the J_gJ_g longitudinal one-body descendant only; the C117 derivative-density "
        "transverse descendant and derivative-count reconciliation remain unavailable"
    )


def jqjq_qg_conditioned_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(40701)
    rows = []
    maximum_residual = 0.0
    minimum_eigenvalue = float("inf")
    for resolution in ("K9", "K11", "K13"):
        fixture = diagnostic_spatial_weight_fixture(resolution)
        matrix = jqjq_qg_conditioned_csr(resolution, fixture)
        vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
        independent = apply_jqjq_qg_conditioned(resolution, fixture, vector)
        residual = float(np.linalg.norm(matrix @ vector - independent))
        maximum_residual = max(maximum_residual, residual)
        spatial = _spatial_c47_order(resolution, fixture).toarray()
        spatial_min = float(np.min(np.linalg.eigvalsh(spatial)))
        minimum_eigenvalue = min(minimum_eigenvalue, spatial_min)
        rows.append(
            {
                "resolution": resolution,
                "dimension": matrix.shape[0],
                "nonzero_entries": int(matrix.nnz),
                "partition_count": len(partition_axis(resolution)),
                "spatial_dimension": spatial.shape[0],
                "explicit_fixture_weight_count": len(fixture),
                "fixture_classification": "DETERMINISTIC_NONPHYSICAL_COMPOSITION_TEST_WEIGHTS",
                "spatial_minimum_eigenvalue_GeV2": spatial_min,
                "sparse_matrix_free_residual": residual,
                "hermiticity_residual": float(np.linalg.norm((matrix - matrix.getH()).data)),
                "units": "GeV^2 times factored common C114/C119 normalization and caller weights",
            }
        )
    payload = {
        "schema": "C407-C117-I2-JQJQ-QG-CALLER-CONDITIONED-COMPOSITION-VALIDATION-V2",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "maximum_sparse_matrix_free_residual": maximum_residual,
        "minimum_spatial_eigenvalue_GeV2": minimum_eigenvalue,
        "all_hermitian": all(row["hermiticity_residual"] < 1e-12 for row in rows),
        "positive_semidefinite_at_tolerance_for_nonnegative_fixture": minimum_eigenvalue >= -1e-12,
        "pass": bool(
            maximum_residual < 2e-10
            and minimum_eigenvalue >= -1e-12
            and all(row["hermiticity_residual"] < 1e-12 for row in rows)
        ),
        "classification": "CALLER_CONDITIONED_JQJQ_QG_COMPOSITION_STRESS_TEST_NOT_OPERATOR_BINDING",
        "source_authorized_graph_member_weights": False,
        "unit_weight_default": False,
        "minimum_norm_default": False,
        "complete_product_normalization": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "SpatialWeights",
    "canonical_spatial_weights",
    "diagnostic_spatial_weight_fixture",
    "jqjq_qg_conditioned_csr",
    "apply_jqjq_qg_conditioned",
    "jqjq_qg_conditioned_linear_operator",
    "apply_jqjq_q_sector_primitive",
    "apply_jgjg_qg_primitive",
    "jqjq_qg_conditioned_validation",
]
