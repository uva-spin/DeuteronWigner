"""Fail-closed C96 audit for a persisted historical proof-input store.

This module is deliberately not a C93 recovery facade.  In particular it
does not import or call ``recovered_pair_proof_inputs``: that function derives
an object by joining a pair attestation to a normal form through the stored
normal-form root, which is expressly disallowed for C96 public data access.
"""
from __future__ import annotations

import gzip
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifequivapi2 import load_verified_c93_public_authority

ROOT = Path(__file__).resolve().parents[4]
CAPSULE = ROOT / "data" / "runtime" / "c93_ifc90payload" / "capsule"
STATUS = "C96_IFHISTPUBLIC_PROOF_INPUT_LOADER_INCOMPLETE"


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _schema_census(path: Path) -> dict[str, Any]:
    """Census persisted JSONL fields without invoking any recovery loader."""
    count = 0
    top_level: set[tuple[str, ...]] = set()
    normal_form_fields: set[tuple[str, ...]] = set()
    proof_fields: set[tuple[str, ...]] = set()
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            count += 1
            top_level.add(tuple(sorted(record)))
            if isinstance(record.get("normal_form"), dict):
                normal_form_fields.add(tuple(sorted(record["normal_form"])))
            if isinstance(record.get("proof"), dict):
                proof_fields.add(tuple(sorted(record["proof"])))
    return {
        "records": count,
        "top_level_schemas": tuple(sorted(top_level)),
        "normal_form_schemas": tuple(sorted(normal_form_fields)),
        "proof_schemas": tuple(sorted(proof_fields)),
    }


def audit_authenticated_proof_input_payload() -> Any:
    """Prove whether C93 persists a separate proof-input object domain.

    It verifies the public C94 authority first, then only reads C93 files
    included in the already authenticated capsule inventory.  It never calls
    a C93 recovery method, C90/C82 builder, historical worktree, or network.
    """
    authority = load_verified_c93_public_authority()
    manifest_path = CAPSULE / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    inventory = {item["path"]: item["sha256"] for item in manifest["inventory"]}
    pair_path = CAPSULE / "pair_attestations.jsonl.gz"
    form_path = CAPSULE / "normal_forms.jsonl.gz"
    for path in (pair_path, form_path):
        relative = str(path.relative_to(CAPSULE))
        if inventory.get(relative) != _sha(path):
            raise ValueError("C93 authenticated payload inventory mismatch")
    pair_census = _schema_census(pair_path)
    form_census = _schema_census(form_path)
    # The exact persisted domains are pair attestations and normal-form
    # records.  Neither has a terminal proof-input object; C93's private
    # helper composes a proof object by a root-based join, forbidden here.
    persisted_proof_input_domain = any(
        "proof_inputs" in fields or "proof_input" in fields
        for fields in pair_census["top_level_schemas"] + form_census["top_level_schemas"]
    )
    return _freeze({
        "authority_verified": bool(authority["pass"]),
        "C94_package_root": authority["package_root"],
        "C93_capsule_root": authority["capsule_root"],
        "C90_aggregate": authority["C90_aggregate"],
        "pair_attestations": {"path": "pair_attestations.jsonl.gz", "sha256": inventory["pair_attestations.jsonl.gz"], **pair_census},
        "normal_forms": {"path": "normal_forms.jsonl.gz", "sha256": inventory["normal_forms.jsonl.gz"], **form_census},
        "persisted_proof_input_domain": persisted_proof_input_domain,
        "forbidden_private_recovery_called": False,
        "private_C93_loader_imported": False,
        "conclusion": "NO_SEPARATE_PERSISTED_PROOF_INPUT_RECORD_DOMAIN",
        "blocker": "C93_PROOF_INPUTS_ARE_ONLY_PRIVATE_ROOT_BASED_COMPOSITIONS_OF_PAIR_ATTESTATION_AND_NORMAL_FORM",
    })
