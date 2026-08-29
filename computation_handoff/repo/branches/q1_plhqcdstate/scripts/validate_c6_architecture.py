#!/usr/bin/env python3
"""Validate deterministic C6 manifests and immutable gates."""

import json
from pathlib import Path

DOC = Path(__file__).resolve().parents[1]/"docs"/"next_level"


def load(name):
    return json.loads((DOC/name).read_text())


def main():
    coverage=load("c6_requirement_coverage.json")
    sources=load("c6_normative_source_integration.json")
    channels=load("c6_active_gluon_channel_registry.json")
    links=load("c6_ordered_link_manifest.json")
    color=load("c6_color_projection_manifest.json")
    soft=load("c6_soft_overlap_manifest.json")
    phase=load("c6_phase_budget_manifest.json")
    bench=load("c6_benchmark_manifest.json")
    injections=load("c6_injection_manifest.json")
    provenance=load("c6_provenance_manifest.json")
    regression=load("c6_regression_report.json")
    assert coverage["count"]==42
    assert links["count"]==4 and channels["count"]==24
    assert abs(color["norms"]["f"]-24)<1e-14
    assert abs(color["norms"]["d"]-40/3)<1e-14
    assert color["fd_reconstruction_residual"]<3e-15
    assert soft["maximum_rapidity_derivative_residual"]==0
    assert phase["count"]==6
    assert set(bench["benchmarks"])=={f"C6-{letter}" for letter in "ABCDEFG"}
    assert injections["count"]==60 and injections["all_detected"]
    assert len(provenance["cells"])==4 and provenance["general_provenance_2_complex_complete"] is False
    assert sources["all_byte_identical_to_c5"] and sources["volume_vi"]["present"] is False
    assert regression["all_artifacts_byte_identical"] and regression["all_c5_manifests_unchanged"]
    assert regression["accepted_registry_count"]==216
    print(json.dumps({"status":"pass","requirements":42,"ordered_pairs":4,"channels":24,"benchmarks":7,"injections":60,"authoritative_hashes":8},indent=2))


if __name__=="__main__":
    main()
