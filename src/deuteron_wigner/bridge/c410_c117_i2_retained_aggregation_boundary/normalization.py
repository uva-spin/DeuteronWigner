"""C410 normalization boundary for the first C117 direction."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .authority import STATUS

MISSING_NORMALIZATION_OBJECT = (
    "source-qualified K-local C260/C262 finite-C43 adapter and operator-"
    "normalization record mapping the C410 source-reduced retained connected "
    "shape to the PROJECT_C117_RI_SMOM_V1 O_C117_1,R insertion, including the "
    "remaining field/state/M2 and normalized-wavepacket convention"
)


@lru_cache(maxsize=1)
def normalization_boundary_record() -> Mapping[str, Any]:
    closed = (
        {
            "factor": "C114 source current-square coefficient",
            "value": "-1/2",
            "status": "EXACT_SOURCE_FACTOR_APPLIED_ONCE",
        },
        {
            "factor": "g_s^2",
            "value": "FACTORED",
            "status": "C259_C260_OPERATOR_BASIS_CONVENTION",
        },
        {
            "factor": "C409 derivative/inverse-derivative L and pi powers",
            "value": "net zero",
            "status": "EXACTLY_RECONCILED",
        },
        {
            "factor": "four source-ordered current products",
            "value": "multiplicity one each",
            "status": "COUNT_ONCE_CLOSED",
        },
        {
            "factor": "vacuum c-number",
            "value": "routed outside retained connected matrix",
            "status": "C129_C131_C136_VACUUM_DIRECTION",
        },
    )
    open_rows = (
        {
            "factor": "finite C43 operator adapter",
            "owner": "C260/C262",
            "status": "UNAVAILABLE_NOT_ZERO",
        },
        {
            "factor": "field/external-state/M2 normalization in the C117 scheme",
            "owner": "C115/C119/C260",
            "status": "UNAVAILABLE_NOT_ZERO",
        },
        {
            "factor": "normalized finite-cell wavepacket mapping",
            "owner": "C260/C262",
            "status": "UNAVAILABLE_NOT_ZERO",
        },
    )
    payload = {
        "schema": "C410-C117-I2-NORMALIZATION-BOUNDARY-V1",
        "status": STATUS,
        "closed_factors": closed,
        "open_factors": open_rows,
        "source_reduced_shape_units": (
            "GeV^2 times the unresolved C260 finite-C43 operator-normalization adapter"
        ),
        "coordinate_value_required_to_define_derivative_shape": False,
        "physical_g_s_required_to_define_operator_shape": False,
        "g_s_squared_factored": True,
        "c_C117_1_selected": False,
        "C260_tree_scheme_target_used_as_physical_value": False,
        "smallest_missing_object": MISSING_NORMALIZATION_OBJECT,
        "complete_C117_action": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def normalization_capsule_schema() -> Mapping[str, Any]:
    required = (
        "capsule_id",
        "resolution",
        "scheme_id",
        "operator_id",
        "finite_C43_adapter_definition",
        "field_normalization",
        "external_state_normalization",
        "Pminus_to_M2_conversion",
        "wavepacket_definition",
        "units",
        "source_locator",
        "source_sha256",
        "signature",
        "no_default",
    )
    payload = {
        "schema": "C410-C117-I2-NORMALIZATION-CAPSULE-SCHEMA-V1",
        "status": STATUS,
        "required": required,
        "resolution_values": ("K9", "K11", "K13"),
        "scheme_id": "PROJECT_C117_RI_SMOM_V1",
        "operator_id": "O_C117_1",
        "g_s_squared": "FACTORED_NOT_NUMERIC_FIELD",
        "c_C117_1": "NOT_PART_OF_OPERATOR_NORMALIZATION_CAPSULE",
        "physical": False,
        "no_default": True,
    }
    return dict(payload, root=content_root(payload))


def validate_normalization_capsule(record: Mapping[str, Any]) -> Mapping[str, Any]:
    schema = normalization_capsule_schema()
    missing = tuple(key for key in schema["required"] if key not in record)
    if missing:
        raise ValueError("normalization capsule missing fields: {}".format(missing))
    if record.get("resolution") not in schema["resolution_values"]:
        raise ValueError("unsupported normalization capsule resolution")
    if record.get("scheme_id") != schema["scheme_id"]:
        raise ValueError("normalization capsule scheme mismatch")
    if record.get("operator_id") != schema["operator_id"]:
        raise ValueError("normalization capsule operator mismatch")
    if record.get("no_default") is not True:
        raise ValueError("normalization capsule must assert no_default=true")
    source_hash = str(record.get("source_sha256", ""))
    if len(source_hash) != 64 or any(ch not in "0123456789abcdef" for ch in source_hash):
        raise ValueError("normalization capsule requires a lowercase SHA-256")
    payload = {
        "schema": "C410-C117-I2-NORMALIZATION-CAPSULE-VALIDATION-V1",
        "status": STATUS,
        "capsule_id": str(record["capsule_id"]),
        "resolution": str(record["resolution"]),
        "scheme_id": str(record["scheme_id"]),
        "operator_id": str(record["operator_id"]),
        "field_count": len(record),
        "structurally_valid": True,
        "numerical_authority_certified_by_C410": False,
        "physical": False,
    }
    return dict(payload, root=content_root(payload))


def complete_c117_i2_csr(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C410 cannot construct O_C117_1,R: {}".format(MISSING_NORMALIZATION_OBJECT)
    )


def apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C410 cannot apply O_C117_1,R: {}".format(MISSING_NORMALIZATION_OBJECT)
    )


__all__ = [
    "MISSING_NORMALIZATION_OBJECT",
    "normalization_boundary_record",
    "normalization_capsule_schema",
    "validate_normalization_capsule",
    "complete_c117_i2_csr",
    "apply_complete_c117_i2",
]
