import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "outputs/validation/wp12_evidence_parity_matrix.json"


def test_wp12_evidence_matrix_is_complete_and_passes_all_rows():
    report = json.loads(REPORT.read_text())
    rows = report["rows"]
    assert len(rows) == 36
    assert len({(row["species"], row["tmd"]) for row in rows}) == 36
    assert report["summary"]["total"] == 36
    assert report["summary"]["pass"] == 36
    assert report["summary"]["open"] == 0
    assert report["status"] == "pass"
    for row in rows:
        assert row["checks"]["flavor_or_color_resolved"]
        assert row["checks"]["explicit_proton_neutron_ledger"]
        assert row["checks"]["all_artifacts_present"]
        assert row["status"] == ("pass" if not row["missing_requirements"] else "open")
