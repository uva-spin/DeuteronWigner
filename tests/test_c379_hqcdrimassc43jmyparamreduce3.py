from deuteron_wigner.bridge import hqcdrimassc43jmyparamreduce3 as c
def test_real():assert c.real_polynomials()["count"]==4 and "4*(1-epsilon)" in c.real_polynomials()["rows"][0]["numerator"]
def test_loop():assert c.loop_polynomials()["count"]==4
def test_soft():assert c.soft_polynomials()["count"]==4 and c.soft_polynomials()["count_once"]
def test_round():assert c.round_trip()["agreement"] and c.round_trip()["mass_terms"]==0
def test_reload():assert not c.load_verified_hqcdrimassc43jmyparamreduce3_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyparamreduce3(i)["pass"] for i in range(384))
