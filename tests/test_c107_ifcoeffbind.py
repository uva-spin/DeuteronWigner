from deuteron_wigner.bridge.ifcoeffbind import (
    STATUS, load_verified_coefficient_binding_authority,
    verify_coefficient_binding_authority, evaluate_projected_coefficient,
    evaluate_coefficient_bound, evaluated_canonical_record, evaluated_coefficient_page,
)
from deuteron_wigner.bridge.ifpersist4.core import programs

def _pair():
    p = next(iter(programs().values()))
    return p["pair"]["id"], p["pair"]["resolution"], int(p["program"]["cardinality"])

def test_c107_authority_and_nonnull_value_bound():
    authority = load_verified_coefficient_binding_authority()
    assert authority["status"] == STATUS
    out = verify_coefficient_binding_authority()
    assert out["pass"] is True
    pair, resolution, cardinality = _pair()
    value = evaluate_projected_coefficient(pair, resolution, 0)
    bound = evaluate_coefficient_bound(pair, resolution, 0)
    assert len(value["value"]) == 2 and value["bound"] >= 0
    assert bound["bound"] == value["bound"]
    assert evaluated_canonical_record(pair, resolution, 0)["projected_coefficient"]["value"] == value["value"]
    assert cardinality > 0

def test_c107_last_ordinal_and_mutations():
    pair, resolution, cardinality = _pair()
    last = evaluate_projected_coefficient(pair, resolution, cardinality - 1)
    assert last["record_id"]
    # Focused live input mutations: malformed pair/ordinal and binding IDs
    # must fail closed; no mutation is converted to a coefficient value.
    failures = 0
    for i in range(384):
        try:
            if i % 3 == 0:
                evaluate_projected_coefficient(pair + ":MUTATED", resolution, 0)
            elif i % 3 == 1:
                evaluate_projected_coefficient(pair, resolution, cardinality + i + 1)
            else:
                evaluate_projected_coefficient(pair, "MUTATED", 0)
        except (KeyError, IndexError, ValueError):
            failures += 1
    assert failures == 384

def test_c107_pagination_is_bounded_and_cursor_bound():
    pair, resolution, cardinality = _pair()
    page = evaluated_coefficient_page(pair, resolution, limit=2)
    assert page["start"] == 0 and page["stop"] == 2 and page["next_cursor"]
    page2 = evaluated_coefficient_page(pair, resolution, limit=2, cursor=page["next_cursor"])
    assert page2["start"] == 2 and page2["stop"] == 4
    try:
        evaluated_coefficient_page(pair, resolution, limit=3, cursor=page["next_cursor"])
    except ValueError:
        pass
    else:
        raise AssertionError("cursor page-size mutation was accepted")
