import numpy as np

from deuteron_wigner.nonnucleonic_transverse import (
    GLUON_NAMES,
    NonNucleonicTransverseModel,
    default_nonnucleonic_ledger,
)
from deuteron_wigner.canonical_parent_enrichment import NonNucleonicSector
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES, project_spin1_quark_correlator,
)
from deuteron_wigner.gluon_correlator import (
    project_to_allowed_spin1_gluon_basis,
)


def test_all_nonnucleonic_sectors_have_complete_positive_parents():
    model = NonNucleonicTransverseModel()
    for sector in NonNucleonicSector:
        for flavor in (2, 1, -2, -1):
            parent = model.quark_parent(sector, flavor, (0.3, 0.1), 1)
            assert parent.minimum_positivity_eigenvalue() >= -1e-12
            values = project_spin1_quark_correlator(
                parent, (0.3, 0.1), model.deuteron_mass_gev
            )
            assert set(values) == set(SPIN1_QUARK_TMD_NAMES)
        gluon = model.gluon_parent(sector, (0.3, 0.1), 1)
        assert gluon.minimum_positivity_eigenvalue() >= -1e-12
        _, values, residual = project_to_allowed_spin1_gluon_basis(
            gluon.values, (0.3, 0.1), model.deuteron_mass_gev
        )
        assert set(values) == set(GLUON_NAMES)
        assert residual < 1e-8


def test_nonnucleonic_link_reversal_and_central_policy():
    model = NonNucleonicTransverseModel()
    for sector in NonNucleonicSector:
        future = model.quark_tmds(sector, 2, 0.3, 1)
        past = model.quark_tmds(sector, 2, 0.3, -1)
        for name, value in future.items():
            expected = -past[name] if name in {
                "h1perp", "f1Tperp", "h1LLperp", "g1LT", "h1LT",
                "h1LTperp", "g1TT", "h1TT", "h1TTperp",
            } else past[name]
            assert value == expected
    ledger = default_nonnucleonic_ledger()
    assert ledger.central_weight(NonNucleonicSector.NNPI) == 0
    assert ledger.central_weight(NonNucleonicSector.DELTADELTA) == 0
    assert ledger.central_weight(NonNucleonicSector.HIDDEN_COLOR) == 0
    assert ledger.central_weight(NonNucleonicSector.SRC) == 0
