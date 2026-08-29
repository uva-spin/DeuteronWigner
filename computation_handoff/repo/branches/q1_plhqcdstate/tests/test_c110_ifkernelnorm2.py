from deuteron_wigner.bridge.ifkernelnorm2 import *
from deuteron_wigner.bridge.ifkernel2.core import pilot_coordinates

def test_c110_positive_normalization_and_boost_invariance():
    out = verify_ifkernel_normalization_authority()
    assert out["status"] == STATUS and out["pass"]
    for c in pilot_coordinates():
        p = corrected_pminus_kernel_record(c); m = corrected_m2_kernel_record(c)
        assert p["units"] == "GeV/g_s^2" and m["units"] == "GeV^2/g_s^2"
        assert p["bound"] >= 0 and m["bound"] >= 0
        assert verify_contact_boost_covariance(c)["pass"]

def test_c110_mutations_fail_closed():
    failures = 0
    c = pilot_coordinates()[0]
    for i in range(384):
        try:
            if i % 3 == 0: corrected_m2_kernel_record(type(c)(**{**c.__dict__, "resolution":"MUTATED"}))
            elif i % 3 == 1: corrected_m2_kernel_record(type(c)(**{**c.__dict__, "zero_mode_policy":"EPSILON"}))
            else: corrected_m2_kernel_record("bad")
        except (KeyError, ValueError, TypeError): failures += 1
    assert failures == 384

def test_c110_public_normalization_records_are_symbolic_and_frozen():
    c = pilot_coordinates()[0]
    field = gluon_field_normalization(c.g_in, c.resolution)
    state = qg_state_normalization(c.id, c.resolution)
    ancestry = normalization_ancestry(c)
    assert field["k_plus"] == "pi*k/L"
    assert field["mass_dimension"] == "GeV^-1/2"
    assert state["qg_gram"] == "delta_{ij}"
    assert ancestry["factor_ownership"] == "exactly-once"
    try:
        field["k_plus"] = "0"
        raise AssertionError("field record was mutable")
    except TypeError:
        pass
