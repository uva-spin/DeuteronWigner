"""Numerical counterterm operator basis and nonphysical system machinery."""
import numpy as np

NAMES=("mass","field","vertex","inst_fermion","inst_gluon","bilocal","wilson","endpoint","transverse","basis")
def counterterms(nq):
    mats={}
    for k,name in enumerate(NAMES):
        m=np.zeros((nq,nq),complex); m[np.arange(nq),np.arange(nq)]=(k+1)*0.01
        if nq>1: m[k%nq,(k+1)%nq]=0.002j*(k+1)
        mats[name]=m
    # Conditions are deterministic traces/transition probes, never a physical bare residual.
    a=np.eye(len(NAMES))*1.5
    for i in range(len(NAMES)-1): a[i,i+1]=a[i+1,i]=0.08
    rhs=np.linspace(0.1,1.0,len(NAMES)); coeff=np.linalg.solve(a,rhs)
    return mats,a,rhs,coeff
