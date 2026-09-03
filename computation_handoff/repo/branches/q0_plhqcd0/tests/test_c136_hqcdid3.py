from deuteron_wigner.bridge.hqcdid3 import core as c
import pytest

def test_authority_and_registry():
    r=c.load_verified_hqcd_identifiability_authority()
    assert r["positive_gate"] and r["selected_plan"]=="ID3-B"
    assert r["directions"]==11 and r["generic_rank"]==2 and r["rank_deficit"]==9
    assert c.unknown_direction_manifest()["unclassified"]==0
    assert len(c.counterterm_primitive_manifest()["blocks"])==6

def test_conditions_and_rank():
    assert c.condition_manifest()["count"]==12
    assert c.condition_selector_manifest()["count"]==12
    with pytest.raises(ValueError): c.evaluate_condition("C136_MASS_K9",c.RESOLUTIONS[0])
    x=c.evaluate_condition("C136_MASS_K9",c.RESOLUTIONS[0],external_input_capsule={"scheme_id":"PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1","no_default":True})
    assert x["route_mismatch"]==0
    assert c.jacobian_report()["route_J3_A_J3_B_mismatches"]==0
    assert c.rank_completion_report()["reduced_solve_authorized"]

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert c.nullspace_manifest()["represented_as_zero"] is False
    for i in range(384): assert not c.mutate_live_hqcdid3(i)["positive_gate"]
