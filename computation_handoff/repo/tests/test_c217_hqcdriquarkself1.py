from deuteron_wigner.bridge import hqcdriquarkself1 as c


def test_domain_and_terms():
    assert c.domain_manifest()["count"]==3
    assert c.term_ledger()["retained_executable"]==5 and not c.term_ledger()["complete"]


def test_safe_programs():
    s=c.self_energy_program_schema();assert not s["eval"] and not s["pickle"] and not s["callbacks"]
    p=c.self_energy_program_manifest();assert p["retained_executable"]==3 and p["full_executable"]==0


def test_routes_hermiticity_and_residual():
    assert c.independent_route_certificate()["retained_agreement"]
    assert c.hermiticity_projector_certificate()["count"]==3
    assert c.residual_frontier()["omitted_interfaces"]==120


def test_release_handoff():
    assert c.release_manifest()["retained_self_energy_executable"] and not c.release_manifest()["full_self_energy_executable"]
    assert c.next_handoff_contract()["next"]=="C218/HQCDRIQUARKOMIT1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdriquarkself1(i)["pass"] for i in range(384))
