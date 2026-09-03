#!/usr/bin/env python3
"""Audit the scientific source tables behind the current TMD atlases."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

import pandas as pd

from deuteron_wigner.figure_acceptance import (
    audit_ensemble_table,
    audit_flavor_traceability,
)

ROOT = Path("outputs/parent_tmds")
OUT = Path("outputs/validation/parent_tmd_figure_acceptance.json")


def main() -> None:
    quark = pd.read_csv(ROOT / "ensemble/quark_parent_tmd_ensemble.csv")
    gluon = pd.read_csv(ROOT / "ensemble/gluon_parent_tmd_ensemble.csv")
    source = pd.read_csv(ROOT / "quark_av18_fine.csv")
    quark_audit = audit_ensemble_table(quark, "quark")
    gluon_audit = audit_ensemble_table(gluon, "gluon")
    flavor = audit_flavor_traceability(source)
    report = {
        "status": "pass" if (
            quark_audit.passed
            and gluon_audit.passed
            and flavor["flavor_resolved_before_assembly"]
        ) else "fail",
        "scope": (
            "serialized-source and presentation-product acceptance; this does "
            "not close the open WP8 physics requirements"
        ),
        "quark": asdict(quark_audit) | {"passed": quark_audit.passed},
        "gluon": asdict(gluon_audit) | {"passed": gluon_audit.passed},
        "flavor_traceability": flavor,
        "visual_inspection": {
            "method": "PyMuPDF rasterization because Poppler is unavailable",
            "inspected": [
                "outputs/parent_tmds/ensemble/quark_parent_tmd_atlas.pdf page 1",
                "outputs/parent_tmds/ensemble/gluon_parent_tmd_atlas.pdf page 1",
                "outputs/figures/production_tmds/u/central.pdf page 1",
            ],
            "finding": (
                "parent curves and bands are smooth and legible; the historical "
                "closure atlas is visually polished but scientifically superseded"
            ),
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    if report["status"] != "pass":
        raise SystemExit("parent TMD figure acceptance failed")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
