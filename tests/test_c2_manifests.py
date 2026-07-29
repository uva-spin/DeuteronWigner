"""C2 manifest, traceability, and immutable artifact acceptance."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def load(name):
    return json.loads((DOCS / name).read_text())


def test_c2_registry_covers_every_named_sector_projection():
    value = load("c2_reduction_registry.json")
    assert value["count"] == 216
    names = {
        (
            item["source_operator"]["parton_species"],
            item["source_operator"]["name"],
        )
        for item in value["entries"]
    }
    assert len({name for species, name in names if species == "q"}) == 18
    assert len({name for species, name in names if species == "qbar"}) == 18
    assert len({name for species, name in names if species == "g"}) == 18
    assert all(item["availability"] == "AVAILABLE_FORWARD" for item in value["entries"])


def test_c2_graph_traces_all_36_evidence_rows_and_named_outputs():
    graph = load("c2_provenance_graph.json")
    node_ids = {item["stable_id"] for item in graph["nodes"]}
    evidence = {item for item in node_ids if item.startswith("evidence:")}
    projections = {item for item in node_ids if item.startswith("projection:")}
    operators = {item for item in node_ids if item.startswith("operator:")}
    assert len(evidence) == len(projections) == len(operators) == 36
    edges = {(item["source"], item["target"], item["relation"]) for item in graph["edges"]}
    for projection in projections:
        suffix = projection.removeprefix("projection:")
        assert (projection, f"operator:{suffix}", "DERIVES_FROM") in edges
        assert (projection, f"evidence:{suffix}", "VALIDATES") in edges


def test_c2_all_authoritative_hashes_are_unchanged():
    report = load("c2_regression_report.json")
    assert report["all_byte_identical"]
    for item in report["artifacts"]:
        actual = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
        assert actual == item["expected_sha256"] == item["after_sha256"]
