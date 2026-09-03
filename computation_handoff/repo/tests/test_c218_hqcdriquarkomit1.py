from deuteron_wigner.bridge import hqcdriquarkomit1 as c

def test_interface_partition():
 x=c.interface_ledger();assert (x["count"],x["closed"],x["remaining"],x["unclassified"])==(120,15,105,0)
 assert len({r["interface_id"] for r in x["rows"]})==120

def test_exact_zero_family():
 z=c.exact_zero_family_certificate();assert z["count"]==15 and z["route_mismatches"]==0
 assert all(r["status"]=="EXACT_ZERO_WITH_OPERATOR_PROOF" for r in z["rows"])

def test_partition_routes_and_hermiticity():
 assert c.partition_certificate()["count_once"]
 assert c.independent_route_certificate()["closed_family_mismatches"]==0
 assert c.hermiticity_projector_certificate()["closed_zero_family_Hermiticity"]=="EXACT"

def test_release_and_handoff():
 assert c.release_manifest()["source_nonzero_remaining"]==105
 assert not c.release_manifest()["full_self_energy_executable"]
 assert c.residual_frontier()["family_count"]==15
 assert c.next_handoff_contract()["next"]=="C219/HQCDRIQUARKFIXEDK1"

def test_authority_isolation_mutations():
 assert c.verify_hqcd_riquarkomit1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["source_nonzero_zeroed"]==0
 assert all(c.mutate_live_hqcdriquarkomit1(i)["pass"] for i in range(384))
