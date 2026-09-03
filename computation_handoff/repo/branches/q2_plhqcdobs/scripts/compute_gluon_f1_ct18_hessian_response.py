#!/usr/bin/env python3
"""Propagate CT18 Hessian gluon-density response through AV18 LF smearing."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.spin import project_matrix, spin_one_basis
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC = 0.1973269804
M_N = 0.93891897
X_VALUES = (0.02, 0.05, 0.10, 0.20, 0.40)
K_VALUES = np.linspace(0.0, 1.5, 61)
WIDTH_GEV2 = 1.0
OUT = Path("outputs/parent_tmds/ensemble/ct18_gluon_f1_hessian_response.csv")
REPORT = OUT.with_suffix(".validation.json")


def main() -> None:
    wave = select_momentum_wave_function("av18")
    quadrature = build_off_forward_spin_quadrature(
        radial=wave.radial, nucleon_mass=M_N/HBARC, k_max=10.0,
        delta_x=0.0, delta_y=0.0, n_k=16, n_cos_theta=12, n_phi=8,
    )
    identity = np.eye(2, dtype=complex)
    scalar = np.einsum(
        "nIHca,ac->nIH", quadrature.spectral, identity, optimize=True
    )
    u_channel = np.asarray([
        project_matrix(value, spin_one_basis()["U"]).real
        for value in scalar
    ])
    members = [LHAPDFProvider("CT18NNLO", member) for member in range(59)]
    rows = []
    for x_n in X_VALUES:
        x_d = x_n/2.0
        active = quadrature.y >= x_d
        y = quadrature.y[active]
        z = x_d/y
        weights = quadrature.weights[active]*u_channel[active]/y
        member_pdf = np.asarray([
            [provider.gluon(float(zz), 5.0) for zz in z]
            for provider in members
        ])
        for k in K_VALUES:
            parton_k2 = (
                k-z*HBARC*quadrature.p_x[active]
            )**2 + (
                z*HBARC*quadrature.p_y[active]
            )**2
            profile = np.exp(-parton_k2/WIDTH_GEV2)/(np.pi*WIDTH_GEV2)
            values = 0.5*np.einsum(
                "n,mn,n->m", weights, member_pdf, profile, optimize=True
            )
            sigma = float(np.sqrt(np.sum(
                ((values[1::2]-values[2::2])/2.0)**2
            )))
            rows.append({
                "species": "g", "tmd": "f1", "x_N": x_n,
                "Q_GeV": 5.0, "k_GeV": k,
                "response_central_GeV-2": float(values[0]),
                "hessian_sigma_GeV-2": sigma,
                "response_low_GeV-2": float(values[0]-sigma),
                "response_high_GeV-2": float(values[0]+sigma),
                "members": 59, "paired_eigenvectors": 29,
                "interpretation": (
                    "CT18 collinear Hessian response through AV18 LF "
                    "smearing; anchor deviations to evolved canonical central"
                ),
            })
    table = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUT, index=False)
    report = {
        "status": "pass",
        "rows": len(table), "x_N": list(X_VALUES),
        "k_points": len(K_VALUES), "paired_eigenvectors": 29,
        "central_scheme": (
            "response only; member deviations are to be anchored to the "
            "BSV19/NNPDF31 matched-CSS canonical central"
        ),
        "uncertainty_scope": (
            "CT18 collinear gluon Hessian plus exact AV18 LF smearing; "
            "matching/evolution/profile axes remain separately named"
        ),
    }
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
