from deuteron_wigner.bridge import hqcdrimassc43ktail1 as c
def test_cancel():assert c.symbolic_expansion()["odd_terms_cancel_pair"] and not "1/x" in c.symbolic_expansion()["paired"]
def test_coefficients():assert len(c.component_coefficients(6,.2)["rows"])==3
def test_numeric():assert c.numeric_certificate()["all_stable"]
def test_frontier():assert c.residual_frontier()["next"]=="C331/HQCDRIMASSC43KTAILSUB1"
def test_reload():assert not c.load_verified_hqcdrimassc43ktail1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43ktail1(i)["pass"] for i in range(384))
