import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / (
    "outputs/parent_tmds/ensemble/bdssv24_quark_g1_bands_x010.csv"
)


def test_bdssv_quark_g1_replica_response_is_complete():
    paths = sorted(TABLE.parent.glob("bdssv24_quark_g1_bands_x*.csv"))
    assert len(paths) == 5
    frame = pd.concat([pd.read_csv(path) for path in paths], ignore_index=True)
    assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert set(frame.flavor) == {2, 1, -2, -1}
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]"}
    assert {
        "proton_impulse", "neutron_impulse", "impulse_total",
        "off_shell", "model_total",
    } <= set(frame.mechanism)
    assert set(frame.replica_count) == {600}
    assert (frame["F_q16_GeV-2"] <= frame["F_q84_GeV-2"]).all()
    for path in paths:
        report = json.loads(path.with_suffix(".validation.json").read_text())
        assert report["status"] == "pass"
        assert report["replica_count"] == 600
