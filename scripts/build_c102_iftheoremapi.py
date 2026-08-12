#!/usr/bin/env python3
"""Build C102's compact public-checker invocation ledger.

All scientific inputs are obtained through their public C94/C98/C100
surfaces.  The sole C97 result stream is opened only after a C102 invocation
has been frozen, solely as the separate historical-result holdout.
"""
from __future__ import annotations

import argparse
import gzip
from hashlib import sha256
import io
import json
from pathlib import Path
import shutil
from typing import Any, Iterator

from deuteron_wigner.bridge.ifequivapi2 import historical_pair_page
from deuteron_wigner.bridge.ifhistpublic2 import (
    historical_pair_normal_form,
    historical_pair_proof_inputs,
    historical_primitive_record,
)
from deuteron_wigner.bridge.ifprimenum import (
    historical_primitive_domain_manifest,
    historical_primitive_record_page,
)
from deuteron_wigner.bridge.iftheoremapi import (
    factorized_expansion_checker_contract,
    verify_factorized_expansion_equivalence,
    verify_factorized_expansion_invocation,
)
from deuteron_wigner.bridge.iftheoremapi.core import _authority as _build_authority

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/runtime/c102_iftheoremapi"
DOCS = ROOT / "docs/next_level"
SCHEMA = "C102-IFTHEOREMAPI-RUNTIME-V1"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
COUNTS = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}
RESULTS = ROOT / "data/runtime/c97_ifproofinput/capsule"


