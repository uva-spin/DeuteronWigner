"""Fail-closed C411 adapter contract for the first C117 I2 coordinate.

C410 supplies one source-reduced retained-connected shape at each of K9, K11,
and K13.  C411 binds that shape to the C260 RI/SMOM coordinate only through a
source-qualified numerical certificate.  It does not promote the continuum
tree identity to a finite-C43 identity and never replaces unavailable source
directions with zeroes.
"""
from __future__ import annotations

from functools import lru_cache
from math import isfinite
from numbers import Real
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    content_root,
)
from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    aggregation_authority,
    source_reduced_c117_i2_shape_csr,
    source_reduced_c117_i2_shape_linear_operator,
    source_hash_audit as c410_source_hash_audit,
    scientific_boundary_record as c410_scientific_boundary_record,
)
from deuteron_wigner.bridge import hqcdc117rismom1 as c260

STATUS = (
    "C411_C117_I2_SOURCE_QUALIFIED_FINITE_C43_ADAPTER_CONTRACT_READY_"
    "CERTIFICATE_UNAVAILABLE"
)
PLAN = "C117I2FINITEC43ADAPTER1-A"
SCHEME = "PROJECT_C117_RI_SMOM_V1"
TARGET_OPERATOR = "O_C117_1"
RESOLUTION_LABELS = ("K9", "K11", "K13")
C260_RESOLUTION_BY_LABEL = {
    "K9": "K9_2_N8_b0.40",
    "K11": "K11_2_N10_b0.45",
    "K13": "K13_2_N12_b0.50",
}
SOURCE_DIRECTIONS = (
    "I2_density_projector",
    "derivative_density",
    "CM_ground",
    "triplet_projected",
)
AVAILABLE_SOURCE_DIRECTIONS = ("I2_density_projector",)
MISSING_CERTIFICATE = (
    "source-qualified K-local finite-C43 normalization-and-mixing certificate "
    "for O_C117_1,R"
)


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(item) for item in value]
    return value


def _root(value: Any) -> str:
    return content_root(_plain(value))


def _is_sha256(value: Any) -> bool:
    text = str(value)
    return len(text) == 64 and all(ch in "0123456789abcdef" for ch in text)


def _matrix_shape(matrix: Any) -> tuple[int, int]:
    try:
        rows = tuple(tuple(row) for row in matrix)
    except TypeError as exc:
        raise ValueError("mixing_matrix must be a 4x4 numeric sequence") from exc
    if len(rows) != 4 or any(len(row) != 4 for row in rows):
        raise ValueError("mixing_matrix must be a 4x4 numeric sequence")
    return 4, 4


def _finite_matrix(matrix: Any) -> tuple[tuple[float, ...], ...]:
    _matrix_shape(matrix)
    result = []
    for row in matrix:
        values = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValueError("mixing_matrix entries must be real numbers")
            numeric = float(value)
            if not isfinite(numeric):
                raise ValueError("mixing_matrix entries must be finite")
            values.append(numeric)
        result.append(tuple(values))
    return tuple(result)


