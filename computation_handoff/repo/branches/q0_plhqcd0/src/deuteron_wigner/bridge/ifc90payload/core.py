"""Read-only loader for the C93 descendant recovered-preimage capsule."""
from __future__ import annotations

import gzip
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
CAPSULE = ROOT / "data/runtime/c93_ifc90payload/capsule"


def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    return value


def _sha(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()


def _manifest() -> dict[str, Any]:
    return json.loads((CAPSULE / "manifest.json").read_text())


def verify_c90_semantic_payload_capsule() -> MappingProxyType:
    manifest = _manifest()
    for record in manifest["inventory"]:
        path = CAPSULE / record["path"]
        if not path.is_file() or path.is_symlink() or _sha(path) != record["sha256"]:
            raise ValueError("C93 capsule inventory verification failure")
    return _freeze({"root": manifest["capsule_root"], "C90_aggregate": manifest["C90_aggregate"], "pass": True,
                    "original_c90_runtime_identity": "NOT_CLAIMED", "builder_called": False})


def load_verified_c90_semantic_payload_capsule() -> MappingProxyType:
    return verify_c90_semantic_payload_capsule()


def _find_gzip(name: str, predicate):
    verify_c90_semantic_payload_capsule()
    with gzip.open(CAPSULE / name, "rt", encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            if predicate(record): return _freeze(record)
    raise KeyError("recovered capsule record")


def recovered_pair_binding(pair_id: str, resolution: str) -> Any:
    return _find_gzip("pair_attestations.jsonl.gz", lambda item: item["pair"]["id"] == pair_id and item["pair"]["resolution"] == resolution)


def recovered_normal_form(root_id: str) -> Any:
    return _find_gzip("normal_forms.jsonl.gz", lambda item: item["normal_form_root"] == root_id)


def recovered_pair_proof_inputs(pair_id: str, resolution: str) -> Any:
    binding = recovered_pair_binding(pair_id, resolution)
    normal = recovered_normal_form(binding["normal_form_root"])
    return _freeze({"pair": binding["pair"], "normal_form": normal["normal_form"], "primitive_roots": normal["normal_form"]["primitive_roots"],
                    "proof": binding["proof"], "C90_aggregate": verify_c90_semantic_payload_capsule()["C90_aggregate"]})


def recovered_primitive_family(family_id: str) -> Any:
    verify_c90_semantic_payload_capsule()
    families = json.loads((CAPSULE / "primitive_families.json").read_text())
    for family in families:
        if family["family_id"] == family_id: return _freeze(family)
    raise KeyError(family_id)


def recovered_theorem_specification() -> Any:
    verify_c90_semantic_payload_capsule()
    return _freeze(json.loads((CAPSULE / "theorem.json").read_text()))
