import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_wp8_manifest_has_unique_complete_requirement_records():
    manifest = json.loads((ROOT / "validation/wp8_manifest.json").read_text())
    requirements = manifest["requirements"]
    ids = [item["id"] for item in requirements]
    assert len(ids) == len(set(ids))
    assert len(requirements) >= 12
    required = {
        "requirement", "declared_status", "tolerance", "test_prefixes",
        "artifacts", "provenance", "affected_outputs",
    }
    for item in requirements:
        assert required <= set(item)
        assert item["declared_status"] in {"implemented", "partial", "open"}
        assert item["tolerance"]
        if item["declared_status"] != "implemented":
            assert item.get("open_reason")

