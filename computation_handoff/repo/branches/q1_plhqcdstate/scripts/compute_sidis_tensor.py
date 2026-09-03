#!/usr/bin/env python3
"""Compute a minimal rank-zero tensor SIDIS W-term ratio."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.fourier import bessel_b_to_k
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.sidis import rank_zero_sidis_structure, tensor_sidis_ratio
from deuteron_wigner.tmd import (
    build_transverse_smearing_spherical,
    rank_zero_tmd_bspace,
)
from deuteron_wigner.tmd_models import GaussianRankZeroTMD
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
    parser.add_argument("--x-d", type=float, default=0.064)
    parser.add_argument("--q", type=float, default=2.0)
    parser.add_argument("--z-h", type=float, default=0.5)
    parser.add_argument("--nucleon-width-gev2", type=float, default=0.25)
    parser.add_argument("--fragmentation-width-gev2", type=float, default=0.20)
    parser.add_argument("--k-max", type=float, default=15.0)
    parser.add_argument("--n-k", type=int, default=36)
    parser.add_argument("--n-cos", type=int, default=24)
    parser.add_argument("--n-phi", type=int, default=16)
    parser.add_argument("--b-max-fm", type=float, default=5.0)
    parser.add_argument("--n-b", type=int, default=101)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tmd-output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.k_max)
    radial = selection.radial
    smearing = build_transverse_smearing_spherical(
        radial=radial,
        nucleon_mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
        k_max=args.k_max,
        n_k=args.n_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
    )
    provider = LHAPDFProvider(args.pdf, args.member)
    width_fm2 = args.nucleon_width_gev2 / HBARC_GEV_FM**2
    proton = GaussianRankZeroTMD(provider.proton, width_fm2)
    neutron = GaussianRankZeroTMD(provider.neutron, width_fm2)
    b = np.linspace(0.0, args.b_max_fm, args.n_b)
    tmd_u = {}
    tmd_ll = {}
    for flavor in QUARK_CHARGES:
        tmd_u[flavor] = np.asarray(
            [
                rank_zero_tmd_bspace(
                    x=args.x_d,
                    scale=args.q,
                    flavor=flavor,
                    b_x=float(coordinate),
                    b_y=0.0,
                    proton_tmd=proton.b_space,
                    neutron_tmd=neutron.b_space,
                    smearing=smearing,
                ).real
                for coordinate in b
            ]
        )
        tmd_ll[flavor] = np.asarray(
            [
                rank_zero_tmd_bspace(
                    x=args.x_d,
                    scale=args.q,
                    flavor=flavor,
                    b_x=float(coordinate),
                    b_y=0.0,
                    proton_tmd=proton.b_space,
                    neutron_tmd=neutron.b_space,
                    smearing=smearing,
                    tensor=True,
                ).real
                for coordinate in b
            ]
        )
    k_gev = np.linspace(0.0, 3.0, 401)
    k_fm = k_gev / HBARC_GEV_FM
    charge_weighted_u_b = sum(
        QUARK_CHARGES[flavor] ** 2 * tmd_u[flavor] for flavor in QUARK_CHARGES
    )
    charge_weighted_ll_b = sum(
        QUARK_CHARGES[flavor] ** 2 * tmd_ll[flavor] for flavor in QUARK_CHARGES
    )
    charge_weighted_u_k = bessel_b_to_k(b, charge_weighted_u_b, k_fm).real
    charge_weighted_ll_k = bessel_b_to_k(b, charge_weighted_ll_b, k_fm).real
    recovered_u = 2.0 * np.pi * np.trapz(
        k_fm * charge_weighted_u_k, x=k_fm
    )
    recovered_ll = 2.0 * np.pi * np.trapz(
        k_fm * charge_weighted_ll_k, x=k_fm
    )
    fragmentation_width = args.fragmentation_width_gev2 / HBARC_GEV_FM**2
    fragmentation = lambda flavor, coordinate: np.exp(
        -fragmentation_width * coordinate**2 / (4.0 * args.z_h**2)
    )
    p_h_t_gev = np.linspace(0.0, 1.0, 21)
    rows = []
    for p_gev in p_h_t_gev:
        u = rank_zero_sidis_structure(
            b=b,
            p_h_t=float(p_gev / HBARC_GEV_FM),
            z_h=args.z_h,
            flavors=tuple(QUARK_CHARGES),
            charges=QUARK_CHARGES,
            deuteron_tmd=lambda flavor, coordinate: np.interp(
                coordinate, b, tmd_u[flavor]
            ),
            fragmentation_tmd=fragmentation,
        )
        ll = rank_zero_sidis_structure(
            b=b,
            p_h_t=float(p_gev / HBARC_GEV_FM),
            z_h=args.z_h,
            flavors=tuple(QUARK_CHARGES),
            charges=QUARK_CHARGES,
            deuteron_tmd=lambda flavor, coordinate: np.interp(
                coordinate, b, tmd_ll[flavor]
            ),
            fragmentation_tmd=fragmentation,
        )
        rows.append(
            {
                "P_hT_GeV": float(p_gev),
                "W_U": u,
                "W_deltaT": ll,
                "deltaT_over_U": tensor_sidis_ratio(
                    unpolarized=u, tensor_difference=ll
                ),
            }
        )
    print(
        f"# wave_function={args.wave_function} x_D={args.x_d} Q={args.q} "
        f"z_h={args.z_h} pdf={args.pdf}/{args.member}"
    )
    print(f"# smearing_norm={smearing.norm():.12f}")
    print(f"# tensor_sum={smearing.norm(tensor=True):.12e}")
    print(
        f"# kT_collinear_U direct={charge_weighted_u_b[0]:.12g} "
        f"recovered={recovered_u:.12g} "
        f"relative_error={(recovered_u / charge_weighted_u_b[0] - 1.0):.3e}"
    )
    print(
        f"# kT_collinear_deltaT direct={charge_weighted_ll_b[0]:.12g} "
        f"recovered={recovered_ll:.12g} "
        f"relative_error={(recovered_ll / charge_weighted_ll_b[0] - 1.0):.3e}"
    )
    print("# P_hT_GeV W_U W_deltaT deltaT_over_U")
    for row in rows:
        print(
            f"{row['P_hT_GeV']:.6g} {row['W_U']:.8g} "
            f"{row['W_deltaT']:.8g} {row['deltaT_over_U']:.8g}"
        )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    if args.tmd_output is not None:
        args.tmd_output.parent.mkdir(parents=True, exist_ok=True)
        with args.tmd_output.open("w", newline="") as stream:
            fieldnames = ("kT_GeV", "F_U", "F_deltaT")
            writer = csv.DictWriter(stream, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(
                {
                    "kT_GeV": float(momentum),
                    "F_U": float(unpolarized),
                    "F_deltaT": float(tensor),
                }
                for momentum, unpolarized, tensor in zip(
                    k_gev, charge_weighted_u_k, charge_weighted_ll_k
                )
            )


if __name__ == "__main__":
    main()
