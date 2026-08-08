"""First-order C36 spacelike Wilson insertion by finite mode quadrature."""
import numpy as np
from .vertices import color_generator

RAPIDITY = 0.73

def _segment(phase, scale, orientation=1):
    s=np.linspace(-1.0,1.0,129)
    return scale*np.trapz(np.exp(1j*orientation*phase*s),s)/2.0

def wilson(basis, orientation=1):
    shape=(len(basis.qg_table),len(basis.q_table)); long=np.zeros(shape,complex); endpoint=np.zeros(shape,complex); trans=np.zeros(shape,complex)
    for a,row in enumerate(basis.qg_table):
        for i,q in enumerate(basis.q_table):
            if row["quark_mode"] != q["longitudinal_mode"]: continue
            c=color_generator(row["adjoint_color"],q["color"],row["quark_color"])
            if c==0: continue
            phase=RAPIDITY*(row["gluon_mode"]+0.25*row["oam"])
            long[a,i]=_segment(phase,c/(1+row["gluon_mode"]),orientation)
            endpoint[a,i]=0.11j*c*np.exp(1j*orientation*phase)
            trans[a,i]=0.07*c*np.exp(1j*orientation*(q["oam"]-row["oam"]))
    return long, endpoint, trans, long+endpoint+trans

def direct_quadrature_element(basis,a,i): return wilson(basis)[3][a,i]