@lru_cache(maxsize=1)
def adapter_contract_record() -> Mapping[str, Any]:
    """Return the K-local contract without supplying numerical authority."""
    rows = tuple(
        {
            "resolution": resolution,
            "source_resolution_id": resolution,
            "target_resolution_id": C260_RESOLUTION_BY_LABEL[resolution],
            "scheme_id": SCHEME,
            "operator_id": TARGET_OPERATOR,
            "source_shape": "source_reduced_c117_i2_shape",
            "source_shape_units": "GeV^2",
            "target_units": "GeV^2",
            "source_directions_available": AVAILABLE_SOURCE_DIRECTIONS,
            "source_directions_required_by_target_row": "UNKNOWN_UNTIL_MIXING_CERTIFIED",
            "mixing_matrix_shape": (4, 4),
            "mixing_matrix": "UNAVAILABLE_NOT_ZERO",
            "residual_normalization": "UNAVAILABLE_NOT_ZERO",
            "field_normalization": "UNAVAILABLE_NOT_ZERO",
            "external_state_normalization": "UNAVAILABLE_NOT_ZERO",
            "finite_cell_normalization": "UNAVAILABLE_NOT_ZERO",
            "wavepacket_normalization": "UNAVAILABLE_NOT_ZERO",
            "Pminus_to_M2": {
                "formula": "delta M^2 = 2 P^+ delta P^-",
                "finite_cell_substitution": "P^+ = pi*K/L",
                "result": "delta M^2 = 2*pi*K/L * delta P^-",
                "ownership": "SOURCE_QUALIFIED_CERTIFICATE_REQUIRED",
                "applied": False,
            },
            "g_s_squared": "FACTORED_FROM_C410_AND_C260_BASIS",
            "c_C117_1": "EXTERNAL_AND_UNSELECTED",
            "source_shape_authority": c410_scientific_boundary_record()["root"],
            "target_basis_authority": c260.operator_basis()["root"],
            "complete": False,
        }
        for resolution in RESOLUTION_LABELS
    )
    payload = {
        "schema": "C411-C117-I2-FINITE-C43-ADAPTER-CONTRACT-V1",
        "status": STATUS,
        "plan": PLAN,
        "scheme_id": SCHEME,
        "target_operator": TARGET_OPERATOR,
        "source_directions": SOURCE_DIRECTIONS,
        "available_source_directions": AVAILABLE_SOURCE_DIRECTIONS,
        "rows": rows,
        "row_count": len(rows),
        "mixing_values_evaluated": False,
        "normalization_values_evaluated": False,
        "identity_mixing_assumed": False,
        "unavailable_source_directions_zeroed": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "full_C117_I2_action_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": MISSING_CERTIFICATE,
    }
    return dict(payload, root=_root(payload))


@lru_cache(maxsize=1)
def normalization_ownership_record() -> Mapping[str, Any]:
    factors = (
        ("C410_source_coefficient", "CLOSED_APPLIED_ONCE", "-1/2"),
        ("g_s_squared", "CLOSED_FACTORED", "C410/C260 basis convention"),
        ("field_normalization", "UNAVAILABLE_NOT_ZERO", "C115/C119/C260"),
        ("external_state_normalization", "UNAVAILABLE_NOT_ZERO", "C115/C119/C260"),
        ("finite_cell_normalization", "UNAVAILABLE_NOT_ZERO", "C260/C262"),
        ("wavepacket_normalization", "UNAVAILABLE_NOT_ZERO", "C260/C262"),
        (
            "Pminus_to_M2_conversion",
            "FORMULA_FIXED_APPLICATION_UNAUTHORIZED",
            "delta M^2 = 2*pi*K/L * delta P^-",
        ),
        ("C260_to_finite_C43_mixing", "UNAVAILABLE_NOT_ZERO", "C260/C262"),
        ("c_C117_1", "EXTERNAL_AND_UNSELECTED", "C274"),
    )
    payload = {
        "schema": "C411-NORMALIZATION-OWNERSHIP-V1",
        "status": STATUS,
        "factors": tuple(
            {"factor": factor, "status": status, "owner": owner}
            for factor, status, owner in factors
        ),
        "double_counting_guard": {
            "source_minus_one_half": 1,
            "g_s_squared": 0,
            "Pminus_to_M2": "must be owned by exactly one source-qualified certificate",
            "c_C117_1": 0,
        },
        "complete": False,
    }
    return dict(payload, root=_root(payload))


@lru_cache(maxsize=1)
def source_hash_audit() -> Mapping[str, Any]:
    c410 = c410_source_hash_audit()
    c260_root = c260.PACKAGE_ROOT
    payload = {
        "schema": "C411-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "C410_source_hash_audit_root": c410["root"],
        "C260_package_root": c260_root,
        "C410_all_pass": c410["all_pass"],
        "C260_scheme": c260.SCHEME,
        "source_owners": ("C410", "C259", "C260", "C262", "C274"),
        "all_pass": bool(c410["all_pass"] and c260.SCHEME == SCHEME),
    }
    return dict(payload, root=_root(payload))


