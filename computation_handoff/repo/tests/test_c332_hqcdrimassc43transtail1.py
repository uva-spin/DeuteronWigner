from deuteron_wigner.bridge import hqcdrimassc43transtail1 as c
def test_divergences():assert c.shell_expansion()["linear_divergence"] and c.shell_expansion()["log_divergence"]
def test_coefficients():assert all(c.divergence_coefficients(9,.4,.2,.01,2.,o)["mode_count"]>0 for o in ("boson","fermion","constraint"))
def test_numeric():assert c.subtracted_sequence()["all_stable"]
def test_frontier():assert c.residual_frontier()["next"]=="C333/HQCDRIMASSC43TRANSUB1"
def test_reload():assert not c.load_verified_hqcdrimassc43transtail1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43transtail1(i)["pass"] for i in range(384))
