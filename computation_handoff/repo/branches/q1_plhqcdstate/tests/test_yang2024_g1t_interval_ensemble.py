import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "outputs/parent_tmds/ensemble/yang2024_g1t_interval_ensemble.csv"


def test_yang_interval_ensemble_is_flavor_and_nucleon_resolved():
    table = pd.read_csv(TABLE)
    assert set(table.nucleon) == {"proton", "neutron"}
    assert set(table.flavor) == {2, 1, -2, -1}
    assert set(table.member_count) == {16}
    assert (table.g1T_interval_low <= table.g1T_central).all()
    assert (table.g1T_central <= table.g1T_interval_high).all()
    report = json.loads(TABLE.with_suffix(".validation.json").read_text())
    assert report["status"] == "pass"
    assert not report["replicas_publicly_available"]
