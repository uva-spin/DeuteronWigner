#!/usr/bin/env python3
"""Audit all six full-correlator gluon wave-function members."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

import pandas as pd

from deuteron_wigner.correlator_io import deserialize_gluon_correlator
from deuteron_wigner.joint_positivity import audit_gluon_correlator_members


ROOT = Path(__file__).resolve().parents[1]
WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
MECHANISMS = ("proton_impulse", "neutron_impulse", "impulse_total")
OUTPUT = ROOT / "outputs/validation/gluon_wave_joint_positivity.json"
ROWS = ROOT / "outputs/validation/gluon_wave_joint_positivity.csv"


def main() -> None:
    members = {}
    point_rows = []
    for wave in WAVES:
        path = ROOT / f"outputs/parent_tmds/gluon_{wave}_medium.correlators.csv"
        table = pd.read_csv(path)
        matrices = []
        for labels, group in table[
            table["mechanism"].isin(MECHANISMS)
        ].groupby(["mechanism", "x_N", "Q_GeV", "k_GeV", "azimuth_rad"], sort=True):
            matrix = deserialize_gluon_correlator(group)
            matrices.append(matrix)
            mechanism, x, q, k, azimuth = labels
            from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator
            point_rows.append({
                "wave_function": wave,
                "mechanism": mechanism,
                "x_N": x,
                "Q_GeV": q,
                "k_GeV": k,
                "azimuth_rad": azimuth,
                "minimum_eigenvalue": (
                    Spin1GluonCorrelator(matrix).minimum_positivity_eigenvalue()
                ),
            })
        members[wave] = matrices
    audit = audit_gluon_correlator_members(members)
    report = {
        "source_pattern": "outputs/parent_tmds/gluon_{wave}_medium.correlators.csv",
        "mechanisms": list(MECHANISMS),
        "members": [asdict(item) for item in audit.members],
        "global_minimum_eigenvalue": audit.global_minimum_eigenvalue,
        "all_compatible": audit.all_compatible,
        "tensions_are_clipped": audit.tensions_are_clipped,
        "projection_only_interpolated_ensemble": {
            "path": "outputs/parent_tmds/ensemble/gluon_parent_tmd_ensemble.csv",
            "joint_positivity_status": "not reconstructible",
            "reason": (
                "wave envelopes do not retain correlated member-level full "
                "target-gluon matrices"
            ),
        },
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    pd.DataFrame(point_rows).to_csv(ROWS, index=False)
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "members": len(audit.members),
        "points": len(point_rows),
        "global_minimum_eigenvalue": audit.global_minimum_eigenvalue,
        "all_compatible": audit.all_compatible,
    }, indent=2))


if __name__ == "__main__":
    main()
