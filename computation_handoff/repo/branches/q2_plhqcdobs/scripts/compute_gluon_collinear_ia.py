#!/usr/bin/env python3
"""Compute the nucleonic one-body collinear deuteron-gluon baseline."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    impulse_convolution,
)
from deuteron_wigner.conventions import delta_t_to_f1ll
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897
GLUON_FLAVOR = 21


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--pdf-set", default="CT18NNLO")
    parser.add_argument("--member", type=int, default=0)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=36)
    parser.add_argument("--n-cos", type=int, default=24)
    parser.add_argument("--n-phi", type=int, default=16)
    parser.add_argument(
        "--x",
        type=float,
        nargs="+",
        default=(0.01, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50, 0.70),
        help="nucleon-mass Bjorken-x values",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.internal_k_max_fm)
    smearing = build_lf_smearing_spherical(
        radial=selection.radial,
        nucleon_mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
        k_max=args.internal_k_max_fm,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
    )
    provider = LHAPDFProvider(args.pdf_set, args.member)
    if not provider.q_min <= args.scale <= provider.q_max:
        raise ValueError(
            f"scale {args.scale:g} GeV is outside the PDF range "
            f"[{provider.q_min:g},{provider.q_max:g}]"
        )
    rows = []
    for x_n in args.x:
        common = dict(
            x=float(x_n),
            scale=args.scale,
            flavor=GLUON_FLAVOR,
            proton_pdf=provider.proton,
            neutron_pdf=provider.neutron,
            smearing=smearing,
            scaling_variable=ScalingVariable.NUCLEON,
            per_nucleon=True,
        )
        f1 = impulse_convolution(**common)
        delta_t = impulse_convolution(**common, tensor=True)
        f1ll = delta_t_to_f1ll(delta_t)
        rows.append(
            {
                "wave_function": args.wave_function,
                "pdf_set": args.pdf_set,
                "member": args.member,
                "Q_GeV": args.scale,
                "x_N": float(x_n),
                "x_D": float(x_n) / 2.0,
                "f1g_per_nucleon": f1,
                "deltaT_f1g_per_nucleon": delta_t,
                "f1LLg_per_nucleon": f1ll,
                "f1LLg_over_f1g": f1ll / f1 if f1 != 0.0 else float("nan"),
                "h1TTg_collinear_one_body": 0.0,
                "h1TTg_null_is_structural": 1,
                "smearing_norm": smearing.unpolarized_norm(),
                "tensor_sum": smearing.tensor_norm(),
            }
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(
        f"# wrote {len(rows)} rows to {args.output}; "
        f"norm={smearing.unpolarized_norm():.12f} "
        f"tensor_sum={smearing.tensor_norm():.3e}"
    )


if __name__ == "__main__":
    main()
