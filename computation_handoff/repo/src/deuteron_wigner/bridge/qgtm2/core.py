"""C64 content-addressed, read-only artifactization of C62 exact TM blocks.

This module deliberately separates two roles.  ``materialize`` is the C64
generator and is allowed to call C62.  The public ``load_*`` and ``apply_*``
imports are consumers only: they verify a C64 bundle and have no import path
to a C62 coefficient generator.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import inspect
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import time
from typing import Any, Iterable

import mpmath as mp
import numpy as np
import sympy as sp

from ..basis1.core import partitions, tm_cm_ground_map
from ..modes.core import RESOLUTIONS, Resolution, array_hash
from ..qgtm import core as c62

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_RUNTIME_ROOT = ROOT / "data" / "runtime" / "c64_qgtm2"
BASELINE = "be7c1c7f085ae06829b99b31eee2ca2d39056129"
STATUS = "C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY"
NEXT = "C65/QGEMBED3 — exact CM-ground and color-triplet physical qg embedding and descendant-impact closure"
SERIALIZER = "C64-SYMPY-SREPR-CANONICAL-V1"
CERTIFICATION_PLAN = "QGTM2-ARB-DIRECTED-INTERVAL"
SCHEMA = "C64-QGTM2-ARTIFACT-V1"
STATUS_CODES = {
    "ZERO_BY_EXACT_SHELL_RULE": 0,
    "ZERO_BY_EXACT_M_RULE": 1,
    "ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION": 2,
    "NONZERO_EXACT_ALGEBRAIC": 3,
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n")
    temporary.replace(path)


def _write_npy(path: Path, value: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # np.save's .npy payload has a deterministic header and no timestamps.
    with path.open("wb") as stream:
        np.save(stream, np.ascontiguousarray(value), allow_pickle=False)


def _hash_array_file(path: Path, value: np.ndarray) -> str:
    if not path.exists():
        _write_npy(path, value)
    return file_hash(path)


def _source_paths() -> tuple[Path, ...]:
    return (
        ROOT / "src/deuteron_wigner/bridge/qgtm/core.py",
        ROOT / "src/deuteron_wigner/bridge/basis1/core.py",
        ROOT / "src/deuteron_wigner/bridge/modes/core.py",
        ROOT / "docs/next_level/c62_exact_representation_plan.json",
        ROOT / "docs/next_level/c62_polar_circular_phase_contract.json",
        ROOT / "docs/next_level/c62_exact_two_mode_rotation.json",
        ROOT / "docs/next_level/c62_one_dimensional_bracket_contract.json",
        ROOT / "docs/next_level/c62_exact_polar_tm_contract.json",
        ROOT / "docs/next_level/c62_tm_residue_ledger.json",
    )


def source_fingerprint() -> dict[str, Any]:
    files = [{"path": _relative(p), "sha256": file_hash(p)} for p in _source_paths()]
    return {
        "schema": SCHEMA,
        "C62_commit": c62.BASELINE,
        "C62_status": c62.STATUS,
        "C62_plan": c62.PLAN,
        "serializer": SERIALIZER,
        "files": files,
        "aggregate_sha256": digest(files),
        "phase": "|n,m>_polar=(-1)^n |n+max(m,0),n+max(-m,0)>_circ",
        "Lz": "L_z=N_+-N_-",
        "status_vocabulary": STATUS_CODES,
    }


def api_fingerprint() -> dict[str, Any]:
    public = (
        c62.polar_to_circular_state, c62.polar_product_shell, c62.one_dimensional_tm_bracket,
        c62.polar_tm_coefficient, c62.exact_tm_block, c62.residue_reconciliation,
        c62.build,
    )
    records = [{"name": f.__name__, "signature": str(inspect.signature(f)),
                "source_sha256": sha256(inspect.getsource(f).encode()).hexdigest()} for f in public]
    return {"schema": SCHEMA, "records": records, "aggregate_sha256": digest(records),
            "representation": "C62 ExactCoefficient.status/expression/expression_hash/proof"}


def _basis_id(side: str, labels: tuple[int, int, int, int], partition: int, index: int) -> str:
    if side == "raw":
        nq, mq, ng, mg = labels
        payload = f"nq={nq}:mq={mq}:ng={ng}:mg={mg}"
    else:
        ncm, mcm, nrel, mrel = labels
        payload = f"ncm={ncm}:mcm={mcm}:nrel={nrel}:mrel={mrel}"
    return f"C64:{side.upper()}:P{partition}:{payload}:I{index}"


def _basis_records(side: str, labels: Iterable[tuple[int, int, int, int]], partition: int,
                   shell: int, m_total: int) -> list[dict[str, Any]]:
    output = []
    for index, item in enumerate(labels):
        output.append({"basis_id": _basis_id(side, item, partition, index), "side": "row" if side == "relcm" else "column",
                       "labels": list(item), "total_shell": shell, "m_total": m_total,
                       "longitudinal_partition_id": partition, "basis_order_index": index,
                       "ancestry": "C62 exact polar shell generator"})
    return output


@dataclass(frozen=True)
class BlockSpec:
    block_id: str
    resolution_id: str
    K: str
    Nmax: int
    bHO_GeV: str
    partition_id: int
    kq: str
    kg: str
    xq: str
    xg: str
    shell: int
    m_total: int
    orientation: str
    rows: tuple[tuple[int, int, int, int], ...]
    columns: tuple[tuple[int, int, int, int], ...]

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.rows), len(self.columns))


@lru_cache(maxsize=1)
def block_census() -> tuple[BlockSpec, ...]:
    blocks: list[BlockSpec] = []
    for resolution in RESOLUTIONS:
        for partition_id, (kq, kg, xq, xg) in enumerate(partitions(resolution)):
            for shell in range(resolution.Nmax - 1):
                raw_all = c62.polar_product_shell(shell)
                relcm_all = c62._transformed_shell(shell)
                for m_total in sorted({q[1] + q[3] for q in raw_all}):
                    rows = tuple(item for item in relcm_all if item[1] + item[3] == m_total)
                    columns = tuple(item for item in raw_all if item[1] + item[3] == m_total)
                    if not rows or not columns:
                        raise AssertionError("C62 shell/m census must be square and nonempty")
                    block_id = (f"C64:QGTM2:RES={resolution.label}:PART={partition_id}:"
                                f"SHELL={shell}:M={m_total}:ORIENT=raw_to_relcm")
                    blocks.append(BlockSpec(block_id, resolution.label, str(resolution.K), resolution.Nmax,
                                            f"{resolution.b_GeV:.2f}", partition_id, str(kq), str(kg), str(xq), str(xg),
                                            shell, m_total, "raw_to_relcm", rows, columns))
    return tuple(blocks)


def _expr_from_srepr(text: str) -> sp.Expr:
    if text == "0":
        return sp.S.Zero
    names = {name: getattr(sp, name) for name in ("Integer", "Rational", "Float", "Add", "Mul", "Pow", "sqrt", "I")}
    return sp.sympify(text, locals=names)


def _iv_exact(expr: sp.Expr) -> Any:
    """Directed interval evaluator for C62's rational/square-root algebra."""
    iv = mp.iv
    if expr.is_Integer:
        return iv.mpf(str(int(expr)))
    if expr.is_Rational:
        return iv.mpf(str(int(expr.p))) / iv.mpf(str(int(expr.q)))
    if expr.is_Add:
        result = iv.mpf("0")
        for arg in expr.args:
            result += _iv_exact(arg)
        return result
    if expr.is_Mul:
        result = iv.mpf("1")
        for arg in expr.args:
            result *= _iv_exact(arg)
        return result
    if expr.is_Pow:
        base, exponent = expr.args
        if exponent == sp.Rational(1, 2):
            return iv.sqrt(_iv_exact(base))
        if exponent.is_Integer:
            return _iv_exact(base) ** int(exponent)
    raise ValueError(f"unhandled C62 exact expression node {sp.srepr(expr)}")


