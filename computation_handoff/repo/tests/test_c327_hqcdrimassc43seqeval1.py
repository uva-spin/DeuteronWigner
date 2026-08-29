from deuteron_wigner.bridge import hqcdrimassc43seqeval1 as c
def test_grid():assert c.sequence_results()["count"]==162 and c.sequence_results()["all_finite"]
def test_axes():
 a=c.axis_certificate();assert a["Nmax_nontrivial"] and a["bHO_nontrivial"] and a["sum_cutoff_nontrivial"] and not a["K2_nontrivial"]
def test_holdout():assert c.ownership()["dynamical_PBC_zero_mode"].startswith("EXPLICIT_HOLDOUT")
def test_frontier():assert c.residual_frontier()["next"]=="C328/HQCDRIMASSC43KHARMONIC1"
def test_reload():assert not c.load_verified_hqcdrimassc43seqeval1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43seqeval1(i)["pass"] for i in range(384))
