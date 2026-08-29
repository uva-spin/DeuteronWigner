import pytest
from deuteron_wigner.bridge import hqcdriquarkadapter1 as c


def test_request_and_structural_authority():
    assert c.request_freeze()["request_id"]==c.REQUEST_ID
    assert c.structural_authority_ledger()["complete"]==7


def test_common_state_is_strict():
    p={k:"caller-bound" for k in c.common_state_schema()["required_fields"]}
    p.update(record_id="C216-TEST",resolution="K9",rho="rho",mu="mu",no_defaults=True,physical=False)
    assert c.validate_common_state(p)["valid"]
    with pytest.raises(ValueError): c.validate_common_state({})


def test_contributions_programs_routes():
    assert c.two_point_contribution_ledger()["count"]==7
    assert c.adapter_program_manifest()["count"]==3 and c.adapter_program_manifest()["executable"]==0
    assert c.route_certificate_manifest()["closed_routes"]==0


def test_release_handoff():
    assert not c.release_manifest()["self_energy_complete"]
    assert c.next_handoff_contract()["next"]=="C217/HQCDRIQUARKSELF1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdriquarkadapter1(i)["pass"] for i in range(384))
