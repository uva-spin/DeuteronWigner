import pytest
from deuteron_wigner.bridge.hqcdinput4 import core as c

def test_fail_closed_and_manifest():
    r = c.load_verified_hqcd_input4_authority()
    assert r["status"] == c.STATUS and not r["positive_gate"]
    assert r["selected_plan"] == "INPUT4-D" and r["capsules_present"] == 0
    assert c.required_capsule_manifest()["count"] == 2
    assert c.missing_capsule_manifest()["count"] == 2

def test_numerical_apis_and_templates_reject():
    with pytest.raises(ValueError): c.identified_coordinate_evaluation()
    with pytest.raises(ValueError): c.validate_capsule({"template_marker": True})
    assert c.coordinate_operator_binding_manifest()["binding_mismatches"] == 0
    assert c.nullspace_manifest()["coordinates_assigned"] == 0
    assert c.unique_full_operator_no_go_certificate()["unique_matrix"] is False

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    for i in range(384): assert not c.mutate_live_hqcdinput4(i)["positive_gate"]
