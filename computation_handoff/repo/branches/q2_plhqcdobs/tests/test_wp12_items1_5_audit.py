import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_items_one_through_five_acceptance_passes():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_items1_5_acceptance.json").read_text()
    )
    assert report["status"] == "pass"
    assert all(report["criteria"].values())
    assert report["item6"] == "ready_after_scientific_inspection"
    assert report["numerical_evidence"][
        "quark_minimum_density_eigenvalue"
    ] >= -1e-10
    assert report["numerical_evidence"][
        "gluon_minimum_density_eigenvalue"
    ] >= -1e-10
