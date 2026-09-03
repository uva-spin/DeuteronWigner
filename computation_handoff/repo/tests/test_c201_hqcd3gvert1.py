from deuteron_wigner.bridge import hqcd3gvert1 as c
import pytest


def _p(r="K9"):
    return {"record_id":f"test-{r}","resolution":r,"external_domain_id":f"C201-EXT-{r}-S3-E","st3_row_id":"C197-ST-3","tree_source_id":f"C201-TREE-{r}-S3-E-f-type","connected_route_id":f"C201-CONN-{r}","inverse_derivative_id":f"C201-DINV-{r}","amputation_ids":(f"C201-AMP-{r}-1",f"C201-AMP-{r}-2",f"C201-AMP-{r}-3"),"projector_id":"C201-PROJ-F","bare_coupling_coordinate":"caller-supplied-symbolic-g_s","gluon_field_scheme":"C184 caller-supplied scheme","ghost_fixture_id":"C200-GHOSTVERT-FIXTURE-K9","active_flavor_record":"caller-supplied explicit flavor record","holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","boundary_link_coordinate":"caller-supplied nonmatrix interface","counterterm_coordinates":c.COUNTERTERMS,"null_coordinates":c.NULLS,"branch_id":"caller-continuous-nonzero","subtraction_coordinate":"NONZERO-K9","enclosure":"EXACT_SYMBOLIC_OUTWARD","units":"C184 source units","no_defaults":True,"physical":False}


def test_authority_frontier_and_runtime():
    assert c.verify_hqcd_3gvert1_authority()["C200_package_root"] == c.C200_ROOT
    assert c.vertex_role_decision()["exact_object"] == "complete three-gluon proper vertex renormalization"
    assert c.vertex_role_decision()["aliases"] == ("complete three-gluon proper vertex renormalization","THREE_GLUON_PROPER_VERTEX")
    assert c.frontier_manifest()["first"] == "C197-ST-3"
    assert c.load_verified_hqcd_3gvert1_authority()["status"] == c.STATUS


def test_domains_parameters_and_tree():
    assert c.external_domain_manifest()["count"] == 18
    assert c.three_gluon_fixture_manifest()["count"] == 3
    assert c.validate_three_gluon_parameter_record(_p())["valid"]
    bad=dict(_p()); bad["no_defaults"]=False
    with pytest.raises(ValueError): c.validate_three_gluon_parameter_record(bad)
    assert c.tree_vertex_manifest()["count"] == 36
    assert c.apply_tree_three_gluon_vertex(_p(),(1,2))["physical"] is False


def test_response_components_and_proper_routes():
    assert c.connected_response_manifest()["count"] == 3
    assert c.inverse_derivative_manifest()["count"] == 3
    assert c.component_manifest()["count"] == 144
    assert c.reducible_subtraction_manifest()["count"] == 18
    assert c.amputation_manifest()["count"] == 18
    assert c.proper_kernel_manifest()["count"] == 3
    assert c.apply_connected_three_gluon_response(_p(),(1,))["physical"] is False
    assert c.apply_amputated_three_gluon_vertex(_p(),(1,))["physical"] is False
    assert c.apply_proper_three_gluon_vertex(_p(),(1,))["physical"] is False


def test_projectors_interfaces_jacobian():
    assert c.vertex_projector_manifest()["count"] == 288
    assert c.vertex_dressing_manifest()["count"] == 3
    assert c.boundary_link_manifest()["count"] == 33
    j=c.jacobian_manifest(); assert (j["dimensions"],j["rank"],j["nullity"],j["left_nullity"]) == ((3,15),1,14,2)
    assert c.ghostvert1_release_manifest()["gates"]["full_ST"] is False


def test_replacement_isolation_and_mutations():
    assert c.st_replacement_manifest()["count"] == 3
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcd3gvert1(i)["pass"] for i in range(384))
    assert c.three_gvert1_completeness_certificate()["remaining_frontier"] == 7
