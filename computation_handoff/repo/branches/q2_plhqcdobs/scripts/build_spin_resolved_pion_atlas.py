#!/usr/bin/env python3
"""Plot source-supported spin-resolved Sullivan-pion TMDs."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

INPUT = Path("outputs/parent_tmds/spin_resolved_pion_tmds.csv")
OUTPUT = Path("output/pdf/spin_resolved_pion_tmd_atlas.pdf")


def main() -> None:
    frame = pd.read_csv(INPUT)
    selected = frame.loc[frame.zero_class.eq("nonzero_source_supported")]
    colors = {"u": "#1f77b4", "d": "#d62728", "ubar": "#17becf", "dbar": "#e377c2"}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for tmd, group in selected.groupby("tmd", sort=False):
            fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
            for flavor, curve in group.groupby("flavor_label", sort=False):
                ax.plot(
                    curve.k_GeV, curve["F_GeV-2"],
                    color=colors[flavor], linewidth=2.0, label=flavor,
                )
            ax.axhline(0.0, color="0.35", linewidth=0.7)
            ax.set_title(f"Fock-normalized Sullivan-pion {tmd}")
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x_N=0.1,k_T;Q=5\,\mathrm{GeV})$ [GeV$^{-2}$]")
            ax.grid(alpha=0.2)
            ax.legend(frameon=False, ncol=2)
            ax.text(
                0.99, 0.80,
                r"Miller recoil $\otimes$ JAM21 $\otimes$ Vpion19",
                transform=ax.transAxes, ha="right", va="top",
                fontsize=8.5, color="0.3",
            )
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
