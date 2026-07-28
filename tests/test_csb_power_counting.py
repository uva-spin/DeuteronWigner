import json
from pathlib import Path

import pandas as pd

from deuteron_wigner.csb_power_counting import (
    TMDChargeSymmetryBreakingEnvelope,
)


ROOT = Path(__file__).resolve().parents[1]


def test_csb_envelope_is_zero_centered_and_rank_aware():
    model = TMDChargeSymmetryBreakingEnvelope()
    assert model.halfwidth(
        central=2.0, f1=4.0, rank_weight=0.5, species="quark"
    ) == 0.1
    assert model.halfwidth(
        central=0.0, f1=4.0, rank_weight=0.5, species="gluon"
    ) > 0


def test_exported_csb_envelope_covers_complete_bases():
    table = pd.read_csv(
        ROOT / "outputs/parent_tmds/wp12_csb_power_counting_envelope.csv"
    )
    assert table.groupby("species").tmd.nunique().to_dict() == {
        "gluon": 18, "quark": 18
    }
    assert (table["central_csb_shift_GeV-2"] == 0).all()
    assert (table["csb_halfwidth_GeV-2"] >= 0).all()
    report = json.loads((
        ROOT / "outputs/validation/wp12_csb_power_counting_envelope.json"
    ).read_text())
    assert report["status"] == "pass"
