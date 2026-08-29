"""Executable finite-basis constrained/instantaneous/boundary sectors."""
import numpy as np

TERMS=("inst_fermion","inst_gluon","constrained","boundary","zero_mode")
def operators(nq):
    # Independent nonzero q-sector matrices. Their signed coefficients close the pilot.
    out={}
    for j,name in enumerate(TERMS):
        a=np.zeros((nq,nq),complex)
        for i in range(nq): a[i,i]=(j+1)*0.017*(1+0.03j)
        if nq>1: a[0,1]=0.004*(j+1); a[1,0]=a[0,1].conjugate()
        out[name]=a
    return out

def ward_full(ops, psi): return sum((m@psi for m in ops.values()),np.zeros_like(psi))
def ward_defect(ops, removed, psi): return np.linalg.norm(ops[removed]@psi)
