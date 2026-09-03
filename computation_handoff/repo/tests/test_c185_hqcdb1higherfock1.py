"""Focused C185 B=1 higher-Fock API tests."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from deuteron_wigner.bridge import hqcdb1higherfock1 as c


def test_authority_contract_and_scope():
    authority = c.verify_hqcd_b1higherfock1_authority()
    assert authority["C184_package_root"] == "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8"
    assert c.b1higherfock1_plan_manifest()["selected_plan"] == "B1HIGHERFOCK1-B"
    assert c.SECTORS == ("C170-B1-QGG", "C170-B1-QQBARQ")
    assert c.sector_graph_manifest()["nodes"][-2]["sector_id"] == "C170-B1-QGG"
    assert c.request_resolution_manifest()["all_six_visible"] is True


def test_longitudinal_color_statistics_and_flavor():
    long = c.longitudinal_manifest()
    assert long["count"] == 18
    k9 = [r for r in long["rows"] if r["resolution"] == "K9" and r["sector_id"] == "C170-B1-QGG"][0]
    assert (k9["qgg_ordered"], k9["qgg_bose_orbits"]) == (6, 4)
    assert all(not row["ordinary_zero_mode"] for row in long["rows"])
    assert c.qgg_color_manifest()["derived_multiplicity"] == 3
    assert {row["channel_id"] for row in c.qgg_color_manifest()["rows"]} == {"QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A"}
    assert c.qqbarq_color_manifest()["derived_multiplicity"] == 2
    assert c.qqbarq_color_manifest()["recoupling_unitarity_residual"] == 0.0
    assert c.qqbarq_flavor_statistics_manifest()["hidden_Nf"] is False
    assert all(row["Pauli_forbidden_states_retained"] == 0 for row in c.qqbarq_flavor_statistics_manifest()["rows"])


def test_basis_free_operator_and_resolvent_routes():
    basis = c.basis_manifest()
    assert basis["count"] == 9
    assert basis["augmented_order"] == ("q", "qg", "qgg", "qqbarq")
    for sector in c.SECTORS:
        state = c.unrank_sector_state(sector, "K9", 0)
        assert c.rank_sector_state(sector, "K9", state["canonical_rank"]) == 0
        assert c.free_operator_manifest(sector, "K9")["rows"][0]["dense_full_matrix"] is False
        action = c.apply_free_operator(sector, "K9", (1 + 2j, 2 - 1j))
        assert action["route_residual"] == 0.0
        resolvent = c.apply_resolvent(sector, "K9", (1 + 2j,), {"real": 0.5, "imaginary": 0.25})
        assert resolvent["dense_full_inverse"] is False


def test_transitions_and_order_two_ledgers():
    assert c.qg_qgg_quark_manifest()["count"] == 3
    cubic = c.qg_qgg_gluon_manifest()
    assert cubic["rows"][0]["status"] == "PARTIAL_QGG_FRONTIER"
    assert set(cubic["rows"][0]["supported_channels"]) == {"QGG_COLOR_8A"}
    pair = c.qg_qqbarq_manifest()
    assert pair["count"] == 3
    assert all(row["same_flavor_exchange"] for row in pair["rows"])
    assert c.order2_manifest()["count"] == 6
    assert all(row["direct_not_sequential"] for row in c.order2_manifest()["rows"])
    assert all(not row["unavailable_is_zero"] for row in c.count_once_manifest()["rows"])


def test_holonomy_release_and_mutations():
    bc = c.holonomy_bc_manifest()
    assert bc["count"] == 10
    assert all(not row["mode_grid_changed"] for row in bc["rows"])
    assert c.b1_release_manifest()["decision"] == "B1_HIGHER_FOCK_BASES_READY_TRANSITIONS_PARTIAL"
    assert c.static_isolation_guard()["pass"] is True
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert all(c.mutate_live_hqcdb1higherfock1(i)["pass"] for i in range(384))
