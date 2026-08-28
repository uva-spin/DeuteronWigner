from deuteron_wigner.bridge import hqcdrimassc43transmatch1 as c
def test_no_standard_match():assert not c.authority_matrix()["standard_match_ready"]
def test_reject_counterterm():assert not c.compatibility_decision()["C332_theta_dependent_subtraction_standard_local"]
def test_derivable():assert c.attempted_routes()["next_derivable"] and not c.attempted_routes()["contradiction"]
def test_frontier():assert c.residual_frontier()["next"]=="C336/HQCDRIMASSC43HEATKERNEL1"
def test_reload():assert not c.load_verified_hqcdrimassc43transmatch1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43transmatch1(i)["pass"] for i in range(384))
