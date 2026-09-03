#!/usr/bin/env python3
"""Assemble and audit the direct WP12 flavor-resolved quark multi-x parents."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import deserialize_quark_correlator
from deuteron_wigner.quark_correlator import T_ODD_QUARK_TMDS


ROOT = Path("outputs/parent_tmds")
DIR = ROOT / "wp12_multikinematic"
OUT = DIR / "quark_all_tmd_multix_q5.csv"
MATRIX = DIR / "quark_all_tmd_multix_q5.correlators.csv"
REPORT = Path("outputs/validation/wp12_quark_multix.json")
SOURCES = {
    0.02: DIR / "quark_x002_q5.csv",
    0.05: DIR / "quark_x005_q5.csv",
    0.10: ROOT / "quark_av18_rich_medium.csv",
    0.20: DIR / "quark_x020_q5.csv",
    0.40: DIR / "quark_x040_q5.csv",
}


def matrix_path(path: Path) -> Path:
    if path == ROOT / "quark_av18_rich_medium.csv":
        return ROOT / "quark_av18_rich_medium.correlators.csv"
    return path.with_suffix(".correlators.csv")


def main() -> None:
    frames, matrices = [], []
    for expected_x, path in SOURCES.items():
        frame = pd.read_csv(path)
        matrix = pd.read_csv(matrix_path(path))
        if not np.allclose(frame.x_N, expected_x, atol=1e-14):
            raise ValueError(f"{path} does not contain x_N={expected_x}")
        frame["source_parent"] = str(path)
        matrix["source_parent"] = str(matrix_path(path))
        frames.append(frame)
        matrices.append(matrix)
    result = pd.concat(frames, ignore_index=True)
    matrix_result = pd.concat(matrices, ignore_index=True)
    result.to_csv(OUT, index=False)
    matrix_result.to_csv(MATRIX, index=False)

    total = result.loc[result.mechanism.eq("model_total")]
    group = total.groupby(["x_N", "flavor", "gauge_link", "tmd"]).size()
    maximum_reversal = 0.0
    for _, block in total.groupby(["x_N", "flavor", "k_GeV", "tmd"]):
        if set(block.gauge_link) != {"[+,+]", "[-,-]"}:
            continue
        values = dict(zip(block.gauge_link, block["F_GeV-2"]))
        sign = -1.0 if block.tmd.iloc[0] in T_ODD_QUARK_TMDS else 1.0
        maximum_reversal = max(
            maximum_reversal, abs(values["[-,-]"]-sign*values["[+,+]"])
        )

    minimum_eigenvalue = np.inf
    selected = matrix_result.loc[matrix_result.mechanism.eq("model_total")]
    labels = [
        "x_N", "flavor", "gauge_link", "k_GeV", "source_parent"
    ]
    for _, block in selected.groupby(labels):
        parent = deserialize_quark_correlator(block)
        minimum_eigenvalue = min(
            minimum_eigenvalue, parent.minimum_positivity_eigenvalue()
        )
    passed = (
        total.tmd.nunique() == 18
        and total.x_N.nunique() == 5
        and set(total.flavor) == {2, 1, -2, -1}
        and set(group).issubset({9})
        and np.isfinite(total["F_GeV-2"]).all()
        and maximum_reversal < 3e-9
        and minimum_eigenvalue >= -2e-9
    )
    report = {
        "status": "pass" if passed else "fail",
        "x_N": sorted(float(x) for x in total.x_N.unique()),
        "Q_GeV": sorted(float(x) for x in total.Q_GeV.unique()),
        "flavors": sorted(int(x) for x in total.flavor.unique()),
        "tmd_count": int(total.tmd.nunique()),
        "rows": len(result), "matrix_rows": len(matrix_result),
        "model_total_rows": len(total),
        "maximum_link_reversal_residual_GeV-2": maximum_reversal,
        "minimum_model_total_density_eigenvalue": float(minimum_eigenvalue),
        "source_parents": [str(x) for x in SOURCES.values()],
        "quadrature": (
            "16x12x8 validated medium at new slices; x=.1 uses the retained "
            "24x16x12 rich production parent"
        ),
        "scope": "direct parent recomputation at each x; no x-rescaling",
        "pre_evolution_contract": (
            "Q=5 boundary scan; multi-Q is explicitly deferred to complete "
            "rank-aware TMD evolution"
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
