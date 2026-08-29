"""Deterministic serialization for C35/S0C architecture records.

The helpers in this module deliberately reject ambiguous or non-finite values.
They are small enough to be audited and do not depend on the historical C35
compatibility implementation in :mod:`deuteron_wigner.bridge.s0c.core`.
"""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from enum import Enum
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Mapping


def canonical_value(value: Any) -> Any:
    """Return a JSON-compatible, type-preserving canonical value.

    Sets and arbitrary iterators are intentionally unsupported: their ordering
    is not an admissible part of a scientific identity.
    """

    if is_dataclass(value) and not isinstance(value, type):
        return {
            field.name: canonical_value(getattr(value, field.name))
            for field in fields(value)
        }
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if isinstance(value, complex):
        return {"real": canonical_value(value.real), "imag": canonical_value(value.imag)}
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, Mapping):
        if not all(isinstance(key, str) for key in value):
            raise TypeError("canonical mappings require string keys")
        return {
            key: canonical_value(value[key])
            for key in sorted(value)
        }
    if isinstance(value, (tuple, list)):
        return [canonical_value(item) for item in value]
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("non-finite floats cannot enter a content address")
        # Erase the otherwise observable -0.0 spelling.
        return 0.0 if value == 0.0 else value
    if value is None or isinstance(value, (str, int, bool)):
        return value
    raise TypeError(f"unsupported canonical value: {type(value).__name__}")


def deterministic_json(value: Any) -> str:
    """Serialize *value* with stable ordering and separators."""

    return json.dumps(
        canonical_value(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def content_hash(value: Any) -> str:
    """Return the SHA-256 content address of *value*."""

    return hashlib.sha256(deterministic_json(value).encode("utf-8")).hexdigest()


class ContentAddressed:
    """Mixin providing deterministic serialization to frozen records."""

    def to_canonical_dict(self) -> dict[str, Any]:
        value = canonical_value(self)
        if not isinstance(value, dict):  # pragma: no cover - defensive
            raise TypeError("content-addressed records must serialize as objects")
        return value

    def to_deterministic_json(self) -> str:
        return deterministic_json(self)

    @property
    def sha256(self) -> str:
        return content_hash(self)


__all__ = [
    "ContentAddressed",
    "canonical_value",
    "content_hash",
    "deterministic_json",
]
