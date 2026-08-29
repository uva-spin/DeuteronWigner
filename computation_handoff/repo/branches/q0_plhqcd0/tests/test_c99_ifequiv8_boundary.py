"""C99 may consume historical authority only through C98's three methods."""
import inspect

import deuteron_wigner.bridge.ifhistpublic2 as c98
from deuteron_wigner.bridge.ifequiv6.core import compile_descendant_programs


def test_c99_cannot_enumerate_historical_primitive_identities_from_c98():
    assert c98.__all__ == (
        "historical_pair_normal_form",
        "historical_pair_proof_inputs",
        "historical_primitive_record",
    )
    assert str(inspect.signature(c98.historical_primitive_record)) == "(family_id: 'str', record_id: 'str') -> 'Any'"
    assert not [name for name in c98.__all__ if "family" in name or "page" in name or "list" in name or "enumer" in name]
    # The current-only side can nevertheless produce its complete canonical
    # pair identity without an historical API call.
    program = next(compile_descendant_programs("K9_2_N8_b0.40"))
    assert program["pair"]["id"]
