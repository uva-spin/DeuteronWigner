"""C165 dependency-locator closure and fail-closed boundary tests."""
from collections import Counter

from deuteron_wigner.bridge import hqcdlfgdep as c
from deuteron_wigner.bridge import hqcdlfglocator2 as c164


def test_authority_and_immutable_c164_root_import():
    authority = c.load_verified_hqcd_lfgdep_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGDEP-D"
    assert authority["package_root"] == c.PACKAGE_ROOT
    assert authority["C164_package_root"] == "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2"
    assert c.accepted_root_object_manifest()["rows"] == c164.accepted_locator_manifest()["rows"]
    assert c.accepted_root_object_manifest()["count"] == 8


def test_inventory_candidates_and_accepted_dependencies_are_object_level():
    inventory = c.source_symbol_inventory()
    candidates = c.candidate_dependency_manifest()
    accepted = c.accepted_dependency_manifest()
    assert inventory["symbol_count"] == 55
    assert candidates["candidate_count"] == 114
    assert candidates["all_candidates_recorded_before_selection"] is True
    assert accepted["accepted_dependency_count"] == 55
    for row in accepted["rows"]:
        assert row["equation_table_appendix_label"]
        assert row["normalized_bounding_box"]
        assert row["page_text_hash"] and row["page_render_hash"] and row["object_crop_hash"]
        assert row["visual_verification"] == "VISUALLY_VERIFIED_LOCAL_RENDER"
        assert row["text_layer_agreement"] == "AGREES_WITH_RENDERED_OBJECT"
        assert c.visual_dependency_report(row["dependency_locator_id"])["dependency_locator_id"] == row["dependency_locator_id"]


def test_graphs_are_acyclic_but_fail_closed_at_exact_leaves():
    closure = c.dependency_closure_manifest()
    assert closure["graph_count"] == 8
    assert closure["closed_graph_count"] == 0
    assert closure["incomplete_graph_count"] == 8
    for root in c.accepted_root_object_manifest()["rows"]:
        graph = c.dependency_graph(root["locator_id"])
        assert graph["cycle_status"] == "ACYCLIC"
        assert graph["cycle_count"] == 0
        assert graph["source_version_consistent"] is True
        assert graph["unresolved_leaves"]
        assert graph["closure_status"] == "DEPENDENCY_LOCATOR_INCOMPLETE"
        assert graph["topological_order"][0] == root["locator_id"]
    assert c.missing_dependency_request_manifest()["count"] == 32


def test_all_25_descriptor_statuses_and_quantity_separation_remain_visible():
    crosswalk = c.descriptor_dependency_crosswalk()
    assert crosswalk["descriptor_count"] == 25
    assert crosswalk["C164_absent_final_object_count"] == 13
    assert crosswalk["C164_role_mismatch_count"] == 4
    assert Counter(row["C165_terminal_status"] for row in crosswalk["rows"]) == {
        "DEPENDENCY_LOCATOR_INCOMPLETE": 8,
        "FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES": 13,
        "SOURCE_ROLE_MISMATCH": 4,
    }
    for quantity in ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING"):
        assert c.componentwise_dependency_manifest(quantity)["quantity_id"] == quantity


def test_gate_and_nonexecution_boundary():
    gate = c.mass_coupling_dependency_gate_report()
    assert gate["gate_closed"] is True
    assert gate["expression_transcription_authorized"] is False
    assert gate["target_execution_authorized"] is False
    assert c.expression_transcription_handoff_contract()["eligible"] is False
    assert c.quantum_dependency_handoff()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"] is True
    assert c.static_isolation_guard()["allow_pickle_false"] is True


def test_restart_query_order_and_384_live_mutations():
    assert c.source_symbol_inventory()["root"] == c.source_symbol_inventory()["root"]
    assert c.candidate_dependency_manifest()["root"] == c.candidate_dependency_manifest()["root"]
    assert c.descriptor_dependency_crosswalk()["root"] == c.descriptor_dependency_crosswalk()["root"]
    for index in range(384):
        result = c.mutate_live_hqcdlfgdep(index)
        assert result["positive_gate"] is False
        assert result["must_fail_or_change_root"] is True
