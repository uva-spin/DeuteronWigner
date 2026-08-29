#!/usr/bin/env python3
"""Compute the retained-spin AV18 collinear gluon-helicity parent."""

import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_gluon_gtmd_wave_components,
    project_deuteron_gluon_target_channel,
    spin_half_collinear_gluon_correlator,
)
from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.pdfs import PolarizedLHAPDFProvider
from deuteron_wigner.moment_grids import ENDPOINT_AWARE_X as X
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC = 0.1973269804
M_N = 0.93891897
M_D = 1.87561294257
OUT = Path("outputs/parent_tmds/gluon_av18_helicity_moments_q5.csv")


def main() -> None:
    wave = select_momentum_wave_function("av18")
    quadrature = build_off_forward_component_quadratures(
        radial=wave.radial, nucleon_mass=M_N / HBARC, k_max=10.0,
        delta_x=0.0, delta_y=0.0, n_k=24, n_cos_theta=16, n_phi=12,
        deuteron_mass=M_D / HBARC,
    )
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)

    def proton(x, kx, ky, dx, dy, q):
        return spin_half_collinear_gluon_correlator(
            0.0, polarized.proton(21, x, q)
        )

    def neutron(x, kx, ky, dx, dy, q):
        return spin_half_collinear_gluon_correlator(
            0.0, polarized.neutron(21, x, q)
        )

    rows = []
    for x_n in X:
        components = convolve_gluon_gtmd_wave_components(
            x=float(x_n / 2.0), k_x=0.0, k_y=0.0, scale=5.0,
            proton_gtmd=proton, neutron_gtmd=neutron, quadratures=quadrature,
        )
        parent = sum(
            value[nucleon]
            for value in components.values()
            for nucleon in ("proton", "neutron")
        )
        phi_l = project_deuteron_gluon_target_channel(parent, "L")
        _, circular, _ = transverse_matrix_parts(phi_l)
        g1 = 2.0 * circular
        if abs(g1.imag) > 1.0e-11:
            raise ValueError("collinear gluon helicity projection is not real")
        rows.append({
            "wave_function": "av18", "pdf_set": "BDSSV24-NLO",
            "member": 0, "Q_GeV": 5.0, "x_N": float(x_n),
            "g1g_per_nucleon": float(0.25 * g1.real),
            "quadrature": "24x16x12",
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    OUT.with_suffix(".metadata.json").write_text(json.dumps({
        "status": "endpoint-aware retained-spin gluon-helicity parent",
        "classification": "phenomenological BDSSV24-NLO plus AV18 LF impulse convolution",
        "scale_GeV": 5.0,
        "x_grid": X.tolist(),
        "quadrature": {"n_k": 24, "n_cos": 16, "n_phi": 12, "k_max_fm_inverse": 10.0},
        "projection": "spin-1 target L coefficient, gluon circular antisymmetric trace",
        "normalization": "x_D=x_N/2 and 1/4 per-nucleon Jacobian",
        "uncertainty": "endpoint fit-window sensitivity stored by the moment audit",
    }, indent=2) + "\n")
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
