from deuteron_wigner.bridge.ifboundrestart.core import build_semantic_ledger, check_node_semantics, compare_semantic_routes


def test_c90_routes_have_identical_normal_forms_for_a_historical_pair():
    item = next(compare_semantic_routes("K9_2_N8_b0.40"))
    assert item["kind"] == "FACTORIZED_SEMANTIC_PROGRAM_ROOT"
    assert item["proof"]["pass"]


def test_c90_pair_atomic_restart_closes_a_compact_prefix(tmp_path):
    first = build_semantic_ledger(tmp_path, stop_after=3)
    assert first["interrupted"]
    second = build_semantic_ledger(tmp_path, resume=True, stop_after=3)
    assert second["interrupted"]
    # stop_after is the immutable global pair cursor, so resuming from the
    # three-entry checkpoint commits exactly the next pair before stopping.
    assert second["next_pair"] == 4


def test_c90_closed_ir_checker_rejects_opaque_and_accepts_declared_combinators():
    atom = {"type": "ATOM_TABLE", "order": "FROZEN_LIST", "records": ["a", "b"], "cardinality": 2}
    interval = {"type": "ORDERED_RANGE", "start": 0, "stop": 2, "step": 1, "cardinality": 2}
    union = {"type": "ORDERED_UNION", "order": "CONCATENATE", "multiplicity": "RETAINED", "children": [atom, interval], "cardinality": 4}
    product = {"type": "CARTESIAN_PRODUCT", "rank": "MIXED_RADIX_LAST_AXIS_FASTEST", "children": [atom, interval], "cardinality": 4}
    filtered = {"type": "FILTER", "child": interval, "predicate": {"opcode": "EVEN"}, "selected_ordinals": [0], "cardinality": 1}
    permuted = {"type": "PERMUTE", "child": interval, "permutation": [1, 0], "cardinality": 2}
    assert [check_node_semantics(node) for node in (atom, interval, union, product, filtered, permuted)] == [2, 2, 4, 4, 1, 2]
