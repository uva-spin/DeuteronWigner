from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import deserialize_gluon_correlator


def test_gluon_polarized_tensor_shadowing_scenarios_are_full_and_distinct():
    path = Path(
        "outputs/parent_tmds/gluon_polarized_tensor_shadowing_scenarios.csv"
    )
    frame = pd.read_csv(path)
    assert set(frame.scenario) == {"spin_weak", "spin_central", "spin_strong"}
    assert frame.k_GeV.nunique() == 9
    assert frame.target_channel.nunique() == 9
    # Inclusive U/trace anchor is common; polarized/tensor responses differ.
    ll = frame.loc[frame.target_channel.eq("LL")].pivot(
        index="k_GeV", columns="scenario", values="trace_real"
    )
    assert not np.allclose(ll["spin_weak"], ll["spin_strong"])
    u = frame.loc[frame.target_channel.eq("U")].pivot(
        index="k_GeV", columns="scenario", values="trace_real"
    )
    np.testing.assert_allclose(u["spin_weak"], u["spin_strong"])


def test_gluon_shadowing_scenario_correlators_are_hermitian():
    frame = pd.read_csv(
        "outputs/parent_tmds/"
        "gluon_polarized_tensor_shadowing_scenarios.correlators.csv"
    )
    keys = ["scenario", "k_GeV"]
    for _, group in frame.groupby(keys):
        values = deserialize_gluon_correlator(group)
        np.testing.assert_allclose(
            values, values.transpose(1, 0, 3, 2).conj(), atol=1e-12
        )
