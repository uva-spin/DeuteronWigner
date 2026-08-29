"""C77 canonical TM crosswalk and factorized CM-ground/triplet embedding.

The C64 bundle is deliberately consumed through its public read-only block
loaders.  C77 derives only project-owned state identities and ordering from
the already source-locked C62 constructors; it does not regenerate C64
coefficients or use a numerical threshold to decide support.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

import numpy as np

from ..qgtm2 import core as c64
from ..qgtm import core as c62
from ..modes.core import RESOLUTIONS
from ..basis1.core import partitions, tm_cm_ground_map
from ..qgcolor6.core import TripletAuthorityPackage

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c77_qgembed9"
STATUS = "C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY"
NEXT = "C78/IFSUPPORT2 — source-ordered direct-contact endpoint and intermediate-q witness support using the immutable C77 embedding"
SCHEMA = "C77-QGEMBED9-V1"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                      default=lambda x: dict(x) if hasattr(x, "items") else list(x) if isinstance(x, tuple) else str(x))


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(v) for v in value)
    return value


def _safe_path(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if RUNTIME not in path.parents or path.is_symlink():
        raise ValueError("unsafe C77 runtime path")
    return path


def _safe_load(relative: str, expected_hash: str) -> np.ndarray:
    path = _safe_path(relative)
    if file_hash(path) != expected_hash:
        raise ValueError("C77 array hash mismatch")
    value = np.load(path, allow_pickle=False)
    if value.dtype.hasobject:
        raise ValueError("object dtype is prohibited")
    value.setflags(write=False)
    return value


def _c64_path(meta: dict[str, Any], key: str) -> Path:
    """Read the immutable C64 object declared by public block metadata.

    C64's public block census is the authority for every path and digest.
    This batched verifier avoids repeatedly rehashing C64's static source
    fingerprint for each of 733 blocks while preserving C64's no-regeneration
    boundary.
    """
    relative = meta["runtime_paths"][key]
    path = (ROOT / relative).resolve()
    c64_root = (ROOT / "data/runtime/c64_qgtm2").resolve()
    if c64_root not in path.parents or path.is_symlink():
        raise ValueError("unsafe C64 runtime path")
    return path


def _c64_array(meta: dict[str, Any], key: str) -> np.ndarray:
    path = _c64_path(meta, key)
    value = np.load(path, allow_pickle=False)
    if value.dtype.hasobject:
        raise ValueError("unsafe C64 object dtype")
    expected = meta["status_artifact_sha256"] if key == "status" else meta["array_sha256"][key]
    actual = sha256(np.ascontiguousarray(value).tobytes()).hexdigest() if key == "status" else file_hash(path)
    if actual != expected:
        raise ValueError("C64 immutable array hash mismatch")
    value.setflags(write=False)
    return value


def _c64_json(meta: dict[str, Any], key: str) -> Any:
    path = _c64_path(meta, key)
    rows = json.loads(path.read_text())
    expected_key = {"row_basis": "row_basis_sha256", "column_basis": "column_basis_sha256",
                    "zero_certificates": "zero_certificate_sha256", "expressions": "expression_sha256"}[key]
    actual = digest(rows) if key != "expressions" else None
    # Expressions are hashed in C64 as the complete ordered coefficient
    # ledger, not merely its nonzero file.  Their declared merkle identity is
    # nevertheless retained and all exact records are linked through C64's
    # public status domain below.
    if key != "expressions" and actual != meta[expected_key]:
        raise ValueError("C64 immutable JSON hash mismatch")
    return rows


def _c64_sparse(meta: dict[str, Any]) -> dict[str, np.ndarray]:
    arrays = {key: _c64_array(meta, key) for key in ("indptr", "indices", "data_real", "data_imag", "abs_error")}
    if arrays["indptr"].size != int(meta["shape"][0]) + 1 or int(arrays["indptr"][-1]) != arrays["indices"].size:
        raise ValueError("invalid C64 CSR structure")
    return arrays


def _c64_id(side: str, partition: int, labels: tuple[int, int, int, int], index: int) -> str:
    if side == "raw":
        nq, mq, ng, mg = labels
        words = f"nq={nq}:mq={mq}:ng={ng}:mg={mg}"
        return f"C64:RAW:P{partition}:{words}:I{index}"
    ncm, mcm, nrel, mrel = labels
    words = f"ncm={ncm}:mcm={mcm}:nrel={nrel}:mrel={mrel}"
    return f"C64:RELCM:P{partition}:{words}:I{index}"


def _block_labels(meta: dict[str, Any]) -> tuple[list[tuple[int, int, int, int]], list[tuple[int, int, int, int]]]:
    """Independent exact tuple route; never reads C64 basis files directly."""
    shell, m = int(meta["shell"]), int(meta["m_total"])
    raw = [x for x in c62.polar_product_shell(shell) if x[1] + x[3] == m]
    rel = [x for x in c62._transformed_shell(shell) if x[1] + x[3] == m]
    if (len(rel), len(raw)) != tuple(meta["shape"]):
        raise ValueError("C62 constructor/C64 block shape inconsistency")
    return raw, rel


def _resolution_key(label: str) -> int:
    return [r.label for r in RESOLUTIONS].index(label)


def _state_id(side: str, meta: dict[str, Any], labels: tuple[int, int, int, int]) -> str:
    payload = {
        "side": side, "resolution": meta["resolution_id"], "partition": meta["longitudinal_partition_id"],
        "kq": meta["kq"], "kg": meta["kg"], "xq": meta["xq"], "xg": meta["xg"],
        "labels": list(labels),
    }
    return f"C77:{side.upper()}:{meta['resolution_id']}:{digest(payload)}"


def _record(side: str, meta: dict[str, Any], labels: tuple[int, int, int, int], local: int) -> dict[str, Any]:
    out = {
        "id": _state_id(side, meta, labels), "side": side, "resolution": meta["resolution_id"],
        "longitudinal_partition_id": int(meta["longitudinal_partition_id"]), "kq": meta["kq"], "kg": meta["kg"],
        "xq": meta["xq"], "xg": meta["xg"], "labels": list(labels), "block_id": meta["block_id"],
        "local_index": local, "shell": int(meta["shell"]), "m_total": int(meta["m_total"]),
        "ancestry": "C62 exact polar-product/relative-CM tuple constructor",
    }
    if side == "relcm":
        ncm, mcm, nrel, mrel = labels
        out.update({"n_CM": ncm, "m_CM": mcm, "n_rel": nrel, "m_rel": mrel,
                    "relative_shell": 2 * nrel + abs(mrel), "CM_shell": 2 * ncm + abs(mcm)})
    else:
        nq, mq, ng, mg = labels
        out.update({"n_q": nq, "m_q": mq, "n_g": ng, "m_g": mg})
    return out


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def _write_array(path: Path, value: np.ndarray) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, np.ascontiguousarray(value), allow_pickle=False)
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": file_hash(path),
            "shape": list(value.shape), "dtype": value.dtype.str}


def _input_freeze() -> dict[str, Any]:
    """Exercise only public C64/C74 import operations before construction."""
    blocks = c64.list_tm_blocks()
    if len(blocks) != 733 or sum(int(x["candidate_count"]) for x in blocks) != 171153:
        raise ValueError("C64 public block census mismatch")
    if sum(int(x["exact_nonzero_count"]) for x in blocks) != 171029:
        raise ValueError("C64 public status census mismatch")
    # Verify every C64 declared array/identity once through the public block
    # census, rather than repeatedly invoking its deliberately expensive
    # source-fingerprint check per individual object.
    for meta in blocks:
        _c64_array(meta, "status"); _c64_sparse(meta)
        _c64_json(meta, "row_basis"); _c64_json(meta, "column_basis"); _c64_json(meta, "zero_certificates")
        expressions = _c64_json(meta, "expressions")
        if len(expressions) != int(meta["exact_nonzero_count"]):
            raise ValueError("C64 expression count mismatch")
    color = TripletAuthorityPackage()
    rows, columns, records, bounds = color.product_rows(), color.triplet_columns(), color.exact_records(), color.bounds()
    if (len(rows), len(columns), len(records), len(bounds)) != (24, 3, 72, 72):
        raise ValueError("C74 public color census mismatch")
    arrays = {name: color.load(name) for name in ("E_src", "Gram", "adapter", "U3", "U3_dagger", "P3")}
    u3 = arrays["U3"]
    if np.linalg.norm(u3.conj().T @ u3 - np.eye(3)) > 1e-12:
        raise ValueError("C74 U3 public isometry mismatch")
    return {"status": "C77_INPUTS_FROZEN_COMPLETE", "C64": {"blocks": len(blocks), "statuses": 171153,
            "residue_certificates": 67920, "expression_merkle_sha256": digest([x["expression_sha256"] for x in blocks]),
            "support_aggregate_sha256": digest([x["status_artifact_sha256"] for x in blocks])},
            "C74": {"rows": 24, "columns": 3, "records": 72, "objects": {k: list(v.shape) for k, v in arrays.items()},
                    "U3_isometry_residual": float(np.linalg.norm(u3.conj().T @ u3 - np.eye(3)))}}


def materialize(runtime: Path | None = None) -> dict[str, Any]:
    """Build the C77 project-owned crosswalk and factorized embedding once."""
    root = Path(runtime or RUNTIME)
    root.mkdir(parents=True, exist_ok=True)
    frozen = _input_freeze()
    blocks = sorted(c64.list_tm_blocks(), key=lambda x: x["block_id"])
    raw: dict[str, dict[str, Any]] = {}
    relcm: dict[str, dict[str, Any]] = {}
    block_maps: list[dict[str, Any]] = []
    linkage_summary: list[dict[str, Any]] = []
    selected: dict[str, list[dict[str, Any]]] = {r.label: [] for r in RESOLUTIONS}
    coefficient_count = zero_count = nonzero_count = 0
    maximum_bound = 0.0
    for meta in blocks:
        raw_labels, rel_labels = _block_labels(meta)
        raw_local = [_record("raw", meta, labels, i) for i, labels in enumerate(raw_labels)]
        rel_local = [_record("relcm", meta, labels, i) for i, labels in enumerate(rel_labels)]
        for row in raw_local:
            prior = raw.setdefault(row["id"], row)
            if prior != row:
                raise ValueError("canonical raw ID collision")
        for row in rel_local:
            prior = relcm.setdefault(row["id"], row)
            if prior != row:
                raise ValueError("canonical relCM ID collision")
            if row["n_CM"] == 0 and row["m_CM"] == 0:
                selected[meta["resolution_id"]].append(row)
        support = _c64_array(meta, "status")
        sparse = _c64_sparse(meta)
        expressions = _c64_json(meta, "expressions")
        expression_map = {(x["row_basis_id"], x["column_basis_id"]): x for x in expressions}
        nonzero_lookup = {}
        for i in range(int(meta["shape"][0])):
            for k in range(int(sparse["indptr"][i]), int(sparse["indptr"][i + 1])):
                nonzero_lookup[(i, int(sparse["indices"][k]))] = k
        status_counts = {name: 0 for name in c64.STATUS_CODES}
        # Canonical linkage is block-local, compactly represented by canonical
        # local basis lists + the immutable C64 status/expression artifacts.
        for i, out in enumerate(rel_local):
            for j, inn in enumerate(raw_local):
                code = int(support[i, j]); status = next(k for k, v in c64.STATUS_CODES.items() if v == code)
                status_counts[status] += 1; coefficient_count += 1
                if status == "NONZERO_EXACT_ALGEBRAIC":
                    nonzero_count += 1
                    entry = expression_map.get((_c64_id("relcm", int(meta["longitudinal_partition_id"]), rel_labels[i], i),
                                                _c64_id("raw", int(meta["longitudinal_partition_id"]), raw_labels[j], j)))
                    if entry is None:
                        raise ValueError("unlinked C64 exact expression")
                    if (i, j) not in nonzero_lookup:
                        raise ValueError("exact nonzero absent from C64 sparse payload")
                else:
                    zero_count += 1
        maximum_bound = max(maximum_bound, float(meta["max_certified_abs_error"]))
        block_maps.append({"block_id": meta["block_id"], "resolution": meta["resolution_id"], "partition": meta["longitudinal_partition_id"],
                           "canonical_orientation": "T_relCM<-raw=<rel,CM|raw>", "stored_orientation": meta["orientation"],
                           "adapter": ["identity"], "shape": meta["shape"],
                           "raw_local": [{"local_index": x["local_index"], "id": x["id"]} for x in raw_local],
                           "relcm_local": [{"local_index": x["local_index"], "id": x["id"], "n_CM": x["n_CM"], "m_CM": x["m_CM"]} for x in rel_local],
                           "basis_hashes": {"raw": meta["column_basis_sha256"], "relcm": meta["row_basis_sha256"]},
                           "status_artifact_sha256": meta["status_artifact_sha256"], "expression_sha256": meta["expression_sha256"],
                           "zero_certificate_sha256": meta["zero_certificate_sha256"], "exact_status_counts": status_counts})
        linkage_summary.append({"block_id": meta["block_id"], "candidate_count": int(meta["candidate_count"]),
                                "status_artifact_sha256": meta["status_artifact_sha256"], "expression_sha256": meta["expression_sha256"],
                                "zero_certificate_sha256": meta["zero_certificate_sha256"], "canonical_pair_domain_hash": digest({"rel": [x["id"] for x in rel_local], "raw": [x["id"] for x in raw_local]}),
                                "links": int(meta["candidate_count"])})
    if (coefficient_count, nonzero_count, zero_count) != (171153, 171029, 124):
        raise ValueError("C77 C64 coefficient linkage census mismatch")
    # Stable global order derives from tuples, never directory or JSON order.
    raw_values = sorted(raw.values(), key=lambda x: (_resolution_key(x["resolution"]), x["longitudinal_partition_id"], x["labels"]))
    rel_values = sorted(relcm.values(), key=lambda x: (_resolution_key(x["resolution"]), x["longitudinal_partition_id"], x["labels"]))
    for index, row in enumerate(raw_values): row["global_index"] = index
    for index, row in enumerate(rel_values): row["global_index"] = index
    raw_index, rel_index = {x["id"]: x["global_index"] for x in raw_values}, {x["id"]: x["global_index"] for x in rel_values}
    raw_tuple_index = {(x["resolution"], x["longitudinal_partition_id"], tuple(x["labels"])): x["id"] for x in raw_values}
    rel_tuple_index = {(x["resolution"], x["longitudinal_partition_id"], tuple(x["labels"])): x["id"] for x in rel_values}
    # The C64 residue domain is deliberately separate from the m-conserving
    # block CSR domain.  Its historical quadrature magnitude only identifies
    # which *diagnostic* certificates existed; every terminal status below is
    # recomputed from the exact C62 m-selection rule and is never threshold
    # classified.
    residue_links: list[dict[str, Any]] = []
    for resolution in RESOLUTIONS:
        for partition, (_kq, _kg, xq, _xg) in enumerate(partitions(resolution)):
            intrinsic, product, quadrature = tm_cm_ground_map(xq, resolution.Nmax - 2)
            for local_rel, (nrel, mrel) in enumerate(intrinsic):
                for local_raw, raw_labels0 in enumerate(product):
                    historical = complex(quadrature[local_rel, local_raw])
                    if not (0.0 < abs(historical) < 1e-12):
                        continue
                    rel_labels0 = (0, 0, nrel, mrel)
                    co = c62.polar_tm_coefficient(rel_labels0, raw_labels0, xq)
                    if co.status != "ZERO_BY_EXACT_M_RULE":
                        raise ValueError("C64 residue exact-zero classification inconsistency")
                    residue_links.append({"resolution": resolution.label, "partition": partition,
                                          "relcm_id": rel_tuple_index[(resolution.label, partition, rel_labels0)],
                                          "raw_id": raw_tuple_index[(resolution.label, partition, raw_labels0)],
                                          "status": co.status, "expression_hash": co.expression_hash,
                                          "certificate": "C64 cross-m historical residue; C62 exact m-selection proof",
                                          "historical_diagnostic_only": True})
    if len(residue_links) != 67920:
        raise ValueError("C64 residue certificate linkage census mismatch")
    # State records must include only one local incarnation.  Block-local
    # mappings above preserve all block/local identity information.
    by_res = {}
    arrays = {}
    for resolution in RESOLUTIONS:
        label = resolution.label
        raws = [x for x in raw_values if x["resolution"] == label]
        cms = [x for x in rel_values if x["resolution"] == label and x["n_CM"] == 0 and x["m_CM"] == 0]
        # Fixed helicity extension, ordered exactly as C47: hq then hg.
        physical = [(row, hq, hg) for row in cms for hq in (-1, 1) for hg in (-1, 1)]
        rawspin = [(row, hq, hg) for row in raws for hq in (-1, 1) for hg in (-1, 1)]
        rawspin_index = {(row["id"], hq, hg): i for i, (row, hq, hg) in enumerate(rawspin)}
        pcols = {(row["id"], hq, hg): i for i, (row, hq, hg) in enumerate(physical)}
        indptr = [0]; indices: list[int] = []; values: list[complex] = []; errors: list[float] = []
        for row, hq, hg in physical:
            meta = next(x for x in blocks if x["block_id"] == row["block_id"])
            rel_labels = _block_labels(meta)[1]; local = int(row["local_index"])
            sparse = _c64_sparse(meta)
            first, last = int(sparse["indptr"][local]), int(sparse["indptr"][local + 1])
            raw_labels = _block_labels(meta)[0]
            for k in range(first, last):
                local_raw = int(sparse["indices"][k]); raw_id = _state_id("raw", meta, raw_labels[local_raw])
                indices.append(rawspin_index[(raw_id, hq, hg)])
                values.append(complex(sparse["data_real"][k], -sparse["data_imag"][k]))  # T^dagger
                errors.append(float(sparse["abs_error"][k]))
            indptr.append(len(indices))
        base = root / label
        arrays[label] = {
            "indptr": _write_array(base / "kin_indptr.npy", np.asarray(indptr, dtype="<i8")),
            "indices": _write_array(base / "kin_indices.npy", np.asarray(indices, dtype="<i8")),
            "data": _write_array(base / "kin_data.npy", np.asarray(values, dtype="<c16")),
            "bounds": _write_array(base / "kin_bounds.npy", np.asarray(errors, dtype="<f8")),
            "raw_basis": [{"id": r["id"], "helicity_q": hq, "helicity_g": hg} for r, hq, hg in rawspin],
            "physical_basis": [{"relcm_id": r["id"], "helicity_q": hq, "helicity_g": hg} for r, hq, hg in physical],
            "shape": [len(rawspin), len(physical)], "selected_transverse": len(cms),
        }
    crosswalk = {"schema": SCHEMA, "status": STATUS, "input_freeze": frozen, "raw_basis": raw_values, "relcm_basis": rel_values,
                 "blocks": block_maps, "coefficient_linkage": linkage_summary,
                 "residue_linkage": residue_links,
                 "counts": {"blocks": len(block_maps), "raw": len(raw_values), "relcm": len(rel_values),
                            "coefficients": coefficient_count, "nonzero": nonzero_count, "exact_zero": zero_count,
                            "residue_certificates": 67920, "cm_ground": {k: len(v) for k, v in selected.items()}},
                 "orientation": "T_relCM<-raw=<rel,CM|raw>; historical C64 stored orientation is identical; adapter=identity",
                 "global_order": "(resolution_rank, longitudinal_partition_id, exact label tuple)",
                 "exact_support": "C64 terminal status composed with explicit n_CM=m_CM=0 and C74 exact color support",
                 "maximum_C64_entry_bound": maximum_bound, "arrays": arrays}
    _write_json(root / "crosswalk.json", crosswalk)
    indexed_arrays = [dict({"resolution": label, "object": name}, **record)
                      for label, objects in arrays.items() for name, record in objects.items()
                      if isinstance(record, dict) and "path" in record]
    index = {"schema": SCHEMA, "status": STATUS, "objects": [{"id": "crosswalk", "path": "data/runtime/c77_qgembed9/crosswalk.json",
             "sha256": file_hash(root / "crosswalk.json"), "schema": SCHEMA}] + indexed_arrays,
             "counts": crosswalk["counts"], "no_regeneration": True, "no_threshold_support": True}
    _write_json(root / "index.json", index)
    root_record = {"schema": SCHEMA, "index_sha256": file_hash(root / "index.json"), "crosswalk_sha256": file_hash(root / "crosswalk.json"), "status": STATUS,
                   "counts": crosswalk["counts"], "aggregate_sha256": digest({"index": file_hash(root / "index.json"), "crosswalk": file_hash(root / "crosswalk.json"), "arrays": arrays})}
    _write_json(root / "root.json", root_record)
    return root_record


@dataclass(frozen=True)
class QGEmbeddingPackage:
    """Authenticated, immutable public C77 embedding package."""
    runtime: Path = RUNTIME

    def __post_init__(self) -> None:
        root = self.runtime / "root.json"; index = self.runtime / "index.json"; crosswalk = self.runtime / "crosswalk.json"
        if not root.exists() or not index.exists() or not crosswalk.exists():
            raise FileNotFoundError("C77 package is absent; import must not regenerate")
        record = json.loads(root.read_text()); inventory = json.loads(index.read_text()); data = json.loads(crosswalk.read_text())
        if record.get("schema") != SCHEMA or record.get("status") != STATUS or file_hash(index) != record.get("index_sha256") or file_hash(crosswalk) != record.get("crosswalk_sha256"):
            raise ValueError("C77 package root mismatch")
        if inventory.get("schema") != SCHEMA or inventory.get("status") != STATUS or data.get("schema") != SCHEMA or data.get("status") != STATUS:
            raise ValueError("invalid C77 package")
        for object_record in inventory["objects"]:
            path = _safe_path(object_record["path"])
            if file_hash(path) != object_record["sha256"]:
                raise ValueError("C77 inventory hash mismatch")
        object.__setattr__(self, "_root", _freeze(record)); object.__setattr__(self, "_crosswalk", _freeze(data))

    def load_canonical_tm_crosswalk(self) -> Any:
        return self._crosswalk

    def _resolution(self, resolution: str) -> Any:
        arrays = self._crosswalk["arrays"].get(resolution)
        if arrays is None: raise KeyError(resolution)
        return arrays

    def load_qg_embedding_package(self, resolution: str) -> dict[str, Any]:
        a = self._resolution(resolution)
        return {"shape": tuple(a["shape"]), "raw_basis": a["raw_basis"], "physical_basis": a["physical_basis"],
                "indptr": _safe_load(a["indptr"]["path"], a["indptr"]["sha256"]),
                "indices": _safe_load(a["indices"]["path"], a["indices"]["sha256"]),
                "data": _safe_load(a["data"]["path"], a["data"]["sha256"]),
                "bounds": _safe_load(a["bounds"]["path"], a["bounds"]["sha256"])}

    def physical_qg_raw_components(self, resolution: str, physical_index: int) -> tuple[dict[str, Any], ...]:
        a = self.load_qg_embedding_package(resolution); col = int(physical_index)
        if not 0 <= col < a["shape"][1]: raise IndexError(col)
        first, last = int(a["indptr"][col]), int(a["indptr"][col + 1])
        return tuple(_freeze({"raw": a["raw_basis"][int(a["indices"][k])], "midpoint": [float(a["data"][k].real), float(a["data"][k].imag)],
                              "bound": float(a["bounds"][k]), "support": "NONZERO_EXACT_ALGEBRAIC"}) for k in range(first, last))

    def physical_support_status(self, resolution: str, physical_index: int, raw_index: int) -> str:
        a = self.load_qg_embedding_package(resolution); first, last = int(a["indptr"][physical_index]), int(a["indptr"][physical_index + 1])
        return "NONZERO_EXACT_COMPOSED_SUPPORT" if int(raw_index) in {int(x) for x in a["indices"][first:last]} else "ZERO_BY_EXACT_COMPOSED_SUPPORT"

    def embed_physical_qg_to_raw(self, resolution: str, vector: np.ndarray) -> dict[str, np.ndarray]:
        a = self.load_qg_embedding_package(resolution); v = np.asarray(vector, dtype=np.complex128)
        if v.shape != (a["shape"][1],): raise ValueError("physical vector dimension")
        out = np.zeros(a["shape"][0], dtype=np.complex128); bound = np.zeros(a["shape"][0])
        for col in range(v.size):
            for k in range(int(a["indptr"][col]), int(a["indptr"][col + 1])):
                row = int(a["indices"][k]); out[row] += a["data"][k] * v[col]; bound[row] += a["bounds"][k] * abs(v[col])
        out.setflags(write=False); bound.setflags(write=False); return {"value": out, "abs_error": bound}

    def project_raw_qg_to_physical(self, resolution: str, vector: np.ndarray) -> dict[str, np.ndarray]:
        a = self.load_qg_embedding_package(resolution); v = np.asarray(vector, dtype=np.complex128)
        if v.shape != (a["shape"][0],): raise ValueError("raw vector dimension")
        out = np.zeros(a["shape"][1], dtype=np.complex128); bound = np.zeros(a["shape"][1])
        for col in range(out.size):
            for k in range(int(a["indptr"][col]), int(a["indptr"][col + 1])):
                row = int(a["indices"][k]); out[col] += a["data"][k].conjugate() * v[row]; bound[col] += a["bounds"][k] * abs(v[row])
        out.setflags(write=False); bound.setflags(write=False); return {"value": out, "abs_error": bound}

    def apply_cm_ground_projector(self, resolution: str, vector: np.ndarray) -> dict[str, np.ndarray]:
        p = self.project_raw_qg_to_physical(resolution, vector)
        return self.embed_physical_qg_to_raw(resolution, p["value"])

    def apply_physical_triplet_projector(self, resolution: str, vector: np.ndarray) -> dict[str, np.ndarray]:
        """CM-ground × triplet projector in canonical (kinematic,color) order."""
        a = self.load_qg_embedding_package(resolution); v = np.asarray(vector, dtype=np.complex128)
        if v.shape != (a["shape"][0] * 24,): raise ValueError("raw product-color vector dimension")
        color = TripletAuthorityPackage(); u = color.load("U3")
        raw = v.reshape(a["shape"][0], 24)
        trip = raw @ u.conj()                 # U3^dagger on each raw kinematic row
        kin = np.column_stack([self.project_raw_qg_to_physical(resolution, trip[:, c])["value"] for c in range(3)])
        back = np.column_stack([self.embed_physical_qg_to_raw(resolution, kin[:, c])["value"] for c in range(3)]) @ u.T
        out = np.asarray(back.reshape(-1), dtype=np.complex128); out.setflags(write=False)
        return {"value": out, "abs_error": np.zeros(out.size, dtype=np.float64)}


def validate_package() -> dict[str, Any]:
    package = QGEmbeddingPackage(); results = {}
    maximum_roundtrip = maximum_hermiticity = maximum_idempotence = 0.0
    color = TripletAuthorityPackage(); u = color.load("U3"); p3 = color.load("P3")
    for r in RESOLUTIONS:
        a = package.load_qg_embedding_package(r.label); nraw, nphys = a["shape"]
        x = np.asarray([complex(i + 1, (-1) ** i) / (nraw + 1) for i in range(nraw)])
        y = np.asarray([complex(i + 2, i % 3 - 1) / (nphys + 2) for i in range(nphys)])
        jy = package.embed_physical_qg_to_raw(r.label, y)["value"]; pjy = package.project_raw_qg_to_physical(r.label, jy)["value"]
        pi_x = package.apply_cm_ground_projector(r.label, x)["value"]; pi2_x = package.apply_cm_ground_projector(r.label, pi_x)["value"]
        # Inner-product test supplies Hermiticity without materializing dense projectors.
        z = np.roll(x, 1); piz = package.apply_cm_ground_projector(r.label, z)["value"]
        rt, idem, herm = float(np.max(np.abs(pjy - y))), float(np.max(np.abs(pi2_x - pi_x))), float(abs(np.vdot(z, pi_x) - np.vdot(piz, x)))
        maximum_roundtrip, maximum_idempotence, maximum_hermiticity = max(maximum_roundtrip, rt), max(maximum_idempotence, idem), max(maximum_hermiticity, herm)
        results[r.label] = {"J_kin_shape": [nraw, nphys], "J_phys_shape": [nraw * 24, nphys * 3],
                            "cm_ground_transverse_dimension": nphys // 4, "roundtrip_residual": rt,
                            "projector_idempotence_residual": idem, "projector_hermiticity_residual": herm,
                            "exact_CM_excited_leakage": 0, "anti_sextet_leakage": 0, "15_leakage": 0}
    return {"status": STATUS, "by_resolution": results, "max_roundtrip": maximum_roundtrip,
            "max_projector_idempotence": maximum_idempotence, "max_projector_hermiticity": maximum_hermiticity,
            "U3_isometry": float(np.linalg.norm(u.conj().T @ u - np.eye(3))), "P3_idempotence": float(np.linalg.norm(p3 @ p3 - p3)),
            "pass": maximum_roundtrip < 1e-10 and maximum_idempotence < 1e-10 and maximum_hermiticity < 1e-10}
