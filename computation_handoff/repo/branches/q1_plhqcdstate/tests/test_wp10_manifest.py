import json
from pathlib import Path


def test_wp10_manifest_has_complete_existing_evidence():
    manifest = json.loads(Path("validation/wp10_manifest.json").read_text())
    assert manifest["completion_ready"] is True
    assert {item["id"] for item in manifest["criteria"]} == {
        "quark_gauge_link_todd",
        "worm_gears_pretzelosity",
        "gluon_color_todd",
        "polarized_tensor_shadowing",
        "mesonic_nonnucleonic",
        "oam_interference",
        "production_acceptance",
    }
    for criterion in manifest["criteria"]:
        assert criterion["status"] == "complete"
        assert criterion["remaining"] == ""
        for field in (
            "implementation_files", "tests", "artifacts", "documentation"
        ):
            for filename in criterion[field]:
                assert Path(filename).exists(), f"missing WP10 evidence: {filename}"
    assert manifest["declared_limitations"]
