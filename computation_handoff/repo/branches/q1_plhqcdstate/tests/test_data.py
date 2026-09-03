"""Tests for manually transcribed experimental inputs."""

from pathlib import Path
import unittest

import numpy as np

from deuteron_wigner.data import load_hermes_b1

ROOT = Path(__file__).resolve().parents[1]


class HermesDataTests(unittest.TestCase):
    def test_table_ii_values_and_units(self) -> None:
        data = load_hermes_b1(ROOT / "data/processed/hermes_b1/table_ii.csv")
        self.assertEqual(len(data.x), 6)
        self.assertAlmostEqual(data.x[0], 0.012)
        self.assertAlmostEqual(data.q2_gev2[-1], 4.69)
        self.assertAlmostEqual(data.b1[0], 0.1120)
        self.assertAlmostEqual(data.b1[-1], -0.0038)
        np.testing.assert_allclose(
            data.b1_total_uncertainty,
            np.hypot(data.b1_stat, data.b1_sys),
        )


if __name__ == "__main__":
    unittest.main()
