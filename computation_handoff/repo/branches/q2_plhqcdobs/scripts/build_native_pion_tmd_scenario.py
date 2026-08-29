#!/usr/bin/env python3
"""Build fit-native high-order pion TMD boundary diagnostics."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    MillerTensorPionDistribution,
)
from deuteron_wigner.pion_tmd import (
    NativeEvolvedTransversePionScenario,
    Vpion19ArtemidePionTMD,
)


OUTPUT = Path("outputs/figures/pion")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    native = Vpion19ArtemidePionTMD(member=0)
    splitting = FockNormalizedMillerPionDistribution(
        MillerTensorPionDistribution()
    )
    nuclear = NativeEvolvedTransversePionScenario(splitting, native)
    b_grid = np.asarray((0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0))
    z, x, q = 0.3, 0.1, 5.0

    intrinsic_members = np.empty((101, b_grid.size))
    nuclear_members = np.empty((101, b_grid.size))
    for member in range(101):
        native.set_member(member)
        intrinsic_members[member] = [
            native.isoscalar_b_value(2, z, float(b), q) for b in b_grid
        ]
        nuclear_members[member] = [
            nuclear.value(2, x, float(b), q) for b in b_grid
        ]

    low = np.percentile(intrinsic_members[1:], 16.0, axis=0)
    high = np.percentile(intrinsic_members[1:], 84.0, axis=0)
    nuclear_low = np.percentile(nuclear_members[1:], 16.0, axis=0)
    nuclear_high = np.percentile(nuclear_members[1:], 84.0, axis=0)
    with (OUTPUT / "native_vpion19_jam21_bspace.csv").open(
        "w", newline=""
    ) as stream:
        writer = csv.writer(stream)
        writer.writerow(
            (
                "b_GeV_inv",
                "intrinsic_z0p3_central",
                "intrinsic_z0p3_replica_p16",
                "intrinsic_z0p3_replica_p84",
                "deuteron_pion_x0p1_central",
                "deuteron_pion_x0p1_replica_p16",
                "deuteron_pion_x0p1_replica_p84",
            )
        )
        writer.writerows(
            zip(
                b_grid, intrinsic_members[0], low, high,
                nuclear_members[0], nuclear_low, nuclear_high,
            )
        )
    with (OUTPUT / "native_vpion19_jam21_bspace_members.csv").open(
        "w", newline=""
    ) as stream:
        writer = csv.writer(stream)
        writer.writerow(("member", "b_GeV_inv", "deuteron_pion_x0p1"))
        writer.writerows(
            (member, b, nuclear_members[member, index])
            for member in range(101)
            for index, b in enumerate(b_grid)
        )

    report = {
        **native.metadata,
        "scale_gev": q,
        "intrinsic_pion_x": z,
        "deuteron_x": x,
        "members_evaluated": 101,
        "replica_interval": "16th-84th percentiles of physical members 1..100",
        "nuclear_recoil": nuclear.metadata["nuclear_recoil"],
        "fock_normalization": splitting.normalization,
        "constants": "build/artemide/const-Vpion19-native",
        "setup_command": (
            "/Users/dustin/miniforge3/bin/python3.9 "
            "tools/prepare_vpion19_artemide.py"
        ),
        "finite": bool(
            np.all(np.isfinite(intrinsic_members))
            and np.all(np.isfinite(nuclear_members))
        ),
    }
    (OUTPUT / "native_vpion19_jam21_bspace.validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
