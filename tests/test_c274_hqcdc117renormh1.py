from deuteron_wigner.bridge import hqcdc117renormh1 as c
def test_slots():assert not c.slot_audit()["non_C117_bundle_closed"] and not c.slot_audit()["missing_as_zero"]
def test_families():assert all(c.hamiltonian_family(r)["Hermitian_by_construction"] for r in c.RESOLUTIONS)
def test_derivatives():assert len(c.derivative_program()["derivatives"])==4
def test_routes():assert c.route_audit()["symbolic_agreement"] and c.route_audit()["count_once_duplicates"]==0
def test_holdouts():assert len(c.holdout_crosswalk()["rows"])==3
def test_frontier():assert c.residual_frontier()["next"]=="C275/HQCDNONC117SLOT1"
def test_scope():assert c.static_isolation_guard()["pass"] and c.release_manifest()["C117_coordinates_selected"]==0
def test_reload():assert c.load_verified_hqcdc117renormh1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdc117renormh1(i)["pass"] for i in range(384))
