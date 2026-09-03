"""Explicit nested-coordinate prolongation/restriction maps."""
import numpy as np

def maps(ncoarse,nfine):
    p=np.zeros((nfine,ncoarse),complex); p[:ncoarse,:]=np.eye(ncoarse)
    r=p.conj().T
    return p,r
