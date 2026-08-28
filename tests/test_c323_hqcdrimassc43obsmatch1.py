from deuteron_wigner.bridge import hqcdrimassc43obsmatch1 as c
def test_owner():assert c.operator_owner()["physical_owner_authenticated"]
def test_match_missing():assert not c.matching_audit()["continuum_match_complete"]
def test_validation_not_physical():assert c.matching_audit()["K9_K11_K13_role"]=="NONPHYSICAL_VALIDATION_ONLY"
def test_frontier():assert c.residual_frontier()["next"]=="C324/HQCDRIMASSC43CONVERGE1"
def test_reload():assert not c.load_verified_hqcdrimassc43obsmatch1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43obsmatch1(i)["pass"] for i in range(384))
