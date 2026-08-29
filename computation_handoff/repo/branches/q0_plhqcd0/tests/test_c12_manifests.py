import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
def test_c12_manifest_coverage():
 assert L("c12_requirement_coverage.json")["count"]>=290 and L("c12_injection_manifest.json")["count"]==124
def test_c12_scientific_manifests():
 assert L("c12_spectral_support_manifest.json")["maximum_final_residual"]<6e-6
 assert L("c12_quark_antiquark_link_odd_manifest.json")["projectors_distinct"]
 assert L("c12_gluon_fd_manifest.json")["row_count"]==24
 assert L("c12_soft_overlap_report.json")["one_subtraction_residual"]==0
def test_c12_regression_isolation():
 r=L("c12_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
