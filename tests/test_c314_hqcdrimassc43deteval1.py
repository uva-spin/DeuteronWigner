from deuteron_wigner.bridge import hqcdrimassc43deteval1 as c
def test_scan():assert len(c.regulator_scan()["N"])==5
def test_owners():assert len(c.regulator_scan()["owners"])==5
def test_reality():assert c.spectral_reduction()["reality"].startswith("paired")
def test_tail():assert not c.tail_certificate()["rational_coefficient_guessed"]
def test_unavailable():assert not c.finite_functionals()["evaluated"]
def test_projection():assert set(c.gram_projection()["basis"])=={"CHI8","RE_TF3"}
def test_covariance():assert c.covariance_contract()["correlated"]
def test_routes():assert c.route_parity()["symbolic_agreement"]
def test_frontier():assert c.residual_frontier()["next"]=="C315/HQCDRIMASSC43SPECTRUM1"
def test_reload():assert c.load_verified_hqcdrimassc43deteval1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassc43deteval1(i)["pass"] for i in range(384))
