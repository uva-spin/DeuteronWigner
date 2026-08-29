from deuteron_wigner.bridge import hqcdrimassc43jmyresidue1 as c
def test_matrix():assert c.residue_matrix()["shape"]==[2,2] and len(c.residue_matrix()["rows"])==4
def test_identities():assert c.derivation_routes()["Aq_equals_Asq"] and c.derivation_routes()["Ah_equals_Ash"] and not c.derivation_routes()["foreign_operator_residue_used"]
def test_cancellation():assert all(c.cancellation_certificate()[k]==0 for k in ("alpha_pole","beta_pole","d_ln_nu1","d_ln_nu2"))
def test_fail_closed():assert c.closure()["separator_cancellation_JMY_certified"] and not c.closure()["finite_groups_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyresidue1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyresidue1(i)["pass"] for i in range(384))
