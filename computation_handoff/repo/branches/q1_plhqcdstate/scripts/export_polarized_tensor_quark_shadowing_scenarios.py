#!/usr/bin/env python3
"""Export AV18 polarized/tensor quark-shadowing parent scenarios at small x."""

from dataclasses import replace
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    deserialize_quark_correlator,
    quark_correlator_rows,
)
from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)
from deuteron_wigner.nuclear_mechanisms import (
    NuclearCorrectionParameters,
    apply_nuclear_corrections,
    build_polarized_tensor_shadowing_input,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.quark_correlator import (
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)

INPUT = Path(
    "outputs/parent_tmds/quark_av18_shadowing_x001_rich_medium.correlators.csv"
)
OUTPUT = Path(
    "outputs/parent_tmds/quark_polarized_tensor_shadowing_scenarios.csv"
)
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")
M_D_GEV = 1.87561294257

SCENARIOS = {
    "spin_weak": (
        {"U": 1.0, "L": 0.30, "T": 0.30, "LL": 0.70, "LT": 0.45, "TT": 0.45},
        0.30,
        0.45,
    ),
    "spin_central": (
        {"U": 1.0, "L": 0.65, "T": 0.65, "LL": 2.0, "LT": 1.5, "TT": 1.5},
        0.65,
        0.75,
    ),
    "spin_strong": (
        {"U": 1.0, "L": 1.0, "T": 1.0, "LL": 3.0, "LT": 2.2, "TT": 2.2},
        1.0,
        1.1,
    ),
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    # Above this cutoff the Gaussian parent is below numerical resolution and
    # the rank-conditioned inverse TMD projector amplifies roundoff. The
    # underlying correlator remains finite, but its separated high-rank
    # projections are not production-authoritative there.
    frame = frame.loc[frame.k_GeV.le(1.2)].copy()
    pdf = LHAPDFProvider("CT18NNLO", 0)
    dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")
    form_factor = TabulatedBodyFormFactor.load(
        "outputs/stage0/body_form_factor_av18.csv"
    )
    diffractive = {
        flavor: build_h1_deuteron_shadowing_input(
            inclusive_density=lambda x, q, f=flavor: (
                pdf.proton(f, x, q) + pdf.neutron(f, x, q)
            ),
            body_form_factor=form_factor,
            dpdf=dpdf,
        )
        for flavor in (2, 1, -2, -1)
    }
    parameters = replace(
        NuclearCorrectionParameters(), average_nucleon_virtuality=0.0
    )
    keys = [
        "wave_function", "input_scenario", "species", "flavor", "flavor_label",
        "gauge_link", "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
    ]
    rows = []
    correlator_rows = []
    for labels, group in frame.groupby(keys, sort=False):
        common = dict(zip(keys, labels))
        proton = deserialize_quark_correlator(
            group.loc[group.mechanism.eq("proton_impulse")]
        )
        neutron = deserialize_quark_correlator(
            group.loc[group.mechanism.eq("neutron_impulse")]
        )
        flavor = int(common["flavor"])
        sector = "valence" if flavor > 0 else "sea"
        k = float(common["k_GeV"])
        azimuth = float(common["azimuth_rad"])
        for scenario, (ratios, axial, transverse) in SCENARIOS.items():
            response = build_polarized_tensor_shadowing_input(
                diffractive[flavor],
                vector_ratios=ratios,
                axial_operator_ratio=axial,
                transverse_operator_ratio=transverse,
            )
            resolved = apply_nuclear_corrections(
                proton_impulse=proton,
                neutron_impulse=neutron,
                x=float(common["x_N"]),
                scale_gev=float(common["Q_GeV"]),
                parton_sector=sector,
                parameters=parameters,
                diffractive_input=diffractive[flavor],
                polarized_shadowing_input=response,
            )
            correction = resolved.corrections["coherent_shadowing"]
            labels_out = {
                **common,
                "scenario": scenario,
                "mechanism": "coherent_shadowing",
                "evidence_class": "model_dependent",
                "uncertainty_axis": "polarized_tensor_response_scenario",
                "validity": "x_N=0.01,Q=5 GeV,k_T<=1.2 GeV",
            }
            correlator_rows.extend(quark_correlator_rows(correction, labels_out))
            projected = (
                project_spin1_quark_correlator_at_origin(correction, M_D_GEV)
                if k == 0.0
                else project_spin1_quark_correlator(
                    correction,
                    (k * np.cos(azimuth), k * np.sin(azimuth)),
                    M_D_GEV,
                )
            )
            rows.extend(
                {
                    **labels_out,
                    "tmd": tmd,
                    "F_GeV-2": (
                        0.0 if abs(float(value)) < 1.0e-12 else float(value)
                    ),
                    "source": response.source,
                }
                for tmd, value in projected.items()
            )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)
    pd.DataFrame(correlator_rows).to_csv(CORRELATORS, index=False)
    print(f"Wrote {len(rows)} projections and {len(correlator_rows)} correlator entries")


if __name__ == "__main__":
    main()
