import numpy as np
from deuteron_wigner.bridge.m0b import RESOLUTIONS, build_basis
from deuteron_wigner.bridge.m0b.basis import order_hash

def test_three_normalized_explicit_coordinate_bases():
    dimensions=[]
    for K,nq,nqg in RESOLUTIONS:
        b=build_basis(K); dimensions.append((len(b.q_table),len(b.qg_table)))
        assert b.q_vectors.shape==(nq,nq) and b.qg_vectors.shape==(nqg,nqg)
        assert np.linalg.norm(b.Gq-np.eye(nq))<1e-12
        assert np.linalg.norm(b.Gqg-np.eye(nqg))<1e-12
        assert np.linalg.eigvalsh(b.Gq).min()>0
        assert all(r["longitudinal_mode"]>0 and r["ir_mass"]>0 for r in b.q_table)
        assert all(r["quark_mode"]+r["gluon_mode"]==K and not r["zero_mode"] for r in b.qg_table)
        assert len(order_hash(b.q_table))==64 and len(order_hash(b.qg_table))==64
    assert len(set(dimensions))==3
