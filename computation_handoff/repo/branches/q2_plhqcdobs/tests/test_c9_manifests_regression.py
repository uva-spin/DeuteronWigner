import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(n):return json.loads((D/n).read_text())
def test_counts_and_color():
 assert load("c9_requirement_coverage.json")["count"]==157
 assert load("c9_injection_manifest.json")["count"]==83
 assert load("c9_hamiltonian_manifest.json")["color"]["singlet_multiplicity"]==2
def test_closure():
 assert load("c9_ward_closure_report.json")["maximum_residual"]<2e-12
 assert load("c9_tensor_network_manifest.json")["maximum_full_bond_residual"]<2e-12
 assert all(abs(x["probability_residual"])<2e-12 and abs(x["Jz_residual"])<2e-12 for x in load("c9_gluon_oam_ledger.json")["rows"])
def test_regression_and_wilson_boundary():
 r=load("c9_regression_report.json");assert r["all_artifacts_unchanged"] and r["production_registry"]==216 and not r["production_reachable"]
 w=load("c9_wilson_reconnection_manifest.json");assert w["discrete_absorption"]==0 and w["finite_epsilon_absorption"]==0 and not w["false_WILSON_READY"]
def test_compiler_and_feshbach():
 assert load("c9_compiler_manifest.json")["mutually_exclusive"]
 assert all(x["remainder_norm"]>0 for x in load("c9_feshbach_comparison.json")["rows"])
