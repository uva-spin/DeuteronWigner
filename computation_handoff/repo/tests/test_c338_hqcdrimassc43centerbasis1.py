from deuteron_wigner.bridge import hqcdrimassc43centerbasis1 as c
def test_covariance(): assert c.covariance_certificate()["pass"]
def test_gram(): assert c.gram_certificate()["full_rank"]
def test_infinite(): assert c.apbc_winding_certificate()["infinite_winding_completion_required"] and not c.apbc_winding_certificate()["finite_exact_span"]
def test_frozen(): assert c.ownership()["C301_center_invariant_subspace"]=="frozen"
def test_reload(): assert not c.load_verified_hqcdrimassc43centerbasis1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43centerbasis1(i)["pass"] for i in range(384))
