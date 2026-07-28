#!/usr/bin/env python3
"""Plot the complete spin-1 TMD prediction table at a representative slice."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


INPUT = Path("outputs/complete/spin1_tmd_phase_space.csv")
OUTDIR = Path("outputs/figures/complete_tmds")
CHANNELS = ("U", "L", "T", "LL", "LT", "TT")
COLORS = plt.get_cmap("tab10").colors


def label(name: str) -> str:
    rendered = name.replace("perpperp", r"^{\perp\perp}").replace("perp", r"^\perp")
    return f"${rendered}$"


def plot_species(data: pd.DataFrame, species: str, flavor: int, title: str, stem: str) -> None:
    selected = data[
        (data["species"] == species)
        & (data["flavor"] == flavor)
        & np.isclose(data["x_N"], 0.10)
        & np.isclose(data["Q_GeV"], 5.0)
        & (data["gauge_link"] == "future_SIDIS")
    ].copy()

    fig, axes = plt.subplots(2, 3, figsize=(13.5, 7.5), sharex=True, constrained_layout=True)
    for ax, channel in zip(axes.flat, CHANNELS):
        panel = selected[selected["target_channel"] == channel]
        for index, (name, group) in enumerate(panel.groupby("tmd", sort=False)):
            group = group.sort_values("k_GeV")
            color = COLORS[index % len(COLORS)]
            linestyle = "--" if bool(group["t_odd"].iloc[0]) else "-"
            ax.fill_between(
                group["k_GeV"],
                group["physical_ratio_lower95"],
                group["physical_ratio_upper95"],
                color=color,
                alpha=0.14,
                linewidth=0,
            )
            ax.plot(
                group["k_GeV"],
                group["physical_ratio_central"],
                color=color,
                linestyle=linestyle,
                linewidth=1.8,
                marker="o",
                markersize=3.2,
                label=label(name),
            )
        ax.axhline(0, color="0.45", linewidth=0.7)
        ax.set_title(channel)
        ax.grid(alpha=0.18, linewidth=0.6)
        ax.legend(frameon=False, fontsize=8, ncol=2, loc="best")
    for ax in axes[-1, :]:
        ax.set_xlabel(r"$k_T$ [GeV]")
    for ax in axes[:, 0]:
        ax.set_ylabel(r"physical ratio to $f_1$")
    fig.suptitle(
        rf"{title}: complete leading-twist spin-1 TMDs, $x=0.10$, $Q=5$ GeV (SIDIS)"
        "\nsolid: T-even; dashed: T-odd; shading: 95% interval",
        fontsize=13,
    )
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTDIR / f"{stem}.png", dpi=190, bbox_inches="tight")
    fig.savefig(OUTDIR / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


def plot_coverage() -> None:
    coverage = pd.read_csv("outputs/complete/spin1_tmd_predictive_coverage.csv")
    coverage["fully_sign_resolved"] = np.isclose(coverage["sign_resolved_fraction"], 1.0)
    grouped = (
        coverage.groupby(["species", "target_channel"], as_index=False)
        .agg(total=("tmd", "size"), resolved=("fully_sign_resolved", "sum"))
    )
    grouped["fraction"] = grouped["resolved"] / grouped["total"]
    fig, ax = plt.subplots(figsize=(9, 4.8), constrained_layout=True)
    labels, values = [], []
    for species, flavor_label in (("g", "gluon"), ("q", "quark"), ("qbar", "antiquark")):
        for channel in CHANNELS:
            row = grouped[(grouped.species == species) & (grouped.target_channel == channel)]
            labels.append(f"{flavor_label} {channel}")
            values.append(float(row.fraction.iloc[0]) if len(row) else 0.0)
    y = np.arange(len(labels))
    ax.barh(y, values, color=COLORS[0], alpha=0.8)
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 1.02)
    ax.set_xlabel("fraction of TMD functions with 95% band excluding zero")
    ax.grid(axis="x", alpha=0.2)
    ax.invert_yaxis()
    for yy, value in zip(y, values):
        ax.text(value + 0.012, yy, f"{value:.0%}", va="center", fontsize=8)
    ax.set_title("Predictive sign resolution by species and target-polarization sector")
    fig.savefig(OUTDIR / "predictive_coverage.png", dpi=190, bbox_inches="tight")
    fig.savefig(OUTDIR / "predictive_coverage.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    data = pd.read_csv(INPUT)
    plot_species(data, "g", 21, "Gluon", "gluon_tmd_ratios_x010_q5")
    plot_species(data, "q", 2, r"$u$ quark", "u_quark_tmd_ratios_x010_q5")
    plot_species(data, "qbar", -2, r"$\bar{u}$ antiquark", "ubar_tmd_ratios_x010_q5")
    plot_coverage()


if __name__ == "__main__":
    main()
