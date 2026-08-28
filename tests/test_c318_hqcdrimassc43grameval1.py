from deuteron_wigner.bridge import hqcdrimassc43grameval1 as c
def test_design():assert len(c.evaluation_design()["quadrature"])==3
def test_results():assert c.non_p0_results()["count"]==3 and not any(x["P0_added"] for x in c.non_p0_results()["rows"])
def test_parity():assert c.route_parity()["direct_vs_normal_equations"]
def test_frontier():assert c.residual_frontier()["next"]=="C319/HQCDRIMASSC43P0FUNC1"
def test_reload():assert not c.load_verified_hqcdrimassc43grameval1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43grameval1(i)["pass"] for i in range(384))
