from deuteron_wigner.bridge.hqcdren import core as c

def test_fail_closed_authority():
    r=c.verify_hqcd_renormalization_authority()
    assert not r["positive_gate"]
    assert r["blocker"]=="C132_HQCDREN_CONDITION_AUTHORITY_INCOMPLETE"
    assert r["source_qualified_nonempty_conditions"]==0
    assert c.load_verified_hqcd_renormalization_authority()["package_root"]==c.PACKAGE_ROOT

def test_conditions_roles_and_parameters():
    assert c.condition_role_manifest()["calibration"]==()
    assert c.renormalization_scheme_manifest()["selected"] is False
    assert c.unknown_parameter_manifest()["mq_mq2_ambiguity"]==0
    assert c.counterterm_condition_crosswalk()["directions"]
    assert c.identifiability_report()["rank"]==0
    assert all(not c.null_direction_manifest()["zeroed"] for _ in range(1))

def test_numeric_routes_fail_closed():
    for r in c.RESOLUTIONS:
        try: c.renormalized_parameter_point(r)
        except RuntimeError: pass
        else: raise AssertionError("parameter point unexpectedly available")
        try: c.renormalized_sparse_matrix(r)
        except RuntimeError: pass
        else: raise AssertionError("matrix unexpectedly available")
        assert c.constraint_preservation_certificate(r)["omitted_interfaces_inserted"]==0

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(not c.mutate_live_hqcdren(i)["positive_gate"] for i in range(384))
