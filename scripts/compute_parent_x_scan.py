#!/usr/bin/env python3
"""Check GTMD->TMD/GPD/PDF/b1 consistency over x and light flavors."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.collinear import (
    ScalingVariable,
    b1_leading_order,
    build_lf_smearing_spherical,
)
from deuteron_wigner.data import load_hermes_b1
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.gtmd_models import FactorizedGaussianGTMD
from deuteron_wigner.gtmd_sampling import (
    convolve_factorized_gaussian_gpd,
    convolve_factorized_gaussian_grid,
    deuteron_x_parent_to_nucleon_x,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.spin import HelicityMatrix
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897
CHARGES = {1: -1.0 / 3.0, 2: 2.0 / 3.0}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--pdf-set", default="CT18NNLO")
    parser.add_argument("--width-gev2", type=float, default=0.25)
    parser.add_argument("--k-grid-max-gev", type=float, default=1.6)
    parser.add_argument("--n-k-grid", type=int, default=25)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=24)
    parser.add_argument("--n-cos", type=int, default=16)
    parser.add_argument("--n-phi", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.internal_k_max_fm)
    mass_fm = AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM
    quadrature = build_off_forward_spin_quadrature(
        radial=selection.radial, nucleon_mass=mass_fm,
        k_max=args.internal_k_max_fm, delta_x=0.0, delta_y=0.0,
        n_k=args.n_internal_k, n_cos_theta=args.n_cos, n_phi=args.n_phi,
    )
    smearing = build_lf_smearing_spherical(
        radial=selection.radial, nucleon_mass=mass_fm,
        k_max=args.internal_k_max_fm, n_k=args.n_internal_k,
        n_cos_theta=args.n_cos, n_phi=args.n_phi,
    )
    provider = LHAPDFProvider(args.pdf_set)
    proton = FactorizedGaussianGTMD(
        provider.proton, args.width_gev2 / HBARC_GEV_FM**2, 0.0
    )
    neutron = FactorizedGaussianGTMD(
        provider.neutron, args.width_gev2 / HBARC_GEV_FM**2, 0.0
    )
    data = load_hermes_b1("data/processed/hermes_b1/table_ii.csv")
    k_gev = np.linspace(-args.k_grid_max_gev, args.k_grid_max_gev, args.n_k_grid)
    k_fm = k_gev / HBARC_GEV_FM
    rows = []
    for x_n, q2 in zip(data.x, data.q2_gev2):
        # The parent uses x_D. HERMES quotes nucleon-mass x_N=2*x_D.
        x_d = float(x_n / 2.0)
        scale = float(max(np.sqrt(q2), provider.q_min))
        parent_gpd = np.zeros((3, 3), dtype=np.complex128)
        parent_tmd = np.zeros(
            (args.n_k_grid, args.n_k_grid, 3, 3), dtype=np.complex128
        )
        for positive_flavor, charge in CHARGES.items():
            for flavor in (positive_flavor, -positive_flavor):
                weight = charge**2
                parent_gpd += weight * convolve_factorized_gaussian_gpd(
                    x=x_d, scale=scale, flavor=flavor, proton=proton,
                    neutron=neutron, quadrature=quadrature,
                ).values
                parent_tmd += weight * convolve_factorized_gaussian_grid(
                    x=x_d, k_x=k_fm, k_y=k_fm, scale=scale, flavor=flavor,
                    proton=proton, neutron=neutron, quadrature=quadrature,
                ).values / HBARC_GEV_FM**2
        numerical_pdf = simpson(
            simpson(parent_tmd, x=k_gev, axis=1), x=k_gev, axis=0
        )
        gpd = HelicityMatrix(parent_gpd)
        per_nucleon = deuteron_x_parent_to_nucleon_x(
            gpd, x_nucleon=float(x_n), x_deuteron=x_d
        )
        numeric = HelicityMatrix(numerical_pdf)
        b1_parent = float(per_nucleon.tensor_difference().real / 2.0)
        b1_independent = b1_leading_order(
            x=float(x_n), scale=scale, flavors=(1, 2), charges=CHARGES,
            proton_pdf=provider.proton, neutron_pdf=provider.neutron,
            smearing=smearing, scaling_variable=ScalingVariable.NUCLEON,
            per_nucleon=True,
        )
        rows.append({
            "wave_function": args.wave_function,
            "x_N": float(x_n),
            "x_D": x_d,
            "Q_input_GeV": float(np.sqrt(q2)),
            "Q_used_GeV": scale,
            "charge_weighted_pdf_U_parent": float(per_nucleon.unpolarized().real),
            "charge_weighted_deltaT_pdf_parent": float(
                per_nucleon.tensor_difference().real
            ),
            "b1_from_parent": b1_parent,
            "b1_independent": b1_independent,
            "b1_relative_difference": (
                (b1_parent - b1_independent) / b1_independent
                if b1_independent != 0.0 else np.nan
            ),
            "tmd_to_pdf_U_relative_error": float(
                (numeric.unpolarized().real - gpd.unpolarized().real)
                / gpd.unpolarized().real
            ),
            "tmd_to_pdf_deltaT_relative_error": float(
                (numeric.tensor_difference().real - gpd.tensor_difference().real)
                / gpd.tensor_difference().real
            ) if gpd.tensor_difference().real != 0.0 else np.nan,
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    maximum_b1_error = max(abs(row["b1_relative_difference"]) for row in rows)
    maximum_tmd_error = max(
        abs(row["tmd_to_pdf_U_relative_error"]) for row in rows
    )
    print(
        f"# {args.wave_function} max_b1_relative_difference={maximum_b1_error:.3e} "
        f"max_tmd_pdf_relative_error={maximum_tmd_error:.3e}"
    )


if __name__ == "__main__":
    main()
