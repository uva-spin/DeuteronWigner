import numpy as np
import pandas as pd


def test_boer_mulders_parent_scenarios_cover_all_flavor_corners_and_links():
    frame = pd.read_csv(
        "outputs/parent_tmds/boer_mulders_parent_scenarios.csv"
    )
    assert len(frame) == 6 * 2 * 9 * 4 * 4
    assert set(frame.flavor_label) == {"u", "d", "ubar", "dbar"}
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]"}
    assert set(frame.uncertainty_axis) == {
        "independent_Boer_Mulders_flavor_coefficients"
    }
    assert set(frame.groupby(
        ["wave_function", "gauge_link", "flavor", "k_GeV"]
    ).scenario.nunique()) == {4}
    future = frame.loc[frame.gauge_link.eq("[+,+]")]
    past = frame.loc[frame.gauge_link.eq("[-,-]")]
    paired = future.merge(
        past,
        on=["wave_function", "flavor", "k_GeV", "scenario"],
        suffixes=("_future", "_past"),
    )
    np.testing.assert_allclose(
        paired["F_GeV-2_past"], -paired["F_GeV-2_future"], atol=2e-10
    )
