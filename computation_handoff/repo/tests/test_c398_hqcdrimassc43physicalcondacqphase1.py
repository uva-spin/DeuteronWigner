from deuteron_wigner.bridge import hqcdrimassc43physicalcondacqphase1 as c
def test_acquisition_is_structural_only():
 a=c.acquisition_ledger();assert a["structures_acquired"]==7 and a["physical_targets_acquired"]==0
 assert all(x["target_status"]=="MISSING_NOT_ZERO" for x in a["rows"])
def test_capsule_fail_closed():
 try:c.validate_target_capsule({})
 except ValueError:pass
 else:raise AssertionError
def test_rank_resolution_and_mutations():
 assert c.rank_forecast()["physical_rank"]==0 and not c.resolution_manifest()["averaged"]
 assert all(c.mutate_live_hqcdrimassc43physicalcondacqphase1(i)["pass"] for i in range(384))
def test_verify_runtime_scope():
 assert c.load_verified_hqcdrimassc43physicalcondacqphase1_authority()["physical"] is False
 assert c.static_isolation_guard()["pass"]
