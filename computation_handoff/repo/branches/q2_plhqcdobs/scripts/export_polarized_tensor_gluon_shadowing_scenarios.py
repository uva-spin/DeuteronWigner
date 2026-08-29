#!/usr/bin/env python3
"""Export irreducible polarized/tensor gluon-shadowing correlator scenarios."""

from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    deserialize_gluon_correlator,
    gluon_correlator_rows,
)
from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.gluon_nuclear_mechanisms import (
    apply_gluon_nuclear_mechanisms,
    build_polarized_tensor_gluon_shadowing_input,
)
from deuteron_wigner.spin import project_matrix, spin_one_basis

INPUT = Path(
    "outputs/parent_tmds/gluon_av18_shadowing_x001_medium.correlators.csv"
)
OUTPUT = Path(
    "outputs/parent_tmds/gluon_polarized_tensor_shadowing_scenarios.csv"
)
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")

SCENARIOS = {
    "spin_weak": {
        "target": {"U": 1.0, "L": 0.30, "T": 0.30, "LL": 0.70, "LT": 0.45, "TT": 0.45},
        "gluon": {"trace": 1.0, "circular": 0.30, "linear": 0.45},
    },
    "spin_central": {
        "target": {"U": 1.0, "L": 0.65, "T": 0.65, "LL": 1.35, "LT": 1.0, "TT": 1.0},
        "gluon": {"trace": 1.0, "circular": 0.65, "linear": 0.80},
    },
    "spin_strong": {
        "target": {"U": 1.0, "L": 1.0, "T": 1.0, "LL": 2.0, "LT": 1.5, "TT": 1.5},
        "gluon": {"trace": 1.0, "circular": 1.0, "linear": 1.2},
    },
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    keys = ["wave_function", "species", "flavor", "gauge_link", "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad"]
    projections = []
    correlator_rows = []
    for labels, group in frame.groupby(keys, sort=False):
        metadata = dict(zip(keys, labels))
        proton = deserialize_gluon_correlator(
            group.loc[group.mechanism.eq("proton_impulse")]
        )
        neutron = deserialize_gluon_correlator(
            group.loc[group.mechanism.eq("neutron_impulse")]
        )
        for scenario, ratios in SCENARIOS.items():
            shadow = build_polarized_tensor_gluon_shadowing_input(
                target_group_ratios=ratios["target"],
                gluon_polarization_ratios=ratios["gluon"],
            )
            result = apply_gluon_nuclear_mechanisms(
                proton_impulse=proton,
                neutron_impulse=neutron,
                x=float(metadata["x_N"]),
                scale_gev=float(metadata["Q_GeV"]),
                inputs={"coherent_shadowing": shadow},
            )
            correction = result.corrections["coherent_shadowing"]
            common = {
                **metadata,
                "scenario": scenario,
                "mechanism": "coherent_shadowing",
                "evidence_class": "model_dependent",
                "uncertainty_axis": "polarized_tensor_response_scenario",
            }
            correlator_rows.extend(gluon_correlator_rows(correction, common))
            for channel, tensor in spin_one_basis().items():
                transverse = np.asarray(
                    [
                        [
                            project_matrix(correction[:, :, i, j], tensor)
                            for j in range(2)
                        ]
                        for i in range(2)
                    ]
                )
                trace, circular, linear = transverse_matrix_parts(transverse)
                projections.append(
                    {
                        **common,
                        "target_channel": channel,
                        "trace_real": float(np.real(trace)),
                        "circular_real": float(np.real(circular)),
                        "linear_xx_real": float(np.real(linear[0, 0])),
                        "linear_xy_real": float(np.real(linear[0, 1])),
                        "linear_norm": float(np.linalg.norm(linear)),
                        "source": shadow.source,
                    }
                )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(projections).to_csv(OUTPUT, index=False)
    pd.DataFrame(correlator_rows).to_csv(CORRELATORS, index=False)
    print(
        f"Wrote {len(projections)} projections and {len(correlator_rows)} "
        f"correlator entries"
    )


if __name__ == "__main__":
    main()