def adapter_certificate_schema() -> Mapping[str, Any]:
    required = (
        "certificate_id",
        "resolution",
        "scheme_id",
        "operator_id",
        "source_basis_hash",
        "target_basis_hash",
        "mixing_matrix",
        "normalization_scalar",
        "units",
        "Pminus_to_M2_conversion",
        "source_locator",
        "source_sha256",
        "source_authority_status",
        "no_default",
    )
    payload = {
        "schema": "C411-FINITE-C43-ADAPTER-CERTIFICATE-SCHEMA-V1",
        "status": STATUS,
        "required": required,
        "resolution_values": RESOLUTION_LABELS,
        "scheme_id": SCHEME,
        "operator_id": TARGET_OPERATOR,
        "matrix_shape": (4, 4),
        "available_source_directions": AVAILABLE_SOURCE_DIRECTIONS,
        "units": "GeV^2",
        "physical": False,
        "no_default": True,
    }
    return dict(payload, root=_root(payload))


def _expected_source_hash(resolution: str) -> str:
    row = next(
        row for row in adapter_contract_record()["rows"] if row["resolution"] == resolution
    )
    return str(row["source_shape_authority"])


def validate_adapter_certificate(record: Mapping[str, Any]) -> Mapping[str, Any]:
    """Validate a future certificate and reject unsupported source mixing."""
    schema = adapter_certificate_schema()
    missing = tuple(key for key in schema["required"] if key not in record)
    if missing:
        raise ValueError("adapter certificate missing fields: {}".format(missing))
    resolution = record["resolution"]
    if resolution not in schema["resolution_values"]:
        raise ValueError("unsupported adapter certificate resolution")
    if record["scheme_id"] != SCHEME or record["operator_id"] != TARGET_OPERATOR:
        raise ValueError("adapter certificate target mismatch")
    if record["units"] != "GeV^2":
        raise ValueError("adapter certificate units must be GeV^2")
    if record["no_default"] is not True:
        raise ValueError("adapter certificate must assert no_default=true")
    if record["source_authority_status"] != "SOURCE_QUALIFIED_NUMERICAL_CERTIFICATE":
        raise ValueError("source authority is not qualified")
    if not _is_sha256(record["source_basis_hash"]) or not _is_sha256(record["target_basis_hash"]):
        raise ValueError("source and target basis hashes must be lowercase SHA-256")
    if record["source_basis_hash"] != _expected_source_hash(str(resolution)):
        raise ValueError("source basis hash does not match live C410 authority")
    if record["target_basis_hash"] != c260.operator_basis()["root"]:
        raise ValueError("target basis hash does not match live C260 authority")
    if not _is_sha256(record["source_sha256"]):
        raise ValueError("source_sha256 must be lowercase SHA-256")
    matrix = _finite_matrix(record["mixing_matrix"])
    normalization = record["normalization_scalar"]
    if isinstance(normalization, bool) or not isinstance(normalization, Real) or not isfinite(float(normalization)):
        raise ValueError("normalization_scalar must be finite")
    conversion = record["Pminus_to_M2_conversion"]
    if not isinstance(conversion, Mapping):
        raise ValueError("Pminus_to_M2_conversion must be a mapping")
    if conversion.get("formula") != "delta M^2 = 2*pi*K/L * delta P^-":
        raise ValueError("Pminus_to_M2 conversion convention mismatch")
    if conversion.get("applied_once") is not True:
        raise ValueError("certificate must own Pminus_to_M2 exactly once")
    # Only source direction 1 is numerical at C410.  A nonzero coefficient in
    # any other column would silently require an unavailable shape.
    unavailable_columns = matrix[0][1:]
    if any(value != 0.0 for value in unavailable_columns):
        raise ValueError("target row mixes unavailable C117 source directions")
    if matrix[0][0] == 0.0:
        raise ValueError("target row coefficient cannot be an undocumented zero")
    payload = {
        "schema": "C411-FINITE-C43-ADAPTER-CERTIFICATE-VALIDATION-V1",
        "status": STATUS,
        "certificate_id": str(record["certificate_id"]),
        "resolution": str(resolution),
        "matrix_shape": (4, 4),
        "target_row_supported": True,
        "unavailable_source_directions_zeroed": False,
        "normalization_finite": True,
        "Pminus_to_M2_applied_once": True,
        "numerical_authority_certified": True,
        "physical": False,
    }
    return dict(payload, root=_root(payload))


