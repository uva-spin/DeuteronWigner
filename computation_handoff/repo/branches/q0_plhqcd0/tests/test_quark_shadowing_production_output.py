import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import deserialize_quark_correlator


def test_quark_polarized_tensor_shadowing_scenarios_are_flavor_complete():
    frame = pd.read_csv(
        "outputs/parent_tmds/quark_polarized_tensor_shadowing_scenarios.csv"
    )
    assert set(frame.scenario) == {"spin_weak", "spin_central", "spin_strong"}
    assert set(frame.flavor_label) == {"u", "d", "ubar", "dbar"}
    assert set(frame.tmd.groupby([frame.scenario, frame.flavor_label]).nunique()) == {18}
    assert np.max(np.abs(frame["F_GeV-2"])) > 0.0
    # LL-sensitive f1LL must respond to the named tensor ratios.
    tensor = frame.loc[
        frame.tmd.eq("f1LL")
        & frame.flavor_label.eq("u")
        & frame.gauge_link.eq("[+,+]")
    ].pivot(index="k_GeV", columns="scenario", values="F_GeV-2")
    assert not np.allclose(tensor["spin_weak"], tensor["spin_strong"])


def test_quark_shadowing_scenario_correlators_are_hermitian():
    frame = pd.read_csv(
        "outputs/parent_tmds/"
        "quark_polarized_tensor_shadowing_scenarios.correlators.csv"
    )
    keys = ["scenario", "flavor", "gauge_link", "k_GeV"]
    for _, group in frame.groupby(keys):
        correlator = deserialize_quark_correlator(group)
        np.testing.assert_allclose(
            correlator.vector, correlator.vector.conj().T, atol=1e-12
        )
        np.testing.assert_allclose(
            correlator.axial, correlator.axial.conj().T, atol=1e-12
        )
        np.testing.assert_allclose(
            correlator.transverse,
            correlator.transverse.conj().transpose(0, 2, 1),
            atol=1e-12,
        )
