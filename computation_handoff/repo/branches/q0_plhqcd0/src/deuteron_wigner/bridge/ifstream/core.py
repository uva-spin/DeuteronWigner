"""Fail-closed bounded-export preflight for C82's canonical record domain.

The implementation intentionally refuses to create a partial stream: C89
requires an exhaustive, persisted, verified record sequence.  Before an
exporter writes its first shard, this module derives the exact record domain
from C78's frozen endpoint-path census and proves that the required safe
record payload cannot fit in the available runtime filesystem.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import shutil
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C88_IFSTREAM_BOUNDED_EXPORT_INCOMPLETE"
NEXT = "C89/IFBOUNDSTREAM — provide a verified storage budget and bounded shard target sufficient for the complete C82 scientific record domain"
SCHEMA = "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
HISTORICAL_C82 = "8e47231ab565f0f729d335b39aa98881176ba166"
SERIALIZER = "UTF8-JSONL-SORTED-KEYS-LF-NO-PICKLE-V1"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(value: Any) -> str:
    return sha256(_canonical(value).encode()).hexdigest()


def _read_json(path: Path) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"unsafe or absent authority record: {path}")
    return json.loads(path.read_text())


def canonical_scientific_schema() -> dict[str, Any]:
    fields = [
        "schema_version", "environment_qualification", "resolution_id", "supported_pair_id",
        "physical_bra_id", "physical_ket_id", "physical_row_index", "physical_column_index",
        "canonical_C80_coordinate_id", "C80_coordinate_equivalence_id",
        "projected_coefficient_identity", "projected_coefficient_midpoint", "certified_absolute_bound",
        "precision", "interval_convention", "terminal_projected_coefficient_status",
        "factor_ownership_identity", "witness_multiplicity", "ordered_witness_endpoint_ancestry_digest",
        "C77_root", "C78_root", "C80_root", "C82_root", "canonical_record_id",
        "contains_no_C80_kernel_value", "contains_no_g_s_squared", "contains_no_coefficient_times_kernel_product",
    ]
    schema = {"schema": SCHEMA, "fields": fields, "serializer": SERIALIZER,
              "prohibitions": ["C80 kernel value", "g_s squared", "coefficient times kernel product"],
              "instance_only_excluded": ["temporary path", "timestamp", "host/process", "shard/checkpoint filename", "current HEAD", "timing"]}
    return {**schema, "schema_sha256": digest(schema)}


def _minimum_record_bytes() -> int:
    """Irreducible JSON bytes for only three required fixed-width identities.

    A real record has 24 additional mandatory scientific fields, so this is a
    strict lower bound rather than a size estimate.
    """
    value = {
        "canonical_C80_coordinate_id": "C80:KAPPA:" + "0" * 64,
        "C80_coordinate_equivalence_id": "C80:KAPPA:" + "0" * 64,
        "canonical_record_id": "C88:REC:" + "0" * 64,
    }
    return len((_canonical(value) + "\n").encode())


def historical_c82_census() -> dict[str, Any]:
    """Read frozen C78 counts without invoking a builder or C82 leaf routine."""
    index = _read_json(ROOT / "data/runtime/c78_ifsupport2/index.json")
    root = _read_json(ROOT / "data/runtime/c78_ifsupport2/root.json")
    rows = []
    for label, record in sorted(index["resolutions"].items()):
        payload = _read_json(ROOT / record["path"])
        counts = payload["counts"]
        if counts["witnesses"] != counts["supported_pairs"]:
            raise ValueError("C78 does not supply exactly one ordered witness per supported pair")
        rows.append({"resolution": label, "supported_pairs": int(counts["supported_pairs"]),
                     "logical_pair_coordinate_records": int(counts["kernel_coordinates"]),
                     "witnesses": int(counts["witnesses"]),
                     "path_count_product_identity": "sum(absorption_path_count * emission_path_count) over C78 ordered witnesses"})
    total = sum(item["logical_pair_coordinate_records"] for item in rows)
    return {"resolution_rows": rows, "supported_pairs": sum(item["supported_pairs"] for item in rows),
            "logical_pair_coordinate_records": total, "C78_root": root["aggregate_sha256"],
            "C78_index_sha256": root["index_sha256"],
            "exact_count_semantics": "C82 uses one leaf per ordered emission-path/absorption-path coordinate; the coordinate includes both raw IDs and both color labels"}


def frozen_inputs() -> dict[str, Any]:
    c87 = _read_json(ROOT / "data/authority/c87_canonical_c72_color_authority/manifest.json")
    c77 = _read_json(ROOT / "data/runtime/c77_qgembed9/root.json")
    c82 = _read_json(ROOT / "data/runtime/c82_ifagg/root.json")
    c80 = _read_json(ROOT / "data/runtime/c80_ifkernel2/root.json")
    census = historical_c82_census()
    return {"historical_C82_commit": HISTORICAL_C82, "environment_qualification": ENVIRONMENT,
            "C87_scientific_root": c87["scientific_root"], "C87_capsule_root": c87["compatibility_root"],
            "C87_claim": c87["claim"], "historical_C72_instance": c87["historical_instance"],
            "C77_root": c77["aggregate_sha256"],
            "C78_root": census["C78_root"], "C80_root": c80["index_sha256"], "C82_root": c82["index_sha256"],
            "pair_order": "C78 witness_groups then emission_endpoint_ids then absorption_endpoint_ids", "schema": canonical_scientific_schema()["schema_sha256"]}


@dataclass(frozen=True)
class ExportLimits:
    max_pairs_in_memory: int = 1
    max_records_in_memory: int = 4096
    max_pending_serialized_bytes: int = 8 * 1024 * 1024
    max_shard_bytes: int = 64 * 1024 * 1024


def bounded_export_preflight(output_dir: Path | None = None, *, limits: ExportLimits = ExportLimits()) -> dict[str, Any]:
    """Return a deterministic pre-write decision; it never creates shards."""
    destination = Path(output_dir or ROOT / "data/runtime/c88_ifstream")
    disk = shutil.disk_usage(destination.parent if destination.parent.exists() else ROOT)
    census = historical_c82_census()
    minimum_per_record = _minimum_record_bytes()
    minimum_total = census["logical_pair_coordinate_records"] * minimum_per_record
    ready = disk.free >= minimum_total
    return {"status": "C88_HISTORICAL_ENVIRONMENT_FROZEN_COMPLETE" if ready else STATUS,
            "next": None if ready else NEXT, "environment_qualification": ENVIRONMENT,
            "historical_C82_commit": HISTORICAL_C82, "inputs": frozen_inputs(), "limits": limits.__dict__,
            "supported_pairs": census["supported_pairs"], "logical_pair_coordinate_records": census["logical_pair_coordinate_records"],
            "minimum_serialized_bytes_per_record": minimum_per_record,
            "minimum_complete_stream_bytes": minimum_total, "available_bytes": disk.free,
            "available_path": str(destination.parent if destination.parent.exists() else ROOT),
            "bounded_export_possible": ready,
            "refusal": None if ready else "No shard, checkpoint, or partial stream is created: the mandatory complete safe stream has an irreducible storage lower bound above available capacity."}
