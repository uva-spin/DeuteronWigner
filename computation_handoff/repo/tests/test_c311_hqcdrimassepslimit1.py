from deuteron_wigner.bridge import hqcdrimassepslimit1 as c
def test_scan():assert len(c.epsilon_scan()["epsilon"])==7
def test_order():assert c.epsilon_scan()["limit_order"].startswith("N-tail")
def test_models():assert len(c.extrapolation_models()["windows"])==3
def test_limits():assert not c.limit_enclosures()["point_value_claim"]
def test_covariance():assert c.covariance_contract()["positive_semidefinite"]
def test_stability():assert c.stability_certificate()["route_agreement"]
def test_nonclaim():assert not c.release_manifest()["C43_matching"]
def test_frontier():assert c.residual_frontier()["next"]=="C312/HQCDRIMASSC43MATCH1"
def test_reload():assert c.load_verified_hqcdrimassepslimit1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassepslimit1(i)["pass"] for i in range(384))
