"""C3 manifest determinism, isolation, and immutable-production regression."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/"docs/next_level"
def load(name): return json.loads((DOCS/name).read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def test_all_c3_benchmarks_and_injections_are_manifested():
    benchmarks=load("c3_benchmark_manifest.json")
    injections=load("c3_injection_manifest.json")
    assert benchmarks["all_passed"] and len(benchmarks["benchmarks"])==4
    assert injections["count"]==24
    assert all(item["status"]=="pass" for item in injections["injections"])
    assert all(item["production_authorization"] is False for item in benchmarks["benchmarks"])


def test_c2_registry_graph_and_composition_are_unchanged():
    baseline=load("c3_baseline_snapshot.json"); report=load("c3_regression_report.json")
    assert sha(DOCS/"c2_reduction_registry.json")==baseline["accepted_registry"]["sha256"]
    assert sha(DOCS/"c2_provenance_graph.json")==baseline["accepted_provenance_sha256"]
    assert sha(DOCS/"c2_composition_manifest.json")==baseline["accepted_composition_sha256"]
    assert report["accepted_registry"]["unchanged"]
    assert report["accepted_provenance_unchanged"]
    assert report["accepted_composition_unchanged"]


def test_all_eight_authoritative_artifacts_and_production_import_are_unchanged():
    report=load("c3_regression_report.json")
    assert report["all_byte_identical"]
    for item in report["artifacts"]:
        assert sha(ROOT/item["path"])==item["expected_sha256"]==item["actual_sha256"]
    assert "deuteron_wigner.pilot" not in (ROOT/"scripts/build_wp12_resolved_nuclear_parent.py").read_text()
