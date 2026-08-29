import numpy as np
from deuteron_wigner.bridge.ifcontact7 import *
from deuteron_wigner.bridge.ifpersist4.core import programs

def test_c111_authority_and_shapes():
    a = verify_qg_direct_contact_authority()
    assert a["pass"] and a["status"] == STATUS
    assert a["count_once"]["logical_records"] == 891992018
    for resolution, shape in (("K9_2_N8_b0.40", (1344, 1344)), ("K11_2_N10_b0.45", (2700, 2700)), ("K13_2_N12_b0.50", (4752, 4752))):
        m = direct_contact_sparse_matrix(resolution)
        assert m["shape"] == shape and m["nnz"] == m["pair_count"]
        assert m["data"].flags.writeable is False

def test_c111_pair_product_and_independent_zero_action():
    pair_id, resolution = next(iter(programs()))
    x = direct_contact_pair_entry(pair_id, resolution)
    assert x["unit"] == "GeV^2/g_s^2" and x["bound"] >= 0
    assert x["expanded_stream_written"] is False
    z = apply_direct_contact(resolution, np.zeros(1344 if resolution.startswith("K9") else 2700 if resolution.startswith("K11") else 4752, dtype=np.complex128))
    assert not np.any(z)

def test_c111_mutations_fail_closed():
    failures = 0
    pair_id, resolution = next(iter(programs()))
    for i in range(384):
        try:
            if i % 3 == 0: direct_contact_pair_entry(pair_id, "MUTATED")
            elif i % 3 == 1: direct_contact_sparse_matrix("MUTATED")
            else: direct_contact_entry(resolution, -1, 0)
        except (KeyError, ValueError, IndexError):
            failures += 1
    assert failures == 384
