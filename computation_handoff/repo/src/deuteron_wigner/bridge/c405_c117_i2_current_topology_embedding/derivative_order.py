"""C405 ordered-gluon-derivative candidate family.

C115/C119 identify the gluon current as

    -f^{abc} A_perp^b partial^+ A_perp^c,

with the derivative acting on the source-ordered ``c`` field.  The frozen
records do not identify that field with the incoming or outgoing external
gluon after product-specific normal ordering.  C405 therefore implements the
complete finite family of explicit BRA/KET assignments, with no default and no
promotion to a C117 operator.

The returned kernels contain only the dimensionless mode factor ``k_g``.  The
explicit ``pi/L`` scale, finite-cell normalization, source phase, product
multiplicity, coupling, and C117 coefficient remain factored and unavailable.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product as cartesian_product
from typing import Any, Mapping, Sequence, Tuple

import numpy as np
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    apply_partition_transfer,
    partition_axis,
    partition_transfer_matrix_exact,
)

from .topology import PRODUCTS, STATUS, product_structure

BRA = "BRA"
KET = "KET"
LEGS: Tuple[str, str] = (BRA, KET)


def _normalize_legs(product_name: str, derivative_legs: Sequence[str]) -> Tuple[str, ...]:
    structure = product_structure(product_name)
    legs = tuple(str(leg).upper() for leg in derivative_legs)
    if len(legs) != structure.gluon_current_count:
        raise ValueError(
            f"{product_name} requires exactly {structure.gluon_current_count} ordered gluon derivative legs"
        )
    if any(leg not in LEGS for leg in legs):
        raise ValueError("each derivative leg must be BRA or KET")
    return legs


def derivative_assignments(product_name: str) -> Tuple[Tuple[str, ...], ...]:
    count = product_structure(product_name).gluon_current_count
    return tuple(tuple(row) for row in cartesian_product(LEGS, repeat=count))


def adjoint_derivative_assignment(
    product_name: str, derivative_legs: Sequence[str]
) -> Tuple[str, Tuple[str, ...]]:
    legs = _normalize_legs(product_name, derivative_legs)
    partner = product_structure(product_name).adjoint_product
    flipped = tuple(KET if leg == BRA else BRA for leg in reversed(legs))
    _normalize_legs(partner, flipped)
    return partner, flipped


def ordered_partition_kernel_exact(
    resolution: str,
    product_name: str,
    derivative_legs: Sequence[str],
) -> Tuple[Tuple[Fraction, ...], ...]:
    """Return kappa(p',p) times explicit ordered gluon-mode factors."""
    if product_name not in PRODUCTS:
        raise KeyError(product_name)
    legs = _normalize_legs(product_name, derivative_legs)
    partitions = partition_axis(resolution)
    base = partition_transfer_matrix_exact(resolution)
    rows = []
    for bra, base_row in enumerate(base):
        values = []
        for ket, coefficient in enumerate(base_row):
            factor = coefficient
            for leg in legs:
                factor *= partitions[bra].k_g if leg == BRA else partitions[ket].k_g
            values.append(factor)
        rows.append(tuple(values))
    return tuple(rows)


def ordered_partition_kernel_dense(
    resolution: str,
    product_name: str,
    derivative_legs: Sequence[str],
) -> np.ndarray:
    return np.asarray(
        [
            [float(value) for value in row]
            for row in ordered_partition_kernel_exact(resolution, product_name, derivative_legs)
        ],
        dtype=np.float64,
    )


def ordered_partition_kernel_csr(
    resolution: str,
    product_name: str,
    derivative_legs: Sequence[str],
) -> csr_matrix:
    return csr_matrix(ordered_partition_kernel_dense(resolution, product_name, derivative_legs))


def apply_ordered_partition_kernel(
    resolution: str,
    product_name: str,
    derivative_legs: Sequence[str],
    vector: np.ndarray,
) -> np.ndarray:
    rows = ordered_partition_kernel_exact(resolution, product_name, derivative_legs)
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape != (len(rows),):
        raise ValueError(f"vector must have shape ({len(rows)},)")
    result = np.zeros_like(values)
    for bra, row in enumerate(rows):
        total = 0j
        for ket, coefficient in enumerate(row):
            total += float(coefficient) * values[ket]
        result[bra] = total
    return result


def assignment_record(
    resolution: str,
    product_name: str,
    derivative_legs: Sequence[str],
) -> Mapping[str, Any]:
    legs = _normalize_legs(product_name, derivative_legs)
    matrix = ordered_partition_kernel_dense(resolution, product_name, legs)
    partner, partner_legs = adjoint_derivative_assignment(product_name, legs)
    partner_matrix = ordered_partition_kernel_dense(resolution, partner, partner_legs)
    payload = {
        "schema": "C405-C117-I2-ORDERED-GLUON-DERIVATIVE-ASSIGNMENT-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product_name,
        "derivative_legs_in_source_current_order": legs,
        "gluon_current_count": len(legs),
        "adjoint_product": partner,
        "adjoint_derivative_legs": partner_legs,
        "shape": matrix.shape,
        "nonzero_entries": int(np.count_nonzero(matrix)),
        "zero_mode_diagonal_exact": bool(np.array_equal(np.diag(matrix), np.zeros(len(matrix)))),
        "adjoint_residual": float(np.linalg.norm(matrix.conj().T - partner_matrix)),
        "dimensionless_factor": "kappa(p_out,p_in) times product of explicitly selected k_g legs",
        "factored_scale": "(pi/L) once per gluon-current derivative",
        "source_ordered_c_field_mapped_to_external_leg": False,
        "normal_ordering_descendant_bound": False,
        "classification": "EXPLICIT_ORDERED_DERIVATIVE_CANDIDATE_NOT_OPERATOR_BINDING",
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def ordered_derivative_inventory() -> Mapping[str, Any]:
    rows = []
    maximum_adjoint_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        for product_name in PRODUCTS:
            for legs in derivative_assignments(product_name):
                record = assignment_record(resolution, product_name, legs)
                rows.append(record)
                maximum_adjoint_residual = max(
                    maximum_adjoint_residual, float(record["adjoint_residual"])
                )
    payload = {
        "schema": "C405-C117-I2-ORDERED-GLUON-DERIVATIVE-INVENTORY-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_rows": 27,
        "assignments_per_resolution": 9,
        "maximum_adjoint_residual": maximum_adjoint_residual,
        "all_zero_mode_diagonals_exact": all(row["zero_mode_diagonal_exact"] for row in rows),
        "no_default_derivative_leg": True,
        "source_ordered_c_field_mapped_to_external_leg": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def apply_unqualified_gluon_derivative(*_args: Any, **_kwargs: Any) -> np.ndarray:
    raise RuntimeError(
        "C405 has no default ordered gluon derivative leg; bind a source-qualified normal-ordering descendant"
    )


__all__ = [
    "BRA",
    "KET",
    "LEGS",
    "derivative_assignments",
    "adjoint_derivative_assignment",
    "ordered_partition_kernel_exact",
    "ordered_partition_kernel_dense",
    "ordered_partition_kernel_csr",
    "apply_ordered_partition_kernel",
    "assignment_record",
    "ordered_derivative_inventory",
    "apply_unqualified_gluon_derivative",
]
