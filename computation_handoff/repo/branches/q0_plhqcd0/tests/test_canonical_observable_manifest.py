import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_canonical_observable_manifest_evidence_exists():
    data = json.loads(
        (ROOT / "validation/canonical_observable_manifest.json").read_text()
    )
    assert len(data["observables"]) >= 5
    assert all(item["status"] == "pass" for item in data["observables"])
    for item in data["observables"]:
        for key in ("artifact",):
            if key in item:
                assert (ROOT / item[key]).is_file()
        for test in item.get("tests", []):
            assert (ROOT / test).is_file()


def test_gluon_process_rule_does_not_invent_a_universal_color_sum():
    data = json.loads(
        (ROOT / "validation/canonical_observable_manifest.json").read_text()
    )
    gluon = next(
        x for x in data["observables"]
        if x["id"] == "gluon_link_color_channels"
    )
    assert "independent" in gluon["hard_color_rule"]
    assert "specified factorization theorem" in gluon["hard_color_rule"]
