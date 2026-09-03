#!/usr/bin/env python3
"""Build the machine-readable acceptance audit for WP12 items 1--5."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import deserialize_gluon_correlator
from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/validation/wp12_items1_5_acceptance.json"
X = {0.02, 0.05, 0.10, 0.20, 0.40}


def load(path: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(ROOT / path, low_memory=False, **kwargs)


def xset(frame: pd.DataFrame) -> set[float]:
    return set(frame.x_N.round(2))


def main() -> None:
    qr = json.loads((ROOT / "outputs/validation/wp12_quark_multix.json").read_text())
    gr = json.loads((ROOT / "outputs/validation/wp12_gluon_multix.json").read_text())
    q = load("outputs/parent_tmds/wp12_multikinematic/quark_all_tmd_multix_q5.csv")
    g = load("outputs/parent_tmds/wp12_multikinematic/gluon_all_tmd_multix_q5.csv")
    wp = load("outputs/parent_tmds/wp12_wilson_projected_members.csv")
    wc = load("outputs/parent_tmds/wp12_wilson_channel_members.csv",
              keep_default_na=False)
    fo = load("outputs/parent_tmds/wp12_fock_oam_members.csv",
              keep_default_na=False)
    nn = load("outputs/parent_tmds/wp12_nonnucleonic_transverse.csv",
              keep_default_na=False)
    rr = json.loads(
        (ROOT / "outputs/validation/wp12_operator_response.json").read_text()
    )
    response = load(
        "outputs/parent_tmds/wp12_operator_response_members.correlators.csv"
    )
    qmodel = q[q.mechanism.eq("model_total")]
    gmodel = g[g.mechanism.eq("model_total")]
    gmatrix_paths = [
        ROOT / f"outputs/parent_tmds/wp12_multikinematic/gluon_x{x}_q5.correlators.csv"
        for x in ("002", "005", "020", "040")
    ] + [
        ROOT / "outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.correlators.csv"
    ]
    g_minima = []
    for path in gmatrix_paths:
        matrix = pd.read_csv(path)
        matrix = matrix[matrix.mechanism.eq("model_total")]
        keys = [
            "color_structure", "gauge_link", "x_N", "Q_GeV",
            "k_GeV", "azimuth_rad",
        ]
        for _, block in matrix.groupby(keys, sort=False):
            g_minima.append(
                Spin1GluonCorrelator(
                    deserialize_gluon_correlator(block)
                ).minimum_positivity_eigenvalue()
            )
    gf = gmodel[gmodel.gauge_link.isin(["[+,+]", "[+,-]"])].copy()
    gp = gmodel[gmodel.gauge_link.isin(["[-,-]", "[-,+]"])].copy()
    gf["pair"] = gf.gauge_link.map({"[+,+]": "same", "[+,-]": "mixed"})
    gp["pair"] = gp.gauge_link.map({"[-,-]": "same", "[-,+]": "mixed"})
    link_keys = [
        "color_structure", "pair", "x_N", "Q_GeV", "k_GeV", "tmd"
    ]
    paired = gf.merge(gp, on=link_keys, suffixes=("_f", "_p"))
    gluon_link_residual = float(np.max(np.abs(
        paired["F_GeV-2_f"]
        - (1.0-2.0*paired["t_odd_f"])*paired["F_GeV-2_p"]
    )))

    c1 = (
        qr["status"] == gr["status"] == "pass"
        and xset(qmodel) == xset(gmodel) == X
        and qmodel.tmd.nunique() == gmodel.tmd.nunique() == 18
        and set(qmodel.flavor) == {-2, -1, 1, 2}
        and np.isfinite(qmodel["F_GeV-2"]).all()
        and np.isfinite(gmodel["F_GeV-2"]).all()
        and xset(wp) == X
        and wp[wp.species.ne("g")].tmd.nunique() == 18
        and wp[wp.species.eq("g")].tmd.nunique() == 18
    )
    c2 = (
        set(wc.member) == {"soft", "central", "strong"}
        and xset(wc) == X
        and set(wc[wc.sector.ne("gluon")].channel) == {"S_P", "S_D", "P_P"}
        and set(wc[wc.sector.eq("gluon")].channel)
        == {"S_D_rank1", "D_D_rank2"}
        and set(wp.member) == {"soft", "central", "strong"}
    )
    c3 = (
        xset(fo) == X
        and set(fo[fo.species.ne("gluon")].flavor) == {-2, -1, 1, 2}
        and fo.calibration_residual.max() < 0.08
        and pd.to_numeric(
            fo.loc[fo.species.eq("gluon"), "minimum_eigenvalue"]
        ).min() >= -1e-12
    )
    c4 = (
        xset(nn) == X
        and set(nn.sector) == {
            "NNpi", "DeltaDelta", "hidden_color_6q", "short_range_NN"
        }
        and set(nn.species) == {"quark", "antiquark", "gluon"}
        and nn[nn.member.eq("central")]["F_GeV-2"].eq(0).all()
        and nn[nn.member.eq("sensitivity")]["canonical_weight"].gt(0).all()
    )
    c5 = (
        rr["status"] == "pass"
        and xset(response) == X
        and set(response.response_member) == {"weak", "central", "strong"}
        and set(response.sector) == {"q", "qbar", "g"}
        and rr["minimum_mapped_parent_eigenvalue"] >= -1e-10
        and rr["maximum_chain_closure_residual"] < 1e-10
    )
    criteria = {
        "all_tmd_multikinematic": bool(c1),
        "channel_wilson": bool(c2),
        "shared_fock_oam": bool(c3),
        "nonnucleonic_transverse": bool(c4),
        "operator_nuclear_maps": bool(c5),
    }
    report = {
        "status": "pass" if all(criteria.values()) else "fail",
        "declared_scope": (
            "Leading-twist forward canonical boundary at Q=5 GeV over "
            "x_N={0.02,0.05,0.10,0.20,0.40}; complete rank-aware multi-Q "
            "evolution remains deferred to item 6."
        ),
        "criteria": criteria,
        "numerical_evidence": {
            "quark_minimum_density_eigenvalue":
                qr["minimum_model_total_density_eigenvalue"],
            "gluon_minimum_density_eigenvalue": min(g_minima),
            "quark_link_reversal_residual":
                qr["maximum_link_reversal_residual_GeV-2"],
            "gluon_link_reversal_residual": gluon_link_residual,
            "response_minimum_density_eigenvalue":
                rr["minimum_mapped_parent_eigenvalue"],
            "response_chain_closure_residual":
                rr["maximum_chain_closure_residual"],
            "maximum_fock_calibration_residual":
                float(fo.calibration_residual.max()),
        },
        "artifacts": {
            "central_quark": "outputs/parent_tmds/wp12_multikinematic/quark_all_tmd_multix_q5.csv",
            "central_gluon": "outputs/parent_tmds/wp12_multikinematic/gluon_all_tmd_multix_q5.csv",
            "wilson_channels": "outputs/parent_tmds/wp12_wilson_channel_members.csv",
            "wilson_projections": "outputs/parent_tmds/wp12_wilson_projected_members.csv",
            "shared_fock": "outputs/parent_tmds/wp12_fock_oam_members.csv",
            "nonnucleonic": "outputs/parent_tmds/wp12_nonnucleonic_transverse.csv",
            "operator_response": "outputs/parent_tmds/wp12_operator_response_members.correlators.csv",
            "inspected_canonical_quark": "outputs/parent_tmds/wp12_canonical_composed_quark.csv",
            "inspected_canonical_gluon": "outputs/parent_tmds/wp12_canonical_composed_gluon.csv",
            "scientific_inspection": "outputs/validation/wp12_scientific_inspection.json",
        },
        "item6": "ready_after_scientific_inspection",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
