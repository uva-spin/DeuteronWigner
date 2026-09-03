import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / (
    "outputs/parent_tmds/ensemble/ct18_gluon_f1_hessian_response.csv"
)


def test_gluon_f1_hessian_response_covers_production_grid():
    table = pd.read_csv(TABLE)
    assert set(table.x_N.round(2)) == {0.02, 0.05, 0.10, 0.20, 0.40}
    assert table.k_GeV.nunique() == 61
    assert set(table.paired_eigenvectors) == {29}
    assert (table["hessian_sigma_GeV-2"] >= 0).all()
    report = json.loads(TABLE.with_suffix(".validation.json").read_text())
    assert report["status"] == "pass"
    assert report["paired_eigenvectors"] == 29
