from deuteron_wigner.bridge import hqcdrimassc43fullcert1 as c
def test_combined(): assert c.combined_certificate()["numerics"]["infinite_limit_enclosed"] and c.combined_certificate()["numerics"]["all_full_rank"]
def test_nonphysical(): assert not c.combined_certificate()["domain"]["physical_prediction"]
def test_exclusions(): assert c.exclusion_certificate()["P0"].startswith("excluded") and c.exclusion_certificate()["physical_L"]=="missing"
def test_provenance(): assert c.provenance_certificate()["authority_chain_complete"]
def test_reload(): assert not c.load_verified_hqcdrimassc43fullcert1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43fullcert1(i)["pass"] for i in range(384))
