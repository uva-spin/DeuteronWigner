from deuteron_wigner.bridge.hqcdinput3 import core as c
import pytest

def test_fail_closed_input_boundary():
    r=c.load_verified_hqcd_input3_authority()
    assert not r["positive_gate"] and r["selected_plan"]=="INPUT3-C"
    assert r["required_capsules"]==2 and r["capsules_present"]==0
    assert c.input_request_manifest()["missing_count"]==2

def test_validation_and_binding():
    with pytest.raises(ValueError): c.evaluate_identified_inputs()
    with pytest.raises(ValueError): c.validate_capsule_set({})
    assert c.coordinate_operator_binding_manifest()["mismatches"]==0
    assert c.nullspace_preservation_manifest()["null_coordinates_set_to_zero"]==0

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    for i in range(384): assert not c.mutate_live_hqcdinput3(i)["positive_gate"]