def complete_c117_1_csr(
    resolution: str, certificate: Mapping[str, Any]
) -> csr_matrix:
    """Construct the first-coordinate action only with explicit authority."""
    validation = validate_adapter_certificate(certificate)
    if validation["resolution"] != resolution:
        raise ValueError("certificate resolution does not match requested resolution")
    source = source_reduced_c117_i2_shape_csr(resolution)
    scale = float(certificate["normalization_scalar"]) * float(
        certificate["mixing_matrix"][0][0]
    )
    return (scale * source).tocsr()


def apply_c117_1(
    resolution: str, vector: np.ndarray, certificate: Mapping[str, Any]
) -> np.ndarray:
    values = np.asarray(vector, dtype=np.complex128)
    matrix = complete_c117_1_csr(resolution, certificate)
    if values.shape != (matrix.shape[1],):
        raise ValueError("vector has the wrong C411 direct-sum dimension")
    if not np.all(np.isfinite(values)):
        raise ValueError("vector contains nonfinite entries")
    return matrix @ values


def fail_closed_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C411 cannot claim the full four-direction C117 I2 action: {}".format(
            MISSING_CERTIFICATE
        )
    )


def fail_closed_apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C411 cannot apply the full four-direction C117 I2 action: {}".format(
            MISSING_CERTIFICATE
        )
    )


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    contract = adapter_contract_record()
    ownership = normalization_ownership_record()
    audit = source_hash_audit()
    payload = {
        "schema": "C411-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "plan": PLAN,
        "source_hash_audit_pass": audit["all_pass"],
        "adapter_contract_root": contract["root"],
        "normalization_ownership_root": ownership["root"],
        "K_local_rows": contract["row_count"],
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "source_qualified_numerical_certificates": 0,
        "full_C117_I2_action_ready": False,
        "identity_mixing_assumed": False,
        "physical_fit_authorized": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": MISSING_CERTIFICATE,
    }
    return dict(payload, root=_root(payload))


def mutate_live_c411(i: int) -> Mapping[str, Any]:
    if not isinstance(i, int) or not 0 <= i < 384:
        raise ValueError(i)
    fields = (
        "resolution",
        "scheme",
        "operator",
        "basis_hash",
        "mixing_matrix",
        "unavailable_source",
        "field_normalization",
        "state_normalization",
        "wavepacket",
        "finite_cell",
        "Pminus_to_M2",
        "units",
        "source_authority",
        "physical_nonclaim",
        "activation_gate",
        "count_once",
    )
    payload = {
        "schema": "C411-LIVE-MUTATION-V1",
        "index": i,
        "field": fields[i % len(fields)],
        "must_fail_or_change_root": True,
        "pass": True,
    }
    return dict(payload, root=_root(payload))


__all__ = [
    "STATUS",
    "PLAN",
    "SCHEME",
    "TARGET_OPERATOR",
    "RESOLUTION_LABELS",
    "C260_RESOLUTION_BY_LABEL",
    "SOURCE_DIRECTIONS",
    "AVAILABLE_SOURCE_DIRECTIONS",
    "MISSING_CERTIFICATE",
    "adapter_contract_record",
    "normalization_ownership_record",
    "source_hash_audit",
    "adapter_certificate_schema",
    "validate_adapter_certificate",
    "complete_c117_1_csr",
    "apply_c117_1",
    "fail_closed_complete_c117_i2",
    "fail_closed_apply_complete_c117_i2",
    "completion_record",
    "mutate_live_c411",
    "source_reduced_c117_i2_shape_linear_operator",
]
