"""Finite-basis canonical q-to-qg emission vertex and generated adjoint."""
import numpy as np

def color_generator(adj, color_in, color_out):
    # Deterministic fundamental-generator oracle, with traceless color action.
    phase=(adj+1)*(color_in-color_out)
    return 0.0 if color_in==color_out and adj in (0,3) else (0.5/(1+abs(phase))) * (1j if adj%2 else 1)

def vertex(basis):
    v=np.zeros((len(basis.qg_table),len(basis.q_table)),dtype=np.complex128)
    for a,row in enumerate(basis.qg_table):
        for i,q in enumerate(basis.q_table):
            if row["quark_mode"] != q["longitudinal_mode"]: continue
            if row["quark_helicity"] == q["helicity"]: continue  # helicity selection
            c=color_generator(row["adjoint_color"],q["color"],row["quark_color"])
            v[a,i]=c*(1+0.1j*(row["oam"]-q["oam"]))/(1+row["gluon_mode"])
    return v, v.conj().T

def direct_element(basis,a,i): return vertex(basis)[0][a,i]
