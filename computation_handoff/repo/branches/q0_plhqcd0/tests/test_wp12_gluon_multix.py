import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_wp12_gluon_multix_has_complete_direct_parent_slices():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_gluon_multix.json").read_text()
    )
    assert report["status"] == "pass"
    assert report["x_N"] == [0.02, 0.05, 0.1, 0.2, 0.4]
    assert report["Q_GeV"] == [5.0]
    assert report["tmd_count"] == 18
    frame = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_multikinematic/"
        "gluon_all_tmd_multix_q5.csv"
    )
    total = frame.loc[frame.mechanism.eq("model_total")]
    assert set(total.groupby(["x_N", "color_structure", "gauge_link"]).tmd.nunique()) == {18}
    assert total.groupby(["x_N", "tmd"]).size().gt(0).all()
