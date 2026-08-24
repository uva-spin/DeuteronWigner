"""Focused C186 qgg cubic-transition and order-two frontier tests."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from deuteron_wigner.bridge import hqcdb1qgg2 as c


def test_authority_and_frozen_c185_boundary():
    authority = c.verify_hqcd_b1qgg2_authority()
    assert authority["C185_package_root"] == "c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885"
    assert c.b1qgg2_plan_manifest()["selected_plan"] == "B1QGG2-B"
    assert c.qgg_handoff_freeze()["C185_package_root"] == authority["C185_package_root"]
    assert c.qgg_handoff_freeze()["C185_cubic_terminal_root"]


def test_cubic_owner_lift_color_and_bose():
    assert c.cubic_owner_manifest()["count"] == 3
    assert c.spectator_lift_manifest()["count"] == 9
    color = c.cubic_color_manifest()
    assert {row["channel_id"] for row in color["rows"]} == {"QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A"}
    assert [row["status"] for row in color["rows"]] == ["EXACT_ZERO_WITH_ALGEBRAIC_PROJECTION", "EXACT_ZERO_WITH_ALGEBRAIC_PROJECTION", "SOURCE_DERIVED_NONZERO_SYMBOLIC"]
    bose = c.cubic_bose_manifest()
    assert bose["count"] == 9
    assert bose["exchange_forbidden_retained"] == 0
    assert all(row["total_exchange_parity"] == 1 for row in bose["rows"] if row["channel_id"] == "QGG_COLOR_8A")


def test_kinematics_action_and_hermitian_routes():
    kin = c.cubic_kinematics_manifest()
    assert len(kin["rows"]) == 9
    assert all(row["ordinary_zero_mode"] is False and row["CM_excited_silently_included"] is False for row in kin["rows"])
    act = c.cubic_action_manifest()
    assert len(act["rows"]) == 9
    assert all(row["sparse"] and row["matrix_free"] and not row["dense_rectangular_default"] for row in act["rows"])
    result = c.apply_cubic_transition({"coordinate": "g_s", "symbolic": True}, (1 + 2j,), channel_id="QGG_COLOR_8A")
    assert result["route_residual"] == 0.0
    assert c.order2_action_manifest()["count"] == 18


def test_order2_typed_frontier_topology_holonomy_and_requests():
    owners = c.order2_owner_manifest()
    assert owners["count"] == 6
    assert all(row["terminal"] != "EXACT_ZERO" for row in owners["rows"])
    colors = c.order2_color_manifest()
    assert len(colors["rows"]) == 18
    assert all(row["status"] == "ORDER2_OWNER_PARTIAL_NOT_ZERO" for row in colors["rows"])
    topology = c.topology_manifest()
    assert topology["complete_qg_1PI_value"] is False
    assert topology["direct_sequential_conflation"] is False
    assert c.holonomy_bc_manifest()["count"] == 5
    assert c.request_resolution_manifest()["all_six_visible"] is True
    assert c.qgg_release_manifest()["decision"] == "QGG_CUBIC_TRANSITION_READY_ORDER2_OWNER_PARTIAL"


def test_isolation_reload_and_mutations():
    assert c.static_isolation_guard()["pass"] is True
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert all(c.mutate_live_hqcd_b1qgg2(i)["pass"] for i in range(384))
