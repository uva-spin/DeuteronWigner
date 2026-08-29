"""C166 leaf-resolution, graph-delta, and fail-closed boundary tests."""
from collections import Counter

import pytest

from deuteron_wigner.bridge import hqcdlfgdep as c165
from deuteron_wigner.bridge import hqcdlfgdep2 as c


def test_authority_and_imported_c165_records_are_unchanged():
    authority = c.load_verified_hqcd_lfgdep2_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGDEP2-C"
    assert authority["C165_package_root"] == "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2"
    assert c.imported_authority_freeze()["accepted_C164_root_count"] == 8
    assert c.imported_authority_freeze()["accepted_C165_dependency_count"] == 55
    assert c.imported_authority_freeze()["C165_graph_count"] == 8
    assert c.imported_authority_freeze()["C165_leaf_count"] == 32
    assert tuple(c.IMPORTED_ROOTS) == tuple(c165.accepted_root_object_manifest()["rows"])
    assert tuple(c.IMPORTED_DEPS) == tuple(c165.accepted_dependency_manifest()["rows"])
    assert tuple(c.IMPORTED_GRAPHS) == tuple(c165.dependency_graph(row["locator_id"]) for row in c165.accepted_root_object_manifest()["rows"])


def test_leaf_inventory_reuse_candidates_and_terminal_records():
    assert c.missing_leaf_inventory()["count"] == 32
    assert c.leaf_candidate_manifest()["all_candidates_recorded_before_selection"] is True
    assert c.leaf_candidate_manifest()["candidate_count"] == 178
    rows = c.leaf_resolution_manifest()["rows"]
    assert len(rows) == 32
    assert Counter(row["terminal_status"] for row in rows) == {
        "RESOLVED_BY_ACCEPTED_DEPENDENCY_REUSE": 17,
        "RESOLVED_BY_EXACT_SOURCE_ALIAS": 1,
        "DEPENDENCY_OBJECT_ABSENT_FROM_LOCAL_PDFS": 8,
        "DEPENDENCY_LOCATOR_INCOMPLETE": 6,
    }
    assert c.missing_dependency_acquisition_manifest()["count"] == 8
    assert c.dependency_reuse_manifest()["unproved_reuse_count"] == 0


def test_graph_deltas_preserve_acyclic_imports_and_count_once():
    deltas = c.graph_delta_manifest()["rows"]
    assert len(deltas) == 8
    assert all(row["all_C165_nodes_edges_preserved"] for row in deltas)
    assert all(row["cycle_result"] == "ACYCLIC" for row in deltas)
    assert all(row["source_version_result"] == "CONSISTENT" for row in deltas)
    assert c.count_once_validation()["duplicate_semantic_nodes"] == 0
    assert c.dependency_closure_manifest()["closed_graph_count"] == 0
    assert c.dependency_closure_manifest()["graph_count"] == 8
    assert all(c.dependency_graph(row["graph_id"])["cycle_count"] == 0 for row in deltas)


def test_descriptor_and_quantity_boundaries_remain_separate():
    crosswalk = c.descriptor_dependency_crosswalk()
    assert crosswalk["descriptor_count"] == 25
    assert crosswalk["preserved_absent_count"] == 13
    assert crosswalk["preserved_role_mismatch_count"] == 4
    for quantity in ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING"):
        assert c.componentwise_dependency_manifest(quantity)["quantity_id"] == quantity
    gate = c.mass_coupling_dependency_gate_report()
    assert gate["gate_closed"] is False
    assert gate["expression_transcription_authorized"] is False
    assert gate["target_execution_authorized"] is False
    assert gate["signed_mass_separate_from_mass_squared"] is True


def test_visual_safe_loading_and_no_execution_boundary():
    visual = c.visual_leaf_manifest()
    assert visual["newly_accepted_count"] == 0
    assert visual["reused_visual_count"] == 55
    assert visual["text_layer_only_accepted"] == 0
    assert c.static_isolation_guard()["pass"] is True
    assert c.static_isolation_guard()["allow_pickle_false"] is True
    assert c.no_expression_transcription_report()["complete_expression_transcriptions"] == 0
    assert c.expression_or_acquisition_handoff_contract()["eligible_for_expression_transcription"] is False


def test_restart_query_order_and_live_mutations():
    assert c.missing_leaf_inventory()["root"] == c.missing_leaf_inventory()["root"]
    assert c.leaf_candidate_manifest()["root"] == c.leaf_candidate_manifest()["root"]
    assert c.graph_delta_manifest()["root"] == c.graph_delta_manifest()["root"]
    for index in range(384):
        mutation = c.mutate_live_hqcdlfgdep2(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True


def test_unknown_ids_fail_closed():
    with pytest.raises(KeyError):
        c.missing_leaf_inventory(graph_id="unknown")
    with pytest.raises(KeyError):
        c.leaf_candidate_manifest(leaf_id="unknown")
    with pytest.raises(KeyError):
        c.visual_leaf_report("unknown")
