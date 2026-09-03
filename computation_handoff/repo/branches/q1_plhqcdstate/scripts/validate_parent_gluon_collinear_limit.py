#!/usr/bin/env python3
"""Validate the b=0 parent gluon limit against independent LF smearing."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    impulse_convolution,
)
from deuteron_wigner.conventions import delta_t_to_f1ll
from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    project_deuteron_gluon_target_channel,
    spin_half_collinear_gluon_correlator,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
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
    parent_quadrature = build_off_forward_spin_quadrature(
        **common, delta_x=0.0, delta_y=0.0
    )
    smearing = build_lf_smearing_spherical(**common)
    pdf = LHAPDFProvider("CT18NNLO", 0)

    def proton(x, k_x, k_y, delta_x, delta_y, scale):
        return spin_half_collinear_gluon_correlator(
            pdf.proton(21, x, scale), 0.0
        )

    def neutron(x, k_x, k_y, delta_x, delta_y, scale):
        return spin_half_collinear_gluon_correlator(
            pdf.neutron(21, x, scale), 0.0
        )

    parent = convolve_gluon_gtmd_point(
        x=args.x_n / 2.0, k_x=0.0, k_y=0.0, scale=args.scale,
        proton_gtmd=proton, neutron_gtmd=neutron,
        quadrature=parent_quadrature,
    )
    u_matrix = project_deuteron_gluon_target_channel(parent, "U")
    ll_matrix = project_deuteron_gluon_target_channel(parent, "LL")
    # Recover scalar coefficients (factor 2), convert x_D -> x_N (1/2),
    # and average over the two nucleons (1/2).
    parent_f1 = 0.25 * 2.0 * transverse_matrix_parts(u_matrix)[0].real
    parent_f1ll = -0.25 * 2.0 * transverse_matrix_parts(ll_matrix)[0].real

    convolution_arguments = dict(
        x=args.x_n, scale=args.scale, flavor=21,
        proton_pdf=pdf.proton, neutron_pdf=pdf.neutron,
        smearing=smearing, scaling_variable=ScalingVariable.NUCLEON,
        per_nucleon=True,
    )
    independent_f1 = impulse_convolution(**convolution_arguments)
    independent_f1ll = float(delta_t_to_f1ll(
        impulse_convolution(**convolution_arguments, tensor=True)
    ))
    residuals = {
        "f1_relative": (parent_f1 - independent_f1) / independent_f1,
        "f1LL_relative": (
            (parent_f1ll - independent_f1ll) / independent_f1ll
            if independent_f1ll != 0.0 else 0.0
        ),
    }
    report = {
        "status": "pass" if max(map(abs, residuals.values())) < 1.0e-10 else "fail",
        "wave_function": args.wave_function,
        "x_N": args.x_n,
        "Q_GeV": args.scale,
        "normalization": "x_D-to-x_N Jacobian and per-nucleon factor: 1/4",
        "parent_b0": {"f1": parent_f1, "f1LL": parent_f1ll},
        "independent_smearing": {
            "f1": independent_f1, "f1LL": independent_f1ll
        },
        "residuals": residuals,
        "h1TT_collinear_one_body": 0.0,
        "h1TT_null_reason": (
            "spin-half collinear gluon correlator has no symmetric-traceless "
            "gluon-index component"
        ),
        "quadrature": {
            "n_k": args.n_internal_k, "n_cos": args.n_cos,
            "n_phi": args.n_phi, "k_max_fm_inverse": args.internal_k_max_fm,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
