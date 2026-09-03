#!/usr/bin/env python3
"""Audit moment coverage of the production AV18 NNpi parent table."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.moment_ledger import (
    EndpointCompletion,
    MomentObservable,
    TabulatedMomentInput,
    audit_sum_rule,
    evaluate_moment,
    local_power_endpoint_completion,
)
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator_at_origin,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs/parent_tmds/nnpi/av18_collinear_parent_refined.csv"
GLUON_SOURCE = ROOT / "outputs/parent_tmds/gluon_av18_collinear_moments_q5.csv"
ALL_PARTON_SOURCE = ROOT / "outputs/parent_tmds/all_parton_av18_momentum_q5.csv"
GLUON_HELICITY_SOURCE = (
    ROOT / "outputs/parent_tmds/gluon_av18_helicity_moments_q5.csv"
)
OUTPUT = ROOT / "outputs/validation/av18_parent_moment_coverage.json"


def main() -> None:
    table = pd.read_csv(SOURCE)
    quarks = table[table["species"].isin(("q", "qbar"))]
    observable_tmd = {
        MomentObservable.NUMBER: "f1",
        MomentObservable.MOMENTUM: "f1",
        MomentObservable.HELICITY: "g1",
        MomentObservable.TENSOR: "f1LL",
        MomentObservable.TRANSVERSITY: "h1",
    }
    entries = []
    number_sources = {}
    for (species, flavor, mechanism), group in quarks.groupby(
        ["species", "flavor", "mechanism"], sort=True
    ):
        x_values = []
        named_values = {observable: [] for observable in observable_tmd}
        for x, point in group.groupby("x_N", sort=True):
            matrices = {
                "vector": np.zeros((3, 3), dtype=np.complex128),
                "axial": np.zeros((3, 3), dtype=np.complex128),
                "transverse": np.zeros((2, 3, 3), dtype=np.complex128),
            }
            for row in point.itertuples():
                value = complex(row.real, row.imag)
                if row.projection == "transverse":
                    matrices["transverse"][
                        int(row.operator_index),
                        int(row.target_out),
                        int(row.target_in),
                    ] = value
                else:
                    matrices[row.projection][
                        int(row.target_out), int(row.target_in)
                    ] = value
            projected = project_spin1_quark_correlator_at_origin(
                Spin1QuarkCorrelator(**matrices),
                mass=1.87561294257,
            )
            x_values.append(float(x))
            for observable, name in observable_tmd.items():
                named_values[observable].append(projected[name])
        for observable in observable_tmd:
            partial = TabulatedMomentInput(
                species=str(species),
                flavor=int(flavor),
                mechanism=str(mechanism),
                observable=observable,
                x=np.asarray(x_values),
                values=np.asarray(named_values[observable]),
                source=str(SOURCE.relative_to(ROOT)),
            )
            if observable is MomentObservable.NUMBER:
                number_sources[(str(species), abs(int(flavor)), str(mechanism))] = partial
            if np.max(np.abs(partial.values)) < 1.0e-13:
                completion = EndpointCompletion(
                    corrections={observable: 0.0},
                    source="exact zero of the configured parent projection",
                    uncertainty_description=(
                        "exact within 1e-13 numerical threshold in this model limit"
                    ),
                )
            else:
                try:
                    completion = local_power_endpoint_completion(partial)
                except ValueError:
                    completion = None
            entries.append(evaluate_moment(TabulatedMomentInput(
                **{
                    field: getattr(partial, field)
                    for field in (
                        "species", "flavor", "mechanism", "observable",
                        "x", "values", "source",
                    )
                },
                endpoint_completion=completion,
            )))

    # Number conservation applies to valence combinations.  Form q-qbar
    # before fitting the low-x endpoint so the common sea singularity can
    # cancel rather than demanding finite separate sea-number integrals.
    valence_entries = []
    for abs_flavor in (1, 2):
        for mechanism in ("proton_impulse", "neutron_impulse", "impulse_total"):
            q = number_sources[("q", abs_flavor, mechanism)]
            qbar = number_sources[("qbar", abs_flavor, mechanism)]
            valence = TabulatedMomentInput(
                species="q-valence",
                flavor=abs_flavor,
                mechanism=mechanism,
                observable=MomentObservable.NUMBER,
                x=q.x,
                values=q.values - qbar.values,
                source=f"{q.source}; correlator-level q-qbar combination",
            )
            completion = local_power_endpoint_completion(valence)
            valence_entries.append(evaluate_moment(TabulatedMomentInput(
                species=valence.species,
                flavor=valence.flavor,
                mechanism=valence.mechanism,
                observable=valence.observable,
                x=valence.x,
                values=valence.values,
                source=valence.source,
                endpoint_completion=completion,
            )))
    entries.extend(valence_entries)

    gluon = pd.read_csv(GLUON_SOURCE).sort_values("x_N")
    for observable, column in (
        (MomentObservable.MOMENTUM, "f1g_per_nucleon"),
        (MomentObservable.TENSOR, "f1LLg_per_nucleon"),
    ):
        partial = TabulatedMomentInput(
            species="g",
            flavor=21,
            mechanism="impulse_total",
            observable=observable,
            x=gluon["x_N"].to_numpy(),
            values=gluon[column].to_numpy(),
            source=str(GLUON_SOURCE.relative_to(ROOT)),
            x_power_override=(
                1 if observable is MomentObservable.TENSOR else None
            ),
        )
        try:
            completion = local_power_endpoint_completion(partial)
        except ValueError:
            completion = None
        entries.append(evaluate_moment(TabulatedMomentInput(
            species=partial.species,
            flavor=partial.flavor,
            mechanism=partial.mechanism,
            observable=partial.observable,
            x=partial.x,
            values=partial.values,
            source=partial.source,
            endpoint_completion=completion,
            x_power_override=partial.x_power_override,
        )))

    gluon_helicity = pd.read_csv(GLUON_HELICITY_SOURCE).sort_values("x_N")
    helicity_partial = TabulatedMomentInput(
        species="g", flavor=21, mechanism="impulse_total",
        observable=MomentObservable.HELICITY,
        x=gluon_helicity["x_N"].to_numpy(),
        values=gluon_helicity["g1g_per_nucleon"].to_numpy(),
        source=str(GLUON_HELICITY_SOURCE.relative_to(ROOT)),
    )
    helicity_completion = local_power_endpoint_completion(helicity_partial)
    entries.append(evaluate_moment(TabulatedMomentInput(
        species=helicity_partial.species, flavor=helicity_partial.flavor,
        mechanism=helicity_partial.mechanism,
        observable=helicity_partial.observable, x=helicity_partial.x,
        values=helicity_partial.values, source=helicity_partial.source,
        endpoint_completion=helicity_completion,
    )))

    all_parton = pd.read_csv(ALL_PARTON_SOURCE)
    momentum_entries = []
    for flavor, group in all_parton.groupby("flavor", sort=True):
        group = group.sort_values("x_N")
        partial = TabulatedMomentInput(
            species=str(group["species"].iloc[0]),
            flavor=int(flavor),
            mechanism="impulse_total",
            observable=MomentObservable.MOMENTUM,
            x=group["x_N"].to_numpy(),
            values=group["f1_per_nucleon"].to_numpy(),
            source=str(ALL_PARTON_SOURCE.relative_to(ROOT)),
        )
        completion = local_power_endpoint_completion(partial)
        momentum_entries.append(evaluate_moment(TabulatedMomentInput(
            species=partial.species, flavor=partial.flavor,
            mechanism=partial.mechanism, observable=partial.observable,
            x=partial.x, values=partial.values, source=partial.source,
            endpoint_completion=completion,
        )))
    momentum_audit = audit_sum_rule(
        "per-nucleon all-active-parton momentum",
        momentum_entries, expected=1.0, tolerance=0.002,
    )

    valence_audit = audit_sum_rule(
        "per-nucleon deuteron valence number",
        [
            entry for entry in entries
            if entry.species == "q-valence"
            and entry.mechanism == "impulse_total"
        ],
        expected=3.0,
        tolerance=0.03,
    )
    refusal = None
    try:
        audit_sum_rule(
            "production parent number diagnostic",
            [
                entry for entry in entries
                if entry.observable is MomentObservable.NUMBER
                and entry.mechanism == "impulse_total"
            ],
            expected=1.0,
            tolerance=1e-3,
        )
    except ValueError as exc:
        refusal = str(exc)
    if refusal is None:
        raise RuntimeError("truncated production table unexpectedly allowed sum-rule claim")
    report = {
        "sources": [
            str(SOURCE.relative_to(ROOT)),
            str(GLUON_SOURCE.relative_to(ROOT)),
            str(ALL_PARTON_SOURCE.relative_to(ROOT)),
            str(GLUON_HELICITY_SOURCE.relative_to(ROOT)),
        ],
        "basis_quantity": (
            "named rank-zero projection of complete collinear quark correlator"
        ),
        "entries": [
            {
                **asdict(entry),
                "observable": entry.observable.value,
            }
            for entry in entries
        ],
        "all_support_complete": all(entry.support_complete for entry in entries),
        "support_complete_entries": sum(entry.support_complete for entry in entries),
        "support_incomplete_entries": sum(not entry.support_complete for entry in entries),
        "conservation_claim_refused": True,
        "valence_number_sum_rule": {
            **asdict(valence_audit),
            "entries": [
                {
                    **asdict(entry),
                    "observable": entry.observable.value,
                }
                for entry in valence_audit.entries
            ],
        },
        "all_parton_momentum_sum_rule": {
            **asdict(momentum_audit),
            "endpoint_uncertainty_quadrature": float(np.sqrt(sum(
                (entry.endpoint_uncertainty or 0.0) ** 2
                for entry in momentum_entries
            ))),
            "active_flavors": [entry.flavor for entry in momentum_entries],
            "entries": [
                {
                    **asdict(entry),
                    "observable": entry.observable.value,
                }
                for entry in momentum_audit.entries
            ],
        },
        "refusal_reason": refusal,
        "required_replacement": (
            "source-validated low-x and high-x endpoint completions for every "
            "species/flavor/mechanism and moment observable"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "entries": len(entries),
        "x_interval": entries[0].x_interval,
        "conservation_claim_refused": True,
    }, indent=2))


if __name__ == "__main__":
    main()
