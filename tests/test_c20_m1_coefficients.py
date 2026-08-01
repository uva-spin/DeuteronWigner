from deuteron_wigner.matching.m1.core import *
from deuteron_wigner.matching.m1.injections import INJECTIONS
def test_coefficients():assert len(coefficients())==10 and all(x.status.startswith("AUDITED") for x in coefficients())
def test_distributions():assert distribution_report()["constant_plus_residual"]==0 and distribution_report()["endpoint_integrable"]
def test_external():assert not external_report()["bundles"][0]["physical"] and external_report()["ancestry_duplicates"]==0
def test_fit():assert fit_report()["conditions"]>fit_report()["parameters"] and fit_report()["holdouts"]>=3
def test_step():assert step_report()["cocycle_residual"]<1e-12 and len(step_report()["defects"])==7
def test_scheme_ope():assert scheme_report_m1()["full_block_roundtrip_residual"]<1e-12 and ope_report_m1()["unavailable_entries"]==48
def test_holdouts_uncertainty():assert len(holdout_report()["classes"])==7 and len(uncertainty_report())==12
def test_readiness_injections():assert not readiness_report_m1()["production_reachable"] and len(INJECTIONS)==560 and len({x[0] for x in INJECTIONS})==560
