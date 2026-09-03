#!/usr/bin/env python3
"""Export complete non-nucleonic transverse parent sensitivity members."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.canonical_parent_enrichment import NonNucleonicSector
from deuteron_wigner.correlator_io import (
    gluon_correlator_rows, quark_correlator_rows,
)
from deuteron_wigner.gluon_correlator import project_to_allowed_spin1_gluon_basis
from deuteron_wigner.nonnucleonic_transverse import NonNucleonicTransverseModel
from deuteron_wigner.quark_correlator import project_spin1_quark_correlator


OUT = Path("outputs/parent_tmds/wp12_nonnucleonic_transverse.csv")
MATRIX = OUT.with_suffix(".correlators.csv")
K = np.linspace(0.05, 1.0, 20)
X = (0.02, 0.05, 0.10, 0.20, 0.40)


def scale_quark(parent, factor):
    return type(parent)(
        factor*parent.vector, factor*parent.axial, factor*parent.transverse
    )


def main() -> None:
    model = NonNucleonicTransverseModel()
    tmd_rows, matrix_rows = [], []
    for sector in NonNucleonicSector:
        probability = model.ledger.probabilities[sector]
        for member in ("central", "sensitivity"):
            weight = (
                model.ledger.central_weight(sector)
                if member == "central" else probability
            )
            for x_n in X:
                for sign, link in ((1, "[+,+]"), (-1, "[-,-]")):
                    for k in K:
                        momentum = (float(k), 0.0)
                        for flavor in (2, 1, -2, -1):
                            parent = scale_quark(
                                model.quark_parent(
                                    sector, flavor, momentum, sign, x_n
                                ),
                                weight,
                            )
                            labels = {
                                "sector": sector.value, "species": (
                                    "quark" if flavor > 0 else "antiquark"
                                ), "flavor": flavor, "member": member,
                                "canonical_weight": weight, "gauge_link": link,
                                "color_structure": "", "x_N": x_n,
                                "Q_GeV": 5.0, "k_T_GeV": k,
                            }
                            projected = project_spin1_quark_correlator(
                                parent, momentum, model.deuteron_mass_gev
                            )
                            tmd_rows.extend({
                                **labels, "tmd": name, "F_GeV-2": value,
                            } for name, value in projected.items())
                            matrix_rows.extend(
                                quark_correlator_rows(parent, labels)
                            )
                        gluon = model.gluon_parent(
                            sector, momentum, sign, x_n
                        )
                        gluon = type(gluon)(weight*gluon.values)
                        labels = {
                            "sector": sector.value, "species": "gluon",
                            "flavor": 21, "member": member,
                            "canonical_weight": weight, "gauge_link": link,
                            "color_structure": "unresolved_sensitivity",
                            "x_N": x_n, "Q_GeV": 5.0, "k_T_GeV": k,
                        }
                        _, projected, residual = (
                            project_to_allowed_spin1_gluon_basis(
                                gluon.values, momentum,
                                model.deuteron_mass_gev
                            )
                        )
                        tmd_rows.extend({
                            **labels, "tmd": name, "F_GeV-2": value,
                            "basis_residual": residual,
                        } for name, value in projected.items())
                        matrix_rows.extend(
                            gluon_correlator_rows(gluon.values, labels)
                        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(tmd_rows).to_csv(OUT, index=False)
    pd.DataFrame(matrix_rows).to_csv(MATRIX, index=False)
    print(f"{OUT}: {len(tmd_rows)} rows; {MATRIX}: {len(matrix_rows)} rows")


if __name__ == "__main__":
    main()
