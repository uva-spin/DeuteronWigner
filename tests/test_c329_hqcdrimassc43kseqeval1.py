from deuteron_wigner.bridge import hqcdrimassc43kseqeval1 as c
def test_grid():assert c.grid_results()["count"]==81 and c.grid_results()["all_finite"]
def test_differences():assert c.adjacent_differences()["count"]==162 and c.adjacent_differences()["all_axes"]==("K2","Nmax","bHO_GeV")
def test_no_fit():assert c.static_isolation_guard()["fit_powers"]==0
def test_frontier():assert c.residual_frontier()["next"]=="C330/HQCDRIMASSC43KTAIL1"
def test_reload():assert not c.load_verified_hqcdrimassc43kseqeval1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43kseqeval1(i)["pass"] for i in range(384))