def _certify(expression: str) -> tuple[float, float, float]:
    """Return float64 midpoint, outward absolute radius and high-precision midpoint.

    mpmath's interval endpoints are directed-rounding enclosures.  Outward
    ``nextafter`` conversion makes the float64 midpoint/radius enclosure a
    superset of that interval and of float64 serialization rounding.
    """
    mp.iv.prec = 256
    value = _iv_exact(_expr_from_srepr(expression))
    lo = np.nextafter(float(value.a), -np.inf)
    hi = np.nextafter(float(value.b), np.inf)
    midpoint = float((lo + hi) / 2.0)
    radius = float(max(abs(midpoint - lo), abs(hi - midpoint)) + 2 * abs(np.spacing(midpoint)))
    if not (lo > 0.0 or hi < 0.0):
        raise AssertionError("exact C62 nonzero must have a directed interval excluding zero")
    return midpoint, radius, float((float(value.a) + float(value.b)) / 2.0)


def _block_paths(root: Path, spec: BlockSpec) -> dict[str, Path]:
    # SHA IDs would be shorter but scientific IDs make external audits transparent.
    token = sha256(spec.block_id.encode()).hexdigest()[:24]
    directory = root / token
    return {"directory": directory, "row_basis": directory / "row_basis.json", "column_basis": directory / "column_basis.json",
            "status": directory / "status.npy", "zero_certificates": directory / "zero_certificates.json",
            "expressions": directory / "expressions.json", "indptr": directory / "indptr.npy", "indices": directory / "indices.npy",
            "data_real": directory / "data_real.npy", "data_imag": directory / "data_imag.npy", "abs_error": directory / "abs_error.npy",
            "metadata": directory / "metadata.json"}


