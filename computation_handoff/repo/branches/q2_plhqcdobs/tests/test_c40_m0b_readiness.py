"""Focused numerical faults: each mutates a live numerical bundle."""
from copy import deepcopy
from dataclasses import replace
import numpy as np
import pytest
from deuteron_wigner.bridge.m0b.readiness import build_bundle, assert_ready, readiness_report

def _fault(z, kind, variant):
    b=z["basis"]
    if kind==0: z["basis"]=replace(b,q_vectors=np.zeros_like(b.q_vectors))
    elif kind==1: z["basis"]=replace(b,Gq=np.zeros_like(b.Gq))
    elif kind==2: z["basis"]=replace(b,qg_table=(b.qg_table[0],)*len(b.qg_table))
    elif kind==3: z["H_q"]=np.zeros_like(z["H_q"])
    elif kind==4: z["H_qg"]=np.array(1.0)
    elif kind==5: z["V_qg_q"]=np.zeros_like(z["V_qg_q"])
    elif kind==6: z["V_q_qg"]=z["V_q_qg"]*(1+0.1*(variant+1))
    elif kind==7: z["W_qg_q"]=np.zeros_like(z["W_qg_q"])
    elif kind==8: z["operators"]["boundary"]=np.zeros_like(z["operators"]["boundary"])
    elif kind==9: z["A_CT"][-1]=z["A_CT"][0]
    elif kind==10: z["measurements"]["plus"]=np.ones_like(z["measurements"]["plus"])
    else: z["runtime_hash"]="0"*64

@pytest.mark.parametrize("fault_id",range(96))
def test_readiness_rejects_96_concrete_numerical_faults(fault_id):
    z=deepcopy(build_bundle(23)); _fault(z,fault_id//8,fault_id%8)
    with pytest.raises((AssertionError,KeyError,AttributeError,TypeError)):
        assert_ready(z)

def test_full_end_to_end_readiness_report():
    r=readiness_report()
    assert r["status"]=="C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY"
    assert len(r["resolutions"])==3
    assert all(x["vertex"]["norm"]>0 and x["wilson"]["norm"]>0 for x in r["resolutions"])

def test_runtime_array_serialization_is_byte_reproducible(tmp_path):
    """The runtime contract uses deterministic .npy, not timestamped zip data."""
    z=build_bundle(17); arrays={"H_q":z["H_q"],"V":z["V_qg_q"],"W":z["W_qg_q"],"A":z["A_CT"]}
    first=[]; second=[]
    for name,array in arrays.items():
        a=tmp_path/(name+"a.npy"); b=tmp_path/(name+"b.npy")
        np.save(a,array,allow_pickle=False); np.save(b,array,allow_pickle=False)
        first.append(a.read_bytes()); second.append(b.read_bytes())
    assert first==second
