from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/figures/wp12_inspection"


def test_constituent_resolved_plots_exist():
    for name in (
        "wp12_quark_valence_constituent_all_tmd.png",
        "wp12_quark_sea_constituent_all_tmd.png",
        "wp12_sivers_proton_neutron_decomposition.png",
    ):
        assert (OUT / name).stat().st_size > 20_000


def test_constituent_curves_are_dense_smooth_functions_with_bands():
    frame = pd.read_csv(OUT / "wp12_quark_constituent_smooth_bands.csv")
    assert frame.k_GeV.nunique() == 241
    assert set(frame.component) == {
        "proton_in_deuteron", "neutron_in_deuteron"
    }
    assert np.all(frame["F_low_GeV-2"] <= frame["F_central_GeV-2"])
    assert np.all(frame["F_central_GeV-2"] <= frame["F_high_GeV-2"])
    assert frame["constituent_halfwidth_GeV-2"].max() > 0
    sivers = frame[frame.tmd.eq("f1Tperp")]
    assert sivers.band_semantics.str.contains("external-fit replica").all()