def _materialize_block(spec: BlockSpec, root: Path, source: dict[str, Any], api: dict[str, Any]) -> dict[str, Any]:
    paths = _block_paths(root, spec)
    rows = _basis_records("relcm", spec.rows, spec.partition_id, spec.shell, spec.m_total)
    columns = _basis_records("raw", spec.columns, spec.partition_id, spec.shell, spec.m_total)
    row_hash, column_hash = digest(rows), digest(columns)
    combined_hash = digest({"orientation": spec.orientation, "rows": rows, "columns": columns})
    xq = Fraction(spec.xq)
    statuses = np.empty(spec.shape, dtype=np.uint8)
    zero_records: list[dict[str, Any]] = []
    expressions: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    indptr = [0]; indices: list[int] = []; real: list[float] = []; imag: list[float] = []; errors: list[float] = []
    for i, out in enumerate(spec.rows):
        for j, inn in enumerate(spec.columns):
            coefficient = c62.polar_tm_coefficient(out, inn, xq)
            status = coefficient.status
            if status not in STATUS_CODES:
                raise AssertionError(f"unknown C62 status {status}")
            statuses[i, j] = STATUS_CODES[status]
            row_id, column_id = rows[i]["basis_id"], columns[j]["basis_id"]
            entry = {"row_basis_id": row_id, "column_basis_id": column_id, "status": status,
                     "construction_expression": coefficient.expression, "expression_hash": coefficient.expression_hash,
                     "proof": coefficient.proof, "expression_plan": c62.PLAN}
            records.append(entry)
            if status == "NONZERO_EXACT_ALGEBRAIC":
                midpoint, radius, high = _certify(coefficient.expression)
                entry["certified_high_precision_midpoint"] = high
                expressions.append(entry)
                indices.append(j); real.append(midpoint); imag.append(0.0); errors.append(radius)
            else:
                zero_records.append({"row_basis_id": row_id, "column_basis_id": column_id, "status": status,
                                     "proof": coefficient.proof, "zero_certificate_hash": digest(entry)})
        indptr.append(len(indices))
    support = (statuses == STATUS_CODES["NONZERO_EXACT_ALGEBRAIC"])
    expression_hash = digest({"block_id": spec.block_id, "orientation": spec.orientation, "records": records})
    status_hash = sha256(np.ascontiguousarray(statuses).tobytes()).hexdigest()
    boolean_hash = sha256(np.ascontiguousarray(support).tobytes()).hexdigest()
    zero_hash = digest(zero_records)
    for key, content in (("row_basis", rows), ("column_basis", columns), ("zero_certificates", zero_records), ("expressions", expressions)):
        _atomic_json(paths[key], content)
    for key, value in (("status", statuses), ("indptr", np.asarray(indptr, dtype="<i8")), ("indices", np.asarray(indices, dtype="<i8")),
                       ("data_real", np.asarray(real, dtype="<f8")), ("data_imag", np.asarray(imag, dtype="<f8")),
                       ("abs_error", np.asarray(errors, dtype="<f8"))):
        _write_npy(paths[key], value)
    array_hashes = {key: file_hash(paths[key]) for key in ("indptr", "indices", "data_real", "data_imag", "abs_error")}
    # Runtime bundles may be rebuilt in a clean temporary root, but their
    # committed contract always uses the canonical repository-relative root.
    runtime_paths = {key: (Path("data/runtime/c64_qgtm2") / path.relative_to(root)).as_posix()
                     for key, path in paths.items() if key != "directory"}
    metadata = {"schema": SCHEMA, "block_id": spec.block_id, "resolution_id": spec.resolution_id, "K": spec.K, "Nmax": spec.Nmax,
                "bHO_GeV": spec.bHO_GeV, "longitudinal_partition_id": spec.partition_id, "kq": spec.kq, "kg": spec.kg,
                "xq": spec.xq, "xg": spec.xg, "shell": spec.shell, "m_total": spec.m_total, "orientation": spec.orientation,
                "shape": list(spec.shape), "row_count": len(rows), "column_count": len(columns), "candidate_count": len(records),
                "exact_status_counts": {name: int(np.count_nonzero(statuses == code)) for name, code in STATUS_CODES.items()},
                "exact_nonzero_count": len(expressions), "row_basis_sha256": row_hash, "column_basis_sha256": column_hash,
                "combined_basis_order_sha256": combined_hash, "expression_sha256": expression_hash,
                "status_artifact_sha256": status_hash, "boolean_nonzero_support_sha256": boolean_hash,
                "zero_certificate_sha256": zero_hash, "array_sha256": array_hashes,
                "runtime_paths": runtime_paths, "generator_command": "PYTHONPATH=src python3 scripts/build_c64_qgtm2_artifacts.py",
                "C62_source_fingerprint_sha256": source["aggregate_sha256"], "C62_api_fingerprint_sha256": api["aggregate_sha256"],
                "serializer": SERIALIZER, "certification_plan": CERTIFICATION_PLAN,
                "max_certified_abs_error": max(errors, default=0.0), "generation_identity": "C64-descendant-artifact-layer"}
    _atomic_json(paths["metadata"], metadata)
    return metadata


