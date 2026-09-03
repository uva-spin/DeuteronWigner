#!/usr/bin/env python3
"""Audit the spin-averaged Miller pion projection and JAM21 ensemble."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.polynomial.legendre import leggauss

from deuteron_wigner.pion_exchange import (
    JAM21IsoscalarPionPDF,
    MillerPionExchangeParameters,
    MillerTensorPionDistribution,
)

OUT = Path("outputs/figures/pion/spin_averaged_pion_jam21.csv")
MEMBERS = Path("outputs/figures/pion/spin_averaged_pion_jam21_members.csv")
REPORT = Path("outputs/figures/pion/spin_averaged_pion.validation.json")
N_MEMBERS = 786
X_GRID = np.geomspace(1.0e-3, 0.7, 16)
Q_GEV = 5.0


def convolve(
    splitting: MillerTensorPionDistribution,
    pdf: JAM21IsoscalarPionPDF,
    x: float,
    nodes: int = 120,
) -> float:
    points, weights = leggauss(nodes)
    y = x + (2.0 - x) * (points + 1.0) / 2.0
    kernel = np.asarray([splitting.spin_averaged_f(float(v)) for v in y]) / y
    pion = np.asarray([pdf.value(2, float(x / v), Q_GEV) for v in y])
    return float((2.0 - x) / 2.0 * np.dot(weights, kernel * pion))


def main() -> None:
    central_splitting = MillerTensorPionDistribution()
    low_splitting = MillerTensorPionDistribution(
        parameters=MillerPionExchangeParameters(axial_mass_gev=0.99)
    )
    high_splitting = MillerTensorPionDistribution(
        parameters=MillerPionExchangeParameters(axial_mass_gev=1.07)
    )
    rows = []
    values = []
    for member in range(N_MEMBERS):
        pdf = JAM21IsoscalarPionPDF(member)
        prediction = np.asarray(
            [convolve(central_splitting, pdf, float(x)) for x in X_GRID]
        )
        values.append(prediction)
        rows.extend(
            {"member": member, "x": x, "Q_GeV": Q_GEV, "f1_pion": value}
            for x, value in zip(X_GRID, prediction)
        )
    ensemble = np.asarray(values)
    reference_pdf = JAM21IsoscalarPionPDF(1)
    low = np.asarray([convolve(low_splitting, reference_pdf, float(x)) for x in X_GRID])
    high = np.asarray(
        [convolve(high_splitting, reference_pdf, float(x)) for x in X_GRID]
    )
    summary = pd.DataFrame(
        {
            "x": X_GRID,
            "Q_GeV": Q_GEV,
            "f1_pion_replica_mean": ensemble.mean(axis=0),
            "f1_pion_replica_std": ensemble.std(axis=0, ddof=1),
            "f1_pion_MA099_member1": low,
            "f1_pion_MA107_member1": high,
            "flavors": "u=d=ubar=dbar (isoscalar pion component only)",
        }
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUT, index=False)
    pd.DataFrame(rows).to_csv(MEMBERS, index=False)
    audit = central_splitting.momentum_audit()
    moments = central_splitting.spin_averaged_moments()
    check = max(
        abs(
            convolve(central_splitting, reference_pdf, float(x), nodes=120)
            - convolve(central_splitting, reference_pdf, float(x), nodes=240)
        )
        for x in X_GRID
    )
    report = {
        "status": "pass" if check < 2.0e-5 else "fail",
        "source": "Miller arXiv:1311.4561 spin average of published F_m",
        "jam21_members": N_MEMBERS,
        "central_definition": "mean of all 786 replicas",
        "maximum_120_vs_240_quadrature_difference": check,
        "pion_number_connected": moments["pion_number_connected"],
        "pion_deuteron_plus_momentum_fraction": audit.pion_fraction,
        "uncompensated_nucleon_plus_pion_total": audit.uncompensated_total,
        "required_nucleon_fraction_for_closure": audit.required_nucleon_fraction,
        "production_activation_default": "refuse until NN momentum policy acknowledged",
        "limitations": (
            "collinear spin-averaged connected pion component; no pion kT/GTMD "
            "profile and no universal nucleon rescaling is inferred"
        ),
        "outputs": {"summary": str(OUT), "members": str(MEMBERS)},
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
