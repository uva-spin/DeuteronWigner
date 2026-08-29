from deuteron_wigner.bridge.hqcdrenred import core as c
import pytest

def test_authority_and_adapters():
    r=c.load_verified_reduced_renormalization_authority()
    assert r["positive_gate"] and r["selected_plan"]=="RRED-A"
    assert r["identified_dimension"]==2 and r["nullspace_dimension"]==9
    assert c.coordinate_adapter_validation()["direct_sum"]
    assert c.original_direction_crosswalk()["count"]==11

def test_symbolic_map_and_no_defaults():
    x=c.solve_identified_coordinates()
    assert x["numeric"] is False
    with pytest.raises(ValueError): c.solve_identified_coordinates(external_input_capsules={})
    assert c.restricted_jacobian_report()["determinant"]==1
    assert c.conditional_solution_manifest()["count"]==1
    assert c.reduced_solve_completeness_certificate()["reduced_maximal_subspace_solve"]

def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert c.nullspace_manifest()["represented_as_zero"] is False
    for i in range(384): assert not c.mutate_live_hqcdrenred(i)["positive_gate"]
