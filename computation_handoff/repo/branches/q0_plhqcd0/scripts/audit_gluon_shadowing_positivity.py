#!/usr/bin/env python3
"""Audit central and named shadowing members as full target-gluon matrices."""

import json
from pathlib import Path

import pandas as pd

from deuteron_wigner.correlator_io import deserialize_gluon_correlator
from deuteron_wigner.gluon_nuclear_mechanisms import (
    apply_gluon_nuclear_mechanisms, build_inclusive_gluon_shadowing_input,
)
from deuteron_wigner.joint_positivity import audit_gluon_correlator_members

SOURCE = Path(
    "outputs/parent_tmds/gluon_av18_shadowing_x001_medium.correlators.csv"
)
OUT = Path("outputs/validation/gluon_shadowing_joint_positivity.json")


def main() -> None:
    table = pd.read_csv(SOURCE)
    members = {"central": [], "shadowing_low": [], "shadowing_high": []}
    for (_, _, k, azimuth), point in table.groupby(
        ["x_N", "Q_GeV", "k_GeV", "azimuth_rad"], sort=True
    ):
        proton = deserialize_gluon_correlator(
            point.loc[point.mechanism.eq("proton_impulse")]
        )
        neutron = deserialize_gluon_correlator(
            point.loc[point.mechanism.eq("neutron_impulse")]
        )
        result = apply_gluon_nuclear_mechanisms(
            proton_impulse=proton, neutron_impulse=neutron, x=0.01,
            scale_gev=5.0,
            inputs={"coherent_shadowing": build_inclusive_gluon_shadowing_input()},
        )
        members["central"].append(result.total)
        for name, correction in result.uncertainty_corrections[
            "coherent_shadowing"
        ].items():
            members[name].append(result.impulse + correction)
    audit = audit_gluon_correlator_members(members)
    report = {
        "status": "pass" if audit.all_compatible else "reported tension; no clipping",
        "source": str(SOURCE),
        "x_N": 0.01, "Q_GeV": 5.0,
        "mechanism": "inclusive target-U/gluon-trace coherent shadowing",
        "members": [item.__dict__ for item in audit.members],
        "global_minimum_eigenvalue": audit.global_minimum_eigenvalue,
        "all_compatible": audit.all_compatible,
        "tensions_are_clipped": audit.tensions_are_clipped,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
