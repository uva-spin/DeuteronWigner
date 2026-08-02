import json, math
from pathlib import Path
import pytest
from deuteron_wigner.process.p0.core import *

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"
ELIG = json.loads((D / "c22q_process_eligibility_matrix.json").read_text())["rows"]
RANKS = {row["operator_id"]: row["rank"] for row in json.loads((D / "c22_m3_multiq_capability_matrix.json").read_text())["rows"]}
ELIG = [{**row, "rank": RANKS[row["operator_id"]]} for row in ELIG]


def test_operational_and_scientific_gate_is_analytic_only():
    registry = EligibilityRegistry(ELIG)
    eligible = next(row["operator_id"] for row in ELIG if row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE")
    assert registry.require_analytic([eligible]) == (eligible,)
    with pytest.raises(ValueError, match="SOURCE_PROCESS_TIER.EMPTY"):
        registry.require_source([eligible])
    with pytest.raises(ValueError, match="PHYSICAL_PROCESS_TIER.EMPTY"):
        registry.require_physical([eligible])


def test_102_ineligible_fail_closed():
    registry = EligibilityRegistry(ELIG)
    rejected = [row["operator_id"] for row in ELIG if row["process_eligibility"] == "NOT_PROCESS_ELIGIBLE"]
    assert len(rejected) == 102
    with pytest.raises(ValueError, match="NOT_PROCESS_ELIGIBLE"):
        registry.require_analytic([rejected[0]])


def test_rank_compatibility_is_metadata_gated():
    rows=[{"operator_id":"x","process_eligibility":"ANALYTIC_PROCESS_ORACLE_ELIGIBLE","rank":2}]
    registry=EligibilityRegistry(rows)
    assert registry.require_analytic(["x"],2)==("x",)
    with pytest.raises(ValueError,match="RANK_MISMATCH"):
        registry.require_analytic(["x"],0)


def test_process_and_measurement_identity_are_immutable():
    process = ProcessId("DY", ("h1", "h2", "gamma*"), (1, -1), ("U", "LL"), "Q2")
    measurement = MeasurementRecord(("Q2", "y", "qT", "phi"), "COLLINS_SOPER", "LEPTON_PLANE", "SPIN1_IRREDUCIBLE", (("Q", 4, 6),))
    assert process.plan_tier == "ANALYTIC_PROCESS_ORACLE" and measurement.acceptance_status == "IDENTITY_ANALYTIC"
    with pytest.raises(Exception):
        process.family = "SIDIS"


def test_factorization_negative_control():
    cert = certificates()["COLORED_HADRO"]
    assert not cert.executable and cert.factorization_status == "BROKEN"
    hard = hard_library()[0]
    fo = fixed_order_library()[0]
    with pytest.raises(ValueError, match="FACTORIZATION_CERTIFICATE"):
        AnalyticWYOracle("bad", "DY", HarmonicId("F", "1", "U", 0, "EVEN", "EVEN"), 1, 1, hard, fo, cert, ("C19:OP:000",))


def test_dy_sidis_links_and_partners_are_distinct():
    basis = {row["process"]: row for row in process_basis()}
    assert basis["DY"]["link"] == "PAST"
    assert basis["SIDIS"]["link"] == "FUTURE"
    assert basis["SIDIS"]["partner"] == "ANALYTIC_TMD_FF"


def test_spin1_basis_has_23_and_todd_closed():
    rows = spin1_basis()
    assert len(rows) == 23
    assert all(row["analytic_status"] == "UNAVAILABLE" for row in rows if row["naive_t_parity"] == "ODD")


def test_rank_resolved_wy_oracles():
    report = wy_report(ELIG)
    assert report["rank_0_3_oracles_implemented"]
    assert report["executed_ranks"] == [0, 2]
    assert report["maximum_residual"] < 0.04
    assert all(row["small_q_finite"] for row in report["rows"])


def test_y_is_fo_minus_same_order_asymptotic():
    eligible = tuple(row["operator_id"] for row in ELIG if row["process_eligibility"] == "ANALYTIC_PROCESS_ORACLE_ELIGIBLE")
    oracle = make_oracle("DY", 0, eligible[:2], EligibilityRegistry(ELIG))
    pieces = oracle.pieces(0.4, 5.0)
    assert abs(float(pieces["Y"]) - (float(pieces["fixed_order"]) - float(pieces["asymptotic"]))) < 1e-15
    assert pieces["status"] == "VALIDATION_ONLY"


def test_inclusive_b1_tagged_and_matched_total_unavailable():
    basis = {row["process"]: row for row in process_basis()}
    assert basis["INCLUSIVE_B1"]["status"] == "OPERATOR_SPECIFIC_UNAVAILABLE"
    assert basis["TAGGED_DIS"]["status"] == "OPERATOR_SPECIFIC_UNAVAILABLE"
    assert basis["TAGGED_DIS"]["nuclear"] == "MATCHED_TOTAL_UNAVAILABLE"


def test_hard_partner_fixed_order_are_synthetic():
    assert all(not x.physical for x in hard_library())
    assert all(not x.physical and x.covariance_status == "SYNTHETIC_NONE" for x in partner_library())
    assert all(not x.physical for x in fixed_order_library())


def test_injection_count():
    rows = injections()
    assert len(rows) == 720 and len({row[0] for row in rows}) == 720
