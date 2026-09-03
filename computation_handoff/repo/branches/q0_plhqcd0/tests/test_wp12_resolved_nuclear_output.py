import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_resolved_parent_output_is_complete_and_closes():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_resolved_nuclear_parent.json").read_text()
    )
    assert report["status"] == "pass"
    assert report["maximum_quark_closure_residual"] < 1e-11
    assert report["maximum_gluon_closure_residual"] < 1e-11
    expected = {
        "proton_in_deuteron", "neutron_in_deuteron", "nucleon_sum",
        "proton_minus_neutron", "nuclear_correction",
        "canonical_spin1_total",
    }
    for name in (
        "wp12_resolved_quark_parent.csv", "wp12_resolved_gluon_parent.csv"
    ):
        frame = pd.read_csv(ROOT / "outputs/parent_tmds" / name)
        assert set(frame.component) == expected
        assert frame.tmd.nunique() == 18
        assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
        assert np.isfinite(frame["F_GeV-2"]).all()


def test_proton_sivers_retains_opposite_u_and_d_orbital_signs():
    frame = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_resolved_quark_parent.csv"
    )
    block = frame[
        frame.component.eq("proton_in_deuteron")
        & frame.tmd.eq("f1Tperp") & frame.gauge_link.eq("[+,+]")
        & np.isclose(frame.x_N, 0.1)
    ]
    moments = {}
    for flavor, part in block.groupby("flavor"):
        part = part.sort_values("k_GeV")
        moments[int(flavor)] = np.trapz(
            2*np.pi*part.k_GeV*part["F_GeV-2"], part.k_GeV
        )
    assert moments[2] < 0 < moments[1]
    assert not np.isclose(moments[2], moments[1])
