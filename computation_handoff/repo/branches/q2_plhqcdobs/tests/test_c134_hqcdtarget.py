from deuteron_wigner.bridge.hqcdtarget import core as c

def test_fail_closed_authority():
    r=c.verify_hqcd_target_authority()
    assert not r["positive_gate"] and r["targets"]==4
    assert r["target_backed_calibration"]==0 and r["rank_deficit"]==11
    assert c.load_verified_hqcd_target_authority()["package_root"]==c.PACKAGE_ROOT

def test_four_capsules_and_adapters():
    assert c.target_manifest()["count"]==4
    for t in c.TARGETS:
        assert c.target_by_id(t)["target_class"]=="TARGET_AUTHORITY_UNAVAILABLE"
        assert c.target_value_semantics(t)["numerical_default"] is False
        assert c.scheme_adapter(t)["status"]=="TARGET_ADAPTER_INCOMPLETE"
    assert c.calibration_condition_manifest()["count"]==0

def test_join_and_isolation_mutations():
    for t in c.TARGETS:
        x=c.evaluate_target_condition(t,"K9_2_N8_b0.40")
        assert x["status"]=="TARGET_AUTHORITY_UNAVAILABLE"
    assert c.static_isolation_guard()["pass"]
    for i in range(384): assert not c.mutate_live_hqcdtarget(i)["positive_gate"]
