#!/usr/bin/env python3
"""Plot unpolarized and tensor Wigner slices from a production NPZ file."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = np.load(args.input)
    b = data["b_gev_inverse"]
    k = data["k_gev"]
    wigner = data["wigner"]
    by0 = len(b) // 2
    ky0 = len(k) // 2
    sliced = wigner[:, by0, :, ky0]
    unpolarized = np.trace(sliced, axis1=-2, axis2=-1).real / 3.0
    tensor = (
        sliced[..., 1, 1] - 0.5 * (sliced[..., 0, 0] + sliced[..., 2, 2])
    ).real
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8), constrained_layout=True)
    extent = (k[0], k[-1], b[0], b[-1])
    first = axes[0].imshow(
        unpolarized, origin="lower", extent=extent, aspect="auto", cmap="viridis"
    )
    limit = float(np.max(np.abs(tensor)))
    second = axes[1].imshow(
        tensor, origin="lower", extent=extent, aspect="auto", cmap="coolwarm",
        norm=TwoSlopeNorm(vmin=-limit, vcenter=0.0, vmax=limit),
    )
    for axis, title in zip(axes, ("Unpolarized", "Tensor difference")):
        axis.set_title(title)
        axis.set_xlabel(r"$k_x$ [GeV]")
        axis.set_ylabel(r"$b_x$ [GeV$^{-1}$]")
    fig.colorbar(first, ax=axes[0], label=r"$\rho_U$")
    fig.colorbar(second, ax=axes[1], label=r"$\delta_T\rho$")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
