import pytest
from deuteron_wigner.bridge.icnorm3 import *

def test_factor_authority():
    out=verify_factor_authority()
    assert out["status"] == STATUS and out["program_count"] == 8
    assert out["unknown_programs"] == out["unknown_ast_operations"] == out["unknown_operands"] == 0
    assert out["required_domain"]["missing"] == 0
    assert out["positive_gate"]
    assert all(x["residual"] == 0 for x in out["route_evaluations"])

def test_factor_records_and_pagination():
    rows=current_factor_leaf_inventory()
    assert len(rows) == 36
    assert factor_page(limit=7)["records"]
    rec=current_factor_record(rows[0]["leaf_id"])
    assert rec["routes"][0]["value"] is not None
    assert rec["routes"][0]["bound"]["radius"] == 0

def test_isolation_and_mutations():
    base=verify_factor_authority()
    assert static_isolation_guard()["pass"]
    assert sum(mutate_live_icnorm3(i) != base for i in range(384)) == 384
