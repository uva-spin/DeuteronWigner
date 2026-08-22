"""Focused C168 adapter-boundary tests."""
from types import MappingProxyType

import pytest

from deuteron_wigner.bridge.hqcdlfgadapter1 import core as c


def test_authority_and_six_terminal_records():
    assert c.verify_hqcd_lfgadapter1_authority()["status"] == c.STATUS
    assert len(c.adapter_request_freeze()["rows"]) == 6
    rows = c.request_resolution_manifest()["rows"]
    assert len(rows) == 6
    assert {x["terminal_status"] for x in rows} == {"NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED"}
    assert all(x["symbolic_program_id"] is None for x in rows)


def test_endpoint_and_contribution_gates():
    endpoints = c.endpoint_identity_manifest()["rows"]
    assert len(endpoints) == 6
    assert all(x["C43"]["pole"] == "antisymmetric/PV inverse partial-plus" for x in endpoints)
    assert all(x["target"]["active_Nf"] == "explicit symbolic active-loop N_f; no numerical value inferred" for x in endpoints)
    assert c.adapter_contribution_ledger()["missing_as_zero"] == 0
    assert c.c43_structure_ledger()["missing_structures_zeroed"] == 0


def test_frontier_and_no_execution():
    frontier = c.dependency_frontier_manifest()
    assert frontier["count"] == 14
    assert frontier["graph_nodes_added"] == 0
    assert frontier["graph_edges_added"] == 0
    assert c.adapter_program_manifest()["program_count"] == 0
    assert c.adapter_diagnostic_manifest()["evaluations"] == 0
    assert c.static_isolation_guard()["pass"] is True


def test_safe_loading_and_fail_closed_queries():
    loaded = c.load_verified_hqcd_lfgadapter1_authority()
    assert loaded["package_root"] == c.PACKAGE_ROOT
    with pytest.raises(KeyError):
        c.endpoint_identity_manifest("unknown-request")
    with pytest.raises(KeyError):
        c.componentwise_adapter_manifest(quantity_id="UNKNOWN")
    with pytest.raises(TypeError):
        c.adapter_request_freeze()["rows"] = ()


def test_mutations_are_guarded():
    for i in range(384):
        result = c.mutate_live_hqcdlfgadapter1(i)
        assert result["positive_gate"] is False
        assert result["must_fail_or_change_root"] is True

