#!/usr/bin/env python3
"""Validate physical WW rank-one quark transforms and scale interpolation."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.evolved_quark_model import EvolvedRankZeroQuarkModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedRankZeroQuarkTMD,
    OneLoopQuarkCSSEvolution,
)
from deuteron_wigner.transversity import JAMDiFFTransversityGrid

OUTPUT = Path("outputs/parent_tmds/rank_one_quark_evolution.validation.json")


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        pdf, polarized, transversity_input=transversity
    )

    def adapter(model, scale_nodes):
        boundary = MatchedRankZeroQuarkTMD(model)
        return EvolvedRankZeroQuarkModel(
            model,
            EvolvedMatchedRankZeroQuarkTMD(
                boundary, OneLoopQuarkCSSEvolution(pdf.alpha_s)
            ),
            b_max_gev_inverse=12.0,
            n_b=401,
            n_rank_one_scales=scale_nodes,
        )

    rows = []
    for nucleon_name, model in (("proton", proton), ("neutron", neutron)):
        models = {
            "25_scales": adapter(model, 25),
            "49_scales": adapter(model, 49),
        }
        for flavor in (2, 1, -2, -1):
            values = {}
            for label, evolved in models.items():
                result = evolved.tmd_values(
                    flavor=flavor,
                    x=0.1,
                    k_x_gev=0.3,
                    k_y_gev=0.0,
                    scale_gev=5.0,
                    gauge_link=GaugeLink("+", "+"),
                )
                values[label] = {
                    name: result[name] for name in ("g1T", "h1Lperp")
                }
            differences = {
                name: abs(values["25_scales"][name] - values["49_scales"][name])
                / max(abs(values["49_scales"][name]), 1e-10)
                for name in ("g1T", "h1Lperp")
            }
            rows.append({
                "nucleon": nucleon_name,
                "flavor": flavor,
                "values": values,
                "relative_scale_grid_change": differences,
            })
    maximum = max(
        value
        for row in rows
        for value in row["relative_scale_grid_change"].values()
    )
    passed = maximum < 2e-3
    report = {
        "status": "pass" if passed else "fail",
        "scope": {
            "x": 0.1, "Q_GeV": 5.0, "k_T_GeV": 0.3,
            "nucleons": ["proton", "neutron"],
            "flavors": [2, 1, -2, -1],
            "functions": ["g1T", "h1Lperp"],
            "b_grid": [401, 12.0],
            "scale_grids": [25, 49],
        },
        "maximum_relative_scale_grid_change": maximum,
        "acceptance": 2e-3,
        "rows": rows,
        "physics": (
            "evolve the coordinate-space rank-one vector coefficient R(b); "
            "invert with J1 and M/(2 pi k), using the analytic k=0 limit"
        ),
        "limitation": (
            "WW boundary only; genuine quark-gluon-quark breaking remains a "
            "separate required model uncertainty"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "maximum_relative_scale_grid_change": maximum,
    }, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
