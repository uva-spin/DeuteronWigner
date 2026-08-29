import tempfile
import unittest
from pathlib import Path

import pandas as pd
import numpy as np

from deuteron_wigner.transversity import (
    JAMDiFFTransversityGrid,
    JAMDiFFTransversityReplicas,
)

JAMDIFF_LHAPDF = Path(
    "data/vendor/JAMDiFF_library/lhapdf/JAMDiFF23-transversity_lo"
)


class JAMDiFFGridTests(unittest.TestCase):
    def test_log_scale_and_log_x_interpolation_and_uncertainty(self):
        rows = []
        for q2, factor in ((4.0, 1.0), (16.0, 3.0)):
            for x in (0.01, 0.1):
                rows.append({
                    "Q2_GeV2": q2, "x": x, "flavor": 2,
                    "xh1_mean": factor * x, "xh1_std": 0.2 * factor * x,
                })
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "grid.csv"
            pd.DataFrame(rows).to_csv(path, index=False)
            grid = JAMDiFFTransversityGrid(path)
            estimate = grid.estimate(2, 0.01, 4.0)
            self.assertAlmostEqual(estimate.mean, 3.0)
            self.assertAlmostEqual(estimate.standard_deviation, 0.6)

    def test_rejects_extrapolation(self):
        rows = [
            {"Q2_GeV2": q2, "x": x, "flavor": 2,
             "xh1_mean": x, "xh1_std": 0.1 * x}
            for q2 in (4.0, 16.0) for x in (0.01, 0.1)
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "grid.csv"
            pd.DataFrame(rows).to_csv(path, index=False)
            grid = JAMDiFFTransversityGrid(path)
            with self.assertRaises(ValueError):
                grid(2, 0.001, 2.0)

    @unittest.skipUnless(
        JAMDIFF_LHAPDF.exists(), "optional official JAMDiFF LHAPDF set absent"
    )
    def test_official_member_identity_reproduces_published_mean_std(self):
        replicas = JAMDiFFTransversityReplicas()
        compact = JAMDiFFTransversityGrid(
            "data/processed/jamdiff_wlqcd_transversity.csv"
        )
        values = replicas.replicas(2, 0.1, 5.0)
        self.assertEqual(values.shape, (968,))
        self.assertAlmostEqual(
            replicas.central(2, 0.1, 5.0),
            compact.estimate(2, 0.1, 5.0).mean,
            delta=5.0e-5,
        )
        self.assertAlmostEqual(
            float(np.std(values, ddof=0)),
            compact.estimate(2, 0.1, 5.0).standard_deviation,
            delta=5.0e-5,
        )


if __name__ == "__main__":
    unittest.main()
