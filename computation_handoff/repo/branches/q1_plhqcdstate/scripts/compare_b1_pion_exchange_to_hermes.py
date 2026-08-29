#!/usr/bin/env python3
"""Propagate Miller tensor pions and JAM21 replicas to the HERMES b1 bins."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.polynomial.legendre import leggauss

from deuteron_wigner.data import load_hermes_b1
from deuteron_wigner.hidden_color import MillerSixQuarkB1
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerPionExchangeParameters,
    MillerTensorPionDistribution,
)

DATA = Path("data/processed/hermes_b1/table_ii.csv")
IMPULSE = Path("outputs/stage1/b1_av18_ct18nnlo.csv")
OUT = Path("outputs/figures/b1/b1_ia_pion_vs_hermes.csv")
MEMBERS = Path("outputs/figures/b1/b1_pion_jam21_members.csv")
FIGURE = Path("output/pdf/b1_ia_pion_vs_hermes.pdf")
VALIDATION = OUT.with_suffix(".validation.json")
N_JAM_MEMBERS = 786


def convolution_gauss(
    splitting: MillerTensorPionDistribution,
    pdf: JAM21IsoscalarPionPDF,
    x: float,
    q_gev: float,
    nodes: int = 160,
) -> float:
    points, weights = leggauss(nodes)
    y = x + (2.0 - x) * (points + 1.0) / 2.0
    kernel = np.asarray([splitting.delta_f(float(value)) for value in y]) / y
    pion = np.asarray(
        [pdf.value(2, float(x / value), q_gev) for value in y]
    )
    # Isoscalar pion exchange gives equal u,d,ubar,dbar. The LO charge sum
    # therefore reduces to b1=(5/9)*Delta_T u.
    return float(5.0 / 9.0 * (2.0 - x) / 2.0 * np.dot(weights, kernel * pion))


def main() -> None:
    hermes = load_hermes_b1(DATA)
    impulse = pd.read_csv(IMPULSE)
    if len(impulse) != len(hermes.x):
        raise RuntimeError("AV18 impulse table does not match HERMES bin count")
    central_splitting = MillerTensorPionDistribution()
    low_splitting = MillerTensorPionDistribution(
        parameters=MillerPionExchangeParameters(axial_mass_gev=0.99)
    )
    high_splitting = MillerTensorPionDistribution(
        parameters=MillerPionExchangeParameters(axial_mass_gev=1.07)
    )
    effective_q = np.maximum(np.sqrt(hermes.q2_gev2), 1.14)
    member_rows = []
    replica_values = []
    low_replica_values = []
    high_replica_values = []
    for member in range(N_JAM_MEMBERS):
        pion = JAM21IsoscalarPionPDF(member)
        values = np.asarray(
            [
                convolution_gauss(central_splitting, pion, x, q)
                for x, q in zip(hermes.x, effective_q)
            ]
        )
        low_values = np.asarray(
            [
                convolution_gauss(low_splitting, pion, x, q)
                for x, q in zip(hermes.x, effective_q)
            ]
        )
        high_values = np.asarray(
            [
                convolution_gauss(high_splitting, pion, x, q)
                for x, q in zip(hermes.x, effective_q)
            ]
        )
        replica_values.append(values)
        low_replica_values.append(low_values)
        high_replica_values.append(high_values)
        for index, value in enumerate(values):
            member_rows.append(
                {
                    "member": member,
                    "bin": index,
                    "x": hermes.x[index],
                    "Q2_GeV2": hermes.q2_gev2[index],
                    "Q_used_GeV": effective_q[index],
                    "b1_pion": value,
                }
            )
    replicas = np.asarray(replica_values)
    low_replicas = np.asarray(low_replica_values)
    high_replicas = np.asarray(high_replica_values)
    replica_mean = replicas.mean(axis=0)
    replica_std = replicas.std(axis=0, ddof=1)
    central = replica_mean
    low = low_replicas.mean(axis=0)
    high = high_replicas.mean(axis=0)
    ia = impulse["b1_IA"].to_numpy(dtype=float)
    total = ia + central
    fock_distribution = FockNormalizedMillerPionDistribution(central_splitting)
    fock_normalization = fock_distribution.normalization
    central_fock_normalized = fock_normalization * central
    total_fock_normalized = ia + central_fock_normalized
    six_quark_model = MillerSixQuarkB1()
    six_quark = np.asarray([six_quark_model.b1(float(x)) for x in hermes.x])
    total_with_six_quark = total + six_quark
    experimental_sigma = hermes.b1_total_uncertainty
    chi2_ia = float(np.sum(((ia - hermes.b1) / experimental_sigma) ** 2))
    chi2_total = float(np.sum(((total - hermes.b1) / experimental_sigma) ** 2))
    chi2_fock = float(
        np.sum(((total_fock_normalized - hermes.b1) / experimental_sigma) ** 2)
    )
    chi2_all = float(
        np.sum(((total_with_six_quark - hermes.b1) / experimental_sigma) ** 2)
    )
    output = pd.DataFrame(
        {
            "x": hermes.x,
            "Q2_GeV2": hermes.q2_gev2,
            "Q_used_GeV": effective_q,
            "Q_boundary_clamped": np.sqrt(hermes.q2_gev2) < 1.14,
            "b1_data": hermes.b1,
            "b1_stat": hermes.b1_stat,
            "b1_sys": hermes.b1_sys,
            "b1_impulse_av18": ia,
            "b1_pion_central": central,
            "b1_pion_replica_mean": replica_mean,
            "b1_pion_replica_std": replica_std,
            "b1_pion_MA099": low,
            "b1_pion_MA107": high,
            "b1_impulse_plus_pion": total,
            "fock_normalization_1_over_Z": fock_normalization,
            "b1_pion_fock_normalized": central_fock_normalized,
            "b1_impulse_plus_pion_fock_normalized": total_fock_normalized,
            "b1_six_quark": six_quark,
            "b1_impulse_plus_pion_plus_six_quark": total_with_six_quark,
        }
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(OUT, index=False)
    pd.DataFrame(member_rows).to_csv(MEMBERS, index=False)

    fig, axis = plt.subplots(figsize=(7.2, 4.8))
    order = np.argsort(hermes.x)
    x = hermes.x[order]
    axis.fill_between(
        x,
        (ia + replica_mean - replica_std)[order],
        (ia + replica_mean + replica_std)[order],
        color="tab:orange",
        alpha=0.25,
        label="JAM21 pion replica 1σ",
    )
    axial_low = np.minimum(low, high)
    axial_high = np.maximum(low, high)
    axis.fill_between(
        x,
        (ia + axial_low)[order],
        (ia + axial_high)[order],
        color="tab:red",
        alpha=0.18,
        label=r"$M_A=1.03\pm0.04$ GeV",
    )
    axis.plot(x, ia[order], "--", color="tab:blue", label="AV18 nucleon IA")
    axis.plot(
        x, total[order], "-", color="tab:red", label="AV18 IA + Sullivan pion"
    )
    axis.plot(
        x,
        total_with_six_quark[order],
        "-.",
        color="tab:purple",
        label="IA + pion + fitted six-quark scenario",
    )
    axis.errorbar(
        hermes.x,
        hermes.b1,
        yerr=experimental_sigma,
        fmt="o",
        color="black",
        capsize=3,
        label="HERMES",
    )
    axis.axhline(0.0, color="0.4", linewidth=0.8)
    axis.set_xscale("log")
    axis.set_xlabel(r"$x$")
    axis.set_ylabel(r"$b_1(x,Q^2)$")
    axis.legend(frameon=False, fontsize=8)
    axis.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIGURE)
    fig.savefig(FIGURE.with_suffix(".png"), dpi=220)
    plt.close(fig)

    quadrature_pdf = JAM21IsoscalarPionPDF(1)
    gauss_check = max(
        abs(
            convolution_gauss(central_splitting, quadrature_pdf, x, q, nodes=160)
            - convolution_gauss(central_splitting, quadrature_pdf, x, q, nodes=320)
        )
        for x, q in zip(hermes.x, effective_q)
    )
    report = {
        "status": "pass" if gauss_check < 2.0e-5 else "fail",
        "hermes_bins": len(hermes.x),
        "jam21_members": N_JAM_MEMBERS,
        "physical_replicas": N_JAM_MEMBERS,
        "central_definition": (
            "mean of all 786 members; every released file including member 0 "
            "is labeled PdfType: replica"
        ),
        "maximum_160_vs_320_y_quadrature_difference": gauss_check,
        "quadrature_acceptance": 2.0e-5,
        "chi2_experimental_only": {
            "impulse": chi2_ia,
            "impulse_plus_pion_central": chi2_total,
            "impulse_plus_fock_normalized_pion": chi2_fock,
            "impulse_plus_pion_plus_fitted_six_quark": chi2_all,
            "points": len(hermes.x),
            "note": "diagnostic only; theory covariance not included",
        },
        "boundary_clamped_bins": int(np.sum(output.Q_boundary_clamped)),
        "fock_normalization": {
            "Z": fock_distribution.ledger.z_factor,
            "one_over_Z": fock_normalization,
            "NN_probability": fock_distribution.ledger.nn_probability,
            "NNpi_probability": fock_distribution.ledger.pinn_probability,
            "NNpi_pion_momentum": (
                fock_distribution.ledger.pinn_sector_pion_momentum
            ),
            "NNpi_nucleon_momentum": (
                fock_distribution.ledger.pinn_sector_nucleon_momentum
            ),
            "momentum_closure": fock_distribution.ledger.total_momentum,
        },
        "boundary_policy": (
            "JAM21 Q minimum 1.14 GeV used for lower-Q HERMES bins; "
            "these rows are diagnostic extrapolation boundaries"
        ),
        "limitations": (
            "This observable is collinear. A separate Vpion19 boundary with "
            "nuclear recoil exists but is not used here. The six-quark curve "
            "is fitted at x=0.452 and is not a flavor-resolved correlator."
        ),
        "outputs": {
            "summary": str(OUT),
            "members": str(MEMBERS),
            "figure": str(FIGURE),
        },
    }
    VALIDATION.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
