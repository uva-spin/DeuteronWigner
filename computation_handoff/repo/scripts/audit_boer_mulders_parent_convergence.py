#!/usr/bin/env python3
"""Audit the new Boer--Mulders LF parent at medium and fine quadrature."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from deuteron_wigner.boer_mulders import BoerMuldersFromSiversModel
from deuteron_wigner.bpv20_sivers import BPV20ArtemideSivers
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import convolve_spin1_quark_wave_components
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import project_spin1_quark_correlator
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
OUTPUT = Path("outputs/validation/boer_mulders_parent_convergence.json")


def main() -> None:
    wave = select_momentum_wave_function("av18")
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    sivers = BPV20ArtemideSivers().fitted_input()
    proton, neutron = build_nucleon_quark_models(
        unpolarized,
        polarized,
        transversity_input=JAMDiFFTransversityGrid(
            "data/processed/jamdiff_wlqcd_transversity.csv"
        ),
        sivers_input=sivers,
        boer_mulders_input=BoerMuldersFromSiversModel(sivers).fitted_input(),
    )
    grids = {
        "medium": (16, 12, 8),
        "fine": (24, 16, 12),
    }
    k_axis = np.asarray([0.15, 0.4, 0.7, 1.0])
    values = {}
    for label, (n_k, n_cos, n_phi) in grids.items():
        quadratures = build_off_forward_component_quadratures(
            radial=wave.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=10.0,
            delta_x=0.0,
            delta_y=0.0,
            n_k=n_k,
            n_cos_theta=n_cos,
            n_phi=n_phi,
            deuteron_mass=M_D_GEV / HBARC_GEV_FM,
        )
        curve = []
        for k in k_axis:
            kx = float(k * np.cos(0.37))
            ky = float(k * np.sin(0.37))
            pieces = convolve_spin1_quark_wave_components(
                x=0.05,
                k_x=kx / HBARC_GEV_FM,
                k_y=ky / HBARC_GEV_FM,
                scale=5.0,
                flavor=2,
                proton=proton,
                neutron=neutron,
                gauge_link=GaugeLink("+", "+"),
                quadratures=quadratures,
                momentum_unit_to_gev=HBARC_GEV_FM,
            )
            parent = 0.25 * sum(
                (item.total.transverse for item in pieces.values()),
                np.zeros((2, 3, 3), dtype=np.complex128),
            )
            # Only the transverse Dirac projection carries h1perp.
            from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
            correlator = Spin1QuarkCorrelator(
                np.zeros((3, 3), dtype=np.complex128),
                np.zeros((3, 3), dtype=np.complex128),
                parent,
            )
            projected = project_spin1_quark_correlator(
                correlator, (kx, ky), M_D_GEV
            )
            curve.append(float(projected["h1perp"]))
        values[label] = np.asarray(curve)
    difference = np.abs(values["fine"] - values["medium"])
    scale = max(float(np.max(np.abs(values["fine"]))), 1.0e-12)
    relative_to_peak = float(np.max(difference) / scale)
    report = {
        "tmd": "h1perp",
        "flavor": "u",
        "wave_function": "av18",
        "x_N": 0.1,
        "Q_GeV": 5.0,
        "k_GeV": k_axis.tolist(),
        "medium": values["medium"].tolist(),
        "fine": values["fine"].tolist(),
        "max_absolute_difference_GeV-2": float(np.max(difference)),
        "max_relative_to_fine_curve_peak": relative_to_peak,
        "tolerance": 0.01,
        "passes": relative_to_peak <= 0.01,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    if not report["passes"]:
        raise SystemExit(
            f"Boer--Mulders medium/fine convergence failed: {relative_to_peak:.3%}"
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
