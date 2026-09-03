import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_manifest_covers_completed_items_one_through_five():
    data = json.loads((ROOT / "validation/wp12_manifest.json").read_text())
    assert [x["id"] for x in data["criteria"]] == [
        "all_tmd_multikinematic", "channel_wilson", "shared_fock_oam",
        "nonnucleonic_transverse", "operator_nuclear_maps",
    ]
    assert all(x["status"] == "complete" for x in data["criteria"])
    assert all(x["completion"] and x["implemented"] and not x["missing"]
               for x in data["criteria"])
    assert data["item6_status"] == (
        "ready_to_start_after_scientific_inspection_pass"
    )
