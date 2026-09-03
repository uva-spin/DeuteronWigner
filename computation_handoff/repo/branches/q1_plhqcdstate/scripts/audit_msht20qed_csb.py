#!/usr/bin/env python3
"""Export and validate the paired MSHT20 QED neutron CSB input."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import quad

from deuteron_wigner.csb_inputs import MSHT20QEDChargeSymmetryBreaking


OUTPUT = Path("outputs/nucleon_inputs/msht20qed_csb_Q5.csv")
VALIDATION = OUTPUT.with_suffix(".validation.json")


def main() -> None:
    model = MSHT20QEDChargeSymmetryBreaking()
    configured = model.as_input()
    x_grid = np.unique(
        np.concatenate((np.geomspace(1.0e-4, 0.1, 80), np.linspace(0.1, 0.4, 80)))
    )
    rows = []
    for flavor in (2, 1, -2, -1):
        for x in x_grid:
            rows.append(
                {
                    "nucleon": "neutron",
                    "flavor": flavor,
                    "tmd": "f1",
                    "x": float(x),
                    "Q_GeV": 5.0,
                    "relative_correction": configured.relative_correction(
                        "neutron", flavor, "f1", float(x), 5.0
                    ),
                    "relative_uncertainty_68CL": configured.relative_uncertainty(
                        "neutron", flavor, "f1", float(x), 5.0
                    ),
                    "source": "MSHT20qed_nnlo / MSHT20qed_nnlo_neutron",
                }
            )
    table = pd.DataFrame(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUTPUT, index=False)

    proton = model._central_proton
    neutron = model._central_neutron

    def number(pdf, flavor: int, x: float) -> float:
        return float(pdf.xfxQ(flavor, x, 5.0) / x)

    valence_integrals = {}
    for nucleon_name, pdf in (("proton", proton), ("neutron", neutron)):
        for flavor in (2, 1):
            value = quad(
                lambda x: number(pdf, flavor, x) - number(pdf, -flavor, x),
                1.0e-6,
                1.0,
                epsabs=2.0e-5,
                epsrel=2.0e-5,
                limit=250,
                points=(1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2, 0.1),
            )[0]
            valence_integrals[f"{nucleon_name}_{flavor}"] = float(value)
    expected = {"proton_2": 2.0, "proton_1": 1.0, "neutron_2": 1.0, "neutron_1": 2.0}
    max_valence_residual = max(
        abs(valence_integrals[key] - target) for key, target in expected.items()
    )
    max_correction = float(table["relative_correction"].abs().max())
    max_uncertainty = float(table["relative_uncertainty_68CL"].max())
    valence_tolerance = 1.0e-2
    report = {
        "status": "pass" if max_valence_residual < valence_tolerance else "fail",
        "source_sets": {
            "proton": {"name": model.proton_set, "data_version": 2},
            "neutron": {"name": model.neutron_set, "data_version": 3},
        },
        "kinematics": {"Q_GeV": 5.0, "x_min": 1.0e-4, "x_max": 0.4},
        "scope": (
            "QED-induced neutron unpolarized f1 amplitude CSB only; "
            "polarized and transverse-profile CSB are not inferred"
        ),
        "hessian": {
            "confidence_level": 0.68,
            "paired_eigenvectors": model.n_eigenvector_pairs,
            "preserves_member_identity": True,
        },
        "max_absolute_relative_correction": max_correction,
        "max_absolute_relative_uncertainty": max_uncertainty,
        "valence_integrals": valence_integrals,
        "max_valence_number_residual": max_valence_residual,
        "valence_tolerance": valence_tolerance,
        "valence_note": (
            "tolerance includes LHAPDF interpolation and finite x>=1e-6 "
            "integration of the released grids"
        ),
        "table": str(OUTPUT),
    }
    VALIDATION.write_text(json.dumps(report, indent=2) + "\n")
    if report["status"] != "pass":
        raise SystemExit(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
