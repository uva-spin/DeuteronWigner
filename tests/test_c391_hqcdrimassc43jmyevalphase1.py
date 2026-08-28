from deuteron_wigner.bridge import hqcdrimassc43jmyevalphase1 as c


def test_fourier_authority():
    row = c.fourier_bessel_manifest("JMY_SCALAR_TRANSVERSE_RANK0")
    assert row["d_perp"] == "2-2*epsilon" and row["bessel_order"] == "-epsilon"


def test_plus_constant():
    row = c.regular_plus_manifest("DR.qv", "JMY_FIG2B_PLUS")
    assert c.apply_distribution_test_action(row, {"polynomial_coefficients": [1]})["fixture_action"] == "0/1"


def test_first_node():
    assert c.first_node_manifest()["executable"]
    result = c.evaluate_first_node({"epsilon": "0", "bT": "1", "kT": "2", "test_function": {"polynomial_coefficients": [1, 2]}})
    assert result["node"] == "DR.qq" and not result["physical"]


def test_groups_and_separator():
    assert len(c.group_laurent_manifest()) == 16
    assert c.separator_manifest("PLUS_CONSTANT_ANNIHILATION")["status"] == "EXACT"
    assert c.phase_release_manifest()["target_remainder_explicit"]


def test_reload_and_mutations():
    assert not c.load_verified_jmy_eval_phase1_authority()["physical"]
    assert all(c.mutate_live_hqcdrimassc43jmyevalphase1(i)["pass"] for i in range(384))
