from deuteron_wigner.bridge import hqcdrimassv0tailrenorm1 as c
def test_scan():assert c.extended_scan()["count"]==7
def test_tail():assert c.tail_formula()["log2_coefficient"]==9 and c.tail_formula()["log_coefficient"]==-24
def test_model():assert c.tail_formula()["alternatives"]["log2_rms"]<.002
def test_remainder():assert c.remainder_scan()["enclosure"][0]<-109.09<c.remainder_scan()["enclosure"][1]
def test_interval():assert c.finite_remainder()["half_width"]==.04
def test_nonclaim():assert c.finite_remainder()["reduced_model_only"]
def test_frontier():assert c.residual_frontier()["next"]=="C309/HQCDRIMASSV0GRAMEVAL1"
def test_reload():assert c.load_verified_hqcdrimassv0tailrenorm1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0tailrenorm1(i)["pass"] for i in range(384))
