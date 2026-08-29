from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/figures/wp12_inspection"


def test_wp12_inspection_band_tables_cover_complete_bases():
    q = pd.read_csv(OUT / "wp12_quark_inspection_bands.csv")
    g = pd.read_csv(OUT / "wp12_gluon_inspection_bands.csv")
    assert q.tmd.nunique() == g.tmd.nunique() == 18
    assert set(q.flavor) == {-2, -1, 1, 2}
    assert set(g.color_structure) == {
        "f_type_antisymmetric", "d_type_symmetric"
    }
    for frame in (q, g):
        assert (frame["F_low_GeV-2"] <= frame["F_central_GeV-2"]).all()
        assert (frame["F_central_GeV-2"] <= frame["F_high_GeV-2"]).all()
        assert set(frame.x_N.round(1)) == {0.1}
        assert frame["pdf_halfwidth_GeV-2"].max() > 0
        assert frame["csb_halfwidth_GeV-2"].max() > 0


def test_wp12_inspection_figures_exist_and_are_nontrivial():
    names = (
        "wp12_quark_all_tmd_F_x010.png",
        "wp12_gluon_all_tmd_F_x010.png",
        "wp12_quark_all_tmd_rank_weighted_x010.png",
        "wp12_gluon_all_tmd_rank_weighted_x010.png",
        "wp12_quark_tmd_inspection_atlas.pdf",
        "wp12_gluon_tmd_inspection_atlas.pdf",
    )
    for name in names:
        assert (OUT / name).stat().st_size > 20_000
