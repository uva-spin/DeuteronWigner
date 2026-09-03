import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "next_level"


def load(name):
    return json.loads((DOC / name).read_text())


def test_c5_manifest_contract():
    assert load("c5_requirement_coverage.json")["count"] == 25
    assert load("c5_injection_manifest.json")["count"] == 48
    assert len(load("c5_benchmark_manifest.json")["benchmarks"]) == 5


def test_c5_regression_oracle_and_downstream_gates():
    regression = load("c5_regression_report.json")
    sources = load("c5_normative_source_integration.json")
    assert regression["all_byte_identical"]
    assert regression["accepted_registry_count"] == 216
    assert regression["c4_architecture"]["requirements"] == 25
    assert sources["all_byte_identical_to_c4"]
    assert not sources["volume_iv_gate"]["ready"]
    assert not sources["volume_v_gate"]["ready"]


def test_c5_phase_and_provenance_remain_validation_only():
    phase = load("c5_phase_budget.json")
    graph = load("c5_provenance_graph.json")
    assert "VALIDATION_ONLY" in phase["statuses"]
    assert phase["phase_budget"]["uv_matching_contribution"] == "UNRESOLVED_NOT_ZERO"
    assert graph["general_provenance_2_complex_complete"] is False
