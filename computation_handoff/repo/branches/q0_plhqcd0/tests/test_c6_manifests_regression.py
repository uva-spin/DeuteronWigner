import json
from pathlib import Path

DOC=Path(__file__).resolve().parents[1]/"docs"/"next_level"


def load(name):
    return json.loads((DOC/name).read_text())


def test_c6_manifest_counts_and_benchmarks():
    assert load("c6_requirement_coverage.json")["count"]==42
    assert load("c6_ordered_link_manifest.json")["count"]==4
    assert load("c6_active_gluon_channel_registry.json")["count"]==24
    assert len(load("c6_benchmark_manifest.json")["benchmarks"])==7
    assert load("c6_injection_manifest.json")["count"]==60


def test_c6_color_soft_and_phase_manifests():
    color=load("c6_color_projection_manifest.json")
    soft=load("c6_soft_overlap_manifest.json")
    assert color["fd_reconstruction_residual"]<3e-15
    assert color["orthogonal_injection_residual"]>0
    assert soft["maximum_rapidity_derivative_residual"]==0
    assert load("c6_phase_budget_manifest.json")["count"]==6


def test_c6_regression_and_c5_immutability():
    regression=load("c6_regression_report.json")
    assert regression["all_artifacts_byte_identical"]
    assert regression["all_c5_manifests_unchanged"]
    assert regression["accepted_registry_count"]==216
    assert regression["injections"]=={"C3":24,"C4":40,"C5":48,"C6":60}


def test_c6_sources_and_gates():
    sources=load("c6_normative_source_integration.json")
    assert sources["all_byte_identical_to_c5"]
    assert not sources["volume_vi"]["present"]
    assert set(sources["downstream_gates"].values())=={"CLOSED"}
