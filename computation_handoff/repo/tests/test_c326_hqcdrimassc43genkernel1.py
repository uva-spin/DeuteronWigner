import pytest
from deuteron_wigner.bridge import hqcdrimassc43genkernel1 as c
def test_parity():assert c.parity()["legacy_all"] and c.parity()["theta_zero"]
def test_axes():assert "bHO" in c.kernel_contract()["independent"]
def test_zero_fail():
 with pytest.raises(ValueError):c.spectral_delta_general(9,8,.4,c.BOUNDARY,"DYNAMICAL",.1,0.,2.,8,"boson")
def test_frontier():assert c.residual_frontier()["next"]=="C327/HQCDRIMASSC43SEQEVAL1"
def test_reload():assert not c.load_verified_hqcdrimassc43genkernel1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43genkernel1(i)["pass"] for i in range(384))
