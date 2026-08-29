#!/usr/bin/env python3
"""Plot the complete rank-resolved spin-1 gluon T-odd f/d boundary."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

INPUT = Path("outputs/parent_tmds/complete_gluon_todd_multiplet.csv")
OUTPUT = Path("output/pdf/complete_gluon_todd_multiplet_atlas.pdf")
COLORS = {
    "negative_d_endpoint": "#4C78A8",
    "central_midpoint": "#163A5F",
    "positive_d_endpoint": "#D95F02",
}
LINESTYLES = {
    "f_type_antisymmetric": "-",
    "d_type_symmetric": "--",
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    frame = frame.loc[frame.gauge_link.eq("[+,+]")]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for tmd, selected in frame.groupby("tmd", sort=False):
            fig, ax = plt.subplots(figsize=(8.0, 5.2), constrained_layout=True)
            for (scenario, color), curve in selected.groupby(
                ["scenario", "color_structure"], sort=False
            ):
                ax.plot(
                    curve.k_GeV,
                    curve["F_GeV-2"],
                    color=COLORS[scenario],
                    linestyle=LINESTYLES[color],
                    linewidth=2.0,
                    label=f"{scenario.replace('_', ' ')}, "
                    f"{color.split('_')[0]}-type",
                )
            ax.axhline(0.0, color="0.35", linewidth=0.7)
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x,k_T;Q)$ [GeV$^{-2}$]")
            ax.set_title(
                rf"Spin-1 gluon ${{{tmd}}}$: $f/d$ T-odd boundary, "
                r"$x_N=0.1$, $Q=5$ GeV"
            )
            ax.grid(alpha=0.2)
            ax.legend(frameon=False, fontsize=8, ncol=2)
            ax.text(
                0.99,
                0.02,
                "solid: antisymmetric f-type; dashed: symmetric d-type\n"
                "past-pointing link is the exact negative of curves shown",
                transform=ax.transAxes,
                ha="right",
                va="bottom",
                fontsize=7.5,
            )
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
