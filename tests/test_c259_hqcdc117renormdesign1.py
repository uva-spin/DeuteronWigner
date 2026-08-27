from deuteron_wigner.bridge import hqcdc117renormdesign1 as c
def test_basis_closed(): assert c.operator_basis()["dimension"]==4 and c.operator_basis()["closed_at_declared_scope"]
def test_primary_corpus(): assert c.literature_corpus()["count"]==12 and c.literature_corpus()["all_primary"]
def test_rank_and_conditioning():
 for r in c.response_diagnostics()["finite_basis"]: assert r["rank"]==4 and r["condition_number"]==1 and not r["left_nullspace"] and not r["right_nullspace"]
def test_selection_and_matching(): assert c.candidate_schemes()["selection"]=="PROJECT_C117_RI_SMOM_V1" and "MSbar" in c.candidate_schemes()["rows"][0]["conversion"]
def test_scope_and_loading(): assert c.static_isolation_guard()["pass"] and not c.adapter_plan()["coefficients_evaluated"] and c.load_verified_hqcdc117renormdesign1_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117renormdesign1(i)["pass"] for i in range(384))
