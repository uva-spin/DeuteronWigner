#!/usr/bin/env python3
"""Compare fit-informed and explicit LF-OAM AV18 parent scenarios."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

FIT = Path("outputs/parent_tmds/quark_av18_rich_medium.csv")
OAM = Path("outputs/parent_tmds/quark_av18_oam_medium.csv")
OUTPUT = Path("output/pdf/quark_oam_parent_scenario_comparison.pdf")
TMDS = ("f1Tperp", "h1perp", "g1T", "h1Lperp", "h1Tperp")
FLAVORS = ("u", "d", "ubar", "dbar")


def select(frame: pd.DataFrame, tmd: str, flavor: str) -> pd.DataFrame:
    return frame.loc[
        frame.mechanism.eq("model_total")
        & frame.gauge_link.eq("[+,+]")
        & frame.tmd.eq(tmd)
        & frame.flavor_label.eq(flavor)
    ].sort_values("k_GeV")


def main() -> None:
    fitted = pd.read_csv(FIT)
    oam = pd.read_csv(OAM)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for tmd in TMDS:
            fig, axes = plt.subplots(
                2, 2, figsize=(9.0, 6.5), sharex=True, constrained_layout=True
            )
            for ax, flavor in zip(axes.flat, FLAVORS):
                fit_curve = select(fitted, tmd, flavor)
                oam_curve = select(oam, tmd, flavor)
                ax.plot(
                    fit_curve.k_GeV, fit_curve["F_GeV-2"],
                    color="#163A5F", linewidth=2.0, label="fit-informed central",
                )
                ax.plot(
                    oam_curve.k_GeV, oam_curve["F_GeV-2"],
                    color="#D95F02", linewidth=1.8, linestyle="--",
                    label="explicit S/P/D OAM scenario",
                )
                ax.axhline(0.0, color="0.4", linewidth=0.7)
                ax.set_title(flavor)
                ax.grid(alpha=0.2)
            axes[1, 0].set_xlabel(r"$k_T$ [GeV]")
            axes[1, 1].set_xlabel(r"$k_T$ [GeV]")
            axes[0, 0].set_ylabel(r"$F$ [GeV$^{-2}$]")
            axes[1, 0].set_ylabel(r"$F$ [GeV$^{-2}$]")
            axes[0, 0].legend(frameon=False, fontsize=8)
            fig.suptitle(
                f"AV18 parent: {tmd} at $x_N=0.1$, $Q=5$ GeV (future link)"
            )
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
