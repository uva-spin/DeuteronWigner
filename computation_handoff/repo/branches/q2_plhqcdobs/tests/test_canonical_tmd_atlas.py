from pathlib import Path

import pandas as pd
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
QCSV = ROOT / "outputs/parent_tmds/canonical/canonical_quark_spin1_tmd_bands.csv"
GCSV = ROOT / "outputs/parent_tmds/canonical/canonical_gluon_spin1_tmd_bands.csv"


def test_canonical_atlas_tables_are_complete_and_ordered():
    quark = pd.read_csv(QCSV)
    gluon = pd.read_csv(GCSV)
    assert quark.tmd.nunique() == 18
    assert set(quark.flavor) == {2, 1, -2, -1}
    assert set(quark.groupby(["flavor", "tmd"]).size()) == {241}
    assert gluon.tmd.nunique() == 18
    assert set(gluon.color_structure) == {
        "f_type_antisymmetric", "d_type_symmetric"
    }
    assert set(gluon.groupby(["color_structure", "tmd"]).size()) == {241}
    for frame in (quark, gluon):
        assert frame.select_dtypes("number").notna().all().all()
        assert (frame["F_low_GeV-2"] <= frame["F_central_GeV-2"]).all()
        assert (frame["F_central_GeV-2"] <= frame["F_high_GeV-2"]).all()
        assert set(frame.band_semantics) == {
            "conservative named-axis theory envelope"
        }


def test_canonical_atlas_preserves_flavor_color_and_active_uncertainty():
    quark = pd.read_csv(QCSV)
    gluon = pd.read_csv(GCSV)
    at_zero = quark.loc[quark.k_GeV.eq(0.0)]
    assert at_zero.loc[at_zero.tmd.eq("f1")].groupby("flavor")[
        "F_central_GeV-2"
    ].first().nunique() == 4
    for tmd in ("h1perp", "g1T", "h1Tperp", "g1LT", "g1TT"):
        block = quark.loc[quark.tmd.eq(tmd)]
        assert (block["F_high_GeV-2"] > block["F_low_GeV-2"]).any()
    for tmd in gluon.loc[gluon.t_odd.eq(1), "tmd"].unique():
        block = gluon.loc[gluon.tmd.eq(tmd)]
        assert (block["model_halfwidth_GeV-2"] > 0).any()


def test_canonical_atlas_pdfs_have_one_page_per_tmd():
    for name in (
        "canonical_quark_spin1_tmd_atlas.pdf",
        "canonical_gluon_spin1_tmd_atlas.pdf",
    ):
        reader = PdfReader(ROOT / "output/pdf" / name)
        assert len(reader.pages) == 18

