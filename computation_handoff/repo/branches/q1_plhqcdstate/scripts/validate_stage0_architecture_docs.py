#!/usr/bin/env python3
"""Validate C0 machine-readable deliverables and cross-document identifiers."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"


def load(name: str) -> dict:
    with (DOCS / name).open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise TypeError(f"{name} must contain a JSON object")
    return value


def unique_ids(records: list[dict], section: str) -> set[str]:
    ids = [record.get("id") for record in records]
    if any(not isinstance(item, str) or not item for item in ids):
        raise ValueError(f"{section} contains a missing/invalid id")
    if len(ids) != len(set(ids)):
        raise ValueError(f"{section} contains duplicate ids")
    return set(ids)


def main() -> None:
    baseline = load("stage0_regression_baseline.json")
    matrix = load("stage0_coverage_matrix.json")
    if not baseline.get("immutable_physics_oracle"):
        raise ValueError("baseline must declare immutable_physics_oracle")
    requirement_ids = unique_ids(matrix["requirements"], "requirements")
    unique_ids(matrix["coordinate_uses"], "coordinate_uses")
    unique_ids(matrix["operator_identity_assessments"], "operator assessments")
    object_ids = unique_ids(matrix["core_objects"], "core_objects")
    artifact_ids = unique_ids(
        baseline["authoritative_artifacts"], "authoritative_artifacts"
    )
    command_ids = unique_ids(baseline["commands"], "commands")
    expected_objects = {
        "SectorSpace", "Intertwiner", "LFMassOperator", "FockState",
        "PathGroupoid", "WilsonTransport", "GTMDOperator", "ReductionMap",
        "MatchingMap", "NuclearAmplitudeMap", "PositiveCorrelator",
        "TruncationTower", "ProvenanceComplex", "EnsembleStore",
        "ObservableLikelihood",
    }
    actual_objects = {record["name"] for record in matrix["core_objects"]}
    if actual_objects != expected_objects:
        raise ValueError("requested core-object set is incomplete")
    for prefix in ("C0-A-", "C0-B-", "C0-C-", "C0-D-", "STA-"):
        if not any(item.startswith(prefix) for item in requirement_ids):
            raise ValueError(f"requirement category {prefix} is absent")
    if len(matrix["coordinate_uses"]) < 9:
        raise ValueError("transverse-coordinate catalog is incomplete")
    if len(matrix["operator_identity_assessments"]) < 10:
        raise ValueError("operator-identity catalog is incomplete")
    if len(object_ids) != 15:
        raise ValueError("all 15 requested core objects are required")
    if len(artifact_ids) != 12 or len(command_ids) != 2:
        raise ValueError("baseline artifact/command inventory is incomplete")
    if not all(record["status"] == "pass" for record in baseline["commands"]):
        raise ValueError("a baseline command did not pass")
    required_docs = [
        DOCS / "stage0_repository_audit.md",
        DOCS / "stageA_migration_plan.md",
        *sorted((DOCS / "architecture_decisions").glob("*.md")),
    ]
    if len(required_docs) != 7:
        raise ValueError("five ADRs and two principal documents are required")
    for path in required_docs:
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"missing or empty documentation: {path}")
    print(json.dumps({
        "status": "pass",
        "requirements": len(requirement_ids),
        "coordinates": len(matrix["coordinate_uses"]),
        "operator_assessments": len(matrix["operator_identity_assessments"]),
        "core_objects": len(object_ids),
        "artifacts": len(artifact_ids),
    }, indent=2))


if __name__ == "__main__":
    main()
