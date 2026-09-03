"""C408 source-routed J_q J_q q-sector I4-local transverse primitive.

C116/C126 assign ``J_qJ_q:q->q`` to the exact ``I4_local`` route.  The q-sector
external C123/C128 basis uses the transverse ground mode and has dimension six
(two quark helicities times three colors).  The same-species contraction sums
over the complete finite C45 transverse intermediate shell.  C408 evaluates
each four-HO member analytically and by an independent generalized
Gauss--Laguerre route.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial, isfinite, pi
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import LinearOperator
from scipy.special import eval_genlaguerre, roots_genlaguerre

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    content_root,
    resolution_record,
)
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    radial_moment_fraction,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.descendants import (
    longitudinal_diagonal_exact,
)
from deuteron_wigner.bridge.modes import core as c45

from .authority import STATUS, routing_authority_record


def _source_resolution(resolution: str) -> c45.Resolution:
    full = resolution_record(resolution)["full_resolution_id"]
    for source in c45.RESOLUTIONS:
        if source.label == full:
            return source
    raise KeyError(resolution)


@lru_cache(maxsize=None)
def q_i4_intermediate_modes(resolution: str) -> tuple[HOMode, ...]:
    source = _source_resolution(resolution)
    return tuple(HOMode(n, m) for n, m in c45.ho_labels(source.Nmax))


def _source_b(resolution: str) -> float:
    value = float(resolution_record(resolution)["b_HO"])
    if not isfinite(value) or value <= 0:
        raise ValueError("b_HO must be finite and positive")
    return value


@lru_cache(maxsize=None)
def q_i4_member_coefficient_exact(resolution: str, n: int, m: int) -> Fraction:
    mode = HOMode(n, m)
    if mode not in set(q_i4_intermediate_modes(resolution)):
        raise KeyError(mode)
    radial = radial_moment_fraction(0, 0, 0, mode.n, abs(mode.m))
    normalization = Fraction(factorial(mode.n), factorial(mode.n + abs(mode.m)))
    return normalization * radial


def q_i4_member_value(resolution: str, mode: HOMode) -> float:
    coefficient = q_i4_member_coefficient_exact(resolution, mode.n, mode.m)
    return (_source_b(resolution) ** 2 / pi) * float(coefficient)


def q_i4_member_quadrature(resolution: str, mode: HOMode, nodes: int = 96) -> float:
    if nodes <= 0:
        raise ValueError("nodes must be positive")
    if mode not in set(q_i4_intermediate_modes(resolution)):
        raise KeyError(mode)
    alpha = abs(mode.m)
    points, weights = roots_genlaguerre(nodes, alpha)
    z = points / 2.0
    polynomial = eval_genlaguerre(mode.n, alpha, z) ** 2
    radial = float(np.sum(weights * polynomial) / (2.0 ** (alpha + 1)))
    normalization = factorial(mode.n) / factorial(mode.n + alpha)
    return (_source_b(resolution) ** 2 / pi) * normalization * radial


@lru_cache(maxsize=None)
def q_i4_spatial_sum(resolution: str) -> float:
    return float(sum(q_i4_member_value(resolution, mode) for mode in q_i4_intermediate_modes(resolution)))


@lru_cache(maxsize=None)
def q_sector_jqjq_scalar(resolution: str) -> float:
    longitudinal = longitudinal_diagonal_exact(resolution, "QUARK", "q->q")
    if len(longitudinal) != 1:
        raise RuntimeError("q-sector longitudinal axis must contain one external mode")
    return float(longitudinal[0]) * q_i4_spatial_sum(resolution)


def q_sector_jqjq_csr(resolution: str) -> csr_matrix:
    qdim = int(resolution_record(resolution)["q_dimension"])
    return q_sector_jqjq_scalar(resolution) * eye(qdim, dtype=np.complex128, format="csr")


def apply_q_sector_jqjq(resolution: str, vector: np.ndarray) -> np.ndarray:
    qdim = int(resolution_record(resolution)["q_dimension"])
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (qdim,):
        raise ValueError("vector must have shape ({},)".format(qdim))
    return q_sector_jqjq_scalar(resolution) * values


def q_sector_jqjq_linear_operator(resolution: str) -> LinearOperator:
    qdim = int(resolution_record(resolution)["q_dimension"])
    return LinearOperator(
        (qdim, qdim),
        matvec=lambda vector: apply_q_sector_jqjq(resolution, vector),
        rmatvec=lambda vector: apply_q_sector_jqjq(resolution, vector),
        dtype=np.complex128,
    )


def q_sector_i4_inventory() -> Mapping[str, Any]:
    rows = []
    summaries = []
    maximum_quadrature = 0.0
    for resolution in ("K9", "K11", "K13"):
        local = []
        for mode in q_i4_intermediate_modes(resolution):
            exact = q_i4_member_coefficient_exact(resolution, mode.n, mode.m)
            value = q_i4_member_value(resolution, mode)
            quadrature = q_i4_member_quadrature(resolution, mode)
            residual = abs(value - quadrature)
            maximum_quadrature = max(maximum_quadrature, residual)
            record = {
                "resolution": resolution,
                "mode": mode.to_record(),
                "coefficient_of_bHO2_over_pi": {
                    "numerator": exact.numerator,
                    "denominator": exact.denominator,
                    "exact": str(exact),
                },
                "value_GeV2": value,
                "quadrature_GeV2": quadrature,
                "quadrature_abs_residual_GeV2": residual,
                "positive": value > 0,
            }
            rows.append(record)
            local.append(record)
        summaries.append(
            {
                "resolution": resolution,
                "mode_count": len(local),
                "spatial_sum_GeV2": q_i4_spatial_sum(resolution),
                "longitudinal_factor": float(
                    longitudinal_diagonal_exact(resolution, "QUARK", "q->q")[0]
                ),
                "q_sector_product_scalar_GeV2": q_sector_jqjq_scalar(resolution),
                "all_positive": all(row["positive"] for row in local),
            }
        )
    payload = {
        "schema": "C408-JQJQ-Q-SECTOR-I4-LOCAL-INVENTORY-V1",
        "status": STATUS,
        "routing_authority_root": routing_authority_record()["root"],
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_mode_counts": {"K9": 36, "K11": 55, "K13": 78},
        "summaries": tuple(summaries),
        "maximum_analytic_quadrature_abs_residual_GeV2": maximum_quadrature,
        "external_q_basis": "C123/C128 transverse ground; 2 helicities times 3 colors",
        "intermediate_transverse_axis": "complete finite C45 one-particle HO shell",
        "unit_contraction_multiplicity": True,
        "common_product_normalization_factored": True,
        "complete_C117_action": False,
        "pass": bool(maximum_quadrature < 5e-13 and all(row["positive"] for row in rows)),
    }
    return dict(payload, root=content_root(payload))


def q_sector_i4_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(40802)
    rows = []
    maximum = 0.0
    for resolution in ("K9", "K11", "K13"):
        matrix = q_sector_jqjq_csr(resolution)
        vector = rng.normal(size=matrix.shape[0]) + 1j * rng.normal(size=matrix.shape[0])
        residual = float(np.linalg.norm(matrix @ vector - apply_q_sector_jqjq(resolution, vector)))
        maximum = max(maximum, residual)
        rows.append(
            {
                "resolution": resolution,
                "shape": matrix.shape,
                "nonzero_entries": int(matrix.nnz),
                "scalar_GeV2": q_sector_jqjq_scalar(resolution),
                "sparse_matrix_free_residual": residual,
                "hermiticity_residual": float(np.linalg.norm((matrix - matrix.getH()).data)),
            }
        )
    inventory = q_sector_i4_inventory()
    payload = {
        "schema": "C408-JQJQ-Q-SECTOR-I4-LOCAL-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "maximum_sparse_matrix_free_residual": maximum,
        "inventory_root": inventory["root"],
        "pass": bool(maximum < 1e-14 and inventory["pass"]),
        "classification": "SOURCE_ROUTED_I4_LOCAL_Q_SECTOR_PRODUCT_BLOCK_PRIMITIVE_COMMON_NORMALIZATION_FACTORED",
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "q_i4_intermediate_modes",
    "q_i4_member_coefficient_exact",
    "q_i4_member_value",
    "q_i4_member_quadrature",
    "q_i4_spatial_sum",
    "q_sector_jqjq_scalar",
    "q_sector_jqjq_csr",
    "apply_q_sector_jqjq",
    "q_sector_jqjq_linear_operator",
    "q_sector_i4_inventory",
    "q_sector_i4_validation",
]
