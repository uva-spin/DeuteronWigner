from deuteron_wigner.bridge.hqcdghost2 import core as c


def _parameter(resolution="K9"):
    return {
        "parameter_id": "C199-NONPHYSICAL-FIXTURE-K9",
        "resolution": resolution,
        "sector_id": "P0",
        "external_ghost_record_id": f"C199-EXT-{resolution}-P0-GHOST",
        "external_antighost_record_id": f"C199-EXT-{resolution}-P0-ANTIGHOST",
        "free_operator_id": f"C199-FP-{resolution}-P0-C175-P0-FP-FREE",
        "complete_operator_ids": (f"C199-FP-{resolution}-P0-C175-P0-FP-FREE", f"C199-FP-{resolution}-P0-C175-P0-FP-COMMUTATOR"),
        "projector_scheme_id": "FP_EIGENMODE_NORMALIZATION",
        "subtraction_coordinate": f"P0-FP-EIGENMODE-{resolution}-NONZERO",
        "fixture_id": f"C199-GHOST-FIXTURE-{resolution}",
        "holonomy_capsule_id": "C183-CALLER-NONPHYSICAL",
        "boundary_link_coordinate": "caller-supplied-nonmatrix",
        "counterterm_coordinates": c.COUNTERTERMS,
        "null_coordinates": c.NULLS,
        "branch_id": "CALLER-CONTINUATION-NONPHYSICAL",
        "enclosure": "EXACT_SYMBOLIC_OUTWARD",
        "units": "source-defined FP units",
        "no_defaults": True,
        "physical": False,
    }


def test_authority_runtime_and_role():
    assert c.load_verified_hqcd_ghost2_authority()["package_root"] == c.C199_PACKAGE_ROOT
    assert c.ghost_role_decision()["decision"] == "Q0_DECOUPLED_P0_CONDITIONAL_RENORMALIZATION"
    assert c.ghost_role_decision()["aliases"] == ("complete ghost-field renormalization", "GHOST_FIELD_RENORMALIZATION")


def test_domains_sources_and_operators():
    assert c.ghost_decomposition_manifest()["count"] == 6
    assert c.external_ghost_manifest()["count"] == 12
    assert c.ghost_fixture_manifest()["count"] == 3
    assert c.fp_operator_manifest()["count"] == 72
    assert c.fp_operator_manifest()["matrix_owner_count"] == 18
    assert c.fp_operator_manifest()["nonmatrix_interface_count"] == 54
    assert c.validate_ghost_parameter_record(_parameter())["valid"]
    assert c.apply_fp_operator(_parameter(), (0, 1))["input_length"] == 2
    try:
        c.apply_fp_operator(_parameter(), (0,), owner_id="C175-RESIDUAL-LINK-OPERATOR")
    except TypeError:
        pass
    else:
        raise AssertionError("nonmatrix owner accepted as matrix")


def test_two_point_determinant_and_response_separation():
    assert c.determinant_separation_manifest()["count"] == 3
    assert c.ghost_two_point_manifest()["count"] == 6
    assert c.ghost_gluon_response_manifest()["count"] == 3
    assert c.ghost_gluon_response_manifest()["rows"][0]["status"] == "USED_SOURCE_QUALIFIED"
    assert c.apply_ghost_propagator(_parameter(), (1, 2))["dense_inverse"] is False
    assert c.apply_inverse_ghost_two_point(_parameter(), (1,))["physical"] is False


def test_projector_convention_factor_and_replacement():
    assert c.boundary_link_manifest()["count"] == 18
    assert c.ghost_projector_manifest()["count"] == 9
    assert c.ghost_convention_manifest()["count"] == 2
    assert c.zghost_manifest()["count"] == 3
    assert c.evaluate_ghost_field_factor(_parameter())["selected"] is False
    assert c.st_replacement_manifest()["count"] == 3
    assert all(x["unrelated_C198_rows_changed"] == 0 for x in c.st_replacement_manifest()["rows"])


def test_jacobian_frontier_release_and_nonmutation():
    assert c.jacobian_manifest()["dimensions"] == (1, 15)
    assert c.jacobian_manifest()["rank"] == 0
    assert c.jacobian_manifest()["nullity"] == 15
    assert c.ghost2_release_manifest()["gates"]["full_ST"] is False
    assert c.ghost2_release_manifest()["decision"].startswith("COMPLETE_CONDITIONAL")
    assert c.dependency_frontier_manifest()["first"] == "C197-ST-2"
    assert c.missing_ghost_object_manifest()["count"] == 9
    assert c.next_st_handoff_contract()["next_object"] == "C197-ST-2"
    assert c.static_isolation_guard()["pass"] is True
    assert sum(c.mutate_live_hqcdghost2(i)["pass"] for i in range(384)) == 384
