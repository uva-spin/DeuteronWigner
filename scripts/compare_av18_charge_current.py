#!/usr/bin/env python3
"""Compare the LF overlap/current proxy with Wiringa's AV18 IA tables."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.form_factors import (
    charge_impulse_from_body,
    load_av18_electromagnetic_tables,
)

HBARC_GEV_FM = 0.1973269804


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--overlap", type=Path, default=Path("outputs/stage0/body_form_factor_av18.csv")
    )
    parser.add_argument(
        "--reference", type=Path, default=Path("data/raw/av18/fdeut.av18")
    )
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with args.overlap.open(newline="") as stream:
        overlap_rows = tuple(csv.DictReader(stream))
    tables = load_av18_electromagnetic_tables(args.reference)
    rows = []
    for source in overlap_rows:
        delta_gev = float(source["DeltaT_GeV"])
        q_fm = delta_gev / HBARC_GEV_FM
        body_lf = float(source["normalized_body_form_factor"])
        ce_reference = tables.body_charge(q_fm) / tables.ce[0]
        ges = tables.isoscalar_electric(q_fm)
        gc_lf = float(charge_impulse_from_body(body_overlap=body_lf, ges=ges))
        gc_reference = tables.charge_form_factor(q_fm) / tables.gc[0]
        rows.append(
            {
                "DeltaT_GeV": delta_gev,
                "q_fm_inv": q_fm,
                "body_LF": body_lf,
                "ce_AV18_reference": ce_reference,
                "body_relative_difference": body_lf / ce_reference - 1.0,
                "GC_LF_current_proxy": gc_lf,
                "GC_AV18_reference": gc_reference,
                "GC_relative_difference": gc_lf / gc_reference - 1.0,
            }
        )
    print("# DeltaT_GeV body_LF ce_ref body_rel_diff GC_LF GC_ref GC_rel_diff")
    for row in rows:
        print(
            f"{row['DeltaT_GeV']:.6g} {row['body_LF']:.9g} "
            f"{row['ce_AV18_reference']:.9g} {row['body_relative_difference']:.6g} "
            f"{row['GC_LF_current_proxy']:.9g} {row['GC_AV18_reference']:.9g} "
            f"{row['GC_relative_difference']:.6g}"
        )
    finite = [
        abs(row["GC_relative_difference"])
        for row in rows
        if abs(row["GC_AV18_reference"]) > 1e-3
    ]
    print(f"# max_abs_GC_relative_difference_away_from_zero={max(finite):.6g}")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
