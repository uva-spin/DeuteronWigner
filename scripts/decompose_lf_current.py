#!/usr/bin/env python3
"""Decompose the LF angular-condition residual by wave/current component."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.form_factors import load_av18_electromagnetic_tables
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_local_current,
)
from deuteron_wigner.lf_current import (
    SpinOnePlusCurrent,
    dirac_pauli_from_sachs,
    nucleon_plus_current,
)
from deuteron_wigner.light_front import SpinRotation
from deuteron_wigner.wavefunctions.av18 import load_av18_momentum
from deuteron_wigner.wavefunctions.cd_bonn import cd_bonn_parameters

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=("av18", "cd-bonn"), default="av18")
    parser.add_argument("--k-max", type=float, default=10.0)
    parser.add_argument("--delta-gev", type=float, nargs="+", default=(0.1, 0.3, 0.5))
    parser.add_argument("--n-k", type=int, default=36)
    parser.add_argument("--n-cos", type=int, default=24)
    parser.add_argument("--n-phi", type=int, default=16)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--spin-rotation", choices=("melosh", "identity"), default="melosh")
    return parser.parse_args()


def helicity_current(matrix: np.ndarray) -> SpinOnePlusCurrent:
    return SpinOnePlusCurrent(
        plus_plus=matrix[0, 0],
        plus_zero=matrix[0, 1],
        plus_minus=matrix[0, 2],
        zero_zero=matrix[1, 1],
    )


def main() -> None:
    args = parse_args()
    if args.wave_function == "av18":
        table = load_av18_momentum("data/raw/av18/deut.wfk")
        if args.k_max > table.grid[-1]:
            raise ValueError(f"AV18 k-max cannot exceed {table.grid[-1]} fm^-1")
        radial = table.radial_callable()
    else:
        parameters = cd_bonn_parameters()
        radial = lambda k: tuple(float(value) for value in parameters.momentum(k))
    electromagnetic = load_av18_electromagnetic_tables("data/raw/av18/fdeut.av18")
    nucleon_mass_fm = AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM
    deuteron_mass_gev = electromagnetic.deuteron_mass_mev / 1000.0
    rows = []
    spin_rotation = SpinRotation(args.spin_rotation)
    for delta_gev in args.delta_gev:
        delta_fm = delta_gev / HBARC_GEV_FM
        quadratures = build_off_forward_component_quadratures(
            radial=radial,
            nucleon_mass=nucleon_mass_fm,
            k_max=args.k_max,
            delta_x=delta_fm,
            delta_y=0.0,
            n_k=args.n_k,
            n_cos_theta=args.n_cos,
            n_phi=args.n_phi,
            spin_rotation=spin_rotation,
        )
        ge = electromagnetic.isoscalar_electric(delta_fm)
        gm = electromagnetic.isoscalar_magnetic(delta_fm)
        f1, f2 = dirac_pauli_from_sachs(
            electric=ge,
            magnetic=gm,
            q2=delta_fm**2,
            mass=nucleon_mass_fm,
        )
        eta = delta_gev**2 / (4.0 * deuteron_mass_gev**2)
        term_matrices = {}
        for wave_label, quadrature in quadratures.items():
            for current_label, current_f1, current_f2 in (
                ("F1", f1, 0.0),
                ("F2", 0.0, f2),
            ):
                half_current = lambda delta_x, delta_y, scale, a=current_f1, b=current_f2: (
                    nucleon_plus_current(
                        f1=a,
                        f2=b,
                        delta_x=delta_x,
                        delta_y=delta_y,
                        mass=nucleon_mass_fm,
                    )
                )
                matrix = convolve_local_current(
                    scale=1.0,
                    proton_current=half_current,
                    neutron_current=half_current,
                    quadrature=quadrature,
                ).values
                term_matrices[(wave_label, current_label)] = matrix
        full_matrix = sum(term_matrices.values())
        full_current = helicity_current(full_matrix)
        full_residual = full_current.angular_condition(eta)
        reconstructed_residual = 0.0j
        for (wave_label, current_label), matrix in term_matrices.items():
            current = helicity_current(matrix)
            contribution = current.angular_condition(eta)
            reconstructed_residual += contribution
            rows.append(
                {
                    "wave_function": args.wave_function,
                    "spin_rotation": spin_rotation.value,
                    "DeltaT_GeV": delta_gev,
                    "wave_component": wave_label,
                    "current_component": current_label,
                    "angular_contribution_real": float(contribution.real),
                    "angular_contribution_imag": float(contribution.imag),
                    "I_pp_real": float(current.plus_plus.real),
                    "I_p0_real": float(current.plus_zero.real),
                    "I_pm_real": float(current.plus_minus.real),
                    "I_00_real": float(current.zero_zero.real),
                    "full_angular_residual": float(abs(full_residual)),
                }
            )
        if not np.allclose(reconstructed_residual, full_residual, atol=2e-14, rtol=0.0):
            raise RuntimeError("component angular residuals do not reconstruct the full result")
        largest = max(
            (
                (abs(helicity_current(matrix).angular_condition(eta)), labels)
                for labels, matrix in term_matrices.items()
            )
        )
        print(
            f"{args.wave_function} Delta={delta_gev:.3f} "
            f"residual={abs(full_residual):.9g} "
            f"relative={full_current.relative_angular_violation(eta):.9g} "
            f"largest_term={largest[1][0]}-{largest[1][1]}:{largest[0]:.9g}"
        )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
