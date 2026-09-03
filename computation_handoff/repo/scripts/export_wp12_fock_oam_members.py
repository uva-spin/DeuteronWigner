#!/usr/bin/env python3
"""Calibrate and export shared Fock/OAM correlated parent members."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.canonical_parent_enrichment import (
    FockResolvedNucleonBoundary,
    FockResolvedSpinHalfGluonBoundary,
    calibrate_shared_fock_oam_ledger,
)


QUARK = Path(
    "outputs/parent_tmds/wp12_multikinematic/quark_all_tmd_multix_q5.csv"
)
GLUON = Path(
    "outputs/parent_tmds/wp12_multikinematic/gluon_all_tmd_multix_q5.csv"
)
OUT = Path("outputs/parent_tmds/wp12_fock_oam_members.csv")
K_REF = 0.375
K = np.linspace(0.0, 1.2, 31)


def bounded(value: float) -> float:
    return float(np.clip(value, -0.35, 0.35))


def value(block: pd.DataFrame, name: str) -> float:
    return float(block.loc[block.tmd.eq(name), "F_GeV-2"].iloc[0])


def main() -> None:
    q = pd.read_csv(QUARK)
    rows = []
    widths = {2: 0.25, 1: 0.23, -2: 0.30, -1: 0.31}
    for x_n in sorted(q.x_N.unique()):
      qx = q.loc[
          q.mechanism.eq("model_total") & q.gauge_link.eq("[+,+]")
          & np.isclose(q.x_N, x_n)
      ]
      k_ref = float(qx.k_GeV.drop_duplicates().iloc[
          np.argmin(abs(qx.k_GeV.drop_duplicates().to_numpy()-K_REF))
      ])
      qx = qx.loc[np.isclose(qx.k_GeV, k_ref)]
      for flavor in (2, 1, -2, -1):
        block = qx.loc[qx.flavor.eq(flavor)]
        f1 = value(block, "f1")
        targets = {
            "rank1_even": bounded(
                0.5*(value(block, "g1T")-value(block, "h1Lperp"))/f1
            ),
            "rank1_odd": bounded(
                0.5*(value(block, "f1Tperp")-value(block, "h1perp"))/f1
            ),
            "rank2_even": bounded(value(block, "h1Tperp")/f1),
            "rank2_odd": bounded(
                0.5*(value(block, "g1TT")+value(block, "h1TT"))/f1
            ),
        }
        ledger, residual = calibrate_shared_fock_oam_ledger(targets)
        width = widths[flavor]
        density = max(0.0, f1*np.pi*width*np.exp(K_REF**2/width))
        boundary = FockResolvedNucleonBoundary(
            ledger, {flavor: density}, {flavor: width}
        )
        amplitudes = ";".join(
            f"{a.label}:{a.amplitude.real:.12g}{a.amplitude.imag:+.12g}j"
            for a in ledger.amplitudes
        )
        for sign, link in ((1, "[+,+]"), (-1, "[-,-]")):
            for k in K:
                for name, result in boundary.tmd_values(
                    flavor, float(k), 0.0, sign
                ).items():
                    rows.append({
                        "species": "quark" if flavor > 0 else "antiquark",
                        "flavor": flavor, "gauge_link": link,
                        "color_structure": "", "k_T_GeV": k,
                        "x_N": x_n, "Q_GeV": 5.0,
                        "tmd": name, "F_GeV-2": result,
                        "calibration_residual": residual,
                        "amplitudes": amplitudes,
                        "classification": "canonical-parent-ratio-informed correlated sensitivity",
                    })

    g = pd.read_csv(GLUON)
    for x_n in sorted(g.x_N.unique()):
      gx = g.loc[
          g.mechanism.eq("model_total")
          & g.color_structure.eq("f_type_antisymmetric")
          & g.gauge_link.eq("[+,+]") & np.isclose(g.x_N, x_n)
      ]
      gluon_k_ref = float(gx.k_GeV.drop_duplicates().iloc[
          np.argmin(abs(gx.k_GeV.drop_duplicates().to_numpy()-K_REF))
      ])
      gx = gx.loc[np.isclose(gx.k_GeV, gluon_k_ref)]
      gf1 = value(gx, "f1")
      targets = {
          "rank1_even": bounded(value(gx, "g1T")/gf1),
          "rank1_odd": bounded(
              0.5*(value(gx, "f1Tperp")+value(gx, "h1"))/gf1
          ),
          "rank2_even": bounded(value(gx, "h1perp")/gf1),
          "rank2_odd": bounded(value(gx, "h1Lperp")/gf1),
      }
      ledger, residual = calibrate_shared_fock_oam_ledger(targets)
      width = 0.30
      density = max(0.0, gf1*np.pi*width*np.exp(gluon_k_ref**2/width))
      boundary = FockResolvedSpinHalfGluonBoundary(ledger, density, width)
      amplitudes = ";".join(
          f"{a.label}:{a.amplitude.real:.12g}{a.amplitude.imag:+.12g}j"
          for a in ledger.amplitudes
      )
      for sign, link in ((1, "[+,+]"), (-1, "[-,-]")):
        for k in K:
            tensor = boundary.correlator(float(k), 0.0, sign)
            joint = tensor.transpose(0, 2, 1, 3).reshape(4, 4)
            for index, result in np.ndenumerate(tensor):
                rows.append({
                    "species": "gluon", "flavor": 21, "gauge_link": link,
                    "color_structure": "shared_fock_parent",
                    "k_T_GeV": k, "tmd": "parent_matrix",
                    "x_N": x_n, "Q_GeV": 5.0,
                    "F_GeV-2": float(result.real),
                    "imag": float(result.imag), "matrix_index": str(index),
                    "minimum_eigenvalue": float(np.linalg.eigvalsh(joint)[0]),
                    "calibration_residual": residual,
                    "amplitudes": amplitudes,
                    "classification": "canonical-parent-ratio-informed correlated sensitivity",
                })
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"{OUT}: {len(rows)} rows")


if __name__ == "__main__":
    main()
