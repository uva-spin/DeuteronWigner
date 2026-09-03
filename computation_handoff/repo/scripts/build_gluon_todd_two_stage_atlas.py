#!/usr/bin/env python3
"""Plot the source-informed six-function gluon T-odd prediction bands."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

INPUT = Path("outputs/parent_tmds/gluon_todd_two_stage_predictions.csv")
OUTPUT = Path("output/pdf/gluon_todd_two_stage_prediction_atlas.pdf")
NAMES = ("f1Tperp", "h1", "h1Lperp", "h1Tperp", "g1LT", "g1TT")
TEX = {
    "f1Tperp": r"$f_{1T}^{\perp g}$", "h1": r"$h_1^g$",
    "h1Lperp": r"$h_{1L}^{\perp g}$",
    "h1Tperp": r"$h_{1T}^{\perp g}$",
    "g1LT": r"$g_{1LT}^g$", "g1TT": r"$g_{1TT}^g$",
}


def main() -> None:
    data = pd.read_csv(INPUT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for color in data.color_structure.unique():
            future = "[+,+]" if color.startswith("f_") else "[+,-]"
            selected = data[
                data.color_structure.eq(color) & data.gauge_link.eq(future)
            ]
            fig, axes = plt.subplots(3, 2, figsize=(10.5, 12), sharex=True)
            for ax, name in zip(axes.flat, NAMES):
                block = selected[selected.tmd.eq(name)]
                pivot = block.pivot(index="k_GeV", columns="scenario", values="F_GeV-2")
                low, high = pivot.min(axis=1), pivot.max(axis=1)
                central_name = "spectator_full_vertex_av18_eikonal_central"
                ax.fill_between(pivot.index, low, high, alpha=.28, color="#2878b5")
                ax.plot(pivot.index, pivot[central_name], color="#174f78", lw=2)
                ax.axhline(0, color="0.25", lw=.7)
                ax.set_title(f"{TEX[name]}  [{name}]")
                ax.set_ylabel(r"$F(x,k_T;Q)$ [GeV$^{-2}$]")
                ax.grid(alpha=.2)
            for ax in axes[-1]:
                ax.set_xlabel(r"$k_T$ [GeV]")
            fig.suptitle(
                f"Spin-1 gluon T-odd prediction: {color}, {future}\n"
                r"$x_N=0.1,\ Q=5$ GeV; line=central, band=model scenarios",
                fontsize=13,
            )
            fig.tight_layout(rect=(0, 0, 1, .95))
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
