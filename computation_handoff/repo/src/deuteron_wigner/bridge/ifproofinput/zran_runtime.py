"""C97 fixed-endian, reloadable zran transport for the unchanged C93 gzip."""
from __future__ import annotations

from dataclasses import dataclass
import gzip
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import time
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
VENDOR = Path(__file__).with_name("vendor")
MAGIC = b"C97ZRAI1"
SCHEMA = 1
HEADER = 280
RECORD = 32790
_HASH_OFFSET = 56

def _sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def _decoded_digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256(); count = 0
    with gzip.open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            count += len(chunk); h.update(chunk)
    return count, h.hexdigest()

def _adapter_source_hash() -> str:
    return _sha_file(VENDOR / "c97_zran_adapter.c")

def _adapter_identity(adapter: Path) -> dict[str, str]:
    lines = subprocess.run([str(adapter), "identity"], check=True, capture_output=True, text=True).stdout.splitlines()
    body = dict(line.split("=", 1) for line in lines)
    if set(body) != {"compile", "runtime", "off_t", "size_t", "endianness"}: raise ValueError("invalid zran ABI identity")
    return body

def compile_adapter(binary: Path) -> None:
    """Compile explicitly; production readers never invoke this helper."""
    binary.parent.mkdir(parents=True, exist_ok=True)
    command = ["cc", "-O2", "-Wall", "-Wextra", "-I", str(VENDOR), str(VENDOR / "c97_zran_adapter.c"), str(VENDOR / "zran.c"), "-lz", "-o", str(binary)]
    subprocess.run(command, check=True, capture_output=True, text=True)

def _manifest(index: Path) -> Path: return index.with_suffix(index.suffix + ".json")

def build_persistent_zran_index(source: Path, index: Path, adapter: Path, *, span: int = 1 << 20) -> MappingProxyType:
    """Build atomically, bind transport hashes, and return frozen metadata."""
    if not adapter.is_file(): raise FileNotFoundError("zran adapter missing; build-if-missing is forbidden")
    source = source.resolve(); index = index.resolve(); temporary = index.with_suffix(index.suffix + ".tmp")
    subprocess.run([str(adapter), "build", str(source), str(temporary), str(span)], check=True, capture_output=True, text=True)
    raw = bytearray(temporary.read_bytes())
    if len(raw) < HEADER or raw[:8] != MAGIC: raise ValueError("adapter emitted invalid index")
    schema, endian, mode, record = struct.unpack_from(">IIII", raw, 8)
    compressed, decoded, stored_span, count = struct.unpack_from(">QQQQ", raw, 24)
    if schema != SCHEMA or endian != 0x01020304 or record != RECORD or stored_span != span or compressed != source.stat().st_size: raise ValueError("adapter header mismatch")
    decoded_count, decoded_sha = _decoded_digest(source)
    if decoded != decoded_count: raise ValueError("decoded length mismatch")
    payload_sha = hashlib.sha256(raw[HEADER:]).digest()
    identity = _adapter_identity(adapter); identity_sha = hashlib.sha256(json.dumps(identity, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    bindings = [_sha_file(source), decoded_sha, _sha_file(VENDOR / "zran.c"), _sha_file(VENDOR / "zran.h"), _adapter_source_hash(), payload_sha.hex(), identity_sha]
    raw[_HASH_OFFSET:_HASH_OFFSET + 224] = b"".join(bytes.fromhex(item) for item in bindings)
    temporary.write_bytes(raw); temporary.replace(index)
    body = {"schema": "C97-ZRAN-INDEX-V1", "source": str(source), "source_sha256": bindings[0], "decoded_sha256": bindings[1], "source_bytes": compressed, "decoded_bytes": decoded, "span": span, "points": count, "mode": mode, "zran_c_sha256": bindings[2], "zran_h_sha256": bindings[3], "adapter_sha256": bindings[4], "payload_sha256": bindings[5], "toolchain_identity": identity, "toolchain_sha256": bindings[6], "index_sha256": _sha_file(index), "index_name": index.name}
    body["root"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    manifest_tmp = _manifest(index).with_suffix(_manifest(index).suffix + ".tmp"); manifest_tmp.write_text(json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n"); manifest_tmp.replace(_manifest(index))
    return MappingProxyType(body)

def load_persistent_zran_index(source: Path, index: Path, adapter: Path) -> MappingProxyType:
    """Authenticate only existing artifacts; no build or full-stream fallback."""
    if not adapter.is_file(): raise FileNotFoundError("zran adapter missing")
    body = json.loads(_manifest(index).read_text()); raw = index.read_bytes()
    if raw[:8] != MAGIC or len(raw) < HEADER: raise ValueError("invalid zran index")
    if _sha_file(source) != body["source_sha256"] or _sha_file(index) != body["index_sha256"]: raise ValueError("zran source or index hash mismatch")
    if hashlib.sha256(raw[HEADER:]).hexdigest() != body["payload_sha256"]: raise ValueError("zran payload hash mismatch")
    if _adapter_identity(adapter) != body["toolchain_identity"]: raise ValueError("zran ABI identity mismatch")
    expected = [body["source_sha256"], body["decoded_sha256"], body["zran_c_sha256"], body["zran_h_sha256"], body["adapter_sha256"], body["payload_sha256"], body["toolchain_sha256"]]
    stored = [raw[_HASH_OFFSET + 32 * n:_HASH_OFFSET + 32 * (n + 1)].hex() for n in range(7)]
    if stored != expected: raise ValueError("zran header binding mismatch")
    return MappingProxyType(body)

@dataclass(frozen=True)
class PersistentZranReader:
    source: Path
    index: Path
    adapter: Path
    metadata: MappingProxyType
    _worker: Any = None
    _last_diagnostics: MappingProxyType | None = None
    def _ensure_worker(self) -> Any:
        if self._worker is None:
            object.__setattr__(self, "_worker", subprocess.Popen([str(self.adapter), "serve", str(self.source), str(self.index)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        return self._worker
    def read_uncompressed_range(self, offset: int, length: int) -> bytes:
        if offset < 0 or length < 0: raise ValueError("negative range")
        started = time.monotonic(); worker = self._ensure_worker()
        assert worker.stdin is not None and worker.stdout is not None
        worker.stdin.write(struct.pack(">QI", offset, length)); worker.stdin.flush()
        header = worker.stdout.read(20)
        if len(header) != 20: raise RuntimeError("zran worker terminated")
        got, restart, compressed = struct.unpack(">QIQ", header)
        if got == (1 << 64) - 1: raise ValueError("zran extraction failure")
        result = worker.stdout.read(got)
        if len(result) != got: raise ValueError("truncated zran worker result")
        if offset >= self.metadata["span"] and restart == 0 and compressed == 0: raise ValueError("full-stream fallback detected")
        object.__setattr__(self, "_last_diagnostics", MappingProxyType({"restart_point": restart, "compressed_start": compressed, "requested_offset": offset, "returned_bytes": got, "latency_seconds": time.monotonic() - started}))
        return bytes(result)
    @property
    def diagnostics(self) -> MappingProxyType | None: return self._last_diagnostics
    def close(self) -> None:
        if self._worker is not None:
            assert self._worker.stdin is not None
            self._worker.stdin.close(); self._worker.wait(timeout=15); object.__setattr__(self, "_worker", None)

def open_verified_zran_reader(source: Path, index: Path, adapter: Path) -> PersistentZranReader:
    return PersistentZranReader(source.resolve(), index.resolve(), adapter.resolve(), load_persistent_zran_index(source.resolve(), index.resolve(), adapter.resolve()))
