"""C175 local finite-cell P0 ghost-sector authority tests."""

import numpy as np

from deuteron_wigner.bridge import hqcdb0ghostsector1 as c
from deuteron_wigner.bridge import hqcdb0resgauge2 as c174


def test_baseline_provenance_and_roots():
    a = c.verify_hqcd_b0ghostsector1_authority()
    assert a["baseline"] == "66081dc2d58954d0e8a03f7caccaa495f03acd70"
    assert a["expected_contract_present"] is False
    assert a["C174_package_root"] == c174.PACKAGE_ROOT
    assert a["C174_to_C175_contract_invented"] is False
    assert c.ghost_handoff_freeze()["records_rebuilt"] == 0


def test_domain_census_and_reversible_order():
    expected = {"K9": 288, "K11": 440, "K13": 624}
    for resolution, dimension in expected.items():
        for role in c.ROLES:
            manifest = c.ghost_domain_manifest(resolution, role)
            assert manifest["dimensions"][resolution] == dimension
            assert len(manifest["rows"]) == dimension
            for rank in (0, dimension // 2, dimension - 1):
                row = c.unrank_ghost_mode(resolution, role, rank)
                assert c.rank_ghost_mode(row) == rank
                assert row["global_su3_direction"] is False
                assert row["physical_polarization"] is False


def test_berezin_boundary_and_roles():
    b = c.berezin_manifest()
    assert b["pair_order"] == "antighost before ghost"
    assert b["ghost_number"] == {"ghost": 1, "antighost": -1}
    assert b["identities"]["one_pair_gaussian"] is True
    assert c.ghost_role_separation_manifest()["not_Hilbert_adjoint"] is True
    assert c.ghost_boundary_link_manifest()["link_unity"] is False


def test_free_sparse_and_matrix_free_routes():
    for resolution in c.RESOLUTIONS:
        dimension = c.ghost_domain_manifest(resolution, "ghost")["dimensions"][resolution]
        vector = np.arange(dimension, dtype=float).astype(complex)
        action = c.apply_free_ghost_operator(resolution, vector)
        assert action["residual"] == 0.0
        assert c.free_ghost_manifest(resolution)["rows"][0]["dense_inverse_constructed"] is False
        query = {"source_vector_id": "test-source", "operator_root": c.free_ghost_manifest(resolution)["rows"][0]["root"], "global_kernel_exclusion": True, "boundary_treatment": "bulk-only; leakage separate", "tolerance": 1e-10}
        solved = c.solve_free_ghost(resolution, vector, query)
        assert solved["residual"] < 1e-8


def test_interaction_color_routes_and_no_target_import():
    interaction = c.ghost_gluon_interaction_manifest()
    assert all(row["coupling_degree"] == 1 for row in interaction["rows"])
    assert all(len(row["routes"]) == 5 for row in interaction["rows"])
    color = c.ghost_color_manifest()
    assert color["all_eight_generators"] is True
    assert color["global_su3_local_determinant"] is False
    assert c.target_ghost_separation_manifest()["target_ghost_imported"] is False


def test_support_is_exact_and_boundary_is_not_zero():
    support = c.longitudinal_support_manifest()
    rows = {row["external_sector_id"]: row for row in support["rows"]}
    assert rows["C151-ONE-GLUON"]["classification"] == "RETAINED_Q0_B0_SOURCE_ORTHOGONAL_WITH_EXACT_LONGITUDINAL_PROOF"
    assert rows["C151-ONE-GLUON"]["boundary_exception"] == "COUPLES_ONLY_THROUGH_BOUNDARY_OR_RESIDUAL_LINK"
    assert c.ghost_boundary_link_manifest("C174-RESIDUAL-LINK-OPERATOR")["rows"][0]["status"] == "REQUIRES_EXPLICIT_BOUNDARY_OPERATOR"


def test_determinant_loop_count_once_and_release():
    assert c.determinant_manifest()["rows"][0]["closed_loop_sign"] == -1
    assert c.ghost_loop_manifest()["rows"][0]["complete_self_energy"] is False
    count = c.ghost_count_once_manifest()
    assert count["duplicate_owners"] == 0
    assert count["missing_as_zero"] == 0
    assert c.b0_release_manifest()["decision"] == "B0_RELEASED_RETAINED_Q0_GHOST_ORTHOGONAL_P0_INTERFACE_SEPARATE"


def test_requests_frontier_and_nonclaims():
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert sum(row["C175_terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in requests["rows"]) == 2
    assert c.missing_ghost_object_manifest()["rows"][0]["not_zero"] is True
    assert c.dependency_frontier_manifest()["C166_graph_nodes_added"] == 0
    assert c.brst_st_boundary_manifest()["BRST"] == "BRST_NOT_CONSTRUCTED"


def test_safe_loader_and_mutation_holdout():
    assert c.load_verified_hqcd_b0ghostsector1_authority()["C175_package_root"] == c.PACKAGE_ROOT
    for index in range(384):
        mutation = c.mutate_live_hqcdb0ghostsector1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
