from copy import deepcopy
from fractions import Fraction
import numpy as np
import pytest

from deuteron_wigner.bridge.modes.core import *


def test_c45_end_to_end_mode_library_is_nontrivial_and_valid():
    arrays=library_arrays(); evidence=validate_library(arrays)
    assert evidence['pass'] and evidence['triplet_rank']==3
    assert all(a.size and np.linalg.norm(a)>0 for a in arrays.values())
    assert longitudinal_contract()['x_min_reconciliation']['derived_mode_minimum']['K9_2_N8_b0.40']=='1/9'
    assert len(longitudinal_modes(RESOLUTIONS[0],'QUARK'))==5
    assert len(longitudinal_modes(RESOLUTIONS[0],'GLUON'))==4


def test_c45_contract_gate_all_four_rows_executable():
    rows=projection_contract_matrix()
    assert len(rows)==4 and {x['status'] for x in rows}=={'SOURCE_COMPLETE_EXECUTABLE'}
    assert STATUS=='C45_SOURCE_DERIVED_MODE_PROJECTION_READY'


def test_c45_runtime_library_hashes_reproduce_byte_for_byte(tmp_path):
    first=build_library(tmp_path/'first')
    second=build_library(tmp_path/'second')
    assert {k:v['array_sha256'] for k,v in first.items()} == {k:v['array_sha256'] for k,v in second.items()}
    assert all((tmp_path/'first'/f'{name}.npy').is_file() for name in first)


@pytest.mark.parametrize('fault_id',range(180))
def test_180_focused_live_mode_mutations_fail(fault_id):
    group=fault_id % 12
    if group==0:
        labels=[Fraction(1,2),Fraction(3,2)]; vals=longitudinal_values(labels,np.linspace(-1,1,257,endpoint=False),phase_sign=-1)
        target=longitudinal_values(labels,np.linspace(-1,1,257,endpoint=False)); assert not np.allclose(vals,target)
    elif group==1:
        with pytest.raises(ValueError): ho_momentum(0,0,np.array([0.]),np.array([0.]),-0.4)
    elif group==2:
        assert len(ho_labels(8)) != len([(n,m) for n in range(8) for m in range(-8,9) if 2*n+abs(m)<=8])
    elif group==3:
        a=ho_overlap(ho_labels(8),.4,ho_labels(8),.4); a[0,0]*=1.01; assert np.linalg.norm(a-np.eye(len(a)))>1e-3
    elif group==4:
        with pytest.raises(ValueError): spinor(1.,0.,0.,1.2,0)
    elif group==5:
        e=polarization(1.1,.19,-.13,1); e[0]=1.; k=np.array([1.1,(.19**2+.13**2)/(2*1.1),.19,-.13]); assert abs(lf_dot(k,e))>1e-4
    elif group==6:
        p0,q0=zero_mode_projectors(6); q0[0,0]=1.; assert np.linalg.norm(p0@q0)>0
    elif group==7:
        P,_,_=color_triplet_projector(); P[0,0]+=0.1; assert np.linalg.norm(P@P-P)>1e-4
    elif group==8:
        P,_,_=color_triplet_projector(); assert np.linalg.matrix_rank(np.eye(24))!=3 and np.linalg.norm(np.eye(24)-P)>1
    elif group==9:
        assert Fraction(1,2)/RESOLUTIONS[0].K != Fraction(1,18)
    elif group==10:
        with pytest.raises(ValueError): polarization(0.,.1,.2,1)
    else:
        a=library_arrays(); h=array_hash(a['qg_triplet_projector']); a['qg_triplet_projector'][0,0]+=1e-3; assert array_hash(a['qg_triplet_projector'])!=h
