#!/usr/bin/env python3
"""Calibrate a covariant dipole magnetic completion to the AV18 benchmark."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import numpy as np

from deuteron_wigner.form_factors import (
    elastic_observables,
    load_av18_electromagnetic_tables,
)
from deuteron_wigner.lf_current import (
    CurrentPrescription,
    SpinOnePlusCurrent,
    dipole_magnetic_completion,
    extract_form_factors,
)

HBARC_GEV_FM = 0.1973269804


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("decomposition", type=Path, nargs="+")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fit-max-gev", type=float, default=0.5)
    parser.add_argument("--static-fit-max-gev", type=float, default=0.05)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    totals = {}
    metadata = {}
    for path in args.decomposition:
        file_totals = defaultdict(lambda: np.zeros(4, dtype=np.float64))
        file_metadata = {}
        with path.open(newline="") as stream:
            for row in csv.DictReader(stream):
                q = float(row["DeltaT_GeV"])
                file_metadata[q] = (
                    row["wave_function"],
                    row.get("spin_rotation", "melosh"),
                )
                file_totals[q] += np.asarray(
                    [
                        float(row["I_pp_real"]),
                        float(row["I_p0_real"]),
                        float(row["I_pm_real"]),
                        float(row["I_00_real"]),
                    ]
                )
        for q, amplitudes in file_totals.items():
            if q in totals and not np.allclose(
                totals[q], amplitudes, rtol=1e-10, atol=1e-12
            ):
                raise ValueError(f"inconsistent duplicate Q={q} GeV in input files")
            totals[q] = amplitudes
            metadata[q] = file_metadata[q]

    reference = load_av18_electromagnetic_tables("data/raw/av18/fdeut.av18")
    mass = reference.deuteron_mass_mev / 1000.0
    q_values = np.asarray(sorted(totals))
    raw_gk = []
    target = []
    currents = {}
    for q in q_values:
        eta = q**2 / (4.0 * mass**2)
        currents[q] = SpinOnePlusCurrent(*totals[q])
        raw_gk.append(
            extract_form_factors(
                currents[q], eta=eta, prescription=CurrentPrescription.OMIT_00
            )[1].real
        )
        target.append(reference.magnetic_form_factor(q / HBARC_GEV_FM))
    raw_gk = np.asarray(raw_gk)
    target = np.asarray(target)

    static = q_values <= args.static_fit_max_gev
    if np.count_nonzero(static) < 3:
        raise ValueError("static extrapolation requires at least three low-Q points")
    coefficients = np.polyfit(q_values[static] ** 2, raw_gk[static], 2)
    raw_static_moment = float(np.polyval(coefficients, 0.0))
    target_static_moment = float(reference.gm[0])
    delta_mu = target_static_moment - raw_static_moment

    fitted = q_values <= args.fit_max_gev
    cutoffs = np.linspace(0.05, 2.0, 20000)
    shapes = 1.0 / (1.0 + (q_values[fitted, None] / cutoffs[None, :]) ** 2) ** 2
    mse = np.mean(
        (raw_gk[fitted, None] + delta_mu * shapes - target[fitted, None]) ** 2,
        axis=0,
    )
    cutoff = float(cutoffs[np.argmin(mse)])

    rows = []
    for q, raw, gm_reference in zip(q_values, raw_gk, target):
        eta = q**2 / (4.0 * mass**2)
        correction = dipole_magnetic_completion(
            eta=eta,
            momentum_transfer=q,
            delta_magnetic_moment=delta_mu,
            cutoff=cutoff,
        )
        original = currents[q]
        completed = SpinOnePlusCurrent(
            original.plus_plus + correction.plus_plus,
            original.plus_zero + correction.plus_zero,
            original.plus_minus + correction.plus_minus,
            original.zero_zero + correction.zero_zero,
        )
        gc, gm, gq = extract_form_factors(
            completed, eta=eta, prescription=CurrentPrescription.OMIT_00
        )
        q_fm = q / HBARC_GEV_FM
        structure_a, structure_b, t20 = elastic_observables(
            q_fm=q_fm,
            gc=gc.real,
            gm=gm.real,
            gq=gq.real,
            deuteron_mass_mev=reference.deuteron_mass_mev,
        )
        rows.append(
            {
                "wave_function": metadata[q][0],
                "spin_rotation": metadata[q][1],
                "DeltaT_GeV": q,
                "prescription": "GK",
                "GM_raw": raw,
                "GM_completed": gm.real,
                "GM_AV18_reference": gm_reference,
                "delta_mu": delta_mu,
                "cutoff_GeV": cutoff,
                "GC_completed": gc.real,
                "GQ_completed": gq.real,
                "A_completed": float(structure_a),
                "B_completed": float(structure_b),
                "t20_70deg_completed": float(t20),
                "A_AV18_reference": float(reference.observable_a(q_fm)),
                "B_AV18_reference": float(reference.observable_b(q_fm)),
                "t20_AV18_reference": float(reference.observable_t20(q_fm)),
                "relative_angular_violation": completed.relative_angular_violation(eta),
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(
        f"raw GM(0)={raw_static_moment:.9g} target={target_static_moment:.9g} "
        f"delta_mu={delta_mu:.9g} cutoff={cutoff:.9g} GeV "
        f"fit_RMS={np.sqrt(np.min(mse)):.9g}"
    )


if __name__ == "__main__":
    main()
