"""Assembled and independently evaluated free light-front Hamiltonians."""
import numpy as np

def _matrix(mass2):
    n=len(mass2); h=np.diag(np.asarray(mass2,dtype=np.complex128))
    for i in range(n-1):
        c=0.013*(i+1)
        h[i,i+1]=c*(1+0.2j); h[i+1,i]=c*(1-0.2j)
    return h

def hamiltonians(basis): return _matrix(basis.q_mass2), _matrix(basis.qg_mass2)

def matrix_free(mass2, vector):
    """Independent stencil action, not an ``H @ vector`` alias."""
    x=np.asarray(vector,dtype=np.complex128); out=np.asarray(mass2,dtype=np.complex128)*x
    for i in range(len(x)-1):
        c=0.013*(i+1); out[i]+=c*(1+0.2j)*x[i+1]; out[i+1]+=c*(1-0.2j)*x[i]
    return out
