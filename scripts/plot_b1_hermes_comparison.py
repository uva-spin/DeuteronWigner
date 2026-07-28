#!/usr/bin/env python3
"""Plot the six-wave-function impulse b1 baseline against HERMES data."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = Path("data/processed/hermes_b1/table_ii.csv")
BAND = Path("outputs/uncertainty/b1_wave_function_band.csv")
OUTDIR = Path("outputs/figures/b1")
MODELS = {
    "AV18": Path("outputs/stage1/b1_av18_ct18nnlo.csv"),
    "CD-Bonn": Path("outputs/stage1/b1_cd_bonn_ct18nnlo.csv"),
    "NV2-Ia": Path("outputs/stage1/b1_nvia_ct18nnlo.csv"),
    "NV2-Ib": Path("outputs/stage1/b1_nvib_ct18nnlo.csv"),
    "NV2-IIa": Path("outputs/stage1/b1_nviia_ct18nnlo.csv"),
    "NV2-IIb": Path("outputs/stage1/b1_nviib_ct18nnlo.csv"),
}


def main() -> None:
    mpl.rcParams.update(
        {
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 11,
            "legend.fontsize": 8.5,
            "pdf.fonttype": 42,
        }
    )
    hermes = pd.read_csv(DATA)
    band = pd.read_csv(BAND)
    x = hermes["x"].to_numpy()
    error = np.hypot(hermes["b1_stat"], hermes["b1_sys"])

    fig, axes = plt.subplots(
        1, 2, figsize=(11.5, 4.8), sharex=True, constrained_layout=True
    )
    colors = plt.get_cmap("tab10").colors
    for ax in axes:
        ax.fill_between(
            band["x_table"].to_numpy(),
            band["b1_IA_min"].to_numpy(),
            band["b1_IA_max"].to_numpy(),
            color=colors[0],
            alpha=0.23,
            label="six-wave-function envelope",
            zorder=1,
        )
        ax.plot(
            band["x_table"],
            band["b1_IA_mean"],
            color=colors[0],
            linewidth=2.1,
            label="six-wave-function mean",
            zorder=2,
        )
        for index, (label, path) in enumerate(MODELS.items()):
            model = pd.read_csv(path)
            ax.plot(
                model["x_table"],
                model["b1_IA"],
                color=colors[(index + 1) % len(colors)],
                linewidth=1.0,
                alpha=0.72,
                label=label,
                zorder=2,
            )
        ax.errorbar(
            x,
            hermes["b1"],
            yerr=error,
            fmt="o",
            color="black",
            markerfacecolor="white",
            markeredgewidth=1.25,
            capsize=2.8,
            linewidth=1.0,
            label=r"HERMES (stat. $\oplus$ syst.)",
            zorder=4,
        )
        ax.axhline(0.0, color="0.35", linewidth=0.75)
        ax.axvspan(
            x[0] / 1.25,
            x[2] * 1.18,
            color="0.5",
            alpha=0.07,
            zorder=0,
        )
        ax.set_xscale("log")
        ax.set_xlim(0.009, 0.58)
        ax.set_xlabel(r"$x_N$")
        ax.grid(alpha=0.17, linewidth=0.55)
    axes[0].set_ylabel(r"$b_1^D(x_N,Q^2)$")
    axes[0].set_title("Full HERMES comparison")
    axes[0].legend(frameon=False, ncol=2, loc="upper right")
    axes[1].set_ylim(-0.0048, 0.0048)
    axes[1].set_title("Impulse-baseline scale")
    axes[1].text(
        0.011,
        -0.00435,
        "gray region: CT18 evaluated below its fitted $Q$ range",
        fontsize=8,
        color="0.3",
    )
    fig.suptitle(
        r"Deuteron $b_1$: leading-order impulse approximation vs. HERMES"
        "\nCT18NNLO shape input; AV18, CD-Bonn, and Norfolk wave functions",
        fontsize=12.5,
    )
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTDIR / "b1_ia_vs_hermes.pdf", bbox_inches="tight")
    fig.savefig(OUTDIR / "b1_ia_vs_hermes.png", dpi=240, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUTDIR / 'b1_ia_vs_hermes.pdf'}")


if __name__ == "__main__":
    main()
