import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_rich_quark_parent_activates_fitted_and_modeled_inputs():
    path = Path("outputs/parent_tmds/quark_av18_rich_medium.csv")
    frame = pd.read_csv(path)
    selected = frame.loc[
        frame.mechanism.eq("model_total")
        & frame.gauge_link.eq("[+,+]")
        & frame.k_GeV.gt(0.0)
    ]
    for tmd in (
        "f1Tperp", "h1perp", "g1T", "h1Tperp", "g1LT", "g1TT",
    ):
        assert np.max(np.abs(selected.loc[selected.tmd.eq(tmd), "F_GeV-2"])) > 0.0
    f1 = selected.loc[selected.tmd.eq("f1")].pivot(
        index="k_GeV", columns="flavor_label", values="F_GeV-2"
    )
    assert not np.allclose(f1["u"], f1["d"])
    assert not np.allclose(f1["ubar"], f1["dbar"])
    for tmd in ("g1LT", "g1TT"):
        pairs = frame.loc[
            frame.mechanism.eq("model_total")
            & frame.tmd.eq(tmd)
            & frame.k_GeV.gt(0.0)
        ]
        future = pairs.loc[pairs.gauge_link.eq("[+,+]")]
        past = pairs.loc[pairs.gauge_link.eq("[-,-]")]
        joined = future.merge(
            past, on=["flavor", "k_GeV"], suffixes=("_f", "_p")
        )
        assert np.allclose(
            joined["F_GeV-2_f"], -joined["F_GeV-2_p"], atol=3.0e-12
        )


def test_rich_quark_metadata_declares_active_csb_and_input_limitations():
    metadata = json.loads(
        Path("outputs/parent_tmds/quark_av18_rich_medium.metadata.json").read_text()
    )
    assert metadata["charge_symmetry"]["active_csb_qed_correction"] is True
    limitations = " ".join(metadata["limitations"])
    assert "Yang et al. 2024" in limitations
    assert "pretzelosity uses independent flavor-resolved" in limitations
    assert "no unsupported CSB" in limitations
    phase = metadata["axial_tensor_nuclear_phase"]
    assert phase["d_state_probability"] > 0.0
    assert abs(phase["sd_radial_coherence"]) > 0.0
    assert "before projection" in phase["implementation"]
