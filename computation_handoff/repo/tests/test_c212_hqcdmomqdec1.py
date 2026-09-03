from deuteron_wigner.bridge import hqcdmomqdec1 as c


def test_dependency_and_independent_audits():
    assert c.dependency_ledger()["all_closed"]
    assert c.independent_closure_audits()["count"] == 2
    assert c.independent_closure_audits()["agree"]


def test_decision_is_scoped_nonphysical():
    d = c.closure_decision()
    assert d["object_id"] == "C197-ST-9"
    assert not d["physical_parameterization"] and not d["numerical_continuum_value"]


def test_nonclaims_and_frontier():
    assert c.nonclaim_ledger()["count"] == 8
    f = c.frontier_manifest()
    assert f["first"] == "C197-ST-10" and f["ordered_remaining"] == ("C197-ST-10",)


def test_release_and_handoff():
    assert c.release_manifest()["C197_ST_9_closed"] and not c.release_manifest()["C197_ST_10_closed"]
    assert c.next_handoff_contract()["next"] == "C213/HQCDPHYSINPUT1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdmomqdec1(i)["pass"] for i in range(384))
