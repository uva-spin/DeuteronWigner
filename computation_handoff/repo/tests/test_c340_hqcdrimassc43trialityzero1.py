from deuteron_wigner.bridge import hqcdrimassc43trialityzero1 as c
def test_recurrence(): assert c.recurrence_certificate()["pass"] and not c.recurrence_certificate()["W3_independent_column"]
def test_rank(): assert c.combined_limit_certificate()["all_full_rank"]
def test_recovery(): assert max(r["coefficient_max_defect"] for r in c.combined_limit_certificate()["rows"])<1e-10
def test_limit(): assert c.combined_limit_certificate()["infinite_limit_enclosed"] and not c.combined_limit_certificate()["finite_exact_span"]
def test_reload(): assert not c.load_verified_hqcdrimassc43trialityzero1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43trialityzero1(i)["pass"] for i in range(384))
