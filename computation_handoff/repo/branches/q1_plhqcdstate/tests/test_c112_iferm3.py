import numpy as np
from deuteron_wigner.bridge.iferm3 import *

RES = (("K9_2_N8_b0.40", 1350), ("K11_2_N10_b0.45", 2706), ("K13_2_N12_b0.50", 4758))

def test_c112_direct_sum_authority():
    out = verify_bare_instantaneous_fermion_authority()
    assert out["pass"] and out["status"] == STATUS
    for r, dim in RES:
        m = bare_instantaneous_fermion_sparse_matrix(r)
        assert m["shape"] == (dim, dim)
        assert m["unit"] == "GeV^2/g_s^2"
        assert cross_sector_zero_certificate(r)["uncomputed"] is False

def test_c112_matrix_free_split_and_counterterm_typing():
    for r, dim in RES:
        z = apply_bare_instantaneous_fermion(r, np.zeros(dim, dtype=np.complex128))
        assert not np.any(z)
        assert counterterm_direction_manifest(r)["rows"][0]["zero_forbidden"] is True
        assert instantaneous_fermion_sector_manifest(r)["global_order"] == "q sector followed by qg sector"

def test_c112_mutations_fail_closed():
    failures = 0
    for i in range(384):
        try:
            if i % 3 == 0: bare_instantaneous_fermion_sparse_matrix("MUTATED")
            elif i % 3 == 1: cross_sector_zero_certificate("MUTATED")
            else: apply_bare_instantaneous_fermion("K9_2_N8_b0.40", np.zeros(6, dtype=np.complex128))
        except (KeyError, ValueError):
            failures += 1
    assert failures == 384
