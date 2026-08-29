"""C41 Branch-B gate: live numerical C40 changes cannot open physics eligibility."""
from copy import deepcopy
import numpy as np
import pytest
from deuteron_wigner.bridge.m0b.readiness import build_bundle, assert_ready
from deuteron_wigner.bridge.r2b.audit import audit_c40_substrate, assert_c40_not_eligible, STATUS

def _target(bundle, family):
    if family==0: return bundle["H_q"]
    if family==1: return bundle["H_qg"]
    if family==2: return bundle["V_qg_q"]
    if family==3: return bundle["W_qg_q"]
    if family==4: return bundle["operators"]["constrained"]
    if family==5: return bundle["counterterms"]["bilocal"]
    if family==6: return bundle["measurements"]["plus"]
    return bundle["basis"].Gq

@pytest.mark.parametrize("fault_id",range(128))
def test_128_live_array_mutations_are_rejected(fault_id):
    bundle=deepcopy(build_bundle(23)); a=_target(bundle,fault_id//16)
    before=a.copy(); delta=(fault_id+1)*0.01*(1j if np.iscomplexobj(a) else 1.0)
    a.flat[fault_id % a.size] += delta
    assert not np.array_equal(a,before)
    with pytest.raises((AssertionError,AttributeError,KeyError,TypeError)):
        assert_ready(bundle)

def test_fidelity_audit_fails_closed_before_any_diagram():
    audit=assert_c40_not_eligible()
    assert audit["status"]==STATUS
    assert len(audit["records"])==16
    assert all(x["status"]=="EXECUTABLE_TOY_NOT_PHYSICS_IDENTICAL" for x in audit["records"])