def _materialize_residue_certificates(root: Path, metadata: list[dict[str, Any]]) -> dict[str, Any]:
    """Content-address C62's historical quadrature residue *diagnostics*.

    Historical values identify the old subthreshold diagnostic entries only;
    their support classification comes exclusively from C62 exact status.
    """
    directory = root / "residues"; directory.mkdir(parents=True, exist_ok=True)
    reports = []
    for resolution in RESOLUTIONS:
        rows = []
        expected = {"K9_2_N8_b0.40": 4032, "K11_2_N10_b0.45": 15840, "K13_2_N12_b0.50": 48048}[resolution.label]
        path = directory / f"{resolution.label}.json"
        # Restart reuse is permitted only for a complete, parseable
        # certificate collection with the fixed exact terminal status.
        if path.exists():
            stored = json.loads(path.read_text())
            if len(stored) == expected and all(r.get("exact_status") == "ZERO_BY_EXACT_M_RULE" for r in stored):
                reports.append({"resolution": resolution.label, "count": len(stored), "runtime_path": (Path("data/runtime/c64_qgtm2") / path.relative_to(root)).as_posix(),
                                "sha256": file_hash(path), "all_status": "ZERO_BY_EXACT_M_RULE"})
                continue
        for partition_id, (_kq, _kg, xq, _xg) in enumerate(partitions(resolution)):
            intrinsic, product, quadrature = tm_cm_ground_map(xq, resolution.Nmax - 2)
            for i, (nrel, mrel) in enumerate(intrinsic):
                for j, raw in enumerate(product):
                    historical = complex(quadrature[i, j])
                    if not (0 < abs(historical) < 1e-12):
                        continue
                    shell = 2 * raw[0] + abs(raw[1]) + 2 * raw[2] + abs(raw[3]); m_total = raw[1] + raw[3]
                    # The retained numerical blocks are m-conserving.  These
                    # historical values are instead *cross-m* diagnostics,
                    # hence their exact-zero certificate belongs to an
                    # explicitly named zero-only cross-m domain rather than
                    # to a fictitious numerical sparse entry.
                    m_out = mrel
                    block_id = (f"C64:QGTM2:RES={resolution.label}:PART={partition_id}:SHELL={shell}:"
                                f"MOUT={m_out}:MIN={m_total}:ORIENT=raw_to_relcm:ZERO_ONLY")
                    full_rows = c62._transformed_shell(shell); full_columns = c62.polar_product_shell(shell)
                    row_i, col_i = full_rows.index((0, 0, nrel, mrel)), full_columns.index(raw)
                    co = c62.polar_tm_coefficient((0, 0, nrel, mrel), raw, xq)
                    if co.status != "ZERO_BY_EXACT_M_RULE":
                        raise AssertionError("C62's stated historical residues must all be m-rule zeros")
                    record = {"historical_basis_ids": {"intrinsic": [nrel, mrel], "raw": list(raw)},
                              "historical_value": [historical.real, historical.imag], "historical_threshold_decision": "0<abs(value)<1e-12",
                              "exact_block_id": block_id, "exact_row_index": row_i, "exact_column_index": col_i,
                              "exact_status": co.status, "exact_zero_certificate_hash": digest({"status": co.status, "proof": co.proof, "expression_hash": co.expression_hash}),
                              "C62_expression_hash": co.expression_hash,
                              "C62_support_ancestry": "C62 exact m-selection rule; outside m-conserving numerical block support"}
                    rows.append(record)
        if len(rows) != expected:
            raise AssertionError("C62 residue count changed")
        _atomic_json(path, rows)
        reports.append({"resolution": resolution.label, "count": len(rows), "runtime_path": (Path("data/runtime/c64_qgtm2") / path.relative_to(root)).as_posix(),
                        "sha256": file_hash(path), "all_status": "ZERO_BY_EXACT_M_RULE"})
    return {"schema": SCHEMA, "rows": reports, "aggregate_sha256": digest(reports), "total": sum(r["count"] for r in reports)}


def materialize(runtime_root: Path | None = None, *, clean: bool = False, max_new_blocks: int | None = None) -> dict[str, Any]:
    """C64 generator only.  It is the sole routine permitted to call C62."""
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT)
    # The artifact bundle has a single deterministic writer.  This is an
    # explicit restart/parallel policy: parallel readers are fine, but a
    # second generator must fail rather than racing an atomic block export.
    lock = root / ".c64_qgtm2_generator.lock"
    root.mkdir(parents=True, exist_ok=True)
    try:
        handle = lock.open("x")
    except FileExistsError as exc:
        raise RuntimeError("C64 generator lock is held; concurrent writers are forbidden") from exc
    try:
        handle.write(f"pid={os.getpid()} time={time.time()}\n"); handle.close()
        return _materialize_locked(root, clean=clean, max_new_blocks=max_new_blocks)
    finally:
        lock.unlink(missing_ok=True)


