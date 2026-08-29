#!/usr/bin/env python3
"""Export all six leading-twist spin-1 gluon T-odd f/d boundaries."""

from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import gluon_correlator_rows
from deuteron_wigner.gluon_todd import (
    GLUON_TODD_RANKS,
    GluonColorStructure,
    Spin1GluonTOddMultipletInput,
    build_cgi_gpm_gluon_sivers_input,
    cgi_gpm_gluon_sivers_scenarios,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.pdfs import LHAPDFProvider

OUTPUT = Path("outputs/parent_tmds/complete_gluon_todd_multiplet.csv")
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    x = 0.1
    q = 5.0
    # Use an axis-aligned representative momentum so hypot(kx, ky) does not
    # round the documented k=1.5 GeV endpoint above its closed validity bound.
    azimuth = 0.0
    k_axis = np.linspace(0.0, 1.5, 41)
    rows = []
    correlator_rows = []
    for parameters in cgi_gpm_gluon_sivers_scenarios():
        multiplet = Spin1GluonTOddMultipletInput(
            build_cgi_gpm_gluon_sivers_input(
                lambda momentum, scale: pdf.proton(21, momentum, scale),
                parameters,
            )
        )
        for color in GluonColorStructure:
            for link in (GaugeLink("+", "+"), GaugeLink("-", "-")):
                for k in k_axis:
                    kx = float(k * np.cos(azimuth))
                    ky = float(k * np.sin(azimuth))
                    common = {
                        "sector": "gluon",
                        "species": "g",
                        "flavor": 21,
                        "flavor_label": "g",
                        "scenario": parameters.label,
                        "color_structure": color.value,
                        "gauge_link": (
                            f"[{link.incoming},{link.outgoing}]"
                        ),
                        "x_N": x,
                        "Q_GeV": q,
                        "k_GeV": float(k),
                        "azimuth_rad": azimuth,
                        "mechanism": "gauge_link_todd",
                        "evidence_class": "model_dependent",
                        "uncertainty_axis": (
                            "CGI_GPM_normalization_x_independent_multiplet_ratios"
                        ),
                        "combine_policy": (
                            "alternative_color_and_ratio_scenario_requires_hard_weights"
                        ),
                    }
                    correlator = multiplet.correlator(
                        color,
                        x=x, k_x_gev=kx, k_y_gev=ky, q_gev=q,
                        gauge_link=link,
                    )
                    correlator_rows.extend(
                        gluon_correlator_rows(correlator.values, common)
                    )
                    for tmd in GLUON_TODD_RANKS:
                        rows.append(
                            {
                                **common,
                                "tmd": tmd,
                                "target_channel": {
                                    "h1Lperp": "L",
                                    "f1Tperp": "T",
                                    "h1": "T",
                                    "h1Tperp": "T",
                                    "g1LT": "LT",
                                    "g1TT": "TT",
                                }[tmd],
                                "rank": GLUON_TODD_RANKS[tmd],
                                "t_odd": 1,
                                "F_GeV-2": multiplet.value(
                                    tmd, color, x=x, k_gev=float(k), q_gev=q,
                                    gauge_link=link,
                                ),
                                "source": (
                                    f"{multiplet.sivers.source}; independent "
                                    "rank-scaled spin-1 multiplet ratios"
                                ),
                            }
                        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)
    pd.DataFrame(correlator_rows).to_csv(CORRELATORS, index=False)
    print(f"Wrote {len(rows)} TMD rows and {len(correlator_rows)} correlator entries")


if __name__ == "__main__":
    main()
