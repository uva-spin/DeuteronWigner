from deuteron_wigner.bridge import hqcdrimassshapetail1 as c
def test_ast():assert c.asymptotic_authority()["source"].startswith("authenticated C303")
def test_scan():assert c.extended_scan()["count"]==27 and c.extended_scan()["N_range"][-1]==1024
def test_windows():assert len(c.tail_enclosures()["windows"])==4
def test_no_guess():assert c.asymptotic_authority()["exact_rational_claim"] is False
def test_separate():assert set(c.finite_remainders()["subtraction_owners"])=={"center","CHI8","RE_TF3"}
def test_order():assert c.finite_remainders()["epsilon_extrapolated"] is False
def test_covariance():assert len(c.covariance_contract()["correlation"])==4
def test_stability():assert c.stability_certificate()["all_within_outward_enclosures"]
def test_frontier():assert c.residual_frontier()["next"]=="C311/HQCDRIMASSEPSLIMIT1"
def test_reload():assert c.load_verified_hqcdrimassshapetail1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassshapetail1(i)["pass"] for i in range(384))
