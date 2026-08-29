"""C167 source-acquisition and adapter-boundary tests."""
from pathlib import Path

import pytest

from deuteron_wigner.bridge import hqcdlfgacquire4 as c
from deuteron_wigner.bridge import hqcdlfgdep2 as c166


def test_boundary_and_runtime_are_frozen():
    authority = c.load_verified_hqcd_lfgacquire4_authority()
    assert authority["baseline"] == c.BASELINE
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGACQUIRE4-D"
    assert authority["C166_package_root"] == "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416"
    assert c.PACKAGE_ROOT == "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d"
    assert c166.PACKAGE_ROOT == authority["C166_package_root"]


def test_all_eight_requests_and_six_locator_leaves_are_exactly_imported():
    expected = tuple(row["request_id"] for row in c166.missing_dependency_acquisition_manifest()["rows"])
    assert tuple(row["request_id"] for row in c.REQUESTS) == expected
    assert len(c.acquisition_request_freeze()["rows"]) == 8
    assert len(c.preserved_locator_leaf_manifest()["rows"]) == 6
    assert c.preserved_locator_leaf_manifest()["source_statuses_unchanged"] is True
    assert c.dependency_frontier_manifest()["count"] == 14


def test_acquisition_is_official_and_archive_is_safe():
    row = c.source_acquisition_manifest()["rows"][0]
    assert row["official_source_identity"] == "arXiv:0901.2599v2"
    assert row["official_url"].startswith("https://arxiv.org/")
    assert row["sha256"] == "5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3"
    archive = Path(row["local_path"])
    assert archive.exists()
    assert c.archive_member_manifest()["count"] == 11
    assert c.archive_member_manifest()["unsafe_members_rejected"] == 0
    assert c.archive_member_manifest()["archive_hash_verified_before_extraction"] is True
    assert all(not m["absolute_path"] and not m["traversal"] and not m["symlink_or_hardlink"]
               for m in c.archive_member_manifest()["rows"])


def test_object_presence_and_rismom_scope_are_separate():
    presence = c.object_presence_manifest()["rows"]
    assert len(presence) == 8
    assert sum(row["presence_status"] == "EXACT_REQUESTED_OBJECT_PRESENT" for row in presence) == 2
    assert sum(row["presence_status"] == "OBJECT_REQUIRES_PROJECT_DERIVATION" for row in presence) == 6
    scope = c.rismom_nf_flavor_manifest()
    assert len(scope["rows"]) == 2
    assert scope["active_Nf_external_flavor_conflated"] == 0
    assert scope["inferred_from_numerical_examples"] == 0
    assert all(row["terminal_status"] == "RI_SMOM_NF_FLAVOR_SOURCE_AUTHORITY_READY" for row in scope["rows"])


def test_c43_endpoint_and_adapter_layers_remain_distinct():
    rows = c.c43_adapter_acquirability_manifest()["rows"]
    assert len(rows) == 6
    assert all(row["layer_C_explicit_adapter"] == "absent from authenticated sources" for row in rows)
    assert all(row["endpoint_definitions_promoted_to_adapter"] is False for row in rows)
    assert all(row["terminal_status"] == "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED" for row in rows)
    assert c.c43_adapter_calculation_request_manifest()["new_calculation_selected"] is False


def test_terminal_resolution_and_no_graph_integration():
    rows = c.request_resolution_manifest()["rows"]
    assert len(rows) == 8
    assert sum(row["terminal_status"] == "RESOLVED_BY_OFFICIAL_TEX_OR_ANCILLARY" for row in rows) == 2
    assert sum(row["terminal_status"] == "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED" for row in rows) == 6
    frontier = c.dependency_frontier_manifest()
    assert frontier["graph_nodes_added"] == 0
    assert frontier["graph_edges_added"] == 0
    assert frontier["C166_graphs_rewritten"] is False


def test_fail_closed_immutability_and_isolation():
    assert c.static_isolation_guard()["pass"] is True
    assert c.static_isolation_guard()["allow_pickle_false"] is True
    assert c.no_execution_report()["target_values"] == 0
    assert c.no_derivation_report()["C43_adapter_derived"] == 0
    with pytest.raises(KeyError):
        c.object_presence_manifest("unknown")
    with pytest.raises(KeyError):
        c.source_acquisition_manifest("unknown")


def test_restart_order_and_live_mutation_holdout():
    assert c.request_resolution_manifest()["root"] == c.request_resolution_manifest()["root"]
    assert c.archive_member_manifest()["root"] == c.archive_member_manifest()["root"]
    assert c.dependency_frontier_manifest()["root"] == c.dependency_frontier_manifest()["root"]
    for index in range(384):
        mutation = c.mutate_live_hqcdlfgacquire4(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
