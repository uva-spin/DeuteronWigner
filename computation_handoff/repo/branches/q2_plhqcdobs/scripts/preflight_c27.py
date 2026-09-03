#!/usr/bin/env python3
"""Deterministic conditional-entry preflight for C27/P1C.

This script never changes scientific capability state. It reports whether the
externally supplied source contract exists and is minimally complete enough to
permit the C27 implementation work package to begin.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "data/incoming/c27_art25"
OUTPUT = ROOT / "docs/next_level/c27_preflight_report.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    files = sorted(p for p in INCOMING.rglob("*") if p.is_file()) if INCOMING.is_dir() else []
    names = {p.name for p in files}
    info = next((p for p in files if p.name == "MSHT20_REP.info"), None)
    dat = [p for p in files if p.name.startswith("MSHT20_REP_") and p.suffix == ".dat"]
    archives = [p for p in files if "MSHT20_REP" in p.name and p.suffix.lower() in {".gz", ".xz", ".zip", ".tar"}]
    generator_markers = {
        "generator source": any("generator" in p.name.lower() or p.suffix in {".py", ".f90", ".cpp"} for p in files),
        "transformation matrix": any("matrix" in p.name.lower() for p in files),
        "seed declaration": any("seed" in p.name.lower() for p in files),
        "generation metadata": any(p.name in {"generation.json", "generator_manifest.json"} for p in files),
        "license or permission": any("license" in p.name.lower() or "permission" in p.name.lower() for p in files),
        "official checksum": any("checksum" in p.name.lower() or p.name.endswith(".sha256") for p in files),
    }
    exact_directory = info is not None and len(dat) >= 1000
    archive_form = bool(archives) and generator_markers["license or permission"] and generator_markers["official checksum"]
    generator_form = all(generator_markers.values())
    msht_admissible = exact_directory or archive_form or generator_form
    frozen = [p for p in files if "frozen" in p.name.lower() or "benchmark" in p.name.lower()]
    status = "C27_PREFLIGHT_PASS" if msht_admissible else "C27_BLOCKED_MISSING_EXACT_MSHT20_REP"
    report = {
        "schema_version": "1.0.0",
        "baseline_commit": "8c2ed28abadf73663e2c816ac49b13541fae6a3b",
        "incoming_directory": str(INCOMING.relative_to(ROOT)),
        "incoming_directory_exists": INCOMING.is_dir(),
        "incoming_file_count": len(files),
        "incoming_files": [
            {"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size, "sha256": sha(p)} for p in files
        ],
        "exact_directory_form": exact_directory,
        "exact_directory_member_files": len(dat),
        "archive_candidates": [str(p.relative_to(ROOT)) for p in archives],
        "archive_form_minimum_metadata_present": archive_form,
        "generator_gates": generator_markers,
        "generator_form_complete": generator_form,
        "msht20_rep_source_form": "NONE" if not msht_admissible else "EXACT_DIRECTORY" if exact_directory else "ARCHIVE" if archive_form else "GENERATOR",
        "source_identity_present": msht_admissible,
        "checksum_present": generator_markers["official checksum"],
        "license_or_permission_present": generator_markers["license or permission"],
        "member_count": len(dat) if dat else None,
        "member_numbering_validated": exact_directory and {f"MSHT20_REP_{i:04d}.dat" for i in range(1000)} <= names,
        "art25_index_coverage": exact_directory and len(dat) >= 1000,
        "frozen_output_bundle_status": "PRESENT_UNVALIDATED" if frozen else "AUTHOR_FROZEN_OUTPUT_UNAVAILABLE",
        "commands_configuration_status": "PRESENT_UNVALIDATED" if any("command" in p.name.lower() or "config" in p.name.lower() for p in files) else "UNAVAILABLE",
        "source_contact_authorization_status": "PRESENT_UNVALIDATED" if generator_markers["license or permission"] else "UNAVAILABLE",
        "status": status,
        "c27_execution_authorized_by_preflight": msht_admissible,
        "scientific_capability_matrices_modified": False,
        "process_outputs_created": False,
        "next_action": "Stage the exact author/source payload under data/incoming/c27_art25 and rerun scripts/preflight_c27.py.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(status)
    return 0 if msht_admissible else 2


if __name__ == "__main__":
    raise SystemExit(main())
