from deuteron_wigner.bridge.hqcdcond import core as c

def test_fail_closed_authority():
    r=c.verify_hqcd_condition_authority()
    assert not r["positive_gate"] and r["source_qualified_nonempty"]==0
    assert r["prospective_rank"]==0 and r["rank_deficit"]==11
    assert c.load_verified_hqcd_condition_authority()["package_root"]==c.PACKAGE_ROOT

def test_definition_target_split():
    for row in c.condition_manifest()["conditions"]:
        assert c.condition_definition_authority(row["condition_id"])["definition_present"]
        assert "target_class" in c.condition_target_authority(row["condition_id"])
        assert c.condition_compatibility(row["condition_id"])["adapter"] is False
    assert c.calibration_condition_manifest()["count"]==0

def test_routes_and_requests():
    assert c.primary_source_manifest()["hash_locked_local"]==1
    assert c.missing_condition_rank_manifest()["rank_deficit"]==11
    assert c.counterterm_condition_crosswalk()["directions"]
    assert c.missing_source_request_manifest()["count"]==4
    assert c.static_isolation_guard()["pass"]
    for i in range(384): assert not c.mutate_live_hqcdcond(i)["positive_gate"]
