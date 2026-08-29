"""Immutable C102 adapter over the accepted public C94 checker.

This module intentionally contains no semantic-program normalizer or theorem
implementation.  Every equivalence decision is delegated exactly once to
``ifequivapi2.verify_factorized_expansion_equivalence``.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
import inspect
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifequivapi2 import (
    expansion_theorem_specification as _accepted_theorem_specification,
    load_verified_c93_public_authority as _accepted_authority,
    verify_factorized_expansion_equivalence as _accepted_checker,
)

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c102_iftheoremapi"
SCHEMA = "C102-IFTHEOREMAPI-V1"
INVOCATION_SCHEMA = "C102-FACTORIZED-SEMANTIC-CHECKER-INVOCATION-V1"
POSITIVE_STATUS = "EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF"


def _plain(value: Any) -> Any:
    if hasattr(value, "items"):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(item) for item in value]
    return value


def _canonical(value: Any) -> str:
    return json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def _sha(value: Any) -> str:
    return sha256(_canonical(value).encode("utf-8")).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({str(key): _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _source_hash(callable_object: Any) -> tuple[str, str]:
    path = Path(inspect.getsourcefile(callable_object) or "")
    if not path.is_file():
        raise RuntimeError("accepted C94 checker source unavailable")
    return str(path.relative_to(ROOT)), sha256(path.read_bytes()).hexdigest()


def _safe_runtime(path: Path) -> Path:
    candidate = path.resolve()
    root = RUNTIME.resolve()
    if not str(candidate).startswith(str(root) + "/") or candidate.is_symlink() or not candidate.is_file():
        raise ValueError("unsafe C102 runtime path")
    return candidate


@lru_cache(maxsize=1)
def _runtime_manifest() -> dict[str, Any]:
    path = _safe_runtime(RUNTIME / "manifest.json")
    body = json.loads(path.read_text())
    root = body.get("C102_PACKAGE_ROOT")
    if body.get("schema") != "C102-IFTHEOREMAPI-RUNTIME-V1" or not isinstance(root, str):
        raise ValueError("unknown C102 runtime manifest")
    if _sha({key: value for key, value in body.items() if key != "C102_PACKAGE_ROOT"}) != root:
        raise ValueError("C102 package root mismatch")
    inventory = body.get("runtime_inventory")
    if not isinstance(inventory, list) or not inventory:
        raise ValueError("C102 runtime inventory missing")
    for item in inventory:
        if set(item) != {"path", "bytes", "sha256"}:
            raise ValueError("C102 runtime inventory schema")
        candidate = _safe_runtime(RUNTIME / item["path"])
        if candidate.stat().st_size != item["bytes"] or sha256(candidate.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("C102 runtime inventory mismatch")
    return body


def _api_root() -> str:
    signature = str(inspect.signature(_accepted_checker))
    source_path, source_sha256 = _source_hash(_accepted_checker)
    return _sha({
        "import_path": "deuteron_wigner.bridge.ifequivapi2.verify_factorized_expansion_equivalence",
        "signature": signature,
        "source_path": source_path,
        "source_sha256": source_sha256,
        "theorem_public_import": "deuteron_wigner.bridge.ifequivapi2.expansion_theorem_specification",
    })


@lru_cache(maxsize=1)
def _authority() -> dict[str, Any]:
    accepted = _plain(_accepted_authority())
    theorem = _plain(_accepted_theorem_specification())
    source_path, source_sha256 = _source_hash(_accepted_checker)
    if accepted.get("schema") != "C94-C93-PUBLIC-FACADE-V1":
        raise ValueError("unknown C94 public authority schema")
    if theorem.get("schema") != "C90-C82-SEMANTIC-IR-V1":
        raise ValueError("unknown accepted theorem schema")
    body = {
        "schema": SCHEMA,
        "C94_package_root": accepted["package_root"],
        "C93_capsule_root": accepted["capsule_root"],
        "C90_aggregate": accepted["C90_aggregate"],
        "theorem": theorem,
        "theorem_root": _sha(theorem),
        "checker_import_path": "deuteron_wigner.bridge.ifequivapi2.verify_factorized_expansion_equivalence",
        "checker_signature": str(inspect.signature(_accepted_checker)),
        "checker_source_path": source_path,
        "checker_source_sha256": source_sha256,
        "checker_api_root": _api_root(),
        "normal_form_schema": theorem["normal_form"],
        "scientific_schema": theorem["schema"],
        "diagnostic_vocabulary": ["pass", "normal_forms_identical", "typed", "kernel_value_queried"],
        "no_local_theorem": True,
        "no_local_normalizer": True,
    }
    body["C102_THEOREM_AUTHORITY_ROOT"] = _sha(body)
    return body


def load_verified_factorized_semantic_theorem_authority() -> Any:
    """Load the C94 public theorem/checker authority without private payload access."""
    authority = _authority(); runtime = _runtime_manifest()
    for key in ("C102_THEOREM_AUTHORITY_ROOT", "C102_CHECKER_API_ROOT", "C94_package_root", "C93_capsule_root", "C90_aggregate"):
        expected = authority["checker_api_root"] if key == "C102_CHECKER_API_ROOT" else authority[key]
        if runtime.get(key) != expected:
            raise ValueError("C102 persisted/public authority mismatch")
    return _freeze({**authority, "C102_PACKAGE_ROOT": runtime["C102_PACKAGE_ROOT"], "C102_HISTORICAL_SELF_REGRESSION_ROOT": runtime["C102_HISTORICAL_SELF_REGRESSION_ROOT"]})


def verify_factorized_semantic_theorem_authority() -> Any:
    authority = _authority()
    if authority["C102_THEOREM_AUTHORITY_ROOT"] != _sha({key: value for key, value in authority.items() if key != "C102_THEOREM_AUTHORITY_ROOT"}):
        raise ValueError("C102 theorem authority root mismatch")
    # The accepted public authority is deliberately called again: this is a
    # source/API identity verification, not a builder or reconstruction path.
    accepted = _plain(_accepted_authority())
    if accepted["package_root"] != authority["C94_package_root"]:
        raise ValueError("C94 package root changed")
    return _freeze({"pass": True, **authority})


def factorized_expansion_theorem_specification() -> Any:
    authority = _authority()
    return _freeze({
        "schema": "C102-PUBLIC-THEOREM-SPECIFICATION-V1",
        "theorem": authority["theorem"],
        "theorem_root": authority["theorem_root"],
        "C94_package_root": authority["C94_package_root"],
        "C102_THEOREM_AUTHORITY_ROOT": authority["C102_THEOREM_AUTHORITY_ROOT"],
    })


def factorized_expansion_checker_contract() -> Any:
    authority = _authority()
    body = {
        "schema": "C102-PUBLIC-CHECKER-CONTRACT-V1",
        "accepted_import_path": authority["checker_import_path"],
        "accepted_signature": authority["checker_signature"],
        "accepted_source_path": authority["checker_source_path"],
        "accepted_source_sha256": authority["checker_source_sha256"],
        "accepted_checker_api_root": authority["checker_api_root"],
        "theorem_root": authority["theorem_root"],
        "input_schema": INVOCATION_SCHEMA,
        "accepted_input": {
            "historical_normal_form": authority["normal_form_schema"],
            "descendant_normal_form": authority["normal_form_schema"],
            "primitive_equivalence_certificates": "nonempty immutable sequence",
            "theorem_version": authority["scientific_schema"],
        },
        "accepted_output": {
            "fields": authority["diagnostic_vocabulary"] + ["proof_certificate_root"],
            "positive_status": POSITIVE_STATUS,
        },
        "no_reimplementation": True,
    }
    body["contract_root"] = _sha(body)
    return _freeze(body)


def _program(value: Any, *, label: str) -> dict[str, Any]:
    raw = _plain(value)
    # A C98 return wrapper has a ``normal_form`` mapping.  A C90 MAP_RECORD
    # itself also has a scalar ``normal_form`` schema field, so identify the
    # typed node before unwrapping.
    program = raw if raw.get("type") == "MAP_RECORD" else raw.get("normal_form", raw)
    if not isinstance(program, dict) or program.get("type") != "MAP_RECORD":
        raise ValueError(f"{label} is not an accepted typed normal form")
    if program.get("normal_form_root") != _sha({key: value for key, value in program.items() if key != "normal_form_root"}):
        # C90 normal-form roots have project-specific construction; their
        # authenticated source is checked by C98/C94.  Do not substitute a
        # local root algorithm here.
        if "normal_form_root" not in program:
            raise ValueError(f"{label} lacks normal-form identity")
    return program


def _certificate_root(certificates: Any) -> str:
    rows = _plain(certificates)
    if not isinstance(rows, list) or not rows:
        raise ValueError("primitive-equivalence certificate sequence required")
    for row in rows:
        if not isinstance(row, dict) or not row.get("family_id") or not row.get("record_id"):
            raise ValueError("invalid primitive-equivalence certificate")
        if row.get("relation") not in {
            "BYTE_IDENTICAL_SCIENTIFIC_RECORD",
            "CANONICALLY_IDENTICAL_SCIENTIFIC_RECORD",
            "SCIENTIFICALLY_IDENTICAL_WITH_EXPLICIT_ADAPTER",
            "INSTANCE_ONLY_DIFFERENCE",
        }:
            raise ValueError("unknown primitive-equivalence relation")
    return _sha(rows)


def verify_factorized_expansion_equivalence(
    historical_program: Any,
    descendant_program: Any,
    primitive_equivalence_certificates: Any,
    *,
    scientific_schema: str,
    canonical_order: str,
) -> Any:
    """Delegate exactly once to the accepted public C94 checker.

    ``canonical_order`` is an authenticated caller identity; C94 itself owns
    the theorem semantics.  It is recorded but never used to decide pass/fail.
    """
    authority = _authority()
    if scientific_schema != authority["scientific_schema"]:
        raise ValueError("scientific schema mismatch")
    if not isinstance(canonical_order, str) or len(canonical_order) != 64:
        raise ValueError("canonical order root must be a SHA-256 identity")
    historical = _program(historical_program, label="historical program")
    descendant = _program(descendant_program, label="comparison program")
    certificates = _plain(primitive_equivalence_certificates)
    certificate_root = _certificate_root(certificates)
    # This is the sole semantic theorem invocation in C102.  No local result
    # is used as a fallback if it raises or is unavailable.
    accepted = _plain(_accepted_checker(
        historical,
        descendant,
        certificates,
        theorem_version=authority["scientific_schema"],
    ))
    if set(accepted) != {"theorem", "normal_forms_identical", "typed", "kernel_value_queried", "pass", "proof_certificate_root"}:
        raise ValueError("accepted C94 checker output schema changed")
    status = POSITIVE_STATUS if accepted["pass"] else "C94_PUBLIC_CHECKER_NONPOSITIVE"
    invocation = {
        "schema": INVOCATION_SCHEMA,
        "status": status,
        "historical_program_root": historical["normal_form_root"],
        "comparison_program_root": descendant["normal_form_root"],
        "primitive_equivalence_certificate_root": certificate_root,
        "scientific_schema": scientific_schema,
        "canonical_order": canonical_order,
        "theorem_root": authority["theorem_root"],
        "checker_source_sha256": authority["checker_source_sha256"],
        "checker_api_root": authority["checker_api_root"],
        "exact_logical_cardinality": historical.get("logical_count"),
        "accepted_checker_result": accepted,
        "diagnostic_category": "C94_PUBLIC_CHECKER_OUTPUT",
        "historical_proof_certificate_identity": "UNAVAILABLE_NOT_INVENTED",
    }
    invocation["computed_invocation_certificate_root"] = _sha(invocation)
    return _freeze(invocation)


def verify_factorized_expansion_invocation(invocation_certificate: Any) -> Any:
    """Verify a C102 wrapper certificate without replaying or replacing C94."""
    record = _plain(invocation_certificate)
    if record.get("schema") != INVOCATION_SCHEMA:
        raise ValueError("unknown invocation schema")
    root = record.pop("computed_invocation_certificate_root", None)
    if not isinstance(root, str) or _sha(record) != root:
        raise ValueError("invocation certificate root mismatch")
    authority = _authority()
    for key in ("theorem_root", "checker_source_sha256", "checker_api_root"):
        expected = authority[{"theorem_root": "theorem_root", "checker_source_sha256": "checker_source_sha256", "checker_api_root": "checker_api_root"}[key]]
        if record[key] != expected:
            raise ValueError("invocation authority mismatch")
    accepted = record.get("accepted_checker_result", {})
    if accepted.get("pass") != (record.get("status") == POSITIVE_STATUS):
        raise ValueError("invocation status/result mismatch")
    return _freeze({"pass": True, "computed_invocation_certificate_root": root, "status": record["status"]})
