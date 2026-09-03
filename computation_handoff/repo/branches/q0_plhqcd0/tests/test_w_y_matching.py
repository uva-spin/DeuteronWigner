import unittest

import numpy as np

from deuteron_wigner.w_y_matching import (
    FixedOrderYRemainder,
    LowQTValidity,
    MatchedWPlusYObservable,
    MatchingOverlapEvidence,
    assess_matching_overlap,
)


class WYMatchingTests(unittest.TestCase):
    def test_w_only_is_limited_to_declared_low_qt_domain(self):
        observable = MatchedWPlusYObservable(lambda qt: 2.0 - qt)
        result = observable.evaluate(0.5, 5.0)
        self.assertEqual(result["mode"], "W_only_low_qT")
        self.assertEqual(result["value"], 1.5)
        with self.assertRaisesRegex(ValueError, "outside"):
            observable.evaluate(1.5, 5.0)

    def test_process_y_term_extends_domain_and_retains_provenance(self):
        y = FixedOrderYRemainder(
            response=lambda qt, q: 0.1 * qt / q,
            process="synthetic SIDIS validation",
            perturbative_order="NLO fixture",
            source="analytic unit-test fixture",
            subtraction_convention="Y=FO-asymptotic fixture",
            overlap_evidence=MatchingOverlapEvidence(
                passed=True, contiguous_points=3,
                maximum_relative_difference=0.1,
                qT_interval_gev=(1.0, 2.0), source="fixture",
            ),
        )
        result = MatchedWPlusYObservable(
            lambda qt: 1.0, y_term=y
        ).evaluate(2.0, 5.0)
        self.assertEqual(result["mode"], "W_plus_Y")
        self.assertFalse(result["inside_W_domain"])
        self.assertAlmostEqual(result["value"], 1.04)
        self.assertEqual(result["y_provenance"]["process"], y.process)

    def test_y_term_rejects_missing_provenance(self):
        with self.assertRaises(ValueError):
            FixedOrderYRemainder(
                response=lambda qt, q: 0.0,
                process="", perturbative_order="NLO",
                source="fixture", subtraction_convention="FO-asymptotic",
            )

    def test_qt_over_q_boundary_is_enforced(self):
        validity = LowQTValidity(maximum_qt_over_q=0.2, maximum_qt_gev=2.0)
        self.assertTrue(validity.contains(0.9, 5.0))
        self.assertFalse(validity.contains(1.1, 5.0))

    def test_overlap_requires_contiguous_same_sign_agreement(self):
        evidence = assess_matching_overlap(
            qt_gev=np.asarray((0.5, 1.0, 1.5, 2.0, 2.5)),
            w_resummed=np.asarray((3.0, 2.0, 1.5, 1.0, 0.5)),
            asymptotic=np.asarray((1.0, 1.9, 1.4, 1.05, -0.5)),
            q_gev=5.0, source="analytic fixture",
        )
        self.assertTrue(evidence.passed)
        self.assertEqual(evidence.contiguous_points, 3)

    def test_failed_overlap_blocks_high_qt_even_with_y_callable(self):
        failed = MatchingOverlapEvidence(
            passed=False, contiguous_points=1,
            maximum_relative_difference=0.9,
            qT_interval_gev=(1.0, 1.0), source="failed fixture",
        )
        y = FixedOrderYRemainder(
            response=lambda qt, q: 0.0, process="SIDIS fixture",
            perturbative_order="NLO", source="fixture",
            subtraction_convention="FO-asymptotic",
            overlap_evidence=failed,
        )
        with self.assertRaisesRegex(ValueError, "overlap"):
            MatchedWPlusYObservable(lambda qt: 1.0, y_term=y).evaluate(2.0, 5.0)


if __name__ == "__main__":
    unittest.main()
