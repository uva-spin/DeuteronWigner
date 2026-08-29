import unittest

import numpy as np

from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)


class GluonTMDEvolutionTests(unittest.TestCase):
    @staticmethod
    def alpha_s(scale):
        return 0.25

    @staticmethod
    def unpolarized(x, scale):
        return 2.0 + 0.1 * scale

    @staticmethod
    def helicity(x, scale):
        return 0.25 * GluonTMDEvolutionTests.unpolarized(x, scale)

    def test_zero_b_has_no_evolution(self):
        evolution = OneLoopGluonCSSEvolution(self.alpha_s)
        self.assertEqual(evolution.factor(0.0, 0.0, 5.0), 1.0)
        self.assertEqual(evolution.canonical_scale(0.0, 5.0), 5.0)

    def test_canonical_scale_is_bounded(self):
        evolution = OneLoopGluonCSSEvolution(self.alpha_s)
        self.assertLessEqual(evolution.canonical_scale(0.1, 10.0), 10.0)
        self.assertGreaterEqual(evolution.canonical_scale(20.0, 10.0), 1.3)

    def test_nonperturbative_profiles_are_ordered(self):
        factors = []
        for profile in (
            NonperturbativeCSProfile.LOW,
            NonperturbativeCSProfile.CENTRAL,
            NonperturbativeCSProfile.HIGH,
        ):
            evolution = OneLoopGluonCSSEvolution(
                self.alpha_s,
                GluonCSSEvolutionConfig(cs_profile=profile),
            )
            factors.append(evolution.factor(2.0, 1.0, 10.0))
        self.assertGreater(factors[0], factors[1])
        self.assertGreater(factors[1], factors[2])

    def test_spin_independent_evolution_preserves_g1_over_f1(self):
        boundary = MatchedGluonTMD(
            self.unpolarized,
            self.alpha_s,
            helicity_gluon_pdf=self.helicity,
            config=GluonTMDMatchingConfig(profile=LargeBProfile.CENTRAL),
        )
        model = EvolvedMatchedGluonTMD(
            boundary, OneLoopGluonCSSEvolution(self.alpha_s)
        )
        values = model.values(0.2, 1.5, 8.0)
        self.assertAlmostEqual(values.g1 / values.f1, 0.25)
        self.assertGreater(values.evolution_factor, 0.0)

    def test_reference_scale_rejects_backward_np_evolution(self):
        evolution = OneLoopGluonCSSEvolution(
            self.alpha_s,
            GluonCSSEvolutionConfig(
                cs_profile=NonperturbativeCSProfile.CENTRAL
            ),
        )
        with self.assertRaises(ValueError):
            evolution.factor(1.0, 0.8, 1.5)

    def test_metadata_marks_intermediate_accuracy(self):
        evolution = OneLoopGluonCSSEvolution(self.alpha_s)
        self.assertFalse(evolution.metadata["production_ready"])
        self.assertTrue(evolution.metadata["spin_independent"])


if __name__ == "__main__":
    unittest.main()
