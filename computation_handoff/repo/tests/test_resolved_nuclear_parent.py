import numpy as np

from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.resolved_nuclear_parent import (
    ResolvedGluonNuclearParent,
    ResolvedQuarkNuclearParent,
)


def qparent(scale):
    eye = scale*np.eye(3, dtype=complex)
    return Spin1QuarkCorrelator(
        eye, 0.1*eye, np.stack((0.02*eye, -0.01*eye))
    )


def test_resolved_quark_parent_preserves_constituents_and_closure():
    resolved = ResolvedQuarkNuclearParent(
        qparent(1.0), qparent(2.0), qparent(3.2)
    )
    assert set(resolved.components()) == {
        "proton_in_deuteron", "neutron_in_deuteron", "nucleon_sum",
        "proton_minus_neutron", "nuclear_correction",
        "canonical_spin1_total",
    }
    assert resolved.closure_residual() < 1e-14
    assert not np.allclose(
        resolved.proton.vector, resolved.neutron.vector
    )


def test_resolved_gluon_parent_preserves_constituents_and_closure():
    p = Spin1GluonCorrelator(np.eye(6).reshape(3, 2, 3, 2).transpose(0, 2, 1, 3))
    n = Spin1GluonCorrelator(2*p.values)
    total = Spin1GluonCorrelator(3.1*p.values)
    resolved = ResolvedGluonNuclearParent(p, n, total)
    assert resolved.closure_residual() < 1e-14
    assert not np.allclose(
        resolved.proton_minus_neutron.values, 0.0
    )
