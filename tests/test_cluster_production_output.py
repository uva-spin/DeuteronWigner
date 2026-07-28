import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_cluster_production_output_is_complete_flavor_resolved_and_sourced():
    path = Path("outputs/parent_tmds/nonnucleonic_cluster_tmds.csv")
    frame = pd.read_csv(path)
    assert len(frame) == 4 * 18 * 41
    assert set(frame.flavor_label) == {"u", "d", "ubar", "dbar"}
    assert set(frame.tmd.groupby(frame.flavor_label).nunique()) == {18}
    assert set(frame.mechanism) == {"non_nucleonic"}
    supported = frame.loc[frame.tmd.isin(["f1", "g1", "f1LL"])]
    unsupported = frame.loc[~frame.tmd.isin(["f1", "g1", "f1LL"])]
    assert np.max(np.abs(supported["F_GeV-2"])) > 0.0
    assert np.count_nonzero(unsupported["F_GeV-2"]) == 0
    assert set(unsupported.zero_class) == {
        "spin_zero_cluster_pdf_operator_boundary"
    }
    assert not np.allclose(
        frame.loc[(frame.flavor_label == "u") & (frame.tmd == "f1"), "F_GeV-2"],
        frame.loc[(frame.flavor_label == "ubar") & (frame.tmd == "f1"), "F_GeV-2"],
    )
    metadata = json.loads(path.with_suffix(".metadata.json").read_text())
    assert metadata["implemented_nonzero_tmds"] == ["f1", "g1", "f1LL"]
    assert "not an extracted hidden-color probability" in metadata["limitations"]
