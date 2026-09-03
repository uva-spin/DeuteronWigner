from deuteron_wigner.bridge import hqcdghostvert1 as c200
import pytest


def _p(resolution="K9"):
    return {"parameter_id": f"test-{resolution}", "resolution": resolution,
            "external_record_id": f"C200-EXT-{resolution}-antighost-in-gluon-ghost",
            "tree_owner_id": "C175-P0-FP-COMMUTATOR-D_A",
            "complete_FP_owner_ids": ("C175-P0-FP-COMMUTATOR",),
            "gluon_field_record_id": f"C184-GLUON-EXTERNAL-{resolution}",
            "projector_id": "C200-PROJ-F", "subtraction_coordinate": f"NONZERO-{resolution}",
            "fixture_id": f"C200-GHOSTVERT-FIXTURE-{resolution}",
            "holonomy_capsule_id": "C183-CALLER-NONPHYSICAL", "cut_side": "C178 declared cut-side frame",
            "coupling_coordinate": "caller-supplied-symbolic-g_s", "counterterm_coordinates": c200.COUNTERTERMS,
            "null_coordinates": c200.NULLS, "branch_id": "caller-continuous-nonzero", "enclosure": "EXACT_SYMBOLIC_OUTWARD",
            "units": "source-defined", "no_defaults": True, "physical": False}


def test_authority_role_frontier_and_runtime():
    assert c200.verify_hqcd_ghostvert1_authority()["C199_package_root"] == c200.C199_ROOT
    assert c200.vertex_role_decision()["exact_object"] == "complete ghost-gluon proper vertex"
    assert c200.vertex_role_decision()["aliases"] == ("complete ghost-gluon proper vertex", "GHOST_GLUON_PROPER_VERTEX")
    assert c200.frontier_manifest()["first"] == "C197-ST-2"
    assert c200.next_st_handoff_contract()["next_object"] == "C197-ST-3"
    assert c200.load_verified_hqcdghostvert1_authority()["status"] == c200.STATUS


def test_domains_parameters_and_default_rejection():
    assert c200.external_domain_manifest()["count"] == 6
    assert c200.ghost_vertex_fixture_manifest()["count"] == 3
    assert c200.validate_ghost_vertex_parameter_record(_p())["valid"]
    bad = dict(_p()); bad["no_defaults"] = False
    with pytest.raises(ValueError): c200.validate_ghost_vertex_parameter_record(bad)
    bad = dict(_p()); bad["coupling_coordinate"] = None
    with pytest.raises(ValueError): c200.validate_ghost_vertex_parameter_record(bad)


def test_dual_vertex_routes_and_actions():
    assert c200.tree_vertex_manifest()["count"] == 6
    assert c200.connected_response_manifest()["count"] == 3
    assert c200.inverse_derivative_manifest()["count"] == 3
    assert c200.reducible_subtraction_manifest()["count"] == 18
    assert c200.amputation_manifest()["count"] == 12
    assert c200.proper_kernel_manifest()["count"] == 3
    p = _p(); v = (1, 2)
    assert c200.apply_tree_ghost_gluon_vertex(p, v)["physical"] is False
    assert c200.apply_connected_ghost_gluon_response(p, v)["result"] == "CONDITIONAL_SYMBOLIC_CONNECTED_RESPONSE"
    assert c200.apply_amputated_ghost_gluon_vertex(p, v)["result"] == "CONDITIONAL_SYMBOLIC_AMPUTATED_PROPER_VERTEX"
    assert c200.apply_proper_ghost_gluon_vertex(p, v)["result"] == "CONDITIONAL_SYMBOLIC_PROPER_GHOST_GLUON_VERTEX"


def test_projector_rescaling_boundary_and_system():
    assert c200.vertex_projector_manifest()["count"] == 18
    assert c200.rescaling_manifest()["count"] == 3
    assert c200.vertex_dressing_manifest()["count"] == 3
    assert c200.boundary_link_manifest()["count"] == 15
    j = c200.jacobian_manifest(); assert (j["dimensions"], j["rank"], j["nullity"], j["left_nullity"]) == ((2, 15), 1, 14, 1)
    assert all(not r["symmetric_split"] for r in c200.rescaling_manifest()["rows"])


def test_replacement_isolation_and_mutations():
    assert c200.st_replacement_manifest()["count"] == 3
    assert c200.ghostvert1_release_manifest()["gates"]["full_ST"] is False
    assert c200.static_isolation_guard()["pass"]
    assert all(c200.mutate_live_hqcdghostvert1(i)["pass"] for i in range(384))
    cert = c200.ghostvert1_completeness_certificate()
    assert cert["C197_ST_2_replaced"] and cert["remaining_frontier"] == 8
