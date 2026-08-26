from deuteron_wigner.bridge import hqcdstctsolve1 as c
import pytest
def _p():return {"record_id":"test","system_id":"C206-SYS-K9-GENERIC","resolution":"K9","scheme":"PROJECT_FINITE_BASIS_ST","holonomy_class":"GENERIC","coordinate_form":"IDENTIFIED_PLUS_NULL_SYMBOLIC","counterterm_order":c.CT,"null_order":c.NULL,"free_parameter_order":c.FREE_PARAMETERS,"branch":"symbolic","enclosure":"EXACT","no_defaults":True,"physical":False}
def test_authority_frontier():
 assert c.verify_hqcd_stctsolve1_authority()["C205_package_root"]==c.C205_ROOT
 assert c.frontier_manifest("C197-ST-8")["rows"][0]["aliases"]==("ST-compatible counterterm solution","ST_COMPATIBLE_COUNTERTERM_SOLUTION")
def test_system_and_parameters():
 s=c.system_freeze_manifest();assert s["count"]==12
 assert c.validate_solve_parameter_record(_p())["valid"]
 bad=dict(_p());bad["free_parameter_order"]=()
 with pytest.raises(ValueError):c.validate_solve_parameter_record(bad)
def test_exact_family():
 assert c.compatibility_manifest()["compatible"]
 assert c.right_null_basis_manifest()["dimension"]==14
 assert c.left_null_basis_manifest()["dimension"]==6
 fam=c.affine_solution_family_manifest()["rows"][0]["family_id"]
 vals={k:f"symbol-{k}" for k in c.FREE_PARAMETERS}
 assert c.evaluate_affine_solution_family(_p(),fam,vals)["residual"]=="EXACT_ZERO"
def test_replacement_release():
 assert c.st_replacement_manifest()["unrelated_rows_changed"]==0
 assert c.stctsolve1_release_manifest()["gates"]["representative_selected"] is False
 assert c.next_st_handoff_contract()["next_object"]=="C197-ST-9"
def test_isolation_mutations():
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdstctsolve1(i)["pass"] for i in range(384))
 assert c.stctsolve1_completeness_certificate()["family_dimension"]==14
