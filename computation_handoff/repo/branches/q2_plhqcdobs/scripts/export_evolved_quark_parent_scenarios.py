#!/usr/bin/env python3
"""Propagate evolved rank-aware quark grids through all six LF parents."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from deuteron_wigner.evolved_quark_grid import EvolvedQuarkGridModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_correlator,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import SPIN1_QUARK_TMD_NAMES
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
GRID = Path("data/processed/evolved_quark_tmd_Q5.npz")
OUTPUT = Path("outputs/parent_tmds/evolved_quark_parent_scenarios.csv")
VALIDATION = OUTPUT.with_suffix(".validation.json")
K_VALUES = (0.0, 0.2, 0.4, 0.7, 1.0)


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        pdf, polarized, transversity_input=transversity
    )
    models = {
        scenario: (
            EvolvedQuarkGridModel(proton, GRID, "proton", scenario),
            EvolvedQuarkGridModel(neutron, GRID, "neutron", scenario),
        )
        for scenario in ("central", "positive")
    }
    rows = []
    reconstruction_maximum = 0.0
    for wave_name in WAVE_FUNCTION_CHOICES:
        wave = select_momentum_wave_function(wave_name)
        quadrature = build_off_forward_spin_quadrature(
            radial=wave.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=10.0,
            n_k=24,
            n_cos_theta=16,
            n_phi=12,
            delta_x=0.0,
            delta_y=0.0,
        )
        for scenario in ("central", "positive"):
            evolved_proton, evolved_neutron = models[scenario]
            for flavor in (2, 1, -2, -1):
                for k_gev in K_VALUES:
                    result = convolve_spin1_quark_correlator(
                        x=0.05,
                        k_x=k_gev / HBARC_GEV_FM,
                        k_y=0.0,
                        scale=5.0,
                        flavor=flavor,
                        proton=evolved_proton,
                        neutron=evolved_neutron,
                        gauge_link=GaugeLink("+", "+"),
                        quadrature=quadrature,
                        momentum_unit_to_gev=HBARC_GEV_FM,
                    )
                    projected = project_parent_derived_quark_tmds(
                        result, k_x_gev=k_gev, k_y_gev=0.0,
                        deuteron_mass_gev=M_D_GEV,
                    )
                    for name in SPIN1_QUARK_TMD_NAMES:
                        reconstruction_maximum = max(
                            reconstruction_maximum,
                            abs(
                                projected["total"][name]
                                - projected["proton"][name]
                                - projected["neutron"][name]
                            ),
                        )
                        for part in ("proton", "neutron", "total"):
                            rows.append({
                                "wave_function": wave_name,
                                "scenario": scenario,
                                "flavor": flavor,
                                "x_D": 0.05,
                                "x_N_reference": 0.1,
                                "Q_GeV": 5.0,
                                "k_T_GeV": k_gev,
                                "part": part,
                                "tmd": name,
                                "value_GeV-2": projected[part][name],
                            })

    # Linearity gives the negative member exactly without another convolution:
    # F(-a)=2F(0)-F(+a).
    index = {
        (
            row["wave_function"], row["flavor"], row["k_T_GeV"],
            row["part"], row["tmd"],
        ): row
        for row in rows if row["scenario"] == "central"
    }
    positive = [row for row in rows if row["scenario"] == "positive"]
    negative_rows = []
    for row in positive:
        key = (
            row["wave_function"], row["flavor"], row["k_T_GeV"],
            row["part"], row["tmd"],
        )
        negative = dict(row)
        negative["scenario"] = "negative"
        negative["value_GeV-2"] = (
            2.0 * index[key]["value_GeV-2"] - row["value_GeV-2"]
        )
        negative_rows.append(negative)
    rows.extend(negative_rows)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    passed = reconstruction_maximum < 2e-11
    report = {
        "status": "pass" if passed else "fail",
        "rows": len(rows),
        "scope": {
            "wave_functions": list(WAVE_FUNCTION_CHOICES),
            "scenarios": ["negative", "central", "positive"],
            "flavors": [2, 1, -2, -1],
            "k_T_GeV": list(K_VALUES),
            "tmd_count": len(SPIN1_QUARK_TMD_NAMES),
            "parts": ["proton", "neutron", "total"],
        },
        "maximum_proton_neutron_reconstruction_GeV-2": reconstruction_maximum,
        "acceptance_GeV-2": 2e-11,
        "negative_scenario": "exact linear reflection 2*central-positive",
        "limitations": (
            "fixed x_D=0.05 and Q=5 GeV production slice; W-term tails above "
            "the low-k phenomenology region are retained only inside convolution"
        ),
    }
    VALIDATION.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
