"""Focused C184 public-API tests."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c


def _record(request=c.ACTIVE_REQUESTS[0], fixture="C184_FIXTURE_CARTAN_INTERIOR", resolution="K9"):
    return c.calculation_parameter_fixture(fixture, request, resolution)


def test_authority_contract_and_request_census():
    authority = c.load_verified_hqcd_lfmatchcalc2_authority()
    assert authority["status"] == c.STATUS
    assert c.verify_hqcd_lfmatchcalc2_authority()["contract_sha256"] == c.CONTRACT_SHA256
    resolution = c.request_resolution_manifest()
    assert resolution["all_six_visible"] is True
    assert resolution["active_count"] == 2
    assert c.lfmatchcalc2_plan_manifest()["selected_plan"] == "LFGMATCHCALC2-B"


def test_strict_parameter_and_holonomy_validation():
    record = _record()
    assert c.validate_calculation_parameter_record(record)["valid"] is True
    assert record["bare_mass"]["coordinate"] == "signed m_R"
    assert record["bare_mass_squared"]["coordinate"] == "m_R^2"
    assert record["counterterm_coordinate"]["selected"] is False
    assert record["null_coordinate"]["selected"] is False
    bad = dict(record)
    bad.pop("resolvent_coordinate")
    try:
        c.validate_calculation_parameter_record(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("partial parameter record accepted")


def test_vertices_and_factorized_loops():
    record = _record()
    source = tuple(complex(i + 1) for i in range(16))
    qq = c.g_qqbar_vertex_manifest("K9", holonomy_capsule_id="GENERIC_CARTAN_INTERIOR")
    assert qq["count"] == 1
    qaction = c.apply_g_qqbar_vertex(record, source, "g_to_qqbar")
    assert qaction["route_residual"] == 0.0
    gg = c.g_gg_vertex_manifest("K9")
    assert {row["channel_id"] for row in gg["rows"]} == {"GG_D", "GG_F"}
    assert all(row["outer_adjoint_multiplicity"] == 2 for row in gg["rows"])
    for channel in ("GG_D", "GG_F"):
        assert c.apply_g_gg_vertex(record, source, channel, "g_to_gg")["route_residual"] == 0.0
    loops = c.propagating_loop_manifest(request_id=record["active_request_id"], resolution_id="K9", fixture_id=record["fixture_id"])
    assert {row["sector_id"] for row in loops["rows"]} == set(c.SECTORS)
    assert all(row["dense_full_inverse"] is False for row in loops["rows"])
    for sector in c.SECTORS:
        assert c.apply_propagating_loop(record, source, sector)["route_residual"] == 0.0


def test_boundary_nonpropagating_aggregation_projection_and_coupling():
    record = _record(request=c.ACTIVE_REQUESTS[1], fixture="C184_FIXTURE_CENTER_SECTOR", resolution="K11")
    source = tuple(complex(i) for i in range(16))
    links = c.ghost_link_holonomy_manifest(request_id=record["active_request_id"], resolution_id="K11", holonomy_capsule_id=record["holonomy_capsule_id"])
    assert links["bulk_endpoint_conflated"] is False
    assert links["holonomy_additive_loop"] is False
    nonprop = c.nonpropagating_manifest(request_id=record["active_request_id"], resolution_id="K11")
    assert nonprop["count"] >= 10
    assert all(row["not_zero"] for row in nonprop["rows"])
    agg = c.apply_proper_two_point(record, source)
    assert agg["route_residual"] == 0.0
    assert c.tensor_projection_manifest(record["active_request_id"], "K11")["count"] == 1
    field = c.field_response_manifest(record["active_request_id"], "K11", record["fixture_id"])
    assert field["rows"][0]["physical_Z_A"] is False
    coupling = c.coupling_component_manifest(record["active_request_id"], "K11", record["fixture_id"])
    assert coupling["rows"][0]["full_coupling"] is False
    assert c.count_once_manifest(record["active_request_id"])["duplicates"] == 0


def test_readiness_isolation_and_mutation_coverage():
    assert c.b0_release_manifest()["decision"] == "B0_C43_TRANSVERSE_GLUON_PROPER_TWO_POINT_READY_COUPLING_COMPONENT_PARTIAL"
    assert c.static_isolation_guard()["pass"] is True
    assert c.quantum_nonmutation_manifest()["new_qubits"] == 0
    assert c.dependency_frontier_manifest()["graph_delta"]["nodes_added"] == 0
    assert all(c.mutate_live_hqcdlfmatchcalc2(i)["pass"] for i in range(384))