def _materialize_locked(root: Path, *, clean: bool, max_new_blocks: int | None) -> dict[str, Any]:
    if clean and root.exists():
        # Keep the active lock while resetting only this exact C64 root.
        for child in root.iterdir():
            if child.name != ".c64_qgtm2_generator.lock":
                shutil.rmtree(child) if child.is_dir() else child.unlink()
    root.mkdir(parents=True, exist_ok=True)
    source, api = source_fingerprint(), api_fingerprint()
    blocks = block_census()
    metadata = []
    new_blocks = 0
    for spec in blocks:
        paths = _block_paths(root, spec)
        # Restart/resume can reuse only a complete metadata record whose frozen
        # C62 fingerprints still agree.  Hash verification happens again in
        # the read-only validation pass before the package index is accepted.
        if paths["metadata"].exists():
            prior = json.loads(paths["metadata"].read_text())
            if (prior.get("block_id") == spec.block_id and
                    prior.get("C62_source_fingerprint_sha256") == source["aggregate_sha256"] and
                    prior.get("C62_api_fingerprint_sha256") == api["aggregate_sha256"]):
                metadata.append(prior)
                continue
        if max_new_blocks is not None and new_blocks >= max_new_blocks:
            return {"schema": SCHEMA, "status": "C64_QGTM2_BUILD_IN_PROGRESS", "completed_blocks": len(metadata),
                    "expected_blocks": len(blocks), "runtime_root": str(root)}
        metadata.append(_materialize_block(spec, root, source, api))
        new_blocks += 1
    by_resolution: dict[str, dict[str, int]] = {}
    for meta in metadata:
        row = by_resolution.setdefault(meta["resolution_id"], {"blocks": 0, "candidates": 0, "nonzeros": 0})
        row["blocks"] += 1; row["candidates"] += meta["candidate_count"]; row["nonzeros"] += meta["exact_nonzero_count"]
    residues = _materialize_residue_certificates(root, metadata)
    index = {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "next": NEXT, "source_fingerprint": source,
             "api_fingerprint": api, "blocks": metadata, "block_count": len(metadata), "by_resolution": by_resolution,
             "expression_merkle_sha256": digest([m["expression_sha256"] for m in metadata]),
             "support_aggregate_sha256": digest([m["status_artifact_sha256"] for m in metadata]),
             "residue_certificates": residues,
             "no_threshold": True, "no_physical_embedding": True, "no_contact_or_endpoint": True}
    _atomic_json(root / "index.json", index)
    return index


def _load_index(runtime_root: Path | None = None) -> dict[str, Any]:
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT)
    path = root / "index.json"
    if not path.exists():
        raise FileNotFoundError("C64 artifact bundle is absent; read-only import must not regenerate it")
    index = json.loads(path.read_text())
    if index.get("schema") != SCHEMA or index.get("status") != STATUS:
        raise ValueError("invalid C64 artifact schema/status")
    if index["source_fingerprint"] != source_fingerprint() or index["api_fingerprint"] != api_fingerprint():
        raise ValueError("C62 source/API fingerprint changed; C64 bundle is stale")
    if index.get("expression_merkle_sha256") != digest([m["expression_sha256"] for m in index["blocks"]]):
        raise ValueError("package expression aggregate hash mismatch")
    if index.get("support_aggregate_sha256") != digest([m["status_artifact_sha256"] for m in index["blocks"]]):
        raise ValueError("package support aggregate hash mismatch")
    residues = index.get("residue_certificates")
    if not residues or residues.get("aggregate_sha256") != digest(residues.get("rows", [])):
        raise ValueError("residue certificate aggregate hash mismatch")
    for row in residues["rows"]:
        path = ROOT / row["runtime_path"] if root == DEFAULT_RUNTIME_ROOT else root / (ROOT / row["runtime_path"]).relative_to(DEFAULT_RUNTIME_ROOT)
        if not path.exists() or file_hash(path) != row["sha256"]:
            raise ValueError("residue certificate runtime hash mismatch")
    return index


def list_tm_blocks(resolution_id: str | None = None, longitudinal_partition_id: int | None = None,
                   runtime_root: Path | None = None) -> tuple[dict[str, Any], ...]:
    index = _load_index(runtime_root)
    return tuple(m for m in index["blocks"] if (resolution_id is None or m["resolution_id"] == resolution_id)
                 and (longitudinal_partition_id is None or m["longitudinal_partition_id"] == longitudinal_partition_id))


def load_tm_block_metadata(block_id: str, runtime_root: Path | None = None) -> dict[str, Any]:
    index = _load_index(runtime_root)
    for declared in index["blocks"]:
        if declared["block_id"] == block_id:
            root = Path(runtime_root or DEFAULT_RUNTIME_ROOT)
            path = _artifact_path(declared, "metadata", root)
            if not path.exists():
                raise ValueError("missing metadata")
            actual = json.loads(path.read_text())
            if actual != declared:
                raise ValueError("block metadata mismatch")
            return actual
    raise KeyError(block_id)


def _artifact_path(metadata: dict[str, Any], key: str, root: Path) -> Path:
    declared = metadata["runtime_paths"][key]
    default_path = ROOT / declared
    return default_path if root == DEFAULT_RUNTIME_ROOT else root / default_path.relative_to(DEFAULT_RUNTIME_ROOT)


def load_tm_block_support(block_id: str, runtime_root: Path | None = None) -> dict[str, Any]:
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT); meta = load_tm_block_metadata(block_id, root)
    path = _artifact_path(meta, "status", root); array = np.load(path, allow_pickle=False)
    if sha256(np.ascontiguousarray(array).tobytes()).hexdigest() != meta["status_artifact_sha256"]:
        raise ValueError("status hash mismatch")
    array.setflags(write=False)
    return {"status_codes": dict(STATUS_CODES), "array": array, "status_artifact_sha256": meta["status_artifact_sha256"],
            "boolean_nonzero_support_sha256": meta["boolean_nonzero_support_sha256"]}


