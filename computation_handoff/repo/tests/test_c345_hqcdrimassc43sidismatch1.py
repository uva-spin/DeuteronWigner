from deuteron_wigner.bridge import hqcdrimassc43sidismatch1 as c
def test_coordinates(): assert c.typed_coordinates()["bound_count"]==2 and c.typed_coordinates()["free_count"]==6
def test_equations(): assert c.compatibility_equations()["equations_consistent"] and not c.compatibility_equations()["unique_solution"]
def test_no_defaults(): assert not c.authority_audit()["mu_equals_Q_authorized"] and not c.authority_audit()["L_equals_inverse_Q_authorized"]
def test_covariance(): assert c.covariance_map()["cross_blocks"].startswith("missing")
def test_reload(): assert not c.load_verified_hqcdrimassc43sidismatch1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43sidismatch1(i)["pass"] for i in range(384))
