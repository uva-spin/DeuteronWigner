"""C92 Route-C audit; deliberately contains no historical reconstruction path."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifboundrestart import load_verified_historical_semantic_attestation

ROOT = Path(__file__).resolve().parents[4]
C90_RUNTIME = ROOT / "data/runtime/c90_ifboundrestart"
STATUS = "C92_IFEQUIVAPI_C90_PAYLOAD_INCOMPLETE"
HISTORICAL_C82 = "8e47231ab565f0f729d335b39aa98881176ba166"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
UNKNOWN_C72 = "UNKNOWN_NOT_CLAIMED"
REQUIRED_PAIR_FIELDS = {
    "normal_form_content", "primitive_family_records", "record_expression_root",
    "coefficient_expression_root", "bound_rule_root", "status_rule_root",
    "ancestry_rule_root", "proof_inputs",
}
REQUIRED_PACKAGE_OBJECTS = {
    "pair_attestation_ledger", "primitive_family_manifest", "primitive_family_records",
    "expansion_theorem_specification", "public_proof_checker_input_schema",
}


def _digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    return value


def audit_existing_c90_payload() -> MappingProxyType:
    """Read only persisted C90 objects; never invoke a C90 compiler or builder."""
    public = load_verified_historical_semantic_attestation()
    payloads: list[dict[str, Any]] = []
    ledgers: list[dict[str, Any]] = []
    for name in ("pass_one", "pass_two", "resume", "parallel"):
        base = C90_RUNTIME / name
        index_path, ledger_path = base / "index.json", base / "ledger.jsonl"
        index = json.loads(index_path.read_text())
        first = json.loads(ledger_path.open().readline())
        fields = set(first)
        payloads.extend([
            {"path": str(index_path.relative_to(ROOT)), "role": "C90 compact runtime index", "schema": index["schema"], "records": 1,
             "size": index_path.stat().st_size, "sha256": _digest(index_path), "covered_by_c90_aggregate": False, "public": False},
            {"path": str(ledger_path.relative_to(ROOT)), "role": "C90 compact pair semantic-root ledger", "schema": index["schema"], "records": index["entries"],
             "size": ledger_path.stat().st_size, "sha256": _digest(ledger_path), "covered_by_c90_aggregate": True, "public": False},
        ])
        ledgers.append({"name": name, "index": index, "fields": sorted(fields), "missing_pair_fields": sorted(REQUIRED_PAIR_FIELDS.difference(fields)),
                        "normal_form_content_persisted": "normal_form" in fields, "proof_inputs_persisted": "proof_inputs" in fields})
    canonical = ledgers[0]
    if any(item["index"]["aggregate"] != canonical["index"]["aggregate"] or item["fields"] != canonical["fields"] for item in ledgers[1:]):
        raise ValueError("C90 deterministic runtime payload disagreement")
    package_present = {"pair_attestation_ledger"}
    missing_objects = sorted(REQUIRED_PACKAGE_OBJECTS.difference(package_present))
    ledger_hashes = {item["sha256"] for item in payloads if item["role"] == "C90 compact pair semantic-root ledger"}
    index_hashes = {item["sha256"] for item in payloads if item["role"] == "C90 compact runtime index"}
    return _freeze({
        "historical_public_aggregate_verified": bool(public["pass"]),
        "historical_aggregate": public["aggregate"],
        "payloads": payloads,
        "canonical_ledger_fields": canonical["fields"],
        "missing_pair_fields": canonical["missing_pair_fields"],
        "missing_package_objects": missing_objects,
        "all_runtime_passes_byte_identical": len(ledger_hashes) == 1 and len(index_hashes) == 1,
        "private_builder_called": False,
        "upstream_scientific_reconstruction_called": False,
        "network_called": False,
    })


def select_packaging_route() -> MappingProxyType:
    audit = audit_existing_c90_payload()
    if audit["missing_pair_fields"] or audit["missing_package_objects"]:
        return _freeze({"route": "C_UNAVAILABLE", "status": STATUS,
                        "reason": "REQUIRED_C90_SCIENTIFIC_OBJECTS_WERE_NOT_PERSISTED_AND_C92_MAY_NOT_RECONSTRUCT_THEM",
                        "missing_pair_fields": audit["missing_pair_fields"], "missing_package_objects": audit["missing_package_objects"]})
    raise RuntimeError("unexpected: positive C92 packaging path is not implemented by this fail-closed audit")
