"""Bounded fixed-endian index for the sole C93 normal-form gzip payload.

The table deliberately stores only transport metadata.  It never persists a
decoded normal-form JSON object, proof result, or certificate.
"""
from __future__ import annotations

from dataclasses import dataclass
import gzip
from hashlib import sha256
import heapq
import json
from pathlib import Path
import resource
import struct
import tempfile
import time
from types import MappingProxyType
from typing import Any, Iterator

from .zran_runtime import PersistentZranReader, _sha_file

MAGIC = b"C97NFKI1"
SCHEMA = "C97-NORMAL-FORM-KEY-INDEX-V1"
HEADER = 336
ENTRY = struct.Struct(">32sQI32s32sQIB3x")
COUNTS = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}
CODE = {resolution: ordinal for ordinal, resolution in enumerate(COUNTS)}
DECODE = {value: key for key, value in CODE.items()}

def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()

def _root(value: Any) -> str: return sha256(canonical(value)).hexdigest()
def _digest_key(key: dict[str, str]) -> bytes: return sha256(b"C93_NORMAL_FORM\0" + canonical(key)).digest()

def canonical_key(*, resolution: str, pair_id: str, normal_form_root: str) -> dict[str, str]:
    if resolution not in CODE or not pair_id or len(normal_form_root) != 64: raise ValueError("invalid normal-form scientific identity")
    return {"domain": "C93_NORMAL_FORM", "key_schema": "C97-NF-KEY-V1", "resolution": resolution, "pair_id": pair_id, "normal_form_root": normal_form_root}

def _source_record(raw: bytes, global_sequence: int, offset: int) -> tuple[bytes, dict[str, Any], bytes]:
    if not raw.endswith(b"\n"): raise ValueError("invalid JSONL boundary")
    outer = json.loads(raw)
    if set(outer) != {"normal_form", "normal_form_root", "pair", "proof"}: raise ValueError("unexpected C93 wrapper schema")
    node = outer["normal_form"]; pair = node["pair"]
    if outer["normal_form_root"] != node["normal_form_root"] or outer["pair"] != pair: raise ValueError("C93 wrapper identity mismatch")
    if pair["resolution"] not in CODE or pair["sequence"] < 0: raise ValueError("invalid pair identity")
    key = canonical_key(resolution=pair["resolution"], pair_id=pair["id"], normal_form_root=node["normal_form_root"])
    entry = ENTRY.pack(_digest_key(key), offset, len(raw), sha256(raw).digest(), bytes.fromhex(node["normal_form_root"]), global_sequence, int(pair["sequence"]), CODE[pair["resolution"]])
    return entry, node, canonical(key)

def _write_header(*, path: Path, count: int, source: Path, zran_manifest: MappingProxyType, table_sha: bytes, c93_root: str, c94_root: str) -> None:
    source_sha = bytes.fromhex(_sha_file(source)); transport_root = bytes.fromhex(zran_manifest["root"])
    serializer_sha = sha256(canonical({"schema": "C97-NF-KEY-V1", "serializer": "canonical-json-v1"})).digest()
    raw = bytearray(HEADER); raw[:8] = MAGIC
    struct.pack_into(">IIIIQQQQQQQ", raw, 8, 1, 0x01020304, ENTRY.size, 0, count, COUNTS["K9_2_N8_b0.40"], COUNTS["K11_2_N10_b0.45"], COUNTS["K13_2_N12_b0.50"], source.stat().st_size, int(zran_manifest["decoded_bytes"]), 0)
    raw[80:112] = source_sha; raw[112:144] = bytes.fromhex(zran_manifest["decoded_sha256"]); raw[144:176] = bytes.fromhex(zran_manifest["index_sha256"]); raw[176:208] = transport_root; raw[208:240] = serializer_sha; raw[240:272] = table_sha; raw[272:304] = bytes.fromhex(c93_root); raw[304:336] = bytes.fromhex(c94_root)
    path.write_bytes(raw)

