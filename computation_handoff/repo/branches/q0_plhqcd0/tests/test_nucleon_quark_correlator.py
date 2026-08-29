import unittest

import numpy as np

from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    NucleonTMDComponent,
    NUCLEON_QUARK_TMD_NAMES,
)
from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


class FlavorResolvedNucleonQuarkTests(unittest.TestCase):
    def test_joint_density_matrix_detects_positive_and_unphysical_inputs(self):
        from deuteron_wigner.nucleon_quark_correlator import SpinHalfQuarkCorrelator

        identity = np.eye(2, dtype=np.complex128)
        zero = np.zeros((2, 2), dtype=np.complex128)
        physical = SpinHalfQuarkCorrelator(
            identity, 0.2 * np.diag((1.0, -1.0)),
            np.asarray((zero, zero)),
        )
        self.assertGreaterEqual(physical.minimum_positivity_eigenvalue(), 0.0)
        unphysical = SpinHalfQuarkCorrelator(
            identity, 1.2 * np.diag((1.0, -1.0)),
            np.asarray((zero, zero)),
        )
        self.assertLess(unphysical.minimum_positivity_eigenvalue(), 0.0)

    def model(self):
        provenance = ComponentProvenance(
            name="test input",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.NUCLEON_IMPULSE,
            sources=("synthetic unit test",),
            assumptions=("Gaussian radial fixture",),
            validity=ValidityDomain(0.01, 0.9, 1.0, 20.0, 2.0),
            uncertainty_kind="parameter scan",
            replaceable_interface="NucleonTMDComponent",
        )
        amplitudes = {
            name: (lambda flavor, x, q, index=index: (index + 1) * flavor * x)
            for index, name in enumerate(NUCLEON_QUARK_TMD_NAMES)
        }
        return FlavorResolvedNucleonQuarkModel(
            {
                name: NucleonTMDComponent(
                    value=value,
                    width_gev2={2: 0.22, 1: 0.31, -2: 0.27, -1: 0.34},
                    provenance=provenance,
                )
                for name, value in amplitudes.items()
            },
            nucleon_mass_gev=0.9389,
        )

    def test_flavor_values_and_widths_remain_distinct(self):
        model = self.model()
        u = model.tmd_values(
            flavor=2, x=0.2, k_x_gev=0.3, k_y_gev=0.0, scale_gev=3.0,
            gauge_link=GaugeLink("+", "+"),
        )
        d = model.tmd_values(
            flavor=1, x=0.2, k_x_gev=0.3, k_y_gev=0.0, scale_gev=3.0,
            gauge_link=GaugeLink("+", "+"),
        )
        self.assertNotEqual(u["f1"], d["f1"])
        self.assertNotEqual(u["g1"], d["g1"])

    def test_t_odd_sign_reversal_only(self):
        model = self.model()
        common = dict(
            flavor=2, x=0.2, k_x_gev=0.3, k_y_gev=0.1, scale_gev=3.0
        )
        future = model.tmd_values(**common, gauge_link=GaugeLink("+", "+"))
        past = model.tmd_values(**common, gauge_link=GaugeLink("-", "-"))
        for name in NUCLEON_QUARK_TMD_NAMES:
            sign = -1.0 if name in ("h1perp", "f1Tperp") else 1.0
            self.assertAlmostEqual(future[name], sign * past[name])

    def test_all_operator_projections_are_hermitian(self):
        model = self.model()
        correlator = model.correlator(
            flavor=2, x=0.2, k_x_gev=0.3, k_y_gev=-0.2,
            delta_x_gev=0.1, delta_y_gev=0.0, scale_gev=3.0,
            gauge_link=GaugeLink("+", "+"),
        )
        correlator.require_hermitian()

    def test_projection_adapter_preserves_flavor(self):
        model = self.model()
        adapter = model.projection_callable("gamma+", GaugeLink("+", "+"))
        u = adapter(2, 0.2, 0.3, 0.1, 0.0, 0.0, 3.0)
        d = adapter(1, 0.2, 0.3, 0.1, 0.0, 0.0, 3.0)
        self.assertFalse(np.allclose(u, d))


if __name__ == "__main__":
    unittest.main()
