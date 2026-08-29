import numpy as np
from deuteron_wigner.bridge.m0b.readiness import build_bundle
from deuteron_wigner.bridge.m0b.distributions import direct_action
from deuteron_wigner.bridge.m0b.refinement import maps

def test_distribution_actions_and_refinement_maps():
    z=build_bundle(23); m=z["measurements"]; f=np.arange(1,7,dtype=float)
    assert np.all((m["x"]>0)&(m["x"]<=1))
    assert abs(m["plus"]@np.ones(6))<1e-12 and abs(m["logplus"]@np.ones(6))<1e-12
    assert abs((m["regular"]@f)[0]-direct_action(m["regular"][0],f))<1e-12
    assert m["delta"][0,-1]==1 and np.linalg.matrix_rank(m["mellin"])==3
    assert np.isfinite(m["convolution"]@f).all()
    p,r=maps(4,6); pg,rg=maps(8,12)
    assert np.linalg.norm(r@p-np.eye(4))<1e-12
    assert np.linalg.norm(rg@pg-np.eye(8))<1e-12
