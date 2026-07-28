#!/usr/bin/env python3
"""Compute the unpolarized one-body transverse overlap form factor."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.form_factors import load_av18_electromagnetic_tables
from deuteron_wigner.gtmd_convolution import (
    TransferMapping,
    build_off_forward_spin_quadrature,
    convolve_local_current,
)
from deuteron_wigner.lf_current import (
    SpinOnePlusCurrent,
    dirac_pauli_from_sachs,
    nucleon_plus_current,
    prescription_spread,
)
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, default="cd-bonn")
    parser.add_argument("--k-max", type=float, default=15.0)
    parser.add_argument("--delta-max-gev", type=float, default=1.0)
    parser.add_argument("--n-delta", type=int, default=11)
    parser.add_argument("--n-k", type=int, default=24)
    parser.add_argument("--n-cos", type=int, default=16)
    parser.add_argument("--n-phi", type=int, default=12)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.k_max)
    radial = selection.radial
    if args.wave_function == "av18":
        electromagnetic = load_av18_electromagnetic_tables(
            "data/raw/av18/fdeut.av18"
        )
    rows = []
    for delta_gev in np.linspace(0.0, args.delta_max_gev, args.n_delta):
        delta_fm = float(delta_gev / HBARC_GEV_FM)
        quadrature = build_off_forward_spin_quadrature(
            radial=radial,
            nucleon_mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
            k_max=args.k_max,
            delta_x=delta_fm,
            delta_y=0.0,
            n_k=args.n_k,
            n_cos_theta=args.n_cos,
            n_phi=args.n_phi,
        )
        # Average target helicities and trace the active nucleon.
        node_overlap = np.einsum("nIIaa->n", quadrature.spectral) / 3.0
        overlap = np.dot(quadrature.weights, node_overlap)
        if abs(overlap.imag) > 1e-10:
            raise ValueError("unpolarized transverse overlap has an unexpected imaginary part")
        row = {
            "DeltaT_GeV": float(delta_gev),
            "minus_t_GeV2": float(delta_gev**2),
            "body_overlap": float(overlap.real),
        }
        if args.wave_function == "av18":
            def isoscalar_half_current(delta_x, delta_y, scale):
                q_fm = float(np.hypot(delta_x, delta_y))
                return electromagnetic.isoscalar_electric(q_fm) * np.eye(2)

            for mapping, label in (
                (TransferMapping.IDENTITY, "GC_identity"),
                (TransferMapping.ACTIVE_FRACTION, "GC_active_fraction"),
            ):
                current = convolve_local_current(
                    scale=1.0,
                    proton_current=isoscalar_half_current,
                    neutron_current=isoscalar_half_current,
                    quadrature=quadrature,
                    transfer_mapping=mapping,
                ).values
                row[label] = float(np.trace(current).real / 3.0)
            row["GC_AV18_reference"] = electromagnetic.charge_form_factor(delta_fm)

            def isoscalar_half_lf_current(delta_x, delta_y, scale):
                q_fm = float(np.hypot(delta_x, delta_y))
                ge = electromagnetic.isoscalar_electric(q_fm)
                gm = electromagnetic.isoscalar_magnetic(q_fm)
                f1, f2 = dirac_pauli_from_sachs(
                    electric=ge,
                    magnetic=gm,
                    q2=q_fm**2,
                    mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
                )
                return nucleon_plus_current(
                    f1=f1,
                    f2=f2,
                    delta_x=delta_x,
                    delta_y=delta_y,
                    mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
                )

            lf_matrix = convolve_local_current(
                scale=1.0,
                proton_current=isoscalar_half_lf_current,
                neutron_current=isoscalar_half_lf_current,
                quadrature=quadrature,
                transfer_mapping=TransferMapping.IDENTITY,
            ).values
            lf_helicity = SpinOnePlusCurrent(
                plus_plus=lf_matrix[0, 0],
                plus_zero=lf_matrix[0, 1],
                plus_minus=lf_matrix[0, 2],
                zero_zero=lf_matrix[1, 1],
            )
            eta = delta_gev**2 / (4.0 * (electromagnetic.deuteron_mass_mev / 1000.0) ** 2)
            row["angular_residual"] = float(abs(lf_helicity.angular_condition(eta)))
            row["relative_angular_violation"] = lf_helicity.relative_angular_violation(eta)
            if eta > 0.0:
                extractions = prescription_spread(lf_helicity, eta=eta)
                charge_values = np.asarray(
                    [form_factors[0].real for form_factors in extractions.values()]
                )
                row["GC_prescription_min"] = float(charge_values.min())
                row["GC_prescription_max"] = float(charge_values.max())
            else:
                row["GC_prescription_min"] = float(lf_matrix[0, 0].real)
                row["GC_prescription_max"] = float(lf_matrix[0, 0].real)
        rows.append(row)
    normalization = rows[0]["body_overlap"]
    for row in rows:
        row["normalized_body_form_factor"] = row["body_overlap"] / normalization
    print(f"# wave_function={args.wave_function} forward_norm={normalization:.12f}")
    columns = tuple(rows[0])
    print("# " + " ".join(columns))
    for row in rows:
        print(" ".join(f"{row[column]:.9g}" for column in columns))
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