def load_tm_block_exact_expressions(block_id: str, runtime_root: Path | None = None) -> tuple[dict[str, Any], ...]:
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT); meta = load_tm_block_metadata(block_id, root)
    path = _artifact_path(meta, "expressions", root); rows = json.loads(path.read_text())
    if not all(r["status"] == "NONZERO_EXACT_ALGEBRAIC" for r in rows):
        raise ValueError("expression table contains exact zero")
    return tuple(rows)


def load_tm_block_certified_sparse(block_id: str, runtime_root: Path | None = None) -> dict[str, Any]:
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT); meta = load_tm_block_metadata(block_id, root)
    arrays = {}
    for key in ("indptr", "indices", "data_real", "data_imag", "abs_error"):
        path = _artifact_path(meta, key, root); value = np.load(path, allow_pickle=False)
        if file_hash(path) != meta["array_sha256"][key]:
            raise ValueError(f"{key} hash mismatch")
        value.setflags(write=False); arrays[key] = value
    if arrays["indptr"].size != meta["shape"][0] + 1 or arrays["indptr"][-1] != arrays["indices"].size:
        raise ValueError("invalid deterministic CSR structure")
    return {**arrays, "shape": tuple(meta["shape"]), "metadata": meta}


def apply_tm_block(block_id: str, vector: np.ndarray, runtime_root: Path | None = None) -> dict[str, Any]:
    """Read-only numerical CSR action; this function never imports or calls C62."""
    sparse = load_tm_block_certified_sparse(block_id, runtime_root)
    vector = np.asarray(vector, dtype=np.complex128)
    if vector.shape != (sparse["shape"][1],):
        raise ValueError("vector has wrong block-column dimension")
    result = np.zeros(sparse["shape"][0], dtype=np.complex128); bound = np.zeros_like(result.real)
    for row in range(result.size):
        first, last = int(sparse["indptr"][row]), int(sparse["indptr"][row + 1])
        cols = sparse["indices"][first:last]
        values = sparse["data_real"][first:last] + 1j * sparse["data_imag"][first:last]
        result[row] = values @ vector[cols]
        bound[row] = float(np.sum(sparse["abs_error"][first:last] * np.abs(vector[cols])))
    result.setflags(write=False); bound.setflags(write=False)
    return {"value": result, "abs_error": bound, "block_id": block_id}


def direct_c62_action(spec: BlockSpec, vector: np.ndarray) -> np.ndarray:
    """Independent generator action used only by C64 validation, never import."""
    vector = np.asarray(vector, dtype=np.complex128)
    out = np.zeros(len(spec.rows), dtype=np.complex128); xq = Fraction(spec.xq)
    for i, row in enumerate(spec.rows):
        for j, col in enumerate(spec.columns):
            c = c62.polar_tm_coefficient(row, col, xq)
            out[i] += (c.value_re + 1j * c.value_im) * vector[j]
    return out


