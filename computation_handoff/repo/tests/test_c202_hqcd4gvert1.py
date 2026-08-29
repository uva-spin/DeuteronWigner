from deuteron_wigner.bridge import hqcd4gvert1 as c
import pytest


def _p(r="K9"):
    return {"record_id":f"test-{r}","resolution":r,"external_domain_id":f"C202-EXT-{r}-S4-1234-12|34","st4_row_id":"C197-ST-4","quartic_tree_source_id":f"C202-TREE-{r}-S4-1234-12|34-f*f","connected_route_id":f"C202-CONN-{r}","three_vertex_derivative_id":f"C202-DER3-{r}","inverse_second_derivative_id":f"C202-DER2-{r}","amputation_ids":(f"C202-AMP-{r}-1",f"C202-AMP-{r}-2",f"C202-AMP-{r}-3",f"C202-AMP-{r}-4"),"projector_id":"C202-PROJ-QUARTIC","pair_channel_id":"12|34","bare_coupling_coordinate":"caller-supplied-symbolic-g_s","gluon_field_scheme":"C184 caller-supplied scheme","ghost_fixture_id":"C202-4G-FIXTURE-K9","three_gluon_record_id":"C201-PROPER-K9","active_flavor_record":"caller-supplied explicit flavor record","holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","boundary_link_coordinate":"caller-supplied nonmatrix interface","counterterm_coordinates":c.CT,"null_coordinates":c.NULL,"branch_id":"caller-continuous-nonzero","subtraction_coordinate":"NONZERO-K9","enclosure":"EXACT_SYMBOLIC_OUTWARD","units":"C184 source units","no_defaults":True,"physical":False}


def test_authority_frontier_and_runtime():
    assert c.verify_hqcd_4gvert1_authority()["C201_package_root"] == c.C201_ROOT
    role=c.vertex_role_decision()
    assert role["exact_object"] == "complete four-gluon renormalization"
    assert c.frontier_manifest()["first"] == "C197-ST-4"
    assert c.load_verified_hqcd_4gvert1_authority()["status"] == c.STATUS


def test_domains_parameters_and_tree():
    assert c.external_domain_manifest()["count"] == 216
    assert c.four_gluon_fixture_manifest()["count"] == 3
    assert c.validate_four_gluon_parameter_record(_p())["valid"]
    bad=dict(_p()); bad["no_defaults"]=False
    with pytest.raises(ValueError): c.validate_four_gluon_parameter_record(bad)
    assert c.tree_vertex_manifest()["count"] == 648
    assert c.apply_tree_four_gluon_vertex(_p(),(1,2))["physical"] is False


def test_response_components_and_proper_routes():
    assert c.connected_response_manifest()["count"] == 3
    assert c.three_vertex_derivative_manifest()["count"] == 3
    assert c.inverse_second_derivative_manifest()["count"] == 3
    assert c.component_manifest()["count"] == 648
    assert c.reducible_subtraction_manifest()["count"] == 81
    assert c.amputation_manifest()["count"] == 21
    assert c.proper_kernel_manifest()["count"] == 3
    assert c.apply_connected_four_gluon_response(_p(),(1,))["physical"] is False
    assert c.apply_amputated_four_gluon_vertex(_p(),(1,))["physical"] is False
    assert c.apply_proper_four_gluon_vertex(_p(),(1,))["physical"] is False


def test_projectors_interfaces_jacobian():
    assert c.vertex_projector_manifest()["count"] == 7128
    assert c.vertex_dressing_manifest()["count"] == 3
    assert c.boundary_link_manifest()["count"] == 36
    j=c.jacobian_manifest(); assert (j["dimensions"],j["rank"],j["nullity"],j["left_nullity"]) == ((4,15),1,14,3)
    assert c.four_gvert1_release_manifest()["gates"]["full_ST"] is False


def test_replacement_isolation_and_mutations():
    assert c.st_replacement_manifest()["count"] == 3
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcd4gvert1(i)["pass"] for i in range(384))
    assert c.four_gvert1_completeness_certificate()["remaining_frontier"] == 6
