import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
def test_c19_manifests():
 for n in ("normative_source_integration","regression_report","requirement_coverage","injection_manifest","scheme_manifest","matching_basis","matching_map_manifest","step_scaling_report","small_b_ope_manifest","rank_transform_report","collinear_evolution_report","two_scale_evolution_report","threshold_report","nuclear_matching_report","accuracy_manifest","benchmark_manifest"):assert L("c19_"+n+".json")["schema_version"]=="1.0.0"
def test_c19_counts():assert L("c19_injection_manifest.json")["count"]==480 and L("c19_requirement_coverage.json")["count"]==len(L("c19_requirement_coverage.json")["rows"])
def test_c19_isolation():assert not L("c19_accuracy_manifest.json")["production_reachable"] and L("c19_regression_report.json")["production_registry"]==216
