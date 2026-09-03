from deuteron_wigner.bridge import hqcdphysadaptercalc1 as c


def test_six_capsules_reconciled():
    assert c.capsule_reconciliation_manifest()["count"]==6
    assert c.contribution_reconciliation_manifest()["count"]==6


def test_safe_partial_programs():
    s=c.partial_program_schema();assert not s["eval"] and not s["pickle"] and not s["callbacks"]
    p=c.partial_program_manifest();assert p["partial_programs"]==6 and p["executable_programs"]==0


def test_routes_and_ordered_residual():
    assert c.route_certificate_manifest()["closed_routes"]==0
    f=c.residual_frontier_manifest();assert f["count"]==6 and f["first"].endswith("QUARK_FIELD-RI_SMOM-2")


def test_release_handoff():
    assert c.release_manifest()["partial_programs"]==6
    assert c.next_handoff_contract()["next"]=="C216/HQCDRIQUARKADAPTER1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdphysadaptercalc1(i)["pass"] for i in range(384))
