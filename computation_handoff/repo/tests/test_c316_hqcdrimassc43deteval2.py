import pytest
from deuteron_wigner.bridge import hqcdrimassc43deteval2 as c
def test_schema():assert not c.parameter_schema()["defaults"] and c.parameter_schema()["signed_mass_separate"]
def test_zero():assert c.spectral_delta("K9",0.,0.,1.,8,"boson")==0.
def test_real():assert isinstance(c.spectral_delta("K11",.2,.01,2.,8,"fermion"),float)
def test_bad():
 with pytest.raises(ValueError):c.spectral_delta("K9",.1,-1.,1.)
def test_owners():assert set(c.component_contract()["owners"])=={"boson","fermion","constraint","P0","vacuum"}
def test_tail():assert not c.tail_subtraction()["exact_tail_guessed"]
def test_K():assert len(c.K_adapters()["rows"])==3 and not c.K_adapters()["K_averaged"]
def test_routes():assert c.route_parity()["zero_theta"]
def test_frontier():assert c.residual_frontier()["next"]=="C317/HQCDRIMASSC43PARAM1"
def test_reload():assert c.load_verified_hqcdrimassc43deteval2_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassc43deteval2(i)["pass"] for i in range(384))
