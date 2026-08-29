import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_scientific_inspection_is_ready_for_item_six():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_scientific_inspection.json").read_text()
    )
    assert report["status"] == "ready_for_item_6"
    assert all(report["gates"].values())
    assert report["metrics"]["quark_nonzero_tmd_count"] == 18
    assert report["metrics"]["gluon_nonzero_tmd_count"] == 18
    assert report["remaining_model_dependence_for_item_6"]
