#!/usr/bin/env python3
"""Report one-amplitude completions of a decomposed LF current."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

from deuteron_wigner.lf_current import (
    CurrentPrescription,
    SpinOnePlusCurrent,
    angular_condition_completion,
)

DEUTERON_MASS_GEV = 1.87561337


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("decomposition", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    totals = defaultdict(lambda: dict(I_pp_real=0.0, I_p0_real=0.0, I_pm_real=0.0, I_00_real=0.0))
    metadata = {}
    with args.decomposition.open(newline="") as stream:
        for row in csv.DictReader(stream):
            delta = float(row["DeltaT_GeV"])
            metadata[delta] = (row["wave_function"], row.get("spin_rotation", "melosh"))
            for field in totals[delta]:
                totals[delta][field] += float(row[field])
    rows = []
    for delta, amplitudes in sorted(totals.items()):
        eta = delta**2 / (4.0 * DEUTERON_MASS_GEV**2)
        current = SpinOnePlusCurrent(
            plus_plus=amplitudes["I_pp_real"],
            plus_zero=amplitudes["I_p0_real"],
            plus_minus=amplitudes["I_pm_real"],
            zero_zero=amplitudes["I_00_real"],
        )
        for bad_amplitude in CurrentPrescription:
            completed, correction = angular_condition_completion(
                current, eta=eta, bad_amplitude=bad_amplitude
            )
            if bad_amplitude == CurrentPrescription.OMIT_PP:
                original = current.plus_plus
            elif bad_amplitude == CurrentPrescription.OMIT_P0:
                original = current.plus_zero
            elif bad_amplitude == CurrentPrescription.OMIT_PM:
                original = current.plus_minus
            else:
                original = current.zero_zero
            rows.append(
                {
                    "wave_function": metadata[delta][0],
                    "spin_rotation": metadata[delta][1],
                    "DeltaT_GeV": delta,
                    "completed_amplitude": bad_amplitude.value,
                    "additive_correction_real": correction.real,
                    "correction_over_full_current_l1": abs(correction)
                    / (
                        abs(current.plus_plus)
                        + abs(current.plus_zero)
                        + abs(current.plus_minus)
                        + abs(current.zero_zero)
                    ),
                    "correction_over_selected_amplitude": (
                        abs(correction / original) if original != 0.0 else float("inf")
                    ),
                    "completed_residual": abs(completed.angular_condition(eta)),
                }
            )
    print("# Delta amplitude correction correction/L1 correction/selected")
    for row in rows:
        print(
            f"{row['DeltaT_GeV']:.3f} {row['completed_amplitude']} "
            f"{row['additive_correction_real']:.9g} "
            f"{row['correction_over_full_current_l1']:.9g} "
            f"{row['correction_over_selected_amplitude']:.9g}"
        )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
