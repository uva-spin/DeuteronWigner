"""Read-only C100 primitive enumeration API.

The loader deliberately reads only C100's authenticated enumeration records
and calls C98's *public* content method when a caller independently wants to
verify a record.  It never opens C98's direct-location index.
"""
from __future__ import annotations

import base64
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifhistpublic2 import historical_primitive_record

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c100_ifprimenum"
SCHEMA = "C100-PRIMITIVE-ENUMERATION-V1"
PAGE_SCHEMA = "C100-PRIMITIVE-RECORD-PAGE-V1"
FAMILY_ORDER = ("C77", "C78", "C80", "C82", "C87")


def _plain(value: Any) -> Any:
    if hasattr(value, "items"): return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(item) for item in value]
    return value

def _canonical(value: Any) -> str: return json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def _sha(value: Any) -> str: return sha256(_canonical(value).encode()).hexdigest()
def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    return value

def _safe(path: Path) -> Path:
    candidate = path.resolve(); root = RUNTIME.resolve()
    if not str(candidate).startswith(str(root) + "/") or candidate.is_symlink() or not candidate.is_file(): raise ValueError("unsafe C100 runtime path")
    return candidate

@lru_cache(maxsize=1)
def _manifest() -> dict[str, Any]:
    body = json.loads(_safe(RUNTIME / "manifest.json").read_text())
    if body.get("schema") != SCHEMA or _sha({key: value for key, value in body.items() if key != "package_root"}) != body.get("package_root"):
        raise ValueError("C100 package-root mismatch")
    return body

@lru_cache(maxsize=1)
def _domain() -> dict[str, Any]:
    body = json.loads(_safe(RUNTIME / "domain.json").read_text())
    manifest = _manifest()
    if sha256(_safe(RUNTIME / "domain.json").read_bytes()).hexdigest() != manifest["runtime_inventory"][0]["sha256"]: raise ValueError("C100 domain file hash mismatch")
    if body.get("schema") != SCHEMA or _sha({key: value for key, value in body.items() if key != "enumeration_root"}) != body.get("enumeration_root") or body["enumeration_root"] != manifest["enumeration_root"]:
        raise ValueError("C100 primitive domain mismatch")
    records = body.get("records", [])
    if len(records) != 35 or len({(r["family_id"], r["record_id"]) for r in records}) != 35: raise ValueError("C100 primitive domain census")
    if tuple(f["family_id"] for f in body["families"]) != FAMILY_ORDER: raise ValueError("C100 family order")
    if [r["global_sequence"] for r in records] != list(range(35)): raise ValueError("C100 global ordering")
    for family in body["families"]:
        rows = [r for r in records if r["family_id"] == family["family_id"]]
        if len(rows) != family["count"] or [r["family_sequence"] for r in rows] != list(range(len(rows))): raise ValueError("C100 family ordering")
    return body

def _cursor(payload: dict[str, Any]) -> str:
    raw = _canonical(payload).encode(); return base64.urlsafe_b64encode(raw).decode().rstrip("=") + "." + _sha(payload)

def _decode_cursor(value: str, *, family_id: str | None, limit: int, package_root: str, c98_root: str) -> int:
    try:
        encoded, digest = value.rsplit(".", 1); raw = base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4)); payload = json.loads(raw)
    except Exception as exc: raise ValueError("invalid C100 cursor") from exc
    expected = {"schema": PAGE_SCHEMA, "package_root": package_root, "C98_package_root": c98_root, "family_id": family_id, "limit": limit, "next": payload.get("next")}
    if payload != expected or _sha(payload) != digest or not isinstance(payload["next"], int): raise ValueError("C100 cursor authentication mismatch")
    return payload["next"]

def historical_primitive_domain_manifest() -> Any:
    """Return the immutable, metadata-only canonical primitive domain."""
    domain = _domain(); manifest = _manifest()
    body = {"schema": SCHEMA, "family_order": [f["family_id"] for f in domain["families"]], "family_count": len(domain["families"]), "record_count": len(domain["records"]), "families": domain["families"], "aggregate_primitive_identity_root": domain["enumeration_root"], "C98_package_root": manifest["C98_package_root"], "C94_package_root": manifest["C94_package_root"], "C100_package_root": manifest["package_root"], "no_scientific_content_copy": True}
    body["return_root"] = _sha(body); return _freeze(body)

def historical_primitive_record_page(*, family_id: str | None = None, cursor: str | None = None, limit: int = 16) -> Any:
    """Return one root-bound page of primitive identity/location metadata."""
    if family_id is not None and family_id not in FAMILY_ORDER: raise KeyError(family_id)
    if not isinstance(limit, int) or not 1 <= limit <= 64: raise ValueError("unsafe page size")
    domain = _domain(); manifest = _manifest()
    rows = [row for row in domain["records"] if family_id is None or row["family_id"] == family_id]
    start = 0 if cursor is None else _decode_cursor(cursor, family_id=family_id, limit=limit, package_root=manifest["package_root"], c98_root=manifest["C98_package_root"])
    if not 0 <= start <= len(rows): raise ValueError("cursor sequence out of range")
    selected = rows[start:start + limit]; next_cursor = None
    if start + len(selected) < len(rows):
        next_cursor = _cursor({"schema": PAGE_SCHEMA, "package_root": manifest["package_root"], "C98_package_root": manifest["C98_package_root"], "family_id": family_id, "limit": limit, "next": start + len(selected)})
    body = {"schema": PAGE_SCHEMA, "family_id": family_id, "limit": limit, "records": selected, "next_cursor": next_cursor, "terminal": next_cursor is None, "C100_package_root": manifest["package_root"], "C98_package_root": manifest["C98_package_root"], "page_digest": _sha({"family_id": family_id, "start": start, "limit": limit, "records": selected, "next_cursor": next_cursor})}
    return _freeze(body)

def verify_enumerated_primitive_directly(family_id: str, record_id: str) -> Any:
    """Public cross-check: C100 identity metadata against C98 public content."""
    domain = _domain(); row = next((r for r in domain["records"] if r["family_id"] == family_id and r["record_id"] == record_id), None)
    if row is None: raise KeyError(record_id)
    record = historical_primitive_record(family_id, record_id)
    if record["record_digest"] != row["record_digest"] or record["inclusion"] != row["inclusion"] or record["family_root"] != row["family_root"]: raise ValueError("C100/C98 primitive direct mismatch")
    return record
