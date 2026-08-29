from deuteron_wigner.bridge import hqcdc117standardside1 as c
def test_audit():assert all(c.standard_side_audit(d)["unavailable_not_zero"] for d in c.DIRECTIONS)
def test_matching():assert c.matching_residuals()["closed"]==0 and c.matching_residuals()["required"]==4
def test_routes():assert not c.source_route_audit()["contradiction"] and not c.source_route_audit()["fabricated"]
def test_uncertainty():assert c.uncertainty_boundary()["standard_side_covariance"] is None
def test_frontier():assert c.residual_frontier()["next"]=="C269/HQCDC117PHYSICALCHANNEL1"
def test_scope():assert c.static_isolation_guard()["pass"] and c.release_manifest()["coefficients_selected"]==0
def test_reload():assert c.load_verified_hqcdc117standardside1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdc117standardside1(i)["pass"] for i in range(384))
