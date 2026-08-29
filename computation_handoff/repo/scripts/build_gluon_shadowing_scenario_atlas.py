#!/usr/bin/env python3
"""Plot irreducible polarized/tensor gluon-shadowing response scenarios."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

INPUT = Path(
    "outputs/parent_tmds/gluon_polarized_tensor_shadowing_scenarios.csv"
)
OUTPUT = Path("output/pdf/gluon_polarized_tensor_shadowing_atlas.pdf")
COMPONENTS = (
    ("trace_real", "gluon trace"),
    ("circular_real", "circular gluon polarization"),
    ("linear_norm", "linear-polarization norm"),
)
COLORS = {
    "spin_weak": "#4C78A8",
    "spin_central": "#163A5F",
    "spin_strong": "#D95F02",
}


def main() -> None:
    frame = pd.read_csv(INPUT)
    channels = list(frame.target_channel.drop_duplicates())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT) as pdf:
        for component, label in COMPONENTS:
            fig, axes = plt.subplots(
                3, 3, figsize=(10.5, 8.2), sharex=True, constrained_layout=True
            )
            for ax, channel in zip(axes.flat, channels):
                selected = frame.loc[frame.target_channel.eq(channel)]
                for scenario, curve in selected.groupby("scenario", sort=False):
                    ax.plot(
                        curve.k_GeV, curve[component],
                        color=COLORS[scenario], linewidth=1.8,
                        label=scenario.replace("_", " "),
                    )
                ax.axhline(0.0, color="0.4", linewidth=0.6)
                ax.set_title(channel)
                ax.grid(alpha=0.2)
            axes[0, 0].legend(frameon=False, fontsize=7.5)
            for ax in axes[-1]:
                ax.set_xlabel(r"$k_T$ [GeV]")
            for ax in axes[:, 0]:
                ax.set_ylabel(r"$\delta\Phi_g$ [GeV$^{-2}$]")
            fig.suptitle(
                f"AV18 coherent shadowing: {label}, $x_N=0.01$, $Q=5$ GeV"
            )
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
