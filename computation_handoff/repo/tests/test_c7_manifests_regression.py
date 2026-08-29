import json
from pathlib import Path

DOC=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(name): return json.loads((DOC/name).read_text())


def test_c7_basis_color_and_benchmark_manifests():
    assert load("c7_basis_manifest.json")["dimensions_by_sector"]=={"qqq":1,"qqqg":2,"qqqq-qbar":3}
    color=load("c7_color_permutation_manifest.json")
    assert [color["sectors"][x]["singlet_multiplicity"] for x in ("qqq","qqqg","qqqq-qbar")]==[1,2,3]
    assert len(load("c7_free_spectrum_manifest.json")["rows"])==9
    assert len(load("c7_vertex_manifest.json")["rows"])==12


def test_c7_tolerances_readiness_and_injections():
    assert load("c7_tolerance_manifest.json")["all_pass"]
    readiness=load("c7_readiness_manifest.json")
    assert len(readiness["readiness"]["validated"])==6
    assert len(readiness["readiness"]["unavailable"])==8
    assert load("c7_injection_manifest.json")["count"]==48


def test_c7_normative_and_regression_gates():
    assert load("c7_normative_source_integration.json")["all_pinned_sources_match"]
    regression=load("c7_regression_report.json")
    assert regression["all_artifacts_byte_identical"]
    assert regression["all_c6_manifests_unchanged"]
    assert regression["accepted_registry_count"]==216


def test_c7_requirement_coverage_is_complete():
    coverage=load("c7_requirement_coverage.json")
    assert coverage["count"]==len(coverage["requirements"])==74
