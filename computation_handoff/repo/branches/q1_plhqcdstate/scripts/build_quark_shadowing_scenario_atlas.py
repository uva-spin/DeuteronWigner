#!/usr/bin/env python3
"""Plot all quark polarized/tensor coherent-shadowing scenario corrections."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

INPUT = Path(
    "outputs/parent_tmds/quark_polarized_tensor_shadowing_scenarios.csv"
)
OUTPUT = Path("output/pdf/quark_polarized_tensor_shadowing_atlas.pdf")
FLAVORS = ("u", "d", "ubar", "dbar")
COLORS = {
    "spin_weak": "#4C78A8",
    "spin_central": "#163A5F",
    "spin_strong": "#D95F02",
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    frame = frame.loc[frame.gauge_link.eq("[+,+]")]
    # The rank-conditioned inverse projector becomes numerically ill
    # conditioned once the parent Gaussian is below practical resolution.
    # Preserve those rows in the audit table, but do not present the
    # k=1.3125--1.5 GeV inversion tail as physical shadowing structure.
    frame = frame.loc[frame.k_GeV.le(1.2)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for tmd, group in frame.groupby("tmd", sort=False):
            fig, axes = plt.subplots(
                2, 2, figsize=(9.0, 6.5), sharex=True, constrained_layout=True
            )
            for ax, flavor in zip(axes.flat, FLAVORS):
                selected = group.loc[group.flavor_label.eq(flavor)]
                for scenario, curve in selected.groupby("scenario", sort=False):
                    ax.plot(
                        curve.k_GeV, curve["F_GeV-2"],
                        color=COLORS[scenario], linewidth=1.8,
                        label=scenario.replace("_", " "),
                    )
                ax.axhline(0.0, color="0.4", linewidth=0.7)
                ax.set_title(flavor)
                ax.grid(alpha=0.2)
                if selected["F_GeV-2"].abs().max() == 0.0:
                    ax.set_ylim(-1.0, 1.0)
                    ax.text(
                        0.5, 0.5, "structural/numerical zero",
                        transform=ax.transAxes, ha="center", va="center",
                        fontsize=8, color="0.3",
                    )
            axes[0, 0].legend(frameon=False, fontsize=8)
            for ax in axes[-1]:
                ax.set_xlabel(r"$k_T$ [GeV]")
            for ax in axes[:, 0]:
                ax.set_ylabel(r"$\delta F$ [GeV$^{-2}$]")
            fig.suptitle(
                f"AV18 coherent quark shadowing: {tmd}, $x_N=0.01$, $Q=5$ GeV\n"
                r"display restricted to the numerically resolved $k_T\leq1.2$ GeV domain"
            )
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
