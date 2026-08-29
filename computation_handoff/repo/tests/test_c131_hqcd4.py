from deuteron_wigner.bridge.hqcd4 import core as c

def test_authority_and_roots():
    r=c.verify_projected_bare_hqcd_authority()
    assert r["positive_gate"] and r["retained_terms"]==6
    assert r["coupling_degrees"]==(0,1,2)
    assert c.load_verified_projected_bare_hqcd_authority()["package_root"]==c.PACKAGE_ROOT

def test_terms_parameters_and_nonmatrix():
    assert c.retained_term_manifest()["unclassified"]==0
    assert c.count_once_certificate()["multiply_owned_retained_terms"]==0
    assert c.bare_parameter_manifest()["mq_mq2_identity"]=="AUTHENTICATED_SOURCE_IDENTITY"
    assert c.counterterm_basis_manifest()["coefficients_selected"]==0
    assert c.vacuum_direction_manifest()["represented_as_zero"] is False
    assert c.omitted_interface_manifest()["added_to_retained"]==0

def test_dimensions_matrices_and_actions():
    for r,d in c.DIMS.items():
        for degree in (0,1,2):
            m=c.bare_coefficient_matrix(r,degree)
            assert m["shape"]==(d,d) and m["dense_allocated"] is False
            assert c.bare_coefficient_bounds(r,degree)["null_bounds"]==0
        a=c.apply_bare_polynomial(r,[0j]*d,coefficient_mode=True)
        assert a["sparse_source_used"] is False

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(not c.mutate_live_hqcd4(i)["positive_gate"] for i in range(384))
