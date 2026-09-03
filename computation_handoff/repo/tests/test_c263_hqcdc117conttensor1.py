from deuteron_wigner.bridge import hqcdc117conttensor1 as c
def test_locality(): assert c.locality_classification()["local"]==0 and c.locality_classification()["nonlocal_or_external"]==4
def test_routes(): assert c.preimage_route_a()["local_vertices"]==0 and c.preimage_route_b()["mismatches"]==0
def test_capsules(): assert c.tensor_capsules()["not_applicable_with_proof"]==4 and c.tensor_capsules()["fabricated_tensors"]==0
def test_rismom_scope(): assert not c.local_rismom_applicability()["PROJECT_C117_RI_SMOM_V1_local_insertions"] and c.local_rismom_applicability()["generic_RI_SMOM_architecture_preserved"]
def test_nonlocal_schema(): assert c.nonlocal_matching_schema()["condition_count"]==4 and c.nonlocal_matching_schema()["rank_required"]==4
def test_frontier(): assert c.residual_frontier()["next"]=="C264/HQCDC117NONLOCALMATCH1" and not c.residual_frontier()["blocker"]
def test_reload_scope(): assert c.static_isolation_guard()["pass"] and c.load_verified_hqcdc117conttensor1_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117conttensor1(i)["pass"] for i in range(384))
