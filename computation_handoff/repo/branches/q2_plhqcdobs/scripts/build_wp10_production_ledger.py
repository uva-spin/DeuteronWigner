#!/usr/bin/env python3
"""Build one provenance-preserving ledger for every WP10 production member."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

OUTPUT = Path("outputs/parent_tmds/wp10_production_member_ledger.csv")
TMD_CHANNEL = {
    "f1": "U", "h1perp": "U", "g1": "L", "h1Lperp": "L",
    "f1Tperp": "T", "g1T": "T", "h1": "T", "h1Tperp": "T",
    "f1LL": "LL", "h1LLperp": "LL",
    "f1LT": "LT", "g1LT": "LT", "h1LT": "LT", "h1LTperp": "LT",
    "f1TT": "TT", "g1TT": "TT", "h1TT": "TT", "h1TTperp": "TT",
    "f1TT_minus_h1TTperp": "TT", "h1TTperpperp": "TT",
    "shadow_trace": "U", "shadow_circular": "polarized",
    "shadow_linear_norm": "linear",
}
COLUMNS = [
    "sector", "species", "flavor", "flavor_label", "tmd", "stage",
    "target_channel", "color_structure", "scenario", "mechanism",
    "gauge_link", "x_N", "Q_GeV", "k_GeV", "F_GeV-2",
    "evidence_class", "uncertainty_axis", "combine_policy",
    "source_artifact", "member_id", "amplitude_identity", "validity",
]


def normalized(rows: pd.DataFrame, **defaults) -> pd.DataFrame:
    result = rows.copy()
    for key, value in defaults.items():
        if key not in result:
            result[key] = value
        else:
            result[key] = result[key].fillna(value)
    for column in COLUMNS:
        if column not in result:
            result[column] = np.nan
    return result[COLUMNS]


def envelope_members(path: str, sector: str) -> list[pd.DataFrame]:
    frame = pd.read_csv(path)
    members = []
    for scenario, column in (
        ("central_av18", "F_central_GeV-2"),
        ("wave_envelope_low", "F_wave_low_GeV-2"),
        ("wave_envelope_high", "F_wave_high_GeV-2"),
    ):
        member = frame.rename(columns={column: "F_GeV-2"}).copy()
        member["scenario"] = scenario
        members.append(
            normalized(
                member,
                sector=sector,
                flavor_label=("g" if sector == "gluon" else ""),
                color_structure="not_applicable",
                mechanism="model_total" if sector == "quark" else "impulse_total",
                gauge_link="[+,+]",
                evidence_class="mixed_fit_lattice_model",
                uncertainty_axis="wave_function_model",
                combine_policy="central_or_alternative_wave_member",
                source_artifact=path,
            )
        )
    return members


def main() -> None:
    ledgers: list[pd.DataFrame] = []
    ledgers.extend(envelope_members(
        "outputs/parent_tmds/rich_ensemble/quark_parent_tmd_ensemble.csv",
        "quark",
    ))
    ledgers.extend(envelope_members(
        "outputs/parent_tmds/rich_ensemble/gluon_parent_tmd_ensemble.csv",
        "gluon",
    ))

    todd_path = "outputs/parent_tmds/ensemble/rich_todd_parent_ensemble.csv"
    todd = pd.read_csv(todd_path).rename(
        columns={"F_central_GeV-2": "F_GeV-2"}
    )
    todd["sector"] = np.where(
        todd["species"].eq("g"), "gluon", "quark"
    )
    ledgers.append(normalized(
        todd,
        target_channel="T",
        x_N=0.1,
        Q_GeV=5.0,
        mechanism="gauge_link_todd",
        evidence_class="phenomenology_or_model",
        combine_policy="alternative_color_and_fit_scenario",
        source_artifact=todd_path,
    ))

    for path, sector, policy in (
        (
            "outputs/parent_tmds/quark_av18_oam_medium.csv",
            "quark",
            "alternative_oam_parent_not_summed_with_fit_central",
        ),
        (
            "outputs/parent_tmds/nonnucleonic_cluster_tmds.csv",
            "quark",
            "separate_additive_non_nucleonic_sensitivity",
        ),
        (
            "outputs/parent_tmds/spin_resolved_pion_tmds.csv",
            "quark",
            "separate_additive_mesonic_component_with_fock_ledger",
        ),
        (
            "outputs/parent_tmds/quark_polarized_tensor_shadowing_scenarios.csv",
            "quark",
            "alternative_shadowing_response_scenario",
        ),
    ):
        frame = pd.read_csv(path)
        if policy.startswith("alternative_oam"):
            frame["scenario"] = frame["input_scenario"]
            frame = frame.loc[
                frame.mechanism.eq("model_total")
                & frame.gauge_link.eq("[+,+]")
            ]
        ledgers.append(normalized(
            frame,
            sector=sector,
            color_structure="not_applicable",
            evidence_class="model_dependent",
            uncertainty_axis=(
                "explicit_model_scenario"
                if "uncertainty_axis" not in frame
                else ""
            ),
            combine_policy=policy,
            source_artifact=path,
        ))

    bm_path = "outputs/parent_tmds/boer_mulders_parent_scenarios.csv"
    ledgers.append(normalized(
        pd.read_csv(bm_path),
        sector="quark",
        color_structure="not_applicable",
        source_artifact=bm_path,
    ))

    gluon_multiplet_path = (
        "outputs/parent_tmds/complete_gluon_todd_multiplet.csv"
    )
    ledgers.append(normalized(
        pd.read_csv(gluon_multiplet_path),
        source_artifact=gluon_multiplet_path,
    ))

    gluon_two_stage_path = (
        "outputs/parent_tmds/gluon_todd_two_stage_predictions.csv"
    )
    ledgers.append(normalized(
        pd.read_csv(gluon_two_stage_path),
        source_artifact=gluon_two_stage_path,
    ))

    axial_tensor_path = (
        "outputs/parent_tmds/quark_axial_tensor_todd_stages.csv"
    )
    ledgers.append(normalized(
        pd.read_csv(axial_tensor_path),
        color_structure="not_applicable",
        source_artifact=axial_tensor_path,
    ))

    gluon_shadow_path = (
        "outputs/parent_tmds/gluon_polarized_tensor_shadowing_scenarios.csv"
    )
    gluon_shadow = pd.read_csv(gluon_shadow_path)
    for component, column in (
        ("shadow_trace", "trace_real"),
        ("shadow_circular", "circular_real"),
        ("shadow_linear_norm", "linear_norm"),
    ):
        member = gluon_shadow.rename(
            columns={column: "F_GeV-2"}
        ).copy()
        member["tmd"] = component
        ledgers.append(normalized(
            member,
            sector="gluon",
            flavor_label="g",
            color_structure="not_applicable",
            combine_policy="alternative_shadowing_response_scenario",
            source_artifact=gluon_shadow_path,
        ))

    ledger = pd.concat(ledgers, ignore_index=True)
    ledger["flavor_label"] = ledger["flavor_label"].replace("", np.nan)
    ledger.loc[
        ledger.sector.eq("gluon") & ledger.flavor_label.isna(), "flavor_label"
    ] = "g"
    ledger["stage"] = ledger["stage"].fillna("not_applicable")
    ledger["target_channel"] = ledger["target_channel"].fillna(
        ledger["tmd"].map(TMD_CHANNEL).fillna("not_applicable")
    )
    ledger["member_id"] = ledger["member_id"].fillna(
        ledger["source_artifact"].astype(str)
        + "::"
        + ledger["stage"].astype(str)
        + "::"
        + ledger["scenario"].astype(str)
    )
    ledger["amplitude_identity"] = ledger["amplitude_identity"].fillna(
        ledger["stage"].astype(str)
        + "::"
        + ledger["mechanism"].astype(str)
        + "::"
        + ledger["tmd"].astype(str)
        + "::"
        + ledger["color_structure"].astype(str)
    )
    ledger["validity"] = ledger["validity"].fillna(
        "see source-artifact metadata; sampled x_N,Q_GeV,k_GeV are serialized"
    )
    required = [
        "sector", "species", "flavor_label", "tmd", "stage", "scenario", "mechanism",
        "gauge_link", "x_N", "Q_GeV", "k_GeV", "F_GeV-2",
        "evidence_class", "uncertainty_axis", "combine_policy",
        "source_artifact", "member_id", "amplitude_identity", "validity",
    ]
    if ledger[required].isna().any().any():
        missing = ledger[required].columns[ledger[required].isna().any()].tolist()
        raise ValueError(f"WP10 ledger has missing required fields: {missing}")
    if not np.all(np.isfinite(ledger["F_GeV-2"])):
        raise ValueError("WP10 ledger contains nonfinite values")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    ledger.to_csv(OUTPUT, index=False)
    metadata = {
        "schema_version": 2,
        "rows": len(ledger),
        "sectors": sorted(ledger.sector.unique()),
        "mechanisms": sorted(ledger.mechanism.unique()),
        "uncertainty_axes": sorted(ledger.uncertainty_axis.unique()),
        "combine_rule": (
            "Rows are identified central, bound, or alternative mechanism "
            "members. They are not a joint probability ensemble and must not "
            "be summed unless combine_policy explicitly permits it."
        ),
        "source_artifacts": sorted(ledger.source_artifact.unique()),
    }
    OUTPUT.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(ledger)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
