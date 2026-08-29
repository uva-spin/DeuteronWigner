#!/usr/bin/env python3
"""Summarize AV18 fixed-k Wigner finite-grid convergence scans."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

FILES = {
    "baseline": "outputs/stage0/fixed_k_wigner_av18.npz",
    "kmax1p2": "outputs/convergence/wigner_av18_kmax1p2.npz",
    "kmax2p0": "outputs/convergence/wigner_av18_kmax2p0.npz",
    "ndelta7": "outputs/convergence/wigner_av18_ndelta7.npz",
    "ndelta13": "outputs/convergence/wigner_av18_ndelta13.npz",
    "dmax0p6": "outputs/convergence/wigner_av18_dmax0p6.npz",
    "dmax1p0": "outputs/convergence/wigner_av18_dmax1p0.npz",
    "dmax1p0_n11": "outputs/convergence/wigner_av18_dmax1p0_n11.npz",
    "dmax0p8_k8": "outputs/convergence/wigner_av18_dmax0p8_k8.npz",
    "dmax1p0_k8": "outputs/convergence/wigner_av18_dmax1p0_k8.npz",
    "dmax1p2_k8": "outputs/convergence/wigner_av18_dmax1p2_k8.npz",
    "dmax1p4_k8": "outputs/convergence/wigner_av18_dmax1p4_k8.npz",
    "dmax1p6_k8": "outputs/convergence/wigner_av18_dmax1p6_k8.npz",
}


def projection(matrix: np.ndarray) -> tuple[float, float]:
    unpolarized = np.trace(matrix).real / 3.0
    tensor = (matrix[1, 1] - 0.5 * (matrix[0, 0] + matrix[2, 2])).real
    return float(unpolarized), float(tensor)


def main() -> None:
    rows = []
    for label, filename in FILES.items():
        data = np.load(filename)
        k = data["k_gev"]
        delta = data["delta_gev"]
        b = data["b_gev_inverse"]
        ik = len(k) // 2
        ib = len(b) // 2
        gtmd_u, gtmd_t = projection(data["gtmd"][len(delta)//2, len(delta)//2, ik, ik])
        wigner_u, wigner_t = projection(data["wigner"][ib, ib, ik, ik])
        rows.append({
            "variant": label,
            "n_k": len(k),
            "k_max_GeV": float(k[-1]),
            "n_delta": len(delta),
            "delta_max_GeV": float(delta[-1]),
            "n_b": len(b),
            "b_max_GeV^-1": float(b[-1]),
            "internal_k_max_fm": float(data["internal_k_max_fm"]),
            "gtmd_k0_U": gtmd_u,
            "gtmd_k0_deltaT": gtmd_t,
            "wigner_b0_k0_U": wigner_u,
            "wigner_b0_k0_deltaT": wigner_t,
            "k_marginal_max_relative_error": float(
                data["gpd_k_grid_relative_error"]
            ),
            "hermiticity_max_error": float(data["delta_hermiticity_max_error"]),
        })
    baseline = next(row for row in rows if row["variant"] == "baseline")
    for row in rows:
        for observable in ("wigner_b0_k0_U", "wigner_b0_k0_deltaT"):
            row[f"{observable}_relative_to_baseline"] = (
                row[observable] / baseline[observable] - 1.0
            )
    destination = Path("outputs/convergence/wigner_av18_summary.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
