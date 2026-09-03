#!/usr/bin/env python3
"""Compute the provisional nucleonic impulse-approximation b1 baseline."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    b1_leading_order,
)
from deuteron_wigner.data import load_hermes_b1
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897
QUARK_CHARGES = {1: -1.0 / 3.0, 2: 2.0 / 3.0, 3: -1.0 / 3.0}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, default="cd-bonn")
    parser.add_argument("--pdf", default="CT18NNLO")
    parser.add_argument("--member", type=int, default=0)
    parser.add_argument("--k-max", type=float, default=15.0)
    parser.add_argument("--n-k", type=int, default=48)
    parser.add_argument("--n-cos", type=int, default=32)
    parser.add_argument("--n-phi", type=int, default=20)
    parser.add_argument(
        "--x-convention",
        choices=("deuteron", "nucleon"),
        default="nucleon",
        help="HERMES tabulates nucleon-mass x; use deuteron only for x_D inputs.",
    )
    parser.add_argument("--output", type=Path, help="optional CSV output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.k_max)
    radial = selection.radial
    smearing = build_lf_smearing_spherical(
        radial=radial,
        nucleon_mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
        k_max=args.k_max,
        n_k=args.n_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
    )
    provider = LHAPDFProvider(args.pdf, args.member)
    data = load_hermes_b1("data/processed/hermes_b1/table_ii.csv")
    print(f"# wave_function={args.wave_function} pdf={args.pdf}/{args.member}")
    print(f"# smearing_norm={smearing.unpolarized_norm():.12f}")
    print(f"# tensor_sum={smearing.tensor_norm():.12e}")
    print(f"# lhapdf_Q_range_GeV=[{provider.q_min:.6g},{provider.q_max:.6g}]")
    rows = []
    for x_table, q2, observed, stat, sys in zip(
        data.x, data.q2_gev2, data.b1, data.b1_stat, data.b1_sys
    ):
        convention = (
            ScalingVariable.DEUTERON
            if args.x_convention == "deuteron"
            else ScalingVariable.NUCLEON
        )
        prediction = b1_leading_order(
            x=float(x_table),
            scale=float(q2**0.5),
            flavors=(1, 2, 3),
            charges=QUARK_CHARGES,
            proton_pdf=provider.proton,
            neutron_pdf=provider.neutron,
            smearing=smearing,
            scaling_variable=convention,
            per_nucleon=(convention == ScalingVariable.NUCLEON),
        )
        rows.append(
            {
                "x_table": float(x_table),
                "Q2_GeV2": float(q2),
                "b1_IA": prediction,
                "b1_data": float(observed),
                "stat": float(stat),
                "sys": float(sys),
                "below_pdf_Qmin": int(q2**0.5 < provider.q_min),
            }
        )
    print("# x_table Q2 b1_IA b1_data stat sys below_pdf_Qmin")
    for row in rows:
        print(
            f"{row['x_table']:.6g} {row['Q2_GeV2']:.6g} {row['b1_IA']:.8g} "
            f"{row['b1_data']:.8g} {row['stat']:.8g} {row['sys']:.8g} "
            f"{row['below_pdf_Qmin']}"
        )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