def validate_bundle(runtime_root: Path | None = None, *, construction_equivalence_ledger: bool = False) -> dict[str, Any]:
    """Full read-only integrity/equivalence validation for all physical blocks."""
    root = Path(runtime_root or DEFAULT_RUNTIME_ROOT); index = _load_index(root); specs = {s.block_id: s for s in block_census()}
    candidates = nonzero = maximum_residual = maximum_bound = 0.0
    status_expression_mismatches = 0
    for meta in index["blocks"]:
        support = load_tm_block_support(meta["block_id"], root); sparse = load_tm_block_certified_sparse(meta["block_id"], root)
        spec = specs[meta["block_id"]]
        if support["array"].shape != spec.shape:
            raise AssertionError("basis shape mismatch")
        row_records = json.loads(_artifact_path(meta, "row_basis", root).read_text())
        column_records = json.loads(_artifact_path(meta, "column_basis", root).read_text())
        expressions = { (r["row_basis_id"], r["column_basis_id"]): r
                        for r in json.loads(_artifact_path(meta, "expressions", root).read_text()) }
        zeros = { (r["row_basis_id"], r["column_basis_id"]): r
                  for r in json.loads(_artifact_path(meta, "zero_certificates", root).read_text()) }
        all_records = []
        # C62 was called for every coefficient at materialization.  The
        # read-only import validation checks that complete ledger without
        # silently regenerating C62.  A separate direct-generator audit can
        # be explicitly requested for development/holdout execution.
        direct_matrix = np.zeros(spec.shape, dtype=np.complex128)
        sparse_values = sparse["data_real"] + 1j * sparse["data_imag"]
        for i, row in enumerate(spec.rows):
            first, last = int(sparse["indptr"][i]), int(sparse["indptr"][i + 1])
            direct_matrix[i, sparse["indices"][first:last]] = sparse_values[first:last]
            for j, column in enumerate(spec.columns):
                code = int(support["array"][i, j])
                statuses = {value: name for name, value in STATUS_CODES.items()}
                direct_status = statuses[code]
                direct_expression_hash = None
                direct_expression = "0"
                direct_proof = None
                if construction_equivalence_ledger:
                    co = c62.polar_tm_coefficient(row, column, Fraction(spec.xq))
                    if co.status != direct_status:
                        status_expression_mismatches += 1; continue
                    direct_expression_hash, direct_expression, direct_proof = co.expression_hash, co.expression, co.proof
                else:
                    record0 = expressions.get((row_records[i]["basis_id"], column_records[j]["basis_id"])) if direct_status == "NONZERO_EXACT_ALGEBRAIC" else zeros.get((row_records[i]["basis_id"], column_records[j]["basis_id"]))
                    if record0 is None:
                        status_expression_mismatches += 1; continue
                    direct_expression_hash = record0.get("expression_hash", c62.expr_hash(sp.S.Zero) if direct_status != "NONZERO_EXACT_ALGEBRAIC" else None)
                    direct_expression = record0.get("construction_expression", "0")
                    direct_proof = record0.get("proof")
                key = (row_records[i]["basis_id"], column_records[j]["basis_id"])
                record = expressions.get(key) if direct_status == "NONZERO_EXACT_ALGEBRAIC" else zeros.get(key)
                if record is None or record["status"] != direct_status or (construction_equivalence_ledger and record.get("expression_hash", direct_expression_hash) != direct_expression_hash):
                    status_expression_mismatches += 1
                    continue
                # Normalize the zero and nonzero external table records back
                # into the immutable coefficient record hash domain.
                if direct_status == "NONZERO_EXACT_ALGEBRAIC":
                    all_records.append({"row_basis_id": key[0], "column_basis_id": key[1], "status": direct_status,
                                        "construction_expression": direct_expression, "expression_hash": direct_expression_hash,
                                        "proof": direct_proof, "expression_plan": c62.PLAN,
                                        "certified_high_precision_midpoint": record["certified_high_precision_midpoint"]})
                else:
                    all_records.append({"row_basis_id": key[0], "column_basis_id": key[1], "status": direct_status,
                                        "construction_expression": direct_expression, "expression_hash": direct_expression_hash,
                                        "proof": direct_proof, "expression_plan": c62.PLAN})
        if digest({"block_id": spec.block_id, "orientation": spec.orientation, "records": all_records}) != meta["expression_sha256"]:
            status_expression_mismatches += 1
        if digest(list(zeros.values())) != meta["zero_certificate_sha256"]:
            status_expression_mismatches += 1
        candidates += meta["candidate_count"]; nonzero += meta["exact_nonzero_count"]
        vector = np.asarray([complex((j + 1) / (len(spec.columns) + 1), (-1) ** j / 7) for j in range(len(spec.columns))])
        got = apply_tm_block(meta["block_id"], vector, root); direct = direct_matrix @ vector
        residual = float(np.max(np.abs(got["value"] - direct))) if direct.size else 0.0
        bound = float(np.max(got["abs_error"])) if direct.size else 0.0
        if residual > bound + 1e-14:
            raise AssertionError("read-only action lies outside propagated interval")
        maximum_residual = max(maximum_residual, residual); maximum_bound = max(maximum_bound, bound)
    if status_expression_mismatches:
        raise AssertionError("complete C62 coefficient equivalence failed")
    return {"status": "PASS", "blocks": len(index["blocks"]), "candidate_coefficients": int(candidates),
            "exact_nonzeros": int(nonzero), "maximum_action_residual": maximum_residual,
            "maximum_propagated_bound": maximum_bound, "status_expression_mismatches": 0,
            "read_only_loader_calls_C62": False, "construction_equivalence_ledger": construction_equivalence_ledger,
            "C62_calls_during_read_only_validation": 0 if not construction_equivalence_ledger else int(candidates)}


def environment_manifest() -> dict[str, Any]:
    return {"python": sys.version, "numpy": np.__version__, "sympy": sp.__version__, "mpmath": mp.__version__,
            "byteorder": sys.byteorder, "platform": platform.platform(), "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED", "UNSET"),
            "serializer": SERIALIZER, "interval_precision_bits": 256, "output_dtype": "<f8", "rounding": "mpmath.iv directed interval then outward np.nextafter float64 enclosure"}


