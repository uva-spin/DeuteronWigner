#!/usr/bin/env python3
"""Compose the inspected WP12 central parent without nuclear double counting."""

from __future__ import annotations

import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.canonical_parent_enrichment import (
    project_spin1_gluon_parent_positivity,
    project_spin1_quark_parent_positivity,
)
from deuteron_wigner.correlator_io import (
    deserialize_gluon_correlator,
    deserialize_quark_correlator,
    gluon_correlator_rows,
    quark_correlator_rows,
)
from deuteron_wigner.gluon_correlator import (
    Spin1GluonCorrelator,
    project_to_allowed_spin1_gluon_basis,
)
from deuteron_wigner.operator_nuclear_response import (
    MEMBERS,
    NuclearResponseMechanism,
    gluon_response_map,
    quark_response_map,
)
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    compose_spin1_quark_correlator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
    reverse_quark_gauge_link,
)


ROOT = Path(__file__).resolve().parents[1]
QINPUT = ROOT / (
    "outputs/parent_tmds/wp12_multikinematic/"
    "quark_all_tmd_multix_q5.correlators.csv"
)
GINPUT = str(
    ROOT / "outputs/parent_tmds/wp12_multikinematic/"
    "gluon_x*_q5.correlators.csv"
)
QOUT = ROOT / "outputs/parent_tmds/wp12_canonical_composed_quark.csv"
GOUT = ROOT / "outputs/parent_tmds/wp12_canonical_composed_gluon.csv"
REPORT = ROOT / "outputs/validation/wp12_canonical_composition.json"
MASS = 1.87561294257
CENTRAL = next(member for member in MEMBERS if member.label == "central")
CENTRAL_CP = (
    NuclearResponseMechanism.SHADOWING,
    NuclearResponseMechanism.ANTISHADOWING,
    NuclearResponseMechanism.OFF_SHELL,
)
QRANKS = {
    "f1": 0, "h1perp": 1, "g1": 0, "h1Lperp": 1,
    "f1Tperp": 1, "g1T": 1, "h1": 0, "h1Tperp": 2,
    "f1LL": 0, "h1LLperp": 2, "f1LT": 1, "g1LT": 1,
    "h1LT": 0, "h1LTperp": 2, "f1TT": 2, "g1TT": 2,
    "h1TT": 1, "h1TTperp": 3,
}
GRANKS = {
    "f1": 0, "g1": 0, "h1perp": 2, "h1Lperp": 2,
    "f1Tperp": 1, "g1T": 1, "h1": 1, "h1Tperp": 3,
    "f1LL": 0, "h1LLperp": 2, "f1LT": 1, "g1LT": 1,
    "h1LT": 1, "h1LTperp": 3, "f1TT_minus_h1TTperp": 2,
    "g1TT": 2, "h1TT": 0, "h1TTperpperp": 4,
}


def qsum(left: Spin1QuarkCorrelator, right: Spin1QuarkCorrelator):
    return Spin1QuarkCorrelator(
        left.vector+right.vector,
        left.axial+right.axial,
        left.transverse+right.transverse,
    )


def labels(first, completion_scale: float) -> dict:
    return {
        "species": first.species, "flavor": int(first.flavor),
        "flavor_label": getattr(first, "flavor_label", "g"),
        "color_structure": getattr(
            first, "color_structure", "not_applicable"
        ),
        "gauge_link": first.gauge_link,
        "x_N": float(first.x_N), "x_D": float(first.x_D),
        "Q_GeV": float(first.Q_GeV), "k_GeV": float(first.k_GeV),
        "azimuth_rad": float(first.azimuth_rad),
        "mechanism": "canonical_composed_total",
        "response_policy": (
            "CP(shadowing->antishadowing->off_shell) on impulse; "
            "add sourced NNpi meson parent; generic mesonic/SRC central off"
        ),
        "positivity_completion_scale": completion_scale,
        "combine_policy": "single inspected canonical parent",
    }


