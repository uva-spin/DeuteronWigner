#!/usr/bin/env python3
"""Export our nucleon-LF gauge-link model through the AV18 convolution."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import gluon_correlator_rows
from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)
from deuteron_wigner.gluon_lfwf_todd import (
    GluonWilsonLineKernel,
    LFWFGaugeLinkSpinHalfGluonGTMD,
    Spin1NuclearWilsonLine,
)
from deuteron_wigner.gluon_todd import GluonColorStructure
from deuteron_wigner.gluon_nuclear_mechanisms import (
    apply_gluon_nuclear_mechanisms,
    build_inclusive_gluon_antishadowing_input,
    build_polarized_tensor_gluon_shadowing_input,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_gluon_gtmd_wave_components,
    project_deuteron_gluon_target_channel,
)
from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.gluon_correlator import project_to_allowed_spin1_gluon_basis
from deuteron_wigner.nucleon_gluon_inputs import (
    EvolvedGluonBoundaryConfig,
    build_evolved_gluon_boundary,
)
from deuteron_wigner.nuclear_mechanisms import (
    build_momentum_sum_antishadowing_input,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
)
from deuteron_wigner.pion_tmd import (
    SpinResolvedTransversePionGluonBoundary,
    Vpion19IntrinsicProfile,
)
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC = 0.1973269804
M_N = 0.93891897
M_D = 1.87561294257
OUTPUT = Path("outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.csv")
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")
METADATA = OUTPUT.with_suffix(".metadata.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--n-k-points", type=int, default=31)
    parser.add_argument("--k-max-gev", type=float, default=1.0)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0.0 < args.x_n < 1.0 or args.scale <= 0 or args.n_k_points < 3:
        raise ValueError("invalid external gluon scan")
    x_n, scale, azimuth = args.x_n, args.scale, 0.37
    output = args.output
    correlators_path = output.with_name(f"{output.stem}.correlators.csv")
    metadata_path = output.with_suffix(".metadata.json")
    wave = select_momentum_wave_function("av18")
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N/HBARC,
        k_max=10.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=12,
        n_cos_theta=10,
        n_phi=8,
        deuteron_mass=M_D/HBARC,
    )
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    boundary = build_evolved_gluon_boundary(
        unpolarized,
        polarized,
        config=EvolvedGluonBoundaryConfig(
            scale_GeV=scale, x_min=x_n/2.0,
            k_max_GeV=5.0, k_points=121,
        ),
        momentum_unit_to_GeV=HBARC,
        nucleon_mass_GeV=M_N,
    )
    dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")
    body_form_factor_path = "outputs/stage0/body_form_factor_av18.csv"
    body_form_factor = TabulatedBodyFormFactor.load(body_form_factor_path)
    diffractive = build_h1_deuteron_shadowing_input(
        inclusive_density=lambda x, q: (
            unpolarized.proton(21, x, q) + unpolarized.neutron(21, x, q)
        ),
        body_form_factor=body_form_factor,
        dpdf=dpdf,
    )
    antishadowing = build_momentum_sum_antishadowing_input(
        lambda x, q: x * (
            unpolarized.proton(21, x, q) + unpolarized.neutron(21, x, q)
        ),
        scale_gev=scale,
        parton_sector="gluon",
        diffractive_input=diffractive,
    )
    nuclear_inputs = {
        "coherent_shadowing": build_polarized_tensor_gluon_shadowing_input(
            diffractive_input=diffractive
        ),
        "antishadowing": build_inclusive_gluon_antishadowing_input(
            antishadowing
        ),
    }
    kernel = GluonWilsonLineKernel(
        alpha_s=0.30, screening_mass_gev=0.36,
        remnant_scale_gev=0.90, n_q=48, n_phi=64,
    )
    rows, matrix_rows = [], []
    k_axis = np.linspace(0.05, args.k_max_gev, args.n_k_points)
    pion_splitting = FockNormalizedMillerPionDistribution(
        MillerTensorPionDistribution()
    )
    pion_boundary = SpinResolvedTransversePionGluonBoundary(
        pion_splitting,
        JAM21IsoscalarPionPDF(0),
        Vpion19IntrinsicProfile(0),
    )
    pion_correlators = pion_boundary.correlators_k(
        x_n, k_axis, scale, b_max_gev_inv=12.0, b_nodes=64
    )
    pion_momentum = pion_splitting.ledger.pinn_sector_pion_momentum
    for color in GluonColorStructure:
        links = (
            (GaugeLink("+", "+"), GaugeLink("-", "-"))
            if color == GluonColorStructure.F_TYPE
            else (GaugeLink("+", "-"), GaugeLink("-", "+"))
        )
        for link in links:
            nucleon = LFWFGaugeLinkSpinHalfGluonGTMD(
                t_even_gtmd=boundary.model,
                color=color,
                gauge_link=link,
                nucleon_mass_gev=M_N,
                transverse_width_gev2=0.30,
                momentum_unit_to_gev=HBARC,
                kernel=kernel,
            )
            nuclear_phase = Spin1NuclearWilsonLine(
                color=color, gauge_link=link,
                d_state_probability=0.05759854074095002,
                sd_coherence=0.3897991321351392,
                kernel=kernel, transverse_width_gev2=0.30,
            )
            for index, k in enumerate(k_axis):
                kx, ky = k*np.cos(azimuth), k*np.sin(azimuth)
                wave_parts = convolve_gluon_gtmd_wave_components(
                    x=x_n/2.0, k_x=kx/HBARC, k_y=ky/HBARC, scale=scale,
                    proton_gtmd=nucleon, neutron_gtmd=nucleon,
                    quadratures=quadratures,
                )
                components = {
                    "proton_impulse": sum(x["proton"] for x in wave_parts.values()),
                    "neutron_impulse": sum(x["neutron"] for x in wave_parts.values()),
                }
                components["impulse_total"] = (
                    components["proton_impulse"] + components["neutron_impulse"]
                )
                components.update({
                    f"wave_{label}": values["proton"] + values["neutron"]
                    for label, values in wave_parts.items()
                })
                components = {
                    name: nuclear_phase.apply(values, (kx, ky))
                    for name, values in components.items()
                }
                resolved = apply_gluon_nuclear_mechanisms(
                    proton_impulse=components["proton_impulse"],
                    neutron_impulse=components["neutron_impulse"],
                    x=x_n,
                    scale_gev=scale,
                    inputs=nuclear_inputs,
                )
                components.update(resolved.corrections)
                pion = nuclear_phase.apply(
                    pion_correlators[index], (kx, ky)
                )
                components["meson_exchange"] = (
                    pion - pion_momentum * resolved.impulse
                )
                components["model_total"] = (
                    resolved.total + components["meson_exchange"]
                )
                for mechanism, correlator in components.items():
                    allowed, projected, symmetry_residual = (
                        project_to_allowed_spin1_gluon_basis(
                            correlator, (kx/HBARC, ky/HBARC), M_D/HBARC
                        )
                    )
                    if (
                        mechanism == "impulse_total"
                        and symmetry_residual > 1.0e-2
                    ):
                        raise ValueError(
                            f"forbidden-symmetry residual {symmetry_residual:g} "
                            f"for {color.value} {link} k={k:g} {mechanism}"
                        )
                    common = {
                        "wave_function": "av18", "sector": "gluon",
                        "species": "g", "flavor": 21,
                        "mechanism": mechanism,
                        "color_structure": color.value,
                        "gauge_link": f"[{link.incoming},{link.outgoing}]",
                        "x_N": x_n, "x_D": x_n/2.0, "Q_GeV": scale,
                        "k_GeV": float(k), "azimuth_rad": azimuth,
                        "amplitude_identity": (
                            "nucleon_lfwf_wilson_line_then_av18_"
                            "spin1_nuclear_wilson_line"
                        ),
                        "evidence_class": "model_lfwf_eikonal",
                        "uncertainty_axis": "kernel_and_nucleon_parent",
                        "combine_policy": "canonical_single_color_basis_requires_process_weight",
                        "symmetry_projection_residual": symmetry_residual,
                    }
                    # Retain every mechanism as a complete parent block.
                    # WP12 composition must be able to replace legacy
                    # shadowing/off-shell responses without inferring them
                    # from a difference of already-combined totals.
                    matrix_rows.extend(
                        gluon_correlator_rows(0.25*allowed.values, common)
                    )
                    f1 = 0.25*projected["f1"]
                    for name, raw in projected.items():
                        rank = {
                            "f1": 0, "g1": 0, "h1perp": 2,
                            "h1Lperp": 2, "f1Tperp": 1, "g1T": 1,
                            "h1": 1, "h1Tperp": 3, "f1LL": 0,
                            "h1LLperp": 2, "f1LT": 1, "g1LT": 1,
                            "h1LT": 1, "h1LTperp": 3,
                            "f1TT_minus_h1TTperp": 2, "g1TT": 2,
                            "h1TT": 0, "h1TTperpperp": 4,
                        }[name]
                        value = 0.25*float(raw)
                        rows.append({
                            **common, "tmd": name, "rank": rank,
                            "t_odd": int(name in {
                                "h1Lperp", "f1Tperp", "h1", "h1Tperp",
                                "g1LT", "g1TT",
                            }),
                            "F_GeV-2": value,
                            "physical_ratio_to_f1": (
                                (k/M_D)**rank*value/f1 if f1 else 0.0
                            ),
                        })
                if index % 15 == 0:
                    print(color.value, link, index+1, "/", len(k_axis), flush=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output, index=False)
    pd.DataFrame(matrix_rows).to_csv(correlators_path, index=False)
    metadata_path.write_text(json.dumps({
        "status": "own nucleon LF Wilson-line parent convolved with AV18",
        "canonical_stage": "WP11-C3 nucleon-to-nucleus parent complete",
        "external_spectator_role": "benchmark only",
        "boundary": boundary.metadata,
        "kernel": kernel.__dict__,
        "nuclear_phase": {
            "d_state_probability": 0.05759854074095002,
            "sd_coherence": 0.3897991321351392,
            "generators": "rank-one LT and rank-two TT spin-one irreps",
        },
        "nuclear_mechanisms": {
            "coherent_shadowing": nuclear_inputs["coherent_shadowing"].source,
            "antishadowing": nuclear_inputs["antishadowing"].source,
            "off_shell": "zero central: no gluon-specific off-shell extraction",
            "meson_exchange": (
                "active Fock-normalized Miller/JAM21/Vpion19 spin-resolved "
                "pion-gluon correlator plus minimal NNpi momentum counterterm"
            ),
            "pion_plus_momentum": pion_momentum,
            "non_nucleonic": "zero central; cluster model remains excluded sensitivity",
            "body_form_factor": body_form_factor_path,
            "antishadowing_momentum_audit": {
                "lost": antishadowing.lost_momentum,
                "restored": antishadowing.restored_momentum,
                "fraction": antishadowing.compensation_fraction,
            },
        },
        "quadrature": {"n_k": 12, "n_cos": 10, "n_phi": 8},
        "normalization": "same x_D=x_N/2 and 1/4 Jacobian as T-even parent",
        "limitations": [
            "color basis remains universal until observable hard weights",
            "no off-forward staple-link transfer kernel",
            "pre-W+Y nodes outside the positive W-term density domain use a complete joint-density spectral projection, never coefficient clipping",
        ],
        "output": str(output),
        "correlator_output": str(correlators_path),
    }, indent=2) + "\n")
    print(
        f"Wrote {len(rows)} TMD rows and {len(matrix_rows)} matrix rows "
        f"to {output}"
    )


if __name__ == "__main__":
    main()
