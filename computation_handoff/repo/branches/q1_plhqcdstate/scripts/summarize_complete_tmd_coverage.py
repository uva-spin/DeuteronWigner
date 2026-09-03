#!/usr/bin/env python3
"""Summarize predictive resolution of the complete constrained TMD grid."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


def main() -> None:
    source = Path("outputs/complete/spin1_tmd_phase_space.csv")
    output = Path("outputs/complete/spin1_tmd_predictive_coverage.csv")
    rows = list(csv.DictReader(source.open()))
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["species"], row["tmd"])].append(row)

    summaries = []
    for (species, tmd), values in sorted(grouped.items()):
        nonzero_points = 0
        resolved_points = 0
        kinematic_zero_points = 0
        relative_half_widths = []
        for value in values:
            central = float(value["physical_ratio_central"])
            lower = float(value["physical_ratio_lower95"])
            upper = float(value["physical_ratio_upper95"])
            if lower == 0.0 and upper == 0.0:
                kinematic_zero_points += 1
                continue
            nonzero_points += 1
            if lower > 0.0 or upper < 0.0:
                resolved_points += 1
            if central != 0.0:
                relative_half_widths.append(
                    0.5 * abs(upper - lower) / abs(central)
                )
        first = values[0]
        summaries.append(
            {
                "species": species,
                "tmd": tmd,
                "target_channel": first["target_channel"],
                "rank": first["rank"],
                "t_odd": first["t_odd"],
                "status": first["status"],
                "sample_points": len(values),
                "kinematic_zero_points": kinematic_zero_points,
                "nonzero_points": nonzero_points,
                "sign_resolved_points": resolved_points,
                "sign_resolved_fraction": (
                    resolved_points / nonzero_points if nonzero_points else 1.0
                ),
                "maximum_relative_95_half_width": (
                    max(relative_half_widths)
                    if relative_half_widths else 0.0
                ),
            }
        )
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)

    resolved_functions = sum(
        float(row["sign_resolved_fraction"]) == 1.0 for row in summaries
    )
    t_even = [row for row in summaries if row["t_odd"] == "0"]
    t_odd = [row for row in summaries if row["t_odd"] == "1"]
    total_nonzero = sum(int(row["nonzero_points"]) for row in summaries)
    total_resolved = sum(int(row["sign_resolved_points"]) for row in summaries)
    t_even_nonzero = sum(int(row["nonzero_points"]) for row in t_even)
    t_even_resolved = sum(int(row["sign_resolved_points"]) for row in t_even)
    payload = {
        "basis_functions": len(summaries),
        "fully_sign_resolved_functions": resolved_functions,
        "fully_sign_resolved_fraction": resolved_functions / len(summaries),
        "t_even_functions": len(t_even),
        "fully_sign_resolved_t_even": sum(
            float(row["sign_resolved_fraction"]) == 1.0 for row in t_even
        ),
        "t_odd_functions": len(t_odd),
        "fully_sign_resolved_t_odd": sum(
            float(row["sign_resolved_fraction"]) == 1.0 for row in t_odd
        ),
        "sign_resolved_nonzero_phase_points": total_resolved,
        "nonzero_phase_points": total_nonzero,
        "sign_resolved_phase_fraction": total_resolved / total_nonzero,
        "t_even_sign_resolved_phase_fraction": (
            t_even_resolved / t_even_nonzero
        ),
        "interpretation": (
            "The T-even completion is sign resolved over nearly all of the "
            "declared phase grid; the exceptions are high-k gluon profile "
            "envelopes where the W-term-only model lacks a Y-term. "
            "T-odd priors intentionally include zero and require process data "
            "or a gauge-link dynamics calculation for sign-resolved prediction."
        ),
    }
    output.with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
