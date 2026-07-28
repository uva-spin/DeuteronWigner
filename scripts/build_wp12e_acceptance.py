#!/usr/bin/env python3
"""Final acceptance audit for the pre-evolution WP12-E evidence gate."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/validation/wp12e_acceptance.json"
DOC = ROOT / "references/wp12e_acceptance.md"


def main() -> None:
    evidence = json.loads((
        ROOT / "outputs/validation/wp12_evidence_parity_matrix.json"
    ).read_text())
    resolved = json.loads((
        ROOT / "outputs/validation/wp12_resolved_nuclear_parent.json"
    ).read_text())
    q = pd.read_csv(
        ROOT / "output/figures/wp12_inspection/wp12_quark_inspection_bands.csv"
    )
    g = pd.read_csv(
        ROOT / "output/figures/wp12_inspection/wp12_gluon_inspection_bands.csv"
    )
    criteria = {
        "all_36_tmd_evidence_rows_pass": evidence["summary"] == {
            "total": 36, "pass": 36, "open": 0
        },
        "resolved_parent_closure_passes": resolved["status"] == "pass",
        "complete_quark_and_gluon_bases": (
            q.tmd.nunique() == 18 and g.tmd.nunique() == 18
        ),
        "pdf_uncertainty_propagated": (
            q["pdf_halfwidth_GeV-2"].max() > 0
            and g["pdf_halfwidth_GeV-2"].max() > 0
        ),
        "csb_uncertainty_propagated": (
            q["csb_halfwidth_GeV-2"].max() > 0
            and g["csb_halfwidth_GeV-2"].max() > 0
        ),
        "bands_are_ordered": all(
            (x["F_low_GeV-2"] <= x["F_central_GeV-2"]).all()
            and (x["F_central_GeV-2"] <= x["F_high_GeV-2"]).all()
            for x in (q, g)
        ),
    }
    criteria = {name: bool(value) for name, value in criteria.items()}
    report = {
        "status": "pass" if all(criteria.values()) else "fail",
        "scope": (
            "leading-twist forward spin-1 quark/antiquark/gluon parent at "
            "Q=5 GeV before complete rank-aware evolution"
        ),
        "criteria": criteria,
        "evidence_rows": evidence["summary"],
        "limitations": [
            "Yang-2024 g1T public covariance/replicas are unavailable; the "
            "published asymmetric-interval hull and shared-Fock sea "
            "sensitivity are used and explicitly are not a confidence region.",
            "Most tensor-polarized and gluon TMDs remain shared-parent model "
            "predictions with named wave/model/nuclear sensitivities, not "
            "direct experimental fits.",
            "Complete rank-aware multi-Q evolution remains the next work item.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2)+"\n")
    DOC.parent.mkdir(parents=True, exist_ok=True)
    DOC.write_text(
        "# WP12-E acceptance\n\n"
        f"Status: **{report['status']}**\n\n"
        + "\n".join(
            f"- [{'x' if passed else ' '}] {name}"
            for name, passed in criteria.items()
        )
        + "\n\n## Declared limitations\n\n"
        + "\n".join(f"- {item}" for item in report["limitations"])
        + "\n"
    )
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
