import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_wp10_ledger_covers_every_required_rich_mechanism_and_identity():
    path = Path("outputs/parent_tmds/wp10_production_member_ledger.csv")
    frame = pd.read_csv(path)
    assert set(frame.sector) == {"quark", "gluon"}
    assert {"u", "d", "ubar", "dbar", "g"}.issubset(set(frame.flavor_label))
    mechanisms = set(frame.mechanism)
    assert {
        "model_total",
        "impulse_total",
        "gauge_link_todd",
        "meson_exchange",
        "non_nucleonic",
        "coherent_shadowing",
        "axial_tensor_gauge_link_rescattering",
    }.issubset(mechanisms)
    assert {"f_type_antisymmetric", "d_type_symmetric"}.issubset(
        set(frame.color_structure)
    )
    assert {"[+,+]", "[-,-]"}.issubset(set(frame.gauge_link))
    assert "pdf_anchored_oam" in set(frame.scenario)
    assert np.all(np.isfinite(frame["F_GeV-2"]))
    assert not frame[
        [
            "scenario", "evidence_class", "uncertainty_axis",
            "stage", "combine_policy", "source_artifact", "member_id",
            "amplitude_identity", "validity",
        ]
    ].isna().any().any()


def test_wp10_ledger_metadata_forbids_unjustified_scenario_sums():
    metadata = json.loads(
        Path(
            "outputs/parent_tmds/wp10_production_member_ledger.metadata.json"
        ).read_text()
    )
    assert metadata["rows"] > 70000
    assert "not a joint probability ensemble" in metadata["combine_rule"]
    assert len(metadata["source_artifacts"]) >= 8
