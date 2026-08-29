import unittest

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.complete_tmd_model import GaugeLink
from deuteron_wigner.correlator_tmd_model import (
    CollinearAnchors,
    CorrelatorParameters,
    ReducedCorrelatorTMDModel,
)
from deuteron_wigner.gtmd import Species
from deuteron_wigner.registry import (
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)


class ReducedCorrelatorTMDModelTests(unittest.TestCase):
    def model(self, species):
        registry = (
            leading_twist_gluon_registry()
            if species == Species.GLUON
            else leading_twist_quark_registry(species)
        )
        return ReducedCorrelatorTMDModel(
            registry,
            species,
            CollinearAnchors(f1=4.0, g1=0.8, f1ll=-0.08, h1=0.6),
        )

    def test_complete_species_bases(self):
        for species, count in (
            (Species.GLUON, 19),
            (Species.QUARK, 18),
            (Species.ANTIQUARK, 18),
        ):
            model = self.model(species)
            values = model.predict_all(
                k=0.4, scale=5.0, gauge_link=GaugeLink.FUTURE
            )
            self.assertEqual(len(values), count)
            model.require_physical_bounds(values)

    def test_all_positive_rank_modulations_vanish_at_origin(self):
        model = self.model(Species.GLUON)
        values = model.predict_all(k=0.0, scale=5.0, gauge_link=GaugeLink.FUTURE)
        entries = {entry.name: entry for entry in model.registry.select()}
        for name, prediction in values.items():
            if entries[name].transverse_rank > 0:
                self.assertEqual(prediction.physical_ratio, 0.0)

    def test_t_odd_sign_reverses_and_t_even_does_not(self):
        model = self.model(Species.QUARK)
        future = model.predict_all(k=0.4, scale=5.0, gauge_link=GaugeLink.FUTURE)
        past = model.predict_all(k=0.4, scale=5.0, gauge_link=GaugeLink.PAST)
        for entry in model.registry.select():
            sign = -1.0 if entry.t_odd else 1.0
            self.assertAlmostEqual(future[entry.name].value, sign * past[entry.name].value)

    def test_rank_zero_t_odd_integral_is_zero(self):
        model = self.model(Species.QUARK)
        entry = model.registry.get(Species.QUARK, "h1LT")
        k = np.linspace(0.0, 5.0, 6001)
        values = np.asarray(
            [
                model.predict(
                    entry, k=float(kk), scale=5.0, gauge_link=GaugeLink.FUTURE
                ).value
                for kk in k
            ]
        )
        self.assertAlmostEqual(2 * np.pi * simpson(k * values, x=k), 0.0, places=9)

    def test_shared_parameter_changes_correlated_channels(self):
        base = self.model(Species.GLUON)
        changed = ReducedCorrelatorTMDModel(
            base.registry,
            Species.GLUON,
            base.anchors,
            CorrelatorParameters(d_probability=0.08),
        )
        a = base.predict_all(k=0.5, scale=5.0, gauge_link=GaugeLink.FUTURE)
        b = changed.predict_all(k=0.5, scale=5.0, gauge_link=GaugeLink.FUTURE)
        self.assertNotEqual(a["g1T"].value, b["g1T"].value)
        self.assertNotEqual(a["f1LT"].value, b["f1LT"].value)


if __name__ == "__main__":
    unittest.main()
