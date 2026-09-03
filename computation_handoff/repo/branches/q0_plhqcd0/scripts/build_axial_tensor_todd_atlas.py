#!/usr/bin/env python3
"""Plot smooth quark g1LT/g1TT results from both dynamical stages."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd

INPUT = Path("outputs/parent_tmds/quark_axial_tensor_todd_stages.csv")
OUTPUT = Path("output/pdf/quark_g1lt_g1tt_two_stage_atlas.pdf")
FLAVORS = ("u", "d", "ubar", "dbar")
CENTRAL = {
    "positivity_bounded_phase": "phase_central",
    "screened_one_gluon_rescattering": "screened_central",
}
LABELS = {
    "positivity_bounded_phase": "independent axial phase",
    "screened_one_gluon_rescattering": "screened one-gluon rescattering",
}
COLORS = {
    "positivity_bounded_phase": "#163A5F",
    "screened_one_gluon_rescattering": "#D95F02",
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    frame = frame.loc[
        frame.gauge_link.eq("[+,+]")
        & frame.tmd.isin(["g1LT", "g1TT"])
    ]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for tmd in ("g1LT", "g1TT"):
            for stage in CENTRAL:
                selected_stage = frame.loc[
                    frame.tmd.eq(tmd) & frame.stage.eq(stage)
                ]
                fig, axes = plt.subplots(
                    2, 2, figsize=(9.0, 6.7), sharex=True,
                    constrained_layout=True,
                )
                for ax, flavor in zip(axes.flat, FLAVORS):
                    selected = selected_stage.loc[
                        selected_stage.flavor_label.eq(flavor)
                    ]
                    pivot = selected.pivot(
                        index="k_GeV", columns="scenario", values="F_GeV-2"
                    ).sort_index()
                    central = pivot[CENTRAL[stage]]
                    low = pivot.min(axis=1)
                    high = pivot.max(axis=1)
                    ax.fill_between(
                        pivot.index, low, high, color=COLORS[stage],
                        alpha=0.22, linewidth=0.0, label="scenario envelope",
                    )
                    ax.plot(
                        pivot.index, central, color=COLORS[stage],
                        linewidth=2.2, label="central",
                    )
                    ax.axhline(0.0, color="0.35", linewidth=0.7)
                    ax.set_title(flavor)
                    ax.grid(alpha=0.2)
                axes[0, 0].legend(frameon=False, fontsize=8)
                for ax in axes[-1]:
                    ax.set_xlabel(r"$k_T$ [GeV]")
                for ax in axes[:, 0]:
                    ax.set_ylabel(r"$F(x,k_T;Q)$ [GeV$^{-2}$]")
                fig.suptitle(
                    rf"Quark ${tmd}$: {LABELS[stage]}, "
                    r"$x_N=0.1$, $Q=5$ GeV, AV18"
                    "\nFuture-pointing staple shown; past-pointing result "
                    "is its exact negative."
                )
                pdf.savefig(fig)
                plt.close(fig)

        # A logarithmic magnitude page makes the dynamical hierarchy visible
        # without disguising the signs shown on the four dimensional-F pages.
        fig, axes = plt.subplots(
            2, 2, figsize=(9.0, 6.7), sharex=True, constrained_layout=True
        )
        for ax, flavor in zip(axes.flat, FLAVORS):
            for stage in CENTRAL:
                selected = frame.loc[
                    frame.flavor_label.eq(flavor)
                    & frame.stage.eq(stage)
                    & frame.scenario.eq(CENTRAL[stage])
                ]
                for tmd, linestyle in (("g1LT", "-"), ("g1TT", "--")):
                    curve = selected.loc[selected.tmd.eq(tmd)]
                    mask = curve.k_GeV.gt(0)
                    ax.semilogy(
                        curve.loc[mask, "k_GeV"],
                        np.abs(curve.loc[mask, "F_GeV-2"]),
                        color=COLORS[stage], linestyle=linestyle,
                        linewidth=1.9,
                        label=f"{LABELS[stage]}, {tmd}",
                    )
            ax.set_title(flavor)
            ax.grid(alpha=0.2)
        axes[0, 0].legend(frameon=False, fontsize=7)
        for ax in axes[-1]:
            ax.set_xlabel(r"$k_T$ [GeV]")
        for ax in axes[:, 0]:
            ax.set_ylabel(r"$|F|$ [GeV$^{-2}$]")
        fig.suptitle(
            r"Central two-stage magnitude comparison, $x_N=0.1$, "
            r"$Q=5$ GeV, AV18"
        )
        pdf.savefig(fig)
        plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
