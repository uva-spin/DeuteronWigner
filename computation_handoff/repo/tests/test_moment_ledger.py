import numpy as np
import pytest
import json

from deuteron_wigner.moment_ledger import (
    EndpointCompletion,
    MomentObservable,
    TabulatedMomentInput,
    audit_sum_rule,
    audit_linear_sum_rule,
    evaluate_moment,
    local_power_endpoint_completion,
)


def source(observable, x, values, completion=None):
    return TabulatedMomentInput(
        species="q",
        flavor=2,
        mechanism="fixture",
        observable=observable,
        x=np.asarray(x),
        values=np.asarray(values),
        source="analytic polynomial fixture",
        endpoint_completion=completion,
    )


def test_number_and_momentum_powers_are_distinct():
    x = np.linspace(0.0, 1.0, 101)
    values = 6.0 * x * (1.0 - x)
    number = evaluate_moment(source(MomentObservable.NUMBER, x, values))
    momentum = evaluate_moment(source(MomentObservable.MOMENTUM, x, values))
    assert number.total == pytest.approx(1.0, abs=2e-8)
    assert momentum.total == pytest.approx(0.5, abs=2e-8)
    assert number.support_complete and momentum.support_complete


def test_gluon_tensor_local_moment_can_require_explicit_x_weight():
    x = np.linspace(0.0, 1.0, 101)
    values = 6.0 * x * (1.0 - x)
    weighted = evaluate_moment(TabulatedMomentInput(
        species="g", flavor=21, mechanism="fixture",
        observable=MomentObservable.TENSOR, x=x, values=values,
        source="analytic fixture", x_power_override=1,
    ))
    assert weighted.x_power == 1
    assert weighted.total == pytest.approx(0.5, abs=2e-8)


def test_truncated_table_integrates_but_refuses_sum_rule_claim():
    x = np.linspace(0.1, 0.9, 81)
    entry = evaluate_moment(source(MomentObservable.NUMBER, x, np.ones_like(x)))
    assert not entry.support_complete
    assert entry.tabulated_integral == pytest.approx(0.8)
    with pytest.raises(ValueError, match="incomplete x support"):
        audit_sum_rule("number", [entry], expected=1.0, tolerance=1e-12)


def test_explicit_endpoint_completion_enables_auditable_claim():
    x = np.linspace(0.1, 0.9, 81)
    completion = EndpointCompletion(
        corrections={MomentObservable.NUMBER: 0.2},
        source="analytic constant tails",
        uncertainty_description="exact fixture",
    )
    entry = evaluate_moment(
        source(MomentObservable.NUMBER, x, np.ones_like(x), completion)
    )
    audit = audit_sum_rule("number", [entry], expected=1.0, tolerance=1e-12)
    assert entry.support_complete
    assert audit.passed
    assert audit.residual == pytest.approx(0.0, abs=1e-15)


def test_completion_for_wrong_observable_does_not_close_support():
    completion = EndpointCompletion(
        corrections={MomentObservable.NUMBER: 0.1},
        source="fixture",
        uncertainty_description="fixture",
    )
    entry = evaluate_moment(
        source(
            MomentObservable.MOMENTUM,
            np.linspace(0.1, 0.9, 9),
            np.ones(9),
            completion,
        )
    )
    assert not entry.support_complete


def test_local_power_completion_recovers_integrable_polynomial_tails():
    x = np.linspace(0.001, 0.95, 301)
    partial = source(MomentObservable.NUMBER, x, 6.0 * x * (1.0 - x))
    completion = local_power_endpoint_completion(partial, points=4)
    completed = evaluate_moment(source(
        MomentObservable.NUMBER, x, partial.values, completion
    ))
    assert completed.support_complete
    assert completed.total == pytest.approx(1.0, rel=3e-3)


def test_signed_linear_sum_rule_represents_valence_combination():
    x = np.linspace(0.0, 1.0, 101)
    q = evaluate_moment(source(MomentObservable.NUMBER, x, 4 * np.ones_like(x)))
    qbar = evaluate_moment(source(MomentObservable.NUMBER, x, np.ones_like(x)))
    audit = audit_linear_sum_rule(
        "valence", ((1.0, q), (-1.0, qbar)), expected=3.0, tolerance=1e-12
    )
    assert audit.passed


def test_production_moment_audit_closes_valence_and_all_parton_momentum():
    with open("outputs/validation/av18_parent_moment_coverage.json") as stream:
        report = json.load(stream)
    assert report["valence_number_sum_rule"]["passed"]
    assert report["all_parton_momentum_sum_rule"]["passed"]
    assert report["all_parton_momentum_sum_rule"]["active_flavors"] == [
        -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 21
    ]
    gluon = [entry for entry in report["entries"] if entry["species"] == "g"]
    by_observable = {entry["observable"]: entry for entry in gluon}
    assert by_observable["momentum"]["support_complete"]
    assert by_observable["helicity"]["support_complete"]
    assert by_observable["tensor"]["support_complete"]
    assert by_observable["tensor"]["x_power"] == 1
    for path in (
        "outputs/parent_tmds/all_parton_av18_momentum_q5.metadata.json",
        "outputs/parent_tmds/gluon_av18_helicity_moments_q5.metadata.json",
    ):
        with open(path) as stream:
            metadata = json.load(stream)
        assert metadata["scale_GeV"] == 5.0
        assert len(metadata["x_grid"]) == 37
