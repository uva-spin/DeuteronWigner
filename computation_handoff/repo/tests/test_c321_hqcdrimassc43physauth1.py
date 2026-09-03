from deuteron_wigner.bridge import hqcdrimassc43physauth1 as c
def test_matrix():assert sum(x["available"] for x in c.authority_matrix()["rows"])==2
def test_incomplete():assert not c.authority_matrix()["physical_capsule_complete"]
def test_recovery():assert c.residual_frontier()["authority_recovery_research"]
def test_frontier():assert c.residual_frontier()["next"]=="C322/HQCDRIMASSC43BOUNDARYAUTH1"
def test_reload():assert not c.load_verified_hqcdrimassc43physauth1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43physauth1(i)["pass"] for i in range(384))
