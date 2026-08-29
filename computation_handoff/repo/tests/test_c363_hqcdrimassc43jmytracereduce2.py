from deuteron_wigner.bridge import hqcdrimassc43jmytracereduce2 as c
def test_scalars():assert c.scalar_traces()["count"]==6 and "2(d-2)" in c.scalar_traces()["rows"][0]["scalar"]
def test_cut_order():assert c.cut_substitution()["order"].startswith("trace")
def test_holdout():assert c.denominator_holdout()["recovered"] and "kT^2+x lambda^2" in c.denominator_holdout()["qq"]
def test_routes():assert c.route_validation()["agreement"] and not c.closure()["counterterm_scalar_reduction"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmytracereduce2_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmytracereduce2(i)["pass"] for i in range(384))
