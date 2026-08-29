#!/usr/bin/env python3
"""Validate production quark b=0 parent limits and tensor conventions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable, build_lf_smearing_spherical, impulse_convolution,
)
from deuteron_wigner.conventions import delta_t_to_f1ll
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_collinear_correlator,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES, select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--flavor", type=int, default=2)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=16)
    parser.add_argument("--n-cos", type=int, default=12)
    parser.add_argument("--n-phi", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    wave = select_momentum_wave_function(args.wave_function)
    mass_fm = M_N_GEV / HBARC_GEV_FM
    common = dict(
        radial=wave.radial, nucleon_mass=mass_fm,
        k_max=args.internal_k_max_fm, n_k=args.n_internal_k,
        n_cos_theta=args.n_cos, n_phi=args.n_phi,
    )
    quadrature = build_off_forward_spin_quadrature(
        **common, delta_x=0.0, delta_y=0.0
    )
    smearing = build_lf_smearing_spherical(**common)
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        unpolarized, polarized, transversity_input=transversity
    )
    parent = convolve_spin1_quark_collinear_correlator(
        x=args.x_n / 2.0, scale=args.scale, flavor=args.flavor,
        proton=proton, neutron=neutron, quadrature=quadrature,
    )
    projected = project_parent_derived_quark_tmds(
        parent, k_x_gev=0.0, k_y_gev=0.0, deuteron_mass_gev=M_D_GEV
    )["total"]
    parent_f1 = 0.25 * projected["f1"]
    parent_f1ll = 0.25 * projected["f1LL"]
    independent_args = dict(
        x=args.x_n, scale=args.scale, flavor=args.flavor,
        proton_pdf=unpolarized.proton, neutron_pdf=unpolarized.neutron,
        smearing=smearing, scaling_variable=ScalingVariable.NUCLEON,
        per_nucleon=True,
    )
    independent_f1 = impulse_convolution(**independent_args)
    independent_f1ll = float(delta_t_to_f1ll(
        impulse_convolution(**independent_args, tensor=True)
    ))
    residuals = {
        "f1_relative": (parent_f1 - independent_f1) / independent_f1,
        "f1LL_relative": (
            (parent_f1ll - independent_f1ll) / independent_f1ll
            if independent_f1ll != 0.0 else 0.0
        ),
        "h1LT_absolute": 0.25 * projected["h1LT"],
    }
    passed = (
        abs(residuals["f1_relative"]) < 1.0e-10
        and abs(residuals["f1LL_relative"]) < 1.0e-9
        and abs(residuals["h1LT_absolute"]) < 1.0e-11
    )
    report = {
        "status": "pass" if passed else "fail",
        "wave_function": args.wave_function, "flavor": args.flavor,
        "x_N": args.x_n, "Q_GeV": args.scale,
        "parent_b0": {
            name: 0.25 * projected[name]
            for name in ("f1", "g1", "h1", "f1LL", "h1LT")
        },
        "independent_smearing": {
            "f1": independent_f1, "f1LL": independent_f1ll
        },
        "residuals": residuals,
        "normalization": "x_D-to-x_N Jacobian and per-nucleon factor: 1/4",
        "h1LT_constraint": "rank-zero but zero unweighted collinear PDF",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