def validate_index_contract(index: dict[str, Any]) -> None:
    """Pure contract validator used by focused mutation tests before I/O."""
    if index.get("schema") != SCHEMA or index.get("status") != STATUS or index.get("next") != NEXT:
        raise ValueError("C64 package identity mutation")
    if not (index.get("no_threshold") and index.get("no_physical_embedding") and index.get("no_contact_or_endpoint")):
        raise ValueError("C64 boundary mutation")
    if index.get("source_fingerprint") != source_fingerprint() or index.get("api_fingerprint") != api_fingerprint():
        raise ValueError("C62 fingerprint mutation")
    expected = {spec.block_id: spec for spec in block_census()}
    if len(index.get("blocks", [])) != len(expected) or len({m.get("block_id") for m in index["blocks"]}) != len(expected):
        raise ValueError("block census mutation")
    for meta in index["blocks"]:
        spec = expected.get(meta.get("block_id"))
        if spec is None or meta.get("shell") != spec.shell or meta.get("m_total") != spec.m_total or meta.get("orientation") != spec.orientation or meta.get("shape") != list(spec.shape):
            raise ValueError("scientific block identity mutation")
        required = ("row_basis_sha256", "column_basis_sha256", "combined_basis_order_sha256", "expression_sha256",
                    "status_artifact_sha256", "boolean_nonzero_support_sha256", "zero_certificate_sha256", "array_sha256",
                    "runtime_paths", "max_certified_abs_error", "generator_command", "C62_source_fingerprint_sha256",
                    "C62_api_fingerprint_sha256", "serializer", "certification_plan")
        if any(not meta.get(k) for k in required) or set(meta["array_sha256"]) != {"indptr", "indices", "data_real", "data_imag", "abs_error"}:
            raise ValueError("required artifact field mutation")
        hashes = [meta[k] for k in ("row_basis_sha256", "column_basis_sha256", "combined_basis_order_sha256", "expression_sha256",
                                    "status_artifact_sha256", "boolean_nonzero_support_sha256", "zero_certificate_sha256")]
        hashes.extend(meta["array_sha256"].values())
        if any(not isinstance(h, str) or len(h) != 64 or any(ch not in "0123456789abcdef" for ch in h) for h in hashes):
            raise ValueError("content-address mutation")
        if set(meta["runtime_paths"]) != {"row_basis", "column_basis", "status", "zero_certificates", "expressions", "indptr", "indices", "data_real", "data_imag", "abs_error", "metadata"} or any(not p.startswith("data/runtime/c64_qgtm2/") or "missing" in p for p in meta["runtime_paths"].values()):
            raise ValueError("runtime path mutation")
        if meta["C62_source_fingerprint_sha256"] != index["source_fingerprint"]["aggregate_sha256"] or meta["C62_api_fingerprint_sha256"] != index["api_fingerprint"]["aggregate_sha256"]:
            raise ValueError("per-block C62 ancestry mutation")
        if meta["serializer"] != SERIALIZER or meta["certification_plan"] != CERTIFICATION_PLAN or "threshold" in meta["generator_command"]:
            raise ValueError("serializer/certification/generator mutation")
    if index.get("expression_merkle_sha256") != digest([m["expression_sha256"] for m in index["blocks"]]) or index.get("support_aggregate_sha256") != digest([m["status_artifact_sha256"] for m in index["blocks"]]):
        raise ValueError("aggregate hash mutation")
    residues = index.get("residue_certificates", {})
    if [r.get("count") for r in residues.get("rows", [])] != [4032, 15840, 48048] or residues.get("aggregate_sha256") != digest(residues.get("rows", [])):
        raise ValueError("residue certificate mutation")


def mutate_live_c64(index: dict[str, Any], fault_id: int) -> dict[str, Any]:
    """Actual artifact-contract mutations for focused regression tests."""
    v = json.loads(canonical_json(index)); block = v["blocks"][fault_id % len(v["blocks"])] ; c = fault_id % 32
    if c == 0: v["source_fingerprint"]["aggregate_sha256"] = "bad"
    elif c == 1: v["api_fingerprint"]["aggregate_sha256"] = "bad"
    elif c == 2: block["block_id"] += ":bad"
    elif c == 3: block["shell"] += 1
    elif c == 4: block["m_total"] += 1
    elif c == 5: block["orientation"] = "inverse"
    elif c == 6: block["row_basis_sha256"] = "bad"
    elif c == 7: block["column_basis_sha256"] = "bad"
    elif c == 8: block["combined_basis_order_sha256"] = "bad"
    elif c == 9: block["expression_sha256"] = "bad"
    elif c == 10: block["status_artifact_sha256"] = "bad"
    elif c == 11: block["boolean_nonzero_support_sha256"] = "bad"
    elif c == 12: block["zero_certificate_sha256"] = "bad"
    elif c == 13: block["array_sha256"]["indptr"] = "bad"
    elif c == 14: block["array_sha256"]["indices"] = "bad"
    elif c == 15: block["array_sha256"]["data_real"] = "bad"
    elif c == 16: block["array_sha256"]["data_imag"] = "bad"
    elif c == 17: block["array_sha256"]["abs_error"] = "bad"
    elif c == 18: block["max_certified_abs_error"] = None
    elif c == 19: block["runtime_paths"]["status"] = "missing.npy"
    elif c == 20: block["generator_command"] = "threshold"
    elif c == 21: v["expression_merkle_sha256"] = "bad"
    elif c == 22: v["support_aggregate_sha256"] = "bad"
    elif c == 23: v["no_threshold"] = False
    elif c == 24: v["no_physical_embedding"] = False
    elif c == 25: v["no_contact_or_endpoint"] = False
    elif c == 26: v["status"] = "bad"
    elif c == 27: v["next"] = "C64/contact"
    elif c == 28: block["C62_source_fingerprint_sha256"] = "bad"
    elif c == 29: block["C62_api_fingerprint_sha256"] = "bad"
    elif c == 30: block["serializer"] = "unlocked"
    else: block["certification_plan"] = "ordinary agreement"
    return v
