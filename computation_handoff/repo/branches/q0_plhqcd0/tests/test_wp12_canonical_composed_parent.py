import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_inspected_canonical_parent_is_complete_positive_and_resolved():
    report = json.loads(
        (ROOT / "outputs/validation/wp12_canonical_composition.json").read_text()
    )
    assert report["status"] == "pass"
    assert report["minimum_quark_eigenvalue"] >= -1e-10
    assert report["minimum_gluon_eigenvalue"] >= -1e-10
    for name, expected_species in (
        ("wp12_canonical_composed_quark.csv", {"q", "qbar"}),
        ("wp12_canonical_composed_gluon.csv", {"g"}),
    ):
        frame = pd.read_csv(ROOT / "outputs/parent_tmds" / name)
        assert set(frame.species) == expected_species
        assert set(frame.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
        assert frame.tmd.nunique() == 18
        assert np.isfinite(frame["F_GeV-2"]).all()
    quark = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_canonical_composed_quark.csv"
    )
    assert set(quark.flavor) == {-2, -1, 1, 2}
    assert not np.allclose(
        quark[quark.flavor.eq(2)]["F_GeV-2"].to_numpy(),
        quark[quark.flavor.eq(1)]["F_GeV-2"].to_numpy(),
    )
