from deuteron_wigner.bridge.ifboundstream.core import factorized_census, iterate_pair_programs, rank_pair_leaf, unrank_pair_leaf, unrank_pair_record


def test_c89_factorized_census_reproduces_c88_domain_exactly():
    census = factorized_census()
    assert census["supported_pairs"] == 154830
    assert census["logical_records"] == 891992018
    assert [row["logical_records"] for row in census["resolution_rows"]] == [28606464, 165991250, 697394304]


def test_c89_rank_unrank_closes_at_factorized_boundaries():
    program = next(iterate_pair_programs("K9_2_N8_b0.40"))
    for ordinal in (0, 1, program.logical_count - 1):
        leaf = unrank_pair_leaf(program, ordinal)
        assert rank_pair_leaf(program, leaf) == ordinal


def test_c89_reconstructs_one_complete_c88_record_without_kernel_value():
    program = next(iterate_pair_programs("K9_2_N8_b0.40"))
    record = unrank_pair_record(program, 0)
    assert record["canonical_record_id"].startswith("C88:REC:")
    assert record["contains_no_C80_kernel_value"]
    assert record["contains_no_coefficient_times_kernel_product"]
