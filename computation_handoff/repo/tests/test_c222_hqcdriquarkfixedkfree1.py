from deuteron_wigner.bridge import hqcdriquarkfixedkfree1 as c
def test_states():assert c.symbolic_state_schema()["cardinality"]=="UNBOUNDED"
def test_free_schema():
 x=c.free_operator_schema();assert x["count"]==2 and not x["operator_complete"]
def test_extension():
 x=c.retained_extension_audit();assert x["C128_free_bilinears_extend"] and not x["C128_retained_indices_reused"] and not x["C128_pperp2_matrix_extends"]
def test_denominator_handoff():assert not c.denominator_program()["executable"] and c.next_handoff_contract()["next"]=="C223/HQCDRIQUARKFIXEDKTRANS1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkfree1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkfree1(i)["pass"] for i in range(384))
