#!/usr/bin/env python3
"""Propagate independent Boer--Mulders coefficient corners through LF parents."""

from pathlib import Path

import numpy as np
import pandas as pd

WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
LAMBDA = {2: 2.0, 1: -1.1, -2: 0.35, -1: -0.25}
RELATIVE = {2: 0.50, 1: 0.70, -2: 1.00, -1: 1.00}
ISOSPIN = {2: 1, 1: 2, -2: -1, -1: -2}
OUTPUT = Path("outputs/parent_tmds/boer_mulders_parent_scenarios.csv")


def interval(flavor: int) -> tuple[float, float]:
    central = LAMBDA[flavor]
    error = abs(central) * RELATIVE[flavor]
    return central - error, central + error


def main() -> None:
    rows = []
    for wave in WAVES:
        path = Path(f"outputs/parent_tmds/quark_{wave}_rich_medium.csv")
        frame = pd.read_csv(path)
        selected = frame.loc[frame.tmd.eq("h1perp")]
        keys = [
            "species", "flavor", "flavor_label", "gauge_link",
            "x_N", "Q_GeV", "k_GeV",
        ]
        for labels, group in selected.groupby(keys, sort=False):
            common = dict(zip(keys, labels))
            flavor = int(common["flavor"])
            partner = ISOSPIN[flavor]
            values = group.set_index("mechanism")["F_GeV-2"]
            proton = float(values["proton_impulse"])
            neutron = float(values["neutron_impulse"])
            impulse = proton + neutron
            total = float(values["model_total"])
            correction_factor = total / impulse if abs(impulse) > 1.0e-20 else 1.0
            first_interval = interval(flavor)
            second_interval = interval(partner)
            for first_label, first in zip(("low", "high"), first_interval):
                for second_label, second in zip(("low", "high"), second_interval):
                    varied_impulse = (
                        proton * first / LAMBDA[flavor]
                        + neutron * second / LAMBDA[partner]
                    )
                    rows.append(
                        {
                            **common,
                            "wave_function": wave,
                            "tmd": "h1perp",
                            "target_channel": "U",
                            "scenario": (
                                f"lambda_{flavor}_{first_label}__"
                                f"lambda_{partner}_{second_label}"
                            ),
                            "active_flavor_coefficient": first,
                            "neutron_partner_coefficient": second,
                            "F_GeV-2": correction_factor * varied_impulse,
                            "mechanism": "model_total",
                            "evidence_class": "model_dependent",
                            "uncertainty_axis": (
                                "independent_Boer_Mulders_flavor_coefficients"
                            ),
                            "combine_policy": "independent_corner_envelope_not_gaussian",
                            "source": (
                                "Barone-Melis-Prokudin proportionality model "
                                "composed with BPV20"
                            ),
                        }
                    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(OUTPUT, index=False)
    print(f"Wrote {len(frame)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
