import numpy as np
import pytest

from deuteron_wigner.gauge_link_phase import (
    QuarkEikonalPhaseModel,
    simple_staple_orientation,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.provenance import EvidenceClass, ValidityDomain


def phase_model():
    amplitudes = {
        "f1Tperp": lambda nucleon, flavor, x, k, q: (1 + 0.1 * flavor) * np.exp(-k),
        "h1perp": lambda nucleon, flavor, x, k, q: (2 - 0.05 * flavor) * np.exp(-2 * k),
    }
    phases = {
        "f1Tperp": lambda nucleon, flavor, x, k, q: 0.1 * flavor * x,
        "h1perp": lambda nucleon, flavor, x, k, q: -0.07 * flavor * (1 - x),
    }
    return QuarkEikonalPhaseModel(
        amplitudes,
        phases,
        source="controlled eikonal interference fixture",
        validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5, process="SIDIS"),
        uncertainty_kind="independent operator/flavor phase parameters",
    )


def test_independent_operator_phases_generate_distinct_nonzero_boundaries():
    model = phase_model()
    sivers = model.fitted_input("f1Tperp")
    boer = model.fitted_input("h1perp")
    s = sivers.value("proton", 2, 0.1, 0.3, 5.0)
    b = boer.value("proton", 2, 0.1, 0.3, 5.0)
    assert s != 0.0
    assert b != 0.0
    assert s != b
    assert sivers.provenance.evidence == EvidenceClass.MODEL


def test_phase_zero_is_exact_controlled_limit():
    model = phase_model()
    zero = QuarkEikonalPhaseModel(
        model.reference_amplitudes,
        {name: (lambda nucleon, flavor, x, k, q: 0.0) for name in model.phases},
        source=model.source,
        validity=model.validity,
        uncertainty_kind=model.uncertainty_kind,
    )
    for operator in ("f1Tperp", "h1perp"):
        assert zero.future_value(operator, "proton", 2, 0.1, 0.3, 5.0) == 0.0


def test_simple_staples_reverse_and_mixed_links_fail_closed():
    assert simple_staple_orientation(GaugeLink("+", "+")) == 1.0
    assert simple_staple_orientation(GaugeLink("-", "-")) == -1.0
    with pytest.raises(ValueError, match="mixed"):
        simple_staple_orientation(GaugeLink("+", "-"))
