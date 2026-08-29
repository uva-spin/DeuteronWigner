from deuteron_wigner.bridge import hqcdriquarkfixedkv1 as c
def test_domain():assert c.canonical_domain_schema()["coupling_degree"]==1
def test_normalization():assert c.normalization_manifest()["L_cancellation"].startswith("exact")
def test_audit():assert not c.primitive_audit()["C52_symbolic_full_primitive"] and c.primitive_audit()["omitted_symbolic_primitive"]=="UNAVAILABLE_NOT_ZERO"
def test_program_handoff():assert not c.operator_program()["executable"] and c.next_handoff_contract()["next"]=="C225/HQCDRIQUARKFIXEDKVPRIM1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkv1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkv1(i)["pass"] for i in range(384))
