#!/usr/bin/env python3
"""Propagate exact retained-NN recoil through the AV18 LF b-space parent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import TabulatedQuarkCorrelatorProvider
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    MillerTensorPionDistribution,
    NNPiLongitudinalRecoilConvolution,
)
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.spin import diagonal_from_u_l_delta_t
from deuteron_wigner.tmd import (
    TransverseSmearingQuadrature,
    build_transverse_smearing_spherical,
    rank_zero_tmd_bspace,
)
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
FLAVORS = ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--b-max", type=float, default=5.0)
    parser.add_argument("--n-b", type=int, default=41)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    wave = select_momentum_wave_function("av18")
    smearing_fm = build_transverse_smearing_spherical(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=10.0,
        n_k=24,
        n_cos_theta=16,
        n_phi=12,
    )
    # Convert the retained transverse momenta to GeV so b is uniformly
    # represented in GeV^-1 in both the nucleon and Sullivan factors.
    smearing = TransverseSmearingQuadrature(
        y=smearing_fm.y,
        p_x=HBARC_GEV_FM * smearing_fm.p_x,
        p_y=HBARC_GEV_FM * smearing_fm.p_y,
        weights=smearing_fm.weights,
        unpolarized=smearing_fm.unpolarized,
        tensor=smearing_fm.tensor,
    )
    proton, neutron = build_nucleon_quark_models(
        LHAPDFProvider("CT18NNLO", 0),
        PolarizedLHAPDFProvider("BDSSV24-NLO", 0),
    )
    proton_b = MatchedRankZeroQuarkTMD(proton)
    neutron_b = MatchedRankZeroQuarkTMD(neutron)
    raw = MillerTensorPionDistribution()
    fock = FockNormalizedMillerPionDistribution(raw)
    recoil = NNPiLongitudinalRecoilConvolution(fock)
    parent_frame = pd.read_csv(args.parent)
    b_axis = np.linspace(0.0, args.b_max, args.n_b)
    rows = []
    b0_residuals = {}
    for flavor, label in FLAVORS:
        def nucleon_value(model, flavor, z, b, scale):
            return model.value("f1", flavor, z, b, scale).value

        def baseline(x_n: float, b: float) -> Spin1QuarkCorrelator:
            unpolarized = 0.25 * rank_zero_tmd_bspace(
                x=x_n / 2.0,
                scale=args.scale,
                flavor=flavor,
                b_x=b,
                b_y=0.0,
                proton_tmd=lambda f, z, coordinate, q: nucleon_value(
                    proton_b, f, z, coordinate, q
                ),
                neutron_tmd=lambda f, z, coordinate, q: nucleon_value(
                    neutron_b, f, z, coordinate, q
                ),
                smearing=smearing,
            ).real
            delta_t = 0.25 * rank_zero_tmd_bspace(
                x=x_n / 2.0,
                scale=args.scale,
                flavor=flavor,
                b_x=b,
                b_y=0.0,
                proton_tmd=lambda f, z, coordinate, q: nucleon_value(
                    proton_b, f, z, coordinate, q
                ),
                neutron_tmd=lambda f, z, coordinate, q: nucleon_value(
                    neutron_b, f, z, coordinate, q
                ),
                smearing=smearing,
                tensor=True,
            ).real
            vector = diagonal_from_u_l_delta_t(
                unpolarized, 0.0, delta_t
            ).values
            return Spin1QuarkCorrelator(
                vector,
                np.zeros((3, 3), dtype=complex),
                np.zeros((2, 3, 3), dtype=complex),
            )

        for b in b_axis:
            base = baseline(args.x_n, float(b))
            correction = recoil.nucleon_correction_b(
                baseline, args.x_n, float(b)
            )
            total = Spin1QuarkCorrelator(
                base.vector + correction.vector,
                base.axial + correction.axial,
                base.transverse + correction.transverse,
            )
            base_p = project_spin1_quark_correlator_at_origin(base, M_D_GEV)
            total_p = project_spin1_quark_correlator_at_origin(total, M_D_GEV)
            for tmd in ("f1", "f1LL"):
                rows.append({
                    "flavor": flavor, "flavor_label": label,
                    "x_N": args.x_n, "Q_GeV": args.scale,
                    "b_GeV-1": float(b), "tmd": tmd,
                    "impulse": base_p[tmd],
                    "impulse_plus_nnpi_nucleon": total_p[tmd],
                    "nnpi_nucleon_correction": total_p[tmd] - base_p[tmd],
                })
        stored = parent_frame[
            (parent_frame["flavor"] == flavor)
            & (parent_frame["mechanism"] == "impulse_total")
            & (parent_frame["gauge_link"] == "[collinear,T-even]")
        ]
        sector = "valence" if flavor > 0 else "sea"
        provider = TabulatedQuarkCorrelatorProvider.from_frame(
            stored, scale_gev=args.scale, parton_sector=sector
        )
        direct_base = provider(args.x_n, args.scale, sector)
        direct_correction = recoil.nucleon_correction(
            lambda shifted_x: provider(shifted_x, args.scale, sector),
            args.x_n,
        )
        expected_projection = project_spin1_quark_correlator_at_origin(
            Spin1QuarkCorrelator(
                direct_base.vector + direct_correction.vector,
                direct_base.axial + direct_correction.axial,
                direct_base.transverse + direct_correction.transverse,
            ),
            M_D_GEV,
        )
        expected = {
            tmd: expected_projection[tmd] for tmd in ("f1", "f1LL")
        }
        at_zero = pd.DataFrame(rows)
        at_zero = at_zero[
            (at_zero["flavor"] == flavor) & (at_zero["b_GeV-1"] == 0.0)
        ]
        b0_residuals[label] = {
            tmd: float(
                at_zero[at_zero["tmd"] == tmd][
                    "impulse_plus_nnpi_nucleon"
                ].iloc[0] - expected[tmd]
            )
            for tmd in ("f1", "f1LL")
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, index=False)
    max_b0 = max(abs(v) for values in b0_residuals.values() for v in values.values())
    report = {
        "status": "pass" if max_b0 < 2.0e-3 else "fail",
        "x_N": args.x_n,
        "Q_GeV": args.scale,
        "quadrature": "AV18 24x16x12",
        "b_unit": "GeV^-1",
        "b0_residuals_against_collinear_conditional_parent": b0_residuals,
        "max_b0_absolute_residual": max_b0,
        "bessel_argument": "x_N*b*qT/[2*(1-eta_pi)]",
        "scope": "retained-NN f1/f1LL recoil; pion-internal b-space term separate",
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    if report["status"] != "pass":
        raise RuntimeError(f"NNpi b-space validation failed: {report}")


if __name__ == "__main__":
    main()
