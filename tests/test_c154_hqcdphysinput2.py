from deuteron_wigner.bridge import hqcdphysinput2 as c


def test_source_capsules_and_flavor_guard():
    assert c.STATUS == "C154_HQCDPHYSINPUT2_FLAVOR_IDENTITY_INCOMPLETE"
    assert c.PLAN == "PHYSINPUT2-B"
    assert len(c.numerical_source_manifest()["rows"]) == 5
    caps = c.accepted_standard_input_capsules()
    assert {x["quantity_id"] for x in caps} == {"light_quark_mass", "qcd_coupling"}
    assert {x["central_value"] for x in caps} == {"3.397", "0.1180"}
    for cap in caps:
        assert c.validate_numerical_input_capsule(cap)["capsule_root"] == cap["capsule_root"]
    assert c.flavor_mapping_decision()["classification"] == "PROJECT_FLAVOR_IDENTITY_INCOMPLETE"


def test_explicit_conversion_and_blocked_targets():
    assert c.input_covariance_manifest()["fabricated_zero"] is False
    assert c.matching_scale_manifest()["complete"] is False
    try:
        c.standard_to_fb_target("light_quark_mass", "K9", {"common_ir_id": "C43_TARGET_COMMON_IR_V1"}, "C154_STD_MUD_MSbar_2GeV_NL4")
    except RuntimeError as exc:
        assert "fail closed" in str(exc)
    else:
        raise AssertionError("blocked matching target was accepted")
    try:
        c.identified_coordinate_solution("K9", input_record_ids=(), matching_record_ids=())
    except RuntimeError:
        pass
    else:
        raise AssertionError("blocked physical solution was accepted")


def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        m = c.mutate_live_hqcdphysinput2(i)
        assert m["positive_gate"] is False and m["must_fail_or_change_root"] is True


def test_clean_reload():
    a = c.load_verified_hqcd_physical_input_authority()
    assert a["package_root"] == c.PACKAGE_ROOT
    assert a["C153_package_root"] == "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
