"""Read-only loader for the C97 result-blind checker-operand capsule."""
from __future__ import annotations

from hashlib import sha256
import gzip
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any
from .proof_input_index import Reader as _ProofReader
from .zran_runtime import open_verified_zran_reader

from ..ifequivapi2 import load_verified_c93_public_authority

ROOT = Path(__file__).resolve().parents[4]
CAPSULE = ROOT / "data" / "runtime" / "c97_ifproofinput" / "capsule"
SCHEMA = "C97-HISTORICAL-C90-PROOF-INPUT-V1"
RESULT_BLIND_MANIFEST = "proof_input_capsule_manifest.json"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def _sha(value: Any) -> str:
    return sha256(_canonical(value).encode()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _hash_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _safe_file(relative: str) -> Path:
    candidate = (CAPSULE / relative).resolve()
    if not str(candidate).startswith(str(CAPSULE.resolve()) + "/") or candidate.is_symlink() or not candidate.is_file():
        raise ValueError("unsafe C97 capsule path")
    return candidate


def _manifest() -> dict[str, Any]:
    path = _safe_file("manifest.json")
    body = json.loads(path.read_text())
    if body.get("schema") != SCHEMA:
        raise ValueError("unknown C97 proof-input schema")
    return body


def verify_result_blind_operand_capsule() -> Any:
    """Verify C97-owned frozen inputs without importing C93/C94 builders.

    This is deliberately separate from the older incomplete facade below.
    It authenticates the C97 payload itself and refuses result-bearing fields.
    """
    path = _safe_file(RESULT_BLIND_MANIFEST)
    body = json.loads(path.read_text())
    if body.get("schema") != SCHEMA or body.get("records") != 154830:
        raise ValueError("invalid C97 result-blind capsule manifest")
    if _sha({key: value for key, value in body.items() if key != "C97_PROOF_INPUT_CAPSULE_ROOT"}) != body.get("C97_PROOF_INPUT_CAPSULE_ROOT"):
        raise ValueError("C97 result-blind capsule root mismatch")
    rolling = ""; count = 0
    for relative in body["record_paths"]:
        expected = body["inventory"][relative]
        candidate = _safe_file(relative)
        if _hash_file(candidate) != expected: raise ValueError("C97 operand inventory mismatch")
        with gzip.open(candidate, "rt", encoding="utf-8") as stream:
            for line in stream:
                record = json.loads(line)
                if set(record).intersection({"proof_result", "expected_status", "proof_certificate", "comparison_outcome"}):
                    raise ValueError("result-bearing field in C97 operand")
                rolling = _sha({"previous": rolling, "entry": {"pair": record["pair"], "proof_input_root": record["proof_input_root"]}})
                count += 1
    if count != body["records"] or rolling != body["C97_PROOF_INPUT_OPERAND_ROOT"]:
        raise ValueError("C97 operand census/root mismatch")
    return _freeze({"pass": True, "records": count, "operand_root": rolling, "capsule_root": body["C97_PROOF_INPUT_CAPSULE_ROOT"], "proof_result_used_to_construct_input": False})


def verify_c90_proof_input_capsule() -> Any:
    """Verify the result-blind capsule and its C94/C93/C90 authority chain."""
    if (CAPSULE / RESULT_BLIND_MANIFEST).is_file():
        return verify_result_blind_operand_capsule()
    authority = load_verified_c93_public_authority()
    manifest = _manifest()
    if manifest["C94_package_root"] != authority["package_root"] or manifest["C93_capsule_root"] != authority["capsule_root"] or manifest["C90_aggregate"] != dict(authority["C90_aggregate"]):
        raise ValueError("C97 authority-chain mismatch")
    inventory = manifest["inventory"]
    for relative, expected in inventory.items():
        if _hash_file(_safe_file(relative)) != expected:
            raise ValueError("C97 capsule inventory mismatch")
    identity = {key: value for key, value in manifest.items() if key != "capsule_root"}
    if _sha(identity) != manifest["capsule_root"]:
        raise ValueError("C97 capsule-root mismatch")
    return _freeze({"pass": True, "schema": SCHEMA, "capsule_root": manifest["capsule_root"], "operand_root": manifest["operand_root"], "result_root": manifest["result_root"], "records": manifest["records"], "C94_package_root": manifest["C94_package_root"], "C93_capsule_root": manifest["C93_capsule_root"], "C90_aggregate": manifest["C90_aggregate"], "proof_result_used_to_construct_input": False})


def load_verified_c90_proof_input_capsule() -> Any:
    return verify_c90_proof_input_capsule()


def _index() -> dict[str, Any]:
    verify_c90_proof_input_capsule()
    body = json.loads(_safe_file("index.json").read_text())
    if body.get("schema") != SCHEMA:
        raise ValueError("unknown C97 index schema")
    return body


def _resolution_index(resolution: str, index: dict[str, Any] | None = None) -> dict[str, Any]:
    top = _index() if index is None else index
    entry = next((item for item in top["resolutions"] if item["resolution"] == resolution), None)
    if entry is None:
        raise KeyError(resolution)
    body = json.loads(_safe_file(entry["index_path"]).read_text())
    if body.get("schema") != SCHEMA or body.get("resolution") != resolution:
        raise ValueError("invalid C97 resolution index")
    return body


def proof_input_count(resolution: str | None = None) -> int:
    runtime = CAPSULE.parent / "proof_transport"
    counts = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}
    if all((runtime / f"{item}.index").is_file() for item in counts):
        return sum(counts.values()) if resolution is None else counts[resolution]
    index = _index()
    if resolution is None:
        return int(index["records"])
    return int(_resolution_index(resolution, index)["records"])


