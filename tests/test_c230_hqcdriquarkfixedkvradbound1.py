from deuteron_wigner.bridge import hqcdriquarkfixedkvradbound1 as c
def test_factors():assert c.factorization_manifest()["count"]==8 and c.factorization_manifest()["source_hash_mismatches"]==0
def test_bound_boundary():assert not c.bound_program_manifest()["complete"] and not c.bound_program_manifest()["numeric_quadrature_promoted"]
def test_routes():assert c.route_certificate()["factor_mismatches"]==0
def test_release():assert c.release_manifest()["factors"]==8 and c.release_manifest()["certified_bounds"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvradbound1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvradbound1(i)["pass"] for i in range(384))
