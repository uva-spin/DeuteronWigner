#!/usr/bin/env python3
"""Fail-closed consistency validation for generated C5 records."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "next_level"


def load(name: str):
    return json.loads((DOC / name).read_text())


def main() -> None:
    coverage = load("c5_requirement_coverage.json")
    benchmark = load("c5_benchmark_manifest.json")
    injections = load("c5_injection_manifest.json")
    cuts = load("c5_cut_ledger_manifest.json")
    phase = load("c5_phase_budget.json")
    provenance = load("c5_provenance_graph.json")
    regression = load("c5_regression_report.json")
    sources = load("c5_normative_source_integration.json")
    assert coverage["count"] == 25 and len(coverage["requirements"]) == 25
    assert set(benchmark["benchmarks"]) == {"C5-A", "C5-B", "C5-C", "C5-D", "C5-E"}
    assert injections["count"] == 48 and injections["all_detected"]
    assert cuts["active_weight"] == cuts["entries"][0]["cut"]["spectral_weight"]
    assert "UNRESOLVED" in phase["phase_budget"]["soft_overlap_contribution"]
    assert provenance["general_provenance_2_complex_complete"] is False
    assert regression["all_byte_identical"]
    assert regression["accepted_registry_count"] == 216
    assert regression["c4_architecture"] == {
        "requirements": 25, "injections": 40,
        "provenance_nodes": 16, "authoritative_hashes": 8,
    }
    assert sources["all_byte_identical_to_c4"]
    assert len(sources["sources"]) == 6
    assert sources["volume_iv_gate"]["ready"] is False
    assert sources["volume_v_gate"]["ready"] is False
    print(json.dumps({
        "status": "pass", "requirements": coverage["count"],
        "benchmarks": len(benchmark["benchmarks"]),
        "injections": injections["count"],
        "authoritative_hashes": len(regression["artifacts"]),
        "normative_sources": len(sources["sources"]),
    }, indent=2))


if __name__ == "__main__":
    main()
