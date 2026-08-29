#!/usr/bin/env python3
"""Validate deterministic C2 manifests and cross-artifact completeness."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def load(name):
    return json.loads((DOCS / name).read_text())


def main() -> None:
    coverage = load("c2_requirement_coverage.json")
    registry = load("c2_reduction_registry.json")
    graph = load("c2_provenance_graph.json")
    composition = load("c2_composition_manifest.json")
    regression = load("c2_regression_report.json")
    baseline = load("c2_baseline_snapshot.json")
    expected = {"C2.BASELINE","C2.REDTYPE","C2.REDREG","C2.NATIVE","C2.TRANSFORM","C2.PROVTYPE","C2.PROVGRAPH","C2.EXCLUSION","C2.COMPOSE","C2.TRACE","C2.INJECT","C2.REGRESS","C2.DOC"}
    ids = [item["id"] for item in coverage["requirements"]]
    if set(ids) != expected or len(ids) != len(set(ids)):
        raise ValueError("C2 requirement coverage is incomplete or duplicated")
    reduction_ids = [item["stable_id"] for item in registry["entries"]]
    if registry["count"] != 216 or len(reduction_ids) != len(set(reduction_ids)):
        raise ValueError("native reduction registry count/identity failure")
    if registry["coverage"] != {"quark":72,"antiquark":72,"gluon":72,"named_functions_each_sector":18}:
        raise ValueError("native reduction sector coverage failure")
    node_ids = [item["stable_id"] for item in graph["nodes"]]
    if len(node_ids) != len(set(node_ids)):
        raise ValueError("duplicate provenance node")
    evidence = [item for item in graph["nodes"] if item["kind"] == "EVIDENCE"]
    if len(evidence) != 36:
        raise ValueError("provenance graph does not cover all evidence rows")
    if not composition["default_plan"]["ordered_selection"]:
        raise ValueError("default composition plan is empty")
    if not regression["all_byte_identical"] or len(regression["artifacts"]) != 8:
        raise ValueError("authoritative regression failed")
    if baseline["tests"]["passed"] != 498:
        raise ValueError("C1 baseline snapshot mismatch")
    for name in ("c2_implementation_report.md","c2_api.md","c2_unresolved_formalism_gaps.md"):
        if not (DOCS / name).is_file():
            raise ValueError(f"missing {name}")
    print(json.dumps({"status":"pass","requirements":len(ids),"reductions":len(reduction_ids),"provenance_nodes":len(node_ids),"evidence_nodes":len(evidence),"authoritative_hashes":8}, indent=2))


if __name__ == "__main__":
    main()
