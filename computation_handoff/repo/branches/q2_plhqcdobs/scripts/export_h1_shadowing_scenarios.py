#!/usr/bin/env python3
"""Export correlated H1-DPDF/FGS scenario responses over x, flavor, and wave."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.wavefunctions.selection import WAVE_FUNCTION_CHOICES

FLAVORS = ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/parent_tmds/shadowing/h1_fgs_scenarios.csv"),
    )
    parser.add_argument("--x-points", type=int, default=25)
    parser.add_argument("--integration-points", type=int, default=48)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.x_points < 10:
        raise ValueError("shadowing response grid requires at least 10 x points")
    pdf = LHAPDFProvider("CT18NNLO", 0)
    dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")
    x_axis = np.unique(np.r_[np.geomspace(1.0e-5, 0.09, args.x_points), 0.1])
    rows: list[dict[str, object]] = []
    for wave in WAVE_FUNCTION_CHOICES:
        body_path = (
            f"outputs/stage0/body_form_factor_{wave.replace('-', '_')}.csv"
        )
        body = TabulatedBodyFormFactor.load(body_path)
        # A unit denominator exposes the common diffractive numerator. The
        # flavor-resolved CT18 p+n density is divided below, avoiding repeated
        # integrations without identifying flavor denominators.
        kernel = build_h1_deuteron_shadowing_input(
            inclusive_density=lambda x, q: 1.0,
            body_form_factor=body,
            dpdf=dpdf,
            integration_points=args.integration_points,
        )
        for q_gev in (2.0, 5.0, 10.0):
            for x in x_axis:
                central_numerator = kernel.value("sea", float(x), q_gev)
                member_numerators = kernel.member_values(
                    "sea", float(x), q_gev
                )
                for flavor, label in FLAVORS:
                    denominator = (
                        pdf.proton(flavor, float(x), q_gev)
                        + pdf.neutron(flavor, float(x), q_gev)
                    )
                    values = {
                        "central": central_numerator / denominator,
                        **{
                            name: value / denominator
                            for name, value in member_numerators.items()
                        },
                    }
                    for member, value in values.items():
                        rows.append({
                            "wave_function": wave,
                            "flavor": flavor,
                            "flavor_label": label,
                            "Q_GeV": q_gev,
                            "x_N": float(x),
                            "dpdf_beta_boundary_clamped": bool(x < 1.0e-4),
                            "member": member,
                            "shadowing_fraction": value,
                            "nuclear_ratio": 1.0 - value,
                        })
    table = pd.DataFrame(rows)
    keys = ["wave_function", "flavor", "flavor_label", "Q_GeV", "x_N"]
    envelope = (
        table.groupby(keys, as_index=False)
        .shadowing_fraction.agg(["min", "max"])
        .reset_index()
        .rename(columns={"min": "fraction_min", "max": "fraction_max"})
    )
    central = (
        table.loc[table.member.eq("central"), keys + ["shadowing_fraction"]]
        .rename(columns={"shadowing_fraction": "fraction_central"})
    )
    envelope = envelope.merge(central, on=keys, validate="one_to_one")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(args.output, index=False)
    envelope_path = args.output.with_name(f"{args.output.stem}.envelope.csv")
    envelope.to_csv(envelope_path, index=False)
    metadata = {
        "source": kernel.source,
        "status": "correlated named scenarios; not a statistical covariance",
        "member_identity": [
            "central", "dpdf_norm_down", "dpdf_norm_up",
            "t_slope_down", "t_slope_up",
        ],
        "correlation_rule": (
            "the same named variation is applied coherently across x, flavor, "
            "Q, and wave function"
        ),
        "statistical_covariance_available": False,
        "reason": (
            "the official H1 v1.0 release used here contains central grids, "
            "not eigenvector or replica grids"
        ),
        "small_x_provenance": (
            "rows with x_N < 1e-4 set dpdf_beta_boundary_clamped=true: the "
            "official H1 beta boundary is clamped there and those rows are "
            "diagnostic extrapolations outside the production x validity"
        ),
        "integration_points": args.integration_points,
        "rows": len(table),
        "envelope_path": str(envelope_path),
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(table)} scenario rows to {args.output}")


if __name__ == "__main__":
    main()
