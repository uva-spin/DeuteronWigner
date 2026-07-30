"""C4 manifest determinism, coverage, and immutable-boundary checks."""

import hashlib
import json
from pathlib import Path


DOC = Path("docs/next_level")


def load(name):
    return json.loads((DOC / name).read_text())


def test_c4_coverage_and_injection_manifests_are_complete():
    coverage = load("c4_requirement_coverage.json")
    assert len(coverage["requirements"]) == 25
    assert all(item["status"] == "PASS" for item in coverage["requirements"])
    injections = load("c4_injection_manifest.json")
    assert injections["count"] == 40
    assert injections["all_detected"]


def test_c4_regression_preserves_authoritative_artifacts_and_c3():
    report = load("c4_regression_report.json")
    baseline = load("c4_baseline_snapshot.json")
    assert report["all_byte_identical"]
    assert report["accepted_registry"]["count"] == 216
    assert report["accepted_provenance_unchanged"]
    assert report["accepted_composition_unchanged"]
    assert all(report["c3_manifests_unchanged"].values())
    for name, expected in baseline["c3"]["manifest_hashes"].items():
        assert hashlib.sha256((DOC / name).read_bytes()).hexdigest() == expected
    assert (
        hashlib.sha256((DOC / "c2_reduction_registry.json").read_bytes()).hexdigest()
        == baseline["accepted_registry"]["sha256"]
    )
    assert (
        hashlib.sha256((DOC / "c2_provenance_graph.json").read_bytes()).hexdigest()
        == baseline["accepted_provenance_sha256"]
    )
    assert (
        hashlib.sha256((DOC / "c2_composition_manifest.json").read_bytes()).hexdigest()
        == baseline["accepted_composition_sha256"]
    )
    for artifact in report["artifacts"]:
        actual = hashlib.sha256(Path(artifact["path"]).read_bytes()).hexdigest()
        assert actual == artifact["expected_sha256"]


def test_c4_provenance_and_route_manifests_are_isolated_and_honest():
    provenance = load("c4_provenance_manifest.json")
    assert provenance["production_reachable"] is False
    assert all(
        node["selection_role"] == "BENCHMARK_ONLY"
        for node in provenance["graph"]["nodes"]
    )
    routes = load("c4_route_closure_manifest.json")
    assert "not full QCD" in routes["interpretation"]
    assert all(
        parent["matching_status"] == "REGULATED_ANALYTIC"
        for parent in routes["parents"]
    )
    assert all(
        "LINK_SHORTENING_REQUIRED"
        in parent["required_matching"]["gpd_pdf_current"]
        for parent in routes["parents"]
    )


def test_normative_source_integration_is_hashed_and_scoped():
    report = load("c4_normative_source_integration.json")
    assert [item["volume"] for item in report["sources"]] == ["0", "I", "II", "III", "IV"]
    for source in report["sources"]:
        assert hashlib.sha256(Path(source["path"]).read_bytes()).hexdigest() == source["sha256"]
    assert "does not claim complete Volume II acceptance" in report["scope_boundary"]
    interface = report["volume_iv_interface_assessment"]
    assert interface["ready_for_volume_iv_nuclear_consumption"] is False
    assert interface["nuclear_dynamics_implemented_in_c4"] is False
