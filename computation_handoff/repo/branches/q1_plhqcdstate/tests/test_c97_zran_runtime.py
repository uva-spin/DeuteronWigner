from __future__ import annotations
import gzip
from pathlib import Path
import shutil
import subprocess
import sys

import pytest
from deuteron_wigner.bridge.ifproofinput.zran_runtime import build_persistent_zran_index, compile_adapter, open_verified_zran_reader

def _fixture(tmp_path: Path):
    tmp_path.mkdir(parents=True, exist_ok=True)
    source = tmp_path / "tiny.gz"; data = (b"abcdef0123456789\n" * 200000)
    with source.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as out: out.write(data)
    adapter = tmp_path / "c97_zran"; compile_adapter(adapter)
    return source, data, adapter

def test_persistent_index_is_deterministic_and_reloads(tmp_path: Path):
    source, data, adapter = _fixture(tmp_path)
    a = tmp_path / "a.zran"; b = tmp_path / "b.zran"
    first = build_persistent_zran_index(source, a, adapter, span=1 << 16)
    second = build_persistent_zran_index(source, b, adapter, span=1 << 16)
    assert a.read_bytes() == b.read_bytes()
    reader = open_verified_zran_reader(source, a, adapter)
    assert reader.read_uncompressed_range(131072, 97) == data[131072:131169]
    assert first["points"] == second["points"]

def test_corruption_and_build_if_missing_fail_closed(tmp_path: Path):
    source, _, adapter = _fixture(tmp_path); index = tmp_path / "index.zran"; build_persistent_zran_index(source, index, adapter, span=1 << 16)
    source.write_bytes(source.read_bytes() + b"changed")
    with pytest.raises(ValueError): open_verified_zran_reader(source, index, adapter)
    # Rebuild a valid fixture, then corrupt a persisted compressed offset and
    # dictionary byte.  The authenticated payload must reject both before C
    # extraction can see a forged access point.
    source, _, adapter = _fixture(tmp_path / "again"); index = tmp_path / "again" / "index.zran"; build_persistent_zran_index(source, index, adapter, span=1 << 16)
    raw = bytearray(index.read_bytes()); raw[280 + 8] ^= 1; index.write_bytes(raw)
    with pytest.raises(ValueError): open_verified_zran_reader(source, index, adapter)
    build_persistent_zran_index(source, index, adapter, span=1 << 16)
    raw = bytearray(index.read_bytes()); raw[280 + 22] ^= 1; index.write_bytes(raw)
    with pytest.raises(ValueError): open_verified_zran_reader(source, index, adapter)
    build_persistent_zran_index(source, index, adapter, span=1 << 16)
    index.write_bytes(index.read_bytes()[:-1])
    with pytest.raises(ValueError): open_verified_zran_reader(source, index, adapter)
    with pytest.raises(FileNotFoundError): build_persistent_zran_index(source, tmp_path / "missing.zran", tmp_path / "missing-adapter")

def test_clean_process_reader_has_no_build_fallback(tmp_path: Path):
    source, data, adapter = _fixture(tmp_path); index = tmp_path / "index.zran"; build_persistent_zran_index(source, index, adapter, span=1 << 16)
    command = """
from pathlib import Path
from deuteron_wigner.bridge.ifproofinput.zran_runtime import open_verified_zran_reader
r = open_verified_zran_reader(Path(__import__('sys').argv[1]), Path(__import__('sys').argv[2]), Path(__import__('sys').argv[3]))
print(r.read_uncompressed_range(131072, 31).hex())
"""
    env = {"PYTHONPATH": str(Path(__file__).resolve().parents[1] / "src")}
    result = subprocess.run([sys.executable, "-c", command, str(source), str(index), str(adapter)], check=True, text=True, capture_output=True, env=env)
    assert bytes.fromhex(result.stdout.strip()) == data[131072:131103]

def test_authenticated_c93_range_after_nonzero_restart(tmp_path: Path):
    root = Path(__file__).resolve().parents[1]; source = root / "data/runtime/c93_ifc90payload/capsule/normal_forms.jsonl.gz"
    if not source.exists(): pytest.skip("runtime source unavailable")
    adapter = tmp_path / "c97_zran"; compile_adapter(adapter); index = tmp_path / "c93.zran"
    metadata = build_persistent_zran_index(source, index, adapter, span=1 << 20)
    assert metadata["points"] == 910
    reader = open_verified_zran_reader(source, index, adapter)
    with gzip.open(source, "rb") as baseline: baseline.seek(8 << 20); expected = baseline.read(4096)
    assert reader.read_uncompressed_range(8 << 20, 4096) == expected
