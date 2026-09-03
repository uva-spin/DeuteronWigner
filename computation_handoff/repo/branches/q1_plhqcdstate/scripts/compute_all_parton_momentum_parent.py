#!/usr/bin/env python3
"""Compute endpoint-aware AV18 collinear parents for the momentum sum rule."""

import csv
import json
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable, build_lf_smearing_spherical, impulse_convolution,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.moment_grids import ENDPOINT_AWARE_X as X
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC = 0.1973269804
M_N = 0.93891897
OUT = Path("outputs/parent_tmds/all_parton_av18_momentum_q5.csv")
def main() -> None:
    wave = select_momentum_wave_function("av18")
    smearing = build_lf_smearing_spherical(
        radial=wave.radial, nucleon_mass=M_N / HBARC, k_max=10.0,
        n_k=36, n_cos_theta=24, n_phi=16,
    )
    pdf = LHAPDFProvider("CT18NNLO", 0)
    rows = []
    for flavor in (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 21):
        for x in X:
            value = impulse_convolution(
                x=float(x), scale=5.0, flavor=flavor,
                proton_pdf=pdf.proton, neutron_pdf=pdf.neutron,
                smearing=smearing, scaling_variable=ScalingVariable.NUCLEON,
                per_nucleon=True,
            )
            rows.append({
                "wave_function": "av18", "pdf_set": "CT18NNLO",
                "member": 0, "Q_GeV": 5.0, "flavor": flavor,
                "species": "g" if flavor == 21 else ("q" if flavor > 0 else "qbar"),
                "x_N": float(x), "f1_per_nucleon": float(value),
                "smearing_norm": smearing.unpolarized_norm(),
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    OUT.with_suffix(".metadata.json").write_text(json.dumps({
        "status": "endpoint-aware parent input for global momentum audit",
        "classification": "phenomenological CT18NNLO plus AV18 impulse convolution",
        "scale_GeV": 5.0,
        "active_flavors": [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 21],
        "x_grid": X.tolist(),
        "quadrature": {"n_k": 36, "n_cos": 24, "n_phi": 16, "k_max_fm_inverse": 10.0},
        "normalization": "per nucleon; nucleon-mass Bjorken x",
        "uncertainty": "endpoint fit-window sensitivity stored by the moment audit",
    }, indent=2) + "\n")
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
