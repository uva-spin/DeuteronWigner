#!/usr/bin/env python3
"""Audit joint spin-density eigenvalues of stored evolved parent scenarios."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from deuteron_wigner.quark_correlator import compose_spin1_quark_correlator

INPUT = Path("outputs/parent_tmds/evolved_quark_parent_scenarios.csv")
OUTPUT = INPUT.with_name("evolved_quark_parent_positivity.validation.json")
M_D_GEV = 1.87561294257


def main() -> None:
    grouped = defaultdict(dict)
    with INPUT.open() as stream:
        for row in csv.DictReader(stream):
            key = (
                row["wave_function"], row["scenario"], int(row["flavor"]),
                float(row["k_T_GeV"]), row["part"],
            )
            grouped[key][row["tmd"]] = float(row["value_GeV-2"])

    rows = []
    for key, tmds in grouped.items():
        wave, scenario, flavor, momentum, part = key
        correlator = compose_spin1_quark_correlator(
            (momentum, 0.0), M_D_GEV, tmds
        )
        eigenvalue = correlator.minimum_positivity_eigenvalue()
        rows.append({
            "wave_function": wave,
            "scenario": scenario,
            "flavor": flavor,
            "k_T_GeV": momentum,
            "part": part,
            "minimum_eigenvalue": eigenvalue,
        })
    worst = min(rows, key=lambda row: row["minimum_eigenvalue"])
    counts = {
        part: sum(
            row["minimum_eigenvalue"] < -1e-10
            for row in rows if row["part"] == part
        )
        for part in ("proton", "neutron", "total")
    }
    passed = not any(counts.values())
    report = {
        "status": "pass" if passed else "diagnostic_violation",
        "group_count": len(rows),
        "worst": worst,
        "negative_below_minus_1e-10": counts,
        "interpretation": (
            "tree-level joint-density positivity is not scheme invariant for "
            "soft-subtracted evolved W terms; no clipping or reweighting applied"
        ),
        "hard_numerical_gate": True,
        "scheme_applicability_caveat": True,
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"], "group_count": len(rows),
        "worst": worst, "negative_below_minus_1e-10": counts,
    }, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
