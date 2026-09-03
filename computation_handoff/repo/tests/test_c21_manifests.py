import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
def test_c21_files():
 for n in ("normative_source_integration","anomalous_dimension_library","beta_threshold_library","cs_kernel_source_manifest","cs_kernel_fit_manifest","evolution_capability_matrix","multiq_grid","evolution_accuracy_manifest","nuclear_evolution_manifest","uncertainty_manifest","holdout_report","requirement_coverage","regression_report","injection_manifest"):assert L("c21_"+n+".json")["schema_version"]=="1.0.0"
def test_c21_counts():assert L("c21_injection_manifest.json")["count"]==640 and len(L("c21_evolution_capability_matrix.json")["rows"])==540
def test_c21_isolation():assert not L("c21_regression_report.json")["production_reachable"] and L("c21_regression_report.json")["production_registry"]==216
