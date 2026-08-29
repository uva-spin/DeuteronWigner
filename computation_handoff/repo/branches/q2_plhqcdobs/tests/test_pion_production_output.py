import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_pion_production_output_has_full_basis_and_sourced_u_ll_content():
    path = Path("outputs/parent_tmds/spin_resolved_pion_tmds.csv")
    frame = pd.read_csv(path)
    assert len(frame) == 4 * 18 * 41
    assert set(frame.flavor_label) == {"u", "d", "ubar", "dbar"}
    assert set(frame.tmd.groupby(frame.flavor_label).nunique()) == {18}
    assert set(frame.mechanism) == {"meson_exchange"}
    supported = frame.loc[frame.tmd.isin(["f1", "f1LL"])]
    unsupported = frame.loc[~frame.tmd.isin(["f1", "f1LL"])]
    assert np.max(np.abs(supported.loc[supported.tmd.eq("f1"), "F_GeV-2"])) > 0.0
    assert np.max(np.abs(supported.loc[supported.tmd.eq("f1LL"), "F_GeV-2"])) > 0.0
    assert np.count_nonzero(unsupported["F_GeV-2"]) == 0
    assert set(unsupported.zero_class) == {"spin_zero_pion_operator_boundary"}


def test_pion_production_metadata_closes_fock_momentum_ledger():
    metadata = json.loads(
        Path(
            "outputs/parent_tmds/spin_resolved_pion_tmds.metadata.json"
        ).read_text()
    )
    assert metadata["implemented_nonzero_tmds"] == ["f1", "f1LL"]
    assert np.isclose(metadata["fock_ledger"]["total_plus_momentum"], 1.0)
    assert metadata["transform"].startswith("rank-zero Fourier-Bessel")
