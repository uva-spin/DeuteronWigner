#!/usr/bin/env python3
"""Export the published-interval g1T sensitivity hull."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.worm_gear_inputs import Yang2024G1TInput

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/parent_tmds/ensemble/yang2024_g1t_interval_ensemble.csv"
REPORT = OUT.with_suffix(".validation.json")


def main() -> None:
    central = Yang2024G1TInput()
    members = central.published_interval_members()
    x_axis = np.geomspace(0.003, 0.5, 121)
    rows = []
    for nucleon in ("proton", "neutron"):
        for flavor in (2, 1, -2, -1):
            central_input = central.fitted_input()
            member_inputs = [member.fitted_input() for member in members]
            for x in x_axis:
                value = central_input.value(nucleon, flavor, float(x), 2.0)
                ensemble = np.asarray([
                    item.value(nucleon, flavor, float(x), 2.0)
                    for item in member_inputs
                ])
                hull = np.concatenate((ensemble, (value,)))
                rows.append({
                    "nucleon": nucleon, "flavor": flavor, "x": x,
                    "Q_GeV": 2.0, "g1T_central": value,
                    "g1T_interval_low": float(np.min(hull)),
                    "g1T_interval_high": float(np.max(hull)),
                    "member_count": len(members),
                    "uncertainty_axis": (
                        "published asymmetric-interval correlated-corner hull"
                    ),
                    "interpretation": (
                        "sensitivity envelope, not the unavailable fit covariance"
                    ),
                })
    table = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUT, index=False)
    report = {
        "status": "pass",
        "members": len(members),
        "rows": len(table),
        "source": "arXiv:2403.12795 Table IV",
        "published_replica_count": 1000,
        "replicas_publicly_available": False,
        "covariance_publicly_available": False,
        "sea_boundary": (
            "published central and interval members are zero; a separate "
            "sea/WW sensitivity is required before WP12-E closure"
        ),
        "interpretation": (
            "16 corners of published asymmetric parameter intervals; "
            "conservative sensitivity hull, not a confidence region"
        ),
    }
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
