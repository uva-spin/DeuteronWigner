#!/usr/bin/env python3
"""Audit correlated JAMDiFF h1 and WW h1Lperp members as full densities."""

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.quark_correlator import (
    compose_spin1_quark_correlator, quark_correlator_basis,
)
from deuteron_wigner.uncertainty_validation import (
    minimum_eigenvalues_under_correlated_replacements,
)

ROOT = Path("outputs/parent_tmds")
OUT = Path("outputs/validation/jamdiff_joint_positivity.json")
ROWS = Path("outputs/validation/jamdiff_joint_positivity.csv")
WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
M_D = 1.87561294257
TOLERANCE = 1.0e-10


def main() -> None:
    member_minima = np.full(968, np.inf)
    rows = []
    for wave in WAVES:
        parent = pd.read_csv(ROOT / f"quark_{wave}_fine.csv")
        parent = parent.loc[
            parent.gauge_link.eq("[+,+]")
            & parent.mechanism.isin(("impulse_total", "model_total"))
        ]
        h1_archive = np.load(
            ROOT / f"uncertainty/jamdiff_transversity_{wave}_fine.members.npz"
        )
        h1l_archive = np.load(
            ROOT / f"uncertainty/jamdiff_h1Lperp_{wave}_fine.members.npz"
        )
        for labels, group in parent.groupby(
            ["flavor", "flavor_label", "mechanism", "k_GeV"], sort=False
        ):
            flavor, flavor_label, mechanism, k = labels
            angle = float(group.azimuth_rad.iloc[0])
            momentum = (float(k) * np.cos(angle), float(k) * np.sin(angle))
            tmds = dict(zip(group.tmd, group["F_GeV-2"]))
            central = compose_spin1_quark_correlator(momentum, M_D, tmds)
            basis = quark_correlator_basis(momentum, M_D)
            key = f"{int(flavor)}_{float(k):.8f}_{mechanism}"
            minima = minimum_eigenvalues_under_correlated_replacements(
                central,
                {"h1": basis["h1"], "h1Lperp": basis["h1Lperp"]},
                {"h1": tmds["h1"], "h1Lperp": tmds["h1Lperp"]},
                {"h1": h1_archive[key], "h1Lperp": h1l_archive[key]},
            )
            member_minima = np.minimum(member_minima, minima)
            rows.append({
                "wave_function": wave, "flavor": int(flavor),
                "flavor_label": flavor_label, "mechanism": mechanism,
                "k_GeV": float(k), "minimum_member_eigenvalue": float(minima.min()),
                "violating_member_count": int(np.count_nonzero(minima < -TOLERANCE)),
                "worst_member": int(np.argmin(minima) + 1),
            })
    compatible = member_minima >= -TOLERANCE
    report = {
        "status": "pass" if compatible.all() else "reported tensions; no clipping",
        "members": 968,
        "components_replaced_together": ["h1", "h1Lperp"],
        "correlation": "common official JAMDiFF member identity, including WW transform",
        "scope": "six waves, four light flavors, impulse/model totals, nine k knots",
        "compatible_members": int(compatible.sum()),
        "violating_members": int((~compatible).sum()),
        "global_minimum_eigenvalue": float(member_minima.min()),
        "worst_member": int(np.argmin(member_minima) + 1),
        "tolerance": TOLERANCE,
        "tensions_are_clipped": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    pd.DataFrame(rows).to_csv(ROWS, index=False)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
