"""Numerical C396 quark/gluon mass-squared directions for C401.

The two operators are derivatives of the source free invariant-mass formula
with respect to resolution-local mass-squared coordinates.  Their fractions
come from C45/C47, while dimensions and direct-sum partition blocks come from
C128/C112.  No physical mass or counterterm value is selected.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Any, Iterable, Mapping

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.free2 import core as c128

from .basis import (
    RESOLUTION_LABELS,
    basis_fraction_provenance,
    canonical_partitions,
    content_root,
    historical_c128_partition_defect_audit,
    normalize_resolution,
    partition_for_direct_index,
    resolution_record,
)

D_MU_Q_SQ = "D_mu_q_sq"
D_DELTA_MU_G_SQ = "D_delta_mu_g_sq"
DIRECTIONS = (D_MU_Q_SQ, D_DELTA_MU_G_SQ)


@dataclass(frozen=True)
class DirectionSpecification:
    direction_id: str
    raw_C396_coordinate: str
    implementation_coordinate: str
    source_formula: str
    q_sector_value: str
    qg_sector_value: str
    coefficient_units: str = "GeV^2"
    operator_units: str = "dimensionless"
    physical_value_selected: bool = False


_DIRECTION_SPECS = {
    D_MU_Q_SQ: DirectionSpecification(
        direction_id=D_MU_Q_SQ,
        raw_C396_coordinate="ct_mass",
        implementation_coordinate="mu_q_sq",
        source_formula="d M_free^2 / d mu_q^2",
        q_sector_value="1",
        qg_sector_value="1/x_q",
    ),
    D_DELTA_MU_G_SQ: DirectionSpecification(
        direction_id=D_DELTA_MU_G_SQ,
        raw_C396_coordinate="ct_gluon_mass",
        implementation_coordinate="delta_mu_g_sq",
        source_formula="d M_free^2 / d delta_mu_g^2",
        q_sector_value="0",
        qg_sector_value="1/x_g",
    ),
}


def _check_direction(direction: str) -> DirectionSpecification:
    try:
        return _DIRECTION_SPECS[direction]
    except KeyError as exc:
        raise KeyError(direction) from exc


def _array_hash(array: np.ndarray) -> str:
    value = np.ascontiguousarray(array)
    return sha256(value.dtype.str.encode() + str(value.shape).encode() + value.tobytes()).hexdigest()


def direction_specification(direction: str) -> dict[str, Any]:
    return _DIRECTION_SPECS[_check_direction(direction).direction_id].__dict__.copy()


def exact_block_records(resolution: str, direction: str) -> tuple[dict[str, Any], ...]:
    spec = _check_direction(direction)
    record = resolution_record(resolution)
    rows: list[dict[str, Any]] = []
    if direction == D_MU_Q_SQ:
        rows.append(
            {
                "sector": "q",
                "direct_start": 0,
                "direct_stop": record["q_dimension"],
                "state_count": record["q_dimension"],
                "exact_value": "1",
                "float_value": 1.0,
                "source": "C43 free quark bilinear projected in C128",
            }
        )
    else:
        rows.append(
            {
                "sector": "q",
                "direct_start": 0,
                "direct_stop": record["q_dimension"],
                "state_count": record["q_dimension"],
                "exact_value": "0",
                "float_value": 0.0,
                "source": "no gluon in the C128 one-quark sector",
            }
        )
    for partition in canonical_partitions(resolution):
        fraction = partition.xq if direction == D_MU_Q_SQ else partition.xg
        exact = 1 / fraction
        rows.append(
            {
                "sector": "qg",
                "partition_id": partition.partition_id,
                "direct_start": partition.qg_direct_start,
                "direct_stop": partition.qg_direct_stop,
                "state_count": partition.qg_state_count,
                "kq": str(partition.kq),
                "kg": str(partition.kg),
                "xq": str(partition.xq),
                "xg": str(partition.xg),
                "exact_value": str(exact),
                "float_value": float(exact),
                "source": spec.qg_sector_value,
            }
        )
    return tuple(rows)


def operator_diagonal(resolution: str, direction: str) -> np.ndarray:
    _check_direction(direction)
    record = resolution_record(resolution)
    diagonal = np.zeros(record["direct_sum_dimension"], dtype=np.float64)
    if direction == D_MU_Q_SQ:
        diagonal[: record["q_dimension"]] = 1.0
    for partition in canonical_partitions(resolution):
        fraction = partition.xq if direction == D_MU_Q_SQ else partition.xg
        diagonal[partition.qg_direct_start : partition.qg_direct_stop] = float(1 / fraction)
    diagonal.setflags(write=False)
    return diagonal


def sparse_coordinate_operator(resolution: str, direction: str) -> dict[str, Any]:
    spec = _check_direction(direction)
    record = resolution_record(resolution)
    diagonal = operator_diagonal(resolution, direction)
    rows = np.flatnonzero(diagonal).astype(np.int64)
    cols = rows.copy()
    data = diagonal[rows].copy()
    for value in (rows, cols, data):
        value.setflags(write=False)
    payload = {
        "schema": "C401-C396-MASS-DIRECTION-SPARSE-COO-V1",
        "resolution": record["resolution_label"],
        "full_resolution_id": record["full_resolution_id"],
        "direction": spec.direction_id,
        "raw_C396_coordinate": spec.raw_C396_coordinate,
        "implementation_coordinate": spec.implementation_coordinate,
        "shape": (record["direct_sum_dimension"], record["direct_sum_dimension"]),
        "rows": rows,
        "cols": cols,
        "data": data,
        "nnz": int(data.size),
        "basis_order": record["basis_order"],
        "operator_units": spec.operator_units,
        "coefficient_units": spec.coefficient_units,
        "Hermitian": True,
        "diagonal": True,
        "physical_value_selected": False,
        "source_packages": ("C43", "C45", "C47", "C128", "C136", "C396"),
        "fraction_root": basis_fraction_provenance(resolution)["root"],
        "array_hashes": {
            "rows": _array_hash(rows),
            "cols": _array_hash(cols),
            "data": _array_hash(data),
            "diagonal": _array_hash(diagonal),
        },
        "exact_blocks": exact_block_records(resolution, direction),
    }
    root_payload = {
        key: value
        for key, value in payload.items()
        if key not in {"rows", "cols", "data"}
    }
    return {**payload, "root": content_root(root_payload)}


def coordinate_operator_csr(resolution: str, direction: str) -> csr_matrix:
    """Return the K-local mass direction as an actual SciPy CSR matrix.

    Structurally exact zeros are omitted rather than stored.  This matters for
    the gluon-mass direction, whose one-quark block is exactly zero.
    """
    record = sparse_coordinate_operator(resolution, direction)
    rows = np.asarray(record["rows"], dtype=np.int64)
    data = np.asarray(record["data"], dtype=np.float64)
    matrix = csr_matrix(
        (data, (rows, rows)),
        shape=tuple(record["shape"]),
        dtype=np.float64,
    )
    matrix.sort_indices()
    return matrix


def coordinate_linear_operator(resolution: str, direction: str) -> LinearOperator:
    """Return the independent matrix-free action as a SciPy LinearOperator."""
    _check_direction(direction)
    record = resolution_record(resolution)
    shape = (record["direct_sum_dimension"], record["direct_sum_dimension"])

    def matvec(vector: np.ndarray) -> np.ndarray:
        return np.asarray(apply_mass_direction(resolution, direction, vector))

    return LinearOperator(shape=shape, matvec=matvec, rmatvec=matvec, dtype=np.complex128)


def apply_sparse_coordinate_operator(operator: Mapping[str, Any], vector: Any) -> np.ndarray:
    shape = tuple(operator["shape"])
    value = np.asarray(vector, dtype=np.complex128)
    if value.shape != (shape[1],):
        raise ValueError(f"vector shape {value.shape} incompatible with operator shape {shape}")
    output = np.zeros(shape[0], dtype=np.complex128)
    np.add.at(
        output,
        np.asarray(operator["rows"], dtype=np.int64),
        np.asarray(operator["data"], dtype=np.float64)
        * value[np.asarray(operator["cols"], dtype=np.int64)],
    )
    output.setflags(write=False)
    return output


def apply_mass_direction(resolution: str, direction: str, vector: Any) -> np.ndarray:
    """Independent matrix-free block action for one mass-squared direction."""
    _check_direction(direction)
    record = resolution_record(resolution)
    value = np.asarray(vector, dtype=np.complex128)
    if value.shape != (record["direct_sum_dimension"],):
        raise ValueError(
            f"vector shape {value.shape} incompatible with {record['direct_sum_dimension']}"
        )
    output = np.zeros_like(value)
    if direction == D_MU_Q_SQ:
        output[: record["q_dimension"]] = value[: record["q_dimension"]]
    for partition in canonical_partitions(resolution):
        fraction = partition.xq if direction == D_MU_Q_SQ else partition.xg
        output[partition.qg_direct_start : partition.qg_direct_stop] = (
            float(1 / fraction)
            * value[partition.qg_direct_start : partition.qg_direct_stop]
        )
    output.setflags(write=False)
    return output


def source_mass_component_action(
    resolution: str,
    vector: Any,
    *,
    mu_q_sq: float,
    delta_mu_g_sq: float,
) -> np.ndarray:
    """Independent source-formula action used for finite-difference holdouts.

    This is the mass-dependent part of the free C43/C47 invariant-mass
    functional on the C128 direct-sum basis.  It deliberately excludes the
    transverse kinetic term, which is parameter independent and cancels in the
    mass finite differences.  The values are diagnostic caller inputs, not
    selected physical masses.
    """
    if not np.isfinite(mu_q_sq) or not np.isfinite(delta_mu_g_sq):
        raise ValueError("finite diagnostic mass-squared values required")
    record = resolution_record(resolution)
    value = np.asarray(vector, dtype=np.complex128)
    if value.shape != (record["direct_sum_dimension"],):
        raise ValueError(
            f"vector shape {value.shape} incompatible with {record['direct_sum_dimension']}"
        )
    output = np.zeros_like(value)
    output[: record["q_dimension"]] = mu_q_sq * value[: record["q_dimension"]]

    # Independent holdout route: reconstruct the exact source partitions
    # directly from C47 rather than reusing ``canonical_partitions`` or either
    # numerical operator implementation above.
    full = record["full_resolution_id"]
    c47_resolution = next(item for item in c47.RESOLUTIONS if item.label == full)
    source_partitions = tuple(c47.partitions(c47_resolution))
    states_per_partition = record["qg_dimension"] // len(source_partitions)
    if states_per_partition * len(source_partitions) != record["qg_dimension"]:
        raise RuntimeError(f"C47/C128 partition-dimension mismatch at {full}")
    for partition_id, (_, _, xq, xg) in enumerate(source_partitions):
        start = record["q_dimension"] + partition_id * states_per_partition
        stop = start + states_per_partition
        coefficient = mu_q_sq / float(xq) + delta_mu_g_sq / float(xg)
        output[start:stop] = coefficient * value[start:stop]
    output.setflags(write=False)
    return output


def deterministic_validation_vectors(resolution: str) -> tuple[tuple[str, np.ndarray], ...]:
    record = resolution_record(resolution)
    dimension = record["direct_sum_dimension"]
    q_only = np.zeros(dimension, dtype=np.complex128)
    q_only[: record["q_dimension"]] = np.arange(1, record["q_dimension"] + 1) * (1.0 + 0.25j)
    partition_probe = np.zeros(dimension, dtype=np.complex128)
    for partition in canonical_partitions(resolution):
        partition_probe[partition.qg_direct_start] = complex(partition.partition_id + 1, -0.5)
        partition_probe[partition.qg_direct_stop - 1] = complex(-0.25, partition.partition_id + 1)
    seed = 401000 + record["K2"]
    rng = np.random.default_rng(seed)
    random = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    random /= np.linalg.norm(random)
    for value in (q_only, partition_probe, random):
        value.setflags(write=False)
    return (("q_only", q_only), ("partition_probe", partition_probe), ("random", random))


def sparse_matrix_free_validation(resolution: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    maximum = 0.0
    for direction in DIRECTIONS:
        operator = sparse_coordinate_operator(resolution, direction)
        csr = coordinate_operator_csr(resolution, direction)
        linear = coordinate_linear_operator(resolution, direction)
        for vector_id, vector in deterministic_validation_vectors(resolution):
            coo_action = apply_sparse_coordinate_operator(operator, vector)
            csr_action = np.asarray(csr @ vector)
            linear_action = np.asarray(linear @ vector)
            matrix_free = apply_mass_direction(resolution, direction, vector)
            scale = max(float(np.linalg.norm(matrix_free)), 1.0)
            route_residuals = {
                "coo_record_vs_matrix_free": float(np.linalg.norm(coo_action - matrix_free)),
                "scipy_csr_vs_matrix_free": float(np.linalg.norm(csr_action - matrix_free)),
                "linear_operator_vs_matrix_free": float(np.linalg.norm(linear_action - matrix_free)),
                "scipy_csr_hermiticity": float(np.linalg.norm((csr - csr.getH()).data)),
            }
            route_relatives = {
                key: residual / scale for key, residual in route_residuals.items()
            }
            relative = max(route_relatives.values(), default=0.0)
            maximum = max(maximum, relative)
            rows.append(
                {
                    "direction": direction,
                    "vector_id": vector_id,
                    "absolute_residuals": route_residuals,
                    "relative_residuals": route_relatives,
                    "maximum_relative_residual": relative,
                }
            )
    payload = {
        "schema": "C401-C396-MASS-SPARSE-MATRIX-FREE-VALIDATION-V2",
        "resolution": normalize_resolution(resolution)[0],
        "routes": (
            "canonical block formula",
            "serialized COO record",
            "SciPy CSR matrix",
            "SciPy LinearOperator",
            "independent matrix-free block action",
        ),
        "rows": tuple(rows),
        "maximum_relative_residual": maximum,
        "tolerance": 1.0e-13,
        "pass": maximum <= 1.0e-13,
    }
    return {**payload, "root": content_root(payload)}


def finite_difference_validation(
    resolution: str,
    *,
    steps: Iterable[float] = (1.0e-2, 1.0e-4, 1.0e-6),
    base_mu_q_sq: float = 0.31,
    base_delta_mu_g_sq: float = 0.17,
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    maximum = 0.0
    for direction in DIRECTIONS:
        for vector_id, vector in deterministic_validation_vectors(resolution):
            analytic = apply_mass_direction(resolution, direction, vector)
            for step in steps:
                step = float(step)
                if not np.isfinite(step) or step <= 0:
                    raise ValueError("positive finite finite-difference steps required")
                if direction == D_MU_Q_SQ:
                    plus = source_mass_component_action(
                        resolution,
                        vector,
                        mu_q_sq=base_mu_q_sq + step,
                        delta_mu_g_sq=base_delta_mu_g_sq,
                    )
                    minus = source_mass_component_action(
                        resolution,
                        vector,
                        mu_q_sq=base_mu_q_sq - step,
                        delta_mu_g_sq=base_delta_mu_g_sq,
                    )
                else:
                    plus = source_mass_component_action(
                        resolution,
                        vector,
                        mu_q_sq=base_mu_q_sq,
                        delta_mu_g_sq=base_delta_mu_g_sq + step,
                    )
                    minus = source_mass_component_action(
                        resolution,
                        vector,
                        mu_q_sq=base_mu_q_sq,
                        delta_mu_g_sq=base_delta_mu_g_sq - step,
                    )
                finite_difference = (plus - minus) / (2.0 * step)
                residual = float(np.linalg.norm(finite_difference - analytic))
                scale = max(float(np.linalg.norm(analytic)), 1.0)
                relative = residual / scale
                maximum = max(maximum, relative)
                rows.append(
                    {
                        "direction": direction,
                        "vector_id": vector_id,
                        "step": step,
                        "absolute_residual": residual,
                        "relative_residual": relative,
                    }
                )
    payload = {
        "schema": "C401-C396-MASS-SOURCE-FORMULA-FINITE-DIFFERENCE-V2",
        "status": "PASS" if maximum <= 2.0e-9 else "FAIL",
        "resolution": normalize_resolution(resolution)[0],
        "diagnostic_base_point": {
            "mu_q_sq": base_mu_q_sq,
            "delta_mu_g_sq": base_delta_mu_g_sq,
            "physical": False,
        },
        "rows": tuple(rows),
        "maximum_relative_residual": maximum,
        "tolerance": 2.0e-9,
        "pass": maximum <= 2.0e-9,
        "historical_C128_numeric_implementation_used": False,
        "reason": (
            "historical C128 quark fractions fail the C45/C47 xq+xg=1 source identity; "
            "the holdout differentiates the source formula independently"
        ),
    }
    return {**payload, "root": content_root(payload)}


def _historical_c128_direction_diagonal(resolution: str, direction: str) -> np.ndarray:
    _check_direction(direction)
    _, full = normalize_resolution(resolution)
    diagonal = np.zeros(c128.DIRECT_DIMS[full], dtype=np.float64)
    if direction == D_MU_Q_SQ:
        diagonal[: c128.Q_DIM] = 1.0
    historical = tuple(c128._partitions(full))  # noqa: SLF001 - defect audit only
    states_per_partition = c128.QG_DIMS[full] // len(historical)
    for partition_id, row in enumerate(historical):
        fraction = float(Fraction(row[2] if direction == D_MU_Q_SQ else row[3]))
        start = c128.Q_DIM + partition_id * states_per_partition
        stop = start + states_per_partition
        diagonal[start:stop] = 1.0 / fraction
    diagonal.setflags(write=False)
    return diagonal


def historical_c128_derivative_comparison(resolution: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for direction in DIRECTIONS:
        canonical = operator_diagonal(resolution, direction)
        historical = _historical_c128_direction_diagonal(resolution, direction)
        difference = historical - canonical
        absolute_difference = np.abs(difference)
        scale = max(float(np.max(np.abs(canonical))), 1.0)
        tolerance = 8.0 * np.finfo(np.float64).eps * scale
        material_mask = absolute_difference > tolerance
        relative = float(np.linalg.norm(difference) / max(np.linalg.norm(canonical), 1.0))
        rows.append(
            {
                "direction": direction,
                "maximum_absolute_difference": float(np.max(absolute_difference)),
                "relative_frobenius_difference": relative,
                "raw_entries_different": int(np.count_nonzero(difference)),
                "material_entries_different": int(np.count_nonzero(material_mask)),
                # Compatibility alias: scientific comparisons use material,
                # tolerance-qualified differences, not bit-level roundoff.
                "entries_different": int(np.count_nonzero(material_mask)),
                "comparison_tolerance": tolerance,
                "byte_identical": bool(np.array_equal(historical, canonical)),
                "historical_matches_source_corrected": bool(
                    np.allclose(historical, canonical, rtol=0.0, atol=tolerance)
                ),
                "historical_diagonal_hash": _array_hash(historical),
                "source_corrected_diagonal_hash": _array_hash(canonical),
            }
        )
    payload = {
        "schema": "C401-HISTORICAL-C128-MASS-DERIVATIVE-COMPARISON-V1",
        "resolution": normalize_resolution(resolution)[0],
        "partition_defect_root": historical_c128_partition_defect_audit()["root"],
        "rows": tuple(rows),
        "expected_result": {
            D_MU_Q_SQ: "MISMATCH_EXPECTED_AND_EXPOSED",
            D_DELTA_MU_G_SQ: "MATCH_EXPECTED",
        },
        "historical_C128_modified": False,
    }
    return {**payload, "root": content_root(payload)}


def mass_direction_operator_inventory() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for resolution in RESOLUTION_LABELS:
        for direction in DIRECTIONS:
            operator = sparse_coordinate_operator(resolution, direction)
            diagonal = operator_diagonal(resolution, direction)
            rows.append(
                {
                    "resolution": resolution,
                    "full_resolution_id": operator["full_resolution_id"],
                    "direction": direction,
                    "raw_C396_coordinate": operator["raw_C396_coordinate"],
                    "implementation_coordinate": operator["implementation_coordinate"],
                    "shape": operator["shape"],
                    "nnz": operator["nnz"],
                    "minimum_diagonal": float(np.min(diagonal)),
                    "maximum_diagonal": float(np.max(diagonal)),
                    "unique_diagonal_values": tuple(float(value) for value in np.unique(diagonal)),
                    "array_hashes": operator["array_hashes"],
                    "exact_blocks": operator["exact_blocks"],
                    "sparse_record_path": (
                        "deuteron_wigner.bridge.c401_c396_mass_directions."
                        "sparse_coordinate_operator"
                    ),
                    "sparse_apply_path": (
                        "deuteron_wigner.bridge.c401_c396_mass_directions."
                        "coordinate_operator_csr"
                    ),
                    "matrix_free_apply_path": (
                        "deuteron_wigner.bridge.c401_c396_mass_directions."
                        "apply_mass_direction"
                    ),
                    "physical_value_selected": False,
                    "rank_claim": False,
                }
            )
    payload = {
        "schema": "C401-C396-MASS-DIRECTION-OPERATOR-INVENTORY-V1",
        "status": "C396_FIRST_SIX_K_LOCAL_NUMERICAL_BINDINGS_READY_DIAGNOSTIC_ONLY",
        "rows": tuple(rows),
        "row_count": len(rows),
        "complete_numerical_apply_rows": len(rows),
        "resolutions": RESOLUTION_LABELS,
        "directions": DIRECTIONS,
        "physical_values_selected": 0,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


def all_validation_records() -> dict[str, Any]:
    sparse = tuple(sparse_matrix_free_validation(resolution) for resolution in RESOLUTION_LABELS)
    finite_difference = tuple(finite_difference_validation(resolution) for resolution in RESOLUTION_LABELS)
    historical = tuple(
        historical_c128_derivative_comparison(resolution) for resolution in RESOLUTION_LABELS
    )
    payload = {
        "schema": "C401-C396-MASS-DIRECTION-VALIDATION-SUMMARY-V1",
        "sparse_matrix_free": sparse,
        "finite_difference": finite_difference,
        "historical_C128_comparison": historical,
        "sparse_matrix_free_pass": all(record["pass"] for record in sparse),
        "finite_difference_pass": all(record["pass"] for record in finite_difference),
        "historical_quark_fraction_defect_exposed": all(
            next(row for row in record["rows"] if row["direction"] == D_MU_Q_SQ)[
                "entries_different"
            ]
            > 0
            for record in historical
        ),
        "historical_gluon_fraction_unchanged": all(
            next(row for row in record["rows"] if row["direction"] == D_DELTA_MU_G_SQ)[
                "entries_different"
            ]
            == 0
            for record in historical
        ),
    }
    payload["pass"] = bool(
        payload["sparse_matrix_free_pass"]
        and payload["finite_difference_pass"]
        and payload["historical_quark_fraction_defect_exposed"]
        and payload["historical_gluon_fraction_unchanged"]
    )
    return {**payload, "root": content_root(payload)}


__all__ = [
    "D_MU_Q_SQ",
    "D_DELTA_MU_G_SQ",
    "DIRECTIONS",
    "DirectionSpecification",
    "direction_specification",
    "exact_block_records",
    "operator_diagonal",
    "sparse_coordinate_operator",
    "coordinate_operator_csr",
    "coordinate_linear_operator",
    "apply_sparse_coordinate_operator",
    "apply_mass_direction",
    "source_mass_component_action",
    "deterministic_validation_vectors",
    "sparse_matrix_free_validation",
    "finite_difference_validation",
    "historical_c128_derivative_comparison",
    "mass_direction_operator_inventory",
    "all_validation_records",
]
