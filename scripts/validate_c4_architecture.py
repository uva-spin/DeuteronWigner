#!/usr/bin/env python3
"""Validate C4 deterministic manifests and immutable boundaries."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "next_level"


def load(name):
    return json.loads((DOC / name).read_text())


def main():
    coverage = load("c4_requirement_coverage.json")
    sectors = load("c4_sector_manifest.json")
    colors = load("c4_color_manifest.json")
    routes = load("c4_route_closure_manifest.json")
    feshbach = load("c4_feshbach_manifest.json")
    provenance = load("c4_provenance_manifest.json")
    injections = load("c4_injection_manifest.json")
    regression = load("c4_regression_report.json")
    normative = load("c4_normative_source_integration.json")
    assert len(coverage["requirements"]) == 25
    assert all(x["status"] == "PASS" for x in coverage["requirements"])
    assert sectors["sea"]["members"][0]["antiquark_integrated_density"] == 0
    assert sectors["gluon"]["members"][0]["gluon_momentum_Hg_integral"] == 0
    assert colors["sea"]["generator_residual"] <= 1e-15
    assert colors["gluon"]["generator_residual"] <= 1e-15
    assert all(
        max(row["residuals"].values()) <= routes["combined_tolerance"]
        for parent in routes["parents"]
        for row in parent["transfer_closure"]
    )
    assert feshbach["energy_residual"] <= 1e-15
    assert feshbach["operator_residual"] <= 1e-15
    assert feshbach["pop_failure"] > 0.1
    assert provenance["production_reachable"] is False
    assert injections["count"] == 40 and injections["all_detected"]
    assert regression["all_byte_identical"]
    assert regression["accepted_registry"]["count"] == 216
    assert regression["accepted_provenance_unchanged"]
    assert regression["accepted_composition_unchanged"]
    assert all(regression["c3_manifests_unchanged"].values())
    assert len(normative["sources"]) == 4
    assert all(item["status"] == "PRESENT_READ" for item in normative["sources"])
    assert len(normative["corrections_after_source_import"]) == 5
    print(json.dumps({
        "status": "pass", "requirements": 25,
        "sea_members": len(sectors["sea"]["members"]),
        "gluon_members": len(sectors["gluon"]["members"]),
        "route_parents": len(routes["parents"]),
        "injections": injections["count"],
        "provenance_nodes": len(provenance["graph"]["nodes"]),
        "authoritative_hashes": len(regression["artifacts"]),
    }, indent=2))


if __name__ == "__main__":
    main()
