from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "outputs/parent_tmds/wp12_wilson_projected_members.csv"


def test_wilson_members_propagate_through_complete_tmd_bases():
    frame = pd.read_csv(PATH, keep_default_na=False, low_memory=False)
    assert set(frame.member) == {"soft", "central", "strong"}
    assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert set(frame.species) == {"q", "qbar", "g"}
    assert set(frame.loc[frame.species.ne("g"), "tmd"].unique()) == {
        "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
        "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
        "h1LTperp", "f1TT", "g1TT", "h1TT", "h1TTperp",
    }
    assert frame.loc[frame.species.eq("g"), "tmd"].nunique() == 18
    assert np.isfinite(frame["F_GeV-2"]).all()


def test_central_wilson_member_reproduces_retained_canonical_projection():
    frame = pd.read_csv(PATH, keep_default_na=False, low_memory=False)
    central = frame[frame.member.eq("central")]
    for source in (
        "quark_all_tmd_multix_q5.csv", "gluon_all_tmd_multix_q5.csv",
    ):
        retained = pd.read_csv(
            ROOT / "outputs/parent_tmds/wp12_multikinematic" / source,
            low_memory=False,
        )
        retained = retained[retained.mechanism.eq("model_total")]
        keys = [
            "species", "flavor", "gauge_link", "x_N", "Q_GeV",
            "k_GeV", "tmd",
        ]
        if source.startswith("gluon"):
            keys.append("color_structure")
        merged = retained.merge(central, on=keys, suffixes=("_r", "_w"))
        assert len(merged) == len(retained)
        assert np.allclose(
            merged["F_GeV-2_r"], merged["F_GeV-2_w"],
            rtol=2e-8, atol=1e-9,
        )
