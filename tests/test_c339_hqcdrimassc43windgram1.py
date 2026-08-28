from deuteron_wigner.bridge import hqcdrimassc43windgram1 as c
def test_rank(): assert c.increasing_rank_certificate()["all_full_rank"]
def test_recovery(): assert max(r["coefficient_max_defect"] for r in c.increasing_rank_certificate()["rows"])<1e-10
def test_separation(): assert c.separation_certificate()["C301_subspace"]=="frozen"
def test_infinite(): assert not c.increasing_rank_certificate()["finite_exact_span"]
def test_reload(): assert not c.load_verified_hqcdrimassc43windgram1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43windgram1(i)["pass"] for i in range(384))
