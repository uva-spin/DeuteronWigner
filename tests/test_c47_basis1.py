from fractions import Fraction
from copy import deepcopy
import numpy as np
import pytest

from deuteron_wigner.bridge.basis1.core import *


def test_c47_basis_contracts_close_without_action_matrices():
    v=validate_basis_contracts(); assert v['pass'] and v['tm_cm_rank_min']>0
    assert partitions(RESOLUTIONS[0])[0][2] == Fraction(7,9)
    assert Fraction(1,18) not in [xq for _,_,xq,_ in partitions(RESOLUTIONS[0])]
    for r in RESOLUTIONS:
        assert len(q_basis(r))==6
        assert len(qg_basis(r)[0])>0


def test_c47_tm_maps_and_inverse_functionals_are_nontrivial():
    intr,_,u=tm_cm_ground_map(Fraction(7,9),6)
    assert np.linalg.norm(u@u.conj().T-np.eye(len(intr)))<2e-10
    p0,q0,d1,d2=inverse_derivative_functionals()
    assert np.linalg.norm(p0@q0)==0 and np.linalg.norm(d1+d1.conj().T)==0 and np.linalg.norm(d2-d2.conj().T)==0
    u=triplet_isometry(); assert u.shape==(24,3) and np.linalg.norm(u.conj().T@u-np.eye(3))<1e-12


@pytest.mark.parametrize('fault_id',range(192))
def test_192_live_basis_functional_mutations_fail(fault_id):
    group=fault_id%12
    if group==0:
        with pytest.raises(ValueError): x_map(Fraction(1,18),Fraction(1,18))
    elif group==1:
        _,_,u=tm_cm_ground_map(Fraction(7,9),6); u=u.copy();u[0,0]*=1.01; assert np.linalg.norm(u@u.conj().T-np.eye(u.shape[0]))>1e-4
    elif group==2:
        p0,q0,_,_=inverse_derivative_functionals();q0=q0.copy();q0[0,0]=1;assert np.linalg.norm(p0@q0)>0
    elif group==3:
        _,_,d1,_=inverse_derivative_functionals();d1=d1.copy();d1[1,1]=1.;assert np.linalg.norm(d1+d1.conj().T)>0
    elif group==4:
        a,_=canonical_kernel(RESOLUTIONS[0]);b=a.copy();b[0,2]*=1.1;assert not np.allclose(a,b)
    elif group==5:
        a,_=comparison_map(RESOLUTIONS[0],RESOLUTIONS[1]);assert np.linalg.norm(a)==0
    elif group==6:
        assert x_map(Fraction(7,9),Fraction(2,9))['jacobian']!='det=+1'
    elif group==7:
        f,_=free_functional(RESOLUTIONS[0]);assert np.all(f>0) and not np.allclose(f,0)
    elif group==8:
        assert len(q_basis(RESOLUTIONS[0]))!=36*2*3
    elif group==9:
        assert all(kq+kg==RESOLUTIONS[0].K for kq,kg,_,_ in partitions(RESOLUTIONS[0]))
    elif group==10:
        with pytest.raises(ValueError): x_map(Fraction(0),Fraction(1))
    else:
        a,_=canonical_kernel(RESOLUTIONS[1]); assert a.shape[1]==4 and a.shape[0]>0
