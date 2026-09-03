#!/usr/bin/env python3
"""Quantify why the finite-b W term is not a full collinear marginal."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import simpson


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("--collinear-validation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    frame = pd.read_csv(args.table)
    collinear = json.loads(args.collinear_validation.read_text())
    integrals = {}
    for name in ("f1", "f1LL"):
        selected = frame.loc[
            frame.mechanism.eq("impulse_total") & frame.tmd.eq(name)
        ].sort_values("k_GeV")
        integrals[name] = float(2.0 * np.pi * simpson(
            selected.k_GeV.to_numpy() * selected["F_GeV-2"].to_numpy(),
            x=selected.k_GeV.to_numpy(),
        ))
    targets = collinear["parent_b0"]
    residuals = {
        name: (integrals[name] - targets[name]) / targets[name]
        for name in integrals
    }
    report = {
        "status": "expected_incomplete_without_fixed_order_Y_term",
        "input": str(args.table),
        "k_domain_GeV": [
            float(frame.k_GeV.min()), float(frame.k_GeV.max()),
            int(frame.k_GeV.nunique()),
        ],
        "finite_b_W_term_integrals": integrals,
        "exact_b0_parent_limits": targets,
        "relative_residuals": residuals,
        "interpretation": (
            "The b=0 parent limit commutes with independent collinear LF "
            "smearing. A finite-b numerical W transform alone is not a "
            "full-k_T distribution: its integral is cutoff sensitive and "
            "requires the fixed-order Y term. These residuals must not be "
            "renormalized away or presented as a collinear sum-rule test."
        ),
        "production_action": (
            "retain the declared low-k_T domain and implement a sourced "
            "fixed-order Y term before claiming a full transverse marginal"
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
