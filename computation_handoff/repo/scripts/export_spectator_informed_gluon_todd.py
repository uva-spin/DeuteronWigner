#!/usr/bin/env python3
"""Export source-informed six-function gluon T-odd predictions at x=.1,Q=5."""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

from deuteron_wigner.correlator_io import gluon_correlator_rows
from deuteron_wigner.gluon_correlator import compose_spin1_gluon_correlator
from deuteron_wigner.gluon_todd import (
    GLUON_TODD_RANKS,
    GluonColorStructure,
    SpectatorInformedGluonTOdd,
    add_gluon_todd_with_positivity,
)
from deuteron_wigner.gtmd import GaugeLink

SOURCE = Path("outputs/parent_tmds/gluon_av18_medium.csv")
OUTPUT = Path("outputs/parent_tmds/gluon_todd_two_stage_predictions.csv")
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")
MASS = 1.87561294257


def scenarios():
    return (
        SpectatorInformedGluonTOdd(
            label="spectator_av18_low", strength=0.55,
            alpha_s=0.25, screening_mass_gev=0.44,
            d_type_relative_coupling=0.35,
        ),
        SpectatorInformedGluonTOdd(),
        SpectatorInformedGluonTOdd(
            label="spectator_av18_high", strength=1.45,
            alpha_s=0.36, screening_mass_gev=0.28,
            d_type_relative_coupling=0.80,
        ),
    )


def main() -> None:
    frame = pd.read_csv(SOURCE)
    base_rows = frame.loc[
        frame.mechanism.eq("impulse_total") & frame.k_GeV.le(1.0)
    ]
    rows, matrix_rows = [], []
    source_k = np.sort(base_rows.k_GeV.unique())
    interpolators = {
        name: PchipInterpolator(
            source_k,
            base_rows.loc[base_rows.tmd.eq(name)]
            .sort_values("k_GeV")["F_GeV-2"],
        )
        for name in base_rows.tmd.unique()
    }
    for k in np.linspace(float(source_k[0]), float(source_k[-1]), 61):
        tmds = {name: float(curve(k)) for name, curve in interpolators.items()}
        momentum = (float(k), 0.0)
        base = compose_spin1_gluon_correlator(momentum, MASS, tmds)
        base_min = base.minimum_positivity_eigenvalue()
        if base_min < -1e-10:
            raise RuntimeError(f"base correlator not positive at k={k}: {base_min}")
        for model in scenarios():
            for color in GluonColorStructure:
                links = (
                    (GaugeLink("+", "+"), GaugeLink("-", "-"))
                    if color == GluonColorStructure.F_TYPE
                    else (GaugeLink("+", "-"), GaugeLink("-", "+"))
                )
                for link in links:
                    raw = model.values(
                        color, f1_gev2=float(tmds["f1"]), k_gev=float(k),
                        gauge_link=link,
                    )
                    result, scale, final = add_gluon_todd_with_positivity(
                        base, momentum=momentum, radial_values=raw
                    )
                    common = {
                        "sector": "gluon", "species": "g", "flavor": 21,
                        "flavor_label": "g", "scenario": model.label,
                        "color_structure": color.value,
                        "gauge_link": f"[{link.incoming},{link.outgoing}]",
                        "x_N": 0.1, "x_D": 0.05, "Q_GeV": 5.0,
                        "k_GeV": float(k), "azimuth_rad": 0.0,
                        "mechanism": "spectator_full_vertex_plus_av18_eikonal",
                        "evidence_class": "model_dependent_source_informed",
                        "combine_policy": (
                            "alternative_color_link_and_model_scenarios_"
                            "require_process_hard_weights"
                        ),
                        "positivity_scale": scale,
                        "minimum_eigenvalue": result.minimum_positivity_eigenvalue(),
                    }
                    matrix_rows.extend(gluon_correlator_rows(result.values, common))
                    for name in GLUON_TODD_RANKS:
                        rows.append({
                            **common,
                            "tmd": name,
                            "target_channel": {
                                "h1Lperp": "L", "f1Tperp": "T", "h1": "T",
                                "h1Tperp": "T", "g1LT": "LT", "g1TT": "TT",
                            }[name],
                            "rank": GLUON_TODD_RANKS[name], "t_odd": 1,
                            "raw_F_GeV-2": raw[name],
                            "F_GeV-2": final[name],
                            "source": (
                                "arXiv:2402.17556 full-vertex hierarchy for "
                                "spin-half functions; AV18 S-D coherence and "
                                "screened adjoint eikonal for spin-1-only functions"
                            ),
                            "uncertainty_axis": (
                                "published_parameter_ranges_plus_d_type_coupling_"
                                "and_screened_eikonal_scenario"
                            ),
                        })
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)
    pd.DataFrame(matrix_rows).to_csv(CORRELATORS, index=False)
    print(f"Wrote {len(rows)} TMD rows and {len(matrix_rows)} matrix rows")


if __name__ == "__main__":
    main()
