#!/usr/bin/env python3
"""Extract LF form factors and elastic observables under all prescriptions."""

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
    NamedCurrentPrescription,
    SpinOnePlusCurrent,
    extract_form_factors,
)

HBARC_GEV_FM = 0.1973269804


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("decomposition", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    totals = defaultdict(lambda: np.zeros(4, dtype=np.float64))
    metadata = {}
    with args.decomposition.open(newline="") as stream:
        for row in csv.DictReader(stream):
            delta = float(row["DeltaT_GeV"])
            metadata[delta] = (row["wave_function"], row.get("spin_rotation", "melosh"))
            totals[delta] += np.asarray(
                [
                    float(row["I_pp_real"]),
                    float(row["I_p0_real"]),
                    float(row["I_pm_real"]),
                    float(row["I_00_real"]),
                ]
            )
    reference = load_av18_electromagnetic_tables("data/raw/av18/fdeut.av18")
    named = {
        NamedCurrentPrescription.GRACH_KONDRATYUK.value: (
            NamedCurrentPrescription.GRACH_KONDRATYUK.omitted_amplitude
        ),
        NamedCurrentPrescription.BRODSKY_HILLER.value: (
            NamedCurrentPrescription.BRODSKY_HILLER.omitted_amplitude
        ),
        "omit_I+0": CurrentPrescription.OMIT_P0,
        "omit_I+-": CurrentPrescription.OMIT_PM,
    }
    rows = []
    for delta, amplitudes in sorted(totals.items()):
        eta = delta**2 / (4.0 * (reference.deuteron_mass_mev / 1000.0) ** 2)
        q_fm = delta / HBARC_GEV_FM
        current = SpinOnePlusCurrent(*amplitudes)
        gc_reference = reference.charge_form_factor(q_fm)
        gm_reference = reference.magnetic_form_factor(q_fm)
        gq_reference = reference.quadrupole_form_factor(q_fm)
        a_reference = reference.observable_a(q_fm)
        b_reference = reference.observable_b(q_fm)
        t20_reference = reference.observable_t20(q_fm)
        point_rows = []
        for label, prescription in named.items():
            gc, gm, gq = extract_form_factors(
                current, eta=eta, prescription=prescription
            )
            if max(abs(gc.imag), abs(gm.imag), abs(gq.imag)) > 1e-10:
                raise ValueError("form-factor extraction has a significant imaginary part")
            structure_a, structure_b, t20 = elastic_observables(
                q_fm=q_fm,
                gc=gc.real,
                gm=gm.real,
                gq=gq.real,
                deuteron_mass_mev=reference.deuteron_mass_mev,
            )
            point_rows.append(
                {
                    "wave_function": metadata[delta][0],
                    "spin_rotation": metadata[delta][1],
                    "DeltaT_GeV": delta,
                    "prescription": label,
                    "GC": gc.real,
                    "GM": gm.real,
                    "GQ": gq.real,
                    "A": float(structure_a),
                    "B": float(structure_b),
                    "t20_70deg": float(t20),
                    "GC_AV18_reference": gc_reference,
                    "GM_AV18_reference": gm_reference,
                    "GQ_AV18_reference": gq_reference,
                    "A_AV18_reference": a_reference,
                    "B_AV18_reference": b_reference,
                    "t20_AV18_reference": t20_reference,
                    "relative_angular_violation": current.relative_angular_violation(eta),
                }
            )
        rows.extend(point_rows)
        print(
            f"{metadata[delta][0]} Delta={delta:.3f} "
            f"GC=[{min(row['GC'] for row in point_rows):.6g},"
            f"{max(row['GC'] for row in point_rows):.6g}] ref={gc_reference:.6g} "
            f"GM=[{min(row['GM'] for row in point_rows):.6g},"
            f"{max(row['GM'] for row in point_rows):.6g}] ref={gm_reference:.6g} "
            f"GQ=[{min(row['GQ'] for row in point_rows):.6g},"
            f"{max(row['GQ'] for row in point_rows):.6g}] ref={gq_reference:.6g}"
        )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
