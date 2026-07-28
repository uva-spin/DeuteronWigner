#!/usr/bin/env python3
"""Audit production-grid quark TMD convergence against finer quadrature.

The comparison is made only between rows with identical physical labels.
Relative maxima exclude numerically unresolved entries, while the global
relative L2 norm retains every entry and therefore remains sensitive to the
full exported spin/flavor/mechanism basis.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


WAVE_FUNCTIONS = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
KEYS = (
    "flavor_label",
    "mechanism",
    "operator_projection",
    "target_channel",
    "tmd",
    "rank",
    "t_odd",
    "gauge_link",
    "x_N",
    "x_D",
    "Q_GeV",
    "k_GeV",
    "azimuth_rad",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path("outputs/parent_tmds"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--candidate-label", default="medium")
    parser.add_argument("--reference-label", default="fine")
    parser.add_argument("--relative-l2-tolerance", type=float, default=0.01)
    parser.add_argument("--pointwise-relative-tolerance", type=float, default=0.02)
    parser.add_argument("--pointwise-absolute-tolerance", type=float, default=2.0e-8)
    parser.add_argument("--resolved-floor", type=float, default=1.0e-8)
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compare_wave(args: argparse.Namespace, wave: str) -> dict:
    candidate_path = args.directory / f"quark_{wave}_{args.candidate_label}.csv"
    reference_path = args.directory / f"quark_{wave}_{args.reference_label}.csv"
    candidate = pd.read_csv(candidate_path)
    reference_table = pd.read_csv(reference_path)
    require(len(candidate) == len(reference_table), f"{wave}: row-count mismatch")
    joined = candidate.merge(
        reference_table,
        on=list(KEYS),
        suffixes=("_candidate", "_reference"),
        validate="one_to_one",
    )
    require(len(joined) == len(candidate), f"{wave}: physical-key mismatch")

    reference = joined["F_GeV-2_reference"].to_numpy()
    estimate = joined["F_GeV-2_candidate"].to_numpy()
    difference = estimate - reference
    reference_norm = float(np.linalg.norm(reference))
    require(reference_norm > 0.0, f"{wave}: zero reference norm")
    relative_l2 = float(np.linalg.norm(difference) / reference_norm)

    scale = np.maximum(np.abs(reference), np.abs(estimate))
    resolved = scale > args.resolved_floor
    require(bool(np.any(resolved)), f"{wave}: no resolved entries")
    relative = np.zeros_like(scale)
    relative[resolved] = np.abs(difference[resolved]) / scale[resolved]
    maximum_index = int(np.argmax(relative))
    maximum_relative = float(relative[maximum_index])
    maximum_row = joined.iloc[maximum_index]
    allowed = (
        args.pointwise_absolute_tolerance
        + args.pointwise_relative_tolerance * scale
    )
    normalized_pointwise_error = np.abs(difference) / allowed
    worst_pointwise_index = int(np.argmax(normalized_pointwise_error))
    maximum_normalized_pointwise_error = float(
        normalized_pointwise_error[worst_pointwise_index]
    )
    worst_pointwise_row = joined.iloc[worst_pointwise_index]

    by_mechanism = {}
    for mechanism, group in joined.groupby("mechanism", sort=True):
        ref = group["F_GeV-2_reference"].to_numpy()
        delta = group["F_GeV-2_candidate"].to_numpy() - ref
        norm = float(np.linalg.norm(ref))
        by_mechanism[mechanism] = (
            float(np.linalg.norm(delta) / norm) if norm > 0.0 else 0.0
        )

    passed = (
        relative_l2 <= args.relative_l2_tolerance
        and maximum_normalized_pointwise_error <= 1.0
    )
    return {
        "status": "pass" if passed else "fail",
        "candidate": str(candidate_path),
        "reference": str(reference_path),
        "rows": int(len(joined)),
        "relative_l2": relative_l2,
        "maximum_resolved_relative": maximum_relative,
        "maximum_resolved_location": {
            "flavor": str(maximum_row.flavor_label),
            "mechanism": str(maximum_row.mechanism),
            "gauge_link": str(maximum_row.gauge_link),
            "k_GeV": float(maximum_row.k_GeV),
            "tmd": str(maximum_row.tmd),
            "target_channel": str(maximum_row.target_channel),
        },
        "maximum_absolute_difference": float(np.max(np.abs(difference))),
        "maximum_normalized_mixed_pointwise_error": (
            maximum_normalized_pointwise_error
        ),
        "worst_mixed_pointwise_location": {
            "flavor": str(worst_pointwise_row.flavor_label),
            "mechanism": str(worst_pointwise_row.mechanism),
            "gauge_link": str(worst_pointwise_row.gauge_link),
            "k_GeV": float(worst_pointwise_row.k_GeV),
            "tmd": str(worst_pointwise_row.tmd),
            "target_channel": str(worst_pointwise_row.target_channel),
        },
        "relative_l2_by_mechanism": by_mechanism,
    }


def main() -> None:
    args = parse_args()
    waves = {wave: compare_wave(args, wave) for wave in WAVE_FUNCTIONS}
    passed = all(item["status"] == "pass" for item in waves.values())
    report = {
        "status": "pass" if passed else "fail",
        "comparison": (
            f"{args.candidate_label} candidate quadrature versus "
            f"{args.reference_label} reference quadrature"
        ),
        "relative_l2_tolerance": args.relative_l2_tolerance,
        "pointwise_relative_tolerance": args.pointwise_relative_tolerance,
        "pointwise_absolute_tolerance_GeV-2": args.pointwise_absolute_tolerance,
        "resolved_floor_GeV-2": args.resolved_floor,
        "waves": waves,
        "worst_relative_l2": max(item["relative_l2"] for item in waves.values()),
        "worst_resolved_relative": max(
            item["maximum_resolved_relative"] for item in waves.values()
        ),
        "worst_normalized_mixed_pointwise_error": max(
            item["maximum_normalized_mixed_pointwise_error"]
            for item in waves.values()
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Convergence audit {report['status']}; wrote {args.output}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
