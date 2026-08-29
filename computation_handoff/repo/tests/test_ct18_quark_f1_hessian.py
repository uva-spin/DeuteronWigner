import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "outputs/parent_tmds/ensemble"


def test_ct18_f1_hessian_covers_full_production_grid():
    paths = sorted(PARENT.glob("ct18_quark_f1_hessian_x*.csv"))
    assert len(paths) == 5
    frame = pd.concat([pd.read_csv(path) for path in paths], ignore_index=True)
    assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert set(frame.flavor) == {2, 1, -2, -1}
    assert set(frame.replica_count) == {58}
    assert (frame["F_q16_GeV-2"] <= frame["F_q84_GeV-2"]).all()
    for path in paths:
        report = json.loads(path.with_suffix(".validation.json").read_text())
        assert report["status"] == "pass"
        assert report["pdf_set"] == "CT18NNLO"
        assert report["replica_count"] == 58
