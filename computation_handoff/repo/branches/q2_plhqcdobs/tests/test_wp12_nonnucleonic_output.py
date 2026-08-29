from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TMD = ROOT / "outputs/parent_tmds/wp12_nonnucleonic_transverse.csv"
MATRIX = ROOT / "outputs/parent_tmds/wp12_nonnucleonic_transverse.correlators.csv"


def test_wp12_nonnucleonic_output_has_every_sector_species_and_basis():
    frame = pd.read_csv(TMD, keep_default_na=False)
    assert set(frame.sector) == {
        "NNpi", "DeltaDelta", "hidden_color_6q", "short_range_NN"
    }
    assert set(frame.species) == {"quark", "antiquark", "gluon"}
    assert set(frame.member) == {"central", "sensitivity"}
    assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert set(frame.loc[frame.species.ne("gluon"), "tmd"].unique()) == {
        "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
        "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
        "h1LTperp", "f1TT", "g1TT", "h1TT", "h1TTperp",
    }
    assert frame.loc[frame.species.eq("gluon"), "tmd"].nunique() == 18


def test_unsupported_central_members_are_exactly_zero_and_parents_complete():
    frame = pd.read_csv(TMD, keep_default_na=False)
    unsupported = frame.loc[frame.member.eq("central")]
    assert (unsupported["canonical_weight"] == 0).all()
    assert (unsupported["F_GeV-2"] == 0).all()
    sensitivity = frame.loc[
        frame.sector.ne("NNpi") & frame.member.eq("sensitivity")
    ]
    assert (sensitivity["canonical_weight"] > 0).all()
    assert (sensitivity["F_GeV-2"].abs() > 0).any()
    matrices = pd.read_csv(MATRIX, keep_default_na=False)
    counts = matrices.groupby([
        "sector", "species", "flavor", "member", "gauge_link", "k_T_GeV"
        , "x_N"
    ]).size()
    assert set(counts) == {36}
