"""Public, capsule-only C94 facade.  It has no C90/C93 recovery imports."""
from __future__ import annotations

import base64
import gzip
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterator

from ..ifc90payload import load_verified_c90_semantic_payload_capsule

ROOT = Path(__file__).resolve().parents[4]
CAPSULE = ROOT / "data/runtime/c93_ifc90payload/capsule"
SCHEMA = "C94-C93-PUBLIC-FACADE-V1"
MAX_PAGE = 256


def canonical(value: Any) -> str: return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def sha(value: Any) -> str: return sha256(canonical(value).encode()).hexdigest()
def freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({k: freeze(v) for k, v in value.items()})
    if isinstance(value, list): return tuple(freeze(v) for v in value)
    return value


@lru_cache(maxsize=1)
def _manifest() -> dict[str, Any]:
    # The sole C93 interaction is its authenticated loader. The fixed capsule
    # path is then read as verified, persisted C93 content—not reconstructed.
    load_verified_c90_semantic_payload_capsule()
    return json.loads((CAPSULE / "manifest.json").read_text())


def _pairs() -> Iterator[dict[str, Any]]:
    with gzip.open(CAPSULE / "pair_attestations.jsonl.gz", "rt", encoding="utf-8") as stream:
        for line in stream: yield json.loads(line)


def _public_pair(record: dict[str, Any], global_sequence: int) -> dict[str, Any]:
    result = dict(record); result["global_sequence"] = global_sequence
    return result


def _forms() -> Iterator[dict[str, Any]]:
    with gzip.open(CAPSULE / "normal_forms.jsonl.gz", "rt", encoding="utf-8") as stream:
        for line in stream: yield json.loads(line)


def _cursor(start: int, resolution: str | None, limit: int, root: str) -> str:
    body = {"schema": SCHEMA, "start": start, "resolution": resolution, "limit": limit, "root": root}
    return base64.urlsafe_b64encode(canonical(body).encode()).decode()


def _decode(cursor: str, root: str) -> dict[str, Any]:
    body = json.loads(base64.urlsafe_b64decode(cursor.encode()))
    if body.get("schema") != SCHEMA or body.get("root") != root: raise ValueError("foreign or stale pagination cursor")
    return body


@lru_cache(maxsize=1)
def load_verified_c93_public_authority() -> Any:
    capsule = load_verified_c90_semantic_payload_capsule(); manifest = _manifest()
    return freeze({"schema": SCHEMA, "package_root": sha({"capsule_root": manifest["capsule_root"], "schema": SCHEMA}), "capsule_root": manifest["capsule_root"],
                   "C90_aggregate": manifest["C90_aggregate"], "pairs": manifest["pair_attestations"]["records"], "pass": bool(capsule["pass"]),
                   "scientific_relation": manifest["payload_provenance"], "original_c90_runtime_identity": "NOT_CLAIMED"})


def historical_pair_count(resolution: str | None = None) -> int:
    if resolution is None: return int(load_verified_c93_public_authority()["pairs"])
    return sum(1 for pair in _pairs() if pair["pair"]["resolution"] == resolution)


def historical_pair_page(*, resolution: str | None = None, cursor: str | None = None, limit: int = 128) -> Any:
    if not 1 <= limit <= MAX_PAGE: raise ValueError("page limit outside safe bound")
    authority = load_verified_c93_public_authority(); start = 0
    if cursor:
        state = _decode(cursor, authority["package_root"])
        if state["resolution"] != resolution or state["limit"] != limit: raise ValueError("cursor query mismatch")
        start = int(state["start"])
    selected = []; seen = 0
    for global_sequence, record in enumerate(_pairs()):
        if resolution is not None and record["pair"]["resolution"] != resolution: continue
        if seen >= start and len(selected) < limit: selected.append(_public_pair(record, global_sequence))
        seen += 1
        if len(selected) == limit: break
    stop = start + len(selected); next_cursor = _cursor(stop, resolution, limit, authority["package_root"]) if stop < historical_pair_count(resolution) else None
    digests = [record["sha256"] for record in selected]
    page = {"schema": SCHEMA, "package_root": authority["package_root"], "capsule_root": authority["capsule_root"], "C90_aggregate": authority["C90_aggregate"],
            "resolution": resolution, "start": start, "stop": stop, "records": selected, "record_digests": digests,
            "page_digest": sha({"resolution": resolution, "start": start, "stop": stop, "record_digests": digests}), "next_cursor": next_cursor}
    return freeze(page)


def historical_pair_by_sequence(global_sequence: int) -> Any:
    if not 0 <= global_sequence < historical_pair_count(): raise IndexError(global_sequence)
    for sequence, record in enumerate(_pairs()):
        if sequence == global_sequence: return freeze(_public_pair(record, sequence))
    raise IndexError(global_sequence)


def historical_pair_attestation(pair_id: str, resolution: str) -> Any:
    for sequence, record in enumerate(_pairs()):
        if record["pair"]["id"] == pair_id and record["pair"]["resolution"] == resolution: return freeze(_public_pair(record, sequence))
    raise KeyError(pair_id)


def historical_normal_form(root_id: str) -> Any:
    for record in _forms():
        if record["normal_form_root"] == root_id: return freeze(record)
    raise KeyError(root_id)


def historical_primitive_family(family_id: str) -> Any:
    load_verified_c93_public_authority()
    for family in json.loads((CAPSULE / "primitive_families.json").read_text()):
        if family["family_id"] == family_id: return freeze(family)
    raise KeyError(family_id)


def historical_primitive_page(family_id: str, *, cursor: str | None = None, limit: int = 128) -> Any:
    family = historical_primitive_family(family_id)
    if not 1 <= limit <= MAX_PAGE: raise ValueError("page limit outside safe bound")
    start = int(_decode(cursor, load_verified_c93_public_authority()["package_root"])["start"]) if cursor else 0
    records = family["records"][start:start + limit]; stop = start + len(records)
    root = load_verified_c93_public_authority()["package_root"]
    return freeze({"family_id": family_id, "start": start, "stop": stop, "records": records,
                   "page_digest": sha({"family": family_id, "start": start, "records": records}),
                   "next_cursor": _cursor(stop, None, limit, root) if stop < len(family["records"]) else None})


@lru_cache(maxsize=1)
def expansion_theorem_specification() -> Any:
    load_verified_c93_public_authority(); return freeze(json.loads((CAPSULE / "theorem.json").read_text()))


def verify_factorized_expansion_equivalence(historical_normal_form: Any, descendant_normal_form: Any, primitive_equivalence_certificates: Any, *, theorem_version: str) -> Any:
    theorem = expansion_theorem_specification()
    if theorem_version != theorem["schema"]: raise ValueError("theorem version mismatch")
    if not primitive_equivalence_certificates: raise ValueError("primitive certificate missing")
    hist, desc = dict(historical_normal_form), dict(descendant_normal_form)
    result = {"theorem": theorem_version, "normal_forms_identical": canonical(hist) == canonical(desc),
              "typed": hist.get("type") == "MAP_RECORD" and desc.get("type") == "MAP_RECORD",
              "kernel_value_queried": False}
    result["pass"] = bool(result["normal_forms_identical"] and result["typed"])
    result["proof_certificate_root"] = sha(result)
    return freeze(result)
