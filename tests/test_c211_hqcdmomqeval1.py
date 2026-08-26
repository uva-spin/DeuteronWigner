import pytest
from deuteron_wigner.bridge import hqcdmomqeval1 as c


def test_named_fixtures_are_complete_nonphysical():
    assert c.fixture_manifest()["count"] == 3
    assert all(c.validate_fixture(c.named_fixture(r))["valid"] for r in c.RESOLUTIONS)


def test_routes_and_overlap():
    assert c.route_evaluation_manifest()["count"] == 9
    assert c.overlap_certificate_manifest()["count"] == 3


def test_execution_and_rejection():
    assert c.evaluate_fixture(c.named_fixture("K9"))["physical"] is False
    bad = dict(c.named_fixture("K9")); bad["gram_zero_excluded"] = False
    with pytest.raises(ValueError): c.validate_fixture(bad)


def test_release_and_handoff():
    assert c.release_manifest()["fixtures_evaluated"] == 3
    assert c.next_handoff_contract()["next"] == "C212/HQCDMOMQDEC1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdmomqeval1(i)["pass"] for i in range(384))
