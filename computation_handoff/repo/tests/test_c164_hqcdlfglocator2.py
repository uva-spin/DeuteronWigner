"""C164 authenticated-PDF locator boundary and fail-closed tests."""
from collections import Counter

from deuteron_wigner.bridge import hqcdlfglocator2 as c


def test_authority_loads_and_authenticates_eight_local_sources():
    authority = c.load_verified_hqcd_lfglocator2_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGLOCATOR2-D"
    assert authority["package_root"] == c.PACKAGE_ROOT
    inventory = c.source_version_manifest()
    assert inventory["count"] == 8
    assert inventory["hashes_verified"] is True
    assert all(row["actual_sha256"] == row["sha256"] for row in inventory["rows"])
    assert c.pdf_printed_page_map()["page_count"] == 206


def test_all_descriptors_have_one_terminal_status_and_missing_object():
    crosswalk = c.descriptor_locator_crosswalk()
    assert crosswalk["descriptor_count"] == 25
    assert len({row["descriptor_id"] for row in crosswalk["rows"]}) == 25
    assert all(row["terminal_status"] and row["exact_first_missing_object"] for row in crosswalk["rows"])
    assert Counter(row["terminal_status"] for row in crosswalk["rows"]) == {
        "FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES": 13,
        "DEPENDENCY_LOCATOR_INCOMPLETE": 8,
        "SOURCE_ROLE_MISMATCH": 4,
    }
    assert c.absence_certificate_manifest()["count"] == 17
    assert c.refined_source_request_manifest()["count"] == 25


def test_accepted_locators_are_object_level_and_visually_verified():
    accepted = c.accepted_locator_manifest()
    assert accepted["accepted_locator_count"] == 8
    required = set(c.accepted_locator_schema()["required"])
    for row in accepted["rows"]:
        assert required <= set(row)
        assert row["pdf_page_index_1based"] == row["pdf_page_index_0based"] + 1
        assert row["equation_table_appendix_label"]
        assert row["normalized_bounding_box"] is not None
        assert row["visual_verification"] == "VISUALLY_VERIFIED_LOCAL_RENDER"
        assert row["object_crop_hash"]
        assert row["dependency_locator_ids"]
        assert c.visual_locator_report(row["locator_id"])["locator_id"] == row["locator_id"]


def test_mass_coupling_gate_and_execution_boundaries_remain_closed():
    gate = c.mass_coupling_locator_gate_report()
    assert gate["gate_closed"] is True
    assert gate["formula_transcription_authorized"] is False
    assert gate["target_execution_authorized"] is False
    cert = c.lfglocator2_completeness_certificate()
    assert cert["complete_expressions"] == 0
    assert cert["target_programs"] == 0
    assert cert["target_values"] == 0
    assert c.expression_handoff_contract()["eligible"] is False
    assert c.static_isolation_guard()["pass"] is True


def test_restart_sharding_query_order_and_safe_mutation_boundary():
    first = c.descriptor_search_query_manifest()["root"]
    second = c.descriptor_search_query_manifest()["root"]
    assert first == second
    assert c.candidate_locator_manifest()["root"] == c.candidate_locator_manifest()["root"]
    assert c.static_isolation_guard()["allow_pickle_false"] is True
    for index in range(384):
        result = c.mutate_live_hqcdlfglocator2(index)
        assert result["positive_gate"] is False
        assert result["must_fail_or_change_root"] is True
