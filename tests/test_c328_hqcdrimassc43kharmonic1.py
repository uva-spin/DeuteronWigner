import pytest
from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as c
def test_domains():assert c.domain_certificate()["fermion_counts"]==(5,6,7) and c.domain_certificate()["boson_counts"]==(4,5,6)
def test_k_nontrivial():assert c.spectral_delta_finite(9,8,.4,c.BOUNDARY,c.ZERO,.2,.01,2.,"fermion")!=c.spectral_delta_finite(11,8,.4,c.BOUNDARY,c.ZERO,.2,.01,2.,"fermion")
def test_parity():assert c.route_parity()["counts_equal"] and c.route_parity()["theta_zero"]
def test_zero_fail():
 with pytest.raises(ValueError):c.spectral_delta_finite(9,8,.4,c.BOUNDARY,"DYNAMICAL",.2,0.,2.,"boson")
def test_reload():assert not c.load_verified_hqcdrimassc43kharmonic1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43kharmonic1(i)["pass"] for i in range(384))
