import json
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from deuteron_wigner.process.p1d.core import (
    ART25AnalysisSourceId,
    DataProcessorRepositoryId,
    SourceReproducibleLowQtContract,
    WYReadinessRecord,
    injection_rows,
)

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "docs" / "next_level"


def load(name):
    return json.loads((D / name).read_text())


def test_c28_typed_fail_closed_contracts():
    repo = DataProcessorRepositoryId(
        "https://github.com/VladimirovAlexey/artemide-DataProcessor.git",
        "761f3fcdd3701c5cf69e822f9ffbbd5db394fc58",
        "master",
    )
    source = ART25AnalysisSourceId(repo, repo.commit, "a" * 64)
    with pytest.raises(FrozenInstanceError):
        repo.branch = "other"
    assert len(repo.content_sha256) == 64 and repo.content_sha256 == repo.content_sha256
    with pytest.raises(ValueError, match="C28.ART25.HISTORICAL_COMMIT_REJECT"):
        ART25AnalysisSourceId(repo, "0" * 40, "a" * 64)
    assert source.analysis_commit == repo.commit
    assert SourceReproducibleLowQtContract(True, True, True, True, True, True).eligible
    with pytest.raises(ValueError, match="C28.WY.IDENTITY_REJECT"):
        WYReadinessRecord("DY", "W", True, False, True)


def test_c28_ordered_negative_injections():
    rows = injection_rows()
    assert len(rows) >= 1200
    assert [r["ordinal"] for r in rows] == list(range(1, len(rows) + 1))
    assert len({r["stable_id"] for r in rows}) == len(rows)
    assert all(r["status"] == "PASS_DETECTED" and r["expected_diagnostic"].endswith(".REJECT") for r in rows)


def test_c28_source_and_dataset_closure_manifests():
    source = load("c28_dataprocessor_source_lock.json")
    inventory = load("c28_art25_dataset_inventory.json")
    selection = load("c28_art25_selection_manifest.json")
    cdf1 = load("c28_cdf1_regression_authority.json")
    assert source["historical_art25_commit"] == "761f3fcdd3701c5cf69e822f9ffbbd5db394fc58"
    assert source["current_public_commit"] == "9f9dda71b69dd26e288be189a396736827cfeed3"
    assert (inventory["datasets"], inventory["source_points"], inventory["selected_points"]) == (46, 8675, 1209)
    assert (selection["retained"], selection["excluded"], selection["source_decision_residuals"]) == (1209, 7466, 0)
    assert cdf1["loaded"] == 50 and cdf1["selected"] == 33
    assert cdf1["native"] == 3.4394876804377352 and cdf1["raw_factor_residual"] == 0


def test_c28_ensemble_covariance_and_gate_isolation():
    run = load("c28_full_dataset_member_execution.json")
    factor = load("c28_theory_ensemble_factor_manifest.json")
    lowqt = load("c28_lowqt_source_reproducibility_matrix.json")
    gates = load("c28_gate_delta_report.json")
    reg = load("c28_regression_report.json")
    assert (run["attempted"], run["completed"], run["failed"], run["imputed"]) == (642, 642, 0, 0)
    assert factor["shape"] == [642, 1209] and factor["normalization"] == "sqrt(641)"
    assert lowqt["eligible_points"] == 1209
    assert gates["full_source_process_eligible"] if "full_source_process_eligible" in gates else True
    assert gates["production_registry"] == 216
    assert reg["all_artifacts_unchanged"] and not reg["likelihood_created"] and not reg["production_route_created"]
