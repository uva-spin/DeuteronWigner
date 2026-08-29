from __future__ import annotations

from deuteron_wigner.bridge import hqcdlfgsource as c163


def test_frozen_authority_and_source_inventory():
    authority = c163.load_verified_hqcd_lfgsource_authority()
    assert authority["status"] == c163.STATUS
    assert authority["package_root"] == c163.PACKAGE_ROOT
    assert authority["C162_package_root"] == c163.C162_ROOT
    inventory = c163.source_artifact_inventory()
    assert inventory["count"] == 8
    assert inventory["hashes_verified"] is True
    assert all(row["present"] and row["hash_matches"] for row in inventory["rows"])


def test_all_descriptors_have_one_terminal_locator_status():
    crosswalk = c163.descriptor_source_crosswalk()
    assert crosswalk["descriptor_count"] == 25
    assert len(crosswalk["rows"]) == 25
    assert len({row["descriptor_id"] for row in crosswalk["rows"]}) == 25
    assert all(row["terminal_status"] == "SOURCE_LOCATOR_INCOMPLETE" for row in crosswalk["rows"])
    assert c163.missing_source_request_manifest()["count"] == 25


def test_no_execution_and_separate_coordinates():
    cert = c163.lfgsource_completeness_certificate()
    assert cert["exact_locators"] == 0
    assert cert["source_expression_capsules"] == 0
    assert cert["target_programs"] == 0
    assert cert["target_values"] == 0
    assert c163.source_coordinate_manifest()["coordinates_kept_separate"] == (
        "g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2"
    )
    assert c163.static_isolation_guard()["pass"] is True


def test_locator_and_capsule_fail_closed():
    descriptor_id = c163.descriptor_source_crosswalk()["rows"][0]["descriptor_id"]
    assert c163.source_locator_manifest(descriptor_id=descriptor_id)["locator_count"] == 0
    assert c163.source_locator_manifest(source_id="arxiv_0901.2599")["locator_count"] == 0
    assert c163.source_expression_capsule(descriptor_id)["capsule"] is None
    assert c163.expression_dependency_graph(descriptor_id)["nodes"] == ()


def test_384_focused_live_mutations_remain_closed():
    for index in range(384):
        result = c163.mutate_live_hqcdlfgsource(index)
        assert result["positive_gate"] is False
        assert result["must_fail_or_change_root"] is True
