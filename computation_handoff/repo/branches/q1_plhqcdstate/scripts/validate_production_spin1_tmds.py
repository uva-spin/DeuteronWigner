#!/usr/bin/env python3
"""Validate completeness, symmetries, bounds, marginals, and smoothness."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import simpson

INPUT = Path("outputs/production_tmds/spin1_tmds_x010_q5.csv")
REPORT = Path("outputs/production_tmds/validation.json")
COMPONENTS = (
    "pdf",
    "wave_function",
    "transverse_profile",
    "evolution",
    "gauge_phase",
    "mechanism",
    "numerical",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = pd.read_csv(INPUT)
    numeric = data.select_dtypes(include=[np.number]).to_numpy()
    require(np.isfinite(numeric).all(), "table contains NaN or infinity")
    basis_counts = (
        data[data.gauge_link == "future_SIDIS"]
        .groupby(["flavor_label"])["tmd"]
        .nunique()
        .to_dict()
    )
    require(
        basis_counts == {"d": 18, "dbar": 18, "g": 19, "u": 18, "ubar": 18},
        f"incomplete basis: {basis_counts}",
    )
    points = data.groupby(["flavor_label", "tmd", "gauge_link"])["k_GeV"].nunique()
    require(bool((points == 241).all()), "not every curve has 241 k points")
    require(len(data) == 43862, f"unexpected row count {len(data)}")

    for component in COMPONENTS:
        lower = data[f"{component}_lower_GeV-2"].to_numpy()
        upper = data[f"{component}_upper_GeV-2"].to_numpy()
        central = data["F_central_GeV-2"].to_numpy()
        require(bool(np.all(lower <= upper)), f"{component} bounds are reversed")
        tolerance = 1.0e-12 + 1.0e-10 * np.abs(central)
        require(
            bool(np.all(central >= lower - tolerance))
            and bool(np.all(central <= upper + tolerance)),
            f"{component} envelope does not contain the central curve",
        )

    keys = ["flavor_label", "tmd", "k_GeV"]
    future = data[data.gauge_link == "future_SIDIS"].set_index(keys)
    past = data[data.gauge_link == "past_DY"].set_index(keys)
    aligned = future.join(
        past[["F_central_GeV-2"]], rsuffix="_past", how="inner"
    )
    expected = np.where(
        aligned["t_odd"].to_numpy().astype(bool),
        -aligned["F_central_GeV-2_past"].to_numpy(),
        aligned["F_central_GeV-2_past"].to_numpy(),
    )
    require(
        bool(np.allclose(aligned["F_central_GeV-2"], expected, atol=1e-13, rtol=1e-12)),
        "SIDIS/DY time-reversal relation failed",
    )

    origin = data[np.isclose(data.k_GeV, 0.0)]
    require(
        bool(np.allclose(origin.loc[origin["rank"] > 0, "physical_ratio_central"], 0.0)),
        "positive-rank physical modulation does not vanish at origin",
    )
    max_modulation = float(np.max(np.abs(data["physical_ratio_central"])))
    require(max_modulation <= 1.0 + 1e-12, "physical positivity bound failed")

    marginal_residuals: dict[str, float] = {}
    smoothness: dict[str, float] = {}
    for (flavor, name, link), group in data.groupby(
        ["flavor_label", "tmd", "gauge_link"]
    ):
        group = group.sort_values("k_GeV")
        k = group["k_GeV"].to_numpy()
        values = group["F_central_GeV-2"].to_numpy()
        scale = max(float(np.max(np.abs(values))), 1.0e-14)
        normalized_second_difference = float(
            np.max(np.abs(np.diff(values, n=2))) / scale
        )
        smoothness[f"{flavor}:{name}:{link}"] = normalized_second_difference
        require(
            normalized_second_difference < 0.02,
            f"non-smooth curve {flavor}:{name}:{link}",
        )
        if name == "h1LT" and flavor != "g":
            integral = float(2 * np.pi * simpson(k * values, x=k))
            marginal_residuals[f"{flavor}:{link}"] = integral
            require(abs(integral) < 2.0e-9, "h1LT zero marginal failed")

    report = {
        "status": "pass",
        "rows": len(data),
        "basis_counts": basis_counts,
        "k_points_per_curve": 241,
        "maximum_absolute_physical_modulation": max_modulation,
        "maximum_normalized_second_difference": max(smoothness.values()),
        "h1LT_marginal_residuals_GeV0": marginal_residuals,
        "checks": [
            "finite values",
            "complete flavor/species basis",
            "dense common k grid",
            "all separate envelopes ordered and central-containing",
            "exact SIDIS/DY T-odd sign reversal",
            "T-even process invariance",
            "positive-rank origin limits",
            "unit physical-modulation bound",
            "rank-zero h1LT zero transverse marginal",
            "central-curve smoothness",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Validation passed; wrote {REPORT}")


if __name__ == "__main__":
    main()
