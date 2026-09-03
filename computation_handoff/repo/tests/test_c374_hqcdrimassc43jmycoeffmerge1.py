from deuteron_wigner.bridge import hqcdrimassc43jmycoeffmerge1 as c
def test_matrix():assert c.merged_matrix()["count"]==14 and c.merged_matrix()["C370_term_coverage"]==13
def test_exclusion():assert c.exclusion_proof()["pass"] and c.exclusion_proof()["occurrences"]==0
def test_routes():assert c.route_validation()["agreement"] and c.route_validation()["soft_count_once"]=="PASS"
def test_gate():assert c.closure()["Laurent_evaluation_ready"] and not c.closure()["Laurent_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmycoeffmerge1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmycoeffmerge1(i)["pass"] for i in range(384))
