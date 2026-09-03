import pytest
from deuteron_wigner.bridge.ifkernel2 import core

def test_c80_factorized_kernel_closes_without_matrix():
    core.materialize(); result=core.validate_package(); package=core.ContactKernelPackage()
    assert result['pass'] and result['focused_live_mutations'] >= 320
    assert package.input_freeze()['status']=='C80_INPUTS_FROZEN_COMPLETE'
    for coordinate in core.pilot_coordinates():
        value=package.evaluate(coordinate)
        assert value['status'] in ('EVALUATED_CERTIFIED','EVALUATED_EXACT_ZERO')
        assert value['normalization']['L']=='EXACTLY_CANCELLED'
        assert value['spin']['route_residual'] < 1e-11
        assert value['color']['route_residual'] < 1e-13

def test_c80_refuses_noncoordinate_and_unsafe_contracts():
    with pytest.raises(TypeError): core.evaluate_bare_contact_kernel('C53')
    c=core.pilot_coordinates()[0]
    with pytest.raises(ValueError): core.evaluate_bare_contact_kernel(core.ContactKernelCoordinate(**{**core.asdict(c),'zero_mode_policy':'EPSILON'}))
