#!/usr/bin/env python3
"""Export complete-parent, positivity-preserving WP12 nuclear-response chains."""

from __future__ import annotations

import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    deserialize_gluon_correlator,
    deserialize_quark_correlator,
    gluon_correlator_rows,
    quark_correlator_rows,
)
from deuteron_wigner.canonical_parent_enrichment import (
    project_spin1_quark_parent_positivity,
)
from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator
from deuteron_wigner.operator_nuclear_response import (
    MEMBERS,
    NuclearResponseMechanism,
    gluon_response_map,
    quark_response_map,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/parent_tmds/wp12_operator_response_members.correlators.csv"
REPORT = ROOT / "outputs/validation/wp12_operator_response.json"
QUARK = ROOT / (
    "outputs/parent_tmds/wp12_multikinematic/"
    "quark_all_tmd_multix_q5.correlators.csv"
)
GLUON_PATTERN = str(
    ROOT / "outputs/parent_tmds/wp12_multikinematic/gluon_x*_q5.correlators.csv"
)
MECHANISMS = tuple(NuclearResponseMechanism)


def _labels(row, *, member: str, stage: str, mechanism: str) -> dict:
    return {
        "sector": row["species"],
        "flavor": int(row["flavor"]),
        "flavor_label": row.get("flavor_label", "g"),
        "color_structure": row.get("color_structure", "not_applicable"),
        "gauge_link": row["gauge_link"],
        "x_N": float(row["x_N"]),
        "x_D": float(row["x_D"]),
        "Q_GeV": float(row["Q_GeV"]),
        "k_GeV": float(row["k_GeV"]),
        "azimuth_rad": float(row["azimuth_rad"]),
        "response_member": member,
        "response_stage": stage,
        "mechanism": mechanism,
        "correlation_group": "wp12_joint_nuclear_response",
        "combine_policy": "ordered_CP_chain_replaces_legacy_scalar_response",
    }


def main() -> None:
    rows: list[dict] = []
    minima: list[float] = []
    closure: list[float] = []

    qframe = pd.read_csv(QUARK)
    qframe = qframe[qframe["mechanism"] == "impulse_total"]
    qkeys = [
        "species", "flavor", "flavor_label", "gauge_link", "x_N", "x_D",
        "Q_GeV", "k_GeV", "azimuth_rad",
    ]
    for _, group in qframe.groupby(qkeys, sort=True, dropna=False):
        first = group.iloc[0]
        # Some mechanism-separated legacy impulse blocks predate the
        # complete-parent PSD contract.  Complete that retained boundary
        # before applying any nuclear response; the completion is not a
        # response mechanism and is recorded in the report below.
        parent, _ = project_spin1_quark_parent_positivity(
            deserialize_quark_correlator(group)
        )
        for member in MEMBERS:
            current = parent
            cumulative = np.zeros((6, 6), dtype=np.complex128)
            for mechanism in MECHANISMS:
                mapped = quark_response_map(mechanism, first.x_N, member).apply(current)
                correction = mapped.quark_target_density_matrix() - current.quark_target_density_matrix()
                cumulative += correction
                labels = _labels(
                    first, member=member.label, stage="increment",
                    mechanism=mechanism.value,
                )
                delta = type(parent)(
                    mapped.vector-current.vector,
                    mapped.axial-current.axial,
                    mapped.transverse-current.transverse,
                )
                rows.extend(quark_correlator_rows(delta, labels))
                current = mapped
            labels = _labels(
                first, member=member.label, stage="mapped_parent",
                mechanism="ordered_total",
            )
            rows.extend(quark_correlator_rows(current, labels))
            minima.append(current.minimum_positivity_eigenvalue())
            closure.append(float(np.max(np.abs(
                current.quark_target_density_matrix()
                - parent.quark_target_density_matrix() - cumulative
            ))))

    gluon_paths = sorted(glob.glob(GLUON_PATTERN))
    gluon_paths.append(str(
        ROOT / "outputs/parent_tmds/"
        "gluon_av18_canonical_lfwf_todd.correlators.csv"
    ))
    for path in gluon_paths:
        gframe = pd.read_csv(path)
        gframe = gframe[gframe["mechanism"] == "impulse_total"]
        gkeys = [
            "species", "flavor", "color_structure", "gauge_link", "x_N",
            "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
        ]
        for _, group in gframe.groupby(gkeys, sort=True, dropna=False):
            first = group.iloc[0]
            parent = Spin1GluonCorrelator(deserialize_gluon_correlator(group))
            for member in MEMBERS:
                current = parent
                cumulative = np.zeros((6, 6), dtype=np.complex128)
                for mechanism in MECHANISMS:
                    mapped = gluon_response_map(
                        mechanism, first.x_N, member
                    ).apply(current)
                    correction = (
                        mapped.joint_density_matrix()
                        - current.joint_density_matrix()
                    )
                    cumulative += correction
                    labels = _labels(
                        first, member=member.label, stage="increment",
                        mechanism=mechanism.value,
                    )
                    rows.extend(gluon_correlator_rows(
                        mapped.values-current.values, labels
                    ))
                    current = mapped
                labels = _labels(
                    first, member=member.label, stage="mapped_parent",
                    mechanism="ordered_total",
                )
                rows.extend(gluon_correlator_rows(current.values, labels))
                minima.append(current.minimum_positivity_eigenvalue())
                closure.append(float(np.max(np.abs(
                    current.joint_density_matrix()
                    - parent.joint_density_matrix() - cumulative
                ))))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    report = {
        "status": "pass" if min(minima) >= -1e-10 and max(closure) < 1e-10 else "fail",
        "source_parent": (
            "retained impulse_total complete correlators; quark parents receive "
            "the declared fixed-unpolarized complete-parent PSD completion "
            "before the response chain"
        ),
        "member_labels": [m.label for m in MEMBERS],
        "mechanism_order": [m.value for m in MECHANISMS],
        "minimum_mapped_parent_eigenvalue": min(minima),
        "maximum_chain_closure_residual": max(closure),
        "row_count": len(rows),
        "interpretation": (
            "Each weak/central/strong member is an ordered completely-positive "
            "map chain on the complete parent. Increment rows telescope to the "
            "mapped-parent row and replace, rather than augment, legacy scalar "
            "response coefficients."
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
