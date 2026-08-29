from deuteron_wigner.bridge import hqcdrimassconstraintkernel1 as c
def test_source():assert "not performed" in c.source_freeze()["mass"]
def test_currents():assert c.current_basis()["count"]==6
def test_resolvents():assert c.resolvent_kernel()["count"]==6 and c.resolvent_kernel()["conjugate_paired"]
def test_cartan():assert c.cartan_kernel()["F8_weights"]["2J1"]=="0"
def test_mass():assert c.mass_input()["value"]=="UNAVAILABLE_NOT_ZERO"
def test_kcov():assert c.resolution_adapter()["count"]==3 and not c.covariance_contract()["off_diagonal_zero"]
def test_frontier():assert c.residual_frontier()["next"]=="C299/HQCDRIMASSCONSTRAINTINPUT1"
def test_reload():assert c.load_verified_hqcdrimassconstraintkernel1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassconstraintkernel1(i)["pass"] for i in range(384))