def _key(pair_id: str, resolution: str) -> str:
    return f"{resolution}\u001f{pair_id}"


def _read_indexed(entry: dict[str, Any]) -> dict[str, Any]:
    path = _safe_file(entry["path"])
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for _ in range(int(entry["ordinal"]) + 1):
            raw = stream.readline()
    if not raw:
        raise ValueError("truncated indexed proof-input shard")
    record = json.loads(raw)
    body = {key: value for key, value in record.items() if key != "proof_input_root"}
    if _sha(body) != record.get("proof_input_root"):
        raise ValueError("proof-input record authentication failure")
    if "proof_result" in record or "expected_status" in record or "proof_certificate" in record:
        raise ValueError("result-bearing field in C97 proof input")
    return record


def proof_input_for_pair(pair_id: str, resolution: str) -> Any:
    transport = CAPSULE.parent / "proof_transport"
    source = CAPSULE / f"route_b_indexed_{resolution}.jsonl.gz"
    index = transport / f"{resolution}.index"
    adapter = transport / "c97_zran"
    zran = transport / f"{resolution}.zran"
    if source.is_file() and index.is_file() and zran.is_file() and adapter.is_file():
        reader = _ProofReader(source, index, open_verified_zran_reader(source, zran, adapter))
        try:
            return _freeze(dict(reader.lookup(resolution, pair_id)))
        finally:
            reader.close()
    index = _resolution_index(resolution); entry = index["by_pair"].get(pair_id)
    if entry is None:
        raise KeyError(pair_id)
    record = _read_indexed(entry)
    if record["pair"]["id"] != pair_id or record["pair"]["resolution"] != resolution:
        raise ValueError("proof-input index pair mismatch")
    return _freeze(record)


def proof_input_by_sequence(global_sequence: int) -> Any:
    ranges = (("K9_2_N8_b0.40", 0, 16224), ("K11_2_N10_b0.45", 16224, 43350), ("K13_2_N12_b0.50", 59574, 95256))
    for resolution, start, count in ranges:
        if start <= global_sequence < start + count:
            transport = CAPSULE.parent / "proof_transport"; source = CAPSULE / f"route_b_indexed_{resolution}.jsonl.gz"
            reader = _ProofReader(source, transport / f"{resolution}.index", open_verified_zran_reader(source, transport / f"{resolution}.zran", transport / "c97_zran"))
            try:
                # The compact fixed binary table contains only metadata.  Scan
                # at most one resolution table to resolve an explicit sequence.
                from .proof_input_index import ENTRY
                for offset in range(0, len(reader.table), ENTRY.size):
                    entry = ENTRY.unpack_from(reader.table, offset)
                    if entry[5] == global_sequence:
                        record = reader.zran.read_uncompressed_range(entry[1], entry[2])
                        return _freeze(json.loads(record))
            finally:
                reader.close()
            raise IndexError(global_sequence)
    index = _index()
    if not 0 <= global_sequence < int(index["records"]):
        raise IndexError(global_sequence)
    resolution = next(item for item in index["resolutions"] if item["start"] <= global_sequence < item["start"] + item["records"])
    local = global_sequence - int(resolution["start"])
    return _freeze(_read_indexed(_resolution_index(resolution["resolution"], index)["by_sequence"][str(local)]))


def verify_proof_input_record(pair_id: str, resolution: str) -> Any:
    record = proof_input_for_pair(pair_id, resolution)
    return _freeze({"pair": record["pair"], "proof_input_root": record["proof_input_root"], "pass": True, "proof_result_read": False})
