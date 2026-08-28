from deuteron_wigner.bridge import hqcdrimassc43ktailsub1 as c
def test_outward():assert all(x["outward"] and x["limit_interval"][0]<=x["limit_interval"][1] for x in c.window_enclosures()["rows"])
def test_windows():assert c.window_enclosures()["all_windows_overlap"]
def test_first_omitted():assert c.limit_enclosure(41,6,.4,.2,.01,2.,"fermion")["first_omitted"]==21.5 and c.limit_enclosure(41,6,.4,.2,.01,2.,"boson")["first_omitted"]==21
def test_frontier():assert c.residual_frontier()["next"]=="C332/HQCDRIMASSC43TRANSTAIL1"
def test_reload():assert not c.load_verified_hqcdrimassc43ktailsub1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43ktailsub1(i)["pass"] for i in range(384))
