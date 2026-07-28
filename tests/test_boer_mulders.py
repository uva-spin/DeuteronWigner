import pytest

from deuteron_wigner.boer_mulders import BoerMuldersFromSiversModel
from deuteron_wigner.nucleon_inputs import FittedMomentumTMDInput
from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


def synthetic_sivers():
    return FittedMomentumTMDInput(
        response=lambda nucleon, flavor, x, k, q: flavor * x * (1.0 + k),
        provenance=ComponentProvenance(
            name="synthetic fitted Sivers",
            evidence=EvidenceClass.PHENOMENOLOGY,
            mechanism=Mechanism.NUCLEON_IMPULSE,
            sources=("unit-test source",),
            assumptions=("future staple",),
            validity=ValidityDomain(0.01, 0.25, 1.5, 10.0, 1.5, process="SIDIS"),
            uncertainty_kind="synthetic replicas",
            replaceable_interface="FittedMomentumTMDInput",
        ),
        process_reference="SIDIS future-pointing gauge link",
    )


def test_boer_mulders_model_is_flavor_and_operator_resolved():
    source = synthetic_sivers()
    model = BoerMuldersFromSiversModel(source)
    fitted = model.fitted_input()
    values = {
        flavor: fitted.value("proton", flavor, 0.1, 0.4, 5.0)
        for flavor in (2, 1, -2, -1)
    }
    assert values[2] != values[1]
    assert values[-2] != values[-1]
    assert values[2] == pytest.approx(
        2.0 * source.value("proton", 2, 0.1, 0.4, 5.0)
    )
    assert fitted.provenance.evidence == EvidenceClass.MODEL
    assert "joint Boer--Mulders/Sivers fit covariance" in " ".join(
        fitted.provenance.assumptions
    )


def test_neutron_is_charge_rotated_without_collapsing_flavors():
    fitted = BoerMuldersFromSiversModel(synthetic_sivers()).fitted_input()
    assert fitted.value("neutron", 2, 0.1, 0.4, 5.0) == pytest.approx(
        fitted.value("proton", 1, 0.1, 0.4, 5.0)
    )
    assert fitted.value("neutron", 1, 0.1, 0.4, 5.0) == pytest.approx(
        fitted.value("proton", 2, 0.1, 0.4, 5.0)
    )


def test_coefficient_sensitivities_are_independent():
    model = BoerMuldersFromSiversModel(synthetic_sivers())
    intervals = {flavor: model.coefficient_interval(flavor) for flavor in (2, 1, -2, -1)}
    assert len(set(intervals.values())) == 4
