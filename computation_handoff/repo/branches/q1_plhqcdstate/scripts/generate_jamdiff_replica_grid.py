#!/usr/bin/env python3
"""Generate and audit the official member-resolved JAMDiFF transversity grid."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.transversity import (
    JAMDiFFReplicaGrid,
    JAMDiFFTransversityReplicas,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=Path("data/processed/jamdiff_wlqcd_transversity_replicas_Q5.npz"),
    )
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--x-points", type=int, default=193)
    args = parser.parse_args()
    # Dense endpoint-aware axis: LF nodes at x_D=0.05 never require x<0.05.
    x_axis = np.unique(np.concatenate((
        np.geomspace(0.05, 0.5, args.x_points // 2),
        np.linspace(0.5, 0.99, args.x_points - args.x_points // 2),
    )))
    source = JAMDiFFTransversityReplicas()
    grid = JAMDiFFReplicaGrid.generate(
        source, scale_gev=args.scale, x_axis=x_axis
    )
    grid.save(args.output)
    rng = np.random.default_rng(20260725)
    errors = []
    for _ in range(64):
        flavor = int(rng.choice(grid.flavors))
        member = int(rng.integers(1, 969))
        x = float(rng.uniform(0.05, 0.99))
        exact = source.replicas(flavor, x, args.scale)[member - 1]
        interpolated = grid.interpolate_all(flavor, [x])[member - 1, 0]
        errors.append(abs(interpolated - exact) / max(abs(exact), 1.0e-10))
    metadata = {
        "source": "JAMDiFF23-transversity_lo official LHAPDF release",
        "source_commit": "2d601943b003ab03d261d492b565c1ebf54d07cc",
        "central_member": 0,
        "physical_replica_members": [1, 968],
        "replica_count": 968,
        "scale_GeV": args.scale,
        "x_axis": [float(x_axis[0]), float(x_axis[-1]), len(x_axis)],
        "interpolation": "linear in x; source LHAPDF interpolation evaluated at nodes",
        "audit_seed": 20260725,
        "audit_points": 64,
        "maximum_relative_error_above_1e-10": max(errors),
        "p95_relative_error_above_1e-10": float(np.quantile(errors, 0.95)),
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
