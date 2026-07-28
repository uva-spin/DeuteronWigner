from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "outputs/parent_tmds/wp12_wilson_channel_members.csv"


def test_wp12_wilson_channel_output_is_complete_and_reverses():
    frame = pd.read_csv(PATH, keep_default_na=False)
    assert set(frame.member) == {"soft", "central", "strong"}
    assert set(frame.correlation_group) == {
        "quark_wilson_kernel", "gluon_wilson_kernel"
    }
    assert set(frame.loc[frame.sector.ne("gluon"), "channel"]) == {
        "S_P", "S_D", "P_P"
    }
    assert set(frame.loc[frame.sector.eq("gluon"), "channel"]) == {
        "S_D_rank1", "D_D_rank2"
    }
    assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    keys = [
        "sector", "flavor", "color_structure", "member", "channel",
        "x_N", "Q_GeV", "k_T_GeV",
    ]
    future = frame.loc[frame.gauge_link.isin(["[+,+]", "[+,-]"])].copy()
    past = frame.loc[frame.gauge_link.isin(["[-,-]", "[-,+]"])].copy()
    merged = future.merge(past, on=keys, suffixes=("_f", "_p"))
    assert len(merged) == len(future)
    assert np.allclose(merged.phase_f, -merged.phase_p, atol=2e-14)
    assert frame.phase.notna().all()
    assert (frame.loc[frame.k_T_GeV.gt(0), "phase"].abs() > 0).all()


def test_wp12_wilson_members_are_correlated_not_functionwise():
    frame = pd.read_csv(PATH, keep_default_na=False)
    assert frame.groupby(["sector", "member"]).correlation_group.nunique().max() == 1
    central = frame.loc[
        frame.member.eq("central") & frame.gauge_link.eq("[+,+]")
        & frame.k_T_GeV.eq(0.4)
    ]
    assert set(central.loc[central.sector.ne("gluon"), "flavor"]) == {2, 1, -2, -1}
