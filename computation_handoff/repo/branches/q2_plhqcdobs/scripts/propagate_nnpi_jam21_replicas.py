#!/usr/bin/env python3
"""Propagate all JAM21 pion replicas through the refined NNpi parent model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.polynomial.legendre import leggauss

from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
    SpinAveragedPionConvolution,
    TensorPionConvolution,
)

FLAVORS = ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar"))
N_MEMBERS = 786


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comparison", type=Path, required=True)
    parser.add_argument("--bands", type=Path, required=True)
    parser.add_argument("--members", type=Path, required=True)
    parser.add_argument("--nodes", type=int, default=160)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    comparison = pd.read_csv(args.comparison)
    x_axis = np.sort(comparison["x_N"].unique())
    scales = comparison["Q_GeV"].unique()
    if scales.size != 1 or args.nodes < 64:
        raise ValueError("one scale and at least 64 quadrature nodes are required")
    scale = float(scales[0])
    raw = MillerTensorPionDistribution()
    fock = FockNormalizedMillerPionDistribution(raw)
    nodes, weights = leggauss(args.nodes)
    quadratures = []
    for x in x_axis:
        y = x + (2.0 - x) * (nodes + 1.0) / 2.0
        jacobian = (2.0 - x) / 2.0
        quadratures.append({
            "z": x / y,
            "spin_average": (
                jacobian * weights
                * np.asarray([fock.spin_averaged_f(float(v)) for v in y])
                / y
            ),
            "tensor": (
                jacobian * weights
                * np.asarray([fock.delta_f(float(v)) for v in y])
                / y
            ),
        })
    pion_f1 = np.empty((N_MEMBERS, x_axis.size))
    pion_f1ll = np.empty_like(pion_f1)
    for member in range(N_MEMBERS):
        pdf = JAM21IsoscalarPionPDF(member)
        for ix, quadrature in enumerate(quadratures):
            values = np.asarray([
                pdf.value(2, float(z), scale) for z in quadrature["z"]
            ])
            pion_f1[member, ix] = np.dot(
                quadrature["spin_average"], values
            )
            pion_f1ll[member, ix] = -2.0 / 3.0 * np.dot(
                quadrature["tensor"], values
            )
        if member % 50 == 0:
            print(f"JAM21 member {member}/{N_MEMBERS - 1}", flush=True)

    # Validate the fixed-node propagation against the adaptive production
    # convolution for the explicitly stored member-0 comparison.
    member0 = JAM21IsoscalarPionPDF(0)
    adaptive_f1 = SpinAveragedPionConvolution(fock, member0)
    adaptive_tensor = TensorPionConvolution(fock, member0)
    exact_f1 = np.asarray([adaptive_f1.f1(2, x, scale) for x in x_axis])
    exact_f1ll = np.asarray([
        adaptive_tensor.f1ll(2, x, scale) for x in x_axis
    ])
    fixed_residual = {
        "f1_max_abs": float(np.max(np.abs(pion_f1[0] - exact_f1))),
        "f1_max_relative": float(np.max(
            np.abs(pion_f1[0] - exact_f1) / np.maximum(np.abs(exact_f1), 1e-12)
        )),
        "f1LL_max_abs": float(np.max(np.abs(pion_f1ll[0] - exact_f1ll))),
        "f1LL_max_relative": float(np.max(
            np.abs(pion_f1ll[0] - exact_f1ll)
            / np.maximum(np.abs(exact_f1ll), 1e-12)
        )),
    }
    member_rows: list[dict[str, object]] = []
    band_rows: list[dict[str, object]] = []
    for flavor, label in FLAVORS:
        source = comparison[comparison["flavor"] == flavor]
        for tmd in ("f1", "g1", "h1", "f1LL", "h1LT"):
            tmd_source = source[source["tmd"] == tmd].sort_values("x_N")
            stored = tmd_source["conditional_recoil"].to_numpy(float)
            if tmd == "f1":
                values = stored[None, :] - exact_f1[None, :] + pion_f1
            elif tmd == "f1LL":
                values = stored[None, :] - exact_f1ll[None, :] + pion_f1ll
            else:
                values = np.broadcast_to(stored, (N_MEMBERS, x_axis.size))
            mean = np.mean(values, axis=0)
            std = np.std(values, axis=0, ddof=1)
            low, high = np.quantile(values, (0.16, 0.84), axis=0)
            for ix, x in enumerate(x_axis):
                band_rows.append({
                    "flavor": flavor, "flavor_label": label, "x_N": x,
                    "Q_GeV": scale, "tmd": tmd,
                    "jam21_replica_mean": mean[ix],
                    "jam21_replica_std": std[ix],
                    "jam21_q16": low[ix], "jam21_q84": high[ix],
                    "member0": values[0, ix],
                    "n_replicas": N_MEMBERS,
                })
                for member in range(N_MEMBERS):
                    member_rows.append({
                        "member": member, "flavor": flavor,
                        "flavor_label": label, "x_N": x, "Q_GeV": scale,
                        "tmd": tmd, "conditional_recoil": values[member, ix],
                    })
    args.bands.parent.mkdir(parents=True, exist_ok=True)
    args.members.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(band_rows).to_csv(args.bands, index=False)
    pd.DataFrame(member_rows).to_csv(args.members, index=False)
    report = {
        "status": "pass" if (
            fixed_residual["f1_max_relative"] < 2.0e-3
            and fixed_residual["f1LL_max_relative"] < 2.0e-3
        ) else "fail",
        "input": str(args.comparison),
        "n_replicas": N_MEMBERS,
        "central_definition": "mean of all released replicas",
        "spread_definition": "sample standard deviation; q16/q84 also stored",
        "fixed_gauss_nodes": args.nodes,
        "member0_fixed_vs_adaptive": fixed_residual,
        "replica_independent_tmds": ["g1", "h1", "h1LT"],
        "replica_dependent_tmds": ["f1", "f1LL"],
    }
    args.bands.with_suffix(".validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    if report["status"] != "pass":
        raise RuntimeError(f"JAM21 propagation validation failed: {report}")


if __name__ == "__main__":
    main()
