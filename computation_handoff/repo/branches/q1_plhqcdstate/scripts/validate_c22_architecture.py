#!/usr/bin/env python3
import json
from pathlib import Path

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"
required = (
    "normative_source_integration", "primary_source_manifest", "distribution_algebra_manifest",
    "coefficient_library", "coefficient_source_audit", "gamma5_scheme_manifest",
    "splitting_function_library", "collinear_evolution_manifest", "ope_rg_consistency_report",
    "smallb_capability_matrix", "m3_multiq_capability_matrix", "nuclear_ope_manifest",
    "accuracy_manifest", "uncertainty_manifest", "holdout_report", "injection_manifest",
    "requirement_coverage", "regression_report",
)
docs = {name: json.loads((D / f"c22_{name}.json").read_text()) for name in required}
assert all(value["schema_version"] == "1.0.0" for value in docs.values())
assert len(docs["m3_multiq_capability_matrix"]["rows"]) == 540
assert docs["m3_multiq_capability_matrix"]["c20_matching_executable"] == 492
assert docs["m3_multiq_capability_matrix"]["c21_fully_evolvable"] == 438
assert docs["injection_manifest"]["count"] >= 720 and docs["injection_manifest"]["all_detected"]
assert not docs["regression_report"]["production_reachable"]
assert not docs["regression_report"]["process_reachable"]
assert docs["regression_report"]["production_registry"] == 216
print("C22/M3 architecture manifests validated")
