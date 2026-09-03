from deuteron_wigner.bridge import hqcdrimassc43match1 as c
def test_audit():assert c.c43_authority_audit()["coefficient_audit"].endswith("=0")
def test_map():assert c.convention_map()["determinant"]==1 and c.convention_map()["basis_round_trip"]
def test_nonpromotion():assert c.matched_enclosures()["label"].endswith("NOT_C43_ACTION_COEFFICIENTS")
def test_K():assert set(c.matched_enclosures()["C43_action_coefficients"])=={"K9","K11","K13"}
def test_covariance():assert c.covariance_contract()["C43_cross_K_covariance"]=="UNAVAILABLE_NOT_DIAGONAL"
def test_routes():assert c.route_parity()["basis_agreement"] and not c.route_parity()["numerical_proximity_used"]
def test_release():assert c.release_manifest()["basis_match"] and not c.release_manifest()["normalization_match"]
def test_frontier():assert c.residual_frontier()["next"]=="C313/HQCDRIMASSC43EFFACT1"
def test_reload():assert c.load_verified_hqcdrimassc43match1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassc43match1(i)["pass"] for i in range(384))
