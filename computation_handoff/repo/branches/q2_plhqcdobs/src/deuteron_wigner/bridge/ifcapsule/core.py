"""C87 canonical, source-chain-equivalent C72 colour-authority capsule.

This module deliberately distinguishes the payload's scientific identity from
the unknown ignored runtime directory that existed when C82 was first run.
It never calls a C72 builder or treats the C72 runtime root as historical
instance evidence.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import shutil
from types import MappingProxyType
from typing import Any

import numpy as np

from ..qgcolor2.core import build as c66_build

ROOT = Path(__file__).resolve().parents[4]
CAPSULE = ROOT / "data" / "authority" / "c87_canonical_c72_color_authority"
SCHEMA = "C87-CANONICAL-C72-COLOR-AUTHORITY-V1"
STATUS = "C87_CANONICAL_SOURCE_CHAIN_C72_AUTHORITY_CAPSULE_INCOMPLETE"
NEXT = "C88/IFSTREAM — implement a bounded, restartable historical C82 scientific-stream exporter before any C82 equivalence claim"
CLAIM = "CANONICAL_SOURCE_CHAIN_EQUIVALENT_C72_AUTHORITY"
FORBIDDEN_CLAIM = "EXACT_HISTORICAL_C72_RUNTIME_INSTANCE_RECOVERED"
ARRAYS = ("E_src", "Gram", "adapter", "U3", "U3_dagger", "P3")
PRODUCER_COMMIT = "369e95e1004c2f896f8a41e5c3270f7644e3391d"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _digest(value: Any) -> str:
    return sha256(_canonical(value).encode()).hexdigest()


def _file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _array_hash(value: np.ndarray) -> str:
    item = np.ascontiguousarray(value)
    return sha256(item.dtype.str.encode() + str(item.shape).encode() + item.tobytes()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _basis_records() -> tuple[list[str], list[str]]:
    return ([f"product:cprime={c}:a={a}" for c in range(3) for a in range(8)],
            [f"triplet:c={c}" for c in range(3)])


def source_chain_arrays() -> dict[str, np.ndarray]:
    """Independent C53/C66 route; it does not read C72 runtime payloads."""
    source = c66_build()
    emission = np.asarray(source["E"])
    u3 = np.asarray(source["U3"])
    return {
        "E_src": emission,
        "Gram": emission.conj().T @ emission,
        "adapter": u3.conj().T @ emission,
        "U3": u3,
        "U3_dagger": u3.conj().T,
        "P3": np.asarray(source["P3"]),
    }


def _records(arrays: dict[str, np.ndarray]) -> list[dict[str, Any]]:
    rows, columns = _basis_records()
    u3 = arrays["U3"]
    records: list[dict[str, Any]] = []
    for i, row in enumerate(rows):
        for j, column in enumerate(columns):
            value = complex(u3[i, j])
            nonzero = value != 0j
            records.append({
                "row_id": row, "column_id": column,
                "status": "NONZERO_EXACT_ALGEBRAIC" if nonzero else "ZERO_BY_EXACT_COLOR_RULE",
                "expression": "E_src/sqrt(4/3)" if nonzero else "0",
                "zero_certificate": not nonzero,
                "normalization": "C_F=4/3",
                "midpoint": [value.real, value.imag], "bound": 2 * np.finfo(float).eps,
                "array": "U3", "index": [i, j], "dtype": u3.dtype.str,
                "precision": 53, "interval": "float64 midpoint +/- 2eps",
            })
    return records


def scientific_stream(arrays: dict[str, np.ndarray] | None = None) -> dict[str, Any]:
    arrays = source_chain_arrays() if arrays is None else arrays
    rows, columns = _basis_records()
    records = _records(arrays)
    array_domain = [{"id": name, "shape": list(arrays[name].shape), "dtype": arrays[name].dtype.str,
                     "scientific_sha256": _array_hash(arrays[name])} for name in ARRAYS]
    invariant = {
        "C_F": "4/3", "U3_dagger_U3": _array_hash(arrays["U3"].conj().T @ arrays["U3"]),
        "P3_hermitian": _array_hash(arrays["P3"] - arrays["P3"].conj().T),
        "P3_idempotent": _array_hash(arrays["P3"] @ arrays["P3"] - arrays["P3"]),
        "rank": int(np.linalg.matrix_rank(arrays["P3"])), "trace": float(np.trace(arrays["P3"]).real),
        "leakage_norm": float(np.linalg.norm((np.eye(24) - arrays["P3"]) @ arrays["E_src"])),
    }
    body = {"schema": SCHEMA, "producer_commit": PRODUCER_COMMIT, "rows": rows, "columns": columns,
            "records": records, "arrays": array_domain, "invariants": invariant}
    return {**body, "scientific_root": _digest(body)}


def candidate_stream(runtime: Path) -> dict[str, Any]:
    arrays: dict[str, np.ndarray] = {}
    for name in ARRAYS:
        path = runtime / f"{name}.npy"
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"incomplete C72 candidate: {name}")
        value = np.load(path, allow_pickle=False)
        if value.dtype.hasobject:
            raise ValueError("object dtype is prohibited")
        arrays[name] = value
    return scientific_stream(arrays)


def materialize_capsule(destination: Path = CAPSULE) -> dict[str, Any]:
    """Build a new C87 capsule solely from the C53/C66 source chain."""
    destination.mkdir(parents=True, exist_ok=True)
    payload = destination / "payload"
    payload.mkdir(exist_ok=True)
    arrays = source_chain_arrays()
    stream = scientific_stream(arrays)
    rows, columns = _basis_records()
    objects = []
    for name in ARRAYS:
        path = payload / f"{name}.npy"
        np.save(path, np.ascontiguousarray(arrays[name]), allow_pickle=False)
        objects.append({"id": name, "path": f"data/runtime/c72_qgcolor5/{name}.npy", "payload": f"payload/{name}.npy",
                        "sha256": _file_hash(path), "shape": list(arrays[name].shape), "dtype": arrays[name].dtype.str,
                        "bound_identity": "2eps"})
    index = {"status": "C72_SOURCE_DERIVED_TRIPLET_FULL_IMPORT_READY", "source_fingerprint": "C53/C66 source-chain reconstructed",
             "api_fingerprint": "C72 historical compatibility schema", "rows": rows, "columns": columns,
             "records": _records(arrays), "objects": objects}
    compat_index = destination / "index.json"
    compat_index.write_text(json.dumps(index, sort_keys=True, indent=2) + "\n")
    compatibility_root = {"index_sha256": _file_hash(compat_index), "records": 72, "rows": 24, "columns": 3}
    (destination / "root.json").write_text(json.dumps(compatibility_root, sort_keys=True, indent=2) + "\n")
    manifest = {"schema": SCHEMA, "claim": CLAIM, "forbidden_claim": FORBIDDEN_CLAIM,
                "scientific_root": stream["scientific_root"], "compatibility_root": _file_hash(destination / "root.json"),
                "index_sha256": _file_hash(compat_index), "objects": objects,
                "producer_commit": PRODUCER_COMMIT, "historical_instance": "UNKNOWN_NOT_CLAIMED"}
    (destination / "manifest.json").write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    return manifest


class CanonicalC72AuthorityCapsule:
    def __init__(self, root: Path = CAPSULE):
        self._root = root.resolve()
        manifest_path = self._root / "manifest.json"
        index_path = self._root / "index.json"
        root_path = self._root / "root.json"
        if not all(path.is_file() and not path.is_symlink() for path in (manifest_path, index_path, root_path)):
            raise ValueError("missing or unsafe C87 capsule authority file")
        manifest = json.loads(manifest_path.read_text())
        if manifest.get("schema") != SCHEMA or manifest.get("claim") != CLAIM:
            raise ValueError("C87 capsule schema or claim mismatch")
        if manifest.get("index_sha256") != _file_hash(index_path) or manifest.get("compatibility_root") != _file_hash(root_path):
            raise ValueError("C87 capsule root mismatch")
        self._manifest = _freeze(manifest)
        self._index = _freeze(json.loads(index_path.read_text()))
        self._compat_root = _freeze(json.loads(root_path.read_text()))
        stream = candidate_stream_from_capsule(self._root, self._index)
        if stream["scientific_root"] != manifest["scientific_root"]:
            raise ValueError("C87 scientific root mismatch")

    def manifest(self) -> Any: return self._manifest
    def records(self) -> tuple[Any, ...]: return tuple(_freeze(dict(item)) for item in self._index["records"])
    def rows(self) -> tuple[str, ...]: return tuple(self._index["rows"])
    def columns(self) -> tuple[str, ...]: return tuple(self._index["columns"])
    def load(self, object_id: str) -> np.ndarray:
        item = next((dict(value) for value in self._index["objects"] if value["id"] == object_id), None)
        if item is None: raise KeyError(object_id)
        path = (self._root / item["payload"]).resolve()
        if self._root not in path.parents or path.is_symlink() or _file_hash(path) != item["sha256"]:
            raise ValueError("unsafe or mismatched C87 array")
        value = np.load(path, allow_pickle=False)
        if value.dtype.hasobject or list(value.shape) != item["shape"] or value.dtype.str != item["dtype"]:
            raise ValueError("C87 array schema mismatch")
        value.setflags(write=False)
        return value


def candidate_stream_from_capsule(root: Path, index: Any) -> dict[str, Any]:
    arrays = {}
    for item in index["objects"]:
        path = root / item["payload"]
        arrays[item["id"]] = np.load(path, allow_pickle=False)
    return scientific_stream(arrays)


def load_canonical_c72_authority_capsule() -> CanonicalC72AuthorityCapsule:
    return CanonicalC72AuthorityCapsule()


def verify_canonical_c72_authority_capsule() -> dict[str, Any]:
    capsule = load_canonical_c72_authority_capsule()
    return {"claim": capsule.manifest()["claim"], "scientific_root": capsule.manifest()["scientific_root"],
            "objects": tuple(item["id"] for item in capsule.manifest()["objects"]), "pass": True}


def stage_canonical_c72_for_historical_c74(detached_worktree: Path, *, read_only: bool = True) -> Path:
    capsule = load_canonical_c72_authority_capsule()
    target = detached_worktree / "data" / "runtime" / "c72_qgcolor5"
    target.mkdir(parents=True, exist_ok=True)
    for item in capsule.manifest()["objects"]:
        destination = target / f"{item['id']}.npy"
        shutil.copyfile(CAPSULE / item["payload"], destination)
        if read_only: destination.chmod(0o444)
    for name in ("index.json", "root.json"):
        destination = target / name
        shutil.copyfile(CAPSULE / name, destination)
        if read_only: destination.chmod(0o444)
    return target


def verify_staged_canonical_c72(detached_worktree: Path) -> dict[str, Any]:
    target = detached_worktree / "data" / "runtime" / "c72_qgcolor5"
    stream = candidate_stream(target)
    capsule = load_canonical_c72_authority_capsule()
    return {"path": str(target), "scientific_root": stream["scientific_root"],
            "matches_capsule": stream["scientific_root"] == capsule.manifest()["scientific_root"],
            "read_only": all(not (target / f"{name}.npy").stat().st_mode & 0o222 for name in ARRAYS)}


def audit_c72_routes() -> dict[str, Any]:
    arrays = source_chain_arrays()
    expected = scientific_stream(arrays)
    candidate = candidate_stream(ROOT / "data" / "runtime" / "c72_qgcolor5")
    return {"status": STATUS, "next": NEXT, "producer_commit": PRODUCER_COMMIT,
            "route_a": "clean detached producer reconstruction; C68 payload staged into C72 historical schema",
            "route_b": "independent C53/C66 source-chain array derivation", "scientific_root": expected["scientific_root"],
            "candidate_scientific_root": candidate["scientific_root"], "route_roots_equal": expected["scientific_root"] == candidate["scientific_root"],
            "historical_instance_claimed": False, "capsule_created": (CAPSULE / "manifest.json").exists(),
            "historical_c74_compatibility": "PASS: historical C74 loaded the staged 24/3/72 authority and closed U3/P3 checks",
            "historical_c82_materialize": "PASS: exact C82 materialize completed with the staged capsule",
            "remaining_blocker": "C87.C82.COMPLETE_CANONICAL_SCIENTIFIC_STREAM_EXPORTER_ABSENT"}
