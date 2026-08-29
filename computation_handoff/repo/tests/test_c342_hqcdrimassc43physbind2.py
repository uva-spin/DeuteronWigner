from deuteron_wigner.bridge import hqcdrimassc43physbind2 as c
def test_matrix(): assert c.authority_matrix()["available_count"]==5 and c.authority_matrix()["C43_ready_count"]==1
def test_p0(): assert next(r for r in c.authority_matrix()["rows"] if r["object"]=="P0")["binding"].startswith("not applicable")
def test_sources(): assert c.source_chain()["boundary_source_hashes_verified"] and c.source_chain()["Wilson_owner_authenticated"]
def test_fail_closed(): assert not c.binding_decision()["physical_capsule_bound"] and c.binding_decision()["activation_gate"]=="NOT_READY"
def test_reload(): assert not c.load_verified_hqcdrimassc43physbind2_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43physbind2(i)["pass"] for i in range(384))
