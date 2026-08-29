#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DOC=ROOT/"docs"/"next_level"
def load(name): return json.loads((DOC/name).read_text())
def main():
    required=("c8_preimplementation_baseline.json","c8_requirement_coverage.json","c8_basis_tower_manifest.json","c8_hamiltonian_term_manifest.json","c8_renormalization_trajectory.json","c8_current_closure_report.json","c8_state_tracking_manifest.json","c8_tensor_network_manifest.json","c8_assumption_plan_manifest.json","c8_injection_manifest.json","c8_state_bundle_manifest.json","c8_tolerance_manifest.json","c8_regression_report.json")
    data={name:load(name) for name in required}
    assert all(x["schema_version"]=="1.0.0" for x in data.values())
    assert data["c8_requirement_coverage.json"]["count"]==104
    assert data["c8_basis_tower_manifest.json"]["dimensions"]==[4,7,10]
    assert data["c8_injection_manifest.json"]["count"]==56
    assert data["c8_tolerance_manifest.json"]["all_pass"]
    assert data["c8_assumption_plan_manifest.json"]["all_identities_distinct"]
    assert data["c8_regression_report.json"]["all_authoritative_unchanged"]
    assert data["c8_regression_report.json"]["all_pinned_c5_c6_unchanged"]
    assert all(x["scope"]=="C8_H1_VALIDATION_ONLY" for x in data["c8_state_bundle_manifest.json"]["bundles"])
    print(json.dumps({"status":"pass","requirements":104,"basis_dimensions":[4,7,10],"plans":3,"injections":56,"state_bundles":3},indent=2))
if __name__=="__main__": main()
