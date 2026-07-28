import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_quark_multix_has_every_flavor_tmd_and_positive_parent():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_quark_multix.json").read_text()
    )
    assert report["status"] == "pass"
    assert report["x_N"] == [0.02, 0.05, 0.1, 0.2, 0.4]
    assert report["flavors"] == [-2, -1, 1, 2]
    assert report["tmd_count"] == 18
    assert report["maximum_link_reversal_residual_GeV-2"] < 3e-9
    assert report["minimum_model_total_density_eigenvalue"] >= -2e-9
    frame = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_multikinematic/"
        "quark_all_tmd_multix_q5.csv"
    )
    total = frame.loc[frame.mechanism.eq("model_total")]
    assert set(total.groupby(["x_N", "flavor", "gauge_link"]).tmd.nunique()) == {18}
