import json


def test_physical_lf_offforward_reduction_artifact_passes_all_waves():
    with open("outputs/validation/physical_offforward_reductions.json") as stream:
        report = json.load(stream)
    assert report["status"] == "pass"
    assert len(report["rows"]) == 6
    assert all(row["nuclear_lf_wave_is_physical"] for row in report["rows"])
    assert all(
        row["nucleon_gtmd_model"] == "factorized_gaussian_rank_zero"
        for row in report["rows"]
    )
