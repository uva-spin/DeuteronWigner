import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_wp12e_acceptance_passes_every_declared_gate():
    report = json.loads((
        ROOT / "outputs/validation/wp12e_acceptance.json"
    ).read_text())
    assert report["status"] == "pass"
    assert all(report["criteria"].values())
    assert report["evidence_rows"] == {"total": 36, "pass": 36, "open": 0}
