#!/usr/bin/env python3
"""Audit screened-eikonal quadrature convergence for g1LT and g1TT."""

import json
from pathlib import Path

import numpy as np

from deuteron_wigner.axial_tensor_todd import (
    EikonalAxialTensorModel,
    EikonalKernelParameters,
)

OUTPUT = Path("outputs/validation/axial_tensor_eikonal_convergence.json")


def main() -> None:
    coarse = EikonalAxialTensorModel(
        kernel=EikonalKernelParameters(n_q=48, n_phi=56),
        d_state_probability=0.05759854074095002,
        sd_radial_coherence=0.3897991321351392,
    )
    fine = EikonalAxialTensorModel(
        kernel=EikonalKernelParameters(n_q=72, n_phi=88),
        d_state_probability=0.05759854074095002,
        sd_radial_coherence=0.3897991321351392,
    )
    residuals = []
    for flavor in (2, 1, -2, -1):
        for k in np.linspace(0.05, 0.9375, 20):
            left = coarse.future_values(
                flavor, f1_gev2=2.0, k_gev=float(k), width_gev2=0.32
            )
            right = fine.future_values(
                flavor, f1_gev2=2.0, k_gev=float(k), width_gev2=0.32
            )
            for a, b in zip(left, right):
                residuals.append(abs(a - b) / max(abs(b), 1.0e-15))
    maximum = float(max(residuals))
    report = {
        "schema_version": 1,
        "coarse": {"n_q": 48, "n_phi": 56},
        "fine": {"n_q": 72, "n_phi": 88},
        "flavors": [2, 1, -2, -1],
        "k_domain_GeV": [0.05, 0.9375],
        "maximum_relative_residual": maximum,
        "tolerance": 5.0e-5,
        "passes": maximum <= 5.0e-5,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not report["passes"]:
        raise SystemExit("eikonal quadrature convergence failed")


if __name__ == "__main__":
    main()
