"""C95 fails closed if C94's exported API cannot supply theorem inputs."""
from __future__ import annotations

from types import MappingProxyType
from typing import Any

from ..ifequivapi2 import load_verified_c93_public_authority

STATUS = "C95_IFEQUIV7_HISTORICAL_PUBLIC_INPUT_INCOMPLETE"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")


def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    return value


def audit_c94_public_inputs() -> Any:
    """Inspect only C94's exported package API, never its core/private capsule paths."""
    import deuteron_wigner.bridge.ifequivapi2 as public
    authority = load_verified_c93_public_authority()
    required = {
        "historical_pair_attestation", "historical_pair_page", "historical_pair_by_sequence",
        "historical_pair_normal_form", "historical_pair_proof_inputs",
        "historical_primitive_family", "historical_primitive_record", "historical_primitive_page",
        "expansion_theorem_specification", "verify_factorized_expansion_equivalence",
    }
    exported = set(public.__all__); missing = sorted(required.difference(exported))
    return _freeze({"authority_verified": bool(authority["pass"]), "public_operations": tuple(public.__all__), "required_operations": tuple(sorted(required)),
                    "missing_operations": tuple(missing), "complete_theorem_input_access": not missing,
                    "blocker": "C94_PUBLIC_API_DOES_NOT_EXPORT_HISTORICAL_NORMAL_FORM_PROOF_INPUT_OR_PRIMITIVE_RECORD_ACCESS" if missing else None,
                    "private_C94_core_imported": False, "private_C93_access": False})


def recompile_descendant_census() -> Any:
    """Current-side-only recompilation; it consumes no historical API output."""
    from ..ifequiv6.core import compile_descendant_programs
    result = {}
    for resolution in RESOLUTIONS:
        pairs = logical = 0
        for program in compile_descendant_programs(resolution):
            pairs += 1; logical += program["cardinality"]
        result[resolution] = {"pairs": pairs, "logical": logical}
    return _freeze(result)
