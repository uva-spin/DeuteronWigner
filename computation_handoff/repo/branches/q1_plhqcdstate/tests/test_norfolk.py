import unittest

import numpy as np

from deuteron_wigner.wavefunctions.norfolk import (
    NORFOLK_MODELS,
    load_norfolk_coordinate,
    load_norfolk_momentum,
    norfolk_radial_callable,
)


class NorfolkWaveFunctionTests(unittest.TestCase):
    EXPECTED_D_STATE = {
        "nvia": 0.052411,
        "nvib": 0.054937,
        "nviia": 0.052212,
        "nviib": 0.052072,
    }

    def test_all_models_have_normalized_momentum_tables(self):
        for suffix, expected_d_state in self.EXPECTED_D_STATE.items():
            wave = load_norfolk_momentum(f"data/raw/norfolk/fdeut.{suffix}")
            self.assertEqual(wave.name, NORFOLK_MODELS[suffix].label)
            norm = np.trapz(
                wave.grid**2 * (wave.u**2 + wave.w**2), wave.grid
            )
            d_state = np.trapz(wave.grid**2 * wave.w**2, wave.grid)
            self.assertAlmostEqual(norm, 1.0, delta=3e-5)
            self.assertAlmostEqual(
                d_state, expected_d_state, delta=3e-6
            )
            self.assertGreaterEqual(wave.grid[-1], 20.0)
            radial = norfolk_radial_callable(wave)
            nodes, weights = np.polynomial.legendre.leggauss(160)
            momenta = 10.0 * (nodes + 1.0)
            continuous_norm = sum(
                10.0
                * weight
                * momentum**2
                * sum(value**2 for value in radial(float(momentum)))
                for momentum, weight in zip(momenta, weights)
            )
            self.assertAlmostEqual(continuous_norm, 1.0, delta=2e-4)

    def test_coordinate_tables_have_expected_coverage(self):
        for suffix in self.EXPECTED_D_STATE:
            wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{suffix}")
            self.assertLessEqual(wave.grid[0], 0.01)
            self.assertGreaterEqual(wave.grid[-1], 99.0)

    def test_rejects_unknown_model_suffix(self):
        with self.assertRaises(ValueError):
            load_norfolk_momentum("data/raw/av18/fdeut.av18")


if __name__ == "__main__":
    unittest.main()
