import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"docs"/"next_level"

def load(name): return json.loads((DOC/name).read_text())

def test_c8_manifest_schema_and_counts():
    assert load("c8_requirement_coverage.json")["count"]==104
    assert load("c8_injection_manifest.json")["count"]==56
    assert load("c8_basis_tower_manifest.json")["dimensions"]==[4,7,10]

def test_c8_tolerances_and_plans():
    assert load("c8_tolerance_manifest.json")["all_pass"]
    plans=load("c8_assumption_plan_manifest.json")
    assert plans["all_identities_distinct"] and plans["mutually_exclusive"]

def test_c8_isolation_and_immutable_outputs():
    report=load("c8_regression_report.json")
    assert report["all_authoritative_unchanged"]
    assert report["all_pinned_c5_c6_unchanged"]
    assert report["production_registry"]==216 and not report["production_reachable"]

def test_c8_state_bundles_are_scoped():
    bundles=load("c8_state_bundle_manifest.json")["bundles"]
    assert len(bundles)==3
    assert all(x["scope"]=="C8_H1_VALIDATION_ONLY" and x["sector_scope"]=="VALENCE_ONLY" for x in bundles)
