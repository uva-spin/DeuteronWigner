#!/usr/bin/env python3
"""Fail-closed consistency checks for generated C7/H0 records."""

import json
from pathlib import Path

DOC=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(name): return json.loads((DOC/name).read_text())


def main():
    coverage=load("c7_requirement_coverage.json")
    sources=load("c7_normative_source_integration.json")
    basis=load("c7_basis_manifest.json")
    color=load("c7_color_permutation_manifest.json")
    free=load("c7_free_spectrum_manifest.json")
    vertex=load("c7_vertex_manifest.json")
    tolerance=load("c7_tolerance_manifest.json")
    readiness=load("c7_readiness_manifest.json")
    injections=load("c7_injection_manifest.json")
    regression=load("c7_regression_report.json")
    assert coverage["count"]==74
    assert sources["volumes_0_vii_indexed"] and sources["all_pinned_sources_match"]
    assert basis["dimensions_by_sector"]=={"qqq":1,"qqqg":2,"qqqq-qbar":3}
    assert {key:value["singlet_multiplicity"] for key,value in color["sectors"].items()}=={"qqq":1,"qqqg":2,"qqqq-qbar":3}
    assert len(free["rows"])==9 and all(row["matrix_shape"]==[row["dimension"],row["dimension"]] for row in free["rows"])
    assert len(vertex["rows"])==12 and vertex["maximum_hermiticity_residual"]<2e-11
    assert tolerance["all_pass"]
    assert readiness["provenance"]["production_reachable"] is False
    assert injections["count"]==48 and injections["all_detected"]
    assert regression["all_artifacts_byte_identical"] and regression["all_c6_manifests_unchanged"]
    assert regression["accepted_registry_count"]==216
    print(json.dumps({"status":"pass","requirements":coverage["count"],"singlet_multiplicities":[1,2,3],"free_blocks":len(free["rows"]),"vertex_blocks":len(vertex["rows"]),"injections":48,"authoritative_hashes":8},indent=2))


if __name__=="__main__": main()
