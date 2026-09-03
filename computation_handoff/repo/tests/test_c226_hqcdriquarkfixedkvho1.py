from deuteron_wigner.bridge import hqcdriquarkfixedkvho1 as c
def test_domain():assert "infinity" in c.projection_domain_schema()["integral"]
def test_audit():assert c.expansion_audit()["count"]==8 and c.expansion_audit()["normal_forms"]==0
def test_forbidden():assert not c.forbidden_projection_certificate()["simple_polynomial_projection"] and not c.forbidden_projection_certificate()["C50_square_grid_quadrature_promoted"]
def test_release():assert not c.release_manifest()["HO_projection_ready"] and c.next_handoff_contract()["next"]=="C227/HQCDRIQUARKFIXEDKVNORM1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvho1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvho1(i)["pass"] for i in range(384))
