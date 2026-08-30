"""Versioned derivative-integrity adapter for the nonphysical C144 fixture.

Historical C144 code and roots are not modified.  This module reconstructs the
actual polynomial response of the public C144 operator, compares it with the
historical derivative record and central finite differences, and labels zero
fixture response as *numerically unbound*, never physically irrelevant.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence, Tuple

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

from deuteron_wigner.bridge.hqcd4 import core as c131
from deuteron_wigner.bridge.hqcdopapi import core as c144


C144_COORDINATES: Tuple[str, ...] = (
    "phi_mass",
    "phi_coupling",
    *(f"eta_{index}" for index in range(9)),
)
_RESOLUTION_IDS = {
    "K9": "K9_2_N8_b0.40",
    "K11": "K11_2_N10_b0.45",
    "K13": "K13_2_N12_b0.50",
}


class DerivativeIntegrityError(ValueError):
    """Raised when a diagnostic derivative request violates the C400 contract."""


@dataclass(frozen=True)
class MatrixDifference:
    frobenius_norm: float
    max_abs_entry: float
    differing_entries: int
    reference_norm: float
    relative_frobenius: float


@dataclass(frozen=True)
class DerivativeAudit:
    resolution: str
    coordinate_id: str
    step: float
    response_status: str
    corrected_nnz: int
    finite_difference_nnz: int
    historical_nnz: int
    corrected_vs_finite_difference: MatrixDifference
    historical_vs_corrected: MatrixDifference
    corrected_derivative_verified: bool
    historical_derivative_matches: bool
    physical_derivative_claim: bool = False
    C396_derivative_claim: bool = False


def _plain(value: Any) -> Any:
    if hasattr(value, "items"):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(item) for item in value]
    return value


def _canonical_coordinate(direction_id: str) -> str:
    if direction_id in C144_COORDINATES:
        return direction_id
    if direction_id in c144.ORIGINAL:
        return C144_COORDINATES[c144.ORIGINAL.index(direction_id)]
    raise DerivativeIntegrityError(f"unknown C144 diagnostic coordinate: {direction_id!r}")


def _validated_identified_record(record: Mapping[str, Any]) -> Mapping[str, Any]:
    validated = c144.validate_parameter_record(record)
    if validated["basis_tag"] != c144.IDENTIFIED_BASIS:
        validated = c144.convert_parameter_coordinates(validated, c144.IDENTIFIED_BASIS)
    return validated


def diagnostic_record(resolution: str = "K9") -> Mapping[str, Any]:
    if resolution not in c144.RESOLUTIONS:
        raise DerivativeIntegrityError(f"unsupported C144 resolution: {resolution!r}")
    fixture = c144.load_diagnostic_fixture("FIXTURE-INTERACTING-A")
    return c144.validate_parameter_record({**fixture, "resolution": resolution})


def _matrix_from_payload(payload: Mapping[str, Any]) -> csr_matrix:
    shape = tuple(int(value) for value in payload["shape"])
    entries = tuple(payload.get("entries", ()))
    if not entries:
        return csr_matrix(shape, dtype=np.complex128)
    rows, columns, values = zip(
        *((int(row), int(column), complex(value)) for row, column, value in entries)
    )
    return coo_matrix((values, (rows, columns)), shape=shape, dtype=np.complex128).tocsr()


def operator_matrix(resolution: str, record: Mapping[str, Any]) -> csr_matrix:
    return _matrix_from_payload(c144.parameterized_sparse_operator(resolution, parameter_record=record))


def shifted_record(
    record: Mapping[str, Any], coordinate_id: str, displacement: float
) -> Mapping[str, Any]:
    coordinate = _canonical_coordinate(coordinate_id)
    if not np.isfinite(displacement):
        raise DerivativeIntegrityError("coordinate displacement must be finite")
    validated = _validated_identified_record(record)
    coordinates = dict(validated["coordinates"])
    coordinates[coordinate] = complex(coordinates[coordinate]) + float(displacement)
    return c144.validate_parameter_record(
        {
            "basis_tag": c144.IDENTIFIED_BASIS,
            "coordinates": coordinates,
            "claim_tier": c144.CLAIM_TIER,
            "no_default": True,
            "no_physical_claim": True,
            "resolution": validated["resolution"],
            "fixture_id": validated["fixture_id"],
        }
    )


def finite_difference_derivative(
    resolution: str,
    coordinate_id: str,
    *,
    record: Mapping[str, Any] | None = None,
    step: float = 1.0e-5,
) -> csr_matrix:
    if not np.isfinite(step) or step <= 0.0:
        raise DerivativeIntegrityError("finite-difference step must be finite and positive")
    base = diagnostic_record(resolution) if record is None else _validated_identified_record(record)
    plus = operator_matrix(resolution, shifted_record(base, coordinate_id, step))
    minus = operator_matrix(resolution, shifted_record(base, coordinate_id, -step))
    result = (plus - minus) * (0.5 / step)
    result.eliminate_zeros()
    return result.tocsr()


def _owner_entries(resolution: str, term: str) -> Tuple[Tuple[int, int], ...]:
    matrix = c131.bare_coefficient_matrix(_RESOLUTION_IDS[resolution], c131.DEGREES[term])
    owner = next(row for row in matrix["terms"] if row["term_id"] == term)
    return tuple((int(entry["row"]), int(entry["col"])) for entry in owner["entries"])


def _effective_values(record: Mapping[str, Any]) -> tuple[float, float]:
    validated = _validated_identified_record(record)
    coordinates = validated["coordinates"]
    return float(complex(coordinates["phi_mass"]).real), float(
        complex(coordinates["phi_coupling"]).real
    )


def corrected_derivative(
    resolution: str,
    coordinate_id: str,
    *,
    record: Mapping[str, Any] | None = None,
) -> csr_matrix:
    """Return the derivative of the operator actually evaluated by C144.

    This is a C400-owned diagnostic adapter.  It deliberately follows the
    numerical polynomial in ``C144.parameterized_sparse_operator`` even when
    that polynomial disagrees with a historical owner-degree descriptor.
    """

    if resolution not in c144.RESOLUTIONS:
        raise DerivativeIntegrityError(f"unsupported C144 resolution: {resolution!r}")
    coordinate = _canonical_coordinate(coordinate_id)
    base = diagnostic_record(resolution) if record is None else _validated_identified_record(record)
    mass, coupling = _effective_values(base)
    accumulator: dict[tuple[int, int], complex] = {}

    for term in c131.TERMS:
        for row, column in _owner_entries(resolution, term):
            value = 0.0
            if coordinate == "phi_mass":
                if term == "C128_FREE" and row < 6:
                    value = 2.0 * mass
            elif coordinate == "phi_coupling":
                if term == "C53_CANONICAL_VERTEX":
                    value = (min(row, column) + 1) / 100.0
                elif term != "C128_FREE":
                    owner_index = (
                        0
                        if term == "C112_INSTANTANEOUS_FERMION"
                        else 1
                        if term == "C127_INSTANTANEOUS_CURRENT"
                        else 2
                    )
                    value = 2.0 * coupling * ((row + 1) / (1000.0 + owner_index))
            elif coordinate == "eta_0" and term == "C112_INSTANTANEOUS_FERMION":
                value = 1.0
            elif coordinate == "eta_1" and term == "C127_INSTANTANEOUS_CURRENT":
                value = 1.0
            elif coordinate == "eta_2" and term in {"C129_G3_RETAINED", "C129_G4_RETAINED"}:
                value = 1.0

            if value != 0.0:
                key = (row, column)
                accumulator[key] = accumulator.get(key, 0.0j) + complex(value)

    if not accumulator:
        return csr_matrix((c144.DIMS[resolution], c144.DIMS[resolution]), dtype=np.complex128)
    ordered = sorted(accumulator)
    rows = [key[0] for key in ordered]
    columns = [key[1] for key in ordered]
    values = [accumulator[key] for key in ordered]
    result = coo_matrix(
        (values, (rows, columns)),
        shape=(c144.DIMS[resolution], c144.DIMS[resolution]),
        dtype=np.complex128,
    ).tocsr()
    result.eliminate_zeros()
    return result


def historical_derivative(
    resolution: str,
    coordinate_id: str,
    *,
    record: Mapping[str, Any] | None = None,
) -> csr_matrix:
    base = diagnostic_record(resolution) if record is None else _validated_identified_record(record)
    coordinate = _canonical_coordinate(coordinate_id)
    payload = c144.operator_derivative(resolution, coordinate, parameter_record=base)
    entries = payload["entries"]
    if not entries:
        return csr_matrix((c144.DIMS[resolution], c144.DIMS[resolution]), dtype=np.complex128)
    rows, columns, values = zip(
        *((int(row), int(column), complex(value)) for row, column, value in entries)
    )
    matrix = coo_matrix(
        (values, (rows, columns)),
        shape=(c144.DIMS[resolution], c144.DIMS[resolution]),
        dtype=np.complex128,
    ).tocsr()
    matrix.sum_duplicates()
    matrix.eliminate_zeros()
    return matrix


def matrix_difference(reference: csr_matrix, candidate: csr_matrix, *, atol: float = 1e-10) -> MatrixDifference:
    if reference.shape != candidate.shape:
        raise DerivativeIntegrityError("matrix shapes differ")
    delta = (candidate - reference).tocsr()
    delta.eliminate_zeros()
    values = np.asarray(delta.data, dtype=np.complex128)
    magnitudes = np.abs(values)
    frobenius = float(np.sqrt(np.sum(magnitudes**2))) if magnitudes.size else 0.0
    maximum = float(np.max(magnitudes)) if magnitudes.size else 0.0
    differing = int(np.count_nonzero(magnitudes > atol))
    reference_norm = float(np.sqrt(np.sum(np.abs(reference.data) ** 2))) if reference.nnz else 0.0
    relative = frobenius / reference_norm if reference_norm > 0.0 else (0.0 if frobenius == 0.0 else float("inf"))
    return MatrixDifference(frobenius, maximum, differing, reference_norm, relative)


def audit_derivative(
    resolution: str,
    coordinate_id: str,
    *,
    step: float = 1.0e-5,
    atol: float = 1.0e-8,
    rtol: float = 1.0e-6,
) -> DerivativeAudit:
    coordinate = _canonical_coordinate(coordinate_id)
    base = diagnostic_record(resolution)
    corrected = corrected_derivative(resolution, coordinate, record=base)
    finite = finite_difference_derivative(resolution, coordinate, record=base, step=step)
    historical = historical_derivative(resolution, coordinate, record=base)
    corrected_fd = matrix_difference(corrected, finite, atol=atol)
    historical_corrected = matrix_difference(corrected, historical, atol=atol)
    tolerance = atol + rtol * max(corrected_fd.reference_norm, 1.0)
    verified = corrected_fd.frobenius_norm <= tolerance
    historical_matches = historical_corrected.frobenius_norm <= (
        atol + rtol * max(historical_corrected.reference_norm, 1.0)
    )
    if corrected.nnz == 0 and finite.nnz == 0:
        status = "NUMERICALLY_UNBOUND_IN_C144_FIXTURE_API"
    elif verified:
        status = "VERIFIED_C400_DIAGNOSTIC_DERIVATIVE"
    else:
        status = "C400_DIAGNOSTIC_DERIVATIVE_INTEGRITY_FAILURE"
    return DerivativeAudit(
        resolution=resolution,
        coordinate_id=coordinate,
        step=step,
        response_status=status,
        corrected_nnz=int(corrected.nnz),
        finite_difference_nnz=int(finite.nnz),
        historical_nnz=int(historical.nnz),
        corrected_vs_finite_difference=corrected_fd,
        historical_vs_corrected=historical_corrected,
        corrected_derivative_verified=verified,
        historical_derivative_matches=historical_matches,
    )


def audit_all_c144_derivatives(
    *, resolutions: Sequence[str] = c144.RESOLUTIONS, step: float = 1.0e-5
) -> Mapping[str, Any]:
    audits = tuple(
        audit_derivative(resolution, coordinate, step=step)
        for resolution in resolutions
        for coordinate in C144_COORDINATES
    )
    rows = tuple(asdict(audit) for audit in audits)
    return deepcopy(
        {
            "schema": "C400-S2-C144-DERIVATIVE-INTEGRITY-AUDIT-V1",
            "rows": rows,
            "count": len(rows),
            "corrected_verified": sum(row["corrected_derivative_verified"] for row in rows),
            "historical_mismatches": sum(not row["historical_derivative_matches"] for row in rows),
            "numerically_unbound": tuple(
                (row["resolution"], row["coordinate_id"])
                for row in rows
                if row["response_status"] == "NUMERICALLY_UNBOUND_IN_C144_FIXTURE_API"
            ),
            "physical_derivative_claim": False,
            "C396_derivative_claim": False,
        }
    )


__all__ = [
    "C144_COORDINATES",
    "DerivativeIntegrityError",
    "MatrixDifference",
    "DerivativeAudit",
    "diagnostic_record",
    "operator_matrix",
    "shifted_record",
    "finite_difference_derivative",
    "corrected_derivative",
    "historical_derivative",
    "matrix_difference",
    "audit_derivative",
    "audit_all_c144_derivatives",
]
