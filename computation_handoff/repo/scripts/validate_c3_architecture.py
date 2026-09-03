#!/usr/bin/env python3
"""Validate the deterministic C3 documentation and isolation package."""

from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/"docs/next_level"
def load(name): return json.loads((DOCS/name).read_text())

def main():
    baseline=load("c3_baseline_snapshot.json"); coverage=load("c3_requirement_coverage.json")
    benchmarks=load("c3_benchmark_manifest.json"); injections=load("c3_injection_manifest.json")
    provenance=load("c3_pilot_provenance.json"); regression=load("c3_regression_report.json")
    expected={"C3.BASELINE","C3.ISOLATE","C3.FIBER","C3.CONFIG","C3.RECOIL","C3.STATE","C3.KERNEL","C3.OVERLAP","C3.BENCH_A","C3.BENCH_B","C3.BENCH_C","C3.BENCH_D","C3.HERMITICITY","C3.NUMBER","C3.COLOR","C3.REDUCTION_BRIDGE","C3.PROVENANCE","C3.INJECT","C3.CONVERGENCE","C3.REGRESS","C3.DOC"}
    ids=[x["id"] for x in coverage["requirements"]]
    if set(ids)!=expected or len(ids)!=len(set(ids)): raise ValueError("C3 coverage mismatch")
    if baseline["accepted_registry"]["count"]!=216: raise ValueError("C2 registry baseline mismatch")
    if len(benchmarks["benchmarks"])!=4 or not benchmarks["all_passed"]: raise ValueError("benchmark failure")
    if injections["count"]!=24 or not all(x["status"]=="pass" for x in injections["injections"]): raise ValueError("injection manifest failure")
    if provenance["reachable_from_accepted"] or provenance["status"]!="VALIDATION_ONLY": raise ValueError("pilot isolation failure")
    if not regression["all_byte_identical"] or not regression["accepted_registry"]["unchanged"] or not regression["accepted_provenance_unchanged"] or not regression["accepted_composition_unchanged"]: raise ValueError("immutable regression failure")
    for name in ("c3_implementation_report.md","c3_api.md","c3_unresolved_formalism_gaps.md"):
        if not (DOCS/name).is_file(): raise ValueError(f"missing {name}")
    print(json.dumps({"status":"pass","requirements":len(ids),"benchmarks":4,"injections":24,"pilot_nodes":len(provenance["nodes"]),"authoritative_hashes":8},indent=2))

if __name__=="__main__": main()
