from deuteron_wigner.bridge import hqcdrimassc43param1 as c
def test_capsules():assert len(c.capsule_family()["rows"])==3 and not c.capsule_family()["physical"]
def test_eval():assert c.validation_evaluations()["finite"] and not c.validation_evaluations()["P0_added"]
def test_parity():assert c.route_parity()["zero_theta"]
def test_frontier():assert c.residual_frontier()["next"]=="C318/HQCDRIMASSC43GRAMEVAL1"
def test_reload():assert not c.load_verified_hqcdrimassc43param1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43param1(i)["pass"] for i in range(384))
