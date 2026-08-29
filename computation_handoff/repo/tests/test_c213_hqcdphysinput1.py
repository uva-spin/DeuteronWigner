from deuteron_wigner.bridge import hqcdphysinput1 as c


def test_authenticated_standard_capsules_are_not_consumed():
    s=c.physical_source_ledger();assert s["count"]==2 and s["hash_locked"]
    assert all(not x["consumed"] for x in s["rows"])


def test_parameter_and_consumption_audits():
    assert c.parameter_authority_ledger()["count"]==9
    a=c.schema_consumption_audit();assert a["covered_classes"]==9 and not a["physical_parameter_record"]


def test_repository_exclusion_and_gap():
    assert c.repository_git_authority_audit()["complete_finite_basis_physical_records"]==0
    assert c.exclusion_quarantine_ledger()["count"]==6
    assert not c.gap_decision()["blocker"]


def test_release_handoff():
    assert c.release_manifest()["audit_complete"] and not c.release_manifest()["C197_ST_10_closed"]
    assert c.next_handoff_contract()["next"]=="C214/HQCDPHYSINPUTMAP1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdphysinput1(i)["pass"] for i in range(384))
