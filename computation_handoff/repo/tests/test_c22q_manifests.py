import hashlib, json
from pathlib import Path

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"


def load(name):
    return json.loads((D / name).read_text())


def test_c22q_deliverables_and_counts():
    names = ("c22q_normative_source_integration.json", "c22q_capability_reconciliation.json", "c22q_qualification_contract.json", "c22q_process_eligibility_matrix.json", "c22q_prerequisite_audit_coverage.json", "c22q_minimal_process_family_audit.json", "c22q_cs_largeb_tier_manifest.json", "c22q_nuclear_operator_qualification.json", "c23_p0_prerequisite_contract.json", "c22q_injection_manifest.json", "c22q_requirement_coverage.json", "c22q_regression_report.json")
    assert all(load(name)["schema_version"] == "1.0.0" for name in names)
    assert load("c22q_injection_manifest.json")["count"] == 160
    assert load("c22q_requirement_coverage.json")["count"] == 336
    assert len(load("c22q_capability_reconciliation.json")["rows"]) == 540


def test_original_prompt_integrity_and_no_execution():
    contract = load("c23_p0_prerequisite_contract.json")
    digest = hashlib.sha256((D / "c23_p0_codex_prompt.md").read_bytes()).hexdigest()
    assert digest == "5346947dd612813386a07ed1827a8ffd9540f03614862e135191eb0a105d4347"
    assert digest == contract["original_prompt_sha256"]
    assert not contract["process_executed"]
    assert (D / "c23_p0_codex_prompt_v2.md").exists()
