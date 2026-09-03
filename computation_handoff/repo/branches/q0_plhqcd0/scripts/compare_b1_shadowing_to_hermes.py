#!/usr/bin/env python3
"""Compare impulse and sourced coherent-shadowing sensitivity with HERMES b1."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from deuteron_wigner.nuclear_mechanisms import (
    NuclearCorrectionParameters,
    default_diffractive_shadowing_input,
    longitudinal_coherence_factor,
)

WAVES = ("av18", "cd_bonn", "nvia", "nvib", "nviia", "nviib")
OUT = Path("outputs/figures/b1")


def main() -> None:
    p = NuclearCorrectionParameters()
    diffractive = default_diffractive_shadowing_input()
    frames = []
    for wave in WAVES:
        frame = pd.read_csv(f"outputs/stage1/b1_{wave}_ct18nnlo.csv")
        frame["wave_function"] = wave
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True)
    q = np.sqrt(data.Q2_GeV2.to_numpy())
    coherence = np.asarray([
        longitudinal_coherence_factor(
            float(x), nucleon_mass_gev=p.nucleon_mass_gev,
            radius_fm=p.deuteron_coherence_radius_fm,
        )
        for x in data.x_table
    ])
    strength = np.asarray([
        diffractive.value("sea", float(x), float(scale))
        if x <= p.shadowing_x_max else 0.0
        for x, scale in zip(data.x_table, q)
    ]) * coherence
    tensor_ratio = p.tensor_shadowing_strength / p.shadowing_strength
    central_factor = 1.0 - tensor_ratio * strength
    data["b1_impulse_plus_shadowing"] = data.b1_IA * central_factor
    data["b1_shadowing_low"] = data.b1_IA * (
        1.0 - tensor_ratio * strength * (1.0 + diffractive.relative_uncertainty)
    )
    data["b1_shadowing_high"] = data.b1_IA * (
        1.0 - tensor_ratio * strength * (1.0 - diffractive.relative_uncertainty)
    )
    output = OUT / "b1_impulse_shadowing_vs_hermes.csv"
    OUT.mkdir(parents=True, exist_ok=True)
    data.to_csv(output, index=False)

    summary = data.groupby("x_table").agg(
        impulse_min=("b1_IA", "min"), impulse_max=("b1_IA", "max"),
        corrected_min=("b1_shadowing_low", "min"),
        corrected_max=("b1_shadowing_high", "max"),
        b1_data=("b1_data", "first"), stat=("stat", "first"), sys=("sys", "first"),
    ).reset_index()
    error = np.hypot(summary.stat, summary.sys)
    fig, ax = plt.subplots(figsize=(8.0, 5.2), constrained_layout=True)
    ax.fill_between(
        summary.x_table, summary.impulse_min, summary.impulse_max,
        alpha=0.25, label="six-wave impulse envelope",
    )
    ax.fill_between(
        summary.x_table, summary.corrected_min, summary.corrected_max,
        alpha=0.30, label="impulse + LT shadowing sensitivity",
    )
    ax.errorbar(
        summary.x_table, summary.b1_data, yerr=error, fmt="o",
        color="black", mfc="white", capsize=3,
        label=r"HERMES (stat. $\oplus$ syst.)",
    )
    ax.axhline(0.0, color="0.35", linewidth=0.7)
    ax.set_xscale("log")
    ax.set_xlabel(r"$x_N$")
    ax.set_ylabel(r"$b_1^D(x_N,Q^2)$")
    ax.set_title("Deuteron $b_1$: impulse and leading-twist shadowing sensitivity")
    ax.legend(frameon=False)
    ax.grid(alpha=0.2)
    fig.savefig(OUT / "b1_impulse_shadowing_vs_hermes.pdf")
    fig.savefig(OUT / "b1_impulse_shadowing_vs_hermes.png", dpi=220)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
