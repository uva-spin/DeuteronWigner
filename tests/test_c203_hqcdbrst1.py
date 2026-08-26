from deuteron_wigner.bridge import hqcdbrst1 as c
import pytest


def _p(r="K9"):
    return {"record_id":f"test-{r}","C202_system_or_fixture":f"C202-JAC-{r}","resolution":r,"sector_id":"P0-local","field_source_inventory":"C203-FIELD-SOURCE","brst_role":"REDUCED_P0_RESIDUAL_BRST_SOURCE_AUTHORITY","ghost_convention":"C175 Berezin order","antighost_convention":"C175 orientation","auxiliary_or_elimination":"C190 exact eliminated-auxiliary scope","gauge_fixing":"C174 project sub-gauge","source_ids":("C203-SOURCE-A_PERP","C203-SOURCE-GHOST_P0"),"bare_coupling_coordinate":"caller-supplied-symbolic-g_s","holonomy_capsule":"C183-CALLER-NONPHYSICAL","boundary_link_coordinate":"caller-bound nonmatrix interface","counterterm_coordinates":c.CT,"null_coordinates":c.NULL,"branch":"caller-continuous-symbolic","enclosure":"EXACT_SYMBOLIC_OUTWARD","provenance":"C43/C172/C174/C175","no_defaults":True,"physical":False}


def test_authority_frontier_and_runtime():
    assert c.verify_hqcd_brst1_authority()["C202_package_root"] == c.C202_ROOT
    assert c.brst_role_decision()["exact_object"] == "BRST source identities"
    assert c.brst_role_decision()["aliases"] == ("BRST source identities","BRST_SOURCE_IDENTITY")
    assert c.frontier_manifest()["first"] == "C197-ST-5"
    assert c.load_verified_hqcd_brst1_authority()["status"] == c.STATUS


def test_inventory_parameters_and_programs():
    assert c.field_source_manifest()["count"] == 17
    assert c.brst_source_manifest()["count"] == 10
    assert c.brst_program_manifest()["count"] == 10
    assert c.validate_brst_parameter_record(_p())["valid"]
    bad=dict(_p()); bad["no_defaults"]=False
    with pytest.raises(ValueError): c.validate_brst_parameter_record(bad)
    assert c.apply_brst_transformation(_p(),"A_PERP",(1,2))["physical"] is False


def test_nilpotency_action_functional_and_descendants():
    assert c.brst_transformation_manifest()["count"] == 30
    assert c.nilpotency_manifest()["count"] == 30
    assert c.action_invariance_manifest()["count"] == 45
    assert c.source_extended_action_manifest()["count"] == 3
    assert c.slavnov_functional_manifest()["count"] == 3
    assert c.descendant_manifest()["count"] == 12
    assert c.evaluate_slavnov_functional(_p())["quantum"] is False


def test_linearized_boundary_jacobian_and_replacement():
    assert c.linearized_operator_manifest()["count"] == 3
    assert c.cohomology_manifest()["count"] == 9
    assert c.boundary_global_manifest()["count"] == 33
    j=c.jacobian_manifest(); assert (j["dimensions"],j["rank"],j["nullity"],j["left_nullity"]) == ((5,15),1,14,4)
    assert c.st_replacement_manifest()["count"] == 3
    assert c.brst1_release_manifest()["gates"]["full_global_ST"] is False


def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdbrst1(i)["pass"] for i in range(384))
    assert c.brst1_completeness_certificate()["remaining_frontier"] == 5
