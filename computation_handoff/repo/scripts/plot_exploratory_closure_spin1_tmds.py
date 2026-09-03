#!/usr/bin/env python3
"""Plot the superseded reduced-correlator closure/regression fixture.

These figures are deliberately segregated from parent-derived results.  A
smooth curve is not evidence of parent-correlator traceability.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

INPUT = Path("outputs/production_tmds/spin1_tmds_x010_q5.csv")
OUTDIR = Path("outputs/figures/exploratory_closure_tmds")
CHANNELS = ("U", "L", "T", "LL", "LT", "TT")
COMPONENTS = (
    "pdf",
    "wave_function",
    "transverse_profile",
    "evolution",
    "gauge_phase",
    "mechanism",
    "numerical",
)
COMPONENT_LABELS = {
    "pdf": "PDF/anchor normalization",
    "wave_function": "deuteron wave-function",
    "transverse_profile": "transverse-profile",
    "evolution": "evolution/broadening",
    "gauge_phase": "gauge-link phase",
    "mechanism": "correlator-mechanism",
    "numerical": "numerical",
}


def math_label(name: str) -> str:
    suffix = ""
    core = name
    if core.endswith("perpperp"):
        core = core[: -len("perpperp")]
        suffix = r"^{\perp\perp}"
    elif core.endswith("perp"):
        core = core[: -len("perp")]
        suffix = r"^\perp"
    symbol, subscript = core[0], core[1:]
    return rf"${symbol}_{{{subscript}}}{suffix}$"


def style() -> None:
    mpl.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 10,
            "legend.fontsize": 7.5,
            "lines.linewidth": 1.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def plot_atlas(
    data: pd.DataFrame,
    flavor_label: str,
    component: str | None,
) -> None:
    selected = data[
        (data["flavor_label"] == flavor_label)
        & (data["gauge_link"] == "future_SIDIS")
    ]
    fig, axes = plt.subplots(
        2, 3, figsize=(13.2, 7.4), sharex=True, constrained_layout=True
    )
    palette = plt.get_cmap("Dark2").colors
    for ax, channel in zip(axes.flat, CHANNELS):
        panel = selected[selected["target_channel"] == channel]
        for index, (name, group) in enumerate(panel.groupby("tmd", sort=False)):
            group = group.sort_values("k_GeV")
            color = palette[index % len(palette)]
            if component is not None:
                ax.fill_between(
                    group["k_GeV"].to_numpy(),
                    group[f"{component}_lower_GeV-2"].to_numpy(),
                    group[f"{component}_upper_GeV-2"].to_numpy(),
                    color=color,
                    alpha=0.19,
                    linewidth=0,
                )
            linestyle = "--" if bool(group["t_odd"].iloc[0]) else "-"
            ax.plot(
                group["k_GeV"],
                group["F_central_GeV-2"],
                color=color,
                linestyle=linestyle,
                label=math_label(name),
            )
        ax.axhline(0.0, color="0.35", linewidth=0.65)
        ax.set_title(channel)
        ax.grid(alpha=0.16, linewidth=0.55)
        ax.margins(x=0)
        ax.legend(frameon=False, ncol=2, loc="best")
    for ax in axes[-1]:
        ax.set_xlabel(r"$k_T\ \mathrm{[GeV]}$")
    for ax in axes[:, 0]:
        ax.set_ylabel(r"$F(x,k_T;Q)\ \mathrm{[GeV^{-2}]}$")
    band_text = (
        "SUPERSEDED exploratory reduced-correlator closure"
        if component is None
        else f"{COMPONENT_LABELS[component]} study band"
    )
    fig.suptitle(
        rf"{flavor_label}: complete leading-twist spin-1 TMDs, "
        rf"$x=0.10$, $Q=5\ \mathrm{{GeV}}$ (SIDIS)"
        f"\n{band_text}; dashed curves are T-odd",
        fontsize=12.5,
    )
    stem = "central" if component is None else component
    target = OUTDIR / flavor_label
    target.mkdir(parents=True, exist_ok=True)
    fig.savefig(target / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(target / f"{stem}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_ratio_diagnostic(data: pd.DataFrame, flavor_label: str) -> None:
    selected = data[
        (data["flavor_label"] == flavor_label)
        & (data["gauge_link"] == "future_SIDIS")
    ]
    fig, axes = plt.subplots(
        2, 3, figsize=(13.2, 7.4), sharex=True, constrained_layout=True
    )
    palette = plt.get_cmap("Dark2").colors
    for ax, channel in zip(axes.flat, CHANNELS):
        panel = selected[selected["target_channel"] == channel]
        for index, (name, group) in enumerate(panel.groupby("tmd", sort=False)):
            group = group.sort_values("k_GeV")
            ax.plot(
                group["k_GeV"],
                group["physical_ratio_central"],
                color=palette[index % len(palette)],
                linestyle="--" if bool(group["t_odd"].iloc[0]) else "-",
                label=math_label(name),
            )
        ax.axhline(0.0, color="0.35", linewidth=0.65)
        ax.set_title(channel)
        ax.grid(alpha=0.16, linewidth=0.55)
        ax.margins(x=0)
        ax.legend(frameon=False, ncol=2, loc="best")
    for ax in axes[-1]:
        ax.set_xlabel(r"$k_T\ \mathrm{[GeV]}$")
    for ax in axes[:, 0]:
        ax.set_ylabel(r"rank-weighted $F/f_1$")
    fig.suptitle(
        rf"{flavor_label}: supplemental physical-modulation ratios, "
        rf"$x=0.10$, $Q=5\ \mathrm{{GeV}}$ (SIDIS)",
        fontsize=12.5,
    )
    target = OUTDIR / flavor_label
    fig.savefig(target / "ratios.pdf", bbox_inches="tight")
    fig.savefig(target / "ratios.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    style()
    data = pd.read_csv(INPUT)
    for flavor_label in ("g", "u", "d", "ubar", "dbar"):
        plot_atlas(data, flavor_label, None)
        for component in COMPONENTS:
            plot_atlas(data, flavor_label, component)
        plot_ratio_diagnostic(data, flavor_label)
    print(f"Wrote superseded exploratory closure figures below {OUTDIR}")


if __name__ == "__main__":
    main()
