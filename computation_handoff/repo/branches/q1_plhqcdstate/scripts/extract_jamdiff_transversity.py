#!/usr/bin/env python3
"""Extract compact published JAMDiFF transversity mean/std grids.

The upstream library is deliberately not vendored. Clone
https://github.com/prokudin/JAMDiFF_library and pass its path here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jamdiff-library", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.jamdiff_library))
    from analysis.qpdlib import tpdf

    x = np.unique(np.concatenate((
        np.geomspace(1.0e-3, 0.1, 81),
        np.linspace(0.1, 0.99, 91),
    )))
    q2_values = (2.0, 4.0, 10.0, 25.0, 100.0)
    flavors = {"u": 2, "d": 1, "ub": -2, "db": -1}
    rows = []
    work = args.jamdiff_library / "results" / "wLQCD"
    for q2 in q2_values:
        result = tpdf.get_xf(x, q2, str(work))
        for label, pdg in flavors.items():
            mean = np.asarray(result["XF"][label]["mean"], dtype=float)
            std = np.asarray(result["XF"][label]["std"], dtype=float)
            rows.extend({
                "Q2_GeV2": q2,
                "x": float(xi),
                "flavor": pdg,
                "xh1_mean": float(mu),
                "xh1_std": float(sigma),
            } for xi, mu, sigma in zip(x, mean, std))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(args.output, index=False)
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    metadata = {
        "source": "https://github.com/prokudin/JAMDiFF_library",
        "source_commit": "2d601943b003ab03d261d492b565c1ebf54d07cc",
        "analysis": (
            "results/wLQCD; compact member-0 mean and population std of "
            "physical LHAPDF members 1-968"
        ),
        "paper": "arXiv:2306.12998",
        "quantity": "replica mean and standard deviation of x*h1",
        "interpolation_domain": {
            "x": [float(x.min()), float(x.max())],
            "Q2_GeV2": list(q2_values),
        },
        "sha256": digest,
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(frame)} rows to {args.output}; sha256={digest}")


if __name__ == "__main__":
    main()
