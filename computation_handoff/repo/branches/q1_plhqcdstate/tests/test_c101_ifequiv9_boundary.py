"""C101 must fail closed when no public theorem checker is exported."""
import deuteron_wigner.bridge.ifhistpublic2 as c98
import deuteron_wigner.bridge.ifprimenum as c100
from deuteron_wigner.bridge.ifequiv6.core import compile_descendant_programs

def test_c101_public_surface_has_inputs_but_no_factorized_theorem_checker():
    assert c98.__all__ == ("historical_pair_normal_form", "historical_pair_proof_inputs", "historical_primitive_record")
    assert c100.__all__ == ("historical_primitive_domain_manifest", "historical_primitive_record_page")
    public_names = set(c98.__all__) | set(c100.__all__)
    assert not {"verify_factorized_expansion_equivalence", "factorized_semantic_checker", "check_historical_expansion_equivalence"}.intersection(public_names)
    # The current side remains independently available before historical input.
    assert next(compile_descendant_programs("K9_2_N8_b0.40"))["normal_form"] == "C90-NORMAL-FORM-V1"