def main() -> None:
    qrows, qmatrix = [], []
    qparents = {}
    grows, gmatrix = [], []
    qmins, gmins, qscales, gscales = [], [], [], []

    qframe = pd.read_csv(QINPUT)
    qkeys = [
        "species", "flavor", "flavor_label", "gauge_link", "x_N", "x_D",
        "Q_GeV", "k_GeV", "azimuth_rad",
    ]
    for _, full in qframe.groupby(qkeys, sort=True):
        first = full.iloc[0]
        mechanisms = {
            name: deserialize_quark_correlator(block)
            for name, block in full.groupby("mechanism")
        }
        current, _ = project_spin1_quark_parent_positivity(
            mechanisms["impulse_total"]
        )
        for mechanism in CENTRAL_CP:
            current = quark_response_map(
                mechanism, first.x_N, CENTRAL
            ).apply(current)
        current = qsum(current, mechanisms["meson_exchange"])
        current, scale = project_spin1_quark_parent_positivity(current)
        momentum = (
            first.k_GeV*np.cos(first.azimuth_rad),
            first.k_GeV*np.sin(first.azimuth_rad),
        )
        pair_key = (
            first.species, int(first.flavor), first.flavor_label,
            float(first.x_N), float(first.x_D), float(first.Q_GeV),
            float(first.k_GeV), float(first.azimuth_rad),
        )
        qparents.setdefault(pair_key, {})[first.gauge_link] = (
            first, current, scale, momentum
        )

    # A polarized CP response can otherwise introduce a small staple-even
    # admixture into a nominally T-odd projection.  Convexly symmetrize the
    # complete future parent with the time-reversed past parent, then rebuild
    # both links from one common coefficient set.  Convexity and the exact
    # reverse-basis map preserve positivity.
    for pair in qparents.values():
        if set(pair) != {"[+,+]", "[-,-]"}:
            raise ValueError("quark composition lacks a staple-reversal pair")
        ffirst, future, fscale, momentum = pair["[+,+]"]
        pfirst, past, pscale, _ = pair["[-,-]"]
        if np.isclose(ffirst.k_GeV, 0.0):
            future_values = project_spin1_quark_correlator_at_origin(
                future, MASS
            )
            past_values = project_spin1_quark_correlator_at_origin(past, MASS)
        else:
            future_values = project_spin1_quark_correlator(
                future, momentum, MASS
            )
            past_values = project_spin1_quark_correlator(
                past, momentum, MASS
            )
        past_as_future = reverse_quark_gauge_link(past_values)
        symmetric_future = {
            name: 0.5*(future_values[name]+past_as_future[name])
            for name in future_values
        }
        symmetric_past = reverse_quark_gauge_link(symmetric_future)
        for first, values, scale in (
            (ffirst, symmetric_future, fscale),
            (pfirst, symmetric_past, pscale),
        ):
            current = compose_spin1_quark_correlator(
                momentum, MASS, values
            )
            common = labels(first, scale)
            f1 = values["f1"]
            qrows.extend({
                **common, "tmd": name, "rank": QRANKS[name],
                "F_GeV-2": value,
                "physical_ratio_to_f1": (
                    (first.k_GeV/MASS)**QRANKS[name]*value/f1
                    if f1 else 0.0
                ),
            } for name, value in values.items())
            qmatrix.extend(quark_correlator_rows(current, common))
            qmins.append(current.minimum_positivity_eigenvalue())
            qscales.append(scale)

    gpaths = sorted(glob.glob(GINPUT)) + [str(
        ROOT / "outputs/parent_tmds/"
        "gluon_av18_canonical_lfwf_todd.correlators.csv"
    )]
    for path in gpaths:
        gframe = pd.read_csv(path)
        gkeys = [
            "species", "flavor", "color_structure", "gauge_link", "x_N",
            "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
        ]
        for _, full in gframe.groupby(gkeys, sort=True):
            first = full.iloc[0]
            mechanisms = {
                name: Spin1GluonCorrelator(
                    deserialize_gluon_correlator(block)
                )
                for name, block in full.groupby("mechanism")
            }
            momentum = (
                first.k_GeV*np.cos(first.azimuth_rad),
                first.k_GeV*np.sin(first.azimuth_rad),
            )
            current, _ = project_spin1_gluon_parent_positivity(
                mechanisms["impulse_total"], momentum, MASS
            )
            for mechanism in CENTRAL_CP:
                current = gluon_response_map(
                    mechanism, first.x_N, CENTRAL
                ).apply(current)
            current = Spin1GluonCorrelator(
                current.values + mechanisms["meson_exchange"].values
            )
            current, scale = project_spin1_gluon_parent_positivity(
                current, momentum, MASS
            )
            _, projected, residual = project_to_allowed_spin1_gluon_basis(
                current.values, momentum, MASS
            )
            common = labels(first, scale)
            f1 = projected["f1"]
            grows.extend({
                **common, "tmd": name, "rank": GRANKS[name],
                "F_GeV-2": value, "basis_residual": residual,
                "physical_ratio_to_f1": (
                    (first.k_GeV/MASS)**GRANKS[name]*value/f1 if f1 else 0.0
                ),
            } for name, value in projected.items())
            gmatrix.extend(gluon_correlator_rows(current.values, common))
            gmins.append(current.minimum_positivity_eigenvalue())
            gscales.append(scale)

    QOUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(qrows).to_csv(QOUT, index=False)
    pd.DataFrame(qmatrix).to_csv(QOUT.with_suffix(".correlators.csv"), index=False)
    pd.DataFrame(grows).to_csv(GOUT, index=False)
    pd.DataFrame(gmatrix).to_csv(GOUT.with_suffix(".correlators.csv"), index=False)
    report = {
        "status": "pass" if min(qmins+gmins) >= -1e-10 else "fail",
        "canonical_policy": (
            "Legacy coefficient shadowing/antishadowing/off-shell blocks are "
            "replaced by ordered joint-spin CP maps. The sourced NNpi meson "
            "correlator is then added once. Generic CP mesonic and SRC maps "
            "remain zero-centered alternatives to avoid double counting."
        ),
        "quark_rows": len(qrows), "gluon_rows": len(grows),
        "minimum_quark_eigenvalue": min(qmins),
        "minimum_gluon_eigenvalue": min(gmins),
        "minimum_quark_completion_scale": min(qscales),
        "minimum_gluon_completion_scale": min(gscales),
        "x_N": [0.02, 0.05, 0.10, 0.20, 0.40],
        "Q_GeV": 5.0,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
