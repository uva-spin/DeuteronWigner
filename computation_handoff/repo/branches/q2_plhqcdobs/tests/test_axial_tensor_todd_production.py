from pathlib import Path

import numpy as np
import pandas as pd


def test_axial_tensor_todd_production_has_both_stages_flavors_and_links():
    frame = pd.read_csv(
        Path("outputs/parent_tmds/quark_axial_tensor_todd_stages.csv")
    )
    assert set(frame.stage) == {
        "positivity_bounded_phase",
        "screened_one_gluon_rescattering",
    }
    assert set(frame.flavor_label) == {"u", "d", "ubar", "dbar"}
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]"}
    selected = frame.loc[
        frame.tmd.isin(["g1LT", "g1TT"]) & frame.k_GeV.gt(0)
    ]
    assert (
        selected.groupby(["stage", "tmd"])["F_GeV-2"]
        .apply(lambda x: np.max(np.abs(x)) > 0.0)
        .all()
    )
    assert selected.minimum_density_eigenvalue.min() >= -1e-10


def test_axial_tensor_todd_production_has_exact_link_reversal():
    frame = pd.read_csv(
        Path("outputs/parent_tmds/quark_axial_tensor_todd_stages.csv")
    )
    selected = frame.loc[frame.tmd.isin(["g1LT", "g1TT"])]
    keys = ["stage", "scenario", "flavor_label", "tmd", "k_GeV"]
    for identity, pair in selected.groupby(keys):
        assert len(pair) == 2, identity
        future = pair.loc[pair.gauge_link.eq("[+,+]"), "F_GeV-2"].iloc[0]
        past = pair.loc[pair.gauge_link.eq("[-,-]"), "F_GeV-2"].iloc[0]
        assert np.isclose(future, -past, atol=2e-10), identity


def test_rescattering_shapes_are_not_constant_rescalings_of_phase_model():
    frame = pd.read_csv(
        Path("outputs/parent_tmds/quark_axial_tensor_todd_stages.csv")
    )
    selected = frame.loc[
        frame.gauge_link.eq("[+,+]")
        & frame.flavor_label.eq("u")
        & frame.tmd.eq("g1LT")
        & frame.k_GeV.gt(0)
    ]
    phase = selected.loc[
        selected.stage.eq("positivity_bounded_phase")
        & selected.scenario.eq("phase_central")
    ].sort_values("k_GeV")
    eikonal = selected.loc[
        selected.stage.eq("screened_one_gluon_rescattering")
        & selected.scenario.eq("screened_central")
    ].sort_values("k_GeV")
    ratio = eikonal["F_GeV-2"].to_numpy() / phase["F_GeV-2"].to_numpy()
    assert np.ptp(ratio) > 1e-3
