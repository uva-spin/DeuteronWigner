import numpy as np
from deuteron_wigner.bridge.m0b.readiness import build_bundle
from deuteron_wigner.bridge.m0b.hamiltonian import matrix_free
from deuteron_wigner.bridge.m0b.vertices import direct_element
from deuteron_wigner.bridge.m0b.wilson import direct_quadrature_element, wilson
from deuteron_wigner.bridge.m0b.constrained import TERMS, ward_defect

def test_hamiltonian_vertex_wilson_and_ward_are_applied():
    z=build_bundle(23); b=z["basis"]; psi=np.arange(1,7)+1j*np.arange(6,0,-1)
    assert np.linalg.norm(z["H_q"]@psi-matrix_free(b.q_mass2,psi))<1e-12
    assert np.linalg.norm(z["H_q"]-z["H_q"].conj().T)<1e-12
    assert np.linalg.norm(z["V_q_qg"]-z["V_qg_q"].conj().T)<1e-12
    assert np.linalg.norm(z["V_qg_q"]@psi)>0
    assert np.linalg.norm(z["W_qg_q"]@psi)>0
    assert np.linalg.norm(z["W_qg_q"]-(z["W_longitudinal"]+z["W_endpoint"]+z["W_transverse"]))<1e-12
    a,i=np.argwhere(abs(z["W_qg_q"])>0)[0]
    assert abs(z["W_qg_q"][a,i]-direct_quadrature_element(b,int(a),int(i)))<1e-14
    assert abs(z["V_qg_q"][a,i]-direct_element(b,int(a),int(i)))<1e-14
    for term in TERMS: assert ward_defect(z["operators"],term,psi)>0
    # Orientation changes the actual finite-path integral, unlike a metadata flag.
    assert np.linalg.norm(wilson(b,orientation=1)[3]-wilson(b,orientation=-1)[3])>0

def test_counterterm_system_is_numerical_not_physical_claim():
    z=build_bundle(17)
    assert z["A_CT"].shape==(10,10) and np.linalg.matrix_rank(z["A_CT"])==10
    assert np.linalg.norm(z["A_CT"]@z["synthetic_coeff"]-z["synthetic_rhs"])<1e-12
    assert all(np.linalg.norm(x)>0 for x in z["counterterms"].values())
