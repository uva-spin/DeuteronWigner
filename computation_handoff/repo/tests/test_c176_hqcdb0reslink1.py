"""C176 residual-link fail-closed and finite-HO boundary tests."""

import numpy as np

from deuteron_wigner.bridge import hqcdb0reslink1 as c
from deuteron_wigner.bridge import hqcdb0resgauge2 as c174
from deuteron_wigner.bridge import hqcdb0ghostsector1 as c175


def test_contract_baseline_and_c175_boundary():
    a = c.verify_hqcd_b0reslink1_authority()
    assert a["baseline"] == "854098ef8fbeeff7a4f47c7c2268f371a9b5c8a0"
    assert a["contract_sha256"] == "34457964822712019148ba83e7d73426a6042cc756cf55678117516713b4753c"
    assert a["C175_package_root"] == c175.PACKAGE_ROOT
    assert c.residual_link_handoff_freeze()["records_rebuilt"] == 0


def test_c43_path_fails_closed_without_inference():
    path = c.path_geometry_manifest()["rows"][0]
    assert path["status"] == "PATH_GEOMETRY_INCOMPLETE"
    assert path["path_inferred"] is False
    assert path["basepoint"] is None
    assert path["endpoint"] is None
    assert c.path_trace_manifest()["status"] == "PATH_GEOMETRY_INCOMPLETE"
    assert c.wilson_link_manifest()["rows"][0]["status"] == "ADJOINT_LINK_EXPANSION_INCOMPLETE"


def test_boundary_evaluation_keeps_p0_q0_separate():
    rows = c.boundary_evaluation_manifest()["rows"]
    assert {row["P0_dimension"] for row in rows} == {72, 110, 156}
    assert all(row["P0_Q0_separate"] for row in rows)
    assert all(row["endpoint_value"] == "UNAVAILABLE_NOT_ZERO" for row in rows)
    assert all(row["route_status"] == "BLOCKED_BY_PATH_GEOMETRY" for row in rows)


def test_ho_boundary_factorized_and_unpruned():
    for resolution in c.RESOLUTIONS:
        row = c.ho_boundary_manifest(resolution)["rows"][0]
        assert row["leakage_threshold_pruned"] is False
        assert row["leakage_nonzero_entries"] > 0
        assert row["leakage_norm"] > 0
        d = row["retained_dimension"]
        vector = np.arange(d, dtype=float).astype(complex)
        action = c.apply_ho_boundary_operator(resolution, vector, "gradient")
        assert action["omitted_space_materialized"] is False
        back = c.apply_ho_boundary_operator(resolution, np.zeros(row["factorized_omitted_dimension"], dtype=complex), "divergence")
        assert len(action["action"]) == row["factorized_omitted_dimension"]
        assert len(back["action"]) == d
        assert c.integration_by_parts_defect_manifest(resolution)["rows"][0]["defect_nonzero"] is True


def test_link_ho_relation_and_color_boundary():
    assert c.boundary_relation_manifest()["relation"] == "NONCOMPOSABLE_NONMATRIX_INTERFACE"
    color = c.link_color_manifest()
    assert color["all_eight_generators"] is True
    assert color["open_adjoint"] is True
    assert color["singlet_projection"] is False
    assert c.open_color_manifest()["gg_multiplicities"] == ("d", "f")


def test_ghost_link_support_kernels_fail_closed():
    assert c.ghost_link_manifest()["rows"][0]["status"] == "GHOST_LINK_INCOMPLETE"
    assert c.endpoint_support_manifest("C151-ONE-GLUON")["rows"][0]["classification"] == "SUPPORT_INCOMPLETE"
    assert c.link_kernel_manifest()["rows"][0]["complete_self_energy"] is False
    assert c.target_link_separation_manifest()["physical_TMD_staple"] == "PHYSICAL_TMD_LINK_NOT_CONSTRUCTED"


def test_release_requests_frontier_and_isolation():
    assert c.b0_release_manifest()["decision"] == "B0_NOT_RELEASED_PATH_GEOMETRY_INCOMPLETE"
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert sum(row["C176_terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in requests["rows"]) == 2
    assert c.missing_boundary_object_manifest()["rows"][0]["not_zero"] is True
    assert c.dependency_frontier_manifest()["C166_graph_nodes_added"] == 0
    assert c.static_isolation_guard()["pass"] is True


def test_loader_and_mutations():
    assert c.load_verified_hqcd_b0reslink1_authority()["package_root"] == c.PACKAGE_ROOT
    for index in range(384):
        mutation = c.mutate_live_hqcdb0reslink1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
