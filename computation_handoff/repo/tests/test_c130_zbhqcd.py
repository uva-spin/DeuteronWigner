from deuteron_wigner.bridge.zbhqcd import core as c

def test_authority_and_roots():
    r=c.verify_zbhqcd_authority()
    assert r["positive_gate"] and r["taxonomy_classes"]==18
    assert r["retained_residual_blocks"]==0 and r["vacuum_zero_mode_directions"]==2
    assert c.load_verified_zbhqcd_authority()["package_root"]==c.PACKAGE_ROOT

def test_two_route_constraints():
    assert c.p0_q0_manifest()["scope_closed"]
    assert c.surface_term_manifest()["route_mismatches"]==0
    assert c.integrated_gauss_law_manifest()["singlet_neutrality_imposed"] is False
    for r in c.RESOLUTIONS:
        assert c.residual_color_generator(r,"q")["intertwiner_residual"]==0
        assert c.residual_color_generator(r,"qg")["intertwiner_residual"]==0
        assert c.projection_identity_certificate(r)["P_R_squared_minus_P_R"]==0

def test_interfaces_are_not_zeros():
    x=c.boundary_interface_manifest("C53_CANONICAL_VERTEX",c.RESOLUTIONS[0])
    assert all(not row["retained_matrix_insertion"] for row in x["interfaces"])
    assert c.vacuum_zero_mode_manifest()["directions"][0]["represented_as_zero"] is False
    assert c.finite_basis_completeness_certificate()["feshbach"] is False

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(not c.mutate_live_zbhqcd(i)["positive_gate"] for i in range(384))
