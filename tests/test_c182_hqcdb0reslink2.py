from __future__ import annotations

import pytest

from deuteron_wigner.bridge import hqcdb0reslink2 as c


def test_contract_plan_and_public_handoff():
    loaded = c.load_verified_hqcd_b0reslink2_authority()
    assert loaded["status"] == c.STATUS
    assert loaded["plan"] == "RESLINK2-B"
    assert c.b0reslink2_plan_manifest()["next"] == "C183/HQCDB0HOLONOMY2"
    assert c.link_handoff_freeze()["C181_package_root"] == c.c181.PACKAGE_ROOT


def test_strict_parameter_layers_and_no_defaults():
    for fixture_id in c.FIXTURE_IDS:
        record = c.fixture_parameter_record(fixture_id)
        assert c.validate_parameter_record(record)["validated"] is True
        assert record["coupling"]["value"] == 0.25
        assert record["holonomy"]["identity_selected"] is False
    bad = dict(c.fixture_parameter_record(c.FIXTURE_IDS[0]))
    bad.pop("coupling")
    with pytest.raises(ValueError):
        c.validate_parameter_record(bad)
    bad = dict(c.fixture_parameter_record(c.FIXTURE_IDS[0]))
    bad["holonomy"] = {"status": "identity", "identity_selected": True}
    with pytest.raises(ValueError):
        c.validate_parameter_record(bad)


def test_trace_link_color_and_order_domains():
    traces = c.boundary_trace_manifest("K9")["rows"]
    assert len(traces) == 8
    assert {row["cut_side_id"] for row in traces} == set(c.CUT_SIDES)
    assert all(not row["Q0_zero_assumed"] for row in traces)
    link = c.local_link_manifest("K9")["rows"]
    assert {row["degree"] for row in link} == {0, 1, 2}
    assert link[-1]["ordered_classes"] == c.MIXED_CLASSES
    assert c.color_manifest()["rows"][-1]["generators"] == c.GENERATORS


def test_local_action_and_conditional_periodic_action():
    p = c.fixture_parameter_record("C182_FIXTURE_RETAINED_BOUNDARY_V1")
    action = c.apply_local_link(p, (1, 0, 0, 0, 0, 0, 0, 0), 2)
    assert len(action["action"]) == 8
    with pytest.raises(ValueError):
        c.apply_periodic_link(c.fixture_parameter_record("C182_FIXTURE_RETAINED_BOUNDARY_V1"), (1, 0, 0, 0, 0, 0, 0, 0))
    full = c.apply_periodic_link(c.fixture_parameter_record("C182_FIXTURE_NONTRIVIAL_HOLONOMY_V1"), (1, 0, 0, 0, 0, 0, 0, 0))
    assert full["state"] == "FULL_PERIODIC_LINK_EXPLICIT_AUTHENTICATED_HOLONOMY"


def test_interfaces_and_request_census():
    assert len(c.request_resolution_manifest()["rows"]) == 6
    assert c.request_resolution_manifest()["active_count"] == 2
    assert len(c.missing_link_object_manifest()["rows"]) == 2
    assert len(c.one_link_kernel_manifest()["rows"]) == 18
    assert len(c.two_link_kernel_manifest()["rows"]) == 18
    assert all(row["C181_boundary_owner"] == "C181_FIRST_OMITTED_BOUNDARY" for row in c.ghost_link_manifest("K9", "DIS_FUTURE", 2)["rows"])
    assert c.b0_release_manifest()["row"]["decision"] == "B0_LOCAL_TRANSVERSE_LINK_READY_HOLONOMY_INTERFACE_CONDITIONAL"


def test_focused_live_mutations_fail_closed():
    for i in range(384):
        mutation = c.mutate_live_hqcdb0reslink2(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
