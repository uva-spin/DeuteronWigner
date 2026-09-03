from deuteron_wigner.bridge import hqcdc117nonlocaltarget2 as c
def test_targets(): assert all(c.target_evaluation(d)["status"]=="PARAMETERIZED_EXECUTABLE" for d in c.DIRECTIONS)
def test_products(): assert all(len(c.current_product_decomposition(d)["rows"])==4 for d in c.DIRECTIONS)
def test_ward(): assert all(not c.ward_st_diagnostic(d)["claimed_zero"] for d in c.DIRECTIONS)
def test_matching(): assert all(not c.physical_matching_residual(d)["standard_physical_side_available"] for d in c.DIRECTIONS)
def test_uncertainty(): assert "A Sigma A^T" in c.correlated_uncertainty()["PSD"]
def test_routes(): assert c.two_route_derivation()["mismatches"]==0 and not c.two_route_derivation()["numerical_convergence_claim"]
def test_frontier(): assert c.residual_frontier()["next"]=="C268/HQCDC117STANDARDSIDE1"
def test_reload_scope(): assert c.static_isolation_guard()["pass"] and c.load_verified_hqcdc117nonlocaltarget2_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117nonlocaltarget2(i)["pass"] for i in range(384))
