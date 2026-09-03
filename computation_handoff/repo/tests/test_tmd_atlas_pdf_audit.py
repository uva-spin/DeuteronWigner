import json


def test_every_authoritative_tmd_atlas_page_rendered_and_passed():
    with open("outputs/validation/tmd_atlas_pdf_audit.json") as stream:
        report = json.load(stream)
    assert report["status"] == "pass"
    assert sum(item["pages"] for item in report["atlases"].values()) == 162
    assert all(item["passed"] for item in report["atlases"].values())
