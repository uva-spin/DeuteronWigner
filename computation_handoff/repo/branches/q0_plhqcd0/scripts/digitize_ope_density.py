#!/usr/bin/env python3
"""Digitize the colored markers in Fig. 3 of Schiavilla et al. (2019).

Input is a 3x rasterization of ``ope_density.pdf`` from the public arXiv source
archive. Axis bounds and marker colors are fixed by that source figure.
"""

import csv
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.ndimage import label


COLORS = {
    "nvia_i1": ((255, 160, 0), 1),
    "nvia_i2": ((0, 220, 230), -1),
    "nvib_i1": ((255, 0, 255), 1),
    "nvib_i2": ((255, 0, 0), -1),
}
X_LEFT, X_RIGHT = 275.0, 2111.0
Y_TOP, Y_BOTTOM = 275.0, 1560.0


def main() -> None:
    source = Path("/tmp/ope-density.png")
    destination = Path("outputs/stage0/norfolk_ope_figure3_digitized.csv")
    image = np.asarray(Image.open(source).convert("RGB"))
    rows = []
    for curve, (color, sign) in COLORS.items():
        mask = np.linalg.norm(image - np.asarray(color), axis=2) < 80.0
        components, count = label(mask)
        for component in range(1, count + 1):
            y_pixels, x_pixels = np.where(components == component)
            if not 80 < len(x_pixels) < 500:
                continue
            x_pixel, y_pixel = x_pixels.mean(), y_pixels.mean()
            if not (280 < x_pixel < 2120 and 270 < y_pixel < 1570):
                continue
            radius = (x_pixel - X_LEFT) / (X_RIGHT - X_LEFT) * 5.0
            density = 0.03 - (y_pixel - Y_TOP) / (Y_BOTTOM - Y_TOP) * 0.06
            if 0.1 < radius < 5.05 and sign * density > -3.0e-4:
                rows.append(
                    {"curve": curve, "radius_fm": radius, "density_fm^-1": density}
                )
    rows.sort(key=lambda row: (row["curve"], row["radius_fm"]))
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
