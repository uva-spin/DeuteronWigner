from deuteron_wigner.bridge import hqcdstboundary2 as c
import pytest


def _p(r="K9", ep="LEFT"):
    return {"record_id":f"test-{r}-{ep}","resolution":r,"endpoint":ep,
        "orientation":"SOURCE_TO_SINK","link_order":1,"boundary_class":"PV",
        "holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","ghost_source_id":"C175-GHOST",
        "antighost_source_id":"C175-ANTIGHOST","residual_link_id":"C182-LINK",
        "boundary_pullback_id":"C181-PULLBACK","counterterm_coordinates":c.CT,
        "null_coordinates":c.NULL,"branch":"caller-symbolic","enclosure":"EXACT_SYMBOLIC_OUTWARD",
        "no_defaults":True,"physical":False}


def test_authority_and_frontier():
    assert c.verify_hqcd_stboundary2_authority()["C203_package_root"] == c.C203_ROOT
    assert c.frontier_manifest("C197-ST-6")["rows"][0]["aliases"] == ("endpoint ghost/link identities","ENDPOINT_GHOST_LINK_IDENTITY")
    assert c.frontier_manifest()["ordered_remaining"][0] == "C197-ST-7"


def test_inventory_parameters_and_safe_programs():
    assert c.endpoint_inventory_manifest()["count"] == 120
    assert c.endpoint_program_manifest()["count"] == 5
    assert c.validate_endpoint_parameter_record(_p())["valid"]
    bad=dict(_p()); bad["holonomy_capsule_id"]="identity"
    with pytest.raises(ValueError): c.validate_endpoint_parameter_record(bad)
    assert c.apply_endpoint_transformation(_p(),"RESIDUAL_LINK",(1,2))["physical"] is False


def test_endpoint_identities_routes_and_remainders():
    assert c.endpoint_transformation_manifest()["count"] == 30
    assert c.endpoint_identity_manifest()["count"] == 96
    assert c.boundary_pullback_commutator_manifest()["count"] == 9
    assert c.endpoint_nilpotency_manifest()["count"] == 18
    assert c.cut_holonomy_remainder_manifest()["count"] == 4
    ident=c.endpoint_identity_manifest()["rows"][0]["identity_id"]
    assert c.evaluate_endpoint_identity(_p(),ident)["holonomy_global_remainder"] == "TYPED_UNAVAILABLE_NOT_ZERO"


def test_jacobian_replacement_and_scope():
    j=c.jacobian_manifest()
    assert (j["dimensions"],j["rank"],j["nullity"],j["left_nullity"]) == ((6,15),1,14,5)
    assert c.st_replacement_manifest()["count"] == 3
    assert c.st_replacement_manifest()["unrelated_rows_changed"] == 0
    assert c.stboundary2_release_manifest()["gates"]["global_zero_mode"] is False
    assert c.next_st_handoff_contract()["next_object"] == "C197-ST-7"


def test_count_once_isolation_and_mutations():
    assert c.topology_manifest()["count"] == c.count_once_manifest()["count"]
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdstboundary2(i)["pass"] for i in range(384))
    assert c.stboundary2_completeness_certificate()["remaining_frontier"] == 4
