#!/usr/bin/env python3
"""Fourier--Bessel transform the GTMD body-overlap marginal to impact space."""

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.special import j0

HBARC_GEV_FM = 0.1973269804


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--b-max-fm", type=float, default=5.0)
    parser.add_argument("--n-b", type=int, default=101)
    arguments = parser.parse_args()
    with arguments.source.open(encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    delta_gev = np.asarray([float(row["DeltaT_GeV"]) for row in rows])
    delta_fm = delta_gev / HBARC_GEV_FM
    form_factor = np.asarray(
        [float(row["normalized_body_form_factor"]) for row in rows]
    )
    b_values = np.linspace(0.0, arguments.b_max_fm, arguments.n_b)
    output = []
    for b_fm in b_values:
        density = simpson(
            delta_fm * j0(b_fm * delta_fm) * form_factor,
            x=delta_fm,
        ) / (2.0 * np.pi)
        output.append(
            {
                "bT_fm": float(b_fm),
                "rho_body_fm^-2": float(density),
                "Delta_max_GeV": float(delta_gev[-1]),
                "truncated_transform": 1,
            }
        )
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(output[0]))
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    main()
