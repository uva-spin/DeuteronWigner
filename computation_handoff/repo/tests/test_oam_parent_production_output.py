import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_oam_scenario_is_parent_derived_and_reverses_only_todd_terms():
    path = Path("outputs/parent_tmds/quark_av18_oam_medium.csv")
    frame = pd.read_csv(path)
    assert set(frame.input_scenario) == {"pdf_anchored_oam"}
    total = frame.loc[frame.mechanism.eq("model_total") & frame.k_GeV.gt(0.0)]
    for tmd in ("f1Tperp", "h1perp", "g1T", "h1Lperp", "h1Tperp"):
        assert np.max(np.abs(total.loc[total.tmd.eq(tmd), "F_GeV-2"])) > 0.0
    future = total.loc[
        total.gauge_link.eq("[+,+]"),
        ["flavor", "tmd", "k_GeV", "t_odd", "F_GeV-2"],
    ]
    past = total.loc[
        total.gauge_link.eq("[-,-]"),
        ["flavor", "tmd", "k_GeV", "F_GeV-2"],
    ].rename(columns={"F_GeV-2": "past"})
    paired = future.merge(past, on=["flavor", "tmd", "k_GeV"])
    sign = np.where(paired.t_odd.eq(1), -1.0, 1.0)
    np.testing.assert_allclose(
        paired["past"], sign * paired["F_GeV-2"], atol=2e-9, rtol=2e-9
    )
    metadata = json.loads(path.with_suffix(".metadata.json").read_text())
    assert metadata["input_scenario"] == "pdf_anchored_oam"
    assert "S/P-odd" in metadata["t_odd_boundary"]["f1Tperp"]
