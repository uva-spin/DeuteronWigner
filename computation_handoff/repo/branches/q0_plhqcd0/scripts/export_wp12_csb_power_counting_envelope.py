#!/usr/bin/env python3
"""Export zero-centered CSB sensitivities for every resolved TMD."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.csb_power_counting import (
    TMDChargeSymmetryBreakingEnvelope,
)

ROOT = Path(__file__).resolve().parents[1]
MASS = 1.87561294257
Q = ROOT / "outputs/parent_tmds/wp12_resolved_quark_parent.csv"
G = ROOT / "outputs/parent_tmds/wp12_resolved_gluon_parent.csv"
OUT = ROOT / "outputs/parent_tmds/wp12_csb_power_counting_envelope.csv"
REPORT = ROOT / "outputs/validation/wp12_csb_power_counting_envelope.json"


def sector(frame: pd.DataFrame, species: str) -> list[dict[str, object]]:
    frame = frame[frame.component.eq("canonical_spin1_total")].copy()
    identity = (
        ["flavor", "gauge_link", "x_N", "Q_GeV", "k_GeV"]
        if species == "quark" else
        ["color_structure", "gauge_link", "x_N", "Q_GeV", "k_GeV"]
    )
    f1 = frame[frame.tmd.eq("f1")].set_index(identity)["F_GeV-2"]
    model = TMDChargeSymmetryBreakingEnvelope()
    rows = []
    for _, item in frame.iterrows():
        key = tuple(item[name] for name in identity)
        rank_weight = (float(item.k_GeV)/MASS)**int(item["rank"])
        width = model.halfwidth(
            central=float(item["F_GeV-2"]),
            f1=float(f1.loc[key]), rank_weight=rank_weight,
            species=species,
        )
        rows.append({
            "species": species, "tmd": item.tmd,
            "flavor": int(item.flavor),
            "color_structure": item.color_structure,
            "gauge_link": item.gauge_link, "x_N": float(item.x_N),
            "Q_GeV": float(item.Q_GeV), "k_GeV": float(item.k_GeV),
            "rank": int(item["rank"]), "central_csb_shift_GeV-2": 0.0,
            "csb_halfwidth_GeV-2": width,
            "lower_csb_shift_GeV-2": -width,
            "upper_csb_shift_GeV-2": width,
            "evidence_class": "model_power_counting_sensitivity",
            "interpretation": model.interpretation,
        })
    return rows


def main() -> None:
    rows = sector(pd.read_csv(Q), "quark")
    rows += sector(pd.read_csv(G), "gluon")
    table = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUT, index=False)
    model = TMDChargeSymmetryBreakingEnvelope()
    report = {
        "status": "pass",
        "rows": len(table),
        "quark_fraction": model.quark_fraction,
        "gluon_fraction": model.gluon_fraction,
        "central_shift_is_exactly_zero": bool(
            np.all(table["central_csb_shift_GeV-2"] == 0)
        ),
        "sources": model.sources,
        "interpretation": model.interpretation,
        "replacement_rule": (
            "replace the named sector envelope when a TMD-specific QCD+QED "
            "lattice calculation or phenomenological CSB fit becomes available"
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
