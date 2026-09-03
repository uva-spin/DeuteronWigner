import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_final_manifest_has_complete_unique_evidence_maps():
    manifest = json.loads(
        (ROOT / "validation/final_acceptance_manifest.json").read_text()
    )
    ids = [item["id"] for item in manifest["criteria"]]
    assert len(ids) == len(set(ids))
    assert len(ids) >= 11
    for item in manifest["criteria"]:
        assert all(item[key] for key in (
            "criterion", "implementation_files", "tests",
            "artifacts", "documentation",
        ))