def build_normal_form_key_index(source_gzip: Path, output_index: Path, zran_manifest: MappingProxyType, *, c93_root: str, c94_root: str, run_records: int = 4096) -> MappingProxyType:
    """Single streaming decode plus bounded run sort and k-way merge."""
    if run_records < 32: raise ValueError("unsafe run size")
    started = time.monotonic(); output_index.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="c97-nf-index-", dir=output_index.parent) as workspace:
        runs: list[Path] = []; batch: list[bytes] = []; counts = {key: 0 for key in COUNTS}; offset = 0; total = 0; max_line = 0
        def close_run() -> None:
            if not batch: return
            batch.sort(key=lambda item: item[:32]); target = Path(workspace) / f"run-{len(runs):05d}.bin"
            with target.open("wb") as out:
                for item in batch: out.write(item)
            runs.append(target); batch.clear()
        with gzip.open(source_gzip, "rb") as source:
            for raw in source:
                entry, node, _ = _source_record(raw, total, offset)
                counts[node["pair"]["resolution"]] += 1; batch.append(entry); offset += len(raw); total += 1; max_line = max(max_line, len(raw))
                if len(batch) == run_records: close_run()
        close_run()
        if total != sum(COUNTS.values()) or counts != COUNTS or offset != int(zran_manifest["decoded_bytes"]): raise ValueError("normal-form source census/decoded-boundary mismatch")
        temporary = output_index.with_suffix(output_index.suffix + ".tmp"); table_hash = sha256()
        streams = [run.open("rb") for run in runs]
        try:
            heap: list[tuple[bytes, int, bytes]] = []
            for ordinal, stream in enumerate(streams):
                value = stream.read(ENTRY.size)
                if value: heapq.heappush(heap, (value[:32], ordinal, value))
            with temporary.open("wb") as out:
                out.write(b"\0" * HEADER); previous = None; emitted = 0
                while heap:
                    digest, ordinal, value = heapq.heappop(heap)
                    if previous == digest: raise ValueError("duplicate or ambiguous canonical-key digest")
                    previous = digest; out.write(value); table_hash.update(value); emitted += 1
                    next_value = streams[ordinal].read(ENTRY.size)
                    if next_value: heapq.heappush(heap, (next_value[:32], ordinal, next_value))
        finally:
            for stream in streams: stream.close()
        if emitted != total: raise ValueError("merge record loss")
        table_sha = table_hash.digest(); header = temporary.with_suffix(".header")
        _write_header(path=header, count=total, source=source_gzip, zran_manifest=zran_manifest, table_sha=table_sha, c93_root=c93_root, c94_root=c94_root)
        with temporary.open("r+b") as out:
            out.seek(0); out.write(header.read_bytes())
        header.unlink(); temporary.replace(output_index)
    body = {"schema": SCHEMA, "records": total, "counts": counts, "source_sha256": _sha_file(source_gzip), "decoded_sha256": zran_manifest["decoded_sha256"], "zran_root": zran_manifest["root"], "zran_index_sha256": zran_manifest["index_sha256"], "entry_bytes": ENTRY.size, "index_bytes": output_index.stat().st_size, "index_sha256": _sha_file(output_index), "table_sha256": table_sha.hex(), "maximum_line_bytes": max_line, "mean_line_bytes": offset / total, "elapsed_seconds": time.monotonic() - started, "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "c93_capsule_root": c93_root, "c94_package_root": c94_root}
    body["root"] = _root(body)
    manifest = output_index.with_suffix(output_index.suffix + ".json"); manifest.write_text(json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n")
    return MappingProxyType(body)

@dataclass(frozen=True)
class NormalFormKeyIndex:
    source: Path
    path: Path
    manifest: MappingProxyType
    zran: PersistentZranReader
    _table: bytes
    def _entries(self) -> bytes:
        return self._table
    def _find(self, digest: bytes) -> tuple[Any, ...]:
        table = self._entries(); lo, hi = 0, self.manifest["records"]
        while lo < hi:
            mid = (lo + hi) // 2
            if table[mid * ENTRY.size:mid * ENTRY.size + 32] < digest: lo = mid + 1
            else: hi = mid
        if lo >= self.manifest["records"] or table[lo * ENTRY.size:lo * ENTRY.size + 32] != digest: raise KeyError("normal-form canonical key")
        return ENTRY.unpack_from(table, lo * ENTRY.size)
    def lookup_normal_form(self, *, resolution: str, pair_id: str, normal_form_root: str) -> MappingProxyType:
        key = canonical_key(resolution=resolution, pair_id=pair_id, normal_form_root=normal_form_root)
        entry = self._find(_digest_key(key)); _, offset, length, line_digest, root, global_seq, local_seq, code = entry
        raw = self.zran.read_uncompressed_range(offset, length)
        if len(raw) != length or sha256(raw).digest() != line_digest: raise ValueError("normal-form line transport mismatch")
        _, node, actual = _source_record(raw, global_seq, offset)
        if actual != canonical(key) or root != bytes.fromhex(normal_form_root) or node["pair"]["sequence"] != local_seq or CODE[resolution] != code: raise ValueError("normal-form indexed identity mismatch")
        return MappingProxyType({"normal_form": MappingProxyType(node), "global_sequence": global_seq, "line_offset": offset, "line_length": length, "key": MappingProxyType(key), "diagnostics": self.zran.diagnostics})
    def close(self) -> None: self.zran.close()

def validate_all_normal_form_source(source_gzip: Path, index: NormalFormKeyIndex, *, direct_holdout_stride: int = 154) -> dict[str, int]:
    """Sequentially validate all source records; retain only a 1,000-entry holdout."""
    offset = 0; total = 0; samples: list[tuple[str, str, str]] = []
    with gzip.open(source_gzip, "rb") as source:
        for raw in source:
            entry, node, key_raw = _source_record(raw, total, offset); stored = index._find(entry[:32])
            if ENTRY.pack(*stored) != entry: raise ValueError(f"key-index/source mismatch at {total}")
            if total % direct_holdout_stride == 0: samples.append((node["pair"]["resolution"], node["pair"]["id"], node["normal_form_root"]))
            offset += len(raw); total += 1
    if total != index.manifest["records"] or offset != int(index.zran.metadata["decoded_bytes"]): raise ValueError("source validation census mismatch")
    for resolution, pair_id, root in samples:
        record = index.lookup_normal_form(resolution=resolution, pair_id=pair_id, normal_form_root=root)
        if record["normal_form"]["normal_form_root"] != root: raise ValueError("direct lookup holdout mismatch")
    return {"records": total, "direct_holdouts": len(samples), "mismatches": 0}

def load_verified_normal_form_key_index(source_gzip: Path, path: Path, zran: PersistentZranReader) -> NormalFormKeyIndex:
    manifest = json.loads(path.with_suffix(path.suffix + ".json").read_text())
    if manifest.get("schema") != SCHEMA or _sha_file(source_gzip) != manifest["source_sha256"] or zran.metadata["root"] != manifest["zran_root"] or _sha_file(path) != manifest["index_sha256"]: raise ValueError("normal-form key-index authority mismatch")
    raw = path.read_bytes()
    if len(raw) != HEADER + manifest["records"] * ENTRY.size or raw[:8] != MAGIC or sha256(raw[HEADER:]).hexdigest() != manifest["table_sha256"]: raise ValueError("invalid key-index structure")
    count, k9, k11, k13 = struct.unpack_from(">QQQQ", raw, 24)
    if (count, k9, k11, k13) != (manifest["records"], COUNTS["K9_2_N8_b0.40"], COUNTS["K11_2_N10_b0.45"], COUNTS["K13_2_N12_b0.50"]): raise ValueError("key-index header census mismatch")
    return NormalFormKeyIndex(source_gzip.resolve(), path.resolve(), MappingProxyType(manifest), zran, raw[HEADER:])
