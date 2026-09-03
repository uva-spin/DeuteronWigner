from deuteron_wigner.bridge.ifm2norm.core import symbolic_total_pplus, m2_kernel_record

def test_c109_focused_mutations_fail_closed():
    failures = 0
    for i in range(384):
        try:
            if i % 2:
                symbolic_total_pplus("MUTATED_K")
            else:
                m2_kernel_record("MUTATED_COORDINATE")
        except (KeyError, RuntimeError):
            failures += 1
    assert failures == 384
