from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "outputs/parent_tmds/wp12_fock_oam_members.csv"


def test_fock_oam_output_is_flavor_resolved_correlated_and_positive():
    frame = pd.read_csv(PATH, keep_default_na=False)
    quark = frame.loc[frame.species.ne("gluon")]
    assert set(quark.flavor) == {2, 1, -2, -1}
    assert quark.tmd.nunique() == 8
    assert set(quark.gauge_link) == {"[+,+]", "[-,-]"}
    assert set(quark.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert quark.groupby(["x_N", "flavor"]).amplitudes.nunique().eq(1).all()
    assert quark.calibration_residual.max() < 0.08
    gluon = frame.loc[frame.species.eq("gluon")]
    assert gluon.groupby(["x_N", "gauge_link", "k_T_GeV"]).size().eq(16).all()
    assert pd.to_numeric(gluon.minimum_eigenvalue).min() >= -1e-12
    assert gluon.groupby("x_N").amplitudes.nunique().eq(1).all()
