import pytest

from deuteron_wigner.bridge.icaxis import *


def test_c123_source_axis_authority_and_dimensions():
    out = verify_current_axis_authority()
    assert out["status"] == STATUS
    assert out["physical_state_dimensions_ok"]
    assert out["logical_witnesses"] == 0
    assert out["matrix_targets"] == 0
    assert out["positive_gate"] is False
    assert out["route_identity_mismatches"] == 0
    assert out["route_cardinality_mismatches"] == 0

    assert axis_cardinality("physical_bra_state", {"resolution": RESOLUTIONS[0], "sector": "q"}) == 6
    assert axis_cardinality("physical_bra_state", {"resolution": RESOLUTIONS[0], "sector": "qg"}) == 1344
    assert axis_cardinality("physical_bra_state", {"resolution": RESOLUTIONS[1], "sector": "qg"}) == 2700
    assert axis_cardinality("physical_bra_state", {"resolution": RESOLUTIONS[2], "sector": "qg"}) == 4752


def test_c123_rank_page_and_immutable_adapters():
    rec = physical_state_axis(RESOLUTIONS[0], "qg")
    first = axis_member_by_rank("physical_bra_state", {"resolution": RESOLUTIONS[0], "sector": "qg"}, 0)
    assert axis_member_rank("physical_bra_state", {"resolution": RESOLUTIONS[0], "sector": "qg"}, first["member_id"]) == 0
    page = axis_member_page(axis_id="physical_bra_state", conditioning_key={"resolution": RESOLUTIONS[0], "sector": "qg"}, limit=7)
    assert len(page["records"]) == 7
    assert page["next_cursor"] is not None
    page2 = axis_member_page(axis_id="physical_bra_state", conditioning_key={"resolution": RESOLUTIONS[0], "sector": "qg"}, cursor=page["next_cursor"], limit=7)
    assert page2["first_rank"] == 7
    with pytest.raises(ValueError):
        axis_member_page(axis_id="physical_bra_state", conditioning_key={"resolution": RESOLUTIONS[0], "sector": "qg"}, cursor=page["next_cursor"][:-2] + "xx", limit=7)

    factors = current_factor_operand_axis(PROGRAMS[0])
    assert factors["member_count"] > 0
    assert factors["values"] == 0 and factors["bounds"] == 0
    assert static_isolation_guard()["pass"]


def test_c123_internal_mode_blocker_is_explicit():
    for axis in ("longitudinal_transfer", "external_modes"):
        d = axis_domain_manifest(axis, RESOLUTIONS[0])
        assert d["route_class"] == "AMBIGUOUS_BLOCKING"
        assert d["member_count"] == 0
        assert empty_axis_domain_certificate(axis, RESOLUTIONS[0])["exact"]
    p = projector_reproduction_certificate("I2_density_projector", RESOLUTIONS[0])
    assert p["status"] == "BLOCKED_BY_UNPUBLISHED_C117_INTERNAL_MODE_MEMBERS"


def test_c123_no_value_or_witness_construction_and_mutation_suite():
    authority = load_verified_current_axis_authority()
    assert authority["status"] == STATUS
    assert authority["witness_values"] == 0
    assert authority["component_sums"] == 0
    assert authority["sparse_entries"] == 0
    assert sum(mutate_live_icaxis(i) != authority for i in range(384)) == 384
