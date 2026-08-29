from deuteron_wigner.controlled_limits import run_controlled_limit_audit


def test_common_controlled_limit_audit_covers_all_named_tmds_and_passes():
    checks = run_controlled_limit_audit()
    assert len(checks) == 6
    assert all(check.passed for check in checks)
    assert all(check.compared_named_tmds == 18 for check in checks)
    assert {check.name for check in checks} == {
        "free_proton_switch",
        "free_neutron_switch",
        "pure_s_zero_d",
        "no_melosh_at_rest",
        "zero_quark_nuclear_corrections",
        "zero_gluon_nuclear_corrections",
    }

