import json
from pathlib import Path

from deuteron_wigner.matching.m3q.core import *

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"


def test_evaluator_returns_every_failure():
    result = evaluate_qualification("x", {})
    assert len(result.failed_validation_gates) == len(VALIDATION_GATES)
    assert len(result.failed_source_gates) == len(SOURCE_GATES)
    assert len(result.failed_physical_gates) == len(PHYSICAL_GATES)


def test_validation_does_not_launder_source_or_physical():
    gates = {name: True for name in VALIDATION_GATES}
    result = evaluate_qualification("x", gates)
    assert result.qualification_tier == "M3_VALIDATION_QUALIFIED"
    assert result.process_eligibility == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE"
    assert not result.source_qualified and not result.physical_input_qualified


def test_reconciliation_counts():
    source = json.loads((D / "c22_m3_multiq_capability_matrix.json").read_text())["rows"]
    rows = reconcile_rows(source)
    assert len(rows) == 540
    assert tier_counts(rows, "m3_qualification_tier") == {"M3_UNAVAILABLE": 102, "M3_VALIDATION_QUALIFIED": 438}
    assert tier_counts(rows, "process_eligibility_tier") == {"ANALYTIC_PROCESS_ORACLE_ELIGIBLE": 438, "NOT_PROCESS_ELIGIBLE": 102}


def test_evolution_only_and_matching_unavailable_never_process_eligible():
    source = json.loads((D / "c22_m3_multiq_capability_matrix.json").read_text())["rows"]
    rows = reconcile_rows(source)
    assert all(row["process_eligibility_tier"] == "NOT_PROCESS_ELIGIBLE" for row in rows if not row["c20_reference_matching"] or not row["c21_m2_tmd_evolution"])


def test_minimal_families_are_tiered():
    rows = minimal_family_audit()
    assert len(rows) == 8
    assert sum(row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE" for row in rows) == 6
    assert all(row["source_qualification"] == "NOT_QUALIFIED" for row in rows)


def test_cs_largeb_physical_remains_blocked():
    report = cs_largeb_manifest()
    assert not report["validation"]["physical"]
    assert report["physical_input"]["status"] == "NOT_QUALIFIED"


def test_nuclear_components_are_separate():
    rows = nuclear_qualification()
    assert len(rows) == 8
    assert sum(row["validation_tier"] == "M3_VALIDATION_QUALIFIED" for row in rows) == 1
    assert next(row for row in rows if row["block"] == "MATCHED_TOTAL")["validation_tier"] == "OPERATOR_SPECIFIC_UNAVAILABLE"


def test_injection_count_and_ids():
    rows = injections()
    assert len(rows) == 160 and len({row[0] for row in rows}) == 160
