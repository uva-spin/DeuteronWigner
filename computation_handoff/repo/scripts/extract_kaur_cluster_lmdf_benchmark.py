#!/usr/bin/env python3
"""Extract the three vector paths from Fig. 2 of arXiv:2507.09886.

The official arXiv source includes ``pdfs.pdf`` as a vector figure.  This
extractor intentionally reads path coordinates rather than raster pixels.
The axis transform is reconstructed from the exact frame and zero-line
coordinates embedded in that PDF.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import fitz


CURVE_NAMES = ("z_f1", "z_g1L", "z_f1LL")
EXPECTED_COLORS = (
    (0.5000079870, 0.0, 0.5000079870),
    (0.7600060105, 0.6399940252, 0.1199970022),
    (0.3333329856, 0.3333329856, 0.3333329856),
)
X_ORIGIN = 61.00400161743164
X_POINTS_PER_UNIT = 500.0
Y_ZERO = 270.60198974609375
# Major y ticks are spaced by 40.984 PDF points per 0.2 units.
Y_POINTS_PER_UNIT = 204.92


def extract(input_pdf: Path, output_csv: Path) -> None:
    document = fitz.open(input_pdf)
    if document.page_count != 1:
        raise ValueError("expected the one-page source figure")
    drawings = document[0].get_drawings()
    curves = drawings[:3]
    if len(curves) != 3:
        raise ValueError("could not locate the three leading vector paths")
    extracted: list[list[tuple[float, float]]] = []
    for curve, expected_color in zip(curves, EXPECTED_COLORS):
        if max(abs(a - b) for a, b in zip(curve["color"], expected_color)) > 2e-6:
            raise ValueError("source curve colors or path ordering changed")
        items = curve["items"]
        if len(items) != 99 or any(item[0] != "l" for item in items):
            raise ValueError("expected each source curve to contain 99 line segments")
        points = [items[0][1], *(item[2] for item in items)]
        extracted.append(
            [
                (
                    (point.x - X_ORIGIN) / X_POINTS_PER_UNIT,
                    (Y_ZERO - point.y) / Y_POINTS_PER_UNIT,
                )
                for point in points
            ]
        )
    z_values = [point[0] for point in extracted[0]]
    for curve in extracted[1:]:
        if max(abs(z - point[0]) for z, point in zip(z_values, curve)) > 2e-6:
            raise ValueError("source paths do not share a common z grid")
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("z", *CURVE_NAMES))
        for index, z in enumerate(z_values):
            writer.writerow(
                (f"{z:.8f}", *(f"{curve[index][1]:.8f}" for curve in extracted))
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/benchmarks/kaur_2026_cluster_lmdf.csv"),
    )
    arguments = parser.parse_args()
    extract(arguments.input_pdf, arguments.output)


if __name__ == "__main__":
    main()
