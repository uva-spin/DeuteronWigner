#!/usr/bin/env python3
"""Assemble retained-NN and native Vpion19 spin-averaged b-space terms."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nucleon", type=Path, required=True)
    parser.add_argument("--pion", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--figure", type=Path, required=True)
    args = parser.parse_args()
    nucleon = pd.read_csv(args.nucleon)
    pion = pd.read_csv(args.pion)
    b_axis = pion["b_GeV_inv"].to_numpy(float)
    rows = []
    for flavor, label in ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar")):
        source = nucleon[
            (nucleon["flavor"] == flavor) & (nucleon["tmd"] == "f1")
        ].sort_values("b_GeV-1")
        nn = np.interp(
            b_axis,
            source["b_GeV-1"].to_numpy(float),
            source["impulse_plus_nnpi_nucleon"].to_numpy(float),
        )
        impulse = np.interp(
            b_axis,
            source["b_GeV-1"].to_numpy(float),
            source["impulse"].to_numpy(float),
        )
        central_pion = pion["deuteron_pion_x0p1_central"].to_numpy(float)
        low_pion = pion["deuteron_pion_x0p1_replica_p16"].to_numpy(float)
        high_pion = pion["deuteron_pion_x0p1_replica_p84"].to_numpy(float)
        for index, b in enumerate(b_axis):
            rows.append({
                "flavor": flavor, "flavor_label": label,
                "x_N": 0.1, "Q_GeV": 5.0, "b_GeV-1": b,
                "impulse": impulse[index],
                "retained_nn_total": nn[index],
                "native_pion_central": central_pion[index],
                "native_pion_profile_p16": low_pion[index],
                "native_pion_profile_p84": high_pion[index],
                "combined_central": nn[index] + central_pion[index],
                "combined_profile_p16": nn[index] + low_pion[index],
                "combined_profile_p84": nn[index] + high_pion[index],
            })
    result = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False)
    fig, axes = plt.subplots(2, 4, figsize=(14.0, 6.5), sharex="col")
    for column, label in enumerate(("u", "d", "ubar", "dbar")):
        values = result[result["flavor_label"] == label]
        b = values["b_GeV-1"].to_numpy()
        axis = axes[0, column]
        axis.plot(b, values["impulse"], "--", color="0.4", label="impulse")
        axis.plot(
            b, values["retained_nn_total"], color="#c67a19",
            label="impulse + NNπ nucleons",
        )
        axis.plot(
            b, values["combined_central"], color="#1f5a94", lw=2.0,
            label="+ native pion",
        )
        axis.fill_between(
            b, values["combined_profile_p16"], values["combined_profile_p84"],
            color="#1f5a94", alpha=0.25,
        )
        axis.set_title(label)
        axis.grid(alpha=0.2)
        component_axis = axes[1, column]
        component_axis.plot(
            b, values["native_pion_central"], color="#1f5a94", lw=2.0,
            label="native pion",
        )
        component_axis.fill_between(
            b,
            values["native_pion_profile_p16"],
            values["native_pion_profile_p84"],
            color="#1f5a94",
            alpha=0.3,
            label="Vpion19 16–84%",
        )
        component_axis.grid(alpha=0.2)
        component_axis.set_xlabel(r"$b_T\;[\mathrm{GeV}^{-1}]$")
    axes[0, 0].legend(frameon=False, fontsize=8)
    axes[1, 0].legend(frameon=False, fontsize=8)
    axes[0, 0].set_ylabel(r"$\widetilde f_1(x_N=0.1,b_T,Q=5\,\mathrm{GeV})$")
    axes[1, 0].set_ylabel(r"$\widetilde f_1^{\,\pi}(x_N=0.1,b_T,Q=5\,\mathrm{GeV})$")
    fig.suptitle("Fock-consistent AV18 NNπ b-space scenario")
    fig.tight_layout()
    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.figure)
    fig.savefig(args.figure.with_suffix(".png"), dpi=180)
    plt.close(fig)
    validation = {
        "status": "pass" if np.all(np.isfinite(
            result.select_dtypes(include=[np.number]).to_numpy()
        )) else "fail",
        "nucleon_input": str(args.nucleon),
        "pion_input": str(args.pion),
        "composition": (
            "Fock-normalized retained NN plus NNpi nucleons, plus separately "
            "Fock-normalized native Vpion19 pion term"
        ),
        "uncertainty_shown": "Vpion19 physical-member q16/q84 profile only",
        "uncertainties_not_combined": (
            "JAM21 786-member collinear PDF ensemble, axial-mass variation, "
            "wave-function and unresolved three-body/off-forward uncertainty"
        ),
        "production_ready": False,
        "reason": "JAM21 substitution is not a Vpion19 refit; fixed-order Y term absent",
        "tensor_scope": (
            "f1 only; no sourced native tensor-pion TMD profile exists, so "
            "f1LL is not manufactured"
        ),
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(validation, indent=2) + "\n"
    )
    if validation["status"] != "pass":
        raise RuntimeError("non-finite combined NNpi b-space scenario")


if __name__ == "__main__":
    main()
