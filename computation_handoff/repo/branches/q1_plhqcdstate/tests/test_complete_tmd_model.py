import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.complete_tmd_model import (
    CompleteSpin1TMDModel,
    GaugeLink,
    PredictionStatus,
)
from deuteron_wigner.gtmd import Species
from deuteron_wigner.registry import (
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)


class CompleteSpin1TMDModelTests(unittest.TestCase):
    def setUp(self):
        self.model = CompleteSpin1TMDModel(
            leading_twist_gluon_registry(),
            mass=1.8756,
            width=0.3,
            f1_anchor=lambda x, q: 4.0 * x * (1.0 - x),
            g1_anchor=lambda x, q: 0.2 * 4.0 * x * (1.0 - x),
            f1ll_anchor=lambda x, q: -0.01 * 4.0 * x * (1.0 - x),
            structural_zeros=frozenset(("h1TT",)),
        )

    def test_complete_gluon_basis_is_returned(self):
        values = self.model.predict_all(
            x=0.2, k=0.4, scale=2.0, gauge_link=GaugeLink.FUTURE
        )
        self.assertEqual(len(values), 19)
        self.model.require_modulation_bounds(values)
        self.model.require_block_budgets(values)

    def test_t_odd_process_sign_reversal(self):
        entry = leading_twist_gluon_registry().get(
            Species.GLUON, "f1Tperp"
        )
        future = self.model.predict(
            entry, x=0.2, k=0.3, scale=2.0, gauge_link=GaugeLink.FUTURE
        )
        past = self.model.predict(
            entry, x=0.2, k=0.3, scale=2.0, gauge_link=GaugeLink.PAST
        )
        self.assertAlmostEqual(future.central, -past.central)
        self.assertAlmostEqual(future.lower, -past.upper)

    def test_direct_rank_two_input_uses_physical_weight(self):
        model = CompleteSpin1TMDModel(
            leading_twist_gluon_registry(),
            mass=2.0,
            width=0.3,
            f1_anchor=lambda x, q: 1.0,
            direct_tmds={
                "f1": lambda x, k, q: (4.0, 3.8, 4.2),
                "h1perp": lambda x, k, q: (2.0, 1.5, 2.5),
            },
        )
        value = model.predict_all(
            x=0.2, k=1.0, scale=2.0, gauge_link=GaugeLink.FUTURE
        )["h1perp"]
        self.assertAlmostEqual(value.physical_ratio_central, 0.125)

    def test_structural_zero_is_exact(self):
        value = self.model.predict_all(
            x=0.2, k=0.4, scale=2.0, gauge_link=GaugeLink.FUTURE
        )["h1TT"]
        self.assertEqual(value.status, PredictionStatus.STRUCTURAL_ZERO)
        self.assertEqual(value.upper, 0.0)

    def test_quark_and_antiquark_registries_are_complete(self):
        for species in (Species.QUARK, Species.ANTIQUARK):
            model = CompleteSpin1TMDModel(
                leading_twist_quark_registry(species),
                mass=1.8756,
                width=0.25,
                f1_anchor=lambda x, q: 1.0,
            )
            values = model.predict_all(
                x=0.3, k=0.5, scale=3.0, gauge_link=GaugeLink.FUTURE
            )
            self.assertEqual(len(values), 18)
            model.require_modulation_bounds(values)
            model.require_block_budgets(values)

    def test_rank_coefficients_have_bounded_physical_modulations(self):
        for k in (0.0, 0.2, 0.5, 1.0, 2.0, 5.0):
            values = self.model.predict_all(
                x=0.2, k=k, scale=2.0, gauge_link=GaugeLink.FUTURE
            )
            self.model.require_modulation_bounds(values)
            self.model.require_block_budgets(values)

    def test_rank_zero_h1lt_has_zero_unweighted_integral(self):
        model = CompleteSpin1TMDModel(
            leading_twist_quark_registry(Species.QUARK),
            mass=1.8756,
            width=0.25,
            f1_anchor=lambda x, q: 1.0,
        )
        entry = model.registry.get(Species.QUARK, "h1LT")
        k = np.linspace(0.0, 4.0, 4001)
        values = np.asarray(
            [
                model.predict(
                    entry,
                    x=0.2,
                    k=float(momentum),
                    scale=2.0,
                    gauge_link=GaugeLink.FUTURE,
                ).central
                for momentum in k
            ]
        )
        self.assertAlmostEqual(
            2.0 * np.pi * simpson(k * values, x=k), 0.0, places=9
        )


if __name__ == "__main__":
    unittest.main()
