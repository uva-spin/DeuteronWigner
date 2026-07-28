#!/usr/bin/env python3
"""Propagate correlated Wilson-kernel members through every TMD projection."""

from __future__ import annotations

import glob
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.axial_tensor_todd import Spin1QuarkNuclearWilsonLine
from deuteron_wigner.correlator_io import (
    deserialize_gluon_correlator,
    deserialize_quark_correlator,
)
from deuteron_wigner.gluon_correlator import (
    project_to_allowed_spin1_gluon_basis,
)
from deuteron_wigner.gluon_lfwf_todd import Spin1NuclearWilsonLine
from deuteron_wigner.gluon_todd import GluonColorStructure
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.quark_correlator import (
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)

from export_wp12_wilson_channels import gluon_kernels, quark_models


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/parent_tmds/wp12_wilson_projected_members.csv"
QMAT = ROOT / (
    "outputs/parent_tmds/wp12_multikinematic/"
    "quark_all_tmd_multix_q5.correlators.csv"
)
GMAT_PATTERN = str(
    ROOT / "outputs/parent_tmds/wp12_multikinematic/gluon_x*_q5.correlators.csv"
)
MASS = 1.87561294257


def link(label: str) -> GaugeLink:
    return {
        "[+,+]": GaugeLink("+", "+"),
        "[-,-]": GaugeLink("-", "-"),
        "[+,-]": GaugeLink("+", "-"),
        "[-,+]": GaugeLink("-", "+"),
    }[label]


def reverse(value: GaugeLink) -> GaugeLink:
    return GaugeLink(
        "-" if value.outgoing == "+" else "+",
        "-" if value.incoming == "+" else "+",
    )


def common(first, member: str) -> dict:
    return {
        "species": first.species,
        "flavor": int(first.flavor),
        "flavor_label": getattr(first, "flavor_label", "g"),
        "color_structure": getattr(first, "color_structure", "not_applicable"),
        "gauge_link": first.gauge_link,
        "x_N": float(first.x_N), "x_D": float(first.x_D),
        "Q_GeV": float(first.Q_GeV), "k_GeV": float(first.k_GeV),
        "azimuth_rad": float(first.azimuth_rad),
        "member": member, "correlation_group": (
            "gluon_wilson_kernel" if first.species == "g"
            else "quark_wilson_kernel"
        ),
        "combine_policy": "member_replaces_central_wilson_operator",
    }


def main() -> None:
    rows: list[dict] = []
    qframe = pd.read_csv(QMAT)
    qframe = qframe[qframe.mechanism.eq("model_total")]
    qkeys = [
        "species", "flavor", "flavor_label", "gauge_link", "x_N", "x_D",
        "Q_GeV", "k_GeV", "azimuth_rad",
    ]
    qmodels = quark_models()
    for _, group in qframe.groupby(qkeys, sort=True):
        first = group.iloc[0]
        parent = deserialize_quark_correlator(group)
        momentum = (
            first.k_GeV*np.cos(first.azimuth_rad),
            first.k_GeV*np.sin(first.azimuth_rad),
        )
        gauge = link(first.gauge_link)
        central = Spin1QuarkNuclearWilsonLine(
            qmodels["central"], int(first.flavor), gauge
        ).unitary(momentum, 0.30)
        for member, model in qmodels.items():
            alternate = Spin1QuarkNuclearWilsonLine(
                model, int(first.flavor), gauge
            ).unitary(momentum, 0.30)
            mapped = Spin1QuarkNuclearWilsonLine.apply_unitary(
                parent, alternate @ central.conj().T
            )
            projected = (
                project_spin1_quark_correlator_at_origin(mapped, MASS)
                if np.isclose(first.k_GeV, 0.0)
                else project_spin1_quark_correlator(mapped, momentum, MASS)
            )
            labels = common(first, member)
            rows.extend({
                **labels, "tmd": name, "F_GeV-2": value,
            } for name, value in projected.items())

    gpaths = sorted(glob.glob(GMAT_PATTERN)) + [str(
        ROOT / "outputs/parent_tmds/"
        "gluon_av18_canonical_lfwf_todd.correlators.csv"
    )]
    kernels = gluon_kernels()
    for path in gpaths:
        gframe = pd.read_csv(path)
        gframe = gframe[gframe.mechanism.eq("model_total")]
        gkeys = [
            "species", "flavor", "color_structure", "gauge_link", "x_N",
            "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
        ]
        for _, group in gframe.groupby(gkeys, sort=True):
            first = group.iloc[0]
            parent = deserialize_gluon_correlator(group)
            momentum = (
                first.k_GeV*np.cos(first.azimuth_rad),
                first.k_GeV*np.sin(first.azimuth_rad),
            )
            color = GluonColorStructure(first.color_structure)
            gauge = link(first.gauge_link)
            central_inverse = Spin1NuclearWilsonLine(
                color, reverse(gauge), 0.0576, 0.3898,
                kernel=kernels["central"],
            )
            unrotated = central_inverse.apply(parent, momentum)
            for member, kernel in kernels.items():
                # Do not numerically unrotate/reapply the identical central
                # member.  At small k, machine-level matrix roundoff is
                # amplified by the rank-four projector for h1TTperpperp.
                # The exact replacement identity is the retained parent.
                mapped = (
                    parent
                    if member == "central"
                    else Spin1NuclearWilsonLine(
                        color, gauge, 0.0576, 0.3898, kernel=kernel
                    ).apply(unrotated, momentum)
                )
                _, projected, residual = project_to_allowed_spin1_gluon_basis(
                    mapped, momentum, MASS
                )
                labels = common(first, member)
                rows.extend({
                    **labels, "tmd": name, "F_GeV-2": value,
                    "basis_residual": residual,
                } for name, value in projected.items())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"{OUT}: {len(rows)} rows")


if __name__ == "__main__":
    main()
