import pytest
from deuteron_wigner.bridge import hqcdrimassc43jmyevaldispatch1 as c
def test_dispatch():assert all(c.dispatch(x,{})["executable"] for x in ("integrate","integrate_cut","MSbar_UV_project","evaluate_ast"))
def test_unknown():
 with pytest.raises(ValueError):c.dispatch("unknown",{})
def test_groups():assert c.executable_groups()["count"]==16 and c.executable_groups()["dispatch_total"]
def test_boundaries():assert c.integration_rules()["MSbar_UV_project"]["operation"]=="negative UV pole part only"
def test_gate():assert c.closure()["dispatch_total"] and not c.closure()["Laurent_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyevaldispatch1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyevaldispatch1(i)["pass"] for i in range(384))
