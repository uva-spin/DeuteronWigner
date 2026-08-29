from deuteron_wigner.bridge import hqcdrimassc43spectrum1 as c
def test_source():assert c.source_freeze()["C40_separate"]
def test_boundary():assert not c.boundary_class_ledger()["physical_selection"]
def test_resolutions():assert [x["resolution"] for x in c.resolution_spectra()["rows"]]==["K9","K11","K13"]
def test_units():assert c.resolution_spectra()["units"].startswith("GeV")
def test_degeneracy():assert c.degeneracy_certificate()["count_once"]
def test_p0():assert c.functional_adapter()["P0"].startswith("GLOBAL_P0")
def test_covariance():assert c.covariance_contract()["cross_K"].startswith("required")
def test_routes():assert c.route_parity()["mode_count_agreement"] and c.route_parity()["trace_agreement"]
def test_frontier():assert c.residual_frontier()["next"]=="C316/HQCDRIMASSC43DETEVAL2"
def test_reload():assert c.load_verified_hqcdrimassc43spectrum1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassc43spectrum1(i)["pass"] for i in range(384))
