#!/usr/bin/env python3
"""Export independent CGI-GPM f/d gluon-Sivers parents and scenarios."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gluon_todd import (
    CGIGPMGluonSiversParameters,
    GluonColorStructure,
    GluonTWeightedProcess,
    SiversAugmentedSpinHalfGluonGTMD,
    build_cgi_gpm_gluon_sivers_input,
    cgi_gpm_gluon_sivers_scenarios,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_gluon_gtmd_wave_components,
    project_deuteron_gluon_target_channel,
)
from deuteron_wigner.gluon_correlator import (
    GluonCorrelatorObservation,
    GluonTargetPolarization,
    project_polarized_gluon_correlators,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.registry import TargetChannel
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--k-min-gev", type=float, default=0.05)
    parser.add_argument("--k-max-gev", type=float, default=1.5)
    parser.add_argument("--n-k-points", type=int, default=17)
    parser.add_argument("--azimuth", type=float, default=0.37)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=16)
    parser.add_argument("--n-cos", type=int, default=12)
    parser.add_argument("--n-phi", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    wave = select_momentum_wave_function(args.wave_function)
    wave.validate_k_max(args.internal_k_max_fm)
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=args.internal_k_max_fm,
        delta_x=0.0,
        delta_y=0.0,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    pdf = LHAPDFProvider("CT18NNLO", 0)

    def gluon_pdf(x: float, q: float) -> float:
        return pdf.proton(21, x, q)

    zero = lambda *values: np.zeros((2, 2, 2, 2), dtype=np.complex128)
    rows: list[dict[str, object]] = []
    k_axis = np.linspace(args.k_min_gev, args.k_max_gev, args.n_k_points)
    for scenario in cgi_gpm_gluon_sivers_scenarios():
        for color in GluonColorStructure:
            normalization = (
                scenario.n_f
                if color == GluonColorStructure.F_TYPE
                else scenario.n_d
            )
            unit_parameters = CGIGPMGluonSiversParameters(
                n_f=1.0 if color == GluonColorStructure.F_TYPE else 0.0,
                n_d=1.0 if color == GluonColorStructure.D_TYPE else 0.0,
                rho=scenario.rho,
                unpolarized_width_gev2=scenario.unpolarized_width_gev2,
                alpha_f=scenario.alpha_f,
                beta_f=scenario.beta_f,
                alpha_d=scenario.alpha_d,
                beta_d=scenario.beta_d,
                label=f"unit_{color.value}",
            )
            boundary = build_cgi_gpm_gluon_sivers_input(
                gluon_pdf, unit_parameters
            )
            process = GluonTWeightedProcess(
                name=f"unmixed {color.value} basis projection",
                coefficients={
                    item: 1.0 if item == color else 0.0
                    for item in GluonColorStructure
                },
                source="color-basis identity map; no observable hard weighting",
                factorization_statement=(
                    "universal CGI-GPM color component retained before "
                    "observable-specific hard coefficients"
                ),
            )
            for link in (GaugeLink("+", "+"), GaugeLink("-", "-")):
                model = SiversAugmentedSpinHalfGluonGTMD(
                    t_even_gtmd=zero,
                    boundary=boundary,
                    process=process,
                    gauge_link=link,
                    nucleon_mass_gev=M_N_GEV,
                    momentum_unit_to_gev=HBARC_GEV_FM,
                )
                for k in k_axis:
                    kx = float(k * np.cos(args.azimuth))
                    ky = float(k * np.sin(args.azimuth))
                    components = convolve_gluon_gtmd_wave_components(
                        x=args.x_n / 2.0,
                        k_x=kx / HBARC_GEV_FM,
                        k_y=ky / HBARC_GEV_FM,
                        scale=args.scale,
                        proton_gtmd=model,
                        neutron_gtmd=model,
                        quadratures=quadratures,
                    )
                    parent = sum(
                        value["proton"] + value["neutron"]
                        for value in components.values()
                    )
                    momentum = (kx / HBARC_GEV_FM, ky / HBARC_GEV_FM)
                    observations = [
                        GluonCorrelatorObservation(
                            momentum=momentum,
                            polarization=GluonTargetPolarization(
                                spin_transverse=spin
                            ),
                            correlator=project_deuteron_gluon_target_channel(
                                parent, label
                            ),
                        )
                        for label, spin in (
                            ("T_x", (1.0, 0.0)),
                            ("T_y", (0.0, 1.0)),
                        )
                    ]
                    projected = project_polarized_gluon_correlators(
                        TargetChannel.T,
                        observations,
                        M_D_GEV / HBARC_GEV_FM,
                    )
                    value = 0.25 * normalization * projected["f1Tperp"]
                    rows.append({
                        "wave_function": args.wave_function,
                        "scenario": scenario.label,
                        "color_structure": color.value,
                        "normalization_Ng": normalization,
                        "species": "g",
                        "flavor": 21,
                        "tmd": "f1Tperp",
                        "target_channel": "T",
                        "rank": 1,
                        "t_odd": 1,
                        "gauge_link": str(link),
                        "x_N": args.x_n,
                        "Q_GeV": args.scale,
                        "k_GeV": float(k),
                        "F_GeV-2": float(value),
                        "parent_derived": 1,
                        "provenance": boundary.source,
                        "uncertainty_axis": "correlated_CGI_GPM_f_d_scenario",
                        "hard_weighting": "unmixed universal color basis",
                    })
    frame = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False)
    print(f"Wrote {len(frame)} rows to {args.output}")


if __name__ == "__main__":
    main()
