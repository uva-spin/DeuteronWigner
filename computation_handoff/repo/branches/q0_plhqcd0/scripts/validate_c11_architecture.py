#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
load=lambda n:json.loads((D/n).read_text())
assert load("c11_normative_source_integration.json")["all_match"]
assert load("c11_injection_manifest.json")["count"]>=100
assert load("c11_quark_antiquark_projector_manifest.json")["generic_rank"]==16
assert load("c11_gluon_projector_manifest.json")["generic_rank"]==16
assert load("c11_helicity_matrix_closure_report.json")["complete"]
r=load("c11_regression_report.json")
assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
assert load("c11_microscopic_replacement_manifest.json")["scope"]["root"]=="C11_H4_VALIDATION_ONLY"
print("C11/H4 architecture manifests validated")
