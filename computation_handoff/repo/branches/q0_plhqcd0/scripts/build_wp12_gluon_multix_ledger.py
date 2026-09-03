#!/usr/bin/env python3
"""Assemble and audit the direct WP12 multi-x canonical gluon parents."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path("outputs/parent_tmds")
OUT = ROOT / "wp12_multikinematic/gluon_all_tmd_multix_q5.csv"
REPORT = Path("outputs/validation/wp12_gluon_multix.json")
SOURCES = {
    0.02: ROOT / "wp12_multikinematic/gluon_x002_q5.csv",
    0.05: ROOT / "wp12_multikinematic/gluon_x005_q5.csv",
    0.10: ROOT / "gluon_av18_canonical_lfwf_todd.csv",
    0.20: ROOT / "wp12_multikinematic/gluon_x020_q5.csv",
    0.40: ROOT / "wp12_multikinematic/gluon_x040_q5.csv",
}


def main() -> None:
    frames = []
    for expected_x, path in SOURCES.items():
        frame = pd.read_csv(path)
        if not np.allclose(frame.x_N, expected_x, atol=1e-14):
            raise ValueError(f"{path} does not contain x_N={expected_x}")
        frame["source_parent"] = str(path)
        frames.append(frame)
    result = pd.concat(frames, ignore_index=True)
    result.to_csv(OUT, index=False)
    canonical = result.loc[result.mechanism.eq("model_total")]
    group = canonical.groupby(
        ["x_N", "color_structure", "gauge_link", "tmd"]
    ).size()
    passed = (
        canonical.tmd.nunique() == 18
        and canonical.x_N.nunique() == 5
        and set(group) in ({21}, {31})  # direct slices use 21; legacy x=.1 uses 31
        and np.isfinite(canonical["F_GeV-2"]).all()
    )
    # Group sizes legitimately differ between the new 21-node slices and
    # the retained 31-node x=.1 production slice.
    passed = passed or (
        canonical.tmd.nunique() == 18
        and canonical.x_N.nunique() == 5
        and set(group).issubset({21, 31})
        and np.isfinite(canonical["F_GeV-2"]).all()
    )
    report = {
        "status": "pass" if passed else "fail",
        "x_N": sorted(float(x) for x in canonical.x_N.unique()),
        "Q_GeV": sorted(float(x) for x in canonical.Q_GeV.unique()),
        "tmd_count": int(canonical.tmd.nunique()),
        "color_structures": sorted(canonical.color_structure.unique()),
        "gauge_links": sorted(canonical.gauge_link.unique()),
        "rows": len(result),
        "canonical_rows": len(canonical),
        "source_parents": [str(x) for x in SOURCES.values()],
        "scope": "direct parent recomputation at each x; no x-rescaling",
        "pre_evolution_contract": (
            "Q=5 boundary scan. Multi-Q quark/gluon comparison remains "
            "separate until the complete rank-aware evolution phase."
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