def plain(value: Any) -> Any:
    if hasattr(value, "items"):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def canonical(value: Any) -> str:
    return json.dumps(plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(value: Any) -> str:
    return sha256(canonical(value).encode()).hexdigest()


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(canonical(value) + "\n")
    temporary.replace(path)


def public_pairs() -> Iterator[dict[str, Any]]:
    """Bounded public C94 pagination; never reaches a C94 private index."""
    cursor = None
    total = 0
    while True:
        page = historical_pair_page(cursor=cursor, limit=256)
        for row in page["records"]:
            total += 1
            yield plain(row)
        cursor = page["next_cursor"]
        if cursor is None:
            break
    if total != sum(COUNTS.values()):
        raise ValueError("C94 public pair pagination census mismatch")


def primitive_certificates() -> tuple[list[dict[str, Any]], str]:
    """Build exact identity-only C100->C98 certificates from public calls."""
    domain = plain(historical_primitive_domain_manifest())
    if domain["family_count"] != 5 or domain["record_count"] != 35:
        raise ValueError("C100 primitive domain census")
    records: list[dict[str, Any]] = []
    cursor = None
    while True:
        page = plain(historical_primitive_record_page(cursor=cursor, limit=7))
        for identity in page["records"]:
            direct = plain(historical_primitive_record(identity["family_id"], identity["record_id"]))
            if direct["record_digest"] != identity["record_digest"] or direct["family_root"] != identity["family_root"] or direct["inclusion"] != identity["inclusion"]:
                raise ValueError("C100/C98 primitive content identity mismatch")
            records.append({
                "family_id": identity["family_id"],
                "record_id": identity["record_id"],
                "record_digest": identity["record_digest"],
                "family_root": identity["family_root"],
                "inclusion": identity["inclusion"],
                "relation": "BYTE_IDENTICAL_SCIENTIFIC_RECORD",
                "C98_return_root": direct["return_root"],
            })
        cursor = page["next_cursor"]
        if cursor is None:
            break
    if len(records) != 35 or len({(row["family_id"], row["record_id"]) for row in records}) != 35:
        raise ValueError("C102 primitive certificate census")
    return records, digest(records)


def _holdout_stream(resolution: str):
    return gzip.open(RESULTS / f"computed_{resolution}.jsonl.gz", "rt", encoding="utf-8")


def deterministic_gzip_writer(path: Path):
    """A fixed-mtime gzip text stream on Python versions lacking gzip.open(mtime)."""
    binary = path.open("wb")
    compressed = gzip.GzipFile(filename="", mode="wb", fileobj=binary, mtime=0)
    return io.TextIOWrapper(compressed, encoding="utf-8"), binary


def run(output: Path, *, checkpoint: int = 512) -> dict[str, Any]:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    # Builder-only source/API attestation.  The persisted public loader is
    # deliberately unavailable until this new package has been closed.
    authority = plain(_build_authority())
    contract = plain(factorized_expansion_checker_contract())
    certificates, certificate_root = primitive_certificates()
    atomic_json(output / "primitive_certificates.json", {
        "schema": "C102-PRIMITIVE-EQUIVALENCE-CERTIFICATES-V1",
        "records": certificates,
        "root": certificate_root,
        "C100_package_root": historical_primitive_domain_manifest()["C100_package_root"],
    })

    streams = {resolution: _holdout_stream(resolution) for resolution in RESOLUTIONS}
    opened = {resolution: deterministic_gzip_writer(output / f"invocations_{resolution}.jsonl.gz.tmp") for resolution in RESOLUTIONS}
    writers = {resolution: item[0] for resolution, item in opened.items()}
    rolling = ""
    resolution_roots = {resolution: "" for resolution in RESOLUTIONS}
    local = {resolution: 0 for resolution in RESOLUTIONS}
    mismatch = {"historical_result": 0, "schema_order": 0, "logical_count": 0, "normal_form": 0}
    calls = successes = 0
    checkpoints: list[dict[str, Any]] = []
    try:
        for pair in public_pairs():
            identity = pair["pair"]
            resolution = identity["resolution"]
            pair_id = identity["id"]
            sequence = int(pair["global_sequence"])
            if sequence != sum(local.values()) or local[resolution] != int(pair.get("resolution_sequence", local[resolution])):
                raise ValueError("public pair ordering mismatch")
            # C98 result-blind public inputs are loaded before the C97 holdout.
            historical = historical_pair_normal_form(pair_id, resolution)
            proof = historical_pair_proof_inputs(pair_id, resolution)
            normal = plain(historical)["normal_form"]
            input_record = plain(proof)["proof_input"]
            if input_record["route_a_normal_form"]["root"] != input_record["route_b_normal_form"]["root"] or input_record["route_b_normal_form"]["root"] != normal["normal_form_root"]:
                raise ValueError("C98 proof-input/normal-form binding mismatch")
            invocation = plain(verify_factorized_expansion_equivalence(
                historical, historical, certificates,
                scientific_schema=input_record["schemas"]["theorem"],
                canonical_order=input_record["logical"]["order_root"],
            ))
            if not verify_factorized_expansion_invocation(invocation)["pass"]:
                raise ValueError("C102 invocation verification failed")
            calls += 1; successes += int(invocation["status"] == "EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF")
            # Only now is the separately persisted historical checker result opened.
            holdout = json.loads(streams[resolution].readline())
            if holdout["pair"]["id"] != pair_id or holdout["pair"]["resolution"] != resolution:
                raise ValueError("C97 historical result order mismatch")
            computed = holdout["computed"]
            equal = bool(computed.get("pass") and invocation["accepted_checker_result"]["pass"])
            mismatch["historical_result"] += int(not equal)
            mismatch["logical_count"] += int(computed.get("cardinality") != normal.get("cardinality"))
            mismatch["normal_form"] += int(computed.get("normal_form_root") != normal.get("normal_form_root"))
            mismatch["schema_order"] += int(invocation["scientific_schema"] != input_record["schemas"]["theorem"])
            compact = {
                "pair": {"id": pair_id, "resolution": resolution, "global_sequence": sequence, "resolution_sequence": local[resolution]},
                "normal_form_root": normal["normal_form_root"],
                "proof_input_root": input_record["proof_input_root"],
                "primitive_equivalence_certificate_root": certificate_root,
                "computed_invocation_certificate_root": invocation["computed_invocation_certificate_root"],
                "accepted_checker_result_root": invocation["accepted_checker_result"]["proof_certificate_root"],
                "status": invocation["status"],
                "historical_proof_certificate_identity": "UNAVAILABLE_NOT_INVENTED",
                "historical_result_semantically_matched": equal,
            }
            writers[resolution].write(canonical(compact) + "\n")
            rolling = digest({"previous": rolling, "entry": compact})
            resolution_roots[resolution] = digest({"previous": resolution_roots[resolution], "entry": compact})
            local[resolution] += 1
            if local[resolution] % checkpoint == 0:
                checkpoints.append({"resolution": resolution, "next_local_sequence": local[resolution], "rolling": rolling, "root": digest({"resolution": resolution, "next": local[resolution], "rolling": rolling})})
    finally:
        for stream in streams.values(): stream.close()
        for writer in writers.values(): writer.close()
        for _, binary in opened.values(): binary.close()
    for resolution in RESOLUTIONS:
        temporary = output / f"invocations_{resolution}.jsonl.gz.tmp"
        final = output / f"invocations_{resolution}.jsonl.gz"
        temporary.replace(final)
        if local[resolution] != COUNTS[resolution]: raise ValueError("resolution invocation census")
    if calls != 154830 or successes != 154830 or any(mismatch.values()):
        raise ValueError(f"C102 self-regression mismatch: {calls=} {successes=} {mismatch=}")
    runtime = []
    for path in sorted(output.iterdir()):
        if path.is_file(): runtime.append({"path": path.name, "bytes": path.stat().st_size, "sha256": file_hash(path)})
    ledger = {
        "schema": SCHEMA,
        "records": calls,
        "resolution_counts": local,
        "invocations": calls,
        "positive": successes,
        "failures": calls - successes,
        "unresolved": 0,
        "historical_result_mismatches": mismatch["historical_result"],
        "historical_certificates_available": 0,
        "historical_certificates_unavailable": calls,
        "mismatches": mismatch,
        "C102_THEOREM_AUTHORITY_ROOT": authority["C102_THEOREM_AUTHORITY_ROOT"],
        "C102_CHECKER_API_ROOT": authority["checker_api_root"],
        "C102_HISTORICAL_SELF_REGRESSION_ROOT": rolling,
        "resolution_roots": resolution_roots,
        "primitive_equivalence_certificate_root": certificate_root,
        "C94_package_root": authority["C94_package_root"],
        "C93_capsule_root": authority["C93_capsule_root"],
        "C90_aggregate": authority["C90_aggregate"],
        "checkpoints": checkpoints,
        "checker_contract_root": contract["contract_root"],
        "proof_result_used_during_invocation_assembly": False,
    }
    atomic_json(output / "ledger.json", ledger)
    runtime = []
    for path in sorted(output.iterdir()):
        if path.is_file(): runtime.append({"path": path.name, "bytes": path.stat().st_size, "sha256": file_hash(path)})
    manifest = {key: value for key, value in ledger.items() if key != "checkpoints"}
    manifest.update({"runtime_inventory": runtime, "no_scientific_content_copy": True, "C102_PACKAGE_ROOT": None})
    manifest["C102_PACKAGE_ROOT"] = digest({key: value for key, value in manifest.items() if key != "C102_PACKAGE_ROOT"})
    atomic_json(output / "manifest.json", manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--checkpoint", type=int, default=512)
    args = parser.parse_args()
    if args.checkpoint < 1: raise SystemExit("checkpoint must be positive")
    print(canonical(run(args.out, checkpoint=args.checkpoint)))


if __name__ == "__main__":
    main()
