from deuteron_wigner.bridge import hqcdrimassc43transub1 as c
def test_intervals():assert all(x["outward"] and x["remainder_radius"]>0 for x in c.window_enclosures()["rows"])
def test_overlap():assert c.window_enclosures()["all_overlap"]
def test_bho_separate():assert len(c.window_enclosures()["fixed_bHO_overlap"])==9
def test_frontier():assert c.residual_frontier()["next"]=="C334/HQCDRIMASSC43BHOLIMIT1"
def test_reload():assert not c.load_verified_hqcdrimassc43transub1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43transub1(i)["pass"] for i in range(384))
