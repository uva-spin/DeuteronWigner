#!/usr/bin/env python3
"""Propagate central MSHT20 QED neutron CSB through all six LF parents."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from deuteron_wigner.csb_inputs import MSHT20QEDChargeSymmetryBreaking
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
OUTPUT = Path("outputs/parent_tmds/msht20qed_csb_parent.csv")
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
    csb_input = MSHT20QEDChargeSymmetryBreaking().as_input()
    evolved_proton = EvolvedQuarkGridModel(proton, GRID, "proton")
    exact_neutron = EvolvedQuarkGridModel(neutron, GRID, "neutron")
    broken_neutron = EvolvedQuarkGridModel(
        neutron, GRID, "neutron", charge_symmetry_breaking=csb_input
    )
    rows = []
    proton_delta_max = 0.0
    closure_max = 0.0
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
        for flavor in (2, 1, -2, -1):
            for k_gev in K_VALUES:
                common = dict(
                    x=0.05,
                    k_x=k_gev / HBARC_GEV_FM,
                    k_y=0.0,
                    scale=5.0,
                    flavor=flavor,
                    proton=evolved_proton,
                    gauge_link=GaugeLink("+", "+"),
                    quadrature=quadrature,
                    momentum_unit_to_gev=HBARC_GEV_FM,
                )
                exact = project_parent_derived_quark_tmds(
                    convolve_spin1_quark_correlator(
                        **common, neutron=exact_neutron
                    ),
                    k_x_gev=k_gev,
                    k_y_gev=0.0,
                    deuteron_mass_gev=M_D_GEV,
                )
                broken = project_parent_derived_quark_tmds(
                    convolve_spin1_quark_correlator(
                        **common, neutron=broken_neutron
                    ),
                    k_x_gev=k_gev,
                    k_y_gev=0.0,
                    deuteron_mass_gev=M_D_GEV,
                )
                for name in SPIN1_QUARK_TMD_NAMES:
                    deltas = {
                        part: broken[part][name] - exact[part][name]
                        for part in ("proton", "neutron", "total")
                    }
                    proton_delta_max = max(proton_delta_max, abs(deltas["proton"]))
                    closure_max = max(
                        closure_max, abs(deltas["total"] - deltas["neutron"])
                    )
                    for part in ("proton", "neutron", "total"):
                        rows.append(
                            {
                                "wave_function": wave_name,
                                "flavor": flavor,
                                "x_D": 0.05,
                                "x_N_reference": 0.1,
                                "Q_GeV": 5.0,
                                "k_T_GeV": k_gev,
                                "part": part,
                                "tmd": name,
                                "exact_isospin_GeV-2": exact[part][name],
                                "msht20qed_csb_GeV-2": broken[part][name],
                                "csb_delta_GeV-2": deltas[part],
                            }
                        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    tolerance = 2.0e-11
    passed = proton_delta_max < tolerance and closure_max < tolerance
    report = {
        "status": "pass" if passed else "fail",
        "rows": len(rows),
        "scope": {
            "wave_functions": list(WAVE_FUNCTION_CHOICES),
            "flavors": [2, 1, -2, -1],
            "tmd_count": len(SPIN1_QUARK_TMD_NAMES),
            "k_T_GeV": list(K_VALUES),
            "x_D": 0.05,
            "Q_GeV": 5.0,
        },
        "maximum_proton_mechanism_leakage_GeV-2": proton_delta_max,
        "maximum_total_minus_neutron_delta_GeV-2": closure_max,
        "acceptance_GeV-2": tolerance,
        "uncertainty_status": (
            "central propagated; paired 38-eigenvector parent propagation pending"
        ),
        "table": str(OUTPUT),
    }
    VALIDATION.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
