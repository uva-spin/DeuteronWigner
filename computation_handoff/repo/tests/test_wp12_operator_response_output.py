import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_operator_response_members_are_complete_and_positive():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_operator_response.json").read_text()
    )
    assert report["status"] == "pass"
    assert report["minimum_mapped_parent_eigenvalue"] >= -1e-10
    assert report["maximum_chain_closure_residual"] < 1e-10
    frame = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_operator_response_members.correlators.csv"
    )
    assert set(frame["response_member"]) == {"weak", "central", "strong"}
    assert set(frame["response_stage"]) == {"increment", "mapped_parent"}
    assert set(frame["sector"]) == {"q", "qbar", "g"}
    assert set(frame["x_N"].round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert set(frame["mechanism"]) == {
        "coherent_shadowing", "antishadowing", "off_shell",
        "meson_exchange", "short_range_correlation", "ordered_total",
    }
