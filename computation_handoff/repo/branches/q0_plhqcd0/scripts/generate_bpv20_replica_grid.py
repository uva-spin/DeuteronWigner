#!/usr/bin/env python3
"""Generate and independently audit the official BPV20 momentum replicas."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.bpv20_sivers import BPV20ArtemideSivers, BPV20ReplicaMomentumGrid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=Path("data/processed/bpv20_sivers_replicas_Q5.npz"),
    )
    parser.add_argument("--q", type=float, default=5.0)
    parser.add_argument("--x-points", type=int, default=65)
    parser.add_argument("--k-points", type=int, default=121)
    parser.add_argument("--audit-points", type=int, default=96)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    x_axis = np.geomspace(0.01, 0.25, args.x_points)
    k_axis = 1.5 * np.linspace(0.0, 1.0, args.k_points) ** 1.5
    reference = BPV20ArtemideSivers()
    grid = BPV20ReplicaMomentumGrid.generate(
        reference, q_gev=args.q, x_axis=x_axis, k_axis_gev=k_axis
    )
    grid.save(args.output)

    rng = np.random.default_rng(20260725)
    relative_errors: list[float] = []
    absolute_errors: list[float] = []
    audit: list[dict[str, float | int]] = []
    for _ in range(args.audit_points):
        member = int(rng.integers(1, 501))
        flavor = int(rng.choice(grid.flavors))
        x = float(np.exp(rng.uniform(np.log(0.01), np.log(0.25))))
        k = float(rng.uniform(0.0, 1.5))
        interpolated = float(grid.interpolate_all(flavor, [x], [k])[member - 1, 0])
        exact = float(reference._momentum_values(member, x, k, args.q)[flavor + 5])
        absolute = abs(interpolated - exact)
        relative = absolute / max(abs(exact), 1.0e-10)
        absolute_errors.append(absolute)
        relative_errors.append(relative)
        audit.append({
            "member": member, "flavor": flavor, "x": x, "k_GeV": k,
            "exact": exact, "interpolated": interpolated,
            "absolute_error": absolute, "relative_error": relative,
        })
    metadata = {
        "source": "BPV20(n3lo).rep official 500-replica release",
        "central_member": "not stored; member 0 remains a separate fit central",
        "replica_members": [1, 500],
        "shape": list(grid.values.shape),
        "Q_GeV": args.q,
        "evaluator": grid.evaluator,
        "axes": {
            "x": {"points": args.x_points, "minimum": 0.01, "maximum": 0.25},
            "k_GeV": {"points": args.k_points, "minimum": 0.0, "maximum": 1.5},
        },
        "interpolation": "bilinear in x and k; x nodes are logarithmic",
        "audit_seed": 20260725,
        "audit_points": args.audit_points,
        "maximum_absolute_error": max(absolute_errors),
        "maximum_relative_error_above_1e-10": max(relative_errors),
        "p95_relative_error_above_1e-10": float(np.quantile(relative_errors, 0.95)),
        "audit": audit,
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(json.dumps({key: value for key, value in metadata.items() if key != "audit"}, indent=2))


if __name__ == "__main__":
    main()
