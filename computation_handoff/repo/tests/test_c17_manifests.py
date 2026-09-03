import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
def test_c17_manifests_readable():
 names=("normative_source_integration","requirement_coverage","injection_manifest","regression_report","continuum_calibration_manifest","finite_volume_spectral_map","pole_residue_report","current_basis_certificate","continuity_closure_report","separator_trajectory","explicit_induced_pion_comparison","pion_active_closure_report","coherent_continuum_manifest","cp_reduction_report","tensor_network_manifest","convergence_manifest","provenance_complex","readiness_manifest","benchmark_manifest")
 for n in names:assert load("c17_"+n+".json")["schema_version"]=="1.0.0"
def test_c17_counts_and_regression():
 q=load("c17_requirement_coverage.json");i=load("c17_injection_manifest.json");r=load("c17_regression_report.json")
 assert q["count"]==len(q["rows"]) and i["count"]>=340 and r["production_registry"]==216 and r["all_artifacts_unchanged"]
def test_c17_closure_and_scope():
 c=load("c17_continuity_closure_report.json");s=load("c17_separator_trajectory.json");r=load("c17_readiness_manifest.json")
 assert abs(c["residual"])<1e-12 and s["matched_variation"]<s["tolerance"] and not r["production_reachable"]
def test_c17_all_benchmark_families():
 b=load("c17_benchmark_manifest.json")
 assert [x["stable_id"] for x in b["rows"]]==[f"N2-{x}" for x in "ABCDEFGHIJKLMNOPQR"]
 assert all(x["status"]=="PASS" for x in b["rows"]) and b["tensor_ablation_signal"]>0
