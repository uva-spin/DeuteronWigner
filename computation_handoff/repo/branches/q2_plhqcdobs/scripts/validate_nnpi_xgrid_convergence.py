#!/usr/bin/env python3
"""Validate coarse/refined x-grid stability of conditional NNpi outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coarse", type=Path, required=True)
    parser.add_argument("--refined", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--total-tolerance", type=float, default=0.01)
    parser.add_argument("--correction-tolerance", type=float, default=0.10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    coarse = pd.read_csv(args.coarse)
    refined = pd.read_csv(args.refined)
    keys = ["flavor", "flavor_label", "x_N", "Q_GeV", "tmd", "pion_member"]
    if not coarse[keys].equals(refined[keys]):
        raise RuntimeError("coarse and refined comparison rows do not align")
    metrics: dict[str, dict[str, dict[str, float]]] = {}
    columns = (
        "baseline", "minimal_unchanged_shape", "conditional_recoil",
        "conditional_minus_minimal",
    )
    for column in columns:
        metrics[column] = {}
        for (flavor, tmd), indices in refined.groupby(
            ["flavor_label", "tmd"]
        ).groups.items():
            left = coarse.loc[indices, column].to_numpy(float)
            right = refined.loc[indices, column].to_numpy(float)
            difference = np.abs(left - right)
            curve_scale = max(float(np.max(np.abs(right))), 1.0e-12)
            metrics[column][f"{flavor}:{tmd}"] = {
                "max_abs": float(np.max(difference)),
                "max_over_curve_peak": float(np.max(difference) / curve_scale),
            }
    summary = {
        column: {
            quantity: max(entry[quantity] for entry in values.values())
            for quantity in ("max_abs", "max_over_curve_peak")
        }
        for column, values in metrics.items()
    }
    status = (
        "pass"
        if summary["conditional_recoil"]["max_over_curve_peak"]
        < args.total_tolerance
        and summary["conditional_minus_minimal"]["max_over_curve_peak"]
        < args.correction_tolerance
        else "fail"
    )
    report = {
        "status": status,
        "coarse": str(args.coarse),
        "refined": str(args.refined),
        "metric": (
            "maximum absolute coarse-refined difference divided by the "
            "peak absolute magnitude of each flavor/TMD curve"
        ),
        "tolerances": {
            "conditional_total": args.total_tolerance,
            "conditional_minus_minimal": args.correction_tolerance,
        },
        "summary": summary,
        "by_curve": metrics,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    if status != "pass":
        raise RuntimeError(f"NNpi x-grid convergence failed: {summary}")


if __name__ == "__main__":
    main()
