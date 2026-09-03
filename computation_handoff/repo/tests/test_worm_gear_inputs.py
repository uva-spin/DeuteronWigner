import pytest

from deuteron_wigner.provenance import EvidenceClass, ValidityDomain
from deuteron_wigner.worm_gear_inputs import (
    PretzelosityMomentModel,
    WWBreakingModel,
    Yang2024G1TInput,
    positivity_informed_pretzelosity_model,
)


def test_ww_zero_breaking_recovers_separate_ww_limits():
    zeros = {f: (lambda flavor, x, q: 0.0) for f in (2, 1, -2, -1)}
    model = WWBreakingModel(
        g1t_ww=lambda flavor, x, q: flavor * x,
        h1lperp_ww=lambda flavor, x, q: -2 * flavor * x,
        g1t_breaking=zeros,
        h1lperp_breaking=zeros,
        source="controlled WW-breaking fixture",
        validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
        uncertainty_kind="named genuine-twist-3 scenarios",
    )
    assert model.g1t_input().value("proton", 2, 0.1, 5.0) == pytest.approx(0.2)
    assert model.h1lperp_input().value("proton", 2, 0.1, 5.0) == pytest.approx(-0.4)


def test_independent_breaking_and_neutron_rotation():
    gbreak = {f: (lambda flavor, x, q, f=f: 0.01 * f) for f in (2, 1, -2, -1)}
    hbreak = {f: (lambda flavor, x, q, f=f: -0.03 * f) for f in (2, 1, -2, -1)}
    model = WWBreakingModel(
        g1t_ww=lambda flavor, x, q: flavor * x,
        h1lperp_ww=lambda flavor, x, q: -2 * flavor * x,
        g1t_breaking=gbreak,
        h1lperp_breaking=hbreak,
        source="controlled WW-breaking fixture",
        validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
        uncertainty_kind="named genuine-twist-3 scenarios",
    )
    g = model.g1t_input()
    h = model.h1lperp_input()
    assert g.value("proton", 2, 0.1, 5.0) != h.value("proton", 2, 0.1, 5.0)
    assert g.value("neutron", 2, 0.1, 5.0) == pytest.approx(
        g.value("proton", 1, 0.1, 5.0)
    )


def test_flavor_resolved_pretzelosity_adapter():
    model = PretzelosityMomentModel(
        moments={
            f: (lambda flavor, x, q, f=f: 0.1 * f * x * (1 - x))
            for f in (2, 1, -2, -1)
        },
        source="model/lattice replacement fixture",
        evidence=EvidenceClass.LATTICE,
        validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
        uncertainty_kind="correlated lattice-model ensemble",
    )
    fitted = model.fitted_input()
    assert fitted.value("proton", 2, 0.1, 5.0) != fitted.value(
        "proton", 1, 0.1, 5.0
    )
    assert fitted.value("neutron", 2, 0.1, 5.0) == pytest.approx(
        fitted.value("proton", 1, 0.1, 5.0)
    )
    assert fitted.provenance.evidence == EvidenceClass.LATTICE


def test_yang_2024_g1t_preserves_fitted_flavor_signs_and_sea_boundary():
    fitted = Yang2024G1TInput().fitted_input()
    assert fitted.value("proton", 2, 0.2, 5.0) > 0.0
    assert fitted.value("proton", 1, 0.2, 5.0) < 0.0
    assert fitted.value("proton", -2, 0.2, 5.0) == 0.0
    assert fitted.value("proton", -1, 0.2, 5.0) == 0.0
    assert fitted.value("neutron", 2, 0.2, 5.0) == pytest.approx(
        fitted.value("proton", 1, 0.2, 5.0)
    )
    assert "sea-zero" in " ".join(fitted.provenance.assumptions)


def test_yang_2024_published_interval_hull_is_explicitly_not_replicas():
    central = Yang2024G1TInput()
    members = central.published_interval_members()
    assert len(members) == 16
    values = [
        member.fitted_input().value("proton", 2, 0.2, 2.0)
        for member in members
    ]
    center = central.fitted_input().value("proton", 2, 0.2, 2.0)
    assert min(values) < center < max(values)


def test_default_pretzelosity_scenario_is_flavor_resolved_and_bounded():
    model = positivity_informed_pretzelosity_model(
        unpolarized=lambda flavor, x, q: 2.0 + 0.1 * flavor,
        helicity=lambda flavor, x, q: 0.2 * flavor,
        widths_gev2={2: 0.23, 1: 0.27, -2: 0.34, -1: 0.36},
    )
    fitted = model.fitted_input()
    values = {
        flavor: fitted.value("proton", flavor, 0.1, 5.0)
        for flavor in (2, 1, -2, -1)
    }
    assert values[2] < 0.0 < values[1]
    assert values[-2] < 0.0 < values[-1]
    assert len(set(values.values())) == 4
