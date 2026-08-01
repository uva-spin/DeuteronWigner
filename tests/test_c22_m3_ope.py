import math

import pytest

from deuteron_wigner.matching.m3.core import *
from deuteron_wigner.matching.m3.injections import INJECTIONS


def test_plus_distribution_constant_and_moment():
    report = distribution_report()
    assert report["constant_plus_residual"] < 1e-12
    assert report["mellin_residual"] < 1e-11


def test_lower_limit_convention():
    assert distribution_report()["lower_limit_residual"] < 1e-11


def test_distribution_content_address_and_immutability():
    d = EndpointDistribution(DeltaEndpointTerm(1.0))
    assert len(d.content_hash) == 64
    with pytest.raises(Exception):
        d.delta = DeltaEndpointTerm(2.0)


def test_exact_rational_zeta_and_small_x_types():
    coefficient = ExactCoefficient((1, 3), ((2, (2, 1)),))
    assert abs(coefficient.value() - (1 / 3 + math.pi**2 / 3)) < 1e-14
    distribution = EndpointDistribution(small_x=(SmallXLogTerm(1, ExactCoefficient((1, 1))),))
    assert abs(distribution.mellin(1) + 1.0) < 1e-10


def test_hpl_domain_and_oracle():
    assert hpl_report("hash")["maximum_sample_residual"] == 0.0
    with pytest.raises(ValueError):
        HarmonicPolylogRecord((0,)).evaluate(1.2)


def test_gamma5_is_explicit():
    record = gamma5_record()
    assert record.singlet_nonsinglet_distinct
    assert "Z5" in record.finite_axial_renormalization


def test_splitting_sum_rules_and_routes():
    report = collinear_report()
    assert report["nonsinglet_number_residual"] < 1e-11
    assert report["singlet_momentum_residual"] < 1e-10
    assert report["xspace_mellin_residual"] < 1e-9


def test_coefficients_source_hashed_and_pretzelosity_distinct():
    hashes = {x: "h" for x in ("1702.06558", "1909.13820", "2509.01655", "1409.5131", "1805.07243", "2509.01703", "1908.03831")}
    records = coefficient_records(hashes)
    pretzel = next(r for r in records if r.target_operator.family == "PRETZEL")
    assert pretzel.status == "ZERO_COEFFICIENT_AT_DECLARED_TWIST_AND_ORDER"
    assert pretzel.expression.mellin(1) == 0.0


def test_rank_maps_are_not_scalar_aliased():
    report = rank_report()
    assert [r["bessel_order"] for r in report["rows"]] == [0, 1, 2, 3]
    with pytest.raises(ValueError):
        SmallBOPEMap("bad", 2, 0, "i^2", 0.938, "x", (0.02, 1.0)).validate()


def test_rg_route_first_omitted_order():
    report = rg_report()
    assert max(report["route_residuals"].values()) <= report["first_omitted_order_scale"]
    assert not report["overfit_to_zero"]


def test_capability_counts_preserve_baselines():
    report = operator_classification()
    assert len(report["rows"]) == 540
    assert report["c20_matching_executable"] == 492
    assert report["c20_matching_unavailable"] == 48
    assert report["c21_fully_evolvable"] == 438
    assert sum(report["counts"].values()) == 540


def test_unsupported_physics_fail_closed():
    gaps = unresolved_gaps()
    assert "TWIST3_SIVERS_QIU_STERMAN" in gaps
    assert "TRIGLUON_F" in gaps and "TRIGLUON_D" in gaps


def test_nuclear_ancestry_and_covariance():
    report = nuclear_report()
    assert report["ancestry_preserved"]
    assert max(report["hidden_color_rotation_residuals"]) < 1e-10
    assert report["component_variation"] > 0


def test_uncertainties_remain_separate():
    assert len(uncertainty_report()) == 19
    assert accuracy_report()["accuracy_laundering_rejected"]


def test_holdouts_frozen():
    report = holdout_report()
    assert len(report["classes"]) == 12
    assert report["frozen_before_final_tuning"] and not report["used_for_calibration"]


def test_injections_and_readiness_isolation():
    assert len(INJECTIONS) == 720
    assert len({row[0] for row in INJECTIONS}) == 720
    report = readiness_report()
    assert not report["production_reachable"] and not report["process_reachable"]
    assert "PROCESS_FACTORIZATION_READY" in report["not_issued"]
