"""Canonical, lossless value serialization for C5 validation objects."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from enum import Enum
from typing import Any


def _normalize(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, complex):
        return {"__complex__": [value.real, value.imag]}
    if not is_dataclass(value) and hasattr(value, "to_dict"):
        return {
            "__type__": f"{value.__class__.__module__}.{value.__class__.__qualname__}",
            "fields": _normalize(value.to_dict()),
        }
    if is_dataclass(value):
        return {
            "__type__": f"{value.__class__.__module__}.{value.__class__.__qualname__}",
            "fields": _normalize(asdict(value)),
        }
    if isinstance(value, dict):
        return {str(key): _normalize(item) for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))}
    if isinstance(value, (tuple, list)):
        return [_normalize(item) for item in value]
    return value


def deterministic_json(value: Any) -> str:
    """Canonical JSON retaining type and complex-value identity."""
    return json.dumps(_normalize(value), sort_keys=True, separators=(",", ":"), allow_nan=False)


def serialized_round_trip(value: Any) -> dict[str, Any]:
    """Return the stable record after a JSON encode/decode/encode cycle."""
    encoded = deterministic_json(value)
    decoded = json.loads(encoded)
    assert json.dumps(decoded, sort_keys=True, separators=(",", ":")) == encoded
    return decoded
